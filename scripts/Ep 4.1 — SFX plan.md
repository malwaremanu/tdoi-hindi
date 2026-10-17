# Ep 4.1 — SFX plan (cold open)

Cold open = `## Cold open` .. the three questions (472 narration words, chunk `c01`).
Signal chain and levels follow the house convention used for Ep 3 / Ep 5 / Ep 6:
narration is the anchor, every bed sits under it, the host intro is dry, and the last
bed cut leaves a dead-air pocket before the body starts.

## Cast (source files)
| id | file | what it is |
|---|---|---|
| AIR | `ep02/sfx/raw_fs/air.mp3` | dry, wide desert air (bed) |
| WIND | `ep03/sfx/raw_fs/wind.mp3` | wind with a little grit (bed) |
| DRONE | `ep02/sfx/raw_fs/drone.mp3` | low sustained tone (tension) |
| BASS | `ep02/sfx/raw_fs/bass.mp3` | sub-bass swell (earth rising / reveal) |
| SARANGI | `ep03/sfx/raw_fs/sarangi.mp3` | single bowed phrase (the name moments) |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | tanpura loop (coda under the questions) |
| DIG | `ep01/sfx/raw_fs/s1_dig.mp3` | spade into packed earth |
| DIG2 | `ep01/sfx/raw_fs/s1b_dig.mp3` | second dig stroke |
| GRAVEL | `ep01/sfx/raw_fs/s2_gravel.mp3` | gravel / rubble |
| BRUSH | `ep01/sfx/raw_fs/s4_brush.mp3` | brush sweep — used for the morning broom |
| CROW | `ep01/sfx/raw_fs/s5_crow.mp3` | one distant crow (city waking) |
| STEPS | `ep03/sfx/raw_fs/steps.mp3` | footsteps on dust |
| synth | generated in the mix script | brick thud, sand trickle, rain, river wash |

Synthesised cues are declared as such in the Sources of the script and in this plan.

## Cue table (anchors are phrase-locked; times are re-spotted from the whisper word
timings of the tightened `c01`, so they move with the narration)
| # | cue | sound | level | pan | envelope |
|---|---|---|---|---|---|
| A1 | "Ek shehar hai. Pakki eenton ka shehar." | AIR + WIND in | -25 dB | centre | 0.4 s fade in, holds under the whole scene |
| A2 | "Hawa chal rahi hai, aur saath ret laa rahi hai" | sand trickle (synth, high-passed) | -30 dB | L→R drift | 2.5 s, three slow grains |
| A3 | "Subah koi aurat aangan buhaarti hai" | BRUSH sweep ×2 | -22 dB | centre-left | 0.9 s each, 0.5 s apart |
| A4 | "Bachche gali mein khelte hain" | CROW (distant) | -32 dB | right, 60 % wet | single, 1.2 s |
| A5 | "zameen oopar uthne lagti hai" | BASS swell | -26 → -19 dB | centre | 6 s rise, no transient |
| B1 | "Wo purani deewar ke oopar ek nayi eent rakhta hai. Phir doosri. Phir teesri." | brick thud ×3 (synth) | -20 dB | centre | 0.35 s decay, thuds on "nayi eent", "doosri", "teesri"; each next thud 1.5 dB louder than the last |
| B2 | second/third generation lines | BRUSH + WIND small lift | -28 dB | centre | 4 s, wall keeps rising |
| C1 | "kuch log kudaal aur bursh lekar aate hain" | DIG + DIG2 + GRAVEL | -18 dB | centre | 3 strokes then rubble |
| C2 | "Neeche se deewarein nikalti hain" | BASS reveal + GRAVEL tail | -20 dB | centre | 3 s rise, dark |
| D1 | "Phir ek din khudai ruk jaati hai." | hard cut: dig bed out, wind only | — | — | cut on the word "ruk", 0.4 s of near-silence (wind -30 dB) |
| D2 | "baarish, aur sookhi ret wali hawa" | rain (synth, band-passed) | -27 dB | centre | in over 2 s, out over 3 s; WIND returns dry |
| E1 | "Doosri baar, ret hat chuki thi" (Nehru's two visits) | STEPS on dust ×4 | -30 dB | L→R | slow, walking away |
| F1 | "Is shehar ka naam hai Mohenjo-daro." | SARANGI single phrase + AIR dip | -23 dB | centre | name lands alone: beds duck to -32 dB for 1.6 s |
| F2 | "Us nadi ka naam yaad rakhiye: Sindhu." | river wash (synth, slow LFO) | -28 dB | centre | in 2 s, stays under the payoff line |
| G1 | "Namaskar, main hoon Asha…" | all beds out | — | — | hard out 0.25 s before "नमस्कार"; host intro is dry |
| G2 | "Aaj ka sawal ek hi hai…" (three questions) | TANPURA at -24 dB | -24 dB | centre | fades in after the first question, holds, then out on the last question |
| H1 | end of the questions → body | dead air | — | — | 1.4 s of silence, then the body's first word |

## Rules kept from the previous episodes
- The host intro and the three questions are never covered by a bed louder than -24 dB.
- The name moment (F1) is the only time the beds duck; nothing else competes with a name.
- The dig/rain block (C–D) is the scene's loudest passage; peak headroom 3 dB below full scale.
- No cue crosses a paragraph boundary: every cue starts and ends inside its own beat.
- Final mix target: -16 LUFS integrated, TP -1.5 dB, LRA 11; body stays dry (no SFX after the cold open).
