#!/usr/bin/env bash
# Generate TTS for every chunk, retrying patiently through Gemini free-tier 429s.
# Free-tier RPD resets at midnight Pacific, so this waits out long windows.
set -u
cd /home/itcell/audiobooks/tdoi/ep01/chunks
PY=/home/itcell/hermes-voice/.venv/bin/python
TTS=/home/itcell/.hermes/skills/media/gemini-text-to-audio/scripts/text_to_speech.py
VOICE="${VOICE:-Asha}"

for c in co1 co2 co3 co4 co5 co6 p1a p1b p1c p1d p1e p1f p1g; do
  [ -s "$c.wav" ] && { echo "$c already done"; continue; }
  for try in $(seq 1 40); do
    out=$($PY "$TTS" --engine tts --voice "$VOICE" "$c.wav" - < "$c.txt" 2>&1 | head -1)
    if echo "$out" | grep -q '^ok'; then
      echo "$c OK (try $try): $out"
      break
    fi
    echo "$c try $try failed: $out"
    sleep 45
  done
  [ -s "$c.wav" ] || echo "$c GAVE UP"
done
echo "--- FINAL STATE ---"
ls -la *.wav 2>/dev/null | awk '{print $9, $5}'
