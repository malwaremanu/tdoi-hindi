# Ep 5.4 — SFX plan (cold open)

Cold open = `## Cold open` .. host intro + the roadmap line (426 narration words, chunk `c01`;
mota andaaza: 0.0-172.8 s, host intro kareeb 138.5 s). Signal chain aur levels wahi hain jo
Ep 3 / Ep 5 / Ep 6 / Ep 4.1 mein hain: **narration anchor hai**, har bed uske neeche baithta hai,
host intro sookha rehta hai, aur aakhri bed ka cut body se pehle ek khaali jhaalar chhodta hai.

Is episode ka signal do cheezein hain — **ghanti** (scene ki reedh; Part 11 mein wahi ghanti
bahut door se lauti hai) aur **vihara ka naam**, jise "Bihar" nibhata hai. Poora cold open
thanda, sookha aur khaali hai; sabse badi aawaz ek hi hai — wo ek ghanti.

## Cast (source files)

| id | file | what it is |
|---|---|---|
| AIR | `ep02/sfx/raw_fs/air.mp3` | sookhi, thandi hawa (bed) |
| DRONE | `ep02/sfx/raw_fs/drone.mp3` | lamba, neeva sur — khaali patthar ka hall (bed) |
| STREAM | `synth:river_wash` | patli dhaar, puliya ke neeche |
| STRIKE | `ep01/sfx/raw_fs/s3_stab.mp3` | ghanti ka ek chotta, bhaari stroke |
| RING | `ep02/sfx/raw_fs/bass.mp3` | ghanti ka goonj (sub, `lowpass=200`) |
| DOOR | `ep03/sfx/raw_fs/door.mp3` | pehla lakdi ka darwaza |
| CREAK | `ep02/sfx/raw_fs/wicker.mp3` | sau darwazon ki halki-halki chaap |
| STEPS | `ep03/sfx/raw_fs/steps.mp3` | nange pair patthar par (teen baar: aahat, kataar, ghisi seedhi) |
| LATCH | `ep01/sfx/raw_fs/s6_latch.mp3` | chhoti si kundi — "ye ek ghar hai" |
| STONE | `synth:stone_scrape` | patthar ke khandhar |
| SARANGI | `ep03/sfx/raw_fs/sarangi.mp3` | ek bowed phrase — naam "Bihar" par |
| TANPURA | `ep03/sfx/raw_fs/tanpura.mp3` | score (sirf ek baar) |

Script ke chaar inline `[SFX: …]` markers aise lagte hain: **ghanti** → STRIKE + RING (magar
"Ek ghanti bajti hai" wali line par, taaki ghanti sach mein ek hi baar baje — cold open ke top par
pre-lap nahi), **lakdi ke darwaze** → DOOR + CREAK, **nange pair** → STEPS ×2, **tanpura** → score.

## Cue table (anchors phrase-locked; neeche diye times whisper word-timings ke andaaze hain
aur waveform par dobara spot karne padenge — phrase hi asli anchor hai)

| # | cue | sound | lands on the phrase | level | pan | envelope |
|---|---|---|---|---|---|---|
| A1 | paani ki patli dhaar | STREAM | **पानी की पतली धार** | −26 dB | +0.3 | 1.5 s in, 2.0 s out; 5 s, dheere LFO |
| B1 | ghanti — ek bhaari stroke | STRIKE | **एक घंटी बजती** | **−18 dB** | 0.0 | attack 5 ms, out 0.35 s; scene ki sabse badi aawaz |
| B2 | ghanti ka goonj | RING (sub, `lowpass=200`) | **एक घंटी बजती** | −24 dB | +0.15 | 0.15 s in, 4 s out; 6.5 s tak goonjta hai, darwaazon se pehle khatam |
| C1 | pehla lakdi ka darwaza | DOOR | **दरवाजे खुलते** | −20 dB | −0.25 | 0.02 s in, 0.5 s out |
| C2 | sau darwaze, ek saath | CREAK | **दरवाजे खुलते** | −23 dB | +0.45 | 0.5 s in, 1.4 s out; "एक। दो। दस। सौ।" ke neeche khulta hai |
| D1 | nange pair, patthar par | STEPS (`highpass=180`) | **नंगे पैरों की आहट** | −22 dB | −0.3 | 0.1 s in, 1.0 s out; 3.2 s |
| D2 | lambi kataar, aur door | STEPS (`highpass=220`) | **लंबी कतार** | −25 dB | +0.35 | 0.4 s in, 1.4 s out; bhikshu ki chuppi mein ghul jaata hai |
| E1 | chhoti kundi | LATCH | **ये एक घर** | −24 dB | −0.25 | 0.02 s in, 0.2 s out; ek hi click |
| F1 | patthar ke khandhar | STONE | **पत्थर के खंडर** | −24 dB | −0.15 | 0.05 s in, 0.4 s out; 1.4 s |
| F2 | ghisi hui seedhi | STEPS (`highpass=250`) | **सीढ़ी घिसी हुई** | −26 dB | +0.5 | 0.8 s in, 1.4 s out; 3 s, bahut door — wahi pair, hazaar saal baad |
| G1 | naam "Bihar" | SARANGI | **विहार का बिहार** | −23 dB | 0.0 | 0.5 s in, 1.8 s out; naam akela land karta hai |
| S1 | score: tanpura | TANPURA | **पंद्रह सौ साल** (entry) → **नमस्कार** −0.25 s (exit) | −25 dB (peak −23) | 0.0 | ek entry, ek swell (neeche) |

**Spot cues: 11** (A1 + B ×2 + C ×2 + D ×2 + E1 + F ×2 + G1; S1 score alag layer hai). Sabse zor ki
headroom B1 ke paas hai; koi bhi cue −16 dB se upar nahi jaata, aur koi cue host intro (138.5 s)
ko cross nahi karta — aakhri cue 124.3 s par khatam ho jaata hai.

## Score (sirf ek entry, sirf ek swell)

Tanpura `ep03/sfx/raw_fs/tanpura.mp3` (`highpass=70,lowpass=6000`), level −25 dB, pan 0.0,
points `[[0,−60],[3,0],[11,+2],[20,+1],[38,+1],[46,0],[51.3,−60]]`:

- **Entry** `पंद्रह सौ साल` par (kareeb 86.9 s) — "Aaj se kareeb pandrah sau saal pehle is desh
  mein aise hazaaron vihara the." Wahi line jo ghar ko paimane mein badalti hai. 3 s mein up.
- **Swell** +2 dB (kareeb 98 s), jab "hajaaron vihaar the … jahan ek saath hazaar log rehte the"
  aata hai — episode ka sabse bada daava. Yahi ek swell hai, poore cold open mein doosra nahi.
- **Settle** +1 dB (kareeb 107 s) "Aur aaj? … khandhar … seedhi ghisi hui hai" ke liye, aur 0 dB
  (base) do aakhri sawalon ke liye — wahan score sirf neeche leta hai, bolta nahi.
- **Exit** `नमस्कार` se 0.25 s pehle (points ke aakhir mein −60 dB). Host intro ke baad kuch nahi.
- Tanpura ke upar naam wali sarangi (G1) ek **spot cue** hai, score nahi — is liye "ek hi entry" ka
  niyam nahi tootta; wo tanpura ke `+1` floor par ek chhoti bowed phrase hai, jaise tanpura ke upar
  sarangi baithti hai. Dono ko ek hi Sa par rakhiye (tanpura ko need ho to ek semitone shift kijiye),
  warna drone ke neeche sarangi besura lagegi.

## Kahan chup rehna hai

1. **0.0–12.0 s** — andhera, thandi subah, pahaadi ke neeche imaarat, sau kamre. Sirf AIR + DRONE,
   koi spot cue nahi. Pehli cheez jo sunayi degi wo paani hai (12.1 s), aur pehla event ghanti
   (36.4 s). Ye 36 second ka khaali hissa jaan-boojh kar hai: imaarat abhi so rahi hai.
2. **52.9–74.2 s** — "Kisi mein jaldi nahi. Koi kisi se kuch nahi kehta." se "Naam tak chhod chuke
   hain." tak koi cue nahi: na kadam, na bheed ki bhoorbhooraahat, na ghanti. Sabse zyada matlab
   isi khamoshi ka hai — bhikshu khud chup hain, aur yahi unka "shor" hai.
3. **Do aakhri sawal (kareeb 131.7–137.7 s)** — "Is ghar ne apne desh ke saath kya kiya? … usne is
   desh ke saath kya kiya?" par koi spot cue nahi; tanpura apne base par hai. Ye sawal nahi sajte.
4. **Host intro (138.5 s) aur uske baad ka roadmap** — beds aur score dono 0.25 s pehle out. Intro
   sookha, roadmap sookha (house rule: cold open ke baad poora episode saaf hai).
5. **Roadmap ke baad 1.2 s sach me khaali** (`dead_air.before_body_seconds`), phir body shuru.

## Rules jo nibhaye gaye

- Har `phrase` Devanagari hai, 2–6 shabd lambi, aur cold open mein **sirf ek baar** aati hai
  (sab 12 phrases check ki gayi hain — ek-ek occurrence). `fallback_at` har cue/duck par hai.
- Anchors un shabdon par khatam hote hain jinke baad vaakya khatam nahi hota (chhote shabd jaise
  "है", "सौ" se bach kar), kyunki alignment wale file mein danda shabd ke saath chipka rehta hai.
- Beds −23 / −26 dB (layer-wise; jodkar narration ke peak se kareeb −18 dB), score −25 dB
  (peak −23), foley −18 … −26. Koi cheez −16 dB se upar nahi. Beds aur score pan 0.0 par,
  voice dead centre.
- Dependency: **C1 aur C2 ek hi phrase** (`दरवाजे खुलते`) par tike hain, sirf offset alag hai —
  pehla darwaza, phir sau. Do cue, ek hi lamha, do pan.
- Duck sirf ek (`name_duck`): window kareeb 82.9–86.4 s, gain 0.30, pre 1.3 s / post 2.2 s.
  "इसका नाम है विहार" akela land karta hai, aur uski window tanpura ke entry (86.9 s) se
  0.56 s pehle band ho jaati hai — score par duck ka koi asar nahi.
- Koi cue host intro ko cross nahi karta; jo bhi layer chali, wo `नमस्कार` − 0.25 s par khatam.

## Sound list (exact paths)

Beds: `ep02/sfx/raw_fs/air.mp3`, `ep02/sfx/raw_fs/drone.mp3`.
Foley/spot: `ep01/sfx/raw_fs/s3_stab.mp3`, `ep01/sfx/raw_fs/s6_latch.mp3`,
`ep02/sfx/raw_fs/bass.mp3`, `ep02/sfx/raw_fs/wicker.mp3`, `ep03/sfx/raw_fs/door.mp3`,
`ep03/sfx/raw_fs/steps.mp3`.
Score: `ep03/sfx/raw_fs/sarangi.mp3` (naam), `ep03/sfx/raw_fs/tanpura.mp3`.
Synth recipes (mix script se): `synth:river_wash`, `synth:stone_scrape`.
Naya download kuch nahi — sab repo pool se.

## Kya sunayi dega

1. शुरू में सिर्फ़ ठंडी सूखी हवा और एक धीमा नीचा सुर रहेगा — कहीं कोई आवाज़ नहीं, जैसे इमारत अभी सो रही हो।
2. पानी की पतली धार कहीं नीचे बहती रहेगी, और फिर एक ही बार भारी घंटी बजेगी, जिसका गूंज लंबे तक रहेगा।
3. घंटी के बाद एक लकड़ी का दरवाज़ा खुलेगा, फिर सौ दरवाज़ों की हल्की-हल्की चरमराहट — बस इतनी सी, कोई बोलेगा नहीं।
4. नंगे पैरों की धीमी आहट बाईं तरफ़ से आएगी, लंबी क़तार दाईं तरफ़ दूर चली जाएगी, और फिर एक कुंडी की छोटी सी क्लिक के साथ पूरा सन्नाटा।
5. "विहार" के नाम पर सारी आवाज़ें दब जाएँगी, और "पंद्रह सौ साल" पर तानपूरा शुरू होकर "हज़ारों विहार थे" पर एक बार ऊपर उठेगा।
6. आज के खंडहर पर पत्थर की घिसट, घिसी हुई सीढ़ी पर वही क़दम बहुत दूर से, और "विहार का बिहार" पर एक सारंगी — इसके बाद नमस्कार से पहले सब ग़ायब।
