# SFX plan brief (cold open) — how to write `scripts/Ep X.Y — SFX plan.md` + `.json`

The house sound design for this podcast is: **effects, ambience and score on the cold open
only; the rest of the episode is clean narration.**
Read these first, in this order:

1. `scripts/Ep 4.1 — SFX plan.md` — the human plan, the shape to copy.
2. `scripts/Ep 4.1 — SFX plan.json` — the machine plan for the same episode, the schema to copy.
3. Your episode's script: `scripts/Ep X.Y <title> — Script.md` — the section `## Cold open`
   (from `## Cold open` to the next `## ` heading) is the only scene you score.
4. The mixer that consumes your JSON: `tools/audio/mix_from_plan.py` (read the top of it; the
   available `synth:` recipes and the anchor logic are there).

## Deliverables (write exactly these two files, nothing else)

- `scripts/Ep X.Y — SFX plan.md` — write in Roman Hindi (like the episode scripts), with:
  the cue table (id | cue | sound | lands on the phrase | level under the voice | pan | fades),
  a short "score" section (exactly one swell), a "kahan chup rehna hai" section (where silence
  matters more than sound), the sound list with the exact file paths you use, and a closing
  4–6 line plain-Hindi "kya sunayi dega".
- `scripts/Ep X.Y — SFX plan.json` — the same plan, machine-readable, exactly the schema of
  the 4.1 file: `episode`, `cold_open_words`, `beds[]`, `cues[]`, `score[]`, `duck[]`, `dead_air`.
  Keys per layer: `id`, `sound`, optional `filter`, `seconds` or `synth_seconds`, `start` (beds)
  or `phrase` (cues/duck), `occurrence`, `offset`, `level_db`, `pan`, `fade_in`, `fade_out`,
  `points` (dB envelope for beds/score, `[[t_seconds, dB], …]`), `end`/`end_phrase`/`end_offset`.

## The rules that decide whether the mix sounds right

- **Anchors are phrases, never seconds.** Each cue's `phrase` is a contiguous run of words from
  your episode's cold open, **written in Devanagari** (the narration is Devanagari at mix time;
  a Roman phrase never matches). Keep them short (2–6 words) and pick words that occur once in
  the cold open — check with your own eyes. Add `"occurrence": N` when a phrase repeats.
  Always give a `fallback_at` in seconds as a safety net.
- **Levels under the voice** (mixer turns these into peaks, the voice is the reference):
  ambience beds −21 … −27 dB, foley/spot cues −18 … −24 dB, score/tanpura −22 … −26 dB,
  the scene's loudest block is allowed one cue at −16 dB. Nothing may sit above −16 dB.
- **Voice dead centre.** Pan foley slightly left (`−0.35 … −0.1`), distance/wide things right
  (`0.2 … 0.6`). Beds and score stay at `0.0`.
- **One swell only.** The score enters once, swells once and leaves; it must be out 0.25 s
  before the host intro line ("नमस्कार …").
- **Duck once, on the name/verdict moment**: `duck` with `pre` 1.0–1.5 s, `post` 2.0–2.5 s,
  `gain` 0.28–0.35, so the key line lands alone.
- **Where silence matters more than sound:** the plan's `dead_air.before_body_seconds`
  (1.0–1.5 s) plus at least two beats inside the cold open where you deliberately place no cue.
- **No cue crosses the host intro.** If a bed runs to the intro, end it on the phrase
  `["नमस्कार"]` with `end_offset: -0.25`.
- No more than ~12 spot cues, and every cue must be motivated by the line it lands on.

## Sound library (copy these exact paths / recipe names)

Ambience beds: `ep02/sfx/raw_fs/air.mp3` (dry air), `ep03/sfx/raw_fs/wind.mp3` (gritty wind),
`ep01/sfx/raw_fs/b1_bed.mp3` (room tone), `ep03/sfx/raw_fs/b1_village.mp3` (village bed),
`ep03/sfx/raw_fs/field.mp3` (open field), `ep02/sfx/raw_fs/drone.mp3`, `ep02/sfx/raw_fs/bass.mp3`
(sub swell — use `filter: "lowpass=200"`), `ep02/sfx/raw_fs/cello.mp3`, `ep03/sfx/raw_fs/sarangi.mp3`
(single bowed phrase), `ep03/sfx/raw_fs/tanpura.mp3` / `tanpura2.mp3`, `ep03/sfx/raw_fs/shruti.mp3`
(shruti-box drone).
Foley: `ep01/sfx/raw_fs/s1_dig.mp3`, `s1b_dig.mp3` (spades), `s2_gravel.mp3` (rubble),
`s3_stab.mp3` (hard impact), `s4_brush.mp3` (sweeping brush), `s5_crow.mp3` (crow),
`s6_latch.mp3` (latch/door), `s8_paper.mp3` (paper/scroll), `s8b_pen.mp3`, `s9_writing.mp3`,
`ep03/sfx/raw_fs/steps.mp3` (footsteps on dust), `ep03/sfx/raw_fs/door.mp3`, `crowd.mp3`
(crowd murmur — never intelligible words), `chuckle.mp3`, `ep02/sfx/raw_fs/engine.mp3`,
`ep02/sfx/raw_fs/wicker.mp3` (creaking/reed), `ep05/sfx/raw_fs/cup.mp3`, `liq.mp3`, `pour.mp3`.
Synthesised recipes (write `synth:<name>`): `brick_thud`, `sand_trickle`, `rain`, `river_wash`,
`gust`, `low_tone`, `stone_scrape`.

Prefer the repo pool over new downloads (licences are settled). You may not download anything.

## Hard constraints

- Write **only your two files**. Never touch another episode's files, the scripts, or any tool.
  Never run `git`.
- `phrase` values must be Devanagari. The `.md` and its cue-table prose may be Roman Hindi.
- Keep the JSON valid: no comments, no trailing commas, no `NaN`.
