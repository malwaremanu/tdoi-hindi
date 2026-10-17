# Ep 5.6 — SFX plan (cold open)

Cold open = `## Cold open` se host intro tak (353 narration shabd, chunk `c01`).
House style wahi hai: effects + ambience + score sirf cold open par, baaki episode saaf narration.
Narration anchor hai, har bed uske neeche baithta hai, host intro dry hai, aur intro se pehle ek
sannate ka pocket chhoota hai.

Scene ka rang do hisson mein badalta hai: **darbaar** (bhara hua par dheema kamra, ek jawan bhikshu,
samraat, mitti ka pyala) → **safar** (khuli sookhi sadak, registaan, pahaad, Hindustan) → **sawaal**
(chaar kone, pahaad ke us paar). Isi liye plan bhi do hisson ka hai: court ka bed + court ke teen
chhote object-cues (kadam, pyala, mitti), phir exit par bed badalta hai (sadak ki hawa + wicker),
aur aakhir mein sirf **ek tanpura** uthta hai jo bade sawal ke neeche ek baar swell karke intro se
pehle nikal jaata hai.

**Note (anchors).** `ep05_6/c01.txt` likhne ke waqt maujood nahi tha, is liye har `phrase` yahan
Roman script ke apne transliteration mein hai (2–6 shabd, cold open mein ek hi baar). Mix karte waqt
mixer inhe `ep05_6/c01.align.json` mein dhoondta hai (fuzzy, matra-blind), aur har cue ke saath ek
`fallback_at` bhi diya gaya hai — agar phrase na mile to wahi seconds pakde jaate hain. Jo phrases
pakke hain (kadam, pyala, mitti, ghol, wicker, kauwa, pothi) wo sab aam shabd hain, koi naam nahi;
"Husan Tsang" wala naam jaan-boojh kar kisi phrase mein nahi liya gaya. Ek baat dhyan mein rakhi gayi:
source text mein danda (।) shabd ke saath hi juda rehta hai, aur `है।`/`हैं।`/`था।` jaise chhote akshar
mixer ke 0.7 fuzzy threshold se neeche gir jaate hain — is liye koi bhi phrase kisi line ke aakhri
chhote shabd par nahi rukta (sab anchor us se ek shabd pehle ya beech mein hai).

## Cast (source files)

| id | file | what it is |
|---|---|---|
| B1 | `ep03/sfx/raw_fs/crowd.mp3` | darbaar/kamre ki dheemi bheed (koi saaf shabd nahi, koi sangeet nahi) |
| B2 | `ep03/sfx/raw_fs/wind.mp3` | sadak ki sookhi, registaani hawa (gritty) |
| M | `ep03/sfx/raw_fs/tanpura.mp3` | tanpura loop — poore cold open ka ek hi score |
| S1 | `ep03/sfx/raw_fs/steps.mp3` | lakdi ke farsh par dheeme kadam |
| S2 | `ep05/sfx/raw_fs/cup.mp3` | chhote mitti ke pyale ko rakhne ki halki thak |
| S3 | `synth:sand_trickle` | ek chutki sookhi mitti (mix script mein bani) |
| S4 | `ep05/sfx/raw_fs/liq.mp3` | pyale mein paani ka dheema ghoomna |
| S5 | `ep02/sfx/raw_fs/wicker.mp3` | peeth par wicker frame ki sookhi chir |
| S6 | `ep01/sfx/raw_fs/s5_crow.mp3` | ek door ka kauwa (Hindustan ki khuli hawa) |
| S7 | `ep01/sfx/raw_fs/s8_paper.mp3` | sookhi palm-leaf pothi ki sarsaraahat |

## Cue table (anchors phrase-locked; `fallback_at` sirf safety net hai, apne andaaze se)

| id | cue (kis line par) | sound | lands on the phrase | level (voice ke neeche) | pan | fades |
|---|---|---|---|---|---|---|
| B1 | "Saatvi sadi. China ki rajdhani." se "Wo pyala peeta hai." tak — kamre ki dheemi bheed | crowd.mp3 (highpass 150 / lowpass 5000) | start 0.0 s; end `निकल पड़ता` +1.5 s (fallback 66.1 s → 67.6 s) | −25 dB | 0.0 | in 2.0 s; samraat ke aane par (≈26 s) 1.5 dB neeche, nikalte waqt (≈65 s) wapas; out 1.5 s |
| M | "Par ye raasta ek-tarfa nahi tha." se sawalon ke ant tak — tanpura | tanpura.mp3 (highpass 70 / lowpass 6000) | entry `ये रास्ता` (fallback 88.4 s); exit `नमस्कार` −0.25 s | −24 dB, swell par −22 dB | 0.0 | in 4.0 s; ek swell; out intro se 0.25 s pehle |
| B2 | "Wo pyala peeta hai." ke baad — khuli sadak ki sookhi hawa | wind.mp3 (highpass 120 / lowpass 7000) | start `प्याला पीता` (fallback 65.0 s); end `आज का सवाल यही` +0.5 s (fallback 110.4 s → 110.9 s) | −24 dB | 0.0 | in 2.5 s; out 2.2 s |
| S1 | "Vidaai ke waqt T'ang samraat khud aate hain." — do dheeme, naap-tol kadam | steps.mp3 | `विदाई के` (fallback 25.5 s), cue −0.5 s | −19 dB | −0.3 | in hard; 2.4 s; out 0.25 s |
| S2 | "Wo ek pyala mangwate hain." — pyala rakhne ki halki thak | cup.mp3 (highpass 200) | `प्याला मंगवाते` (fallback 36.3 s) +0.5 s | −19 dB | −0.2 | in 0.005 s; 0.8 s; out 0.3 s |
| S3 | "Phir apni mutthi mein mitti lete hain." — ek chutki sookhi mitti | synth:sand_trickle | `अपनी मुट्ठी में` (fallback 38.5 s) +0.4 s | −19 dB | −0.15 | in 0.15 s; 1.8 s; out 0.5 s |
| S4 | "us mitti ko pyale mein ghol dete hain." — paani ka dheema ghoomna | liq.mp3 (highpass 200) | `मिट्टी को प्याले में` (fallback 46.0 s) +0.2 s | **−16 dB** (scene ka ek hi sabse ooncha cue) | −0.12 | in 0.1 s; 1.6 s; out 0.6 s |
| S5 | "Aur nikal padta hai." — wicker frame ki ek sookhi chir | wicker.mp3 (highpass 120 / lowpass 6000) | `और निकल पड़ता` (fallback 66.1 s) +0.6 s | −18 dB | −0.1 | in hard; 0.6 s; out 0.25 s |
| S6 | "Barason yahan ghoomta hai." — ek door ka kauwa | s5_crow.mp3 (highpass 200 / lowpass 6000) | `बरसों यहां घूमता` (fallback 70.9 s) +0.4 s | −24 dB | +0.5 | in 0.01 s; 1.2 s; out 0.3 s |
| S7 | "uske saath saikdon pothiyan hain." — pothi ki halki sarsaraahat | s8_paper.mp3 (highpass 300 / lowpass 6000) | `साथ सैकड़ों पोथियां` (fallback 81.3 s) +0.3 s | −20 dB | −0.25 | in 0.01 s; 1.2 s; out 0.4 s |
| D | "Bhikshu ka naam Hsuan Tsang hai." — naam akela | duck (poori layer) | `भिक्षु का नाम` (fallback 57.2 s) | pre 1.2 s, post 2.4 s, gain 0.30 | — | 3.6 s ki window |
| — | "Chaliye." ke baad, body se pehle | dead air | — | 1.3 s kuch bhi nahi | — | — |

## Score — ek hi tanpura, ek hi swell

Score **ek hi** hai aur **ek hi baar** aata hai: `ep03/sfx/raw_fs/tanpura.mp3`, highpass 70 /
lowpass 6000, pan 0.0, base −24 dB (score ki window −22…−26 dB).

- **Entry** `ये रास्ता` par (≈88.4 s): "Par ye raasta ek-tarfa nahi tha." Tanpura 4.0 s mein uthta hai.
  Yahi wo line hai jahan kahani ek-tarfa raaste se sawal ki taraf mudti hai.
- **Swell — sirf ek**: "wo pahaad ke us paar kaise pahunchi?" — "वो पहाड़ के उस पार" par +2 dB
  (base −24 dB → −22 dB), peak ≈117.9 s, 1.5 s ka hold, phir wapas. Yahan soch pahaad paar karti hai;
  is ek jagah ke ilawa score kahin nahi uthta.
- **Exit** `नमस्कार` par −0.25 s (≈123.25 s): tanpura intro se pehle poori tarah gayab; host intro
  ke neeche kuch bhi nahi rehta. (Score ke points uske apne entry se relative hain — align ke baad
  swell ko waveform par ek baar dohra kar dekh lena.)

## Kahan chup rehna hai

Sannata is cold open ka hissa hai, bharna nahi:

1. **"Us raaste par registaan hai. Barfeele darre hain. Aur daaku bhi. … Uska naam Bharat hai."** —
   Raasta yahan *bataaya* ja raha hai, tay nahi kiya ja raha. Koi hawa nahi, koi barf nahi, koi daaku
   ya ghode nahi. Sirf kamre ki dheemi bheed. "Uska naam Bharat hai" par koi cue nahi, koi duck nahi —
   naam wahi akela chalta hai (duck sirf ek baar hai, aur wo Hsuan Tsang wale naam par hai).
2. **"Bhikshu se kehte hain: ise pi lo."** aur **"Wo pyala peeta hai."** — Samraat ke shabd, phir
   bhikshu peeta hai: koi ghoont, koi saans, koi pyala nahi. Bed badalna hi yahan "nikal gaya" kehta hai.
3. **"Wo yahan gyaan dhoondhne aaya tha. Aur pothiyan hi uski asli daulat thi."** — Pothi ki
   sarsaraahat (S7) ke baad aur tanpura ke entry ke beech kuch bhi nahi: saikdon pothiyan chup-chaap sambhal
   kar rakhi hui hain.
4. **"To aaj ka sawal yahi hai." ke baad ke do sawal** — Sadak ki hawa yahin khatam ho jaati hai,
   is liye dono sawal akeli tanpura ke saath, bina bed ke chalte hain.
5. **Intro ke pehle** — `नमस्कार` se 0.25 s pehle tanpura band; "Chaliye." aur "Ab tak" ke beech
   1.3 s ka sannata. Body par kuch bhi nahi (poore episode mein SFX sirf cold open ka hai).

## Sound list (exact paths jo use hui)

Beds aur score: `ep03/sfx/raw_fs/crowd.mp3`, `ep03/sfx/raw_fs/wind.mp3`, `ep03/sfx/raw_fs/tanpura.mp3`.
Foley: `ep03/sfx/raw_fs/steps.mp3`, `ep05/sfx/raw_fs/cup.mp3`, `ep05/sfx/raw_fs/liq.mp3`,
`ep02/sfx/raw_fs/wicker.mp3`, `ep01/sfx/raw_fs/s5_crow.mp3`, `ep01/sfx/raw_fs/s8_paper.mp3`.
Synth: `synth:sand_trickle` (mix_from_plan.py mein bani recipe).
Naya download: kuch nahi. `ep02/sfx/raw_fs/bass.mp3` (sub swell) yahan jaan-boojh kar nahi liya —
wo hill-wali episodes ka roop hai aur is scene mein mitti ke pyale ke neeche wo bhaari lagta hai.

## Kya sunayi dega

1. शुरू में एक बड़े कमरे जैसी धीमी भीड़ की आवाज़ होगी — कोई शब्द साफ़ नहीं, कोई संगीत नहीं।
2. सम्राट आएंगे तो कमरे की आवाज़ एक डिग्री नीचे हो जाएगी, दो धीमे क़दम आएंगे, प्याला रखने की हल्की तक आएगी, फिर मिट्टी गिरने और पानी में घुलने की छोटी आवाज़ — यही पूरे ओपन का सबसे ऊंचा cue है।
3. भिक्षु निकलते ही भीड़ की जगह सूखी रेगिस्तानी हवा आएगी, wicker की एक सूखी चिर होगी, और भारत पहुँचने पर एक दूर का कौआ और पोथी की एक हल्की सरसराहट।
4. नाम वाली लाइन — "भिक्षु का नाम..." — 1.2 सेकंड पहले से 2.4 सेकंड बाद तक पूरी आवाज़ नीचे रहेगी, ताकि सिर्फ़ नाम सुनाई दे।
5. "पर ये रास्ता एक-तरफ़ा नहीं था" पर अकेला धीमा तानपूरा उठेगा, "पहाड़ के उस पार कैसे पहुँची" पर एक बार ऊपर उठेगा, और "नमस्कार" से ठीक पहले चुप हो जाएगा — फिर नीचे लगभग डेढ़ सेकंड पूरा सन्नाटा।
