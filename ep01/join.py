#!/usr/bin/env python3
"""Concatenate the cold-open chunks into one narration file.

Sentences are read as separate takes, so they need a real breath between them —
0.55 s of silence. Each take is also peak-normalised first, because the TTS
returns slightly different levels per call and a single mix would let one loud
take dominate.
"""
import os
import struct
import subprocess
import sys

FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"
FP = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffprobe"
BASE = "/home/itcell/audiobooks/tdoi/ep01"
CHUNKS = os.path.join(BASE, "chunks")
OUT = os.path.join(BASE, "ep01_cold_open.mp3")
PAUSE = 0.55


def dur(path):
    r = subprocess.run([FP, "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(r.stdout.strip())


def main():
    names = sys.argv[1:] or ["co1", "co2", "co3", "co4", "co5", "co6"]
    tmpdir = os.path.join(BASE, "_norm")
    os.makedirs(tmpdir, exist_ok=True)

    # 1) peak-normalise every take to the same level, 48k mono
    normed = []
    for n in names:
        src = os.path.join(CHUNKS, n + ".wav")
        dst = os.path.join(tmpdir, n + ".wav")
        subprocess.run([FF, "-y", "-i", src, "-af",
                        "dynaudnorm=f=200:g=5:p=0.95,aresample=48000",
                        "-ac", "1", "-ar", "48000", dst],
                       capture_output=True, check=True)
        normed.append((n, dst))

    # 2) place each take AFTER the previous one finishes, plus a breath.
    # These are paragraph-length takes, so the offset must be cumulative —
    # a flat per-take delay overlaps them all on top of each other.
    inputs = []
    for _, p in normed:
        inputs += ["-i", p]
    filters = []
    offset = 0.0
    for i, (_, p) in enumerate(normed):
        d = dur(p)
        delay_ms = int(round(offset * 1000))
        filters.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=mono,"
                       f"adelay={delay_ms}|{delay_ms}[a{i}]")
        offset += d + PAUSE
    total = offset + 0.8
    labels = "".join(f"[a{i}]" for i in range(len(normed)))
    filters.append(f"{labels}amix=inputs={len(normed)}:normalize=0,"
                   f"atrim=0:{total:.3f},asetpts=PTS-STARTPTS[out]")

    tmp_wav = os.path.join(BASE, "_cold_open_raw.wav")
    subprocess.run([FF, "-y", *inputs, "-filter_complex", ";".join(filters),
                    "-map", "[out]", "-ar", "48000", "-ac", "1", tmp_wav],
                   capture_output=True, check=True)

    # 3) broadcast-ish loudness for spoken word, then mp3 for chat delivery
    subprocess.run([FF, "-y", "-i", tmp_wav,
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                    "-ar", "48000", "-ac", "2",
                    "-codec:a", "libmp3lame", "-q:a", "2", OUT],
                   capture_output=True, check=True)

    d = dur(OUT)
    size = os.path.getsize(OUT)
    print(f"wrote {OUT}")
    print(f"duration {d:.1f}s  size {size} bytes  takes={len(normed)}")


if __name__ == "__main__":
    main()
