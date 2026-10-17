#!/usr/bin/env python3
"""Take-vs-text fidelity QC that survives a weak ASR pass.

Why it is built this way
  A single long transcription pass drops passages (whisper skipped ~9 s of a correct
  Ep 4.1 cold open) and mangles Hindi spelling, so "words not in the transcript" is
  not evidence of a bad take. This tool instead:

  1. transcribes the chunk in overlapping windows (default 60 s / 55 s hop) with
     `vad_filter=False` and unions the words — an overlapping pass recovers most of
     what a long pass skips;
  2. aligns every source word to that union with a consonant-skeleton fuzzy match
     (Ratio >= 0.72, searched around the previous hit) so the ASR's spelling errors
     ("रेत"→"रेट", "लगता"→"लकता") do not count as misses;
  3. reports runs of 4+ consecutive unmatched source words, and for each run measures
     the audio itself: **silence** there means the take really dropped the words,
     **speech** there means the ASR failed and the words are almost certainly spoken.

  <whisper-venv>/bin/python3 tools/audio/qc_take.py --workdir ep04_1 \
      --chunks c01,c02,c03,c04,c05 [--model large-v3] [--window 60] [--hop 55]

GPU: install nvidia-cublas-cu12 + nvidia-cudnn-cu12 into the venv and export
LD_LIBRARY_PATH to the venv's nvidia/*/lib dirs in the shell BEFORE launching python
(in-process it is too late — ctranslate2 dlopens lazily).
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


def norm(w: str) -> str:
    w = unicodedata.normalize("NFC", w).lower()
    w = re.sub(r"[^\w\u0900-\u097F]", "", w).replace("ँ", "ं")
    return w


def skel(w: str) -> str:
    return re.sub(r"[\u093E-\u094D\u0901\u0902]", "", norm(w))


def ratio(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def pick_model(name: str, want_gpu: bool = True):
    from faster_whisper import WhisperModel
    import ctranslate2
    if want_gpu and ctranslate2.get_cuda_device_count() > 0:
        for ct in ("float16", "int8_float16"):
            try:
                m = WhisperModel(name, device="cuda", compute_type=ct)
                print(f"model {name} on GPU ({ct})", flush=True)
                return m
            except Exception as exc:  # noqa: BLE001
                print(f"cuda/{ct} unavailable: {str(exc)[:140]}", flush=True)
    m = WhisperModel(name, device="cpu", compute_type="int8")
    print(f"model {name} on CPU (int8)", flush=True)
    return m


def decode(path, offset=None, duration=None):
    tmp = path
    if duration is not None:
        tmp = f"{path}.win.wav"
        subprocess.run([FF, "-y", "-ss", str(offset), "-t", str(duration), "-i", path,
                        "-ac", "1", "-ar", str(SR), tmp], check=True, capture_output=True)
    raw = tmp + ".s16"
    subprocess.run([FF, "-y", "-i", tmp, "-ac", "1", "-ar", str(SR), "-f", "s16le", raw],
                   check=True, capture_output=True)
    x = np.fromfile(raw, dtype=np.int16).astype(np.float32) / 32768.0
    os.remove(raw)
    if tmp != path:
        os.remove(tmp)
    return x


def transcribe(model, audio, offset=0.0, vad=False):
    segs, _ = model.transcribe(audio, language="hi", word_timestamps=True,
                               vad_filter=vad, beam_size=5)
    out = []
    for s in segs:
        for w in (s.words or []):
            if w.word.strip():
                out.append((w.word.strip(), w.start + offset, w.end + offset))
    return out


def union_pass(model, wav, win_s, hop_s):
    x = decode(wav)
    total = len(x) / SR
    words = []
    t = 0.0
    while t < total:
        dur = min(win_s, total - t)
        if dur < 1.5:
            break
        seg = x[int(t * SR):int((t + dur) * SR)]
        got = transcribe(model, seg, offset=t, vad=False)
        words += got
        print(f"    window {t:7.1f}-{t + dur:7.1f}s  {len(got):4d} words", flush=True)
        t += hop_s
    words.sort(key=lambda w: w[1])
    return words


def speech_rms(x, a, b):
    s = slice(max(0, int(a * SR)), min(len(x), int(b * SR)))
    seg = x[s]
    if len(seg) == 0:
        return -120.0
    return 20 * np.log10(max(1e-9, float(np.sqrt(np.mean(seg ** 2)))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--chunks", required=True)
    ap.add_argument("--model", default="large-v3")
    ap.add_argument("--window", type=float, default=60.0)
    ap.add_argument("--hop", type=float, default=55.0)
    ap.add_argument("--min-run", type=int, default=4)
    ap.add_argument("--cpu", action="store_true")
    args = ap.parse_args()

    model = pick_model(args.model, want_gpu=not args.cpu)
    dropped_total = 0
    unresolved_total = 0

    for ch in [c.strip() for c in args.chunks.split(",") if c.strip()]:
        wav = os.path.join(args.workdir, ch + ".wav")
        txt = os.path.join(args.workdir, ch + ".txt")
        if not (os.path.exists(wav) and os.path.exists(txt)):
            print(f"{ch}: missing inputs", flush=True)
            continue
        audio = decode(wav)
        print(f"\n=== {ch} ({len(audio) / SR:.1f}s) ===", flush=True)
        words = union_pass(model, wav, args.window, args.hop)
        json.dump([{"w": w, "s": round(s, 2), "e": round(e, 2)} for w, s, e in words],
                  open(os.path.join(args.workdir, ch + ".asr.json"), "w"), ensure_ascii=False)

        H = [(skel(w), s, e) for w, s, e in words if skel(w)]
        src = [w for w in open(txt, encoding="utf-8").read().split() if skel(w)]
        match, pos = [], 0
        for s in src:
            sk = skel(s)
            best, bj = 0.0, None
            for j in range(max(0, pos - 8), min(len(H), pos + 20)):
                r = ratio(sk, H[j][0])
                if r > best:
                    best, bj = r, j
            if best >= 0.72:
                pos = bj + 1
                match.append(bj)
            else:
                match.append(None)

        runs, cur = [], []
        for k, m in enumerate(match):
            if m is None:
                cur.append(k)
            else:
                if len(cur) >= args.min_run:
                    runs.append(cur)
                cur = []
        if len(cur) >= args.min_run:
            runs.append(cur)

        matched = sum(1 for m in match if m is not None)
        print(f"{ch}: source {len(src)} | union {len(H)} | matched {matched} "
              f"({100.0 * matched / max(1, len(src)):.1f}%) | runs: {len(runs)}", flush=True)
        for r in runs:
            a, b = r[0], r[-1]
            prev = next((match[k] for k in range(a - 1, -1, -1) if match[k] is not None), None)
            nxt = next((match[k] for k in range(b + 1, len(match)) if match[k] is not None), None)
            t0 = H[prev][2] if prev is not None else 0.0
            t1 = H[nxt][1] if nxt is not None else t0 + 12.0
            rms = speech_rms(audio, t0 + 0.1, max(t1, t0 + 0.6))
            verdict = "DROPPED (no speech there)" if rms < -45 else "UNRESOLVED (speech present)"
            if rms < -45:
                dropped_total += 1
            else:
                unresolved_total += 1
            print(f"   {t0:7.2f}-{t1:7.2f}s rms {rms:6.1f} dBFS  {verdict}: "
                  f"{' '.join(src[a:b + 1])[:80]}", flush=True)

    print(f"\nTOTAL: {dropped_total} dropped, {unresolved_total} unresolved", flush=True)


if __name__ == "__main__":
    main()
