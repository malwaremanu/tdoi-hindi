# Ep 5.1 — SFX plan (cold open)

Cold open = `## Cold open` .. `## Ab tak` (367 narration words, chunk `c01`). Besnagar ka
khamba, chheni, dhool aur sookhi dopahar — phir wahi khamba us daur ka nishaan ban jaata hai
jab "hamlavar" aate rehte hain aur desh unhe apna bana leta hai.
House convention (Ep 3 / Ep 5 / Ep 6 / Ep 4.1): narration anchor hai, har bed uske neeche
baithta hai, host intro (नमस्कार) bilkul sookha hai, aur body se pehle ek dead-air pocket
rehta hai. **Sirf cold open ko sound milta hai** — `## Ab tak` se aage poora episode saaf.

## Cast (source files)

| id | file | what it is |
|---|---|---|
| AIR | `ep02/sfx/raw_fs/air.mp3` | dry, wide desert air (bed) |
| WIND | `ep03/sfx/raw_fs/wind.mp3` | thin gritty wind, far away (bed) |
| STAB | `ep01/sfx/raw_fs/s3_stab.mp3` | the hard chisel blow into stone |
| CROW | `ep01/sfx/raw_fs/s5_crow.mp3` | one distant crow (a village is there) |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | tanpura loop — the one swell |
| synth | `tools/audio/mix_from_plan.py` | `stone_scrape` (chheni ki tik-tik), `sand_trickle` (patthar ki dhool), `low_tone` (door ki ghanti), `gust` (darwaza) |

Synthesised cues are declared as such — koi download nahi, sirf repo pool.

## Cue table

Anchors phrase-locked hain: har cue apni Devanagari line ke us shabd par baithta hai jo
script mein hai. `fallback_at` (seconds) sirf safety net hai jab `--no-align` mix ho; ye
andaaze Ep 4.1 ke asli take se banaye gaye hain, isliye ±5 s ka farq maan lena. Mixer
`points` ko layer ke apne start se tolta hai (t = 0 = layer start), dB `level_db` ke
upar-niche.

| # | cue | sound | lands on the phrase | level | pan | fades |
|---|---|---|---|---|---|---|
| B1 | sookhi dopahar ki hawa, shuru se aakhir tak | AIR bed (`air.mp3`, HP 90 / LP 8000) | `ये गांव बेसनगर` se pehle se, `नमस्कार` se 0.25 s pehle out | -21 dB | centre | in 2.5 s, out 2.5 s |
| B2 | patli, door ki khushk hawa | WIND bed (`wind.mp3`, HP 140 / LP 6500) | `नमस्कार` se 0.25 s pehle out | -25 dB (thes par 1.5 dB neeche) | centre | in 3.5 s, out 2.5 s |
| A1 | chheni ki pehli tik-tik, patthar par | `synth:stone_scrape` 0.4 s | `एक लकीर खींचता` | -20 dB | -0.3 | 0.005 / 0.12 |
| A2 | chheni ki ek thes — hard blow | STAB (`s3_stab.mp3`) 0.6 s | `फिर दूसरी` | **-16 dB** (scene ka sabse loud block) | -0.15 | 0.005 / 0.35 |
| A3 | patthar ki dhool girna | `synth:sand_trickle` 1.8 s | `फिर दूसरी` (+0.35 s) | -24 dB | +0.25 | 0.06 / 0.6 |
| A4 | teesri tik-tik | `synth:stone_scrape` 0.4 s | `फिर तीसरी` | -21 dB | -0.1 | 0.005 / 0.12 |
| A5 | ek door ka kauwa | CROW (`s5_crow.mp3`) 1.2 s | `सांची से ज्यादा दूर` | -24 dB | +0.55 | 0.03 / 0.25 |
| A6 | door kisi mandir ki ghanti, ek baar (library mein ghanti nahi hai: neecha `low_tone` tol) | `synth:low_tone` 2.6 s | `रुकीये और इसे` (-1.5 s) | -24 dB | +0.5 | 0.02 / 1.6 |
| A7 | niyam 1 par tik-tik | `synth:stone_scrape` 0.3 s | `अपने पर काबू रखना` | -21 dB | -0.2 | 0.004 / 0.10 |
| A8 | niyam 2 par tik-tik | `synth:stone_scrape` 0.3 s | `दूसरों के लिए त्याग करना` | -21 dB | -0.12 | 0.004 / 0.10 |
| A9 | niyam 3 par tik-tik | `synth:stone_scrape` 0.3 s | `अपना फर्ज ईमानदारी से निभाना` | -22 dB | -0.18 | 0.004 / 0.10 |
| A10 | darwaza band hone lage — ek sookhi gust | `synth:gust` 3.5 s | `ये दरवाजा बंद होने` | -23 dB | +0.35 | 0.9 / 1.4 |
| M1 | tanpura — ek hi entry | TANPURA (`tanpura.mp3`, HP 70 / LP 6000) | `ये गांव बेसनगर` par shuru, `नमस्कार` se 0.25 s pehle out | -24 dB, swell par -22 dB | centre | in 4 s, out 2.5 s |
| D1 | duck — key line akela | — | `इस देश का एक देवता` | gain 0.3 (pre 1.3 s, post 2.4 s) | — | — |

**Spot cues: 10** (A1–A10) — sab apni line se motivated, koi cue 12 se zyada nahi, aur ek
bhi cue host intro ko cross nahi karta. Sabse loud cheez chheni ki thes hai (-16 dB); beds
apni layer par -21 / -25 par rehte hain, isliye summed bed bhi -16 se upar nahi jaata.

## Score — ek hi swell

Ek hi instrument: tanpura drone, koi dhun nahi, koi percussion nahi.

| kab | M1 | kya hota hai |
|---|---|---|
| 0 → `ये गांव बेसनगर` | off | pehle sirf patthar: hawa, chheni, dhool — koi music nahi |
| `ये गांव बेसनगर` | → -24 dB | jagah ka naam aata hai, tanpura 4 s mein bichh jaata hai (script ka "Besnagar par shuru") |
| naam tak (`इसे हेलिओडोरस ने खड़ा किया`) | -24 → **-22 dB** | **yahi ek swell hai** — likhaai aur naam par tanpura do dB upar uthta hai |
| `इस देश का एक देवता` se aage | wapas -24 dB | verdit line par neeche, key line akeli rehti hai |
| `सवाल दो हैं` → `नमस्कार` | → -∞ | 2.5 s mein ghulta hai aur `नमस्कार` se 0.25 s pehle poora gaayab |

Rules: swell sirf ek baar (naam par), score kabhi kisi stressed shabd par shuru/band nahi
hota, aur `नमस्कार` ke baad poore episode mein koi score nahi.

Note: script ki inline `[SFX: tanpura … "Besnagar" par shuru]` line host intro ke saath hi
baithi hai. House rule ("koi cue host intro ko cross na kare, score `नमस्कार` se pehle out")
ke hisaab se tanpura ko **pehle** Besnagar par — `ये गांव बेसनगर है` — entry di gayi hai, aur
wo `नमस्कार` se 0.25 s pehle chala jaata hai. Agar writer chahe ki tanpura der se aaye, to
wahi layer `रुकीये और इसे` par bhi baith sakta hai — baaqi plan waisa hi rahega.

## Kahan chup rehna hai

1. **`वो एक यूनानी है`** — "wo ek Yunani hai." par koi naya sound nahi. Yahi cold open ka
   pehla jhatka hai: beds chalu, bas.
2. **`ये छोटी बात नहीं है। ये एक निशान है।`** — dono chhoti lines par kuch nahi. Verdict ke
   baad jagah khaali rehni chahiye.
3. **`सवाल दो हैं` se `नमस्कार` tak** — score aur beds dono ja chuke hain. Do sawal aur host
   intro poore sookhe hain; koi tail, koi hiss, koi whoosh nahi.
4. **`नमस्कार` ke baad** — `Aaj ka sawal do hisson mein hai…` bhi saaf, aur `## Ab tak` se
   aage poora episode bina SFX.
5. **Body se pehle 1.2 s** — `Besnagar ka.` ke baad poora sannata, phir body ka pehla shabd.

## Sound list (exact paths)

Beds: `ep02/sfx/raw_fs/air.mp3` (HP 90 / LP 8k, -21 dB) · `ep03/sfx/raw_fs/wind.mp3`
(HP 140 / LP 6.5k, -25 dB).
Foley: `ep01/sfx/raw_fs/s3_stab.mp3` (thes) · `ep01/sfx/raw_fs/s5_crow.mp3` (door ka kauwa).
Synthesised (mixer ke recipes): `synth:stone_scrape` (chheni ki tik-tik, teen niyam bhi) ·
`synth:sand_trickle` (patthar ki dhool) · `synth:low_tone` (door kisi mandir ki ghanti ki
jagah ek neecha, door ka tol) · `synth:gust` (darwaza band hone lage).
Score: `ep03/sfx/raw_fs/tanpura.mp3` (HP 70 / LP 6k, -24 dB, swell par -22 dB).
Koi naya download nahi.

## Kya sunayi dega

1. शुरू में बस सूखी दोपहर की हवा, और पत्थर पर छेनी की तेज़ टिक-टिक — पहली लकीर, फिर एक ठोस चोट, और उसके बाद पत्थर की धूल।
2. "ये गाँव बेसनगर है" पर दूर एक कौवा, और पीछे धीरे-धीरे तानपूरा बिछ जाएगा।
3. "रुकिए, और इसे ध्यान से देखिए" से ठीक पहले दूर से एक धीमी, नीची घंटी जैसी टोल।
4. तीन नियमों पर छेनी तीन बार टिक-टिक करेगी, नाम पर तानपूरा एक बार ऊपर उठेगा, और "इस देश का एक देवता" पर सब कुछ एक क़दम पीछे हट जाएगा।
5. "एक दिन ये दरवाज़ा बंद होने लगता है" पर एक सूखी हवा का झोंका, फिर दो सवाल पूरी ख़ामोशी में, और "नमस्कार" से पहले सब ग़ायब।
