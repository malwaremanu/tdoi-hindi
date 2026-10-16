#!/usr/bin/env python3
"""Ep 6 cold open: narration + hall air + darbar murmur + paper cues + tanpura score.

Implements scripts/Ep 6 — SFX plan.md exactly: same source files, levels, pans and
envelopes as the plan's cue table, timed against the tightened narration
ep06/c01_t.wav (transcript: ep06/c01_t.whisper.json).
"""
import os
import subprocess
import sys

import numpy as np

BASE = "/home/itcell/audiobooks/tdoi/ep06"
SFX = os.path.join(BASE, "sfx")
EP1_RAW = "/home/itcell/audiobooks/tdoi/ep01/sfx/raw_fs"
EP3_RAW = "/home/itcell/audiobooks/tdoi/ep03/sfx/raw_fs"
EP5_RAW = "/home/itcell/audiobooks/tdoi/ep05/sfx/raw_fs"
FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
SR = 48000
COLD_END = 103.0           # buffer; host intro starts at 102.92
PEAK_HEADROOM = 3.0

# ---- plan cue anchors (tightened narration timeline, seconds) ----
T_B2_IN = 14.62            # "दर्भार भरा है" — the hall fills
T_STEP = 17.85             # gap before "अजनबी काले चोगो"
T_BOOK = 22.68             # gap after "जस्विट पादरी" — book handed over
T_STIR = 29.12             # "हाथ में लेते हैं" — B2 stir
T_TURN1 = 32.95            # page turn, on "पलडते" (documented overlap)
T_TURN2 = 33.46            # gap before "फिर तुस्रा"
T_HUSH = 35.16             # "अब दियान देजे" — the hall leans in
T_SETDOWN = 70.42          # gap after "रहती जाते है" — book set down
T_M1_IN = 71.12            # "एक चोटा सबाल" — score enters
T_B2_OUT = 74.34           # "कोई उसे जुबान पर नहीं लाता"
T_QUESTION = 76.94         # "ये बनी कैसे?" — nothing plays here
T_B1_OUT = 88.00           # "अगले कामपर चला जाता है" — hall leaves
T_CODA = 89.32             # "तीन सो साल बाद" — score returns at -20
T_M1_STOP = 102.45         # hard stop, ≥0.45 s dead air before "नमस्कार"


def sh(a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr[-1500:])
    return r


def load(path, extra=""):
    raw = path + ".f64tmp.f32"
    args = [FF, "-y", "-i", path, "-ac", "1", "-ar", str(SR)]
    if extra:
        args += ["-af", extra]
    args += ["-f", "f32le", raw]
    sh(args)
    x = np.fromfile(raw, dtype=np.float32)
    os.remove(raw)
    return x


def env(points, n):
    pts = sorted(points, key=lambda p: p[0])
    t = np.arange(n) / SR
    db = np.interp(t, [p[0] for p in pts], [p[1] for p in pts])
    return 10 ** (db / 20.0)


def place(buf, seg, at, gain_db, pan, env_db=None, fade_in=0.02, fade_out=0.10):
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


def loud_window(path, dur, extra="", offset_frac=None):
    """Loudest `dur` seconds, or a window at `offset_frac` when given (so the two
    page turns are not literally the same slice)."""
    x = load(path, extra)
    w = int(dur * SR)
    if len(x) <= w:
        return x
    if offset_frac is not None:
        s = int(len(x) * offset_frac)
        return x[s:s + w]
    e = np.convolve(x ** 2, np.ones(w) / w, mode="valid")
    s = int(np.argmax(e))
    return x[s:s + w]


def gain_for(cue_peak, narr_peak, level_db):
    return (narr_peak - (abs(level_db) - PEAK_HEADROOM)) - cue_peak


def db(x):
    return 20 * np.log10(max(1e-9, float(np.max(np.abs(x)))))


def main():
    os.makedirs(SFX, exist_ok=True)
    src = os.path.join(BASE, "c01_t.wav")
    norm = os.path.join(SFX, "_c01_norm.wav")
    sh([FF, "-y", "-i", src, "-af", "dynaudnorm=f=200:g=5:p=0.95,aresample=48000",
        "-ac", "1", "-ar", str(SR), norm])
    x = load(norm)
    narr_peak = db(x)
    total = len(x)
    print(f"narration {total / SR:.1f}s  peak {narr_peak:.1f} dBFS")

    buf = np.zeros((total, 2), dtype=np.float64)
    place(buf, x, 0.0, 0.0, 0.0, fade_in=0.0, fade_out=0.0)

    # ---------------- B1: still hall air ----------------
    b1 = load(os.path.join(EP1_RAW, "b1_bed.mp3"), "highpass=120,lowpass=9000")
    if len(b1) < int((T_B1_OUT + 2) * SR):
        b1 = np.tile(b1, int(((T_B1_OUT + 2) * SR) // len(b1)) + 1)
    b1 = b1[: int(T_B1_OUT * SR)]
    e1 = env([(0, -60), (1.5, 0), (T_B1_OUT - 0.9, 0), (T_B1_OUT, -60)], len(b1))
    place(buf, b1, 0.0, gain_for(db(b1), narr_peak, -16), 0.0, e1, 0.0, 0.0)

    # ---------------- B2: darbar murmur (fills, stirs, hushes, leaves) ----------------
    b2 = load(os.path.join(EP3_RAW, "crowd.mp3"), "highpass=150,lowpass=5000")
    b2_end = T_B2_OUT + 2.3
    if len(b2) < int(b2_end * SR):
        b2 = np.tile(b2, int((b2_end * SR) // len(b2)) + 1)
    b2 = b2[: int(b2_end * SR)]
    e2 = env([(T_B2_IN, -60), (T_B2_IN + 2.5, -18),
              (T_STIR, -18), (T_STIR + 2.0, -16),
              (T_HUSH, -16), (T_HUSH + 1.5, -22),
              (T_B2_OUT, -22), (T_B2_OUT + 2.3, -60)], len(b2))
    place(buf, b2, 0.0, gain_for(db(b2), narr_peak, -12), 0.0, e2, 0.0, 0.0)

    # ---------------- M1: tanpura drone (one swell, then coda) ----------------
    m1 = load(os.path.join(EP3_RAW, "tanpura.mp3"), "highpass=70,lowpass=6000")
    need = int(COLD_END * SR)
    if len(m1) < need:
        m1 = np.tile(m1, need // len(m1) + 1)
    m1 = m1[:need]
    em = env([(T_M1_IN, -60), (T_M1_IN + 4.0, -18),
              (T_M1_IN + 4.0 + 1.3, -15),      # the one swell peaks 01:16.4
              (76.9, -60),                     # gone before the question
              (T_CODA, -60), (T_CODA + 3.0, -20),
              (99.9, -20), (T_M1_STOP, -60)], len(m1))
    place(buf, m1, 0.0, gain_for(db(m1), narr_peak, -15), 0.0, em, 0.0, 0.0)

    # ---------------- spot cues ----------------
    steps = load(os.path.join(EP3_RAW, "steps.mp3"))
    place(buf, steps[: int(0.95 * SR)], T_STEP,
          gain_for(db(steps), narr_peak, -16), +0.35, fade_in=0.01)

    book = loud_window(os.path.join(EP1_RAW, "s8_paper.mp3"), 0.7)
    place(buf, book, T_BOOK, gain_for(db(book), narr_peak, -16), -0.15,
          fade_in=0.01, fade_out=0.12)

    turn1 = loud_window(os.path.join(EP1_RAW, "s8_paper.mp3"), 0.55)
    place(buf, turn1, T_TURN1, gain_for(db(turn1), narr_peak, -16), -0.15,
          fade_in=0.01, fade_out=0.08)

    turn2 = loud_window(os.path.join(EP1_RAW, "s8_paper.mp3"), 0.45,
                        offset_frac=0.30)
    place(buf, turn2, T_TURN2, gain_for(db(turn2), narr_peak, -16), -0.10,
          fade_in=0.01, fade_out=0.10)

    thud = load(os.path.join(EP5_RAW, "cup.mp3"), "lowpass=2000,highpass=90")
    place(buf, thud[: int(0.6 * SR)], T_SETDOWN,
          gain_for(db(thud), narr_peak, -15), +0.10, fade_in=0.005, fade_out=0.30)
    settle = loud_window(os.path.join(EP1_RAW, "s8_paper.mp3"), 0.15,
                         offset_frac=0.62)
    place(buf, settle, T_SETDOWN + 0.36,
          gain_for(db(settle), narr_peak, -18), 0.0, fade_out=0.10)

    # ---------------- sum, limit, write ----------------
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
