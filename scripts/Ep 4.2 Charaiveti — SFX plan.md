# Ep 4.2 Charaiveti — SFX plan (cold open)

Cold open = `## Cold open` .. `## Ab tak` — 437 narration words, chunk `c01` (`c01.txt`, 441 Devanagari
tokens, kareeb 182.6 s). Yahan sirf wahi scene score hota hai; baaki episode dry narration hai.
Signal chain wahi hai jo Ep 4.1 / Ep 3 / Ep 5 mein chali: narration anchor hai, har bed uske neeche
baithta hai, host intro poora dry hai, aur aakhri layer `नमस्कार` se 0.25 s pehle kat jaati hai.

Teen beat jaan-boojh kar khali chhode gaye hain: **"गुरु कुछ नहीं कहते"**, **"लड़का सोचता रह
जाता है / उसे जवाब नहीं मिला"** aur **raakh/angare wala chhota beat** — kuch jagah chuppi hi
sahi jawab hai, wahan koi cue nahi jaata.

## Cast / sound list (exact paths)

| id | file | kya hai |
|---|---|---|
| FIELD | `ep03/sfx/raw_fs/field.mp3` | jungle ki subah — khula bed (0 → 1944) |
| WIND | `ep03/sfx/raw_fs/wind.mp3` | patton wali hawa, patli gritty layer |
| DHAARA | `synth:river_wash` | behti patli dhaara (bed + "paani" wala swell) |
| ROOM | `ep01/sfx/raw_fs/b1_bed.mp3` | 1944 ki kothri ka room tone |
| AIR | `ep02/sfx/raw_fs/air.mp3` | kothri ka halka jhonka = lalten ki lau (high-pass) |
| CHIDIYA | `ep01/sfx/raw_fs/s5_crow.mp3` | ek akeli chidiya, teen hits |
| GUST | `synth:gust` | kaanpte patte |
| KAAGAZ | `ep01/sfx/raw_fs/s8_paper.mp3` | kitaab ka panna palatna |
| PEN | `ep01/sfx/raw_fs/s8b_pen.mp3` | kalam ka theharna / rukna |
| LIKHAI | `ep01/sfx/raw_fs/s9_writing.mp3` | copy mein sawal utaarna |
| SHRUTI | `ep03/sfx/raw_fs/shruti.mp3` | score — shruti-box, ek hi swell |

Synthesised cues (`river_wash`, `gust`) yahin declare kiye gaye hain; baaki sab repo pool se.
(Chidiya ke liye pool mein crow hi hai — ek akeli dawn call, do baar, bilkul jaisa script kehta hai.)

## Cue table (anchors phrase-locked, seconds fallback hain)

| id | cue (kis line par) | sound | phrase (Devanagari) | level | pan | fades |
|---|---|---|---|---|---|---|
| A1 | "Paas hi ek dhaara beh rahi hai" → poora pehla hissa | DHAARA (synth bed) | — | −25 dB | −0.15 | 3.5 s in, 1944 par cut |
| A2 | "Par ek pal ke liye bhi ruki nahi." | CHIDIYA, pehli baar | `रुकी नहीं` | −32 dB | +0.55 | 0.02 / 0.10 |
| A3 | wahi line, doosri baar | CHIDIYA, doosri baar | `रुकी नहीं` (+1.9 s) | −33 dB | +0.20 | 0.02 / 0.12 |
| A4 | "Fir un patton ko, jo hawa mein kaanp rahe hain." | GUST 3.5 s | `जो हवा में कांप रहे` | −26 dB | +0.35 | 0.4 / 1.2 |
| A5 | "Ladka phir poochta hai. Aur ye paani?" | DHAARA 6 s (synth cue) | `और ये पानी` | −24 dB | −0.30 | 0.8 / 1.5 |
| A6 | "Guru kuch nahi kehte." | **koi cue nahi** | — | — | — | — |
| A7 | raakh / angare wala beat | **koi cue nahi** | — | — | — | — |
| B1 | "Ab bahut aage aaiye. Dhai hazaar saal se bhi aage." | CHIDIYA, aakhri | `ढाई हजार साल से भी आगे` | −30 dB | −0.45 | 0.02 / 0.12 |
| B2 | "Saal unnis sau chavalis." | FIELD + WIND + DHAARA **hard out** | `उन्नीस सौ चवालीस` | — | — | bed ends −0.15 s; phir ~1.3 s sannata |
| C1 | "Ahmadnagar ka qila. Ek kothri. Raat. Mez par ek lalten." | ROOM (bed, 2 s fade in) + AIR 2.4 s | `अहमदनगर का किला` | −26 / −30 dB | 0 / +0.40 | 0.3 / 0.8 |
| C2 | "Ek qaidi ek purani kitaab ke panne palat raha hai." | KAAGAZ 1.1 s | `किताब के पन्ने पलट` | −21 dB | −0.25 | 0.02 / 0.25 |
| C3 | "Ek panne par ruk jaata hai." | PEN 0.6 s | `पन्ने पर रुक जाता` | −23 dB | −0.30 | 0.01 / 0.20 |
| C4 | "Aur apni copy mein wahi sawal utaarta hai." | LIKHAI 2.6 s | `कॉपी में वही सवाल` | −20 dB | −0.20 | 0.05 / 0.40 |
| D1 | "Ye qaidi hain Jawaharlal Nehru." | **duck** (naam akela) | `जवाहरलाल नेहरू` | ×0.3 | — | pre 1.2 / post 2.4 |
| D2 | "Ladka sochta reh jaata hai. Use jawab nahi mila." | **koi cue nahi** | — | — | — | — |
| E1 | "To wo sawal poochne wala ladka kahan gaya?" | PEN 0.7 s (kalam rukti hai) | `लड़का कहां गया` | −24 dB | −0.35 | 0.02 / 0.35 |
| E2 | "Namaskar, main hoon Asha…" | sab beds + score out | `उन्नीस सौ चवालीस` / `नमस्कार` | — | — | 0.25 s pehle out; intro dry |

Kul 10 spot cues. Sabse tez spot cue −20 dB (LIKHAI) — −16 dB ki chhoot use nahi ki gayi, headroom
poora hai. Chhoti door wali details (chidiya −32/−33) 4.1 ke crow (−32) jaise hi jaan-boojh kar
voice se kaafi neeche hain.

## Score (ek hi swell)

- **Entry:** `जिन्हें हम उपनिषद कहते` (−0.6 s) — jab narration kehti hai ki ye sawal sach mein
  poochhe gaye the, aur Upanishad ke roop mein likhe gaye. Yahi scene ka hinge hai.
- **Swell:** chhand **"कौन जानता है? Kaun yahan keh sakta hai?"** par envelope 0 dB par aata hai
  (level −22 dB = is layer ka peak). Rise kareeb 4 s ka, koi transient nahi.
- **Exit:** `नमस्कार` − 0.25 s par poori tarah bahar. Score ek hi baar uthta hai, ek hi baar chadhta
  hai aur jaata hai; host intro aur uske baad wale do sawal bilkul dry hain.
- **1944 par score kata nahi.** Script kehti hai dhaara, hawa aur chidiya ek saath band ho jaate
  hain — wo teen layer katte hain (B2), par shruti wahi dhun kothri mein le jaati hai. Isliye hard
  cut ke baad sannata bhi lagta hai aur kahani tootti nahi.

## Kahan chup rehna hai

1. **`उन्नीस सौ चवालीस`** — FIELD + WIND + DHAARA ek frame mein, us word ke andar. Uske baad
   ~1.3 s sannata; ROOM 2 s ke fade se aata hai. Yahi scene ka sabse bara silence moment hai.
2. **"गुरु कुछ नहीं कहते."** — koi cue nahi, koi accent nahi. Guru ka jawab uski chuppi hai.
3. **"लड़का सोचता रह जाता है। उसे जवाब नहीं मिला।"** — koi cue nahi; sirf beds.
4. **Raakh aur angare** (~13–16 s) — jalti aag ka crackle jaan-boojh kar nahi hai; subah ki
   thandi raakh hai, aag nahi.
5. **Ant** — kalam rukne ke baad kuch nahi; `नमस्कार` se 0.25 s pehle sab layers out.
   Intro ke baad **1.3 s dead air**, phir body.

## Rules jo nibhaye gaye

- Har phrase `ep04_2/c01.txt` ka **exact contiguous hissa** hai (Devanagari, wahi tokens).
- Anchor `occurrence` ka dhyan: `नमस्कार` mixer ke fuzzy match mein pehli baar `मुस्कुराते` (~58 s)
  par bhi pakda jaata hai, isliye bed/score par **`end_occurrence: 2`** diya gaya hai. Baaki saare
  phrase (`कहां गया`, `ढाई हजार साल से भी आगे`, `कॉपी में वही सवाल`, …) cold open mein ek hi baar
  aate hain — mila kar dekha gaya.
- Phrase apne aap mein punctuation se bacha kar chune gaye (aakhri word aksar mid-sentence), kyunki
  mixer ka normalisation danda/quote ko bhi ginta hai aur `हैं।` ⇒ `ह` jaisa 1-akshar word 0.7
  threshold se neeche chala jaata hai.
- Voice dead centre; foley halka bayen (−0.2…−0.35), door ki cheezein daayen (+0.2…+0.55), beds aur
  score 0.0 par.
- Koi cue host intro ko cross nahi karta (aakhri cue `नमस्कार` se ~0.7 s pehle khatam).
- Level bands: beds −23…−26, spot −20…−26 (ambience-jaisi synth), chhoti door details −30…−33,
  score −22…−26. Sabse tez block kothri (C1–C4) hai; −16 dB ki chhoot use nahi hui.
- `points`/`fallback_at` ke seconds `c01.wav` (182.56 s) aur c01 ke word-count se nikale gaye andaze
  hain. Pehle aligned mix ke baad `ep04_2/sfx/cue_times.json` se ek baar re-spot kar lena —
  anchors khud sahi jagah land karte hain, sirf bed/score ke envelope points thoda khisak sakte hain.
- Final mix target: −16 LUFS integrated, TP −1.5 dB, LRA 11; cold open ke baad SFX band.

## Kya sunayi dega

1. Jungle ki purani subah: halki hawa, patton ki sarsarahat, aur paas mein behti ek patli dhaara —
   jo ek pal bhi ruki nahi.
2. Ek akeli chidiya do baar bolti hai, patte kaanpte hain, aur jab ladka poochta hai "aur ye paani?",
   to dhaara zara ubhar kar jawab deti hai. Guru ke chup ho jaane par kuch nahi bajta.
3. "Saal unnis sau chavalis" — dhaara, hawa aur chidiya ek frame mein kat jaate hain, aur ek pal ka
   poora sannata baithta hai.
4. Phir kothri: lalten ki halki lau, kaagaz ka panna, kalam theharki, aur copy mein utarti likhai.
5. "Jawaharlal Nehru" par sab kuch dab jaata hai — naam akela khada rehta hai.
6. Aakhri sawal par kalam ruk jaati hai, shruti utar jaati hai, aur host ke "namaskar" se pehle
   0.25 s ka poora khali. Intro dry. Aage kahani bina SFX ke chalti hai.
