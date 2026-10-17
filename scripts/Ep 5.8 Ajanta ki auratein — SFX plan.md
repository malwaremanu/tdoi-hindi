# Ep 5.8 — SFX plan (cold open)

Cold open = `## Cold open` .. `चलिए।` (21 para, **436 narration shabd**, chunk `c01`) — diya, gaar,
Ajanta ki auratein, aur phir wahi khaali jagah. House convention wahi hai: narration anchor hai,
har bed uske neeche baithta hai, host intro dry hai, aur aakhri bed cut ke baad body se pehle
sannata rehta hai.

- Anchors narration ke **Devanagari** shabd hain. `ep05_8/c01.txt` abhi repo mein nahi hai, isliye
  ye phrases `tools/audio/transliterate.py` wale house transliteration se nikale gaye hain
  (Ep 5 ke `ep05/full/c01.txt` se mila kar) — har phrase cold open mein **sirf ek jagah** aata hai
  (mixer ke `find_phrase` se jaancha gaya: 11 cue + 1 score + 1 duck, aur har bed ka start/end
  anchor — sab ek-ek hit; devanagari ke aakhri akshar par `।` hone se 1-akshari shabd (`है`, `ही`)
  anchor ke ant mein nahi rakhe gaye).
- `fallback_at` / `end_fallback` ~160 shabd-prati-minute ke andaaze se hain — ye sirf safety net
  hain (jab `--no-align` chale); asli mix `ep05_8/c01.align.json` se hoga, isliye waqt narration ke
  saath khud badlega.
- Mix: `python3 tools/audio/mix_from_plan.py --workdir ep05_8 --chunk c01 --plan "scripts/Ep 5.8 Ajanta ki auratein — SFX plan.json"`

## Cast (source files)
| id | file / recipe | what it is |
|---|---|---|
| GUHA | `ep01/sfx/raw_fs/b1_bed.mp3` | gaar ka band room-tone (bed) |
| CHATTAN | `ep02/sfx/raw_fs/air.mp3` (lowpass=1200) | nam, dabi hui gaar ki saans (bed) |
| SAANS | `ep03/sfx/raw_fs/wind.mp3` (lowpass=350) | nam chattan ki dheemi saans (spot) |
| TANAV | `ep02/sfx/raw_fs/drone.mp3` | Guru ki salah par low tension (bed) |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | score — ek hi swell |
| CHHAINI | `ep01/sfx/raw_fs/s3_stab.mp3` | patthar par chhaini (hard impact) |
| BRUSH | `ep01/sfx/raw_fs/s4_brush.mp3` | deewar par rang ka brush (do jagah) |
| CROWD | `ep03/sfx/raw_fs/crowd.mp3` | deewar par juloos (bheed, koi samajh mein aane wala shabd nahi) |
| CHUCKLE | `ep03/sfx/raw_fs/chuckle.mp3` | “sab jeevit” par door ki halki hansi |
| DIYA-CUP | `ep05/sfx/raw_fs/cup.mp3` | diya patthar par rakhna |
| BASS | `ep02/sfx/raw_fs/bass.mp3` (lowpass=200) | “wo khatarnak hain” ka wazan |
| synth | `tools/audio/mix_from_plan.py` ke andar | `gust` (lau ki hiss), `brick_thud` (boond), `stone_scrape` (deewar) |

Chhota par zaroori mixer note: `filter` sirf **file** sounds par lagta hai — `synth:` recipes par
nahi. Isliye jahan shape chahiye tha wahan file chuni gayi (`wind.mp3` lowpass=350), aur synth cues
raw recipe + `synth_seconds` par chalte hain.

## Cue table (anchor = phrase, waqt narration ke saath chalta hai; fallback seconds bracket mein)
| # | cue | sound | lands on the phrase | level | pan | fades |
|---|---|---|---|---|---|---|
| 1 | diya | `synth:gust` | “फिर एक रोशनी” (2.2 s) — lau jal uthti hai | −23 dB | −0.15 | 0.45 in / 0.7 out |
| 2 | saans | `ep03/sfx/raw_fs/wind.mp3` (lowpass=350) | “गीले पत्थर की” (9.8 s) — nam chattan ki dheemi saans | −24 dB | +0.35 | 0.9 in / 1.1 out |
| 3 | boond | `synth:brick_thud` | “साल का रंग” (16.9 s) — ek boond patthar par | −22 dB | +0.5 | 0.005 / 0.3 |
| 4 | chhaini | `ep01/sfx/raw_fs/s3_stab.mp3` | “सालों तक छैनी चली” (34.4 s) | **−16 dB** | −0.15 | 0.005 / 0.25 |
| 5 | brush1 | `ep01/sfx/raw_fs/s4_brush.mp3` | “रंग चढ़ा” (36.2 s) — rang deewar par chadhta hai | −21 dB | −0.3 | 0.05 / 0.3 |
| 6 | nirnay | `ep02/sfx/raw_fs/bass.mp3` (lowpass=200) | “वो खतरनाक” (48.8 s) — salah ka wazan | −23 dB | 0.0 | 0.35 / 0.6 |
| 7 | deewar | `synth:stone_scrape` | “और दीवार खुलती जाती” (54.5 s) — roshni patthar par khisakti hai | −22 dB | +0.4 | 0.08 / 0.4 |
| 8 | juloos | `ep03/sfx/raw_fs/crowd.mp3` | “जुलूस में चली” (65.2 s) — deewar ka juloos | −24 dB | +0.45 | 0.5 in / 1.2 out |
| 9 | jeevit | `ep03/sfx/raw_fs/chuckle.mp3` | “सब जीवित” (69.7 s) — door ki goonj | −24 dB | +0.55 | 0.1 / 0.8 |
| 10 | brush2 | `ep01/sfx/raw_fs/s4_brush.mp3` | “उन्हें पत्थर पर उतार दिया” (96.2 s) — wahi brush wapas | −22 dB | −0.25 | 0.15 / 0.6 |
| 11 | rukta | `ep05/sfx/raw_fs/cup.mp3` (highpass=90) | “दिया एक जगह रुक जाता” (114.7 s) — diya patthar par rakha jaata hai | −21 dB | −0.2 | 0.01 / 0.35 |

Beds (teen, sab narration ke neeche):

| bed | sound | kab se kab tak | level | pan |
|---|---|---|---|---|
| guha | `ep01/sfx/raw_fs/b1_bed.mp3` | 0.0 s se, `नमस्कार` par −0.25 s (≈133.05 s) band | −22 dB | 0.0 |
| nam_chattan | `ep02/sfx/raw_fs/air.mp3` (lowpass=1200) | 0.0 s se, `नमस्कार` par −0.25 s band | −26 dB | 0.0 |
| guru_tanav | `ep02/sfx/raw_fs/drone.mp3` | “वो वाक्य आज भी” (43.0 s) se `बस` (≈50.65 s) tak | −24 dB | 0.0 |

Beds `points` nahi dete (mixer ka default 2 s in / 1.2 s out envelope hi theek hai). `guru_tanav` ke
points **layer ke apne start se** hain: `[[0,−60],[1.2,0],[4.5,0],[6.0,−60]]` — yaani “बस।” se pehle
hi drone gayab.

## Score — ek hi swell
`ep03/sfx/raw_fs/tanpura.mp3` (highpass=70, lowpass=6000), **−25 dB**, pan 0.0. Enter:
“अजंता की औरतें मशहूर हो गईं” (81.8 s) par; chhoti `+1.5 dB` us line par jahan wo Guru ki baat maan
kar bhi unhe patthar par utaar deta hai (“उन्हें पत्थर पर उतार दिया”, 96.2 s); phir “दिया एक जगह रुक
जाता है” (≈113.8 s) par tanpura chup — aur ant (`−60 dB`) tak chup. Plan journal mein end
`नमस्कार` par −0.25 s hai, yaani **host intro se 0.25 s pehle score khatam** (chahe wo pehle se hi
sannata ho). Ek entry, ek swell, ek exit — teesra nahi.

Envelope (start se ginne): `[[0,−60],[2.5,0],[14.4,1.5],[23.0,0],[32.0,−60]]`.

## Duck (ek hi)
“अजंता की औरतें मशहूर हो गईं” par — `pre` 1.2 s, `post` 2.4 s, `gain` 0.3. Cold open ka naam/faisla
yahi hai, isliye sirf yahi ek baar poora SFX neeche jaata hai aur line akeli sunayi deti hai. Iske
alawa kisi naam par duck nahi.

## Kahan chup rehna hai
- **“बस।”** — `guru_tanav` drone ka end-anchor `बस` (−0.05 s) hai, par uske points usse pehle hi
  −60 dB par le jaate hain: teen vaakya wali salah ke baad “बस।” poori tarah akela rehta hai (koi
  spot cue nahi).
- **“वहां दीवार खाली है। कोई रंग नहीं। कोई चेहरा नहीं। बस पत्थर — और उस पर एक खाली जगह।”** — score
  yahan tak pahunchne se pehle chup ho chuka hai, aur koi cue nahi: sirf do halke beds. Khaali
  deewar ko koi awaaz nahi chahiye — use khaali hi rehna hai.
- **“आज हम उस खाली जगह पर लौटेंगे …”** — hand-off line, koi cue nahi (isse pehle “चलिए।” ke baad
  1.2 s pura sannata, phir body `## Ab tak` shuru).
- **“नेहरू इस पर रुक कर लिखते हैं …”** — yahan jaan-boojh kar koi foley nahi: likhne ki awaaz se
  quote ki shaanti toot jaati hai. Score besharmaan nahi, par foley nahi.
- Host intro, sawal aur roadmap — ek dum dry (koi bed, koi cue nahi).

## Sound list (exact paths / recipes jo istemaal hue)
Ambience/score: `ep01/sfx/raw_fs/b1_bed.mp3` · `ep02/sfx/raw_fs/air.mp3` · `ep02/sfx/raw_fs/drone.mp3` ·
`ep02/sfx/raw_fs/bass.mp3` · `ep03/sfx/raw_fs/tanpura.mp3`.
Foley: `ep01/sfx/raw_fs/s3_stab.mp3` · `ep01/sfx/raw_fs/s4_brush.mp3` (×2) · `ep03/sfx/raw_fs/wind.mp3` ·
`ep03/sfx/raw_fs/crowd.mp3` · `ep03/sfx/raw_fs/chuckle.mp3` · `ep05/sfx/raw_fs/cup.mp3`.
Synth: `synth:gust` (lau) · `synth:brick_thud` (boond) · `synth:stone_scrape` (deewar).
Kuch bhi download nahi kiya gaya — sab repo pool se hai.

## Kya sunayi dega
Pehle sirf andhera aur gaar ki dabi hui saans — phir ek halki lau, aur patthar par ek boond.
Saalon tak chhaini chalti hai, uske upar rang ka brush chadhta hai, aur Guru ki teen vaakya aate hi
ek low tanav dab ke baith jaata hai. “बस।” par poori gaar khaali ho jaati hai.
Deewar khulte hi bheed ka juloos aur door ki halki hansi aati hai — auratain bharpoor, sab jeevit.
“Ajanta ki auratein mashhoor ho gayin” par tanpura ek hi baar ubharta hai, “unhe patthar par utaar
diya” par chhoti leta hai, aur jaise hi diya khaali jagah par rukta hai, tanpura gayab.
Uske baad sirf patthar: koi rang, koi chehra, koi awaaz nahi — aur host “नमस्कार” se pehle poora
sannata, yahan tak ki aap apni hi saans sun saken.
