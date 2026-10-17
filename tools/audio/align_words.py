#!/usr/bin/env python3
"""Forced-ish alignment: give every source word of a take a timestamp.

Whisper's Hindi transcript of a take is imperfect, so the ASR word list cannot be
matched one-to-one. This does a banded DP alignment between the *known* source words
and the ASR words (score = consonant-skeleton similarity, gaps allowed, monotonic),
then reads each source word's time off its aligned ASR word; source words inside an
ASR gap inherit an interpolated time. That makes phrase anchors reliable: an SFX plan
can say "the thud lands on the third 'फिर तीसरी'" and the mixer finds that word's audio
time exactly.

  <whisper-venv>/bin/python3 tools/audio/align_words.py --workdir ep04_1 \\
      --chunks c01,c02 [--model large-v3] [--band 40]

Writes <workdir>/<chunk>.align.json: [{"w","s","e","asr"}]  (asr = aligned ASR word)
"""
from __future__ import annotations

import argparse
import difflib
import glob
import json
import os
import re
import subprocess
import unicodedata

import numpy as np

FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
SR = 16000


def skel(w: str) -> str:
    w = unicodedata.normalize("NFC", w).lower()
    w = re.sub(r"[^\w\u0900-\u097F]", "", w).replace("ँ", "ं")
    return re.sub(r"[\u093E-\u094D\u0901\u0902]", "", w)


def sim(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def pick_model(name):
    from faster_whisper import WhisperModel
    import ctranslate2
    if ctranslate2.get_cuda_device_count() > 0:
        for ct in ("float16", "int8_float16"):
            try:
                m = WhisperModel(name, device="cuda", compute_type=ct)
                print(f"model {name} on GPU ({ct})", flush=True)
                return m
            except Exception as exc:  # noqa: BLE001
                print(f"cuda/{ct} unavailable: {str(exc)[:120]}", flush=True)
    print(f"model {name} on CPU", flush=True)
    return WhisperModel(name, device="cpu", compute_type="int8")


def decode(path):
    raw = path + ".s16"
    subprocess.run([FF, "-y", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "s16le", raw],
                   check=True, capture_output=True)
    x = np.fromfile(raw, dtype=np.int16).astype(np.float32) / 32768.0
    os.remove(raw)
    return x


def asr_words(model, path, window=60.0, hop=55.0):
    x = decode(path)
    total = len(x) / SR
    out, t = [], 0.0
    while t < total:
        dur = min(window, total - t)
        if dur < 1.5:
            break
        segs, _ = model.transcribe(x[int(t * SR):int((t + dur) * SR)], language="hi",
                                   word_timestamps=True, vad_filter=False, beam_size=5)
        for s in segs:
            for w in (s.words or []):
                if w.word.strip():
                    out.append((w.word.strip(), w.start + t, w.end + t))
        t += hop
    out.sort(key=lambda r: r[1])
    return out


def align(src, heard, band=40):
    """Banded Needleman-Wunsch on skeletons; returns per-source-word ASR index or -1."""
    A = [skel(w) for w in src]
    B = [skel(w) for w in heard]
    n, m = len(A), len(B)
    NEG = -1e9
    score = np.full((n + 1, m + 1), NEG, dtype=np.float64)
    ptr = np.zeros((n + 1, m + 1), dtype=np.int8)      # 0 diag, 1 up(skip src), 2 left(skip asr)
    score[0, :] = -0.35 * np.arange(m + 1)
    score[:, 0] = -0.35 * np.arange(n + 1)
    ptr[0, 1:] = 2
    ptr[1:, 0] = 1
    for i in range(1, n + 1):
        j0 = max(1, int(i * m / max(1, n)) - band)
        j1 = min(m, int(i * m / max(1, n)) + band)
        for j in range(j0, j1 + 1):
            d = score[i - 1, j - 1] + (sim(A[i - 1], B[j - 1]) - 0.5) * 2
            u = score[i - 1, j] - 0.35
            l = score[i, j - 1] - 0.35
            if d >= u and d >= l:
                score[i, j], ptr[i, j] = d, 0
            elif u >= l:
                score[i, j], ptr[i, j] = u, 1
            else:
                score[i, j], ptr[i, j] = l, 2
    i, j = n, m
    mapw = [-1] * n
    while i > 0 or j > 0:
        p = ptr[i, j]
        if i > 0 and j > 0 and p == 0:
            mapw[i - 1] = j - 1
            i, j = i - 1, j - 1
        elif i > 0 and (j == 0 or p == 1):
            mapw[i - 1] = -1
            i -= 1
        else:
            j -= 1
    return mapw


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--chunks", required=True)
    ap.add_argument("--model", default="large-v3")
    ap.add_argument("--band", type=int, default=40)
    args = ap.parse_args()

    model = pick_model(args.model)
    for ch in [c.strip() for c in args.chunks.split(",") if c.strip()]:
        wav = os.path.join(args.workdir, ch + ".wav")
        txt = os.path.join(args.workdir, ch + ".txt")
        heard = asr_words(model, wav)
        src = [w for w in open(txt, encoding="utf-8").read().split() if skel(w)]
        heard_k = [w for w, _, _ in heard if skel(w)]
        times = [(s, e) for w, s, e in heard if skel(w)]
        mapw = align(src, heard_k, args.band)
        out, last_end = [], 0.0
        for k, (word, mi) in enumerate(zip(src, mapw)):
            if mi >= 0:
                s, e = times[mi]
                last_end = e if e > last_end else last_end
            else:
                s, e = last_end, last_end        # placeholder; filled by interpolation below
            out.append({"w": word, "s": round(s, 3), "e": round(e, 3), "asr": mi >= 0})
        # interpolate unaligned words between their aligned neighbours
        for k, rec in enumerate(out):
            if rec["asr"]:
                continue
            prev = next((out[i] for i in range(k - 1, -1, -1) if out[i]["asr"]), None)
            nxt = next((out[i] for i in range(k + 1, len(out)) if out[i]["asr"]), None)
            if prev and nxt and nxt["s"] > prev["e"]:
                span = nxt["s"] - prev["e"]
                total_missing = sum(1 for i in range(k, len(out))
                                    if not out[i]["asr"] and out[i]["s"] <= nxt["s"])
                step = span / max(1, total_missing + 1)
                rank = sum(1 for i in range(list(out).index(prev) + 1, k + 1)
                           if not out[i]["asr"])
                rec["s"] = round(prev["e"] + step * rank, 3)
                rec["e"] = round(rec["s"] + max(0.05, step * 0.7), 3)
            elif prev:
                rec["s"] = round(prev["e"] + 0.05, 3)
                rec["e"] = round(rec["s"] + 0.15, 3)
            else:
                rec["s"], rec["e"] = 0.05, 0.2
        p = os.path.join(args.workdir, ch + ".align.json")
        json.dump(out, open(p, "w"), ensure_ascii=False)
        aligned = sum(1 for r in out if r["asr"])
        print(f"{ch}: {len(src)} source words, {aligned} aligned directly "
              f"({100.0 * aligned / max(1, len(src)):.1f}%) -> {p}", flush=True)


if __name__ == "__main__":
    main()
