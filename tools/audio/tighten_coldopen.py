#!/usr/bin/env python3
"""Tighten paragraph pauses in the Ep3 r2 cold open, keeping the cue gaps and the
sannata zone untouched, then splice the untouched tail behind it.

  python3 tighten_coldopen.py IN.wav OUT.wav --until 134.68
"""
import argparse, os, struct, subprocess, sys
import numpy as np

FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
SR = 48000
THR = 400
MIN_GAP = 0.25
MAX_GAP = 1.0
NEW_GAP = 0.75

# regions a cue sits in (raw-take seconds) + the deliberate silence zone:
# never shortened, so the plan's gaps and dead air survive exactly.
KEEP = [
    (50.3, 51.4),    # S5 car door gap
    (60.6, 61.25),   # S7 single shout gap
    (62.05, 63.15),  # S8 group shout gap
    (63.55, 64.65),  # S9 roar peak gap
    (65.8, 66.85),   # S9 second beat gap
    (67.9, 68.65),   # S10 footsteps gap
    (85.29, 94.31),  # question + sannata + chuckle: dead air, never tightened
]


def run(a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr[-2000:])


def wav_wrap(pcm, rate=SR):
    return (b"RIFF" + struct.pack("<I", 36 + len(pcm)) + b"WAVEfmt "
            + struct.pack("<IHHIIHH", 16, 1, 1, rate, rate * 2, 2, 16)
            + b"data" + struct.pack("<I", len(pcm)) + pcm)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dst")
    ap.add_argument("--until", type=float, required=True)
    a = ap.parse_args()

    work = os.path.dirname(os.path.abspath(a.dst))
    head_raw, tail_raw = os.path.join(work, "_h.raw"), os.path.join(work, "_t.raw")
    run([FF, "-y", "-ss", "0", "-t", f"{a.until:.3f}", "-i", a.src,
         "-ac", "1", "-ar", str(SR), "-f", "s16le", head_raw])
    run([FF, "-y", "-ss", f"{a.until:.3f}", "-i", a.src,
         "-ac", "1", "-ar", str(SR), "-f", "s16le", tail_raw])

    x = np.fromfile(head_raw, dtype=np.int16)
    tail = np.fromfile(tail_raw, dtype=np.int16)
    n = len(x)
    quiet = np.abs(x) <= THR
    idx = np.flatnonzero(np.diff(quiet.astype(np.int8)) != 0) + 1
    runs, start = [], 0
    for b in list(idx) + [n]:
        if quiet[start]:
            runs.append((start, b))
        start = b

    pieces, cursor, cuts = [], 0, []
    for s, e in runs:
        t0, t1 = s / SR, e / SR
        dur = e - s
        protected = any(not (t1 <= k0 or t0 >= k1) for k0, k1 in KEEP)
        if (not protected) and dur >= MAX_GAP * SR:
            pieces.append(x[cursor:s])
            pieces.append(np.zeros(int(NEW_GAP * SR), dtype=np.int16))
            cursor = e
            cuts.append((t0, dur / SR))
    pieces.append(x[cursor:])
    out = np.concatenate(pieces)
    out = np.concatenate([out, tail])   # untouched tail behind the tightened head

    with open(a.dst, "wb") as f:
        f.write(wav_wrap(out.tobytes()))
    print(f"head {n / SR:.2f}s -> {len(out) / SR:.2f}s "
          f"({len(cuts)} pauses {MAX_GAP}s+ -> {NEW_GAP}s), tail {len(tail) / SR:.2f}s")
    for t, d in cuts[:30]:
        print(f"   {t:7.2f}s  {d:.2f}s")
    for k0, k1 in KEEP:
        print(f"   kept {k0:.2f}-{k1:.2f}")
    for p in (head_raw, tail_raw):
        os.remove(p)


if __name__ == "__main__":
    main()
