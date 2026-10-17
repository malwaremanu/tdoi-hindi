#!/usr/bin/env python3
"""Rebuild book chapter files from the Internet Archive full text (much more complete
than the repo's current book/the-discovery-of-india.txt).

- input : /tmp/ia_tdoi_raw.txt  (https://archive.org/download/TheDiscoveryOfIndia-Eng-JawaharlalNehru/discovery-of-india_djvu.txt)
- ref   : book/toc.json (chapter + section titles)
- output: book/chapters_v2/chNN.txt  (same "# chapter / ## section" shape as book/chapters/)
- report: book/chapters_v2/_report.json  (+ human summary on stdout)

Usage: python3 tools/book/rebuild_chapters_ia.py [--write]
"""
from __future__ import annotations

import json
import os
import re
import sys

ROOT = "/home/itcell/audiobooks/tdoi"
IA = "/tmp/ia_tdoi_raw.txt"
TOC = f"{ROOT}/book/toc.json"
OLD = f"{ROOT}/book/chapters"
OUT = f"{ROOT}/book/chapters_v2"

NUM = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6,
       "SEVEN": 7, "EIGHT": 8, "NINE": 9, "TEN": 10}


def clean(t: str) -> str:
    t = t.replace("\r", "\n")
    t = re.sub(r"-\n\s*", "", t)                 # de-hyphenate words split across lines
    lines = []
    for ln in t.split("\n"):
        s = ln.strip()
        if not s:
            lines.append("")
            continue
        if re.fullmatch(r"[ivxlcIVXLC0-9\.\s]{1,6}", s):   # page numbers / roman folios
            continue
        lines.append(re.sub(r"\s+", " ", s))
    out = "\n".join(lines)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.strip()


def find_body_chapters(ia: str):
    """Body chapter starts: 'CHAPTER <NUMWORD>' occurring after the table of contents."""
    starts = []
    for m in re.finditer(r"CHAPTER\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN)\b", ia):
        word = m.group(1)
        # skip the table-of-contents entries: those are followed by ':' on the same line
        tail = ia[m.end():m.end() + 3]
        if tail.strip().startswith(":"):
            continue
        starts.append((NUM[word], m.start()))
    # dedupe: first (body) occurrence per chapter number
    seen, keep = set(), []
    for num, pos in starts:
        if num in seen:
            continue
        seen.add(num)
        keep.append((num, pos))
    return sorted(keep, key=lambda x: x[0])


def _fold(s: str) -> str:
    """OCR/diacritic-insensitive fold for heading matching."""
    s = s.lower()
    for a, b in (("ā", "a"), ("ī", "i"), ("ū", "u"), ("ṛ", "r"), ("ś", "s"), ("ṣ", "s"),
                 ("ṇ", "n"), ("ṭ", "t"), ("ḍ", "d"), ("ṃ", "m"), ("ṅ", "n"), ("ñ", "n"),
                 ("’", "'"), ("‘", "'"), ("—", " "), ("–", " ")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def section_positions(chunk: str, sections: list[str]):
    """Locate each section heading inside the chapter chunk (first match, in order).

    Matching is fold-based (case/diacritic/punctuation insensitive) and allows headings
    broken across lines, because the OCR text wraps long headings.
    """
    folded_chunk = _fold(chunk)
    pos, cursor = [], 0
    for s in sections:
        key = _fold(s)
        if not key:
            continue
        m = re.search(re.escape(key), folded_chunk[cursor:])
        if not m:
            # try the first four words of the heading (OCR often mangles the tail)
            short = " ".join(key.split()[:4])
            m = re.search(re.escape(short), folded_chunk[cursor:])
        if m:
            # map folded index back to an approximate raw index: walk raw text counting folded chars
            target = m.start()
            count, raw_i = 0, cursor
            for raw_i in range(cursor, len(chunk)):
                nxt = _fold(chunk[raw_i:raw_i + 1])
                count += len(nxt) + (0 if nxt else 0)
                if count >= target:
                    break
            pos.append((s, raw_i))
            cursor = raw_i
    return pos



def main(write=False):
    ia_raw = open(IA, errors="ignore").read()
    toc = json.load(open(TOC))
    chapters = find_body_chapters(ia_raw)
    print("body chapters found:", [c[0] for c in chapters])
    bounds = []
    for i, (num, pos) in enumerate(chapters):
        end = chapters[i + 1][1] if i + 1 < len(chapters) else len(ia_raw)
        bounds.append((num, pos, end))

    report = {}
    for num, start, end in bounds:
        meta = next((c for c in toc if c["id"] == f"ch{num:02d}"), None)
        if not meta:
            continue
        raw = ia_raw[start:end]
        # drop the repeated chapter title line(s) at the top
        raw = re.sub(r"^\s*CHAPTER\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN)\b", "", raw)
        body = clean(raw)
        secs = section_positions(body, meta["sections"])
        parts = []
        for i, (s, p) in enumerate(secs):
            q = secs[i + 1][1] if i + 1 < len(secs) else len(body)
            text = body[p:q]
            text = re.sub(r"^\s*" + re.escape(s).replace(r"\ ", r"\s+"), "", text, count=1, flags=re.I)
            parts.append((s, text.strip()))
        if not parts:
            parts = [(meta["title"], body)]

        out = [f"# {meta['title']}", ""]
        for s, text in parts:
            out += [f"## {s}", "", text, ""]
        content = "\n".join(out)

        old_path = f"{OLD}/ch{num:02d}.txt"
        old_words = len(open(old_path, errors="ignore").read().split()) if os.path.exists(old_path) else 0
        report[f"ch{num:02d}"] = dict(title=meta["title"], sections=len(parts),
                                      words=len(content.split()), old_words=old_words,
                                      gain=len(content.split()) - old_words)
        if write:
            os.makedirs(OUT, exist_ok=True)
            open(f"{OUT}/ch{num:02d}.txt", "w").write(content)

    if write:
        os.makedirs(OUT, exist_ok=True)
        json.dump(report, open(f"{OUT}/_report.json", "w"), indent=1)
    tot_new = sum(r["words"] for r in report.values())
    tot_old = sum(r["old_words"] for r in report.values())
    print(f"{'ch':5s} {'sections':>8s} {'IA words':>9s} {'repo words':>10s} {'gain':>8s}")
    for k, r in sorted(report.items()):
        print(f"{k:5s} {r['sections']:8d} {r['words']:9d} {r['old_words']:10d} {r['gain']:+8d}")
    print(f"TOTAL {tot_new} vs repo {tot_old}  (gain {tot_new - tot_old:+d} words)")
    if not write:
        print("(dry run — pass --write to write book/chapters_v2/)")


if __name__ == "__main__":
    main(write="--write" in sys.argv)
