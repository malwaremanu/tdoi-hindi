# Ep 4.4 — SFX plan (cold open)

Cold open = `## Cold open` .. "Namaskar, main hoon Asha…" ke baad ke teen sawal — 482
narration shabd, chunk `c01`. Signal chain wahi hai jo Ep 3 / Ep 4.1 mein thi: narration
anchor hai, har bed uske neeche baithta hai, host intro sookha rehta hai, aur aakhri bed
body se pehle ek dead-air pocket chhodta hai.

Is episode ka cold open 4.1 se alag jagah khada hai: scene Himalaya ki ek choti — Kailash —
par shuru hota hai, neeche maidan ko dekhta hai, aur "do kitaabein + ek naqsha" ke vaade par
khatam hota hai. Isliye lead bed **hawa** hai (choti par tez), doosra bed **maidan** hai
(nadiyan, gaon, khet), aur teesra **gaon** sirf tab tak chalta hai jab tak scene Nehru ki
declared kalpana na ban jaaye. Score ek hi baar aata hai: shruti drone, "yahin se ek poori
duniya khulti hai" par andar, ek hi swell naqshe ke vaade par, aur host intro se 0.25 s pehle
out.

Script ke chaar inline cues (choti par hawa · door ki dhol ki thap · door ki mandir ki ghanti ·
dhol dheere-dheere paas) is plan mein mukhya cues hain; baaki cue har line se motivated hai.
Plan mein 12 spot cue hain (seema ke andar).

Devanagari anchors ghar ke transliteration se liye gaye hain (jo `tools/audio/transliterate.py`
4.4 ke cold open par deta hai), taaki `phrase` mix ke waqt asli narration se match kare.
Second waale numbers (fallback_at, points) 2.7 shabd/sekond par ganine gaye hain — 4.1 ke take
ka asli rate — aur alignment ke baad dobara spot karne hain.

## Cast (source files)

| id | file | kya hai |
|---|---|---|
| HAVA | `ep03/sfx/raw_fs/wind.mp3` | choti par tez, thode grit wali hawa (lead bed) |
| MAIDAN | `ep02/sfx/raw_fs/air.mp3` | khula, sookha maidan (doosra bed) |
| GAON | `ep03/sfx/raw_fs/b1_village.mp3` | gaon/khet ki door wali zameen (teesra bed) |
| SHRUTI | `ep03/sfx/raw_fs/shruti.mp3` | shruti-box drone — is scene ka poora score |
| SARANGI | `ep03/sfx/raw_fs/sarangi.mp3` | ek bowed phrase (naam ke lamhe ke liye) |
| DHOL | `ep01/sfx/raw_fs/s3_stab.mp3` + `lowpass=300` | dhol ki thap — hard impact ko lowpass se dhol jaisa banaya gaya (3 baar: door, phir paas) |
| GHANTI | `ep05/sfx/raw_fs/cup.mp3` + `highpass=300,lowpass=6000` | mandir ki door wali ghanti, ek hi baar — pool mein bell nahi hai, struck-cup ka ring + lambi fade door ki ghanti jaisa padhta hai |
| CROWD | `ep03/sfx/raw_fs/crowd.mp3` | bazaar ki chah-chah (kabhi samajh aane wale shabd nahi) |
| CHUCKLE | `ep03/sfx/raw_fs/chuckle.mp3` | door wala jashn (ek halki hansi) |
| WICKER | `ep02/sfx/raw_fs/wicker.mp3` + `highpass=350,lowpass=5200` | raat ki aag ki char-char — creak/reed ko crackle ki tarah |
| BASS | `ep02/sfx/raw_fs/bass.mp3` + `lowpass=200` | utarne ka khinchav (sub swell) |
| STEPS | `ep03/sfx/raw_fs/steps.mp3` | dhool par kadam — chhod kar jaana |
| synth | `mix_from_plan.py` mein bante hain | `gust`, `river_wash` |

## Cue table (anchors phrase-locked; times 2.7 shabd/sekond par ganine gaye, alignment ke
baad re-spot karne hain)

| # | cue | sound | jis phrase par land karta hai | level | pan | fades |
|---|---|---|---|---|---|---|
| B0 | teen beds in | HAVA + MAIDAN + GAON | scene ke shuru par; MAIDAN 9.2 s se khulta hai (11.5 s par poora, "Neeche nadiyan hain"), GAON 12.0 s se (14.5 s par poora, "Gaon hain. Khet hain") | −23 / −25 / −27 dB | centre | HAVA 2.5 s fade in; MAIDAN/GAON apne beat par khulte hain |
| A1 | "Himalaya ke un pahaadon" | `synth:gust` (3.5 s) | `हिमालय के उन पहाड़ों` (≈1.9 s, offset −1.2) | −22 dB | +0.30 (door/right) | 1.2 s in, 1.4 s out |
| A2 | "Uska naam Kailash hai." | SARANGI (3.2 s) | `उसका नाम कैलाश` (≈4.4 s, offset −1.9) | −23 dB | centre | 0.4 s in, 1.6 s out; naam ke aas-paas sab kuch duck (D1) |
| A3 | "Neeche nadiyan hain." | `synth:river_wash` (5 s) | `नीचे नदियां` (≈10.4 s, offset −1.0) | −27 dB | +0.45 (wide) | 1.5 s in, 1.5 s out |
| A4 | "Kaise jashn manate hain" | CHUCKLE (1.2 s) | `कैसे जश्न मनाते` (≈22.6 s, offset −0.6) | −24 dB | +0.40 | 0.05 s in, 0.5 s out |
| A5 | "Bazaar ki chah-chah" | CROWD (5 s) | `बाजार की चाह-चाह` (≈26.7 s, offset −1.8) | −25 dB | +0.50 | 1.5 s in, 1.5 s out |
| A6 | "Aag ke aas-paas baithi ek toli" | WICKER, filtered (6 s) | `आग के आस-पास बैठी एक टोली` (≈32.6 s, offset −3.0) | −24 dB | −0.30 (paas, thoda left) | 1.5 s in, 2.5 s out |
| B1 | "Unhe neeche utarne ka mann karta hai." | BASS (6 s) | `नीचे उतरने का मन करता` (≈40.4 s, offset −1.0) | −26 dB | centre | 3 s in (transient nahi), 2.5 s out |
| B2 | "Ye aadmiyon ke beech khelte hain." | DHOL, lowpass (0.9 s) | `ये आदमियों के बीच खेलते` (≈50.4 s, offset −0.4) | −22 dB | +0.40 (door, maidan mein) | 0.005 s in, 0.35 s out |
| C1 | "Kalpana kijiye" | GHANTI (cup, 6 s) | `कल्पना कीजिए` (≈81.5 s, offset −0.3) | −24 dB | +0.35 (door) | 0.01 s in, 4 s out; GAON bed isi se ~1.5 s pehle chala jaata hai |
| C2 | "Aaj koi unhe sach nahi maanta" | STEPS (3 s) | `आज कोई उन्हें सच नहीं मानता` (≈114.8 s, offset −0.5) | −24 dB | −0.35 | 0.02 s in, 0.6 s out — Yunan ke devta chhod diye gaye |
| D2 | "Ek din in kahaniyon ko" | DHOL, lowpass (0.9 s) | `एक दिन इन कहानियों को` (≈150.4 s, offset −0.4) | −19 dB | +0.25 | 0.005 s in, 0.35 s out |
| D3 | "do kitaabon mein baandh diya jayega" | DHOL, lowpass (0.9 s) | `दो किताबों में बाँध दिया जाएगा` (≈152.6 s, offset −0.4) | **−16 dB** | +0.10 | 0.005 s in, 0.35 s out — scene ka sabse tez block, isi ek cue ko −16 ki chhoot |
| E1 | "Namaskar, main hoon Asha…" | kuch nahi | — | — | — | teen beds + score intro se 0.25 s pehle out; intro aur uske teen sawal sookhe |
| E2 | teen sawal → body | dead air | — | — | — | 1.4 s ki chuppi, phir "Ab tak" ka pehla shabd |

## Score (ek hi swell)

Ek hi score layer: `ep03/sfx/raw_fs/shruti.mp3`, base −26 dB, `highpass=70,lowpass=5000`.

- **Andar aata hai** `यहीं से एक पूरी दुनिया खुलती` par (≈64.8 s) — yaani jab narration
  kehta hai ki yahin se ek poori duniya khulti hai. Pehle se pehle nahi: Kailash, choti,
  neeche ka maidan aur devta — sab kuch sirf hawa/maidan/gaon se bante hain, score nahi.
- **Ek hi swell**: "Har saal kahani ban kar lautte hain" (≈124.8 s) se chadhta hua
  `दो किताबों में बाँध दिया जाएगा` par +3 dB, aur `...एक पूरे देश का नक्शा` par +4 dB
  (≈155.5 s) — poora peak −22 dB par. Yahin scene ka emotional apex hai: do kitaabein + naqsha.
- **Out**: host intro se 0.25 s pehle (`नमस्कार` + `end_offset −0.25`); aakhri 2 s mein
  −60 dB tak girta hai. Intro aur uske teen sawal bilkul sookhe chalti hain — episode ka
  baaki hissa saaf narration hai.
- Envelope `points` **layer ke apne start se 0-based** hain (0 … 92.7 s), kyunki mixer ka
  `env()` `t = arange(n)/SR` se ginta hai. (4.1 ki score file mein points absolute seconds
  mein likhe the, jisse wo layer chup ho jaati thi — yahan wo galti nahi dohrai gayi.)

## Kahan chup rehna hai (silence > sound)

1. **Do beat andar jaan-boojh kar khaali hain** (koi spot cue nahi, sirf beds):
   - `पहले उन्हें शक्ल लेनी पड़ेगी। नाम चाहिए होंगे। घर चाहिए होंगे…` (≈56–64 s) — devta
     shakl le rahe hain; ye list sun-ne wali hai, uske upar kuch nahi.
   - `पर रुकिए। ये कहानियां आईं कहाँ से? … और कब?` (≈143–148 s) — hook-out sawal.
     Yahin score bhi sirf hold karta hai, chadhta nahi.
2. **Naam par hush (duck D1):** "Uska naam Kailash hai." — `pre 1.3 s`, `post 2.4 s`,
   `gain 0.3`. Hawa, maidan, gaon, sarangi aur narration, sab ~10 dB neeche gira kar sirf naam
   ko baithne dete hain. Is scene mein **ek hi duck** hai.
3. **Chhoti si chuppi pehle intro se:** beds `नमस्कार` se 0.25 s pehle out (points 155.0 →
   157.55 s par −60 dB), taaki intro ka pehla shabd saaf, sookha uthe.
4. **Body se pehle:** teen sawal poore hone ke baad `dead_air.before_body_seconds = 1.4 s`
   sachchi chuppi, phir "Ab tak" ka pehla shabd. Ye us body ka darwaza hai.

## Level bands (voice reference)

| kya | band | is plan mein |
|---|---|---|
| ambience beds | −21 … −27 dB | −23 (HAVA), −25 (MAIDAN), −27 (GAON) |
| foley / spot cues | −18 … −24 dB | −22, −23, −24 (−24 sabse zyada baar), ek cue −16 |
| score | −22 … −26 dB | base −26, swell ka peak −22 |
| sabse tez block | ek cue ko −16 dB | `dhol_paas2` (D3) |

Sab kuch voice ke neeche hai; −16 dB se upar kuch nahi. Pan: voice centre; foley thoda left
(−0.35 … −0.10) — sirf `aag` (aag paas hai) aur `chal_chhod` (kadam chhod kar jaate hain);
door/wide cheezein right (+0.20 … +0.50) — `windgust`, `nadi`, `jashn`, `bazaar`, `dhol_door`,
`ghanti`, `dhol_paas1`. Beds aur score centre (0.0).

## Sound list (exact paths jo plan mein use hue)

```
ep03/sfx/raw_fs/wind.mp3        bed   highpass=140,lowpass=6500
ep02/sfx/raw_fs/air.mp3         bed   highpass=90,lowpass=8000
ep03/sfx/raw_fs/b1_village.mp3  bed   highpass=110,lowpass=7000
ep03/sfx/raw_fs/shruti.mp3      score highpass=70,lowpass=5000
ep03/sfx/raw_fs/sarangi.mp3     cue A2
ep01/sfx/raw_fs/s3_stab.mp3     cue B2, D2, D3   lowpass=300 / lowpass=350
ep05/sfx/raw_fs/cup.mp3         cue C1  highpass=300,lowpass=6000
ep03/sfx/raw_fs/crowd.mp3       cue A5
ep03/sfx/raw_fs/chuckle.mp3     cue A4
ep02/sfx/raw_fs/wicker.mp3      cue A6  highpass=350,lowpass=5200
ep02/sfx/raw_fs/bass.mp3        cue B1  lowpass=200
ep03/sfx/raw_fs/steps.mp3       cue C2
synth:gust                      cue A1
synth:river_wash                cue A3
```

Naya kuch download nahi kiya gaya; repo pool hi kaafi tha. Do jagah substitution hai (library
mein seedha sound nahi hai) aur dono neeche "shak" mein likhi hain.

## Shak / dhyan dene wali baatein

- **Ghanti (C1)**: pool mein mandir ki ghanti nahi hai. `cup.mp3` ka struck-cup ring,
  highpass/lowpass + 4 s ki fade ke saath door ki ghanti jaisa padhta hai — par ye replace
  kiya ja sakne wala choice hai.
- **Dhol (B2, D2, D3)**: `s3_stab.mp3` ek hard impact hai; `lowpass=300` uskse dhol ki thap
  banata hai. Teesri baar (D3) −16 dB par scene ka sabse tez block hai, kyunki script khud
  kehta hai "dhol dheere-dheere paas aati hui".
- **Aag (A6)**: `wicker.mp3` ka creak, filtered, raat ki aag ki char-char ban jaata hai.
- **Anchors**: saare 12 cue anchors cold open mein **ek-ek baar** aate hain (occurrence 1).
  Anchor ka aakhri shabd jaan-boojh kar aisa chuna gaya hai jo `।` par **nahi** khatam hota,
  ya itna lamba hai ki mixer ki 0.7 similarity poori kar de — `है` / `हैं` jaise chhote shabd
  aakhri jagah nahi rakhe gaye. Wajah: mixer ka `norm()` danda (U+0964) nahi hatata, isliye
  "रेत हटाते **हैं।**" jaisa phrase match nahi hota (4.1 ke `dig2`/`rubble` anchors isi wajah
  se fallback par chale jaate hain, aur chup-chaap galat jagah baithenge).
- **Seconds**: sab fallback/points 2.7 shabd/sekond par ganine gaye hain. Alignment ke baad
  points (beds aur score ke envelope) dobara spot karne hain — cue khud phrase par tik jaate
  hain.

## Kya sunayi dega (saaf-shabd mein)

1. Shuru mein oonchi choti par tez hawa, aur neeche se ek khula maidan khulta hai — nadiyon
   ki dhulai, gaon, khet, bazaar ki chah-chah, shaam ki aag ki char-char.
2. "Uska naam Kailash hai" par sab kuch ek pal ke liye dheema ho jata hai — hawa bhi, aur
   ek sarangi ki ek hi bowed phrase naam ko ghere rehti hai.
3. Devta jab neeche utarne ka sochte hain to zameen ke neeche se ek gehra sub girta hai,
   aur maidan mein kahin door ek dhol ki ek thap padti hai.
4. "Kalpana kijiye" par door ek mandir ki ghanti ek hi baar bajti hai, aur gaon wali zameen
   peeche chali jaati hai.
5. Aakhir mein dhol dheere-dheere paas aati hai — pehli thap door, doosri paas, teesri
   sabse tez — aur usi ke saath ek shruti drone chadh kar do kitaabon aur naqshe ke vaade par
   chhoota hai.
6. Phir sab chup. "Namaskar, main hoon Asha" sookha uthta hai, uske teen sawal bina kisi
   sound ke, aur body se pehle 1.4 second ki poori chuppi.
