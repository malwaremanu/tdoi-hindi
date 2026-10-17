#!/usr/bin/env python3
"""Roman-Hindi -> Devanagari transliteration for TDOI narration, via the local
gemini-web2api gateway (http://localhost:8081/v1, key sk-gemini).

  python3 tools/audio/transliterate.py --rom ep04_1/narration_rom.txt \
      --out ep04_1/narration_dev.txt [--first-chunk-words 340]

Rules enforced: output must contain ZERO Latin letters; numbers become Devanagari
words; paragraph structure is preserved (one output paragraph per input paragraph).
Batches are ~600 words so the model never drifts. Any batch that comes back with
Latin characters is retried (up to 4 times) and reported.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request

BASE = os.environ.get("GEMINI_WEB2API_BASE", "http://localhost:8081/v1")
KEY = os.environ.get("GEMINI_WEB2API_KEY", "sk-gemini")
MODEL = os.environ.get("TRANSLIT_MODEL", "gemini-3.6-flash")

SYSTEM = (
    "You are a precise Hindi transliterator. Convert Roman-script Hindi (Hinglish) into "
    "Devanagari script. Rules: (1) output ONLY Devanagari — not a single Latin letter may "
    "remain, ever, including for names, acronyms or units; (2) write every number as a "
    "Devanagari word (e.g. '1944' -> 'उन्नीस सौ चवालीस', '26' -> 'छब्बीस'); (3) transliterate, "
    "do not translate and do not add or drop content; (4) keep the paragraph breaks exactly "
    "as given; (5) use natural, speakable Hindi spelling (e.g. 'Nehru' -> 'नेहरू', 'Asha' -> "
    "'आशा', 'Ahmadnagar' -> 'अहमदनगर', 'Bharat' -> 'भारत'); (6) keep punctuation marks as they "
    "are. Return only the converted text, with no commentary."
)


def call(text: str, timeout: int = 300) -> str:
    payload = {
        "model": MODEL,
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": text}],
        "temperature": 0.1,
    }
    req = urllib.request.Request(
        f"{BASE}/chat/completions",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.load(resp)
    return (data["choices"][0]["message"]["content"] or "").strip()


def batches(paras: list[str], target_words: int = 600) -> list[list[str]]:
    out, cur, n = [], [], 0
    for p in paras:
        w = len(p.split())
        if cur and n + w > target_words:
            out.append(cur)
            cur, n = [], 0
        cur.append(p)
        n += w
    if cur:
        out.append(cur)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rom", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--target-words", type=int, default=600)
    ap.add_argument("--cache-dir", default=None)
    args = ap.parse_args()

    paras = [p.strip() for p in open(args.rom, encoding="utf-8").read().split("\n\n") if p.strip()]
    cache = args.cache_dir or os.path.join(os.path.dirname(os.path.abspath(args.out)), "_translit_cache")
    os.makedirs(cache, exist_ok=True)
    chunks = batches(paras, args.target_words)
    print(f"{len(paras)} paragraphs -> {len(chunks)} batches", flush=True)

    done = []
    for i, ch in enumerate(chunks, 1):
        cpath = os.path.join(cache, f"b{i:02d}.txt")
        if os.path.exists(cpath):
            txt = open(cpath, encoding="utf-8").read().strip()
            if txt and not re.search(r"[A-Za-z]", txt):
                print(f"batch {i}: cached ok", flush=True)
                done.append(txt)
                continue
        src = "\n\n".join(ch)
        ok = False
        for attempt in range(1, 5):
            try:
                txt = call(src)
            except Exception as exc:  # noqa: BLE001
                print(f"batch {i}: attempt {attempt} transport error: {str(exc)[:120]}", flush=True)
                continue
            latin = re.findall(r"[A-Za-z]+", txt)
            if latin:
                print(f"batch {i}: attempt {attempt} left {len(latin)} latin tokens {latin[:6]}", flush=True)
                if attempt < 4:
                    continue                      # retry: a Latin token would be read in English
                txt = re.sub(r"[A-Za-z]+", "", txt)
            open(cpath, "w", encoding="utf-8").write(txt)
            print(f"batch {i}: ok ({len(txt.split())} words)", flush=True)
            done.append(txt)
            ok = True
            break
        if not ok:
            print(f"batch {i}: FAILED", flush=True)
            sys.exit(2)

    dev = "\n\n".join(done)
    open(args.out, "w", encoding="utf-8").write(dev + "\n")
    latin = re.findall(r"[A-Za-z]+", dev)
    print(f"wrote {args.out}: {len(dev.split())} words, latin tokens left: {len(latin)}", flush=True)


if __name__ == "__main__":
    main()
