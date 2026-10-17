#!/usr/bin/env python3
"""QC a chunked episode take set: transcribe with word timestamps and check the
take against the source text.

  <whisper-venv>/bin/python3 tools/audio/verify_episode.py --workdir ep04_1 \
      --chunks c01,c02,c03,c04,c05 [--gap-report c01]

Writes <workdir>/<chunk>.whisper.json and prints, per chunk:
  source words | words heard | similarity | missing-word list | extra-word list
With --gap-report it also prints the silence gaps between spoken segments of that
chunk (used to decide where paragraph pauses may be tightened).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import unicodedata

import numpy as np
from faster_whisper import WhisperModel

FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"


def load16k(path):
    raw = path + ".s16"
    subprocess.run([FF, "-y", "-i", path, "-ac", "1", "-ar", "16000", "-f", "s16le", raw],
                   check=True, capture_output=True)
    x = np.fromfile(raw, dtype=np.int16).astype(np.float32) / 32768.0
    os.remove(raw)
    return x


def norm(s):
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"[^\w\s\u0900-\u097F]", " ", s)
    return [w for w in s.split() if w]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--chunks", required=True)
    ap.add_argument("--gap-report", default="")
    ap.add_argument("--model", default="small")
    args = ap.parse_args()

    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    chunks = [c.strip() for c in args.chunks.split(",") if c.strip()]
    summary = []
    for n in chunks:
        wav = os.path.join(args.workdir, n + ".wav")
        txt = os.path.join(args.workdir, n + ".txt")
        if not os.path.exists(wav):
            print(f"{n}: MISSING wav", flush=True)
            continue
        src = open(txt, encoding="utf-8").read() if os.path.exists(txt) else ""
        segs, _ = model.transcribe(load16k(wav), language="hi", word_timestamps=True,
                                   vad_filter=True, beam_size=5)
        seg_list, said = [], []
        for s in segs:
            d = {"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text}
            if s.words:
                d["words"] = [{"w": w.word, "s": round(w.start, 2), "e": round(w.end, 2)}
                              for w in s.words]
                said += [w.word for w in s.words]
            seg_list.append(d)
        json.dump({"source_words": len(src.split()), "segs": seg_list},
                  open(os.path.join(args.workdir, n + ".whisper.json"), "w"), ensure_ascii=False)
        a, b = norm(src), norm(" ".join(said))
        sa, sb = set(a), set(b)
        sim = (2 * len(sa & sb)) / (len(sa) + len(sb)) if (sa or sb) else 0.0
        missing = [w for w in a if w not in sb]
        extra = [w for w in b if w not in sa]
        print(f"{n}: source {len(a)} | heard {len(b)} | sim {sim:.3f}", flush=True)
        if missing:
            print(f"   missing ({len(missing)}): {' '.join(missing[:24])}", flush=True)
        if extra:
            print(f"   extra ({len(extra)}): {' '.join(extra[:16])}", flush=True)
        summary.append([n, len(a), len(b), round(sim, 3)])

        if args.gap_report and n == args.gap_report:
            print(f"--- {n} gaps between spoken segments (>0.55 s) ---", flush=True)
            for p, q in zip(seg_list, seg_list[1:]):
                g = q["start"] - p["end"]
                if g > 0.55:
                    print(f"   {p['end']:7.2f} -> {q['start']:7.2f}  ({g:.2f}s) "
                          f"after: {p['text'].strip()[-44:]!r}", flush=True)
            print(f"   total {seg_list[-1]['end']:.2f}s", flush=True)

    print("summary:", json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
