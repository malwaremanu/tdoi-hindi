#!/usr/bin/env python3
"""Take-vs-text fidelity QC using an LLM audio call (house method).

Whisper's Devanagari is too unstable for string similarity, so the take is
re-transcribed by a multimodal LLM (same key pool as the TTS, separate quota) and
compared with the source text: exact-token similarity plus a consonant-skeleton
fuzzy alignment for word-level recall and candidate drops.

  python3 tools/audio/verify_gemini.py --workdir ep04_1 --chunks c01,c02,c03,c04,c05
                                      [--model gemini-2.5-flash] [--bitrate 32k]

Writes <workdir>/<chunk>.gemini.txt, prints per chunk:
  source tokens | transcript tokens | similarity | recall | candidate drop runs
"""
from __future__ import annotations

import argparse
import base64
import difflib
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_episode import pick_key  # noqa: E402  (same key pool, TTS-usage ordered)

# LLM audio calls are a different quota from TTS, so they are counted in their own
# file: spending the TTS budget on QC would cost real episode takes.
LLM_POOL = os.path.expanduser("~/.hermes/keys/gemini_llm_pool.json")


def llm_mark(key: str, status: int):
    today = time.strftime("%Y-%m-%d")
    try:
        data = json.load(open(LLM_POOL))
    except Exception:  # noqa: BLE001
        data = {}
    if data.get("day") != today:
        data = {"day": today, "keys": {}}
    rec = data["keys"].setdefault(key[-6:], {"used_today": 0, "exhausted_today": False})
    rec["used_today"] += 1
    rec["last_used"] = time.strftime("%Y-%m-%d %H:%M:%S")
    if status in (429, 403):
        rec["exhausted_today"] = True
    tmp = LLM_POOL + ".tmp"
    json.dump(data, open(tmp, "w"), indent=1)
    os.replace(tmp, LLM_POOL)

FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
HOST = "generativelanguage.googleapis.com"
PROMPT = ("Transcribe this Hindi audio verbatim. Return only the transcript text in "
          "Devanagari script, exactly as spoken, with no commentary, no timestamps and "
          "no headings.")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"[^\w\s\u0900-\u097F]", " ", s).replace("ँ", "ं")
    return re.sub(r"\s+", " ", s).strip()


def skel(w: str) -> str:
    return re.sub(r"[\u093E-\u094D\u0901\u0902]", "", re.sub(r"\W", "", w))


def ratio(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio() if a and b else 0.0


def to_mp3(wav: str, out: str, bitrate: str):
    subprocess.run([FF, "-y", "-i", wav, "-ac", "1", "-ar", "16000", "-b:a", bitrate, out],
                   check=True, capture_output=True)


def transcribe(mp3: str, model: str, timeout: int = 600) -> str:
    b64 = base64.b64encode(open(mp3, "rb").read()).decode()
    payload = {"contents": [{"parts": [{"text": PROMPT},
                                       {"inline_data": {"mime_type": "audio/mp3", "data": b64}}]}]}
    key = pick_key()
    if not key:
        raise RuntimeError("every key in the pool is spent for today")
    req = urllib.request.Request(
        f"https://{HOST}/v1beta/models/{model}:generateContent",
        data=json.dumps(payload).encode(),
        headers={"x-goog-api-key": key, "Content-Type": "application/json"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        llm_mark(key, e.code)
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:300]}") from None
    llm_mark(key, 200)
    cand = data.get("candidates") or []
    if not cand:
        raise RuntimeError("no candidates: " + json.dumps(data)[:300])
    parts = (cand[0].get("content") or {}).get("parts") or []
    return " ".join(p.get("text", "") for p in parts).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--chunks", required=True)
    ap.add_argument("--model", default="gemini-2.5-flash")
    ap.add_argument("--bitrate", default="32k")
    ap.add_argument("--min-run", type=int, default=4)
    args = ap.parse_args()

    tmp = os.path.join(args.workdir, "_asr")
    os.makedirs(tmp, exist_ok=True)
    for ch in [c.strip() for c in args.chunks.split(",") if c.strip()]:
        wav = os.path.join(args.workdir, ch + ".wav")
        txt = os.path.join(args.workdir, ch + ".txt")
        if not (os.path.exists(wav) and os.path.exists(txt)):
            print(f"{ch}: missing inputs", flush=True)
            continue
        out_txt = os.path.join(args.workdir, ch + ".gemini.txt")
        mp3 = os.path.join(tmp, ch + ".mp3")
        if os.path.exists(out_txt) and os.path.getsize(out_txt) > 50:
            heard = open(out_txt, encoding="utf-8").read()
            print(f"{ch}: cached transcript", flush=True)
        else:
            to_mp3(wav, mp3, args.bitrate)
            t0 = time.time()
            heard = transcribe(mp3, args.model)
            open(out_txt, "w", encoding="utf-8").write(heard + "\n")
            os.remove(mp3)
            print(f"{ch}: transcribed in {time.time() - t0:.0f}s "
                  f"({os.path.getsize(out_txt)} bytes)", flush=True)

        src_words = open(txt, encoding="utf-8").read().split()
        heard_words = heard.split()
        a = [w for w in norm(" ".join(src_words)).split() if w]
        b = [w for w in norm(heard).split() if w]
        sa, sb = set(a), set(b)
        sim = (2 * len(sa & sb)) / (len(sa) + len(sb)) if (sa or sb) else 0.0

        H = [skel(w) for w in heard_words]
        S = [w for w in src_words if skel(w)]
        match, pos, matched = [], 0, 0
        for s in S:
            sk = skel(s)
            best, bj = 0.0, None
            for j in range(max(0, pos - 8), min(len(H), pos + 20)):
                r = ratio(sk, H[j])
                if r > best:
                    best, bj = r, j
            if best >= 0.72:
                pos = bj + 1
                matched += 1
                match.append(1)
            else:
                match.append(0)
        runs, cur = [], []
        for k, m in enumerate(match):
            if not m:
                cur.append(k)
            else:
                if len(cur) >= args.min_run:
                    runs.append(cur)
                cur = []
        if len(cur) >= args.min_run:
            runs.append(cur)

        print(f"{ch}: source {len(a)} tokens | transcript {len(b)} | similarity {sim:.3f} | "
              f"word recall {100.0 * matched / max(1, len(S)):.1f}% | runs: {len(runs)}", flush=True)
        for r in runs:
            print(f"   drop? {' '.join(S[r[0]:r[-1] + 1])[:110]}", flush=True)


if __name__ == "__main__":
    main()
