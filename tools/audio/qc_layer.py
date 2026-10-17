#!/usr/bin/env python3
"""Measure an episode's cold-open mix: narration vs the SFX layer, window by window.

  python3 tools/audio/qc_layer.py --workdir ep04_2 [--chunk c01]

Prints the true "dB under voice" of the effect layer (the mix keeps the layer as
`_c01_sfx_only.wav`, so this is the layer that was actually added, not `mixed - dry`,
which the tanh limiter distorts) plus the host-intro window, which must be digital silence
in the layer.
"""
import argparse, os, subprocess, sys
import numpy as np

FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
REPO = "/home/itcell/audiobooks/tdoi"
SR = 48000


def load(p):
    raw = p + ".f32"
    subprocess.run([FF, "-y", "-i", p, "-ac", "1", "-ar", str(SR), "-f", "f32le", raw],
                   check=True, capture_output=True)
    x = np.fromfile(raw, dtype=np.float32)
    os.remove(raw)
    return x


def db(x):
    return 20 * np.log10(max(1e-9, float(np.sqrt(np.mean(x ** 2)))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--chunk", default="c01")
    ap.add_argument("--step", type=float, default=10.0)
    args = ap.parse_args()
    work = args.workdir if os.path.isabs(args.workdir) else os.path.join(REPO, args.workdir)
    sfx = os.path.join(work, "sfx")
    dry = load(os.path.join(sfx, f"_{args.chunk}_norm.wav"))
    mix = load(os.path.join(sfx, f"_{args.chunk}_mixed.wav"))
    lay = load(os.path.join(sfx, f"_{args.chunk}_sfx_only.wav"))
    n = min(len(dry), len(mix), len(lay))
    dry, mix, lay = dry[:n], mix[:n], lay[:n]
    total = n / SR
    print(f"{'window':<18}{'narr':>8}{'mix':>8}{'sfx':>8}{'sfx-narr':>10}")
    t = 0.0
    while t < total:
        e = min(total, t + args.step)
        sl = slice(int(t * SR), int(e * SR))
        nd, ms, ls = db(dry[sl]), db(mix[sl]), db(lay[sl])
        print(f"{t:6.1f}-{e:6.1f}{nd:>8.1f}{ms:>8.1f}{ls:>8.1f}{ls - nd:>10.1f}")
        t = e
    print(f"whole: narr {db(dry):.1f}  mix {db(mix):.1f}  sfx {db(lay):.1f} "
          f"({db(lay) - db(dry):+.1f} dB)")


if __name__ == "__main__":
    main()
