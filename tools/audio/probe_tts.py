#!/usr/bin/env python3
"""Probe the TTS endpoint and print the REAL error body (voice errors come back
as 400 with a message; quota errors come back as 429) — the wrapper script only
surfaces the status code, which is not enough to tell them apart."""
import json
import re
import sys
import urllib.error
import urllib.request

def key():
    env = open("/home/itcell/.hermes/.env").read()
    return re.search(r"^GEMINI_API_KEY=(.*)$", env, re.M).group(1).strip()

voice = sys.argv[1] if len(sys.argv) > 1 else "Asha"
text = sys.argv[2] if len(sys.argv) > 2 else "नमस्ते।"

payload = {
    "contents": [{"parts": [{"text": text}]}],
    "generationConfig": {
        "responseModalities": ["AUDIO"],
        "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}},
    },
}
req = urllib.request.Request(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent",
    data=json.dumps(payload).encode(),
    headers={"x-goog-api-key": key(), "Content-Type": "application/json"},
    method="POST",
)
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.load(r)
    part = d["candidates"][0]["content"]["parts"][0]
    data = part.get("inlineData") or {}
    print(f"OK voice={voice} mime={data.get('mimeType')} bytes={len(data.get('data') or '')}")
except urllib.error.HTTPError as e:
    body = e.read().decode(errors="replace")
    print(f"HTTP {e.code}")
    print(body[:800])
except Exception as e:
    print(f"{type(e).__name__}: {e}")
