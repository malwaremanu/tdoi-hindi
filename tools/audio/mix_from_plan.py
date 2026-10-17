#!/usr/bin/env python3
"""Apply an episode's SFX plan (JSON) to its cold-open take.

  python3 tools/audio/mix_from_plan.py --workdir ep04_2 --chunk c01 \
      --plan "scripts/Ep 4.2 — SFX plan.json" [--out ep04_2/sfx/_c01_mixed.wav]

Anchor resolution: every cue names a phrase (a contiguous run of source words, in
Devanagari) and the mixer looks that phrase up in `<workdir>/<chunk>.align.json`
(produced by align_words.py), so the cue lands on the actual audio time of those words
no matter how the take was re-rendered. `--no-align` mixes at the plan's fallback
seconds instead (plan files may carry "fallback_at" for that).

The SFX layer is written next to the mix as `_c01_sfx_only.wav` for QC, and the resolved
cue times are saved to `sfx/cue_times.json` for the record.
"""
from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import subprocess
import sys
import unicodedata

import numpy as np

REPO = "/home/itcell/audiobooks/tdoi"
FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
SR = 48000
PEAK_HEADROOM = 3.0
rng = np.random.default_rng(7)


# ------------------------------------------------------------------ helpers
def sh(a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr[-1500:])


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
    db_ = np.interp(t, [p[0] for p in pts], [p[1] for p in pts])
    return 10 ** (db_ / 20.0)


def place(buf, seg, at, gain_db, pan=0.0, env_db=None, fade_in=0.02, fade_out=0.10):
    i = int(at * SR)
    if i < 0 or i >= len(buf):
        return
    seg = seg[: len(buf) - i]
    n = len(seg)
    g = 10 ** (gain_db / 20.0)
    e = env_db if env_db is not None else np.ones(n)
    fi, fo = int(fade_in * SR), min(int(fade_out * SR), n)
    if fi:
        e[:fi] *= np.linspace(0, 1, fi)
    if fo:
        e[-fo:] *= np.linspace(1, 0, fo)
    l = 1.0 if pan <= 0 else 1.0 + pan * 0.55
    r = 1.0 if pan >= 0 else 1.0 - pan * 0.55
    buf[i:i + n, 0] += seg * e * g * l
    buf[i:i + n, 1] += seg * e * g * r


def db(x):
    return 20 * np.log10(max(1e-9, float(np.max(np.abs(x)))))


def gain_for(cue_peak, narr_peak, level_db):
    return (narr_peak - (abs(level_db) - PEAK_HEADROOM)) - cue_peak


def loud_window(path, dur, extra="", offset_frac=None):
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


# ------------------------------------------------------------------ synth library
def brick_thud(dur=0.35, seed=0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    body = np.sin(2 * np.pi * 105 * t) * np.exp(-t * 26)
    click = rng.normal(0, 0.6, n) * np.exp(-t * 120)
    x = np.convolve(0.8 * body + 0.5 * click, np.ones(24) / 24, mode="same")
    return (x / max(1e-9, np.max(np.abs(x)))).astype(np.float32)


def sand_trickle(dur=2.5, grains=140):
    n = int(dur * SR)
    x = np.zeros(n, dtype=np.float32)
    for _ in range(grains):
        s = rng.integers(0, max(1, n - 2000))
        ln = int(rng.integers(300, 2200))
        g = rng.normal(0, 1, ln) * np.exp(-np.linspace(0, 6, ln))
        x[s:s + ln] += (g * rng.uniform(0.3, 1.0)).astype(np.float32)
    x = x - np.convolve(x, np.ones(200) / 200, mode="same")
    return (x / max(1e-9, np.max(np.abs(x)))).astype(np.float32)


def rain(dur=10.0):
    n = int(dur * SR)
    hiss = rng.normal(0, 1, n)
    hiss = np.convolve(hiss, np.ones(8) / 8, mode="same") - \
        np.convolve(hiss, np.ones(160) / 160, mode="same")
    drops = np.zeros(n, dtype=np.float32)
    for _ in range(int(dur * 55)):
        s = rng.integers(0, max(1, n - 900))
        ln = int(rng.integers(90, 600))
        drops[s:s + ln] += (rng.normal(0, 1, ln) * np.exp(-np.linspace(0, 8, ln))).astype(np.float32)
    x = hiss.astype(np.float32) * 0.8 + drops * 0.5
    x = x * (1.0 + 0.12 * np.sin(2 * np.pi * 0.16 * np.arange(n) / SR))
    return (x / max(1e-9, np.max(np.abs(x)))).astype(np.float32)


def river_wash(dur=8.0):
    n = int(dur * SR)
    x = np.convolve(rng.normal(0, 1, n), np.ones(90) / 90, mode="same")
    x = x * (1.0 + 0.35 * np.sin(2 * np.pi * 0.22 * np.arange(n) / SR + 1.1))
    return (x / max(1e-9, np.max(np.abs(x)))).astype(np.float32)


def gust(dur=3.0):
    n = int(dur * SR)
    x = np.convolve(rng.normal(0, 1, n), np.ones(60) / 60, mode="same")
    swell = np.hanning(n) ** 0.5
    x = x * swell
    x = x - np.convolve(x, np.ones(400) / 400, mode="same")
    return (x / max(1e-9, np.max(np.abs(x)))).astype(np.float32)


def low_tone(dur=2.5, hz=70.0):
    t = np.arange(int(dur * SR)) / SR
    x = np.sin(2 * np.pi * hz * t) * np.hanning(len(t)) ** 0.7
    x += 0.3 * np.sin(2 * np.pi * hz * 2 * t) * np.hanning(len(t)) ** 0.7
    return (x / max(1e-9, np.max(np.abs(x)))).astype(np.float32)


def stone_scrape(dur=1.2):
    n = int(dur * SR)
    x = np.convolve(rng.normal(0, 1, n), np.ones(8) / 8, mode="same")
    x = x - np.convolve(x, np.ones(120) / 120, mode="same")
    x = x * (1.0 + 0.5 * np.sin(2 * np.pi * 9 * np.arange(n) / SR))
    x *= np.hanning(n) ** 0.4
    return (x / max(1e-9, np.max(np.abs(x)))).astype(np.float32)


SYNTH = {"brick_thud": brick_thud, "sand_trickle": sand_trickle, "rain": rain,
         "river_wash": river_wash, "gust": gust, "low_tone": low_tone,
         "stone_scrape": stone_scrape}


def resolve_sound(spec, cue):
    """spec: 'file' path (repo-relative) or 'synth:<name>'."""
    if spec.startswith("synth:"):
        name = spec.split(":", 1)[1]
        dur = float(cue.get("synth_seconds", 0) or 0)
        fn = SYNTH[name]
        return fn(dur) if dur else fn()
    return load(os.path.join(REPO, spec), cue.get("filter", ""))


# ------------------------------------------------------------------ anchors
def norm(w):
    w = unicodedata.normalize("NFC", w).lower()
    w = re.sub(r"[^\w\u0900-\u097F]", "", w).replace("ँ", "ं")
    return re.sub(r"[\u093E-\u094D\u0901\u0902]", "", w)


def find_phrase(align, phrase, occurrence=1):
    """Time of the LAST word of `phrase` (contiguous source words) in the aligned take."""
    A = [norm(r["w"]) for r in align]
    P = [norm(w) for w in phrase]
    if not P:
        return None
    hits, seen = [], 0
    for i in range(len(A) - len(P) + 1):
        ok = True
        for a, p in zip(A[i:i + len(P)], P):
            if difflib.SequenceMatcher(None, a, p, autojunk=False).ratio() < 0.7:
                ok = False
                break
        if ok:
            seen += 1
            if seen == occurrence:
                hits.append(align[i + len(P) - 1])
                break
    return float(hits[0]["e"]) if hits else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--chunk", default="c01")
    ap.add_argument("--plan", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--no-align", action="store_true")
    args = ap.parse_args()

    plan = json.load(open(args.plan, encoding="utf-8"))
    work = args.workdir if os.path.isabs(args.workdir) else os.path.join(REPO, args.workdir)
    sfx_dir = os.path.join(work, "sfx")
    os.makedirs(sfx_dir, exist_ok=True)

    align_path = os.path.join(work, args.chunk + ".align.json")
    align = json.load(open(align_path, encoding="utf-8")) if os.path.exists(align_path) else []

    src = os.path.join(work, args.chunk + ".wav")
    norm_wav = os.path.join(sfx_dir, f"_{args.chunk}_norm.wav")
    sh([FF, "-y", "-i", src, "-af", "dynaudnorm=f=200:g=5:p=0.95,aresample=48000",
        "-ac", "1", "-ar", str(SR), norm_wav])
    x = load(norm_wav)
    n = len(x)
    narr_peak = db(x)
    total = n / SR
    print(f"narration {total:.1f}s peak {narr_peak:.1f} dBFS  alignments "
          f"{'yes' if align else 'no'}", flush=True)

    buf = np.zeros((n, 2), dtype=np.float64)
    place(buf, x, 0.0, 0.0, 0.0, fade_in=0.0, fade_out=0.0)
    resolved = {}

    def anchor_time(rec):
        if not args.no_align and align and rec.get("phrase"):
            t = find_phrase(align, rec["phrase"], int(rec.get("occurrence", 1) or 1))
            if t is not None:
                return t
        return rec.get("fallback_at")

    # ---- beds / score (looping layers with dB envelopes) -------------------
    for layer in plan.get("beds", []) + plan.get("score", []):
        start = anchor_time(layer) if layer.get("phrase") else float(layer.get("start", 0.0))
        end = float(layer.get("end", total))
        if layer.get("end_phrase"):
            t = find_phrase(align, layer["end_phrase"], int(layer.get("end_occurrence", 1) or 1)) \
                if (align and not args.no_align) else None
            end = (t if t is not None else float(layer.get("end_fallback", total))) \
                + float(layer.get("end_offset", 0.0))
        elif layer.get("end_phrase"):
            end = float(layer.get("end_fallback", total)) + float(layer.get("end_offset", 0.0))
        end = max(start + 0.5, min(end, total))
        ln = int((end - start) * SR)
        seg = resolve_sound(layer["sound"], layer)
        if len(seg) < ln:
            seg = np.tile(seg, ln // max(1, len(seg)) + 2)
        seg = seg[:ln]
        pts = [(float(p[0]), float(p[1])) for p in layer.get("points", [])]
        if pts:
            e = env(pts, ln)
            if float(layer.get("offset", 0.0)):
                pass
        else:
            e = env([(0, -60), (min(2.0, (end - start) / 4), 0),
                     (max(0.1, end - start - 1.2), 0), (end - start, -60)], ln)
        g = gain_for(db(seg), narr_peak, float(layer.get("level_db", -24)))
        pan = float(layer.get("pan", 0.0))
        fi = 0.0 if pts else 0.02
        fo = 0.0 if pts else 0.10
        place(buf, seg, start, g, pan, e, fi, fo)
        resolved[layer.get("id", layer["sound"])] = round(start, 2)
        print(f"  layer {layer.get('id', layer['sound'])}: {start:6.2f}-{end:6.2f}s "
              f"at {layer.get('level_db')} dB", flush=True)

    # ---- spot cues ---------------------------------------------------------
    for cue in plan.get("cues", []):
        t = anchor_time(cue)
        if t is None:
            t = float(cue.get("fallback_at", 0.0))
        t += float(cue.get("offset", 0.0))
        seg = resolve_sound(cue["sound"], cue)
        dur = cue.get("seconds")
        if dur:
            seg = seg[: int(float(dur) * SR)]
        g = gain_for(db(seg), narr_peak, float(cue.get("level_db", -20)))
        place(buf, seg, t, g, float(cue.get("pan", 0.0)), None,
              float(cue.get("fade_in", 0.01)), float(cue.get("fade_out", 0.12)))
        resolved[cue.get("id", cue["sound"])] = round(t, 2)
        print(f"  cue {cue.get('id', cue['sound'])}: {t:6.2f}s "
              f"{os.path.basename(cue['sound'])} at {cue.get('level_db')} dB", flush=True)

    # ---- duck windows ------------------------------------------------------
    duck = np.ones(n)
    for d in plan.get("duck", []):
        t = anchor_time(d)
        if t is None:
            t = float(d.get("fallback_at", 0.0))
        a = int(max(0.0, t - float(d.get("pre", 1.2))) * SR)
        b = int(min(total, t + float(d.get("post", 2.0))) * SR)
        duck[a:b] = min(duck[a:b].min(), float(d.get("gain", 0.3)))
        print(f"  duck {t:6.2f}s -> {d.get('gain', 0.3)}", flush=True)
    buf *= duck[:, None]

    layer = buf - (duck[:, None] * x[:, None])
    lout = os.path.join(sfx_dir, f"_{args.chunk}_sfx_only.wav")
    layer.astype(np.float32).tofile(lout + ".f32")
    sh([FF, "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", lout + ".f32", lout])
    os.remove(lout + ".f32")
    print(f"sfx layer peak {db(layer):.1f} dBFS", flush=True)

    peak = np.max(np.abs(buf))
    if peak > 0.95:
        buf *= 0.95 / peak
    buf = np.tanh(buf * 1.05) / np.tanh(1.05)
    out = args.out or os.path.join(sfx_dir, f"_{args.chunk}_mixed.wav")
    buf.astype(np.float32).tofile(out + ".f32")
    sh([FF, "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", out + ".f32", out])
    os.remove(out + ".f32")
    json.dump(resolved, open(os.path.join(sfx_dir, "cue_times.json"), "w"), indent=1)
    print(f"wrote {out} {len(buf) / SR:.1f}s peak {db(buf):.1f} dBFS", flush=True)


if __name__ == "__main__":
    main()
