#!/usr/bin/env python3
"""Post-process book/chapters_v2/*.txt (from rebuild_chapters_ia.py):

1. drop heading-echo lines that leaked into the body,
2. reflow OCR line wrapping into real paragraphs,
3. write a GAP report: paragraphs present in v2 but missing from the old
   book/chapters/<ch>.txt (i.e. everything the repo copy had lost).

Usage: python3 tools/book/fix_chapters_v2.py
"""
from __future__ import annotations

import json
import os
import re

ROOT = "/home/itcell/audiobooks/tdoi"
OLD = f"{ROOT}/book/chapters"
V2 = f"{ROOT}/book/chapters_v2"


def reflow(text: str) -> str:
    blocks = [re.sub(r"\s+", " ", b).strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    merged: list[str] = []
    for b in blocks:
        if merged and not re.search(r"[.!?:;\"')\]]$", merged[-1]) and not re.match(r"^[A-Z#]", b) and len(merged[-1]) + len(b) < 1400:
            merged[-1] = merged[-1] + " " + b
        else:
            merged.append(b)
    out = "\n\n".join(merged)
    # OCR hyphen breaks: "concep- tion" / "well- known" -> join
    out = re.sub(r"(\w)- (\w)", r"\1\2", out)
    # footnote markers left by the OCR ("[1]", "1 ", "12 ") at a sentence start
    out = re.sub(r"(?m)^\s*\d{1,2}\s+(?=[A-Z])", "", out)
    return re.sub(r"[ \t]{2,}", " ", out)


def _fold(s: str) -> str:
    return re.sub(r"[^a-z]", "", s.lower())


def split_sections(content: str):
    """Yield (heading, body) for a '# chapter / ## section' file."""
    parts = re.split(r"^## ", content, flags=re.M)
    head = parts[0]
    out = []
    for p in parts[1:]:
        title, _, body = p.partition("\n")
        out.append((title.strip(), body.strip()))
    return head.strip(), out


def main():
    report = {}
    for name in sorted(os.listdir(V2)):
        if not name.endswith(".txt"):
            continue
        ch = name[:-4]
        path = os.path.join(V2, name)
        content = open(path, errors="ignore").read()
        head, sections = split_sections(content)
        fixed = []
        for title, body in sections:
            body = reflow(body)
            # drop the first line if it is just the heading again
            first, _, rest = body.partition("\n")
            f_first, f_title = _fold(first), _fold(title)
            if f_first and (f_first in f_title or f_title.startswith(f_first[:16]) or f_first.startswith(f_title[:16])):
                body = rest.strip()
            fixed.append((title, body))
        outp = [head, ""]
        for title, body in fixed:
            outp += [f"## {title}", "", body, ""]
        open(path, "w").write("\n".join(outp))

        # gap report vs the old repo chapter
        old_path = os.path.join(OLD, name)
        old = re.sub(r"\s+", " ", open(old_path, errors="ignore").read()) if os.path.exists(old_path) else ""
        new_paras = [p for _, body in fixed for p in body.split("\n\n")]
        missing = [p for p in new_paras if re.sub(r"\s+", " ", p.strip())[:90] not in old]
        words_new = sum(len(b.split()) for _, b in fixed)
        words_old = len(open(old_path, errors="ignore").read().split()) if os.path.exists(old_path) else 0
        report[ch] = dict(sections=len(fixed), words=words_new, old_words=words_old,
                          recovered_paragraphs=len(missing),
                          recovered_words=words_new - words_old,
                          sample=[p[:110] for p in sorted(missing, key=len, reverse=True)[:3]])
    json.dump(report, open(f"{V2}/_report.json", "w"), ensure_ascii=False, indent=1)

    lines = ["# Recovered source text (repo chapter files vs Internet Archive full text)", "",
             "| ch | sections | v2 words | repo words | recovered paragraphs | recovered words |",
             "|---|---|---|---|---|---|"]
    for ch, r in sorted(report.items()):
        lines.append(f"| {ch} | {r['sections']} | {r['words']:,} | {r['old_words']:,} | {r['recovered_paragraphs']} | +{r['recovered_words']:,} |")
    lines += ["", "## Samples of recovered paragraphs", ""]
    for ch, r in sorted(report.items()):
        if r["sample"]:
            lines.append(f"**{ch}**")
            lines += [f"- {s}…" for s in r["sample"]]
            lines.append("")
    open(f"{V2}/_gap_report.md", "w").write("\n".join(lines))
    print(f"processed {len(report)} chapters; report -> {V2}/_gap_report.md")
    for ch, r in sorted(report.items()):
        print(f"{ch} sections={r['sections']:3d} words={r['words']:6d} (repo {r['old_words']:6d}) recovered_paras={r['recovered_paragraphs']:4d}")


if __name__ == "__main__":
    main()
