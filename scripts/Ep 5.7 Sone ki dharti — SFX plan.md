# Ep 5.7 — SFX plan (cold open)

Cold open = `scripts/Ep 5.7 Sone ki dharti — Script.md` ka `## Cold open` se `## Ab tak` tak ka
hissa — 313 narration shabd (headings aur do `[SFX: …]` lines chhod kar). Scene: Bayon ke dwar par
ginti bhool jaane wale wahi tarashe hue chehre, phir khandhar aur Angkor Vat, phir sawal — aur
aakhir mein nazar samundar ki taraf mudi hai. House style: **sirf cold open par awaaz; ident ke baad
poora episode saaf narration.**

Do baatein pehle, taaki plan padhne mein saaf rahe:

- **Anchors phrase hain, seconds nahi.** Har cue ka asli waqt narration ke words se tay hoga (mixer
  `ep05_7/c01.align.json` se phrase dhoondhta hai). Jo seconds neeche diye hain wo nominal hain.
- **Seconds ka model:** Ep 4.1 ke apne take se naapa gaya rate ~2.53 narration shabd/sekand (382
  shabd → 151.0 s) se banaye gaye hain. Is episode ka take abhi nahi bana (`ep05_7/` maujood hi
  nahi), isliye `fallback_at`/`end_fallback` sirf safety net hain — take aane par ek baar re-spot
  kar lena.
- Devanagari phrases repo ke apne transliterator (`tools/audio/transliterate.py`, gemini-web2api)
  se banaye gaye hain, isliye wo narration ki spelling se milenge. Das cue phrases mein se har ek
  cold open mein **ek hi baar** aata hai; ek hi jagah dikkat hai — beds/score ka end phrase
  `["नमस्कार"]` (jise bhoolna nahi, dekhiye `## Mix notes / QC` mein `end_occurrence` ki warning).

## Cast (source files)

| id | file | what it is |
|---|---|---|
| AIR | `ep02/sfx/raw_fs/air.mp3` | sookhi, khuli hawa (main bed) |
| GRIT | `ep03/sfx/raw_fs/wind.mp3` | wahi recording, patli grit layer ki tarah (dekhiye `## Sound list` ka note) |
| FIELD | `ep03/sfx/raw_fs/field.mp3` | deewaron ke us paar ka khula, door ka aasman |
| SARANGI | `ep03/sfx/raw_fs/sarangi.mp3` | ek bowed phrase — naam ke lamhe ke liye |
| BASS | `ep02/sfx/raw_fs/bass.mp3` | sub-bass, mandir khada hone ke liye (`filter: lowpass=200`) |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | tanpura — scene ka ek hi score |
| GRAVEL | `ep01/sfx/raw_fs/s2_gravel.mp3` | malba / khandhar |
| synth | `tools/audio/mix_from_plan.py` | `stone_scrape`, `gust`, `brick_thud`, `river_wash` |

## Cue table

`lands on the phrase` = mixer us phrase ke aakhri shabd ke khatam hone ka waqt leta hai; `offset`
usi par lagta hai. NA = nahi lagta (bed).

| id | cue (narration line) | sound | lands on the phrase | level under the voice | pan | fades |
|---|---|---|---|---|---|---|
| AIR | poora cold open (bed) | `ep02/sfx/raw_fs/air.mp3` | NA — `start: 0.0`, `end_phrase: ["नमस्कार"]` -0.25 s | -22 dB | 0.0 | 2.5 s in; out ident se 0.25 s pehle |
| GRIT | poora cold open (bed) | `ep03/sfx/raw_fs/wind.mp3` (HP 400) | NA — wahi end | -26 dB | 0.0 | 2.5 s in; out ident se 0.25 s pehle |
| FIELD | poora cold open (bed) | `ep03/sfx/raw_fs/field.mp3` | NA — wahi end | -27 dB | 0.0 | 3 s in; out ident se 0.25 s pehle |
| S1 | "Ek chehra hai. Patthar mein tarasha hua." | `synth:stone_scrape` (1.3 s) | **पत्थर में तराशा हुआ** | -22 dB | -0.30 | in 0.05 / out 0.40 |
| S2 | "Upar se neeche, sab taraf, wahi ek shakl." | `synth:gust` (2.6 s) | **ऊपर से नीचे सब तरफ** | -24 dB | +0.50 | in 0.8 / out 0.8 |
| S3 | "Ek dwar par ek." | `synth:brick_thud` | **एक द्वार पर एक** | -21 dB | -0.35 | in 0.005 / out 0.25 |
| S4 | "Uske baad ek aur." | `synth:brick_thud` | **उसके बाद एक और** | -22 dB | -0.20 | in 0.005 / out 0.25 |
| S5 | "Ginti bhool jaaiye… wahi ek shakl." | `synth:brick_thud` | **वही एक शक्ल** | -23 dB | -0.05 | in 0.005 / out 0.25 |
| S6 | "Is dwar ka naam Bayon hai." | `ep03/sfx/raw_fs/sarangi.mp3` (3.2 s) | **इस द्वार का नाम बायोन है** | -23 dB | 0.0 | in 0.4 / out 1.6; offset -1.6 |
| S7 | "Kuch door ek aur bada mandir khada hai. Angkor Vat." | `ep02/sfx/raw_fs/bass.mp3`, `lowpass=200` (7 s) | **अंगकोर वट** | -20 dB | 0.0 | in 2.5 / out 3.0; offset -0.9 |
| S8 | "Uske chaaron taraf khandhar hain." | `ep01/sfx/raw_fs/s2_gravel.mp3` (1.2 s) | **उसके चारों तरफ खंडहर** | **-18 dB** (scene ka sabse ooncha cue) | -0.15 | in 0.05 / out 0.30 |
| S9 | "Naqli jheel aur talab. Nahrein. Un par pul." | `synth:river_wash` (4 s) | **नकली झील और तालाब** | -24 dB | +0.45 | in 1.2 / out 1.5; offset -0.5 |
| S10 | "…wahi chehra — bahut bada, tarasha hua." | `synth:stone_scrape` (1.6 s) | **बहुत बड़ा तराशा हुआ** | -21 dB | +0.30 | in 0.05 / out 0.50 |
| SCORE | "Samundar. Aur ek raasta…" se "…taraf dekh rahi hai." | `ep03/sfx/raw_fs/tanpura.mp3` | entry **समुंदर और एक रास्ता** (73.9 s) | -24 dB, swell par +2 dB (asardar -22 dB) | 0.0 | in 2.2 s; out `["नमस्कार"]` -0.25 s (86.3 s) |

**Spot cues: 10** (S1–S10), sab narration ke us line se prerit hain jispar wo girte hain. Sabse ooncha
cue S8 hai (-18 dB); kuch bhi -16 dB se oopar nahi jaata.

## Score (ek hi swell)

Ek hi layer, ek hi entry, ek hi swell, aur ident se pehle poori tarah gayab.

| waqt (nominal) | tanpura | kya ho raha hai |
|---|---|---|
| 73.9 → 76.1 s | -60 → 0 dB (fade in) | "समुंदर। और एक रास्ता…" par pravesh — samundar aaya, to tanpura bhi |
| 76.1 → 82.5 s | -24 dB flat | sawal ka block, beds ke saath, kuch nahi hilta |
| 82.5 → 85.2 s | **-24 → -22 dB (swell)** | "…is desh ki taraf dekh rahi hai" par ek hi baar oopar uthna |
| 85.2 → 86.3 s | -22 → -60 dB | jaate hue girna; **86.6 s par "नमस्कार"** — beech mein 0.25 s khaali |
| ident ke baad | band | intro, teen sawal aur "Chaliye." — sab beds/score ke bina |

Rules: tanpura samundar se pehle **kabhi nahi** (script khud kehta hai "koi sangeet nahi" — isliye
entry itni der se hai); ident ke baad score dobara **nahi** aata (ek hi swell); chaaron taraf flat,
na koi doosri dhun, na reverb.

## Kahan chup rehna hai (silence beats)

1. **"Halki. Chup. … vo khush hai ya udaas." (~4.0–12.6 s)** — chehre ki muskaan par kuch nahi.
   Sirf beds. Yahi scene ka pehla silence beat hai.
2. **"Jaise kisi ne ek hi soch li ho… dohrate hi chala gaya ho." (~24.1–31.6 s)** — dohrayaav ka
   khayal shabdon mein hai, isliye yahan koi cue nahi (thud S3–S5 usse pehle khatam ho jaate hain).
3. **"Ek pyaara, muskurata, par rahasyamayi Cambodian chehra. Jaise kisi devta ka chehra ho." aur
   "Angkor ki ye muskaan. Bar-baar wahi muskaan." (~53.4–60.9 s)** — rahasyamayi chehre par na
   stinger, na swell.
4. **"Ab ek sawal… jo yahan nahi hai." (~60.9–72.7 s)** — sawal sirf beds par poocha jaata hai;
   "jo yahan nahi hai" par jaan-boojh kar kuch nahi (jo cheez nahi hai, uski awaaz bhi nahi).
5. **Ident se pehle (~86.3 s)** — score aur beds dono 86.6 s wale "नमस्कार" se 0.25 s pehle out.
   Script ki line: "ident se pehle sannata."
6. **Intro + teen sawal + "Chaliye."** — poori tarah saaf voice; aur body se pehle **1.2 s** ka
   asli sannata (dead air). Cold open ke baad poora episode saaf rehta hai.

## Sound list (exact paths)

| kaam | path / recipe |
|---|---|
| dry air bed | `ep02/sfx/raw_fs/air.mp3`, `highpass=90,lowpass=8000` |
| grit bed | `ep03/sfx/raw_fs/wind.mp3`, `highpass=400,lowpass=6000` |
| door ka khula aasman bed | `ep03/sfx/raw_fs/field.mp3`, `highpass=250,lowpass=7000` |
| naam | `ep03/sfx/raw_fs/sarangi.mp3` |
| mandir ka wazan | `ep02/sfx/raw_fs/bass.mp3`, `lowpass=200` |
| score | `ep03/sfx/raw_fs/tanpura.mp3`, `highpass=70,lowpass=6000` |
| khandhar | `ep01/sfx/raw_fs/s2_gravel.mp3` |
| patthar par chhaini | `synth:stone_scrape` |
| hawa ka jhonka | `synth:gust` |
| dohraye hue dwar | `synth:brick_thud` |
| jheel / nahar | `synth:river_wash` |

Do notes jo mix se pehle dekh lena:

- `ep02/sfx/raw_fs/air.mp3` aur `ep03/sfx/raw_fs/wind.mp3` **ek hi file hain** (md5
  `0e1687e50ad830415b3b658fee3dfd5a`). Isliye AIR aur GRIT ko do alag jagah nahi, ek hi recording ke
  do band ki tarah treat kiya gaya hai: same file, alag filter, aur 4 dB ka antar (AIR -22, GRIT -26)
  — warna dono milkar bas +4 dB EQ lagte hain.
- FIELD bed ka andaaza hai ki `field.mp3` door ki sookhi hawa/pattiyon jaisa lagta hai. Agar sunne
  mein uske andar aawazein, engine ya koi modern shor milta hai, to bed hata dein (cue table aur
  JSON se `field` entry nikaal dein) — baaki plan waise hi chalega.

Kuch bhi download nahi kiya gaya; sab repo pool se hai.

## Mix notes / QC

- **Levels:** beds -22/-26/-27 dB, spot cues -18 se -24 dB, score -24 (swell par -22). Scene ka sabse
  ooncha cue S8 (-18 dB) hai — `khandhar` ka malba. Kuch bhi -16 dB se oopar nahi.
- **Pan:** voice dead centre. Foley left (-0.35 … -0.05 ke beech), door/wide cheezein right
  (gust +0.50, nahar +0.45, door ka chehra +0.30). Beds aur score 0.0 par.
- **Duck ek hi baar:** naam ke lamhe par — phrase **इस द्वार का नाम बायोन है**, `pre: 1.2`,
  `post: 2.2`, `gain: 0.3`, yaani 34.8 s se 38.2 s tak beds/score neeche, taaki naam akela gire.
  Doosri jagah koi duck nahi.
- **Charts:** beds aur score ke `points` nominal seconds mein hain (0 → 86.3 s). Take aane par
  pehle `align.json` se anchors dekhein, phir `points` ko naye waqt par saraka dein. Agar take
  lamba nikla, to beds ka fade-out aakhri 3 s mein hi rakhna (ident se 0.25 s pehle khatam).
- **Koi cue host intro ko cross nahi karta.** Beds/score `["नमस्कार"]` par -0.25 s par out hote hain.
- **Anchor ki do warnings (mix se pehle padh lena):**
  - Beds aur score ka `end_phrase` `["नमस्कार"]` hai, par mixer ka fuzzy matcher is skeleton ko cold
    open mein **do jagah** match karta hai: pehle "मुस्कुराता," par (53.75 s) aur phir asli
    "नमस्कार," par (86.56 s). Isliye `end_occurrence: 2` diya gaya hai — hata dene par teenon beds
    aur score 54 s par hi kat jaayenge. `end_fallback: 86.6` safety net hai.
  - Chhote ek-shabd words jinke aage danda/comma lagta hai ("हैं।", "है।") fuzzy match mein 0.7
    threshold se neeche reh jaate hain (ratio ~0.67). Isliye S8 ka phrase
    `["उसके","चारों","तरफ","खंडहर"]` hai (aakhri shabd "खंडहर" bina punctuation ke milta hai) —
    warna wo cue sirf fallback par chalta.
- **Verification:** yehi JSON `tools/audio/mix_from_plan.py` se do baar chalaya gaya (scratch mein
  130 s ka dummy take, pehle `--no-align`, phir isi Devanagari text se bane `align.json` ke saath):
  beds 0 → 86.31 s, tanpura 73.91 → 86.31 s, saare 10 cue apne intended waqt par (2.17, 16.45,
  18.03, 20.94, 22.33, 34.37, 42.18, 44.26, 46.14, 51.87 s), duck 35.97 s, SFX layer ka peak
  -29 dBFS (narration se ~14 dB neeche). Kuch bhi "नमस्कार" (86.56 s) ko cross nahi karta.
- **QC:** phone speaker par ek baar — agar beds shabdon se pehle sunai den, 1 dB neeche; headphones
  par ek baar — naam ke waqt beds/score ki chaadar, pre-ident sannata, aur S1/S10 ki chhaini
  patthar jaisi lagti hai ya nahi.

## Kya sunayi dega

1. शुरू में सूखी हवा पत्थर की दीवारों के बीच चलेगी, दूर कहीं खुला आसमान बहुत हल्का रहेगा, और अंदर किसी संगीत की आवाज़ नहीं होगी।
2. चेहरा तराशने की एक छोटी खुरचन, ऊपर से नीचे चलती हवा का एक झोंका, और एक के बाद एक दबी हुई थापें जो धीरे-धीरे हल्की पड़ती जाएंगी — जैसे गिनती छूट रही हो।
3. कंबोडिया और बयोन का नाम सुनाई देते ही एक सितार-सी एक-एक फिरती हुई सांस आएगी, और उसी वक़्त बाक़ी सब थोड़ी देर के लिए दब जाएगा।
4. "अंगकोर वट" पर नीचे से एक भारी सुर उठेगा, फिर खंडहर की खड़खड़, झील-नहर की धुली-धुली लहर, और दूसरी बार पत्थर पर चलती छैनी।
5. मुस्कुराते, रहस्यमयी चेहरे पर पूरा सन्नाटा होगा, और सवाल भी सिर्फ़ हवा के नीचे पूछा जाएगा।
6. "समुंदर" पर तानपूरा बहुत धीरे से आएगा, आख़िरी लाइन पर एक बार हल्का सा ऊपर उठेगा — और "नमस्कार" से पहले ख़त्म हो जाएगा।
