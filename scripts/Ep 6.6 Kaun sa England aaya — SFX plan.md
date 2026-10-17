# Ep 6.6 — SFX plan (cold open)

Cold open = `## Cold open` .. ident ki teen aakhri lines ("Aaj ka sawal…", "Us Jaipur wale dono parche…")
— **384 narration words**, chunk `c01`. Scene: Jaipur ki chhat, raat; mez par do parche (Portugal ki
tables aur apne yahan ki ginti), ek deepak, aur darbaar ke kaam karne wale log.

Signal chain wahi hai jo Ep 3 / 5 / 6 / 4.1 mein hai: **narration anchor hai**, har bed uske neeche
baithta hai, host intro sookha rehta hai, aur aakhri bed cut ident se pehle ek sannata chhodta hai.
Baaki poora episode saaf narration hai — sirf ye cold open score hota hai.

Anchors: har cue ka `phrase` is cold open ke narration shabdon ka **contiguous silsila** hai, Devanagari
mein (JSON mein wahi). Saare phrases mixer ke apne match niyam (`norm` + 0.7 similarity,
`mix_from_plan.py`) se 384-shabd wale cold open par jaanche gaye hain — har phrase ek hi jagah milta hai
(jahan do jagah milta, wahan `occurrence` diya hai). Spelling bhi repo ke apne Devanagari takes se
milaayi gayi (`उंगली`, `लाइन`, `नमस्कार,`, `रात भर`); `परचे`/`पर्चे` aur `कागज़`/`कागज` mixer ke `norm`
mein ek hi ban jaate hain. `fallback_at` 0.32 s/shabd par naapa gaya hai (Ep 4.1 ke plan se: 472 shabd
→ 151.0 s), taaki `--no-align` par, ya take ka Devanagari kahin badal jaye to, cue phir bhi apni jagah
ke paas baithe. `c01.align.json` ban jaane par yehi phrases audio ke asli waqt par lock ho jaate hain.

## Cast (source files)

| id | file | what it is |
|---|---|---|
| AIR | `ep02/sfx/raw_fs/air.mp3` | chhat ki sookhi raat ki hawa (bed) |
| VILLAGE | `ep03/sfx/raw_fs/b1_village.mp3` | neeche soya hua shehar — door ki dheemi awaaz (bed) |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | ek lamba dheema sur — is scene ka **ek hi swell** |
| PAPER | `ep01/sfx/raw_fs/s8_paper.mp3` | kaagaz / parcha (ungli, parche uthana) |
| WRITING | `ep01/sfx/raw_fs/s9_writing.mp3` | likhna — ginti ka darj hona |
| WICKER | `ep02/sfx/raw_fs/wicker.mp3` | baithak ki chataai/moodhe ki halki charkharahat |
| CELLO | `ep02/sfx/raw_fs/cello.mp3` | ek hi bowed phrase — "tables kam theek hain" ka bhulaav |
| CROWD | `ep03/sfx/raw_fs/crowd.mp3` | dheemi bheed ki bhoorh — shabd samajh nahi aate |
| synth | mix script mein banti hain | `gust` (deepak ki lau, raat ki hawa), `low_tone` (raat bhar ki ginti, aakhri sawal) |

Sarangi jaan-boojh kar nahi liya: uska kaam naam ka hai, aur naam ka pal yahan **tanpura + duck** sambhalte hain.

## Cue table (anchors are phrase-locked; `#` id = JSON ka `id`)

| # | cue (line jispar land karta hai) | sound | lands on the phrase | level under the voice | pan | fades |
|---|---|---|---|---|---|---|
| A1 | "Jaipur. Raat." | AIR in + VILLAGE in | bed, `start: 0.0` | −24 / −27 dB | 0.0 | 2.0 s fade in (mixer ka default envelope), poore scene tak hold |
| 1 `paper1` | "Mez par do purane kaagaz." | PAPER ×1 | `मेज पर दो पुराने कागज़` | −22 dB | −0.20 | 1.4 s, offset −0.5 s (parcha rakha jaata hai) |
| 2 `flame` | "Aur ek deepak." | GUST, `lowpass=1200` — deepak ki lau ka hilaav | `और एक दीपक` | −27 dB | +0.35 | 1.8 s, 0.4 s in / 0.6 s out |
| 3 `paper2` | "Ab dono parche saath rakhe jaate hain." | PAPER ×1 | `दोनों परचे साथ रखे` | −23 dB | −0.30 | 1.2 s, offset −0.4 s |
| 4 `finger` | "Ek aadmi ungli rakh kar ek line padhta hai." | PAPER ×1 (ungli ka sarsaraana) | `एक आदमी उंगली` | −21 dB | −0.30 | 1.6 s, offset −0.3 s — scene ka sabse nazdeeki foley |
| 5 `lean` | "Doosra wahi line apne parche par dhoondhta hai." | WICKER (chataai ki charkharahat) | `अपने परचे` | −26 dB | −0.15 | 1.1 s, offset −0.2 s |
| 6 `tally` | "…chup-chaap ginti mein darj ho jaata hai." | WRITING | `दर्ज हो जाता` | −22 dB | −0.15 | 1.8 s, offset −0.2 s |
| 7 `nighttone` | "Ye ginti raat bhar chalti hai." | LOW_TONE (70 Hz, synth) | `गिनती रात भर चलती` | −26 dB | 0.0 | 4.0 s, 1.5 s in / 1.5 s out — raat ka lamba waqt |
| 8 `tables` | "Portugal ki tables kam theek hain." | CELLO — ek hi bowed phrase | `पुर्तगाल की टेबल्स कम ठीक` | −25 dB | 0.0 | 3.5 s, offset −2.0 s, 0.8 s in / 1.2 s out |
| S1 | "Ye aaj ki baat nahi hai." → ident | TANPURA — **ek hi swell** | `आज की बात नहीं` (chalu), `नमस्कार` par −0.25 s out | −24 dB | 0.0 | points: −60 → −4 (3 s) → −1 (11 s) → 0 (hold) → −60; layer est. 55.7 → 105.35 s |
| D1 | "Us raja ka naam Sawai Jai Singh hai." | **duck** ×1 — beds + tanpura 0.30 par | `राजा का नाम सवाई जय सिंह` | pre 1.5 s / post 2.4 s / gain 0.30 | — | naam akela landta hai, phir tanpura wapas ubharta hai |
| 9 `crowd` | "Uske aas-paas kuch log aur bhi hain." | CROWD (bhoorh, shabd nahi) | `कुछ लोग और भी` | −27 dB | +0.35 | 4.5 s, offset −0.3 s, 1.0 s in / 1.5 s out |
| 10 `breeze` | "Us raat, us chhat par, ek baat saaf dikh rahi thi." | GUST — chhat par se guzarti raat ki hawa | `उस रात उस छत पर` | −26 dB | +0.45 | 3.0 s, offset −0.5 s, 1.0 s in / 1.5 s out |
| 11 `bigdi` | "To phir baat kahan bigdi?" | LOW_TONE (synth, chhota) | `तो फिर बात कहां बिगड़ी` | −24 dB | 0.0 | 1.4 s, offset −1.0 s, 0.2 s in / 0.8 s out — phir sannata |
| E1 | "Namaskar, main hoon Asha…" | sab out | — | — | — | beds ident se 0.25 s pehle khatam (bed ka default 1.2 s fade out); tanpura apne points se usse bhi ~2 s pehle chup |
| F1 | ident ke teen lines → body | dead air | — | — | — | 1.2 s asli sannata, phir "## Ab tak" ka pehla shabd |

Kul **11 spot cues** + 2 beds + 1 score. Sabse unchi cue −21 dB; koi cheez −16 dB se oopar nahi
(house rule). Door/khuli cheezein (deepak, bheed, chhat ki hawa) seedhe daayen, foley hamesha thoda
baayen, voice beech mein.

## Swar (score) — sirf ek swell

Score sirf ek hai: **TANPURA**, aur wo ek hi baar aata hai. Wo `आज की बात नहीं` par chalu hota hai
(script ki apni SFX line wahi jagah hai), 3 s mein ubharta hai, 11 s tak chadhta hai — yaani theek us
waqt poora khulta hai jab `उस राजा का नाम सवाई जय सिंह है` aata hai — aur D1 ka duck us naam ko akela
kar deta hai. Uske baad dheema-dheema ghulta hai (points ka aakhri hissa) aur **ident se 0.25 s pehle
poora chup** ho jaata hai. Ek entry, ek swell, ek exit — bas.

`tables` (CELLO) score nahi hai, wo ek spot cue hai: "Portugal ki tables kam theek hain" — ek hi bowed
phrase, bila melody, sirf rang. Sarangi is episode ke cold open mein nahi hai.

## Kahan chup rehna hai

- **Teen beats jahan jaan-boojh kar koi cue nahi hai:** (1) `आसमान। ग्रह। तारे। उनके चलने का वक़्त।` —
  sirf do beds, koi foley nahi; (2) `उनका घेरा छोटा था।` — galti ka kaaran bina kisi awaaz ke girta hai,
  agla sound tanpura hai; (3) naam ke baad ka pal — `जिसे तारों को गिनती में बदलना आता था` — duck ke
  window mein kuch naya nahi daala, sirf tanpura laut kar aata hai.
- **Ident se pehle sannata:** `तो फिर बात कहां बिगड़ी?` ke baad ka low tone 1.4 s mein mar jaata hai,
  tanpura ~2 s pehle kho jaata hai, aur beds aakhri 1.2 s mein. Isliye "नमस्कार" lagbhag khaali hawa se
  aata hai — script ki line "tanpura ghulta hai; ident se pehle sannata" theek yahi hai.
- **Ident aur uski teen lines bilkul sookhi** hain — koi bed, koi cue nahi (G1 rule: no cue host intro
  ke aar-paar).
- **Body se pehle 1.2 s asli chuppi** (`dead_air.before_body_seconds`), phir "Ab tak" shuru.

## Awaaz list (exact files jo is plan mein use hue)

Beds: `ep02/sfx/raw_fs/air.mp3` (filter `highpass=90,lowpass=8000`) ·
`ep03/sfx/raw_fs/b1_village.mp3` (filter `lowpass=1400`).
Score: `ep03/sfx/raw_fs/tanpura.mp3` (filter `highpass=70,lowpass=6000`).
Foley/spot: `ep01/sfx/raw_fs/s8_paper.mp3` (×3 — parcha, parcha, ungli) ·
`ep01/sfx/raw_fs/s9_writing.mp3` · `ep02/sfx/raw_fs/wicker.mp3` ·
`ep02/sfx/raw_fs/cello.mp3` · `ep03/sfx/raw_fs/crowd.mp3`.
Synth (mix script): `synth:gust` (×2: deepak ki lau, chhat ki hawa) · `synth:low_tone` (×2: raat bhar ki
ginti, aakhri sawal).
Koi download nahi, repo pool ke bahar kuch nahi, aur koi doosri episode ki file nahi chhui.

## Kya sunayi dega

Raat ki chhat. Hawa chalti hai aur neeche soye shehar ki bhoorh bahut door, bahut dheemi rehti hai.
Mez par do parche rakhe jaate hain — kaagaz ki halki sarsaraahat, phir kisi ki ungli ek line par rukti hai.
Deepak ki lau ek baar dheere se hilti hai. Ginti ka likha jaana sunayi deta hai, aur raat bhar chalne wali
ginti ek lambi dheemi ghoonjh ban jaati hai. "Portugal ki tables kam theek hain" par ek hi uddas sur
uthata hai. Phir tanpura chalu hota hai, dheere-dheere ubharta hai — aur jaise hi naam aata hai, sab kuch
0.3 par dabb jaata hai, sirf naam bachta hai. Uske baad bheed ki dheemi bhoorh, chhat par se guzarti ek
hawa, aur ek chhota sawal: "To phir baat kahan bigdi?" — jiska jawab sirf sannata deta hai.
