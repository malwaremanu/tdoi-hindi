#!/usr/bin/env python3
"""Prepare an episode's narration for TTS: script -> cleaned Roman-Hindi text file.

  python3 tools/audio/prep_narration.py --script "scripts/Ep 4.1 ... — Script.md" \
      --workdir ep04_1 [--first-chunk-words 340] [--words 1300]

- takes everything from `## Cold open` up to `## Sources`
- drops production cues: lines that are only [ ... ] and inline [SFX: ...] spans
- drops markdown headings, bold/italic markers and links
- writes <workdir>/narration_rom.txt + <workdir>/chunks.plan.txt (chunk sizes)
"""
from __future__ import annotations

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_episode import extract_narration, split_chunks  # noqa: E402


def clean(text: str) -> str:
    out = []
    for line in text.split("\n"):
        s = line.strip()
        if not s:
            out.append("")
            continue
        if re.fullmatch(r"[\[\(].*[\]\)]", s):          # pure production cue line
            continue
        s = re.sub(r"\[[^\]]*\]", "", s)                # inline cues
        s = re.sub(r"\{[^}]*\}", "", s)
        s = re.sub(r"\*\*|\*|__", "", s)
        s = re.sub(r"\s{2,}", " ", s).strip()
        if s:
            out.append(s)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", required=True)
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--first-chunk-words", type=int, default=0)
    ap.add_argument("--words", type=int, default=1300)
    args = ap.parse_args()

    raw = extract_narration(args.script)
    text = clean(raw)
    os.makedirs(args.workdir, exist_ok=True)
    rom = os.path.join(args.workdir, "narration_rom.txt")
    open(rom, "w", encoding="utf-8").write(text + "\n")

    if args.first_chunk_words:
        head, cur, n = "", [], 0
        for para in text.split("\n\n"):
            w = len(para.split())
            if cur and n + w > args.first_chunk_words:
                break
            cur.append(para)
            n += w
        head = "\n\n".join(cur).strip()
        rest = text[len(head):].strip()
        chunks = [head] + split_chunks(rest, args.words)
    else:
        chunks = split_chunks(text, args.words)

    plan = [len(c.split()) for c in chunks]
    open(os.path.join(args.workdir, "chunks.plan.txt"), "w").write(
        f"{len(chunks)} chunks, {sum(plan)} words\n" + "\n".join(f"c{i+1:02d}: {w} words" for i, w in enumerate(plan)))
    print(f"{args.workdir}: {len(chunks)} chunks, {sum(plan)} words, "
          f"~{sum(plan)/160:.0f} min audio", flush=True)
    for i, w in enumerate(plan, 1):
        print(f"  c{i:02d}: {w} words", flush=True)
    print("wrote", rom, flush=True)


if __name__ == "__main__":
    main()
