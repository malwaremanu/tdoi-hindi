#!/usr/bin/env python3
"""Repair a plan's Devanagari anchors against an episode's real take.

Plan writers transliterate the cold open themselves, so a phrase can miss the take's
actual spelling, and a guessed `occurrence` can overshoot (a bed told to end on the
*second* "नमस्कार" never ends when the take has one). This tool repairs both, using
`<workdir>/<chunk>.align.json`:

  1. a phrase that does not resolve at its `occurrence` is retried at 1, 2, 3 … and the
     working occurrence is written back;
  2. a phrase that resolves nowhere is replaced by the best matching window of source
     words (mean consonant-skeleton ratio >= --threshold) and the change is logged;
  3. the repaired plan is saved in place (a `_repairs` entry records every change), so the
     mix is reproducible and the plan on disk is the one that was mixed.

  python3 tools/audio/fix_anchors.py --workdir ep04_2 --plan "scripts/Ep 4.2 … plan.json"
      [--chunk c01] [--threshold 0.6] [--dry-run]
"""
from __future__ import annotations

import argparse
import difflib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mix_from_plan import find_phrase, norm  # noqa: E402

REPO = "/home/itcell/audiobooks/tdoi"


def ratio(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio() if a and b else 0.0


def best_window(align, phrase, threshold):
    """Best contiguous run of source words for `phrase` (length ±1)."""
    A = [norm(r["w"]) for r in align]
    P = [norm(w) for w in phrase]
    best = (0.0, None, None)
    for L in range(max(1, len(P) - 1), len(P) + 2):
        for st in range(0, len(A) - L + 1):
            mean = sum(ratio(A[st + k], P[k]) for k in range(min(L, len(P)))) / max(1, min(L, len(P)))
            if mean > best[0]:
                best = (mean, st, L)
    score, st, L = best
    if st is None or score < threshold:
        return None, score
    return [align[st + k]["w"] for k in range(L)], score


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--plan", required=True)
    ap.add_argument("--chunk", default="c01")
    ap.add_argument("--threshold", type=float, default=0.6)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    work = args.workdir if os.path.isabs(args.workdir) else os.path.join(REPO, args.workdir)
    align = json.load(open(os.path.join(work, args.chunk + ".align.json"), encoding="utf-8"))
    plan = json.load(open(args.plan, encoding="utf-8"))
    repairs = []

    def fix(rec, key, label):
        phrase = rec.get(key)
        if not phrase:
            return
        occ_key = "end_occurrence" if key == "end_phrase" else "occurrence"
        want = int(rec.get(occ_key, 1) or 1)
        if find_phrase(align, phrase, want) is not None:
            return
        for occ in (1, 2, 3, 4):
            t = find_phrase(align, phrase, occ)
            if t is not None:
                rec[occ_key] = occ
                repairs.append(f"{label}: occurrence {want} -> {occ} ({' '.join(phrase)})")
                return
        new, score = best_window(align, phrase, args.threshold)
        if new:
            rec[key] = new
            rec[occ_key] = 1
            repairs.append(f"{label}: phrase {' '.join(phrase)!r} -> {' '.join(new)!r} "
                           f"(ratio {score:.2f})")
        else:
            repairs.append(f"{label}: UNREPAIRABLE {' '.join(phrase)!r} (best {score:.2f})")

    for layer in plan.get("beds", []) + plan.get("score", []):
        fix(layer, "phrase", f"layer {layer.get('id')}")
        fix(layer, "end_phrase", f"layer {layer.get('id')} end")
    for rec in plan.get("cues", []):
        fix(rec, "phrase", f"cue {rec.get('id')}")
    for rec in plan.get("duck", []):
        fix(rec, "phrase", f"duck {rec.get('id')}")

    for line in repairs:
        print("  " + line, flush=True)
    if not repairs:
        print("  nothing to repair", flush=True)
    if not args.dry_run:
        plan.setdefault("_repairs", []).extend(repairs)
        tmp = args.plan + ".tmp"
        json.dump(plan, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        os.replace(tmp, args.plan)
        print(f"  wrote {args.plan}", flush=True)


if __name__ == "__main__":
    main()
