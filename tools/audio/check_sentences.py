#!/usr/bin/env python3
"""Sentence-level presence audit of a take against its source text.

Sequential word matching drifts as soon as the transcript inserts or merges a word,
which fakes "missing" runs inside perfectly good audio. This audit is drift-proof:
every source sentence is looked for **anywhere** in the transcript, compared on a
consonant skeleton (so the ASR's spelling errors do not count), and only sentences
that find no good match anywhere are reported.

  python3 tools/audio/check_sentences.py --workdir ep04_1 --chunks c01,c02,c03,c04,c05
                                        [--transcript-suffix .gemini.txt] [--threshold 0.75]

Uses the cached transcript of the previous step, so it costs nothing to re-run.
"""
from __future__ import annotations

import argparse
import difflib
import os
import re
import unicodedata


def skel(s: str) -> str:
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"[^\w\s\u0900-\u097F]", " ", s).replace("ँ", "ं")
    s = re.sub(r"[\u093E-\u094D\u0901\u0902]", "", s)
    return re.sub(r"\s+", "", s)


def sentences(text: str, max_words: int = 22):
    """Paragraphs, split further on danda/./?/! so one long paragraph can still be
    pinpointed; keeps every fragment >= 3 words."""
    out = []
    for para in [p.strip() for p in text.split("\n\n") if p.strip()]:
        parts = [p.strip() for p in re.split(r"(?<=[।?!.])\s+", para) if p.strip()]
        buf = ""
        for p in parts:
            if len(buf.split()) + len(p.split()) <= max_words:
                buf = (buf + " " + p).strip()
            else:
                if buf:
                    out.append(buf)
                buf = p
        if buf:
            out.append(buf)
    return [s for s in out if len(s.split()) >= 3]


def best_match(needle: str, hay: str, step: int) -> tuple[float, int]:
    if not needle or not hay:
        return 0.0, -1
    L = len(needle)
    if L >= len(hay):
        return difflib.SequenceMatcher(None, needle, hay, autojunk=False).ratio(), 0
    best, at = 0.0, -1
    for st in range(0, len(hay) - L + 1, step):
        r = difflib.SequenceMatcher(None, needle, hay[st:st + L], autojunk=False).ratio()
        if r > best:
            best, at = r, st
            if best > 0.97:
                break
    return best, at


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--chunks", required=True)
    ap.add_argument("--transcript-suffix", default=".gemini.txt")
    ap.add_argument("--threshold", type=float, default=0.75)
    args = ap.parse_args()

    total_flagged = 0
    total_sentences = 0
    for ch in [c.strip() for c in args.chunks.split(",") if c.strip()]:
        txt = os.path.join(args.workdir, ch + ".txt")
        tr = os.path.join(args.workdir, ch + args.transcript_suffix)
        if not (os.path.exists(txt) and os.path.exists(tr)):
            print(f"{ch}: missing inputs", flush=True)
            continue
        source = open(txt, encoding="utf-8").read()
        heard = open(tr, encoding="utf-8").read()
        hay = skel(heard)
        sents = sentences(source)
        flagged = []
        for s in sents:
            n = skel(s)
            step = max(8, len(n) // 3)
            r, _ = best_match(n, hay, step)
            if r < args.threshold:
                flagged.append((round(r, 2), s))
        total_flagged += len(flagged)
        total_sentences += len(sents)
        print(f"{ch}: {len(sents)} sentences | below {args.threshold}: {len(flagged)}", flush=True)
        for r, s in flagged:
            print(f"   {r:.2f}  {s[:120]}", flush=True)
    print(f"\nTOTAL: {total_flagged}/{total_sentences} sentences below threshold", flush=True)


if __name__ == "__main__":
    main()
