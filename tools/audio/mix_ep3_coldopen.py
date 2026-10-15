#!/usr/bin/env python3
"""Ep 3 cold open: narration + bed + effects + tanpura score, per scripts/Ep 3 — SFX plan.md.

Works in numpy so every layer can have its own envelope (the plan has a crowd that
hushes, stirs, stands and goes quiet, and a score with exactly one swell).

Levels follow the producer rule: effects 12-16 dB under the narration, score 2-4 dB
below the effects. Everything is placed on the narration timeline of the normalised
cold-open take (t=0 = first word).
"""
import os
import subprocess
import sys

import numpy as np

BASE = "/home/itcell/audiobooks/tdoi/ep03"
SFX = os.path.join(BASE, "sfx")
RAW = os.path.join(SFX, "raw_fs")
EP1_RAW = "/home/itcell/audiobooks/tdoi/ep01/sfx/raw_fs"
FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
SR = 48000
COLD_END = 98.0            # host intro starts here — stays clean
PEAK_HEADROOM = 3.0


def sh(a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr[-1500:])
    return r


def load(path, extra=""):
    """Decode to mono float32 at SR."""
    raw = path + ".f32"
    sh([FF, "-y", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", raw])
    if extra:  # apply the plan's EQ before measuring/placing
        sh([FF, "-y", "-i", path, "-ac", "1", "-ar", str(SR), "-af", extra,
            "-f", "f32le", raw])
    x = np.fromfile(raw, dtype=np.float32)
    os.remove(raw)
    return x


def env(points, n):
    """Piecewise-linear envelope in dB over n samples: points=[(t, dB), ...]."""
    t = np.arange(n) / SR
    db = np.interp(t, [p[0] for p in points], [p[1] for p in points])
    return 10 ** (db / 20.0)


def place(buf, seg, at, gain_db, pan, env_db=None, fade_in=0.02, fade_out=0.10):
    """Mix seg into stereo buf at 'at' seconds with gain, pan (-1 L..+1 R), envelope."""
    i = int(at * SR)
    if i >= len(buf):
        return
    seg = seg[: len(buf) - i]
    n = len(seg)
    g = 10 ** (gain_db / 20.0)
    e = env_db if env_db is not None else np.ones(n)
    fi, fo = int(fade_in * SR), int(fade_out * SR)
    if fi:
        e[:fi] *= np.linspace(0, 1, fi)
    if fo:
        e[-fo:] *= np.linspace(1, 0, fo)
    l = 1.0 if pan <= 0 else 1.0 + pan * 0.55
    r = 1.0 if pan >= 0 else 1.0 - pan * 0.55
    buf[i:i + n, 0] += seg * e * g * l
    buf[i:i + n, 1] += seg * e * g * r


def loud_window(path, dur, extra=""):
    """Return the loudest `dur` seconds of a file (avoids picking a quiet patch)."""
    x = load(path, extra)
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


def main():
    # --- normalised narration take (same treatment as the episode join) ---
    src = os.path.join(BASE, "full", "c01.wav")
    norm = os.path.join(SFX, "_c01_norm.wav")
    sh([FF, "-y", "-i", src, "-af", "dynaudnorm=f=200:g=5:p=0.95,aresample=48000",
        "-ac", "1", "-ar", str(SR), norm])
    x = load(norm)
    narr_peak = db(x)
    total = len(x)
    print(f"narration {total / SR:.1f}s  peak {narr_peak:.1f} dBFS")

    buf = np.zeros((total, 2), dtype=np.float64)
    place(buf, x, 0.0, 0.0, 0.0, fade_in=0.0, fade_out=0.0)   # voice dead centre

    # ---------------- B1: dry field / village heat ----------------
    b1 = load(os.path.join(RAW, "b1_village.mp3"), "highpass=120,lowpass=9000")
    if len(b1) < total + SR:
        b1 = np.tile(b1, int((total + SR) // len(b1)) + 1)
    b1 = b1[:int(69.5 * SR)]
    e1 = env([(0, -60), (1.5, 0), (69.0, 0), (69.5, -60)], len(b1))
    place(buf, b1, 0.0, gain_for(db(b1), narr_peak, -16), 0.0, e1, 0.0, 0.0)

    # ---------------- B2: distant crowd, with hush / stir / stand ----------------
    b2 = load(os.path.join(RAW, "crowd.mp3"), "highpass=150,lowpass=5000")
    if len(b2) < int(63 * SR):
        b2 = np.tile(b2, int(63 * SR) // len(b2) + 1)
    b2 = b2[:int(63 * SR)]
    e2 = env([(11.3, -60), (13.8, -18), (28.0, -18), (29.5, -22),
              (37.7, -22), (39.7, -18), (47.0, -18), (48.5, -15),
              (53.0, -15), (53.6, -12), (55.2, -15), (55.8, -15),
              (58.0, -18), (60.5, -18), (63.0, -60)], len(b2))
    place(buf, b2, 0.0, gain_for(db(b2), narr_peak, -12), 0.0, e2, 0.0, 0.0)

    # ---------------- score M1: tanpura drone ----------------
    m1 = load(os.path.join(RAW, "tanpura.mp3"), "highpass=70,lowpass=6000")
    need = int(98.0 * SR)
    if len(m1) < need:
        m1 = np.tile(m1, need // len(m1) + 1)
    m1 = m1[:need]
    em = env([(28.0, -60), (32.0, -18), (47.0, -18), (53.6, -15),
              (54.0, -17), (55.2, -17), (55.3, -15), (55.8, -18),
              (61.0, -18), (63.0, -60), (78.5, -60), (81.5, -20),
              (95.0, -20), (97.6, -60)], len(m1))
    place(buf, m1, 0.0, gain_for(db(m1), narr_peak, -15), 0.0, em, 0.0, 0.0)

    # ---------------- score M2: shruti box, swell only ----------------
    m2 = load(os.path.join(RAW, "shruti.mp3"), "highpass=70,lowpass=6000")
    seg = m2[: int(8.8 * SR)]
    e2m = env([(47.0, -60), (50.0, -18), (54.0, -18), (55.8, -60)], len(seg))
    place(buf, seg, 47.0, gain_for(db(seg), narr_peak, -16), 0.0, e2m, 0.0, 0.0)

    # ---------------- spot effects ----------------
    kite = load(os.path.join(EP1_RAW, "s5_crow.mp3"), "lowpass=6000")
    place(buf, kite, 3.35, gain_for(db(kite), narr_peak, -16), +0.40, fade_in=0.01)

    gust = loud_window(os.path.join(RAW, "wind.mp3"), 3.2)
    eg = env([(0, -60), (1.2, 0), (1.7, 0), (3.2, -60)], len(gust))
    place(buf, gust, 24.3, gain_for(db(gust), narr_peak, -16), -0.30, eg, 0.0, 0.0)

    car = load(os.path.join(RAW, "car_dirt.mp3"))[: int(5.0 * SR)]
    ec = env([(0, -60), (1.6, -14), (4.6, -12), (5.0, -12)], len(car))
    place(buf, car, 32.4, gain_for(db(car), narr_peak, -12), +0.55, ec, 0.0, 0.0)

    stop = loud_window(os.path.join(RAW, "car_dirt.mp3"), 0.9)
    place(buf, stop, 37.05, gain_for(db(stop), narr_peak, -13), +0.20, fade_out=0.35)

    door = loud_window(os.path.join(RAW, "door.mp3"), 0.8)
    place(buf, door, 40.45, gain_for(db(door), narr_peak, -14), +0.20)

    stand = loud_window(os.path.join(RAW, "crowd.mp3"), 1.4)
    es = env([(0, -60), (0.4, 0), (1.0, 0), (1.4, -60)], len(stand))
    place(buf, stand, 47.0, gain_for(db(stand), narr_peak, -13), 0.0, es, 0.0, 0.0)

    shout = loud_window(os.path.join(RAW, "crowd.mp3"), 0.5, "highpass=300,lowpass=2500")
    place(buf, shout, 50.35, gain_for(db(shout), narr_peak, -14), +0.10, fade_out=0.2)

    roar = loud_window(os.path.join(RAW, "crowd.mp3"), 4.6)
    er = env([(0, -60), (0.4, 0), (0.8, 0), (1.0, -3), (2.2, -3),
              (2.35, 0), (2.85, 0), (4.6, -60)], len(roar))
    place(buf, roar, 53.2, gain_for(db(roar), narr_peak, -12), 0.0, er, 0.0, 0.0)

    steps = load(os.path.join(RAW, "steps.mp3"))
    place(buf, steps[: int(0.9 * SR)], 57.15, gain_for(db(steps), narr_peak, -14), -0.10)

    chuck = load(os.path.join(RAW, "chuckle.mp3"))
    place(buf, chuck, 75.45, gain_for(db(chuck), narr_peak, -16), -0.25, fade_out=0.15)

    # ---------------- sum, limit, write ----------------
    peak = np.max(np.abs(buf))
    if peak > 0.95:
        buf *= 0.95 / peak
    buf = np.tanh(buf * 1.05) / np.tanh(1.05)      # gentle limiting, no pumping
    out = os.path.join(SFX, "_c01_mixed.wav")
    buf.astype(np.float32).tofile(out + ".f32")
    sh([FF, "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", out + ".f32", out])
    os.remove(out + ".f32")
    print("wrote", out, f"{len(buf) / SR:.1f}s  peak {db(buf):.1f} dBFS")


if __name__ == "__main__":
    main()
