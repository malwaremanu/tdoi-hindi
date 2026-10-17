#!/usr/bin/env python3
"""Ep 4.1: join the mixed cold open with the clean body takes.

python3 join_ep4_1.py -> ep04_1/ep04_1_full_sfx.mp3 (+ ep04_1_coldopen_sfx.mp3)
"""
import os
import subprocess
import sys

FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
FP = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffprobe"
BASE = "/home/itcell/audiobooks/tdoi/ep04_1"
SFX = "/home/itcell/audiobooks/tdoi/ep04_1/sfx"
PAUSE = 1.4          # plan H1: dead-air pocket before the body
CO = os.path.join(SFX, "_c01_mixed.wav")
BODY = ["c02", "c03", "c04", "c05"]


def sh(a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr[-1500:])


def dur(p):
    r = subprocess.run([FP, "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", p], capture_output=True, text=True)
    return float(r.stdout.strip())


def main():
    norm = os.path.join(BASE, "_norm")
    os.makedirs(norm, exist_ok=True)
    layers = [(CO, True)]
    for n in BODY:
        src = os.path.join(BASE, n + ".wav")
        dst = os.path.join(norm, n + ".wav")
        if not os.path.exists(dst):
            sh([FF, "-y", "-i", src, "-af",
                "dynaudnorm=f=200:g=5:p=0.95,aresample=48000",
                "-ac", "2", "-ar", "48000", dst])
        layers.append((dst, True))

    inputs, filters, offset = [], [], 0.0
    for i, (p, _) in enumerate(layers):
        inputs += ["-i", p]
        d = dur(p)
        ms = int(round(offset * 1000))
        filters.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,"
                       f"adelay={ms}|{ms}[a{i}]")
        offset += d + PAUSE
    labels = "".join(f"[a{i}]" for i in range(len(layers)))
    filters.append(f"{labels}amix=inputs={len(layers)}:normalize=0,"
                   f"atrim=0:{offset + 0.8:.3f},asetpts=PTS-STARTPTS[out]")

    raw = os.path.join(BASE, "_full_sfx_raw.wav")
    sh([FF, "-y", *inputs, "-filter_complex", ";".join(filters),
        "-map", "[out]", "-ar", "48000", "-ac", "2", raw])

    out = os.path.join(BASE, "ep04_1_full_sfx.mp3")
    sh([FF, "-y", "-i", raw, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-ar", "44100", "-ac", "2", "-codec:a", "libmp3lame", "-q:a", "2", out])
    print(f"joined {dur(out):.1f}s -> {out}")

    # cold open only, for a quick listen
    co = os.path.join(BASE, "ep04_1_coldopen_sfx.mp3")
    sh([FF, "-y", "-i", CO, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-ar", "44100", "-ac", "2", "-codec:a", "libmp3lame", "-q:a", "2", co])
    print(f"cold open {dur(co):.1f}s -> {co}")


if __name__ == "__main__":
    main()