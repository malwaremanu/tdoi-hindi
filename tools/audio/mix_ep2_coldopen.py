#!/usr/bin/env python3
"""Ep 2 cold open: narration + engine bed + a restrained score, per scripts/Ep 2 — SFX plan.md.

The engine is the scene: a steady prop drone with one lift, one throttle-back and one
fade. The score is a bowed-string floor (D drone) with exactly two cello notes (A, then
F) and one swell. Everything leaves before the host intro at 01:12.

Levels: effects 12-16 dB under the narration, score 2-4 dB below the effects.
"""
import os
import subprocess
import sys

import numpy as np

BASE = "/home/itcell/audiobooks/tdoi/ep02"
SFX = os.path.join(BASE, "sfx")
RAW = os.path.join(SFX, "raw_fs")
FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
SR = 48000
COLD_END = 92.0
PEAK_HEADROOM = 3.0


def sh(a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr[-1500:])


def load(path, extra="", pitch=None):
    """Mono float32 at SR; optional EQ chain and pitch shift in semitones."""
    raw = path + ".f32"
    fx = []
    if extra:
        fx.append(extra)
    if pitch:
        ratio = 2 ** (pitch / 12.0)
        fx.append(f"asetrate={int(SR * ratio)},aresample={SR},atempo={1 / ratio:.6f}")
    chain = (",".join(fx)) if fx else "anull"
    sh([FF, "-y", "-i", path, "-ac", "1", "-ar", str(SR), "-af", chain, "-f", "f32le", raw])
    x = np.fromfile(raw, dtype=np.float32)
    os.remove(raw)
    return x


def env(points, n):
    t = np.arange(n) / SR
    db = np.interp(t, [p[0] for p in points], [p[1] for p in points])
    return 10 ** (db / 20.0)


def place(buf, seg, at, gain_db, pan, env_db=None, fade_in=0.02, fade_out=0.10):
    i = int(at * SR)
    if i >= len(buf) or len(seg) == 0:
        return
    seg = seg[: len(buf) - i]
    n = len(seg)
    g = 10 ** (gain_db / 20.0)
    e = env_db if env_db is not None else np.ones(n, dtype=np.float64)
    fi, fo = int(fade_in * SR), int(fade_out * SR)
    if fi:
        e[:fi] *= np.linspace(0, 1, fi)
    if fo:
        e[-fo:] *= np.linspace(1, 0, fo)
    l = 1.0 if pan <= 0 else 1.0 + pan * 0.55
    r = 1.0 if pan >= 0 else 1.0 - pan * 0.55
    buf[i:i + n, 0] += seg * e * g * l
    buf[i:i + n, 1] += seg * e * g * r


def loud_window(x, dur):
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
    src = os.path.join(SFX, "narration_92s.wav")
    # original take, unmodified pacing — only sounds are added, never re-timed
    sh([FF, "-y", "-t", str(COLD_END), "-i", os.path.join(BASE, "ep02_full.mp3"),
        "-ac", "1", "-ar", str(SR), src])
    norm = os.path.join(SFX, "_c01_norm.wav")
    sh([FF, "-y", "-i", src, "-af", "dynaudnorm=f=200:g=5:p=0.95,aresample=48000",
        "-ac", "1", "-ar", str(SR), norm])
    x = load(norm)
    total = len(x)
    narr_peak = db(x)
    print(f"narration {total / SR:.1f}s  peak {narr_peak:.1f} dBFS")

    buf = np.zeros((total, 2), dtype=np.float64)
    place(buf, x, 0.0, 0.0, 0.0, fade_in=0.0, fade_out=0.0)

    # ---- B1: engine, steady cruise, with the 00:08 lift and the 01:07.6 fade ----
    eng = load(os.path.join(RAW, "engine2.mp3"), "lowpass=7000,highpass=80")
    if len(eng) < int(72 * SR):
        eng = np.tile(eng, int(72 * SR) // len(eng) + 1)
    eng = eng[: int(72 * SR)]
    eb = env([(0, -60), (0.8, 0), (8.0, 0), (9.5, 3), (12.0, 3), (12.8, 0),
              (67.6, 0), (68.5, 0), (71.8, -60)], len(eng))
    place(buf, eng, 0.0, gain_for(db(eng), narr_peak, -16), -0.30, eb, 0.0, 0.0)

    # ---- E2: engine throttles back (same recording, ~1 semitone down, slower) ----
    thr = load(os.path.join(RAW, "engine2.mp3"), "lowpass=6500,highpass=90", pitch=-1.2)
    thr = thr[int(55 * SR): int(55 * SR) + int(5 * SR)]
    et = env([(0, -60), (1.5, 0), (3.2, 0), (4.4, -60)], len(thr))
    place(buf, thr, 67.6, gain_for(db(thr), narr_peak, -14), -0.30, et, 0.0, 0.0)

    # ---- B2: thin air over the fuselage ----
    air = load(os.path.join(RAW, "air.mp3"), "highpass=400,lowpass=6000")
    if len(air) < int(72 * SR):
        air = np.tile(air, int(72 * SR) // len(air) + 1)
    air = air[: int(72 * SR)]
    ea = env([(0, -60), (1.0, 0), (68.5, 0), (71.8, -60)], len(air))
    place(buf, air, 0.0, gain_for(db(air), narr_peak, -22), +0.20, ea, 0.0, 0.0)

    # ---- M1: bowed-string drone on D ----
    m1 = load(os.path.join(RAW, "drone.mp3"), "highpass=70,lowpass=6000")
    need = int(42 * SR)
    if len(m1) < need:
        m1 = np.tile(m1, need // len(m1) + 1)
    m1 = m1[:need]
    em = env([(24.5, -60), (28.5, -20), (64.2, -20), (64.9, -60)], len(m1))
    place(buf, m1, 24.5, gain_for(db(m1), narr_peak, -18), 0.0, em, 0.0, 0.0)

    # ---- M2a: one cello note (A) under the kalash / ash lines ----
    a_note = load(os.path.join(RAW, "cello.mp3"), "highpass=90,lowpass=5500", pitch=-3.0)
    a_note = loud_window(a_note, 5.4)
    ea2 = env([(0, -60), (1.5, 0), (3.4, 0), (5.4, -60)], len(a_note))
    place(buf, a_note, 39.6, gain_for(db(a_note), narr_peak, -18), +0.15, ea2, 0.0, 0.0)

    # ---- M2b: one cello note (F) — the one swell ----
    f_note = load(os.path.join(RAW, "cello.mp3"), "highpass=90,lowpass=5500", pitch=-7.0)
    f_note = loud_window(f_note, 6.9)
    ef = env([(0, -60), (2.0, -2), (2.9, 0), (4.4, 0), (6.9, -60)], len(f_note))
    place(buf, f_note, 47.6, gain_for(db(f_note), narr_peak, -16), +0.15, ef, 0.0, 0.0)

    # ---- E1: one soft wicker creak from the basket ----
    wick = load(os.path.join(RAW, "wicker.mp3"), "highpass=150,lowpass=6000")
    wick = loud_window(wick, 0.6)
    place(buf, wick, 32.5, gain_for(db(wick), narr_peak, -16), +0.35, fade_out=0.15)

    peak = np.max(np.abs(buf))
    if peak > 0.95:
        buf *= 0.95 / peak
    buf = np.tanh(buf * 1.05) / np.tanh(1.05)
    out = os.path.join(SFX, "_c01_mixed.wav")
    buf.astype(np.float32).tofile(out + ".f32")
    sh([FF, "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", out + ".f32", out])
    os.remove(out + ".f32")
    print("wrote", out, f"{len(buf) / SR:.1f}s  peak {db(buf):.1f} dBFS")


if __name__ == "__main__":
    main()
