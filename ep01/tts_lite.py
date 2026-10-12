#!/usr/bin/env python3
"""Hindi audiobook chunk -> WAV via gemini-3.8-flash-lite-tts (voice Fola).

The skill's text_to_speech.py hardcodes gemini-3.8-flash-tts, whose free tier is
10 req/day and is already exhausted; flash-lite-tts has its own quota bucket.
Fola is the model voice — "Asha" is only the narrator persona in the script.
"""
import base64
import json
import re
import struct
import sys
import time
import urllib.error
import urllib.request

MODEL = "gemini-3.8-flash-lite-tts"
VOICE = "Fola"


def key():
    env = open("/home/itcell/.hermes/.env").read()
    return re.search(r"^GEMINI_API_KEY=(.*)$", env, re.M).group(1).strip()


def wav_wrap(pcm, rate):
    return (b"RIFF" + struct.pack("<I", 36 + len(pcm)) + b"WAVEfmt "
            + struct.pack("<IHHIIHH", 16, 1, rate, rate * 2, 2, 16)
            + b"data" + struct.pack("<I", len(pcm)) + pcm)


def synth(text):
    payload = {
        "contents": [{"parts": [{"text": text}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": VOICE}}},
        },
    }
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
        data=json.dumps(payload).encode(),
        headers={"x-goog-api-key": key(), "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=90) as r:
        d = json.load(r)
    part = d["candidates"][0]["content"]["parts"][0]
    inline = part.get("inlineData") or {}
    mime = (inline.get("mimeType") or "").lower()
    raw = base64.b64decode(inline.get("data") or "")
    if "wav" in mime:
        return raw
    rate = 24000
    m = re.search(r"rate=(\d+)", mime)
    if m:
        rate = int(m.group(1))
    return wav_wrap(raw, rate)


def main():
    src, out = sys.argv[1], sys.argv[2]
    text = open(src).read().strip()
    if not text:
        sys.exit(f"empty: {src}")
    last = None
    for attempt in range(1, 6):
        try:
            data = synth(text)
            open(out, "wb").write(data)
            print(f"OK {out} {len(data)}B")
            return 0
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")
            last = f"HTTP {e.code} {re.sub(r'\\s+',' ',body)[:180]}"
            print(f"  try{attempt} {last}")
            if e.code in (429, 500, 503):
                time.sleep(30 * attempt)
                continue
            break
        except Exception as e:
            last = f"{type(e).__name__}: {e}"
            print(f"  try{attempt} {last}")
            time.sleep(20)
    print(f"FAILED {src}: {last}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
