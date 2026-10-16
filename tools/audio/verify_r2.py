#!/usr/bin/env python3
"""Transcribe the Ep3 r2 takes with word timestamps + verify against source text."""
import json, os, re, sys, subprocess, unicodedata
import numpy as np
from faster_whisper import WhisperModel

FF = "/home/itcell/.hermes/tools/ffmpeg-9.0.1-linux-x64/bin/ffmpeg"

def load16k(path):
    """Decode to mono float32 @16 kHz via ffmpeg (PyAV in this venv is incompatible)."""    
    raw = path + ".s16"
    subprocess.run([FF, "-y", "-i", path, "-ac", "1", "-ar", "16000", "-f", "s16le", raw],
                   check=True, capture_output=True)
    x = np.fromfile(raw, dtype=np.int16).astype(np.float32) / 32768.0
    os.remove(raw)
    return x

D = "/home/itcell/audiobooks/tdoi/ep03/r2"
NAMES = ["c01", "c02", "c03", "c04", "c05", "c06"]

def norm(s):
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"[^\w\s\u0900-\u097F]", " ", s)
    return [w for w in s.split() if w]

model = WhisperModel("small", device="cpu", compute_type="int8")
report = []
for n in NAMES:
    wav = os.path.join(D, n + ".wav")
    src = open(os.path.join(D, n + ".txt"), encoding="utf-8").read()
    segs, info = model.transcribe(load16k(wav), language="hi", word_timestamps=True,
                                  vad_filter=True, beam_size=5)
    seg_list = []
    said_words = []
    for s in segs:
        d = {"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text}
        if s.words:
            d["words"] = [{"w": w.word, "s": round(w.start, 2), "e": round(w.end, 2)}
                          for w in s.words]
            said_words += [w.word for w in s.words]
        seg_list.append(d)
    json.dump({"source_words": len(src.split()), "segs": seg_list},
              open(os.path.join(D, n + ".whisper.json"), "w"), ensure_ascii=False)
    a, b = norm(src), norm(said_words and " ".join(said_words) or "")
    sa, sb = set(a), set(b)
    sim = (2 * len(sa & sb)) / (len(sa) + len(sb)) if (sa or sb) else 0.0
    report.append([n, len(a), len(b), round(sim, 3)])
    print(f"{n}: source {len(a)} | said {len(b)} | sim {sim:.3f}", flush=True)
print("summary:", json.dumps(report), flush=True)
