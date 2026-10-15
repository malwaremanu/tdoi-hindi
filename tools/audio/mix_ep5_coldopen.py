#!/usr/bin/env python3
"""Ep 5 cold open: court -> road -> India, with a cello->tanpura score handover.

Follows scripts/Ep 5 — SFX plan.md. Everything after the cold open stays clean.

Stereo throughout: beds/score keep their real width, spot cues are panned.
env() values are dB OFFSETS from each layer's nominal level (0 dB = nominal).

Producer rule: effects 12-16 dB under the narration, score 2-4 dB below effects.
"""
import os
import subprocess
import sys

import numpy as np

BASE = "/home/itcell/audiobooks/tdoi/ep05"
SFX = os.path.join(BASE, "sfx")
EP1 = "/home/itcell/audiobooks/tdoi/ep01/sfx/raw_fs"
EP2 = "/home/itcell/audiobooks/tdoi/ep02/sfx/raw_fs"
EP3 = "/home/itcell/audiobooks/tdoi/ep03/sfx/raw_fs"
MINE = os.path.join(SFX, "raw_fs")
FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
SR = 48000
PEAK_HEADROOM = 3.0


def sh(a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr[-1500:])


def load(path, extra=""):
    """Stereo float64 at SR."""
    raw = path + ".f64"
    fx = extra if extra else "anull"
    sh([FF, "-y", "-i", path, "-ac", "2", "-ar", str(SR), "-af", fx, "-f", "f64le", raw])
    x = np.fromfile(raw, dtype=np.float64).reshape(-1, 2)
    os.remove(raw)
    return x


def mono(path, extra=""):
    """Mono float64 at SR."""
    raw = path + ".f64m"
    fx = extra if extra else "anull"
    sh([FF, "-y", "-i", path, "-ac", "1", "-ar", str(SR), "-af", fx, "-f", "f64le", raw])
    x = np.fromfile(raw, dtype=np.float64)
    os.remove(raw)
    return x


def env(points, n):
    t = np.arange(n) / SR
    db = np.interp(t, [p[0] for p in points], [p[1] for p in points])
    return 10 ** (db / 20.0)


def place(buf, seg, at, gain_db, pan=0.0, width=None, env_db=None,
          fade_in=0.02, fade_out=0.10):
    """Mix a mono or stereo seg into stereo buf.

    width (0..1.5) scales the side signal — only meaningful for stereo sources.
    """
    i = int(at * SR)
    if i >= len(buf) or len(seg) == 0:
        return
    seg = seg[: len(buf) - i]
    n = len(seg)
    if seg.ndim == 1:
        seg = np.column_stack([seg, seg])
    if width is not None:
        mid = (seg[:, 0] + seg[:, 1]) / 2
        side = (seg[:, 0] - seg[:, 1]) / 2 * width
        seg = np.column_stack([mid + side, mid - side])
    g = 10 ** (gain_db / 20.0)
    e = env_db if env_db is not None else np.ones(n)
    fi, fo = int(fade_in * SR), int(fade_out * SR)
    if fi:
        e[:fi] *= np.linspace(0, 1, fi)
    if fo:
        e[-fo:] *= np.linspace(1, 0, fo)
    l = g * (1.0 if pan <= 0 else 1.0 + pan * 0.55) * e
    r = g * (1.0 if pan >= 0 else 1.0 - pan * 0.55) * e
    buf[i:i + n, 0] += seg[:, 0] * l
    buf[i:i + n, 1] += seg[:, 1] * r


def loud_window(x, dur):
    """Loudest `dur` seconds of a (mono) signal."""
    w = int(dur * SR)
    if len(x) <= w:
        return x
    e = np.convolve(x ** 2, np.ones(w) / w, mode="valid")
    s = int(np.argmax(e))
    return x[s:s + w]


def gain_for(cue_peak, narr_peak, level_db):
    return (narr_peak - (abs(level_db) - PEAK_HEADROOM)) - cue_peak


def db(x):
    return 20 * np.log10(max(1e-9, float(np.max(np.abs(x)))))


def loop_to(x, samples):
    if len(x) < samples:
        reps = int(np.ceil(samples / len(x)))
        x = np.tile(x, (reps, 1)) if x.ndim == 2 else np.tile(x, reps)
    return x[:samples]


def main():
    src = os.path.join(SFX, "narration_cold.wav")
    sh([FF, "-y", "-t", "106.4", "-i", os.path.join(BASE, "full", "c01.wav"),
        "-ac", "1", "-ar", str(SR), src])
    norm = os.path.join(SFX, "_c01_norm.wav")
    sh([FF, "-y", "-i", src, "-af", "dynaudnorm=f=200:g=5:p=0.95,aresample=48000",
        "-ac", "1", "-ar", str(SR), norm])
    x = mono(norm)
    narr_peak = db(x)
    total = len(x)
    print(f"narration {total / SR:.1f}s  peak {narr_peak:.1f} dBFS")

    buf = np.zeros((total, 2), dtype=np.float64)
    place(buf, x, 0.0, 0.0, 0.0, fade_in=0.0, fade_out=0.0)

    # ---------------- B1: court / city hall ----------------
    court = load(os.path.join(EP3, "crowd.mp3"), "highpass=150,lowpass=5000")
    court = loop_to(court, int(41 * SR))
    e1 = env([(0.0, -60), (1.5, 0), (18.0, 0), (20.0, -1), (38.0, -1),
              (40.0, -60)], len(court))
    place(buf, court, 0.0, gain_for(db(court), narr_peak, -15), 0.0,
          width=0.70, env_db=e1, fade_in=0.0, fade_out=0.0)

    # ---------------- B2: open road wind ----------------
    road = load(os.path.join(EP3, "wind.mp3"), "highpass=200,lowpass=3000")
    road = loop_to(road, int(45.5 * SR))
    e2 = env([(38.0, -60), (40.0, 0), (43.0, 0), (43.5, -3), (45.0, -60)],
             len(road))
    place(buf, road, 0.0, gain_for(db(road), narr_peak, -15), 0.0,
          width=0.90, env_db=e2, fade_in=0.0, fade_out=0.0)

    # ---------------- B3: India, village afternoon ----------------
    india = load(os.path.join(EP3, "b1_village.mp3"), "highpass=120,lowpass=9000")
    india = loop_to(india, int(53 * SR))
    e3 = env([(41.0, -60), (43.0, 0), (45.0, -1), (50.0, -1), (52.5, -60)],
             len(india))
    place(buf, india, 0.0, gain_for(db(india), narr_peak, -14), 0.0,
          width=0.70, env_db=e3, fade_in=0.0, fade_out=0.0)

    # ---------------- M1: cello drone (the journey) ----------------
    m1 = mono(os.path.join(EP2, "drone.mp3"), "highpass=70,lowpass=4000")
    m1 = loop_to(m1, int(48.5 * SR))
    em1 = env([(6.0, -60), (10.0, 0), (18.0, 0), (20.0, -1), (38.0, -1),
               (40.0, 0), (41.0, 0), (43.0, 0.5), (45.0, 0.5), (48.0, -60)],
              len(m1))
    place(buf, m1, 0.0, gain_for(db(m1), narr_peak, -18), 0.0,
          width=0.50, env_db=em1, fade_in=0.0, fade_out=0.0)

    # ---------------- M2: tanpura (India) ----------------
    m2 = mono(os.path.join(EP3, "tanpura.mp3"), "highpass=70,lowpass=6000")
    need = int(65 * SR)
    m2 = loop_to(m2, need)
    em2 = env([(41.0, -60), (43.0, -3.5), (45.0, -3.5), (48.0, 0),
               (50.0, 0), (52.5, -2), (54.8, -60), (56.2, -60),
               (59.2, -2), (62.4, -2), (64.4, -60)], len(m2))
    place(buf, m2, 0.0, gain_for(db(m2), narr_peak, -18), 0.0,
          width=0.50, env_db=em2, fade_in=0.0, fade_out=0.0)

    # ---------------- spot effects ----------------
    steps = mono(os.path.join(EP3, "steps.mp3"), "highpass=120,lowpass=7000")
    steps = loud_window(steps, 0.7)[: int(0.7 * SR)]
    es = env([(0, -60), (0.05, 0), (0.6, 0), (0.7, -60)], len(steps))
    place(buf, steps, 20.2, gain_for(db(steps), narr_peak, -15), -0.20,
          env_db=es, fade_in=0.0, fade_out=0.0)

    cup = mono(os.path.join(MINE, "cup.mp3"), "highpass=300,lowpass=7000")
    cup = loud_window(cup, 0.4)[: int(0.4 * SR)]
    ec = env([(0, -60), (0.03, 0), (0.3, 0), (0.4, -60)], len(cup))
    place(buf, cup, 21.8, gain_for(db(cup), narr_peak, -16), +0.10,
          env_db=ec, fade_in=0.0, fade_out=0.0)

    grit = mono(os.path.join(EP1, "s2_gravel.mp3"), "highpass=300,lowpass=6000")
    grit = loud_window(grit, 0.28)[: int(0.28 * SR)]
    place(buf, grit, 26.3, gain_for(db(grit), narr_peak, -15), +0.10,
          fade_out=0.06)

    swirl = mono(os.path.join(MINE, "liq.mp3"), "highpass=150,lowpass=6000")
    swirl = loud_window(swirl, 0.4)[: int(0.4 * SR)]
    ew = env([(0, -60), (0.05, 0), (0.25, 0), (0.4, -60)], len(swirl))
    place(buf, swirl, 26.58, gain_for(db(swirl), narr_peak, -15), +0.10,
          env_db=ew, fade_in=0.0, fade_out=0.0)

    pack = mono(os.path.join(EP2, "wicker.mp3"), "highpass=150,lowpass=6000")
    pack = loud_window(pack, 0.6)[: int(0.6 * SR)]
    place(buf, pack, 40.1, gain_for(db(pack), narr_peak, -15), -0.10,
          fade_out=0.12)

    crow = mono(os.path.join(EP1, "s5_crow.mp3"), "lowpass=6000")
    place(buf, crow, 44.35, gain_for(db(crow), narr_peak, -16), +0.50,
          fade_out=0.15)

    manu = mono(os.path.join(EP1, "s8_paper.mp3"), "highpass=200,lowpass=7000")
    manu = loud_window(manu, 0.7)[: int(0.7 * SR)]
    em = env([(0, -60), (0.05, 0), (0.55, 0), (0.7, -60)], len(manu))
    place(buf, manu, 49.1, gain_for(db(manu), narr_peak, -15), -0.20,
          env_db=em, fade_in=0.0, fade_out=0.0)

    peak = np.max(np.abs(buf))
    if peak > 0.95:
        buf *= 0.95 / peak
    buf = np.tanh(buf * 1.05) / np.tanh(1.05)
    out = os.path.join(SFX, "_c01_mixed.wav")
    buf.astype(np.float64).tofile(out + ".f64")
    sh([FF, "-y", "-f", "f64le", "-ar", str(SR), "-ac", "2", "-i", out + ".f64", out])
    os.remove(out + ".f64")
    print("wrote", out, f"{len(buf) / SR:.1f}s  peak {db(buf):.1f} dBFS")


if __name__ == "__main__":
    main()
