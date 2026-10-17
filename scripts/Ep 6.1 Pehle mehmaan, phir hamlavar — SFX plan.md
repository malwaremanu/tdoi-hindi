# Ep 6.1 — SFX plan (cold open)

Scope: `## Cold open` se ident tak (chunk `c01`). 350 narration words — 253 unme ident se
pehle, aur wahi 253 words is plan mein score hote hain. Is episode ka baaki sab kuch
(`Ab tak`, B1–B10, `Aaj ke hisaab se`, Outro) **dry narration** hai: koi bed, koi cue,
koi score nahi.

House convention wahi hai (Ep 3 / Ep 4.1 / Ep 6): narration anchor hai, har bed uske neeche
baithta hai, host intro saaf (dry) hai, scene ka ek hi score-swell hai, aur aakhri bed cut
body se pehle ek sannate ka pocket chhodta hai.

**Anchor note.** `ep06_1/c01.txt` abhi maujood nahi hai, isliye saare `phrase` values
ko is plan ke liye Devanagari mein likha gaya hai (script ke Roman cold open ka
transliteration, baaki episodes ke Devanagari narration wale spelling-dhang mein —
`बगदाद`, `ख़लीफ़ा हारूँ-अल्-रशीद`, `मानक`, `वैद्य`, `रेगिस्तान`). Mixer `norm()` vowel-sign,
nukta aur anusvara gira kar consonant-skeleton par `difflib` ratio ≥ 0.7 se match karta hai,
to chhote spelling-fark se anchor nahi tootega. Jab `c01.txt` bane, ek baar
`mix_from_plan.py --check-only` chalane par har anchor ka time nikal aayega; neeche har
phrase ke saath uski jagah bhi likhi hai, taaki badlaav turant pakda jaaye.

Doosri note: `points` (dB envelope) **layer ke apne shuru se** gine gaye hain — mixer ka
`env()` t = 0 se interpolate karta hai. (Ep 4.1 ki file mein score ke points absolute
seconds mein the, jis se wo envelope 0..21 s par -60 dB par atak jaata tha; yahan wo galti
nahi dohrayi gayi.)

## Cast (source files)

| id | file | kya hai |
|---|---|---|
| AIR | `ep02/sfx/raw_fs/air.mp3` | sookhi, garm hawa (bed) |
| WIND | `ep03/sfx/raw_fs/wind.mp3` | ret wali gritty hawa (bed, safar par +2 dB) |
| MAHAL | `ep01/sfx/raw_fs/b1_bed.mp3` | mahal ka room tone (raat ka andar ka hissa) |
| CROWD | `ep03/sfx/raw_fs/crowd.mp3` | door ki bheed ki gunjan (bazaar, aur mashhoor baat) |
| PAPER | `ep01/sfx/raw_fs/s8_paper.mp3` | pothiyan / sookhi jadiyan lapetna |
| STEPS | `ep03/sfx/raw_fs/steps.mp3` | patthar aur dhool par kadam (hakeem; oont ke qadam) |
| WICKER | `ep02/sfx/raw_fs/wicker.mp3` | door ki khidki ki chhitak (creak) |
| LATCH | `ep01/sfx/raw_fs/s6_latch.mp3` | pittal ke dabe ki kilkari |
| CUP | `ep05/sfx/raw_fs/cup.mp3` | halki dhaatu ki tik (katora mez par) |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | score — ek hi instrument, ek hi swell |
| synth | `synth:gust` | sookhi hawa ka jhonka (mix script mein banta hai) |

## Cue table

Id: **A** = bed, **B** = spot cue, **M** = score, **D** = duck, **S** = silence.
`lands on the phrase` column mein wo Devanagari phrase hai jiske **aakhri shabd** par cue
baithti hai (mixer ka anchor); timing narration ke word-timing se aati hai, isliye take
dobara render hone par bhi cue apni line par hi rehti hai. Approx times 3.12 shabd/second
ke hisaab se hain (sirf QC ke liye).

| id | cue | sound | lands on the phrase | level | pan | fades |
|---|---|---|---|---|---|---|
| A1 | sookhi garm Baghdad ki hawa — scene ke pehle shabd se | AIR | `start: 0.0`, `end: नमस्कार` | -25 dB | centre | in 2.5 s, out 2.0 s (ident se 0.25 s pehle) |
| A2 | ret wali gritty hawa | WIND | `start: 0.0`, `end: नमस्कार` | -27 dB (safar par -25) | centre | in 2.5 s, out 2.0 s |
| A3 | mahal ka room tone — "raat hai" se Manak ke nikalne tak | MAHAL | `महल के अंदर` → `वो निकल पड़ता` | -27 dB | centre | in 2.0 s, out 2.0 s |
| B1 | galiyon ki bheed (Arabi, Farsi, door ke desh) | CROWD (hp 180 / lp 4500) | `अरबी फ़ारसी` | -23 dB | +0.30 | in 0.7 s, out 1.6 s, 6.0 s |
| B2 | bazaar mein bikti pothiyan (Yunani + Sanskrit) | PAPER (hp 300 / lp 6000) | `बाज़ार में यूनानी पोथियाँ` | -22 dB | -0.30 | in 0.02 s, out 0.25 s, 1.6 s |
| B3 | hakeem aate-jaate hain — patthar par dheere kadam | STEPS (hp 100 / lp 5000) | `हकीम आते` | -21 dB | -0.30 | in 0.05 s, out 0.35 s, 2.6 s |
| B4 | door kahin khidki ki halki chhitak | WICKER (hp 200 / lp 3500) | `वज़ीर सोचते` | -24 dB | +0.45 | in 0.03 s, out 0.40 s, 1.4 s |
| B5 | shehar mein mashhoor baat (bheed, ab door aur dheemi) | CROWD (hp 200 / lp 4000) | `एक बात मशहूर` | -24 dB | +0.20 | in 1.2 s, out 1.8 s, 5.0 s |
| B6 | Manak ka saaman bandhna (pothiyan, sookhi jadiyan) | PAPER (hp 150 / lp 3500) | `कुछ सूखी जड़ियाँ` | -21 dB | -0.25 | in 0.02 s, out 0.30 s, 1.8 s |
| B7 | pittal ke dabe ki kilkari | LATCH (hp 180 / lp 4500) | `पीतल का डिब्बा` | -24 dB | -0.35 | in 0.005 s, out 0.15 s, 0.7 s |
| B8 | bahar nikla — sookhi hawa ka jhonka (synth) | `synth:gust` | `निकल पड़ता` | -24 dB | +0.35 | in 0.8 s, out 1.2 s, 3.5 s |
| B9 | oont ke qadmon ki dheemi thapak — ret par, patthar par | STEPS (hp 80 / lp 4000) | `नदियाँ हफ़्तों का रास्ता` | **-20 dB** (scene ka sabse uncha) | +0.25 | in 0.4 s, out 0.9 s, 3.2 s |
| B10 | ilaj shuru — pittal ka katora mez par | CUP (hp 150 / lp 6000) | `इलाज शुरू करता` | -23 dB | -0.35 | in 0.01 s, out 0.20 s, 1.0 s |
| M1 | score: tanpura | TANPURA | `कहानी उस धर्म के आने` → `और वहीं रह गया` | -25 dB, swell par -22 dB | centre | in 2.0 s, out 2.7 s (dekhiye §2) |
| D1 | **ek hi duck** — naam akela utre | beds 0.3 par | `नाम भारत का` | gain 0.30, pre 1.2 s, post 2.2 s | — | — |
| S1 | "khalifa theek ho jaate hain" — sirf beds | — | `ख़लीफ़ा ठीक हो जाते हैं` | koi cue nahi | — | — |
| S2 | "wo Baghdad mein bas jaata hai" — sirf beds + tanpura | — | `बगदाद में बस जाता है` | koi cue nahi | — | — |
| S3 | sannata — ident se pehle (score pehle hi ghul chuka hota hai) | — | `और वहीं रह गया` ke baad | ident ka pehla shabd sannate mein girta hai; body se pehle ka gap 1.3 s | — | — |

**Spot cues: 10 (B1–B10), poore 88 second mein.** Koi cue ident ke paar nahi jaata; koi cue
do beat ko chhoota nahi (har cue apni hi line par shuru aur khatam hoti hai). 4.1 ke
`fallback_at` ki tarah har cue ke saath seconds ka safety net bhi JSON mein hai.

## 1. Score (M1 — ek hi instrument, ek hi swell)

Instrument: tanpura loop (Pa–Sa–Sa–Sa), koi melody nahi, koi tabla/bansuri nahi, reverb
nahi. Filter: highpass 70 Hz, lowpass 6 kHz. Base level **-25 dB**, aur sirf ek baar
**-22 dB** tak uthata hai.

| kahan | M1 level | kya hota hai |
|---|---|---|
| `पर ध्यान दीजिए` se pehle | off | Poore Baghdad hisse mein koi score nahi — sirf hawa, mahal, aadmi |
| `कहानी उस धर्म के आने` (= "us dharm ke aane ki shuruat hai") | -25 dB (in) | Tanpura enters: kahani dharm ki kahani ban jaati hai — S02/S03 ka seam |
| ~8.5 s aage: "ek beemar aadmi hai, aur ek vaidya" | **-22 dB** | **Wahi ek swell** — cold open ka apna verdict |
| "aur wahin reh gaya" | -25 → -60 dB | Swell ke baad ghul jaata hai, koi tail nahi |
| `नमस्कार` | out | Score ident ke pehle shabd se ~0.4 s pehle poori tarah gayab; host intro dry |

Niym: swell ek hi baar, aur wo bhi zyada se zyada 3 dB (relative) — score kabhi -22 dB se
upar nahi jaata, aur narration ke phrase ke aar-paar kuch nahi jaata. (Score ki lambai
anchor se aati hai: ~74.6 s par enters, ~87.9 s par khatam — koi absolute second
hard-code nahi kiya gaya.)

## 2. Kahan chup rehna hai

Sannata yahan awaaz se zyada kaam karta hai:

1. **"Aur wo naam Bharat ka hai."** — Yahi scene ka pehla bada pal hai aur yahan ek bhi cue
   nahi hai. Sirf ek duck (D1) hai: teen beds 0.30 par gir jaate hain, to naam akela girta
   hai. Uske baad hi shehar ki gunjan (B5) uthhti hai — awaaz naam ke *baad* aati hai.
2. **"Khalifa theek ho jaate hain."** — Ek line, koi cue nahi. B1–B4 wale sab sounds band
   ho chuke hain; bimaari ka poora shor chup ho jaata hai. Koi "recovery sting" nahi.
3. **"Wo Baghdad mein bas jaata hai…"** — Manak ke rukne par koi cue nahi: sirf beds aur
   (aage) tanpura. Rukna ek chup ka faisla hai, uske liye koi impact nahi.
4. **"Yahan koi fauj nahi hai. Koi talwar nahi hai."** — Yahi is episode ki spine hai; yahan
   jaan-boojh kar kuch nahi rakha. Na koi stab, na koi khanak, na koi low whoosh — chup hi
   "koi talwar nahi hai" kehti hai. Score bhi is waqt sirf -25 dB par baithta hai.
5. **Ident se pehle ka sannata, aur body se pehle ka pocket** — tanpura "aur wahin reh gaya"
   par hi ghul chuka hota hai, to namaskar ka pehla shabd sannate mein girta hai (~0.4 s ka
   poora khamosh beat), aur `नमस्कार` ke baad poora episode dry hai. Body (`## Ab tak`) se
   pehle ka gap 1.3 s ka rakha gaya hai (JSON: `dead_air.before_body_seconds`) — use chhota
   na karein; is episode mein us pocket ko koi sound cross nahi karta.

## 3. Levels, pan aur headroom

- Beds **-25 / -27 dB** (range -21…-27 ke andar), score **-25 dB** (swell par -22), spot cues
  **-20 … -24 dB**. Narration ke upar kuch bhi nahi baithta.
- Scene ka sabse uncha block **safar–Baghdad ka pahunchav** hai (B8 jhonka + B9 oont ke qadam
  + WIND ka +2 dB lift, ~44.5–48.6 s) aur wahi peak **-20 dB** hai. Is cold open mein koi
  fauj, koi hamla aur koi talwar nahi hai, isliye brief ki -16 dB ki chhoot jaan-boojh kar
  istemaal nahi ki gayi — sabse unchi cheez bhi ceiling se 4 dB neeche hai.
- **Pan:** voice aur beds/score dead centre (0.0). Kareeb ki foley thodi baayen (B2, B3, B6,
  B7, B10: -0.25 se -0.35), door aur chaudi cheezein daayen (B1 +0.30, B5 +0.20, B8 +0.35,
  B9 +0.25, khidki +0.45).
- **Duck** D1 aik hi baar: `नाम भारत का` par gain 0.30, pre 1.2 s, post 2.2 s — naame wali
  line apne dam par girta hai.

## 4. Sound list (exact paths)

| kaam | file |
|---|---|
| Baghdad ki sookhi hawa | `ep02/sfx/raw_fs/air.mp3` |
| ret wali gritty hawa | `ep03/sfx/raw_fs/wind.mp3` |
| mahal ka room tone | `ep01/sfx/raw_fs/b1_bed.mp3` |
| bazaar / mashhoor baat ki bheed | `ep03/sfx/raw_fs/crowd.mp3` |
| pothiyan, sookhi jadiyan | `ep01/sfx/raw_fs/s8_paper.mp3` |
| hakeem ke kadam, oont ke qadam | `ep03/sfx/raw_fs/steps.mp3` |
| door ki khidki ki chhitak | `ep02/sfx/raw_fs/wicker.mp3` |
| pittal ke dabe ki kilkari | `ep01/sfx/raw_fs/s6_latch.mp3` |
| katora mez par | `ep05/sfx/raw_fs/cup.mp3` |
| score | `ep03/sfx/raw_fs/tanpura.mp3` |
| hawa ka jhonka | `synth:gust` (mix script mein banta hai) |

Kuch bhi download nahi hua aur nahi karna hai; saare sources repo ke pool se hain. CROWD do
jagah aati hai (B1, B5) aur STEPS do jagah (B3, B9) — dono baar filter aur level badal kar,
taaki ek hi awaaz do jagah na lage. Koi crowd recording mein samajh aane wale shabd ya nara
nahi hai.

## 5. Kya sunayi dega

1. Shuru mein Baghdad ki sookhi garm hawa — aur thodi der se uske neeche patthar wale mahal
   ka sila hua sannata, jaise hum kisi band kamre mein aa gaye hon.
2. Galiyon ki door ki bheed, bazaar mein bikti kitaabon ki halki awaaz, phir patthar ke farsh
   par hakeem ke dheere kadam aur door kahin khidki ki chhitak.
3. "Aur wo naam Bharat ka hai" — yahan sab kuch ek pal ke liye dab jaata hai, aur naam akela
   girta hai; uske baad hi shehar ki gunjan wapas uthhti hai.
4. Manak ke haath mein pothiyan lapetne ki awaaz, pittal ke dabe ki ek chhoti kilkari, phir
   bahar ki hawa ka jhonka aur oont ke qadmon ki dheemi thapak — yahi scene ka sabse uncha
   hissa hai.
5. Raat ka mahal dheere se chup ho jaata hai, aur "us dharm ke aane ki shuruat hai" par
   tanpura baithta hai; "ek beemar aadmi hai, aur ek vaidya" — wahi ek swell — aur "aur wahin
   reh gaya" par sab ghul jaata hai.
6. Namaskar se pehle poora sannata; uske baad poora episode saaf aur dry.
