# Ep 6 — SFX + score plan (cold open, 00:00–01:43)

**Show:** The Discovery of India, Hindi mein · **Narrator:** Asha (voice: Fola)
**Scene:** Fatehpur Sikri, late 16th century. A red-sandstone courtyard hall, high jharokhas cutting slant light through dust. The darbar is full — amirs, pandits, maulvis — and in the middle, strangers in black coats: Portuguese Jesuits, presenting a thick printed Bible. Akbar takes it, turns pages, thanks them, sets it aside. Nobody asks how it was printed. Three hundred years later Nehru stops at this moment in a jail.
**Style:** Same house style as Ep 1 and Ep 3: a BBC history documentary, not a radio drama. Sparse, dry, literal. Score = **one drone instrument only** (tanpura), no melody, no percussion, exactly one swell. Only the cold open gets sound; from **01:43 to the end of the episode there is nothing under the voice.**

Level convention (as Ep 1/Ep 3): narration mastered to **-16 LUFS integrated**. "dB under voice" = the cue's short-term loudness relative to the voice at that moment.
- **Effects: 12–16 dB under the voice.** Every spot event and the summed bed land inside -12…-16.
- **Score: 2–4 dB below the effects** playing at the same moment (-15 ceiling at the swell); where no effects play (the coda, 01:29–01:42) it stays at **-20**.

Cue times are on the **tightened narration timeline** (`ep06/c01_t.wav`; transcript `ep06/c01_t.whisper.json`).

---

## 1. Cue table

IDs: **B** = bed, **S** = spot effect, **M** = score. Pan: L/R % from centre; voice dead centre.

| # | Time (MM:SS.s) | Narration line | Cue | Entry / exit | Level | Pan | Fades |
|---|---|---|---|---|---|---|---|
| 1 | 00:00.0 → | दूपेहर है, पतेपुर सिक्रे… | **B1** still-warm hall air: static, dry, no birds, no wind | Starts with the first word — scene already in progress | -16 | centre, narrow | In: 1.5 s |
| 2 | 00:14.6 → 00:17.1 | दर्भार भरा है, आमीर, पन्टित, मोल्वी | **B2** distant darbar murmur joins: wide, soft, no intelligible words | Answers the line: the hall was still, now it is full | B2 layer -18 | wide | In: 2.5 s |
| 3 | 00:17.85 → 00:18.8 | (gap before अजनबी) | **S1** two or three soft footfalls on stone — the strangers walking in | Sits in the gap; clear of "अजनबी काले चोगो" | -16 | R 35% | In: hard. Out: natural |
| 4 | 00:22.7 → 00:23.4 | (gap after पादरी) | **S2** cloth-and-paper: the wrapped book handed over | In the 0.8 s gap between the priests and "वो एक तोग्वा पेष" | -16 | centre-left, L 15% | In: hard. Out: natural |
| 5 | 00:29.1 → 00:32.0 | बाच्छा अगबर उसे हाथ में लेते हैं, भारी है | **B2 stir** — the hall lifts slightly as the book changes hands | Rises on "हाथ में लेते हैं", holds under the line | B2 → -16 | — | Up: 2 s |
| 6 | 00:32.95 → 00:33.5 | वो पन्ना पलडते हैं | **S3** one heavy page turn | Starts on "पलडते" — deliberate word overlap (documented) | -16 | centre | In: hard. Out: natural |
| 7 | 00:33.46 → 00:33.95 | (gap before फिर तुस्रा) | **S4** a second page turn, shorter | In the 0.54 s gap, must clear "फिर" | -16 | centre | In: hard. Out: 100 ms |
| 8 | 00:35.2 → 00:36.7 | अब दियान देजे… | **B2 hush** — the murmur drops; everyone leans in to look | The hall goes quiet to hear the printed letters | B2 → -22 | — | Down: 1.5 s |
| 9 | 00:45.9 → 00:63.1 | योरोप में आसी किताब… → सब भहस करते हैं | — (B1 + very low B2) | Keep clear: this is the portrait of Akbar and his darbar | B1 -16, B2 -22 | — | — |
| 10 | 00:63.1 → 00:66.4 | और फिर भी, अखबर किताब बन्द करते हैं | — (no sound for closing) | The action is in the voice; illustrating it would tip into drama | — | — | — |
| 11 | 00:70.4 → 00:71.1 | (gap after रहती जाते है) | **S5** a heavy book set down: one dull thud with a little paper settle | In the 0.76 s gap, before "एक चोटा सबाल" | -15 | L 10% | In: hard. Out: 300 ms |
| 12 | 00:71.1 → 00:75.1 | एक चोटा सबाल हवामे लटकर है जाते है… | **M1 score enters** (tanpura drone, see §2) | The question starts hanging; the drone arrives with it | M1 → -18 | centre | In: 4 s |
| 13 | 00:74.3 → 00:76.6 | कोई उसे जुबान पर नहीं लाता | **B2 out, M1 begins its swell then leaves** | Both must be gone before the question | B2 → -∞ (2.3 s); M1 peaks -15 at 76.4 then → -∞ by 76.9 | — | see §2 |
| 14 | 00:76.94 → 00:79.0 | **ये बनी कैसे?** | — **B1 only** | **The thesis line of the episode.** No score, no crowd, no spot cue | B1 -16 | — | — |
| 15 | 00:79.5 → 00:88.7 | कोई चापा काना नहीं… → अगले कामपर चला जाता है | — B1 continues, alone | Field-less equivalent of Ep 3's "B1 stays": the hall's air only | B1 -16 | — | — |
| 16 | 00:88.0 → 00:88.9 | (under अगले कामपर चला जाता है) | **B1 out** — the darbar moves on and the room's air leaves with it | Fades under the last words; after this, true silence | → -∞ | — | Out: 900 ms |
| 17 | 00:89.3 → 00:92.3 | तीन सो साल बाद… | **M1 coda**: the tanpura returns alone, lower than before. No bed — we have left the hall | Re-enters on "तीन सो साल बाद", carries the jail framing lines | **-20** | centre | In: 3 s |
| 18 | 00:99.9 → 01:42.45 | (under बारत पीचे क्यो रहे गया) | **M1 out** | Fades over the last line, hard stop **01:42.45**, ≥0.45 s dead air before नमस्कार | → -∞ | — | Out: 2.5 s (log-ish) |
| 19 | 01:42.9 → | नमस्कार, मैं हु आशा… | — **clean voice** | No score tail, no bed, no whoosh — rest of episode stays clean | — | — | — |

**Spot-cue count: 6 distinct sounds and 6 events in 103 s.** One overlap (S3, on the word), everything else in a gap. After 01:42.9 nothing plays but Asha.

---

## 2. Score design (M1 only)

**Instrument:** tanpura drone — Pa–Sa–Sa–Sa loop, CC0, ≥60 s (reuse `ep03/sfx/raw_fs/tanpura.mp3`, the same source that passed in Ep 3). No melody, no second instrument: the swell here is done by M1's own level, so no shruti box is used — the cold open is 103 s and needs one gesture, not two.

EQ as before: high-pass 70 Hz, 3 dB scoop 1.5–3 kHz, low-pass 6 kHz. Loop seamlessly (tile ≥103 s).

| Time | M1 level | What happens |
|---|---|---|
| 00:00 → 01:11.1 | Off | The hall alone: air, murmur, paper, voices |
| 01:11.1 → 01:15.1 | → **-18** | Enters on "एक चोटा सबाल" over 4 s — the question starts to hang |
| 01:15.1 → 01:16.4 | -18 → **-15** | **The one swell:** rises with "कोई उसे जुबान पर नहीं लाता" |
| 01:16.4 → 01:16.9 | → **-∞** | Must drop out before "ये बनी कैसे?" — the question gets no music |
| 01:16.9 → 01:29.3 | Off | The question, its answers, the hall moving on |
| 01:29.3 → 01:32.3 | → **-20** | The coda. Lower because no effects play now; frames the jail |
| 01:32.3 → 01:39.9 | -20 | Holds under the framing lines |
| 01:39.9 → 01:42.45 | → **-∞** | Out under the last line; hard stop with dead air before नमस्कार |

**Rules:** never starts or ends on a stressed word; swells only at 01:15–01:17; no reverb; no score at all after 01:42.45.

---

## 3. Continuous beds (B1 + B2): hall air, darbar murmur

**B1 — the hall:** a still, warm-air bed. Source `b1_bed.mp3` (358 s, steady, no birdsong in it — checked: it is the same static bed used as Ep 1's heat bed), high-pass 120 Hz, low-pass 9 kHz. Narrow/stereo-wide ≤50%.
**B2 — the darbar:** `crowd.mp3`, a distant crowd recorded far off: soft murmur, no intelligible words, no PA, no applause. High-pass 150 Hz, low-pass 5 kHz so it reads as "outside the frame" and doesn't fight the consonants.

| Time | B1 | B2 | Summed bed | Movement |
|---|---|---|---|---|
| 00:00.0 | → -16 | — | -16 | Fades in over 1.5 s |
| 00:14.6 → 00:17.1 | -16 | -∞ → -18 | ≈ -14 | The hall fills with "दर्भार भरा है" |
| 00:29.1 → 00:31.1 | -16 | → -16 | ≈ -13 | **Stir**: the book changes hands |
| 00:35.2 → 00:36.7 | -16 | → -22 | ≈ -15 | **Hush**: everyone leans in |
| 00:36.7 → 01:14.3 | -16 | -22 | ≈ -15 | Hushed hall through the printed-letters passage |
| 01:14.3 → 01:16.6 | -16 | → -∞ | -16 | **The hall goes quiet** before the question |
| 01:16.9 → 01:28.0 | -16 | — | -16 | Air only, under the question and its answers |
| 01:28.0 → 01:28.9 | → -∞ | — | -∞ | **Out for good.** Nothing comes back except M1 |

Both sources need ≥110 s of seamless material — `b1_bed.mp3` (358 s) and `crowd.mp3` (177 s) both qualify; tile and truncate rather than looping audibly.

---

## 4. Where silence matters more than sound

1. **01:16.9 → 01:19.0, "ये बनी कैसे?"** The centre of the episode. Score and crowd are both gone; the line is asked over nothing but the hall's air. No sting, no drone, no murmur.
2. **01:42.45 → 01:42.9, the beat before नमस्कार.** Hard dead air after M1's stop, so the host intro arrives in a clean studio.
3. **01:10.4 → 01:11.1, "किताब एक तरफ रहती जाते है" → "एक चोटा सबाल".** The book-set-down cue lives here and nothing else does — one thud in a gap, no music under it.
4. **00:45.9 → 00:63.1, Akbar's portrait.** No footsteps, no fabric, no musical colour for "दर्म, जंग, मशीने". The narration does the work.
5. **01:28.0 → 01:29.3, after the hall moves on.** True silence between the room leaving and the score returning. Do not tighten or fill it.
6. **01:42.9 → end of episode.** Clean voice, always.

---

## 5. Sound list: search terms and sources

> **Licence note (as Ep 1/Ep 3):** Freesound **CC0 filter** or **Pixabay Content License** only. Check the licence per file. Never CC-BY-NC. No crowd recording with intelligible words or slogans. All sources below already exist in `ep01/sfx/raw_fs/` and `ep03/sfx/raw_fs/` — **no new download needed** unless a QC listen rejects one.

| ID | Sound | Source (already local) | What to pick / why |
|---|---|---|---|
| **B1** | Still hall air | `ep01/sfx/raw_fs/b1_bed.mp3` (358 s, steady) | Static warm air; no birds, no traffic |
| **B2** | Distant darbar murmur | `ep03/sfx/raw_fs/crowd.mp3` (177 s) | Wide, soft, far off, no intelligible words |
| **S1** | Footfalls on stone | `ep03/sfx/raw_fs/steps.mp3` | Two or three soft steps, no heels |
| **S2** | Wrapped book handed over | `ep01/sfx/raw_fs/s8_paper.mp3` | One cloth/paper movement, close |
| **S3/S4** | Page turns | `ep01/sfx/raw_fs/s8_paper.mp3` (two different 0.5 s slices) | Heavy old paper, single turns, no flutter |
| **S5** | Book set down | `ep05/sfx/raw_fs/cup.mp3` + 150 ms of `ep01/…/s8_paper.mp3` | A dull low thud after EQ (low-pass 2 kHz) + a whisper of paper. Not a slam |
| **M1** | Tanpura drone | `ep03/sfx/raw_fs/tanpura.mp3` | Same source as Ep 3; Pa–Sa–Sa–Sa, no tabla/vocals |

Reference only (not for publication): BBC searches `court ambience india`, `book page turn heavy`.

---

## 6. Mix notes

- **Ducking:** none (as Ep 1/Ep 3). Spot cues are placed by hand in gaps; only S3 deliberately overlaps its word, handled by level.
- **Levels:** ceiling -15/16 (S5/S2 family); bed -14 to -16; M1 -18 base, -15 at the single swell, -20 in the coda. With FX + score on, integrated loudness of 00:00–01:43 must rise by roughly what Ep 3's approved mix showed (≈ +4.5 LU pre-master); the final `loudnorm I=-16` pass sets the episode standard.
- **EQ/space:** high-pass spot cues 80–100 Hz; cut 2–4 kHz by 2–3 dB on B2 so the murmur doesn't sit on Hindi consonants. No reverb anywhere. Distance comes from the recordings.
- **Stereo:** voice dead centre; the priests/steps right (they enter from the hall's side), the book/paper slightly left, crowd wide, score centre.
- **Timing:** all cue times are on `ep06/c01_t.wav`'s timeline (00:00.0 = first sample of "दूपेहर"). If the narration is re-rendered, re-spot at least: M1 entry (01:11.1), M1 swell-out (01:16.4), B2 exit (01:16.6), B1 exit (01:28.0), M1 hard stop (01:42.45).
- **Avoid:** melody, sitar/bansuri phrases, tabla, patriotic cues, risers/whooshes/booms, intelligible slogans, PA feedback, applause, period-radio crackle — and anything at all after 01:42.9.
- **QC:** listen once on phone speakers at low volume — if the murmur or drone is noticed before the words, pull it 2 dB. Then on headphones confirm 01:16.9–01:19 and 01:42.45–01:42.9 are truly silent, and that nothing at all plays under the host intro.

---

## 7. Kya sunayi dega

1. शुरू में बस एक शांत, गरम हॉल की हवा — फिर धीरे-धीरे दूर की भीड़ की गुनगुनाहट जुड़ जाएगी, जैसे दरबार भर गया हो.
2. पाद्रियों के कदम, लिपटी हुई किताब का हाथ बदलना, और दो भारी पन्नों के पलटने की आवाज़ — बस इतना ही, ज़्यादा नहीं.
3. जब अकबर किताब एक तरफ रखते हैं, तो एक भारी, धीमी सी थप्प — और उसके बाद तानपूरा धीरे से उठता है.
4. सवाल से ठीक पहले भीड़ और संगीत दोनों चले जाते हैं; "ये बनी कैसे?" सिर्फ हवा के ऊपर पूछा जाता है.
5. आख़िर में दरबार चला जाता है, सन्नाटा आता है, फिर धीमा तानपूरा नेहरू की जेल तक ले जाता है और नमस्कार से पहले बिल्कुल ख़ामोश हो जाता है.
