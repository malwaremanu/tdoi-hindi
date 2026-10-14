#!/usr/bin/env python3
"""Tighten the inter-sentence pauses inside one region of an episode file.

Only the given region (the cold open) is touched: silence longer than MAX_GAP is
cut down to NEW_GAP. Everything after T is copied through untouched, sample for
sample, so the rest of the episode keeps the pacing it already has.

  python3 gap_fix.py IN.mp3 OUT.mp3 --until 56.9 [--max-gap 0.55 --new-gap 0.32]
"""
import argparse
import os
import struct
import subprocess
import sys

import numpy as np

FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
SR = 48000
THR = 400          # |sample| under this counts as silence (~-38 dBFS)
MIN_GAP = 0.25     # only pauses at least this long get shortened


def run(args):
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr[-2000:])


def decode(path, start, dur, raw):
    run([FF, "-y", "-ss", f"{start:.3f}", "-t", f"{dur:.3f}", "-i", path,
         "-ac", "1", "-ar", str(SR), "-f", "s16le", raw])


def wav_wrap(pcm, rate=SR):
    return (b"RIFF" + struct.pack("<I", 36 + len(pcm)) + b"WAVEfmt "
            + struct.pack("<IHHIIHH", 16, 1, 1, rate, rate * 2, 2, 16)
            + b"data" + struct.pack("<I", len(pcm)) + pcm)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--until", type=float, required=True)
    ap.add_argument("--max-gap", type=float, default=0.55)
    ap.add_argument("--new-gap", type=float, default=0.32)
    a = ap.parse_args()

    work = os.path.dirname(os.path.abspath(a.dst))
    head_raw, tail_raw = os.path.join(work, "_head.raw"), os.path.join(work, "_tail.raw")
    decode(a.src, 0, a.until, head_raw)
    x = np.fromfile(head_raw, dtype=np.int16)
    n = len(x)
    print(f"head: {n / SR:.2f}s ({n} samples)")

    quiet = np.abs(x) <= THR
    # find runs of silence
    idx = np.flatnonzero(np.diff(quiet.astype(np.int8)) != 0) + 1
    runs = []
    start = 0
    for b in list(idx) + [n]:
        if quiet[start]:
            runs.append((start, b))
        start = b

    min_len, max_len = int(MIN_GAP * SR), int(a.max_gap * SR)
    new_len = int(a.new_gap * SR)
    pieces, cursor, cuts = [], 0, []
    for s, e in runs:
        if (e - s) >= max_len:
            pieces.append(x[cursor:s])
            keep_sil = np.zeros(new_len, dtype=np.int16)
            pieces.append(keep_sil)
            cursor = e
            cuts.append((s / SR, (e - s) / SR))
    pieces.append(x[cursor:])
    out = np.concatenate(pieces)
    print(f"pauses tightened: {len(cuts)}")
    for t, d in cuts[:20]:
        print(f"   {t:6.2f}s  {d:.2f}s -> {a.new_gap:.2f}s")
    out.tofile(os.path.join(work, "_head_fixed.raw"))
    with open(os.path.join(work, "_head_fixed.raw"), "rb") as f:
        head_wav = os.path.join(work, "_head_fixed.wav")
        open(head_wav, "wb").write(wav_wrap(f.read()))

    # tail: untouched
    tail_wav = os.path.join(work, "_tail.wav")
    total = float(subprocess.run(
        ["/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffprobe", "-v", "error",
         "-show_entries", "format=duration", "-of", "csv=p=0", a.src],
        capture_output=True, text=True).stdout.strip())
    tail_dur = max(0.1, total - a.until)
    run([FF, "-y", "-ss", f"{a.until:.3f}", "-i", a.src, "-t", f"{tail_dur:.3f}",
         "-ac", "1", "-ar", str(SR), tail_wav])

    lst = os.path.join(work, "_concat.txt")
    open(lst, "w").write(f"file '{head_wav}'\nfile '{tail_wav}'\n")
    joined = os.path.join(work, "_joined.wav")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", joined])
    run([FF, "-y", "-i", joined, "-ar", "44100", "-codec:a", "libmp3lame", "-q:a", "2", a.dst])
    dur = subprocess.run([FF, "-i", a.dst, "-f", "null", "-"], capture_output=True, text=True)
    print("wrote", a.dst, os.path.getsize(a.dst), "bytes")


if __name__ == "__main__":
    main()
