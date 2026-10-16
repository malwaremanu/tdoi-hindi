#!/usr/bin/env python3
"""Ep 3 (r2 rewrite) cold open: narration + bed + effects + tanpura score.

Same cue list, levels, pans and sound sources as tools/audio/mix_ep3_coldopen.py,
re-spotted against the tightened r2 narration (transcribed timings, see
ep03/r2/c01_t.whisper.json). Plan: scripts/Ep 3 — SFX plan.md.
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
COLD_END = 128.50          # buffer length; host intro starts at 127.84
PEAK_HEADROOM = 3.0

# ---- re-spotted anchors (seconds on the tightened narration timeline) ----
# Raw-take word timings minus the pauses tighten_coldopen.py removed (7 cuts,
# 2.75 s), cross-checked against ep03/r2/c01_t.whisper.json.
T_KITE = 6.10              # gap after "उत्तर भारत का एक गाँव"
T_CROWD_IN = 16.01         # "इस मैदान में लोग बैठे हैं"
T_GUST = 30.70             # "हवा में धूल है … धूप"
T_LOOK = 34.65             # "सब एक ही तरफ देख रहे हैं" — B2 hush + M1 in
T_CAR = 39.02              # "फिर दूर से धूल का एक लंबा बादल उठता है"
T_STOP = 45.42             # "गाड़ी रुकती है" — crunch on "रुकती"
T_DOOR = 48.55             # gap after "उतरता है", before "सिर पर सफ़ेद टोपी"
T_STAND = 54.92            # "भीड़ खड़ी हो जाती है" — S6 + the one swell begins
T_SHOUT = 58.45            # gap after "और फिर एक आवाज़ उठती है"
T_TEN = 59.90              # gap after "फिर दस"
T_ROAR = 60.78             # "फिर हज़ार" — roar onset, peak in the gap after it
T_CHANT = 62.28            # "भारत माता की जय" — dip under it, beat after
T_STEPS = 65.75            # gap after "मंच पर चढ़ता है"
T_SETTLE = 66.30           # "लोग इंतज़ार कर रहे हैं"
T_OUT = 74.00              # "पर वो भाषण शुरू नहीं करता" — B2 + M1 gone by 76.2
T_QUIET = 83.10            # B1 out, before "मैदान में सन्नाटा"
T_LAUGH = 89.25            # gap after "कोई हल्के से हँस देता है"
T_CODA = 92.00             # "साल है 1936" — score returns at -20
T_M1_STOP = 127.40         # hard stop, 0.44 s of dead air before "नमस्कार"


def sh(a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr[-1500:])
    return r


def load(path, extra=""):
    raw = path + ".f32"
    if extra:
        sh([FF, "-y", "-i", path, "-ac", "1", "-ar", str(SR), "-af", extra,
            "-f", "f32le", raw])
    else:
        sh([FF, "-y", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", raw])
    x = np.fromfile(raw, dtype=np.float32)
    os.remove(raw)
    return x


def env(points, n):
    pts = sorted(points, key=lambda p: p[0])   # np.interp needs sorted xp
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


def loud_window(path, dur, extra=""):
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
    src = os.path.join(BASE, "r2", "c01_t.wav")
    norm = os.path.join(SFX, "_r2c01_norm.wav")
    sh([FF, "-y", "-i", src, "-af", "dynaudnorm=f=200:g=5:p=0.95,aresample=48000",
        "-ac", "1", "-ar", str(SR), norm])
    x = load(norm)
    narr_peak = db(x)
    total = len(x)
    print(f"narration {total / SR:.1f}s  peak {narr_peak:.1f} dBFS")

    buf = np.zeros((total, 2), dtype=np.float64)
    place(buf, x, 0.0, 0.0, 0.0, fade_in=0.0, fade_out=0.0)

    # ---------------- B1: dry field / village heat ----------------
    b1 = load(os.path.join(RAW, "b1_village.mp3"), "highpass=120,lowpass=9000")
    if len(b1) < total + SR:
        b1 = np.tile(b1, int((total + SR) // len(b1)) + 1)
    b1 = b1[:int(T_QUIET * SR)]
    e1 = env([(0, -60), (1.5, 0), (T_QUIET - 0.5, 0), (T_QUIET, -60)], len(b1))
    place(buf, b1, 0.0, gain_for(db(b1), narr_peak, -16), 0.0, e1, 0.0, 0.0)

    # ---------------- B2: distant crowd, hush / stir / stand ----------------
    b2 = load(os.path.join(RAW, "crowd.mp3"), "highpass=150,lowpass=5000")
    need = int((T_OUT + 3) * SR)
    if len(b2) < need:
        b2 = np.tile(b2, int(need // len(b2)) + 1)
    b2 = b2[:int((T_OUT + 3) * SR)]
    e2 = env([(T_CROWD_IN, -60), (T_CROWD_IN + 2.5, -18), (T_LOOK, -18),
              (T_LOOK + 1.5, -22), (T_STOP, -22), (T_STOP + 2.0, -18),
              (T_STAND, -18), (T_STAND + 1.5, -15), (T_ROAR, -15),
              (T_ROAR + 0.6, -12), (T_ROAR + 1.6, -15), (T_ROAR + 2.0, -15),
              (T_ROAR + 3.4, -18), (T_SETTLE, -18), (T_SETTLE + 2.0, -18),
              (T_OUT, -18), (T_OUT + 2.2, -60)], len(b2))
    place(buf, b2, 0.0, gain_for(db(b2), narr_peak, -12), 0.0, e2, 0.0, 0.0)

    # ---------------- score M1: tanpura drone ----------------
    m1 = load(os.path.join(RAW, "tanpura.mp3"), "highpass=70,lowpass=6000")
    need = int(COLD_END * SR)
    if len(m1) < need:
        m1 = np.tile(m1, int(need // len(m1)) + 1)
    m1 = m1[:need]
    em = env([(T_LOOK, -60), (T_LOOK + 4.0, -18), (T_STAND, -18),
              (T_STAND + 3.0, -15), (T_STAND + 7.2, -15), (T_CHANT, -15),
              (T_CHANT + 0.3, -17), (T_CHANT + 1.3, -17),
              (T_CHANT + 1.6, -15), (T_CHANT + 2.0, -15),
              (T_CHANT + 3.2, -18), (T_OUT - 0.3, -18), (T_OUT + 2.2, -60),
              (T_CODA, -60), (T_CODA + 3.0, -20), (T_M1_STOP - 2.6, -20),
              (T_M1_STOP, -60)], len(m1))
    place(buf, m1, 0.0, gain_for(db(m1), narr_peak, -15), 0.0, em, 0.0, 0.0)

    # ---------------- score M2: shruti box, swell only ----------------
    m2 = load(os.path.join(RAW, "shruti.mp3"), "highpass=70,lowpass=6000")
    seg = m2[: int(11.5 * SR)]
    e2m = env([(0, -60), (3.0, -18), (T_CHANT - T_STAND, -18),
               (T_CHANT - T_STAND + 1.2, -20), (T_CHANT - T_STAND + 1.8, -60)],
              len(seg))
    place(buf, seg, T_STAND, gain_for(db(seg), narr_peak, -16), 0.0, e2m, 0.0, 0.0)

    # ---------------- spot effects ----------------
    kite = load(os.path.join(EP1_RAW, "s5_crow.mp3"), "lowpass=6000")
    place(buf, kite, T_KITE, gain_for(db(kite), narr_peak, -16), +0.40, fade_in=0.01)

    gust = loud_window(os.path.join(RAW, "wind.mp3"), 3.2)
    eg = env([(0, -60), (1.2, 0), (1.7, 0), (3.2, -60)], len(gust))
    place(buf, gust, T_GUST, gain_for(db(gust), narr_peak, -16), -0.30, eg, 0.0, 0.0)

    car = load(os.path.join(RAW, "car_dirt.mp3"))[: int(7.0 * SR)]
    ec = env([(0, -60), (1.6, -14), (6.3, -12), (7.0, -12)], len(car))
    place(buf, car, T_CAR, gain_for(db(car), narr_peak, -12), +0.55, ec, 0.0, 0.0)

    stop = loud_window(os.path.join(RAW, "car_dirt.mp3"), 0.9)
    place(buf, stop, T_STOP, gain_for(db(stop), narr_peak, -13), +0.20, fade_out=0.35)

    door = loud_window(os.path.join(RAW, "door.mp3"), 0.8)[: int(0.7 * SR)]
    place(buf, door, T_DOOR, gain_for(db(door), narr_peak, -14), +0.20)

    stand = loud_window(os.path.join(RAW, "crowd.mp3"), 1.4)
    es = env([(0, -60), (0.4, 0), (1.0, 0), (1.4, -60)], len(stand))
    place(buf, stand, T_STAND, gain_for(db(stand), narr_peak, -13), 0.0, es, 0.0, 0.0)

    shout = loud_window(os.path.join(RAW, "crowd.mp3"), 0.5, "highpass=300,lowpass=2500")
    place(buf, shout, T_SHOUT, gain_for(db(shout), narr_peak, -14), +0.10, fade_out=0.2)

    ten = loud_window(os.path.join(RAW, "crowd.mp3"), 1.0)
    et = env([(0, -60), (0.1, 0), (0.6, 0), (1.0, -60)], len(ten))
    place(buf, ten, T_TEN, gain_for(db(ten), narr_peak, -15), +0.15, et, 0.0, 0.0)

    roar_len = 7.2
    roar = loud_window(os.path.join(RAW, "crowd.mp3"), roar_len)
    d = T_CHANT - T_ROAR          # chant starts this far after the roar onset
    # peak in the gap after "फिर हज़ार", dip under the chant, one more beat, decay
    er = env([(0, -60), (0.4, 0), (d - 0.05, 0), (d + 0.05, -3),
              (d + 1.30, -3), (d + 1.45, 0), (d + 2.15, 0), (d + 3.40, -4),
              (roar_len - 1.6, -14), (roar_len, -60)], len(roar))
    place(buf, roar, T_ROAR, gain_for(db(roar), narr_peak, -12), 0.0, er, 0.0, 0.0)

    steps = load(os.path.join(RAW, "steps.mp3"))
    place(buf, steps[: int(0.6 * SR)], T_STEPS, gain_for(db(steps), narr_peak, -14),
          -0.10)

    chuck = load(os.path.join(RAW, "chuckle.mp3"))
    place(buf, chuck, T_LAUGH, gain_for(db(chuck), narr_peak, -16), -0.25,
          fade_out=0.15)

    # ---------------- sum, limit, write ----------------
    peak = np.max(np.abs(buf))
    if peak > 0.95:
        buf *= 0.95 / peak
    buf = np.tanh(buf * 1.05) / np.tanh(1.05)
    out = os.path.join(SFX, "_r2_c01_mixed.wav")
    buf.astype(np.float32).tofile(out + ".f32")
    sh([FF, "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", out + ".f32", out])
    os.remove(out + ".f32")
    print("wrote", out, f"{len(buf) / SR:.1f}s  peak {db(buf):.1f} dBFS")


if __name__ == "__main__":
    main()
