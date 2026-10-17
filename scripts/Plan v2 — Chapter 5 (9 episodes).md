# Plan v2 — Chapter 5, "Through the Ages" → 9 episodes

Oct 17, 2026 · @Manupal Choudhary

Supersedes **§3.1** of `scripts/Ep 4+ — Chapter-to-Episodes Method.md` (the seven-episode table built on the lossy copy). Rules R1–R18 of that document still apply; this sheet is the phase A–E output for the nine-episode set. **No script is written or re-cut until this sheet is agreed.**

---

## 0. What changed, and why

**The source changed.** `book/chapters/ch05.txt` was a lossy copy: 28,033 words. `book/chapters_v2/ch05.txt` was rebuilt on 2026-10-17 from the Internet Archive full text: **43,296 words, 21 `## ` sub-sections**. The chapter lost more than a third of itself, and the loss was not spread evenly — it fell hardest on the sub-sections that carry the back half of the set:

| Sub-section | Lossy copy | v2 (real) | Gained |
|---|---|---|---|
| Growth and Decay | 1,360 | 3,105 | +1,745 |
| The Six Systems of Philosophy | 3,297 | 4,539 | +1,242 |
| India and Greece | 1,779 | 3,253 | +1,474 |
| The Old Indian Theatre | 2,235 | 3,556 | +1,321 |
| Mathematics in Ancient India | 1,541 | 2,727 | +1,186 |
| India and China | 2,129 | 3,597 | +1,468 |
| Old Indian Art | 1,404 | 2,361 | +957 |
| Indian Colonies and SE Asia | 2,238 | 3,195 | +957 |
| Nationalism & Imperialism under the Guptas | 943 | 1,591 | +648 |
| Progress versus Security | 1,139 | 1,553 | +414 |
| India and Iran | 2,129 (incl. Greece) | 1,888 | − (split wrongly) |

Two consequences. First, **the eight GAPs the old scripts flagged are now resolved in v2** (the Heliodorus inscription's three precepts, the poet's lines in "India's Urge to Freedom", Sylvain Levi / Sitwell / Epstein / La Place / Dantzig / Hogben / Stcherbatsky, the `$2a`–`$2b` truncations). Nothing needs to be checked against a library copy any more — only re-checked against v2 itself. Second, **seven episodes no longer fit**: at 28,033 words the chapter ran at 0.27–0.9× and the scripts that came out of it are fact blizzards; at 43,296 words a seven-episode set would run at 0.6–0.7× — worse. The owner's decision: **9 episodes**, source ≈ 4,800 words each, narration 5,000–5,200 each, **ratio ≈ 1.0×**. That is 9 × ~4,810 ≈ 43,300 — the chapter's own size. Nothing needs dropping and nothing needs listing.

**Set question (unchanged, it is the chapter's own):** *Itni chamak ke baad, thakaan kahan se aayi?*

**Set answer, built up across the nine payoffs.**
- 5.1 hamla-var apne ho gaye — kyunki darwaza khula tha; band hone laga jab "apna" ka matlab "sirf apna" hone laga.
- 5.2 padosi se rishta jang se nahi toota — samundar ke naye raaste ne toota.
- 5.3 do manch the — darbaar ka manch bahar chala gaya, gaon ka manch yahin raha.
- 5.4 vihara badh gaye, khet peeche reh gaye.
- 5.5 jo soch apne virodhi ko bhi ghol sakti hai, wo khuli jang kabhi nahi ladi.
- 5.6 raasta bahar ki taraf lamba khula tha — andar sab kuch ek hi soch mein simat raha tha.
- 5.7 jo bahar gaya wo patthar mein khada hai; jo ghar mein raha wo kho gaya.
- 5.8 sabse bada tohfa ginti ka tha — aur wahi sabse pehle ghar se nikal gaya.
- 5.9 thakaan bahar se nahi aayi. Darwaze band hue, to roshni andar hi dheemi padi. Aur jo vyavastha is samaaj ko sadiyon tak baandhe rakhi, usi ne nayi pratibha ka raasta band kar diya.

**Set answer, delivered to Ch 6:** *Hindsa* — the Indian numerals — reach Baghdad, and a chapter later the same road brings back a new world.

### 0.1 Set overview

| Ep | Title (slug) | Carrying question | Source (S-ids) | Source words | Narration | U ≤ |
|---|---|---|---|---|---|---|
| 5.1 | **Hamlavar jo apne ho gaye** (`ep05-1-hamlavar-jo-apne-hue`) | Itne hamlon ke baad Bharat Bharat kaise bana raha — aur darwaza band karna kab shuru hua? | S02, S03, S04, S05 | 4,633 | 5,050 | 70 |
| 5.2 | **Do bhai, ek dhun** (`ep05-2-do-bhai-ek-dhun`) | Bharat ke sabse purane padosi kaun the, aur unse rishta kaise toota? | S06, S07 | 5,141 | 5,100 | 65 |
| 5.3 | **Shakuntala ka safar** (`ep05-3-shakuntala-ka-safar`) | Jis bhasha mein koi ghar par baat nahi karta tha, uska natak duniya tak kaise pahuncha — aur ghar mein kyun ruk gaya? | S08, S09a | 5,397 | 5,150 | 60 |
| 5.4 | **Vihara se Bihar** (`ep05-4-vihara-se-bihar`) | Jo dharm logon ki zubaan mein bola, wo apne desh ke saath kya kar gaya? | S09b, S10, S11 | 4,603 | 5,050 | 45 |
| 5.5 | **Bina jung ki vidaai** (`ep05-5-bina-jung-ki-vidaai`) | Bharat ne Buddh dharm ko bina yuddh ke kaise ghol liya? | S12, S13, S14a | 5,197 | 5,100 | 60 |
| 5.6 | **Chaar kone, pahaad ke us paar** (`ep05-6-chaar-kone-pahaad-ke-us-paar`) | Jo soch is desh ke chaar kone tak pahunchi, wo pahaad ke us paar kaise pahunchi — aur wahan se kya laayi? | S14b, S15 | 5,283 | 5,100 | 70 |
| 5.7 | **Sone ki dharti** (`ep05-7-sone-ki-dharti`) | Bharat samundar ke us paar kya le gaya — aur kitne saal tak le jaata raha? | S16, S17 | 4,280 | 5,050 | 65 |
| 5.8 | **Ajanta ki auratein** (`ep05-8-ajanta-ki-auratein`) | Jis desh ki deewarein, dhaatu aur dawa duniya bhar mein bikte the, usne apna sabse bada tohfa kaise banaya? | S18, S19, S20a | 4,426 | 5,000 | 55 |
| 5.9 | **Shunya, aur phir dopahar** (`ep05-9-shunya-aur-phir-dopahar`) | Jo desh shunya khoj sakta tha, wo thak kaise gaya? | S20b, S21 | 4,205 | 5,050 | 50 |
| | | | **Total** | **43,165** | **~45,650** | |

Spine types (R4): 5.1 **object** (Heliodorus pillar) · 5.2 **pair** (two brothers, one tune) · 5.3 **pair of stages** · 5.4 **object** (the vihara) · 5.5 **mystery** (Malraux's question) · 5.6 **journey/road** (two roads: Shankara's and the pilgrims') · 5.7 **place** (the Land of Gold) · 5.8 **object** (the painted wall and the crafts behind it) · 5.9 **object → verdict** (the zero, then the afternoon).

**Balance check (R11).** Set average = 4,796 source words. Ceiling = 1.25× = 5,995. Heaviest episode: 5.3 at 5,397 (1.12×) — inside. Lightest: 5.9 at 4,205 (0.88×) — it is the finale, and a finale may sit under the average because its verdict material is the densest in the book. No episode exceeds the ceiling; none is below 0.87×; every narration target is 5,000–5,200 for a 32–33 minute cut at ~160 wpm.

**The S-id problem — read this before anything else.** The existing scripts use a 22-sub-section numbering taken from the lossy copy (S01…S22, with "Peaceful Development and Methods of Warfare" as its own S04). **v2 has 21 sub-sections and no "Peaceful Development" heading of its own** — its text sits inside S02 and the "India's Urge to Freedom" block. Moving forward, **v2 numbering (S01–S21) is the only numbering**. Mapping from the old scripts' ids:

| Old id (scripts 5.1–5.7) | v2 id | Sub-section |
|---|---|---|
| S01 | S01 | Through the Ages (heading only) |
| S02 | S02 | Nationalism and Imperialism under the Guptas |
| S03 | S03 | South India |
| S04 ("Peaceful Development and Methods of Warfare") | *inside S02/S04* | (no separate heading in v2) |
| S05 | S04 | India's Urge to Freedom |
| S06 | S05 | Progress versus Security |
| S07 | S06 | India and Iran |
| S08 | S07 | India and Greece |
| S09 | S08 | The Old Indian Theatre |
| S10 | S09 | Vitality and Persistence of Sanskrit |
| S11 | S10 | Buddhist Philosophy |
| S12 | S11 | Effect of Buddhism on Hinduism |
| S13 | S12 | How did Hinduism Absorb Buddhism in India? |
| S14 | S13 | The Indian Philosophical Approach |
| S15 | S14 | The Six Systems of Philosophy |
| S16 | S15 | India and China |
| S17 | S16 | Indian Colonies and Culture in South-East Asia |
| S18 | S17 | The Influence of Indian Art Abroad |
| S19 | S18 | Old Indian Art |
| S20 | S19 | India's Foreign Trade |
| S21 | S20 | Mathematics in Ancient India |
| S22 | S21 | Growth and Decay |

**Rebuild artifact to know about (not a fact, a layout quirk).** In v2 the `## ` heading lines are printed about one paragraph early: the true start of a sub-section is usually the *bare* heading line a few lines later, and a small block of text (~50–250 words) that belongs to one sub-section sits inside the previous sub-section's block. Practical rule for the writer: **open v2 at the sub-section's heading and read a paragraph before and after it**; the coverage table below names the clusters, so match on content, not on line position. Per-episode source figures here are approximate to ±3% for this reason; ~130 words in the file are rebuild residue (duplicate heading lines, footnote strips, OCR fragments such as the stray "Na" that is all of S01).

---

## 1. Numeric budget

| Item | Budget for this set |
|---|---|
| Source words per episode | 4,800 average (this plan: 4,205–5,397) |
| Narration per episode | **5,000–5,200 words = 31–33 min** at ~160 wpm. (This overrides R6's 4,200–5,000, which was written for the 30-minute ceiling; the owner's brief for the nine-episode set is 5,000–5,200. R6's ≥3,500 floor and 650-word beat ceiling stay.) |
| Ratio | narration ÷ source ≈ 1.0 (this plan: 0.95–1.21) |
| Beats | 8–11 per episode, 250–650 words each, one idea each (R12) |
| U atoms | **≤75 per episode**, ≤3 in any 160-word stretch (R16). Plan column budgets below. |
| Dates | ≤1 per beat unless the beat is *about* the date; everything else relative ("do saal baad", "dhai sau saal tak") |
| Numbers | round; ≤3 spoken per beat; big ones get a body; precise figures → T5 |
| Aaj-bridges | ≤2 inline + the closing "Aaj ke hisaab se" (≤200) |
| T5 "Kitaab mein aur" | ≤20% of the episode's U atoms; **never** a claim, an argument or an anecdote |
| Cold open | 300–450 words, the only slot with SFX |
| Ab tak | 50–60 words |
| Outro | ≤90 words, ends "Tab tak ke liye, namaskar." |

**U log (estimated, to be finalised in each script's Writer's check).** 5.1 ~58 · 5.2 ~60 · 5.3 ~52 · 5.4 ~38 · 5.5 ~54 · 5.6 ~66 · 5.7 ~62 · 5.8 ~48 · 5.9 ~44. Set total ~482, cap allows 675, so the binding constraint is *per-episode reads*, not the set — the danger zones are 5.2 (Greek and Persian names), 5.6 (Chinese pilgrims and place names) and 5.7 (Indonesian empires). Those three must run R17 signal 2 hard: **max 3 named items spoken per list, the tail to T5.**

---

## 2. Episode sheets

Words in the beat tables are **narration targets**. Tier key: T1 scene · T2 line · T3 cluster · T4 recap · T5 notes.

### 2.1 Ep 5.1: Hamlavar jo apne ho gaye

- **Premise.** After the Mauryas the door stayed open: Greek kings turned Buddhist, Shakas became Rajputs and Jats, Huns became petty chiefs — and the south, barely touched, grew rich on the sea. Then the Guptas turned absorption into a shell and the shell into a wall.
- **Carrying question.** *Itne hamlon ke baad Bharat Bharat kaise bana raha — aur darwaza band karna kab shuru hua?*
  **Answer (payoff).** *Bana raha kyunki usne har aane wale ko apna bana liya. Aur darwaza us waqt band hone laga jab "apna" ka matlab "sirf apna" hone laga — ye Gupta kaal ki chamakti hui khaal ke andar hi shuru ho gaya tha.*
- **Spine.** **Object:** the Heliodorus pillar at Besnagar — a Greek's words cut in Sanskrit. Returns in the payoff as Rajput, Jat, Kathi.
- **Cold open (rewrite the existing 5.1 cold open, now that v2 gives the inscription).** Besnagar, near Sanchi, 1st century BC. A granite pillar, a chisel, a man dictating in Sanskrit a sentence about himself. Reveal: he is a Greek. The line itself (this is now in the source and may be spoken once): *three precepts lead to heaven — self-restraint, sacrifice, care.* Close: *Ek Yunani, jo apni baat Sanskrit mein likhwa raha hai. Ye kaisa desh hai, jo apne hamla-varon ko bhi apna bana leta hai?* SFX: wind, stone dust, a chisel strike, tanpura on "Besnagar".
- **Owns.** S02 Nationalism and Imperialism under the Guptas 1,591 · S03 South India 893 · S04 India's Urge to Freedom 596 · S05 Progress versus Security 1,553 = **4,633 source / 5,050 narration**.

| # | Beat (Roman Hindi) | What happens in the story | Delivers (v2 clusters) | Words | U |
|---|---|---|---|---|---|
| — | Cold open + ident + Ab tak | see above; Ab tak = Ep 4.5's Ashoka outro, "a Greek envoy's Sanskrit pillar" paid off | S02-b (Heliodorus, Besnagar, three precepts) | 490 | 3 |
| B1 | Sookhi shaakha, naya beej | The Maurya tree fades to a smaller Sunga state; in Bactria, Greeks are spreading down | S02-a (Sunga, shrinking area, southern states, Bactrians/Indo-Greeks) | 380 | 4 |
| B2 | Do raah | The Yueh Chih push the Shakas out of the Oxus valley into north India; the Shakas and then the Kushans take India and India takes them | S02-c, S02-d (Shakas/Scythians, Seistan = Shakasthan, Yueh Chih, Kanishka; "some turned Hindu, most turned Buddhist"; patrons of Indian culture; nationalist undercurrent) | 400 | 7 |
| B3 | Chautha Chandra | Under the Kushans Buddhism splits; a schism is settled by debate, as this land settles things | S02-e (Mahayana/Hinayana, the great debates) + T4: Nagarjuna's full story is 5.5 | 340 | 4 |
| B4 | Shell | 320 AC the Guptas rise; a strong anti-foreign feeling turns into a hard beautiful shell; inside it, tolerance to everyone already in; outside it, a bar on the door | S02-f, S02-g (Gupta age, great rulers, anti-foreign feeling, synthesis, tolerance-inside/aggression-outside, "the shell was deep and wide") | 430 | 5 |
| B5 | Safed Hoon | A century and a half of the Guptas, a century and a half of successors; then the White Huns come in hordes, one of them (Mihiragula) leaves a memory, a prince (Baladitya) resists, a king (Yashovarman) wins a famous day — and then the Huns simply sink into the sea of India as petty chiefs | S02-h, S02-i (Gupta span 150 years, successors, White Huns, Mihiragula, Baladitya, Yashovarman; Huns' brief rule ~50 years, absorbed as petty chiefs) | 420 | 7 |
| B6 | Kanauj ka raja | North India's last glow: Harshavardhana of Kanauj (early 7th century), the Chinese pilgrim at his court; his death in 648 AC and the empire falls apart; Ujjayini waits | S02-j (Harsha, Kanauj, Hsuan Tsang, 648 AC, empire breaks, Ujjayini) + T4: Hsuan Tsang's own road is 5.6 | 390 | 5 |
| B7 | Samundar ki taaqat | South India, for over a thousand years: the Andhras beat the Shakas, then Pallavas, Chalukyas, Rashtrakutas, Cholas; Rajendra's ships to Ceylon and Burma; Greek colonies and Roman coins; and when the north is hit, the north's craftsmen move south | S03-a, S03-b, S03-c (1,000+ years, dynasties, Rajendra, Ceylon, Burma, sea trade, Greek colonies, Roman coins, northern migration incl. builders/craftsmen) | 460 | 8 |
| B8 | Do sau saal ki sarkar | A list of dynasties gives a wrong idea: each of them lasted two or three centuries — longer than the British Empire lasted in India | S02 tail + S03 tail (peaceful development: 1,000 years, Maurya/Kushan/Gupta and in the south Andhra/Chalukya/Rashtrakuta, 200–300 years each, no interference with the mass of people, agreements between warring states) | 360 | 3 |
| B9 | Jang ke niyam | Wars were fought under rules; Chanakya's book even describes machines that kill a hundred at once, and a kind of explosive, and trench warfare; and then: the Pax Britannica delusion | S03 (war theory, righteous war, Arthashastra machines/explosives/trench warfare; distressful periods, famine; "Pax Britannica first brought peace" as one of history's great delusions) | 350 | 3 |
| B10 | Soch, aur mila-jula khoon | The poet's famous lines about a patient East; the reply: India resisted every invasion, often successfully; the proudest "pure" stock in India is a mixture of five races; and what held it together was an idea — a passion for synthesis | S04-a, S04-b; S05-a..S05-j (poet's lines; always resisted; urge to freedom; Aryan/Dravidian/Turanian/Semitic/Mongolian mixture; geography and an idea of life; constant change; progress vs security; communal conformity with individual belief; flexibility; synthesis; Rajputs, Jats, Kathis as the typical Indians) | 470 | 8 |
| B11 | Hamlavar jo apne ho gaye (**payoff**) | Back to the pillar: the Greek's Sanskrit line is the whole method of this country in one stone — and the day the absorption stopped being welcome and became defence, the shell hardened | S02-b return + S05 end (every outside element gave something and took much; the last memory of this relationship is an invasion) | 400 | 3 |
| — | Aaj ke hisaab se | "Pure" blood is a modern idea, not an old Indian one; a country is held by an idea, not by walls | — | 180 | 0 |
| — | Outro (cliffhanger) | *"Us khamba par likhne wala Yunani tha. Par Sanskrit mein. Aur is desh ka sabse purana padosi Iran hai — na jang se alag hua, na mitti se. Ek dhun hai, jise do bhai sadiyon baad pehchaante hain."* | — | 80 | 0 |
| | | | **Total** | **~5,050** | **~58** |

*Reuses:* the existing 5.1 script entire — cold open idea, the eleven part titles, the pillar spine. **Patch required:** source line to `book/chapters_v2/ch05.txt`; lift the two GAP notes (Heliodorus inscription, the poet's lines) because v2 has them; rename S04/S05/S06 ids to v2 S04/S05.
*Kalpana:* the chisel scene at Besnagar, the moonlit courtyard (if kept).
*T5 for 5.1:* Dodwell's "absorbent like the ocean"; Vincent Smith on Muslim Turks; Childe; the full list of ten peoples; Marshall-style second quotes if used.

---

### 2.2 Ep 5.2: Do bhai, ek dhun

- **Premise.** The oldest neighbour shared a root, a court tongue and a grave-digger's aside about the Taj — "the soul of Iran in the body of India". The brilliant neighbour lived a short life, died young and left India its images.
- **Carrying question.** *Bharat ke sabse purane padosi kaun the, aur unse rishta kaise toota?*
  **Answer.** *Sabse purane padosi Iran the, aur sabse zinda bhi wahi hain. Unse rishta jang ne nahi toda — samundar ke naye raaste ne toda, jo is desh ko Asia se kaat kar Europe se jod gaye. Aur doosra padosi, Greece? Usse rishta kabhi lamba hua hi nahi. Wo doob gaya — par jaane se pehle apne but yahin chhod gaya: moorat ki puja is desh mein usi ke raaste aayi.*
- **Spine.** **Pair:** two brothers separated east and west, who recognise each other by an old flute tune. First image in the cold open, last image in the payoff.
- **Cold open (keep, verbatim from existing 5.2).** Allahabad, 1944: the leader of an Iranian cultural mission tells the legend of the two brothers. ~370 words. SFX: a room, a flute, distant street.
- **Owns.** S06 India and Iran 1,888 · S07 India and Greece 3,253 = **5,141 source / 5,100 narration**.
- **Beats — keep the existing eleven, unchanged:** B1 Ek mool, do raahein · B2 Parshavas se Parsi tak · B3 Darius ka sabse amir ilaaka · B4 Persepolis se Safed Bharat tak · B5 Farsi ghar mein, Iran imaarat mein · B6 Nadir Shah, aur band darwaze · B7 Chamak jo doob gayi · B8 Do desh, ek dhang · B9 Do ghar, do reet · B10 Taaza hawa · B11 But — ek lafz jo Buddha se aaya (**payoff**: image worship reaching India from Greece is the "but", and the flute returns).
- **Cluster map for the two sub-sections (write to this; word targets in brackets).**
  - S06: root shared before Indo-Aryan civilisation; Zoroastrian/Vedic; Pahlavi and Avesta close to Vedic Sanskrit; Persian as Asia's court language (Constantinople → Gobi); Persian in Indian courts till the British; modern Indian languages full of Persian (250); Iran absorbing its own invaders; Indus Valley seals resembling Iran/Mesopotamia; Achaemenian contacts; Avesta naming India; Parshavas → "Parsi"; Cyrus; Darius's Sind and west Punjab, "the richest and most populous province", Sind then green and now dry; Herodotus's 360 talents of gold dust; Indian troops in the Persian army; trade to Babylon before the 7th century BC (280); Alexander's aftermath, Persepolis and Ashoka's buildings; Graeco-Buddhist art; Kabul–Kandahar–Seistan, "White India"; north by land, south by sea, a southern kingdom's embassy to Iran (240); Turk/Afghan/Moghul conquests; the 15th-century Timurid Renaissance; the new architecture, Delhi and Agra, the Taj Mahal line (180); the last memory being Nadir Shah's invasion; the British barring every route; the Zoroastrian refugees as the one continuing bond; Iran looking back at its own pre-Islamic past (260); Rapson's naval-power quote → T5; the Allahabad legend → cold open and B11 (180).
  - S07: Nehru refusing the Orient/Occident split; Greek/Hebrew/Latin scholarship; Plato and Aristotle dominating; industry entrenching the difference (300); every people has its own message, Greece "definite and superb"; both lands found joy in the present, India's eyes also on the beyond; old Greece's short life (400); India nearer to old Greece than Europe is; the real secret is tenderness and tolerance, not esoteric doctrine (300); geography — no rivers, no forests, the sea; life accepted in both, belief in an inner life (350); Hellenism's experimental science at Alexandria; the burst of invention and the arithmetic/algebra advance (300); women — no seclusion in India, Greek women welcome at Indian courts, maids-in-waiting in the old plays, imports at Barygaza/Broach (280); Greek homosexuality and its acceptance → handle in one restrained line (100); contacts from the earliest times, the Ujjayini observatory, Alberuni in the 11th century (250); mutual influence, each strong enough, the modern reaction against crediting Greece with everything (250); **image worship came to India from Greece** — Vedic religion had no idols, no temples (300); the mind's passion for unity, and the thinkers who deny it (200).
- **Cliffhanger → 5.3.** *"Par ek cheez hai, jispar Europe ne sau saal bahas ki: is desh ka natak — kya wo Greece se aaya? 1789 mein ek Angrez ne ek natak ka anuvaad chhapa, aur Europe hil gaya."*
- *Reuses:* the existing 5.2 script entire (cold open, eleven parts, spine, SFX pointers). **Patch required:** v2 source line; re-check the `$2a`/`$2b` truncation marks and the three footnotes against v2 and lift whichever v2 resolves (the Zimmern footnote is now present); rename S07/S08 ids to v2 S06/S07.
- *T5 for 5.2:* Darmesteter on the borderland; Rapson; the Pahlavi/Avesta detail names; the full Persian-poet list.

---

### 2.3 Ep 5.3: Shakuntala ka safar

- **Premise.** A play that stirred Goethe; a stage that wrote no tragedies; and a language that no one spoke at home yet everyone educated understood — which travelled further than any Indian language ever did, and then stopped being where new thought happened.
- **Carrying question.** *Jis bhasha mein koi ghar par baat nahi karta tha, uska natak duniya tak kaise pahuncha — aur ghar mein kyun ruk gaya?*
  **Answer (payoff).** *Natak duniya tak isliye pahuncha ki wo un logon ki zubaan mein tha jo poore desh mein padhe-likhe the. Aur ghar mein wo isliye ruk gaya, kyunki usi zubaan ko koi ghar ki zubaan nahi bolta tha. Do manch the — darbaar ka manch, jo bahar chala gaya; aur gaon ka manch, jo yahin raha. Jo bahar gaya wo kho gaya; jo yahin raha, wahi sabse aage ki zubaan ban gaya.*
- **Spine.** **Two stages** (darbaar ka manch / gaon ka manch), opened in B6, paid off in B11.
- **Cold open (keep).** 1789: Jones's translation of Kalidasa's Shakuntala reaches Europe; a stir; Goethe. Note: this uses the source's own last paragraphs of S08 — the cold open runs ahead of the story, as 5.3 already does. ~360 words.
- **Owns.** S08 The Old Indian Theatre 3,556 · **S09a** = S09 minus the language-family tail (**1,841 of 2,470**) = **5,397 source / 5,150 narration**.
- **Beats (existing eleven; only B10 shrinks, B11 is rewritten).**

| # | Beat | What happens | Delivers (v2 clusters) | Words | U |
|---|---|---|---|---|---|
| — | Cold open + ident + Ab tak | Jones, 1789, Goethe; Ab tak = Ep 5.2's Greece question | S08 (Jones, 1789, editions, Goethe, Faust prologue) | 420 | 4 |
| B1 | Europe ka sawal | Did India borrow its drama from Greece? Two reasons it seemed plausible, and a whole century of argument | S08-a (the Greek-origin theory, its plausibility, the 19th-century debate, the verdict of independence) | 340 | 3 |
| B2 | Pahadi ke neeche ek manch | A rock-cut theatre on Ramgarh hill; the Natya-Shastra and the older books it rests on; Chinese and Tibetan versions | S08-b (Natya-Shastra 3rd c AC based on earlier books, Ramgarh hill's natya-shala 2nd c BC, the Chinese translation by an Indian scholar, Sylvain Levi) | 400 | 5 |
| B3 | Ek kavi jise zindagi ne laad kiya | Kalidasa at Ujjayini, one of the nine gems; the Cloud Messenger | S08-f (Kalidasa greatest poet-dramatist, Ujjayini, Chandragupta II Vikramaditya, nine gems, a life of recognition, Meghaduta) | 400 | 5 |
| B4 | Char natak, char zamane | The Clay Cart, the Signet Ring (~400 AC, a political play with no love story), Harsha's three plays, Bhavabhuti ~700 AC — and the playwrights we have lost | S08-c, S08-g, S08-h, S08-i (Sanskrit drama established by 3rd c BC, some say 5th c BC; lost playwrights, Bhasa's 13 plays, Ashvaghosha's fragments from Turfan; Shudraka; Vishaka-datta; Harsha; Bhavabhuti) | 420 | 8 |
| B5 | Jahan bura ant likhna mana tha | Greek drama stands on tragedy — why does man suffer? India's rules forbade a tragic ending; yet the hero always faces the hazard | S08-r, S08-s, S08-t (Greek tragedy's problem of evil; the Sanskrit convention of no tragedy; strict rules; the courageous hero; Chanakya's line; Keith's verdict → T5) | 430 | 5 |
| B6 | Do manch | Two stages: the aristocratic court theatre in a mixed Sanskrit-and-Prakrit text (educated men in Sanskrit, women and ordinary folk in Prakrit), and the popular theatre of myth that always existed | S08-n, S08-o, S08-p, S08-q (mixed language, the court audience vs the crowd, actresses — unlike Greece, stage directions, seating rules, dream-like quality) | 450 | 4 |
| B7 | Zubaan ka faasla | Why the drama declined: because much in India was declining; and because the language it was written in was already nobody's home language | S08-j, S08-k, S08-l, S08-m (decline after Murari in the 9th c; Afghan/Turkish/Moghul patronage of music and poetry, Ibrahim Adil Shah, only image-making restricted; Farsi's competition; vernaculars written only after ~1000 AC; and still plays produced — the 1892 Sanskrit Midsummer Night's Dream, the play counts → T5) | 430 | 4 |
| B8 | Jones ka doosra kaam | 1784: Jones looks at Sanskrit and starts a science; German scholarship takes it further; a new Indian scholarship grows beside the old | S09-c, S09-d, S09-e (Jones's 1784 judgment, comparative philology founded, German universities, the old uncritical Indian scholarship, the new European-inspired school, its advantage and its inherited disadvantage) | 420 | 5 |
| B9 | Zubaan vyakaran se badi cheez hai | A language is more than grammar — it is a people's poetic testament; words change, translation fails, and philology cannot reach it | S09-b, S09-f, S09-g, S09-h, S09-i, S09-j (decline into complexity; language > grammar; the poetic testament; the difficulty of entering its spirit; philology barren; the Authorized Version Bible parallel; the widening gap) | 450 | 4 |
| B10 | Wo zubaan jo kisi ke muh par nahi thi | Even in Kalidasa's day Sanskrit was the language of the educated, not of the people — and that is exactly why it held the modern languages back | S09-k, S09-l, S09-m, S09-n, S09-o (never the people's language, but understood across India; the Dante/Latin comparison; books still written today; its continuing use delaying the modern languages; Thailand's technical terms) | 470 | 4 |
| B11 | Do manch, ek zubaan (**payoff**) | Back to the two stages and the two roads out of the same language | S08/S09 synthesis + spine return | 400 | 2 |
| — | Aaj ke hisaab se | When a language is nobody's mother tongue, what happens to the art made in it? (Tagore-era Hindi-Urdu question) | — | 170 | 0 |
| — | Outro (cliffhanger) | *"Sanskrit kisi ke ghar ki zubaan nahi thi. To logon ki zubaan mein kaun bola? Magadh mein ek aadmi uthega, jo apni pehli baat logon ki boli mein kahega — aur us boli se ek dharm paida hoga, jo is desh ke ghar-ghar tak paunch jayega."* | — | 85 | 0 |
| | | | **Total** | **~5,150** | **~54** |

- *Reuses:* existing 5.3 P1–P9 and P11 mostly verbatim, cold open verbatim. **Move out:** the language-family cluster (~630 words: Indo-Aryan and Dravidian lists, the Hindi-Urdu question, Pashto, Singhalese, Sanskrit's kinship with European and Slavonic languages) → **5.4-B1**.
- *T5 for 5.3:* Sylvain Levi; Ryder; Gilbert Murray's Euripides translations (both quotations stay notes-only, R9); A. Berriedale Keith; Joseph Wood Krutch; the play counts (377 plays by 189 authors in Sylvain Levi's 1890 list; 650 in a later one); F. W. Bain if quoted.

---

### 2.4 Ep 5.4: Vihara se Bihar

- **Premise.** Buddha chose the tongue the people already spoke. His followers built houses for those who had left the world, and the houses grew into colleges, into treasuries, and finally into a province's name. Meanwhile the fields they left behind sank in the world's eyes — and a religion that began as a protest against degradation degraded a great many people without meaning to.
- **Carrying question.** *Jo dharm logon ki zubaan mein bola, wo apne desh ke saath kya kar gaya?*
  **Answer (payoff).** *Usne ghar diye: hazaaron vihara, jinse paathshaala paida hui, daulat paida hui — aur ek poore soobe ka naam paida hua, Bihar. Par jo cheez usne sabse oonchi rakhi — kisi jaan ko na maarna — usi ne kheti ko neeche kar diya, aur un logon ko aur neeche jinka kaam kheti thi. Jo dharm sabse zyada logon ke paas pahuncha, usne sabse pehle apne ghar ka chehra badal diya — aur dheere-dheere wo khud yahan se nikal gaya.*
- **Spine.** **Object: the vihara** — a house built for those who gave up the world, which became a school, then a treasury, then a plan of attack on the maps of its enemies. Its name survives as a province.
- **Cold open (new).** Dawn at a monastery: a bell, a long line of shaven heads, hundreds of doors opening at once. Then the turn: this house has a name, and the province around it is named after this house, a thousand years later, and still is. ~370 words, kalpana declared for the interior, the vihara and the monastic numbers are the source's own. SFX (new plan, cold open only): a low bell once, a door, many bare feet on stone, tanpura on "vihara".
- **Owns.** **S09b** = the language-family tail of S09 (**629 of 2,470**) · S10 Buddhist Philosophy 2,197 · S11 Effect of Buddhism on Hinduism 1,777 = **4,603 source / 5,050 narration**.

| # | Beat | What happens | Delivers (v2 clusters) | Words | U |
|---|---|---|---|---|---|
| — | Cold open + ident + Ab tak | the monastery at dawn; Ab tak = Ep 5.3's "who spoke to the people?" | S11-g/S11-h (small forest settlements → huge monasteries, the flow of people) | 450 | 3 |
| B1 | Jo zubaan ghar-ghar mein bachi | The family Sanskrit left behind: the Indo-Aryan languages, the Dravidian ones, Hindi-Urdu as one tongue with two scripts, Pashto, Singhalese, and the kinship with European languages | S09-p..S09-v (sound and recitation rules; Veda recitation today; Indo-Aryan list; Dravidian list; the real language question = Hindi-Urdu; Pashto; Singhalese; Slavonic and European kin) | 300 | 8 |
| B2 | Buddh ki zubaan | Buddha speaks the Prakrit of his own district so as to reach the people; Pali grows out of it; three hundred years later Sanskrit comes back and Buddhist scholars write philosophy in it | S10-a, S10-b (Prakrit → Pali; the Sanskrit revival; Ashvaghosha's writings and plays, the earliest plays we have) | 380 | 4 |
| B3 | Us daur ka toofan | The age that produced the Buddha was an age of ferment — not in India alone: Lao-tze and Confucius, Zoroaster and Pythagoras are near-contemporaries | S10-c (tremendous mental ferment; the age of Lao-tze, Confucius, Zoroaster, Pythagoras) | 340 | 6 |
| B4 | Phoot kyun padi | Schools grow side by side, then schism; and the Buddha himself had warned against learned controversy over metaphysics | S10-d, S10-e (different schools; Buddhism's own schisms; scholasticism and polemics; Buddha's warning; "whereof one cannot speak…" as one spoken line only, R9) | 400 | 4 |
| B5 | Nagarjuna ka tark | Was he original? — much of the morality can be matched from older books; what was really objected to was not his philosophy but the practice he attacked | S10-f, S10-g (the originality question; the morality matched from Hindu books; the real revolt against conventional practice and priestcraft) | 380 | 5 |
| B6 | Seedi jo khaali mein khatam hoti hai | The Mahayana makes the Buddha a god; the two ways quarrel for centuries; then Nagarjuna builds a ladder of arguments that removes each step as he climbs, until nothing is left — and calls it Shunyata, whose word is also the word for the zero mark | S10-h..S10-v (Mahayana/Hinayana; Buddha as god; bitter controversy; Hinayana countries' contempt; the Pali Canon vs the Mahayana's tolerance; Nagarjuna in Kanishka's reign; the ladder; Shunyata = shunya, relativity; "on account of Shunyata everything becomes possible"; four Buddhist schools; Vasubandhu's Abhidharmakosa; Radhakrishnan's account; airy nothing; reason and the beyond) | 620 | 6 |
| B7 | Vihara se Bihar | What the teaching did to the old religion: a national faith with no missions becomes the world's first missionary faith — Ashoka's embassies and missions, the end of animal sacrifice, non-violence strengthened | S11-a..S11-e (permanent effects on religion; Magadha where Brahminism was weak; a living religion for 1,000+ years; the Aryan faith restricted vs Buddhism universal; Ashoka's missionary work; ritual disappearing, animal sacrifice especially; non-violence) | 480 | 6 |
| B8 | Bhikshu ka ghar | Asceticism, pessimism, and the great flow of people into monasteries — small forest settlements become huge nunneries and monasteries, and one at Balkh holds a thousand monks | S11-f, S11-g, S11-h, S11-i (pessimism towards life, Hinayana and Jaina; forest settlements → monasteries; Central Asia's monasteries; Nava-vihara at Balkh with 1,000 monks; why more otherworldliness in India than China/Japan/Burma) | 420 | 5 |
| B9 | Satyakama ka jawab | A boy's mother is not married to any of the four orders; he tells the teacher the truth; the teacher's answer is the whole point | S11-j, S11-k, S11-l (caste's curious effect, the opposite of the teaching's outlook; Satyakama and his mother Jabala; "no one but a true Brahmin would thus speak out"; the Brahmins the only rigid caste then; Kshatriya doors open) | 450 | 4 |
| B10 | Hal chalane wala neeche | Non-violence made ploughing a lowly trade; the Indo-Aryans' proudest work went down the scale; so a teaching that began against degrading people degraded a great many | S11-m, S11-n (tilling the soil as lowly occupation; the occupation that had been the pride of the Indo-Aryans; Buddhism's revolt against degradation leading unconsciously to the degradation of vast numbers) | 400 | 2 |
| B11 | Vihara se Bihar (**payoff**) | Back to the bell and the shaven heads: the house the teaching built, and the province still named after it — and the door it opened that has not closed yet | S10/S11 synthesis; the vihara spine returns | 350 | 3 |
| — | Aaj ke hisaab se | A protest movement that becomes an institution; Bihar's name | — | 150 | 0 |
| — | Outro (cliffhanger → 5.5) | *"Aath-nau saal pehle, Paris mein, ek French lekhak ne Nehru se namaskar se pehle ek sawal poochha: is bade dharm ko yahan se gayab karne ke liye koi jang nahi hui. To kis cheez ne ye kaam kiya? Jawab agle episode mein — aur jawab ki taraf jaane wala raasta chhe darwazon se hokar jaata hai."* | — | 90 | 0 |
| | | | **Total** | **~5,050** | **~44** |

- *Reuses:* existing 5.4's **P1–P8** stay (Nagarjuna's ladder = existing P5 was one beat; here the whole Shunyata block is B6, which absorbs existing P4 and P5 — keep their prose). **Moves out:** the Malraux cold open and existing P9–P11 (Bina yuddh ki vidaai / Do gawah / Malraux ke sawal ka jawab) → **5.5**. **New:** cold open (vihara), B1 (from 5.3), and the split of the old P1–P8 into eleven delivery beats as above.
- *T5 for 5.4:* Stcherbatsky; Vasubandhu; Radhakrishnan; Garbe; the four schools' names; the Dravidian/Indo-Aryan list tails beyond three languages.

---

### 2.5 Ep 5.5: Bina jung ki vidaai

- **Premise.** In a Paris room, before hello, a Frenchman asks how a great religion was pushed out of its homeland without a war. The answer is not a weapon — it is a way of thinking in which two opposite ideas are allowed to live in the same house. Proof: six doors, and a prisoner doing his yoga at dawn in Ahmadnagar fort.
- **Carrying question.** *Bharat ne Buddh dharm ko bina yuddh ke kaise ghol liya?*
  **Answer (payoff, from existing 5.4).** *Yuddh ki zaroorat hi nahi padi, kyunki seema thi hi nahi. Buddh dharm isi ghar ki soch se bana tha, isliye wo wapas usi soch mein ghul gaya — Buddha ek avatar ban gaya, uska darshan Vedant mein mil gaya, aur uska sangh Shankara ke math ban gaya. Is desh ki soch ek virodh ko maar kar doosra nahi jeetti; wo donon ko ek hi ghar mein rakhti hai. Wahi ghar chhe darwazon ka hai.*
- **Spine.** **Mystery:** Malraux's question, asked in the cold open, answered in B10/B11. Recurring image: the **six doors** (each darshana a doorway; five of them open here, the sixth is left standing at the end).
- **Cold open (keep — move existing 5.4's cold open here).** Paris, "aath-nau saal pehle", rain on a window; the question before the greeting; the honest admission that the straight answer is missing. ~420 words. SFX: rain, a window, a distant engine, then hard silence.
- **Owns.** S12 How did Hinduism Absorb Buddhism in India? 871 · S13 The Indian Philosophical Approach 1,473 · **S14a** = S14 up to and including Yoga and Vivekananda (**2,853 of 4,539**) = **5,197 source / 5,100 narration**.

| # | Beat | What happens | Delivers (v2 clusters) | Words | U |
|---|---|---|---|---|---|
| — | Cold open + ident + Ab tak | Malraux in Paris; Ab tak = Ep 5.4's vihara and Buddha's language | S12-a (the Paris question) | 470 | 3 |
| B1 | Ek sawal, do ghar | Why the question was not academic for Malraux; why few in Europe would ask it; and why it was Nehru's own question | S12-b, S12-c (the question typical of a French intellectual; few in Europe would trouble; it was a question after Nehru's own heart) | 330 | 2 |
| B2 | Do gawah | The first witness: there was no massacre — only local quarrels between a ruler and a wealthy Sangha; the two faiths argued and, because of the arguing, came closer, chiefly through the Mahayana | S12-d, S12-e, S12-f (no widespread or violent extermination; local conflicts with the Sangha; Brahminism and Buddhism reacting and approaching; the Mahayana approach; "sickly imaginings and forgeries of the brain") | 420 | 4 |
| B3 | Brahminism ka punarjanm | The second witness: Buddhism had started as reform and it tapped new popular strength — and then the Gupta renaissance restored Brahminism, and in the 8th century a philosopher built orders of monks on the abandoned design of the Buddhist sangha | S12-g, S12-h, S12-i, S12-j + S13-a (Buddhism as revival releasing new talent; Ashoka's patronage, dominant religion, spread abroad; the Gupta renaissance; Shankaracharya's maths — an adoption of the sangha model; degraded Buddhism left in East Bengal and Sind; Buddhism vanishing as a widespread religion) | 480 | 6 |
| B4 | Darshan sabke paas hota hai | One thought leads to another; every mind is a bundle of contradictions; and in the old, smaller world a harmony of personality was easier | S13-b, S13-c, S13-d, S13-e (thoughts overlap, old and new side by side, irreconcilable; the difficulty of reconciling; material vs metaphysical problems; more unity in the old personality at a lower level; the personality grown beyond the individual; the little world) | 420 | 2 |
| B5 | Ek hi mann, kai soch | Why this old structure and its philosophy have lasted here more than anywhere else — and what it costs and gives | S13-f, S13-g, S13-h, S13-i (India's old social organisation persisting; it must have virtue; Havell: religion as working hypothesis, not dogma → T5; metaphysics' permanence; Buddhist philosophy's part and Islam's impress) | 400 | 4 |
| B6 | Chhe darwaze | The house has six doors. They begin before the Buddha, they criticise and borrow from each other, and they all begin from one presumption: the universe is orderly and runs on law | S14-a, S14-b, S14-k (pre-Buddhist beginnings; Brahminical and Buddhist systems side by side; the six names — Nyaya, Vaisheshika, Samkhya, Yoga, Mimamsa, Vedanta; the common presumption of order and rhythm) | 430 | 7 |
| B7 | Pehla darwaza — Nyaya | Logic as a science of right reasoning; close to Aristotle's syllogisms and not the same; critical rather than faithful — the nearest thing India had to a method of proof | S14-c, S14-d (Nyaya analytic and logical; the comparison with Aristotle; the principles of reasoning; its critical method vs modern objective science) | 400 | 4 |
| B8 | Doosra darwaza — alag-alag, aur anu | A system that starts from separateness and ends with atoms, governed by a moral law | S14-e (Vaisheshika; the separateness of selves and objects; the atomic theory; dharma as the moral law of the universe) | 330 | 3 |
| B9 | Teesra darwaza — Samkhya | The oldest shaped system: two first causes, an ever-changing nature and a spirit that does not change; and the number of spirits is infinite | S14-f, S14-g, S14-h (Kapila, c. 7th century BC; Garbe's verdict → T5; the system co-ordinated after Buddhism's rise; purely metaphysical; dualism of prakriti and purusha; infinite purushas) | 420 | 5 |
| B10 | Chautha darwaza — Patanjali ka Yoga, aur qaidi ki asana | Yoga as a method for body and mind; Europe's misunderstanding of it as navel-gazing and tricks; the real discipline of the body; then, in Ahmadnagar fort in 1944, a prisoner doing a few asanas every day he can | S14-i..S14-u (Patanjali's method; the West's "quaint practices" and exploiters; the later stages and ecstasy; body first — fit, supple, strong; asanas suited to any age; Nehru's own practice; eating and drinking, ethical preparation, ahimsa; control of the senses; Vivekananda's stress on reason, on experience as the only source of knowledge, on the freedom of the mind; Yoga as an experimental system for modern psychology) | 560 | 8 |
| B11 | Paanchwa darwaza — Mimamsa (**payoff**) | The ritual door, which shaped popular Hinduism and Hindu law; and then the answer to Paris | S14-j (Mimamsa: ritualistic, tending to polytheism, its rules laying down dharma, its deep influence on popular Hinduism and Hindu law) + S12/S13 payoff: *seema thi hi nahi* — the mechanism of absorption, in Asha's words | 560 | 5 |
| — | Aaj ke hisaab se | Living with people who think the opposite of you; why argument is not war | — | 160 | 0 |
| — | Outro (cliffhanger → 5.6) | *"Paanch darwaze khul gaye. Chhetta bacha hai — sabse bada, sabse chupa hua. Jis darwaze ne baaki sabko nigal liya. Aur us darwaze ke peeche ek aadmi khada hai, jo is desh ke chaar kone tak paidal jaayega — sirf isliye ki ye ek desh lage."* | — | 90 | 0 |
| | | | **Total** | **~5,100** | **~54** |

- *Reuses:* existing 5.4's cold open + P9–P11 (Malraux) as the frame; existing 5.5's P2, P3 (approach) as B4/B5; existing 5.5's P4 (Nyaya) as B7; P5 (Vaisheshika) as B8; P6 + P7 (Yoga + asanas) as B10; P8 (Mimamsa) folded into B11. **The existing 5.5's P1 (Chaar kone chaar ghar) and P9–P10 (Vedanta, four maths) move to 5.6.**
- *T5 for 5.5:* Richard Garbe; Havell; Vivekananda's quoted lines (gist only, R9); the six systems' sub-terms (pramana, padartha, tanmatra…); the full Greek-syllogism comparison.

---

### 2.6 Ep 5.6: Chaar kone, pahaad ke us paar

- **Premise.** The sixth door is the one that swallowed the others: a reality that is one, a world that is a shadow of it, and a man from the far south who walked to the four corners of India so that the land would feel like one. Then the road turns outward: over the mountains, where monks carried the same thought to China, and Chinese pilgrims walked back to sit in Nalanda.
- **Carrying question.** *Jo soch is desh ke chaar kone tak pahunchi, wo pahaad ke us paar kaise pahunchi — aur wahan se kya laayi?*
  **Answer (payoff).** *Andar wahi soch chaar kone tak paidal gayi; bahar wahi soch pothiyon aur bhikshuon ke saath pahaad paar gayi. Aur wahan se wapas aaya wahi tha jo is desh ke paas kam tha: kitaben — hazaaron pothiyan, chhapai, aur ek nayi duniya ka naqsha. Raasta dono taraf khula tha; isi liye jab tak khula raha, dono taraf kuch naya paida hota raha.*
- **Spine.** **Road/journey**: two roads in one episode — the road *inside* India (Shankara to the four maths, and the pilgrims who walked the same roads for a different reason) and the road *out* (the dust cup, the Gobi, the Himalayas, the sea route back). First image in the cold open, last image in the payoff.
- **Cold open (keep — the old Ep 5 cold open, Hsuan Tsang and the dust cup).** Re-time on the new narration; SFX from `scripts/Ep 5 — SFX plan.md` (B1, S1, S2, S3, B2, S4, B3, M2, S6). ~380 words.
- **Owns.** **S14b** = S14 from Mimamsa's end onward — Vedanta, Shankara, the four maths, the pilgrims (**1,686 of 4,539**) · S15 India and China 3,597 = **5,283 source / 5,100 narration**.

| # | Beat | What happens | Delivers (v2 clusters) | Words | U |
|---|---|---|---|---|---|
| — | Cold open + ident + Ab tak | Hsuan Tsang sets out from China with a cup of dust; Ab tak = Ep 5.5's five doors and Malraux's answer | S15-f (Hsuan Tsang's road: T'ang dynasty, Harshavardhana's court) | 430 | 4 |
| B1 | Chhetta darwaza — Vedanta | The last door: a pure monism; the only ultimate reality is the Atman; the world we see is its reflection, or a shadow on the empirical plane — and "maya" is not "illusion" but something subtler | S14-v, S14-w, S14-x, S14-y (Vedanta from the Upanishads, many shapes, always monistic; Atman as the only reality; how the one appears as the many; Shankara's advaitism built step by step; maya mistranslated as illusion; finite minds forming limited conceptions) | 420 | 6 |
| B2 | Malabar ka pandit | Shankara's bargain: he accepted the caste organisation as the race's collected experience, and still held that anyone of any caste could reach the highest knowledge; his philosophy of world-negation — and his astonishing energy | S14-z, S14-aa (Shankara accepting caste but opening the highest knowledge to all; world negation and withdrawal; yet a man of amazing energy, no escapist; born in Malabar) | 400 | 5 |
| B3 | Chaar kone, chaar math | The four maths: Sringeri in the south, Puri in the east, Dwaraka in the west, Badrinath in the Himalayas. Why those journeys mattered: travel was slow and hard, and to go and meet people from every part of the country was to build the country in the mind | S14-ab, S14-ac, S14-ad, S14-ae (the four maths and their places; the significance of the long journeys; the conception of a common land and common culture; the roads not used only by the upper castes — pilgrims; the choice of sacred places — the icy cave of Amarnath, the temple of the Virgin Goddess, lovely natural settings) | 520 | 8 |
| B4 | Pahaad ke us paar | Back to the road: it was Buddhism that brought India and China near each other; Buddhist culture spread all over Central Asia and parts of Indonesia, with monasteries and study centres dotted across the route, so travellers found shelter all the way | S15-a, S15-b (contacts through Buddhism; possible sea-borne trade before Ashoka; silk; the spread of Buddhist culture across Central Asia and Indonesia; the welcome for travellers; routes by land and sea; Chinese scholars breaking their journey in Indonesia to learn Sanskrit) | 400 | 5 |
| B5 | Pehla vidvaan | 67 AD: an Indian scholar reaches China in the reign of the Emperor Ming Ti and settles at Lo Yang; the manuscripts and the original works written in Chinese | S15-c, S15-d (Kashyapa Matanga, 67 AD, Ming Ti, Lo Yang; Sanskrit manuscripts carried and translated; original books written in Chinese; Kumarajiva's 401 AD and his 47 works, Nagarjuna's life; Jinagupta's 37 translations; the three thousand monks and ten thousand families figures → T5) | 380 | 9 |
| B6 | Guru ki aakhri salah | The traffic runs both ways: Fa Hien, Sung Yun, then the most famous of them all — across the Gobi, Samarkand, Balkh, Khotan, Yarkand, over the Himalayas | S15-e, S15-f (the two-way traffic and the named travellers; Hsuan Tsang in the 7th century, the T'ang dynasty, Harshavardhana; the route and the perils; the Buddhist rulers and monasteries of Central Asia; the Turks who were ardent Buddhists) | 420 | 8 |
| B7 | Paanch hisse, ek pyaas | A Chinese traveller's record of India, written from the capital of the greatest Chinese age; and what he carried home | S15-g, S15-h (the Si-Yu-Ki and what it says about India — benign principles, simple executive, no forced labour, light taxes, merchants coming and going; Si-an-fu as a centre of art and learning; the return via Central Asia with manuscripts; the wide sway of Buddhism through Khorasan, Iraq, Mosul; Iran's role in the beauty of life; Turfan's seven colours) | 400 | 7 |
| B8 | I-tsing ki thaali | A later pilgrim, hard on Hsuan Tsang's heels, interested less in philosophy than in the fine points of ritual; what he called this land, and why | S15-k (I-tsing starting in 671 AC, nearly two years to the port of Tamralipti, studying at Nalanda, several hundred Sanskrit texts carried back, the ritual and ceremonial detail, the monastic rules, Aryadesha / "the noble region", Hsin-tu, deva-putra, and his judgment about Chinese superiority) | 400 | 8 |
| B9 | Nalanda ke khandhar | Two courts exchange embassies and letters; and a university whose diggings still astonish | S15-i, S15-j (Harsha of Kanauj and the T'ang emperor exchanging embassies and letters; the lost load of sacred texts at the Indus and the request for copies; Nalanda university described by Hsuan Tsang and by others, and Nehru's own visit to the excavated ruins) | 380 | 4 |
| B10 | Jo pahaad paar nahi gayi | What did *not* cross: among the oldest printed books found in China are 8th-century **Sanskrit** books, printed from wooden blocks — and yet there is no evidence of printing in India during all those centuries of exchange; and what did cross — thought, arts, sciences, and Confucius and Lao-tze's names into Indian memory; plus the 16th-century novel in which a Chinese writer makes a pilgrimage out of Hsuan Tsang's journey | S15-l, S15-m, S15-n (8th-c Sanskrit printed books in China from wooden blocks; the Imperial Printing Commission in the 10th c and the Sung era; no printing in India then, and the surprise of it; block printing to Tibet; Chinese printing into Europe under the Yuan, 1260–1368, and Germany in the 15th c; the slow European acceptance; what each country learned from the other; Confucius and Lao-tze known in India; the Chinese proverb; *Monkey* by Wu Ch'en-en, translated by Arthur Waley, and its dedication) | 430 | 6 |
| B11 | Chaar kone, pahaad ke us paar (**payoff**) | The wheel turns: cut off for centuries, then brought together again by a trading company — with opium and a war on the Chinese side; today's pilgrims fly over the mountains | S15-o, S15-p (the British East India Company bringing them back together; the opium and the war; Hu Shih and "the Indianization of China"; the new pilgrims crossing or flying over the mountains, bringing messages of goodwill) | 420 | 5 |
| — | Aaj ke hisaab se | A road in both directions is what keeps a civilisation awake; who closes a road, and why | — | 170 | 0 |
| — | Outro (cliffhanger → 5.7) | *"Pahaad wale raaste par bhikshu chalte the. Ek doosra raasta bhi tha — samundar wala, jahaaz wala, vyapaari wala. Us par is desh ne apne naam se zyada apni mitti bheji: mandir, patthar, aur zubaan. Wo raasta sone ki ek dharti tak jaata tha."* | — | 90 | 0 |
| | | | **Total** | **~5,100** | **~66** |

- *Reuses:* existing 5.6's cold open and its China beats P1–P6 (Pahaad ke us paar · Guru ki aakhri salah · Paanch hisse, ek pyaas · Wapas lauta bojh · I-tsing ki thaali · Jo cheez pahaad paar nahi gayi) — expand each to the cluster list above. **Moves in:** existing 5.5's P1 (Chaar kone chaar ghar) and P9–P10 (Vedanta, the four maths) as B1–B3. **Moves out:** existing 5.6's P7, P8, P10, P11 (the sea, the Land of Gold, the two empires, 1511) → **5.7**; its P9 (Mitti, dhaatu, dawa = trade, chemistry, metals) → **5.8-B6/B7**.
- *T5 for 5.6:* Kumarajiva, Jinagupta, the monk-count figures; the five branches of study at Nalanda; the full printing history; Aryadesha/Hsin-tu variant names; Sung Yun, Fa Hien's dates; Arthur Waley; Hu Shih; Bagchi.

---

### 2.7 Ep 5.7: Sone ki dharti

- **Premise.** From the first century onward, wave after wave of Indians sailed east — to Ceylon, Burma, Malaya, Java, Sumatra, Borneo, Siam, Cambodia, Indo-China — looking for trade and finding kingdoms. They left their gods, their alphabet, their law and their art; Angkor and Borobudur stand on that crossing of two peoples. It lasted thirteen hundred years, and it ended in one year: 1511, when Europe's ships arrived in the Strait of Malacca.
- **Carrying question.** *Bharat samundar ke us paar kya le gaya — aur kitne saal tak le jaata raha?*
  **Answer (payoff).** *Apne naam, apni zubaan, apna kanoon, apne devta aur apna patthar. Aur ye kaam sadiyon tak chalta raha — terah sau saal, jab tak samundar wala raasta is desh ke haath mein tha. 1511 mein wahi raasta kisi aur ka ho gaya, aur usi saal se bahar ka kaam ruk gaya. Jo bahar gayi cheez apni jagah khadi hai — Angkor mein, Borobudur mein — par uski jarh wapas is desh mein dikhne lagi, kyunki yahan mitti sookh rahi thi.*
- **Spine.** **Place: the Land of Gold** (Svarnabhumi / Svarnadvipa) — the name the sailors gave it; the recurring image is the repeated carved face of the Bayon at Angkor, which opens and closes the episode.
- **Cold open (keep — reuse existing 5.7's cold open, the Bayon smile).** Retitle the spine to the Land of Gold, keep the scene; the "bindu" line at the end is cut (the zero now belongs to 5.8/5.9) and replaced by the sea line. ~380 words. SFX: dry wind between stone walls, distant leaves, no music.
- **Owns.** S16 Indian Colonies and Culture in South-East Asia 3,195 · S17 The Influence of Indian Art Abroad 1,085 = **4,280 source / 5,050 narration**.

| # | Beat | What happens | Delivers (v2 clusters) | Words | U |
|---|---|---|---|---|---|
| — | Cold open + ident + Ab tak | the Bayon's repeated smile; Ab tak = Ep 5.6's two roads | S17-e/S17-f (Angkor's ruins, the great gate's vast sculptured head, the Khmer genius) | 430 | 3 |
| B1 | Sadiyon tak, samundar paar | To understand India you have to travel far in time and space; the countries where India spread out; and the scholars who uncovered it | S16-a, S16-b, S16-c, S16-d, S16-e (glimpses of what India was; the countries of Asia; Sir Charles Eliot's testimony → T5; the recent discoveries that changed the picture; Sailendra and Quaritch Wales → T5; Greater India; the gaps and contradictions; the sources: inscriptions, copper plates, Javanese and Balinese literature, Greek and Latin writers, ruins) | 400 | 7 |
| B2 | Sone ki dharti | From the first century AD, wave after wave of Indian colonists east and south-east; the sailors' name for the lands they sailed to | S16-f, S16-l, S16-m (Ceylon, Burma, Malaya, Java, Sumatra, Borneo, Siam, Cambodia, Indo-China, Formosa, the Philippines; Svarnabhumi and Svarnadvipa, the Land of Gold; the Malva tribe and the Malay race; Kalinga, Pallav, Orissa; thirteen hundred years in five phases) | 420 | 12 |
| B3 | Vyapaar ki pyaas | Why did anyone go? Because trade, not conquest, was the supreme passion of those centuries; then missionaries followed the merchants | S16-g, S16-h, S16-p (Majumdar's judgment → T5; Yavadvipa; trade rising in the 3rd–2nd centuries BC; Ashoka's missionaries; the old Sanskrit stories of voyages; regular maritime intercourse by the 1st century AD; the Malay Peninsula on the direct China–India route) | 400 | 6 |
| B4 | Do mastool wale jahaaz | Ships built for the open sea; coins that show two masts; the Andhra coast, Ajanta's ships; naval powers fighting over sea routes | S16-i, S16-j, S16-o (shipbuilding a flourishing industry; ports; Andhra coins of the 2nd–3rd centuries showing two masts; Ajanta; the states as naval powers interested in trade and sea-route control; their conflicts; Indian art's religious basis going out with the religion; wars that were political and economic) | 400 | 6 |
| B5 | Pandrah sau log | A Tamil inscription of 1088 AD names a corporation of traders, "brave men, born to wander over many countries" | S16-k (the Corporation of the Fifteen Hundred, 1088 AC) | 320 | 4 |
| B6 | Do samrajya ke beech | These colonies sat between the two great civilisations — India and China; some touched China's frontier; the biggest of them, Sri Vijaya, dominated sea and land by the 8th century, and older states had already grown in Malaya, Cambodia and Java | S16-n, S16-q, S16-r (between two civilisations, on the trade route; the Sailendra Empire / Sri Vijaya dominant by the 8th century; what was believed about it before; the earlier states in Malaya, Cambodia and Java; R. J. Wilkinson's finds in the northern Malay Peninsula) | 420 | 10 |
| B7 | Teen sau saal, do samrajya | Majapahit: a centralised empire with a commerce department and a colonial department — and a cruel war with Sri Vijaya that won everything and seeded the next war | S16-s, S16-t (Majapahit's taxation and departments; the war with Srivijaya; its complete victory and the fresh conflict it sowed) | 380 | 6 |
| B8 | 1511 | The last of these states was still standing at the end of the 15th century. Then, within a few years, the Portuguese under Albuquerque took Malacca. Europe had reached the Far East on its new sea power — and thirteen hundred years of an Indian sea ended | S16-u (Albuquerque and Malacca, 1511) | 340 | 4 |
| B9 | Naam pehle | The first evidence of India abroad is not art but names: every ruler of these lands took an Indian name; and there were great centres of Sanskrit learning from Champa to Majapahit | S17-a, S17-b, S17-c (records of empires interesting for the history of art; Indian civilisation taking root across south-east Asia; Sanskrit learning at Champa, Angkor, Sri Vijaya, Majapahit; writing going to the Philippines; Cambodia's alphabet from South India, Sanskrit words, the Laws of Manu in force) | 420 | 8 |
| B10 | Patthar ki zubaan | Above all else it is in the art and architecture that the Indian influence shows — fused with the genius of each place until it becomes something neither land could have made alone | S17-g, S17-i, S17-j (the original impulse modified and fused; Quaritch Wales: when India's guiding hand was removed, that genius was released → T5; the excavations by French and Dutch scholars; buried cities; the Siamese student's letter to Tagore's Santiniketan; Hellenism's parallel spread) | 400 | 7 |
| B11 | Wahi muskaan (**payoff**) | Back to Angkor: the smile that repeats, the inspiration that faded at home, and the one line from a French scholar to close | S17-d, S17-h, S17-k (Angkor Vat and the vast area of ruins — artificial lakes, canals, bridges, the great gate; the Khmer genius and Jayavarman; **the original inspiration faded in India itself because the mind and the soil became overworked and undernourished for lack of fresh currents**; Sylvain Levi's line from Persia to the Chinese sea → gist spoken, name to T5) | 430 | 6 |
| — | Aaj ke hisaab se | Ideas cross water more easily than armies; and they can outlive their home | — | 170 | 0 |
| — | Outro (cliffhanger → 5.8) | *"Jo cheez bahar gayi, wo patthar mein khadi hai. Par is desh ne apne haathon se kya banaya? Deewarein jinpar auratein hain, dhaatu jo talwar se zyada mazboot thi, dawa, aur ek chhota sa nishaan — shunya. Agli baar hum ghar mein lautenge."* | — | 90 | 0 |
| | | | **Total** | **~5,050** | **~62** |

- *Reuses:* existing 5.7's P1, P2 (Angkor, and "Jahan mitti upjaau thi" for the Cambodia/alphabet material), plus existing 5.6's P7, P8, P10, P11 (the sea, the Land of Gold, the two empires, 1511). Cold open reused from existing 5.7.
- *T5 for 5.7:* Sir Charles Eliot; Quaritch Wales; R. J. Wilkinson; Majumdar; Leclère; Osbert Sitwell; Sylvain Levi; the colonists' full land list beyond three; the Sailendra/Majapahit dynastic lists.

---

### 2.8 Ep 5.8: Ajanta ki auratein

- **Premise.** A cave full of women painted by men whose Master told them never to look at a woman. That contradiction is this episode's door into what India made with its hands: frescoes, temples cut from living rock, steel the world bought for its wars, dyes and medicines, an astronomy good enough that its calendar is still in use — and a number system whose worth no one here guessed.
- **Carrying question.** *Jis desh ki deewarein, dhaatu aur dawa duniya bhar mein bikte the, usne apna sabse bada tohfa kaise banaya?*
  **Answer (payoff).** *Usne wo cheez banayi jo dekhne mein kuch bhi nahi thi: ek chhota sa nishaan, jise khaali jagah dikhane ke liye likha jaata hai. Us nishaan ne ginti ke darwaze khol diye — aur wahi nishaan aage chalkar sabse pehle is desh se bahar nikal gaya. Yahi is katha ka sabse bada sabak hai: is desh ne jo sabse bada diya, wo patthar mein nahi, khaali jagah mein likha tha.*
- **Spine.** **Object: the painted wall** — and the hands behind it (the dye, the steel, the medicine, the numbers). First image in the cold open (a monk's lamp on a fresco), last image in the payoff (the same lamp on an empty space on the wall).
- **Cold open (new, sourced).** A cave at Ajanta in lamplight; the monk's own rule is read out in three words — keep away from women — and then the lamp turns and the wall is full of women: princesses, singers, dancers, seated and standing. ~370 words. SFX (new, cold open only): a lamp, damp rock, one water-drop, a single low voice, tanpura on "Ajanta".
- **Owns.** S18 Old Indian Art 2,361 · S19 India's Foreign Trade 465 · **S20a** = S20 up to the zero's consequences — the *worth* of the number system (**~1,600 of 2,727**) = **4,426 source / 5,000 narration**.

| # | Beat | What happens | Delivers (v2 clusters) | Words | U |
|---|---|---|---|---|---|
| — | Cold open + ident + Ab tak | the lamp and the women on the wall; Ab tak = Ep 5.7's sea road | S18-l, S19 (as placed by the rebuild) (the monks' rule about women and the women in plenty; Ajanta's frescoes) | 430 | 4 |
| B1 | Aadha itihaas | Some of the finest Indian art is outside India; and in northern India much of the oldest is gone | S18-a, S18-b, S18-c, S18-d (finest expressions abroad; lost northern monuments; art tied to religion and philosophy; beauty with a deeper significance; Nehru's untutored layman's reaction) | 380 | 4 |
| B2 | Yunani aankh se dekha | For a century Europeans judged Indian art by the Greek yardstick and called the rest degenerate; one Englishman's contempt, and Nehru's answer to it | S18-e, S18-f, S18-g (Europeans trained in the Greek tradition; Gandhara as the familiar; Sitwell's opinions and Nehru's response → T5; Binyon and Havell; Havell on the artist identifying with nature) | 430 | 7 |
| B3 | Ajanta ki auratein | The Golden Age caves: Ajanta dug out and painted in the Gupta period, Bagh and Badami with it; a world away and yet very real | S18-l, S18-m, S18-n (Gupta period 4th–6th centuries; Ajanta, Bagh, Badami; the dream-like, very real world; Ellora in the 7th–8th and the Kailasa temple carved from solid rock; Elephanta's Shiva Nataraja and Havell's words; Epstein on the London Nataraja → T5) | 460 | 8 |
| B4 | Ek sir, teen jagah | A head from Borobudur now in Copenhagen; Indian art in Java; and a doubt: who taught whom | S18-o, S18-p, S18-k, S18-h (the Borobudur Bodhisattva head, Glyptotek, Havell; Havell on Indian art in Java; the early naturalism partly from Chinese influence; Chinese influence at various stages; sculpture and architecture India's forte, painting China's and Japan's; Indian music's influence across Asia) | 420 | 7 |
| B5 | Graven images | The Vedas were against images; there were no temples; so how did a land that forbade the carved god fill itself with statues? | S18-j (the religious prejudice against graven images; Vedic opposition; image worship arriving late, only at a comparatively late period in Buddhism) + T4: 5.2-B11's "image worship came from Greece" | 340 | 3 |
| B6 | Bazaar se duniya tak | What India sold in the first millennium: merchants who controlled foreign markets, dominance in the eastern seas, and pepper and spices reaching the Mediterranean | S19-a, S19-b (trade widespread through the first millennium; pepper and spices via India or from India; the give-and-take of materials found and developed locally; India rich in what others lacked) | 400 | 4 |
| B7 | Dhaatu aur dawa | Chemistry more advanced than elsewhere in the early centuries; steel tempering known early, Indian steel and iron valued abroad for war; metals and metallic compounds for medicine; distillation | S19-c, S19-d (chemistry; *History of Hindu Chemistry* → T5; steel tempering; iron and steel valued for warlike purposes; metals and medicinal preparations; distillation) | 400 | 6 |
| B8 | Aakash ki ginti | Astronomy, the oldest of the sciences, was a university subject, mixed up with astrology; a solar calendar was worked out that is still in popular use | S19-e, S19-f (astronomy in the curriculum and astrology; the accurate calendar still in use; mechanical appliances; shipbuilding; "machines" mostly for war) | 400 | 5 |
| B9 | Ghulaam nahi the | One hidden advantage over the great ancient civilisations: no slave-labour economy — and Nehru's uncomfortable judgment comparing caste with slavery | S19-g (the absence of slave labour as an advantage over Greece and others; caste "infinitely better than slavery" — deliver as *Nehru's* judgment, flagged in Sources as his, and answer it in "Aaj ke hisaab se") | 320 | 3 |
| B10 | La Place ka salaam | One would expect this people to excel at mathematics; Europe got its arithmetic and algebra from the Arabs, and the Arabs from India | S20-a, S20-b, S20-c (the "Arabic numerals" provenance; La Place's tribute → T5; the origins of geometry, arithmetic and algebra going back to remote periods; geometrical algebra for Vedic altars; the most ancient books' mentions) | 420 | 5 |
| B11 | Khaali jagah ka nishaan | Why here and not in Greece: not one man's lightning but a social demand; a Greek contempt for applied science; and a warning about cultures that teach only the gifted | S20-d, S20-e, S20-f, S20-g, S20-h, S20-i (Dantzig's puzzle and Greece's contempt for applied science → T5; Hogben's answer: every culture contains its own doom unless it educates the mass **— the sentence that 5.9 will collect**; the invention as the product of the social milieu, not an erratic genius) | 460 | 6 |
| — | Aaj ke hisaab se | Nehru's caste/slavery comparison, answered; who gets educated, and what that decides | — | 170 | 0 |
| — | Outro (cliffhanger → 5.9) | *"Ek nishaan bacha tha: shunya. Usne ginti ke darwaze khol diye — bhinn, rin, anant. Aur phir wo nishaan ghar se nikal gaya. Bagdad ke ek khalifa ne kitaben mangwayi, aur ek naya naam paida hua: Hindsa."* | — | 80 | 0 |
| | | | **Total** | **~5,000** | **~48** |

- *Reuses:* existing 5.7's P3 (Aadha itihaas) and P4 (Ajanta ki auratein) as B1–B3; existing 5.6's P9 (Mitti, dhaatu, dawa) as B7. **New:** cold open, B6, B9, B10, B11.
- *T5 for 5.8:* Osbert Sitwell; Lawrence Binyon; E. B. Havell; Epstein; P. C. Ray's *History of Hindu Chemistry*; Dantzig; Hogben; La Place; Halsted; the metals and gem lists; the port and export lists from S19's neighbours.

---

### 2.9 Ep 5.9: Shunya, aur phir dopahar

- **Premise.** The zero leaves home: Indian books reach Baghdad under a Khalif, the numerals travel to Europe as "Hindsa", a Sicilian coin of 1134 carries them and Britain takes until 1490. Then, in a Madras office, a clerk writes numbers into a diary with no one to read them. And behind him the whole picture: a civilisation that is still rich, still writing, still building — and visibly tiring, from the north first.
- **Carrying question.** *Jo desh shunya khoj sakta tha, wo thak kaise gaya?*
  **Answer (payoff).** *Kyunki jab bahar se aane wali hawa band ho gayi, to roshni bhi andar hi dheemi pad gayi. Ye thakaan kisi ek jang se nahi aayi; ye dheemi-dheemi aayi, aur uttar se dakshin tak pahunchi. Aur us vyavastha ne, jisne is samaaj ko sadiyon tak baandhe rakha, nayi pratibha ko upar aane ka raasta band kar diya. Har sabhyata apne andar apna ant liye chalti hai — agar wo sirf chuni hui pratibha ko padhaye, aur jan-samuh ko nahi.*
- **Spine.** **Object → verdict:** the zero's journey out (the object) and then the afternoon of a civilisation (the verdict); the cold open's image is the clerk and his diary, and the payoff returns to the same page with the Hindsa line — the number that went round the world coming back to a room in Madras where nobody is reading it.
- **Cold open (new; uses the existing 5.7 P8 image).** Madras, an office, a clerk with a register; he copies numbers all day, and at night writes other numbers, of his own, into a notebook — and posts them to England. ~370 words, kalpana declared for the room, the facts (clerk, Madras, no education, short life) are the source's. SFX: a ceiling fan, an adding-machine, a fountain pen, a letter dropping into a box, tanpura on the letter's fall.
- **Owns.** **S20b** = the zero's consequences and the mathematicians' succession, Baghdad, Europe, Ramanujan (**~1,100 of 2,727**) · S21 Growth and Decay 3,105 = **4,205 source / 5,050 narration**.

| # | Beat | What happens | Delivers (v2 clusters) | Words | U |
|---|---|---|---|---|---|
| — | Cold open + ident + Ab tak | the clerk in Madras; Ab tak = Ep 5.8's empty mark and the Baghdad line | S20-o (Ramanujan) | 410 | 3 |
| B1 | Shunya | What the zero and the place-value system did when they arrived: fractions, multiplication and division of fractions, the rule of three, division by zero running to infinity, negative quantities | S20-j (zero and decimal place-value unbarring the gates; fractions and their rules; the rule of three; a/0; negative quantities) | 380 | 4 |
| B2 | Naam ki kataar | Five centuries of mathematicians — and then it stops | S20-k, S20-l (books from the 5th to the 12th century; the earlier Baudhayana, Apastamba, Katyayana; Brahmagupta and Bhaskara; Lilavati and the question of the daughter, its simple style still used in schools; Narayana 1150, Ganesha 1545 as repetitions; almost no original mathematics after the 12th century) | 420 | 9 |
| B3 | Hindsa | The Khalif Al-Mansur's reign, Indian scholars reaching Baghdad with books on mathematics and astronomy — and the new numerals getting a name | S20-m (Al-Mansur 753–774; the Indian scholars and their books; the name *Hindsa*; the earlier penetration of place-value into western Asia) | 400 | 5 |
| B4 | Europe ke darwaze | From Baghdad to Europe through the Moorish universities of Spain; the old objection to infidel symbols; a Sicilian coin of 1134; Britain in 1490 | S20-n (the Arab world → Europe; the Moorish universities; opposition to the new numbers; the first known use on a Sicilian coin of 1134; Britain 1490) | 400 | 5 |
| B5 | Madras ka ek clerk | Back to the notebook: a poor Brahmin family in the south, no chance of a proper education, a clerkship — and a mind that Europe had no answer for; his short life as the symbol of India's condition | S20-o (Ramanujan's family and clerkship; the mathematicians who finally read him; his brief life and death as symbolic of conditions in India; how few of our millions get any education) | 400 | 5 |
| B6 | Ek hazaar saal, kai utaar-chadhaav | The first millennium was not one long decline: ups and downs, invasions, internal troubles — and a national life bubbling with energy, with the Gupta age as its classical moment | S21-a, S21-b (vigorous national life in the first thousand years; ups and downs; the Gupta Age 4th–6th centuries as the Golden Age, patron of a widespread intellectual and artistic activity) | 400 | 4 |
| B7 | Safed Hoon, phir bhi | Even before that Golden Age closed, the White Huns came in successive hordes, were pushed back, and came again; and long-drawn conflict did more damage than any one defeat | S21-c, S21-d (weakness visible before the Golden Age closed; the White Huns' repeated hordes; the long conflict weakening India politically and militarily; the settlement of large numbers of Huns producing an inner change; the 7th-century revival under Harsha; Ujjayini a centre of art again) | 420 | 6 |
| B8 | Dopahar shuru hoti hai | An inner weakness with no date to it, a slow and creeping one; the north splitting into small states but life still rich; Benares and the universities | S21-e, S21-f, S21-g (the inner weakness seizing India, slow, undated; the north split but life still rich; Benares; the universities — Vikramshila near Bhagalpur, Vallabhi in Kathiawar, Ujjayini, Amravati in the south) | 440 | 8 |
| B9 | Kitaben, aur aakhri naam | The afternoon of a civilisation: the glow of morning long gone; literature's last great figure; and one last emigration by sea | S21-h, S21-i, S21-j (the millennium's end as the afternoon of a civilisation; the south still vital; Bhavabhuti in the 8th century as the last great literary figure; style growing involved, no freshness; Bhaskara II in the 12th; the last major colonial emigration in the 9th century; the Cholas a sea power till the 11th) | 420 | 7 |
| B10 | Jarh kahan thi | The honest difficulty: was it the loss of political freedom that caused cultural decay, or was decay the reason freedom was lost? Every civilisation has its declines; India had survived them before | S21-k, S21-l, S21-m, S21-n, S21-o (India drying up, the slow process beginning in the north and reaching the south; the loss of political freedom → cultural decay; but why should freedom be lost unless decay preceded it; earlier periods of decay and India's rejuvenation; the collapse of Rome and Europe's classical civilisation as the comparison; no dramatic collapse in India, amazing staying power, but progressive decline) | 500 | 5 |
| B11 | Dopahar (**payoff**) | The one answer Nehru will stand on, and the handoff: the spirit of exclusiveness sapping the creative faculty, life cut into set frames, a structure that gave stability and blocked expansion — and a Baghdad road that a chapter later brings back a new world | S21-p, S21-q, S21-r (the spirit of exclusiveness; life cut up into set frames where each man's job was fixed; the social structure giving stability but blocking expansion and a larger cohesion; decline all along the line — intellectual, philosophical, political, in warfare, in contact with the outside world, and a growth of local sentiment) + the set question answered + Hindsa handoff to 6.1 | 520 | 5 |
| — | Aaj ke hisaab se | Who gets to be India's Ramanujan now; "chuni hui pratibha" | — | 180 | 0 |
| — | Outro (cliffhanger → 6.1) | *"Jab ye kitaabein Bagdad pahunchi, to wahan unhe ek naya naam mila: Hindsa. Usi naam se ye ginti Europe tak gayi. Aur usi raaste par, kuch sau saal baad, is desh ki taraf ek nayi shaam utarne wali thi — ek nayi duniya, nayi taaqatein, aur naye sawal."* | — | 90 | 0 |
| | | | **Total** | **~5,050** | **~61** |

- *Reuses:* existing 5.7's P5 (Shunya), P6 (Ginti ka jangla), P7 (Hindsa), P9–P11 (the decay verdict) — note its P11 ran 674 words, which is where the split signalled itself; P8 (Madras ka ek clerk) becomes this episode's cold open.
- *Split point inside S20 (if the draft runs long):* the seam is after B2 — the mathematicians' succession can open 5.8's tail... no, it cannot move backwards; instead move **B4 (Europe's doors)** material into the "Kitaab mein aur" block if needed. The maths is one arc here on purpose.
- *T5 for 5.9:* Aryabhata, Varahamihira, Brahmagupta, Bhaskara, Lilavati, Narayana, Ganesha, Al-Mansur, Moorish universities, Vikramshila, Vallabhi, Amravati, Bhavabhuti's works.

---

## 3. Coverage table (§2.6 format, R14) — every v2 sub-section and fact cluster → episode → beat

Format as §2.6 of the method. **Flag column:** `—` clean · `GAP` missing in source · `ART` rebuild artifact / mismatched heading · `T5-only` cluster that may be spoken nowhere. Word counts are the sub-section's own (approximate, see §0's note).

| ID | Sub-section | Words | Fact cluster | Ep–Beat | Tier | Flag |
|---|---|---|---|---|---|---|
| S01 | Through the Ages | 5 | heading only; the rebuild left the fragment "Na" | 5.1 Ab tak | — | GAP (heading only) |
| S02 | Nationalism & Imperialism under the Guptas | 1,591 | Sunga after the Mauryas; smaller area; southern states rising; Bactrians/Indo-Greeks | 5.1-B1 | T1 | — |
| S02 | | | Heliodorus pillar, Besnagar near Sanchi, 1st c BC, Sanskrit inscription, the three precepts | 5.1-CO + B11 | T1 | — (GAP resolved in v2) |
| S02 | | | Shakas/Scythians (Seistan = Shakasthan), Yueh Chih, pushed into north India, conversion | 5.1-B2 | T2 | — |
| S02 | | | Kushans, Kanishka, Buddhist legend, patronage of Indian culture, nationalist undercurrent | 5.1-B2 | T1 | — |
| S02 | | | Mahayana/Hinayana schism, debates | 5.1-B3 | T2 | — |
| S02 | | | Gupta age from 320 AC, great rulers, anti-foreign feeling, the shell, tolerance inside / aggression outside | 5.1-B4 | T1/T2 | — |
| S02 | | | ~150 years of the Guptas + ~150 of successors; White Huns, Mihiragula, Baladitya, Yashovarman; brief Hun rule, petty chiefs, absorption | 5.1-B5 | T1/T2 | — |
| S02 | | | Harshavardhana of Kanauj, Hsuan Tsang, 648 AC, empire breaks, Ujjayini | 5.1-B6 + T4 to 5.6-CO | T2 | — |
| S03 | South India | 893 | 1,000+ years of southern states; Andhras beat the Shakas; Chalukyas, Rashtrakutas, Pallavas, Cholas; Rajendra; Ceylon, Burma; Sassanid | 5.1-B7 | T1/T2 | — |
| S03 | | | southern products, sea trade, ships to distant lands, Greek colonies, Roman coins | 5.1-B7 | T1 | — |
| S03 | | | northern invasions → migration south incl. builders and craftsmen; the south becomes a storehouse | 5.1-B7 | T2 | — |
| S02/S03 | *Peaceful Development (no heading in v2)* | ~600 | 1,000 years of dynasties lasting 200–300 years each; less interference with the mass of people; agreements between warring states | 5.1-B8 | T2 | ART (heading lost in rebuild) |
| S02/S03 | | | Indo-Aryan theory of righteous war; Chanakya's machines that kill a hundred at once, explosives, trench warfare; distressful periods, famine; the Pax Britannica delusion | 5.1-B9 | T2 | — |
| S04 | India's Urge to Freedom | 596 | the poet's lines about the patient East; the lines are often quoted | 5.1-B10 | T1 | — (GAP resolved in v2) |
| S04 | | | always resisted, often successfully; the urge to freedom and refusal to submit | 5.1-B10 + B11 | T2 | — |
| S05 | Progress versus Security | 1,553 | mixture of five races; geography and climate; an idea of life; the absurdity of talking of an impulse; continual change | 5.1-B10 | T1/T2 | — |
| S05 | | | progress vs security; communal conformity with individual belief; flexibility of groups; the passion for synthesis | 5.1-B10 | T2 | — |
| S05 | | | Rajputs/Jats/Kathis as the most typically Indian; every outside element gave and took | 5.1-B10 | T2 | — |
| S06 | India and Iran | 1,888 | oldest and most persistent; relationship before Indo-Aryan civilisation; common root; Zoroastrian/Vedic; Pahlavi/Avesta | 5.2-B1, B2 | T2 | — |
| S06 | | | Persian as Asia's court language; Constantinople→Gobi; Persian in Indian courts till the British; modern Indian languages full of Persian | 5.2-B5 | T2 | — |
| S06 | | | Iran absorbing its own invaders (the Arabs, 7th c) | 5.2-B2 | T2 | — |
| S06 | | | Indus Valley seals resembling Iran/Mesopotamia; Achaemenian contacts; Avesta naming India; Parshavas → Parsi; Cyrus | 5.2-B2, B3 | T2 | — |
| S06 | | | Darius's Sind and west Punjab; "richest and most populous province"; Sind then green, now dry; Herodotus 360 talents of gold dust; Indian troops in the Persian army | 5.2-B3 | T1/T2 | — |
| S06 | | | trade to Babylon before the 7th c BC; Alexander's aftermath; Persepolis and Ashoka's buildings; Graeco-Buddhist art; Kabul–Kandahar–Seistan, "White India" | 5.2-B3, B4 | T2 | — |
| S06 | | | north by land, south by sea; a southern kingdom's embassy to Iran; Turk/Afghan/Moghul conquests; the Timurid Renaissance; new architecture; the Taj Mahal line | 5.2-B4, B5 | T2 | — |
| S06 | | | the last memory = Nadir Shah's invasion; the British barring every route; the Zoroastrian refugees; Iran looking back at its pre-Islamic past; Rapson's naval quote | 5.2-B6 | T2 | Rapson → T5-only |
| S06 | | | the Allahabad legend of the two brothers and the flute | 5.2-CO + B11 | T1 | — |
| S07 | India and Greece | 3,253 | Nehru rejecting Orient/Occident; Greek/Hebrew/Latin scholarship; Plato and Aristotle; industry entrenching the difference | 5.2-B7 | T2 | — |
| S07 | | | every people its own message; Greece "definite and superb"; joy in the present and eyes on the beyond; Greece's short life | 5.2-B8 | T2 | — |
| S07 | | | India nearer to old Greece than Europe is; the secret = tenderness and tolerance, not a secret doctrine | 5.2-B8 | T2 | — |
| S07 | | | geography — no rivers, no forests, the sea; life accepted in both; inner life; curiosity and speculation | 5.2-B8, B9 | T2 | — |
| S07 | | | Hellenism's experimental science; Alexandria; the burst of invention and the arithmetic/algebra advance | 5.2-B9 | T2 | — |
| S07 | | | women: no seclusion in India; Greek women at Indian courts; maids-in-waiting in the plays; imports at Barygaza/Broach | 5.2-B9 | T2 | — |
| S07 | | | homosexuality in Greek literature; one restrained line only | 5.2-B9 | T2 | flagged: keep to one line |
| S07 | | | contacts from the earliest times; Ujjayini observatory; Alberuni in the 11th c; mutual influence; the reaction against crediting Greece with everything | 5.2-B10 | T2 | — |
| S07 | | | image worship came to India from Greece; Vedic religion had no idols or temples | 5.2-B11 (payoff) + T4 in 5.8-B5 | T1/T2 | — |
| S07 | | | the mind's passion for unity; thinkers who deny order | 5.2-B10 | T2 | — |
| S08 | The Old Indian Theatre | 3,556 | the Greek-origin theory, its plausibility, the century-long debate | 5.3-B1 | T1/T2 | — |
| S08 | | | Natya-Shastra 3rd c AC and earlier books; Ramgarh hill's natya-shala 2nd c BC; the Chinese translation by an Indian; Sylvain Levi | 5.3-B2 | T2 | Levi → T5-only |
| S08 | | | Sanskrit drama established by 3rd c BC (some say 5th); lost playwrights; Bhasa's 13 plays; Ashvaghosha's fragments, Turfan, Buddha Charita | 5.3-B4 | T2 | — |
| S08 | | | Jones's Shakuntala 1789; the European commotion; editions and translations; Goethe; the Faust prologue | 5.3-CO | T1 | — |
| S08 | | | Kalidasa the greatest; Ujjayini; Chandragupta II Vikramaditya; the nine gems; Meghaduta | 5.3-B3 | T1/T2 | Ryder → T5-only |
| S08 | | | Shudraka's Clay Cart; Vishaka-datta's Mudra-Rakshasa ~400 AC; Harsha's three plays; Bhavabhuti ~700 AC | 5.3-B4 | T2 | — |
| S08 | | | decline after Murari (9th c); Afghan/Turkish/Moghul patronage of music and poetry; Ibrahim Adil Shah; only image-making restricted | 5.3-B7 | T2 | — |
| S08 | | | decline before the Afghans and Turks reached Delhi; Farsi's competition; vernaculars written after ~1000 AC; plays still produced (1892 Sanskrit Midsummer Night's Dream; the three counts) | 5.3-B7 | T2 | counts → T5-only |
| S08 | | | mixed Sanskrit + Prakrit (educated men / women and ordinary folk); the aristocratic court audience; the popular mythological stage; actresses; stage directions and seating; the dream-like quality | 5.3-B6 | T1 | — |
| S08 | | | Greek tragedy's problem of evil; the Euripides lines; no tragedy permitted in Sanskrit; strict rules; the courageous hero; Chanakya's line; Keith's verdict | 5.3-B5 | T2 | Murray, Keith → T5-only |
| S08 | | | the 1924 New York staging of the Clay Cart and Krutch's notice; "wholly artificial yet profoundly moving" | 5.3-B5, B11 | T2 | Krutch → T5-only |
| S09 | Vitality and Persistence of Sanskrit | 2,470 | Sanskrit rich and precise; Panini's grammar 2,600 years old; decline into complexity; Jones 1784; comparative philology; German scholarship; the old and new Indian scholarship | 5.3-B8 | T2 | — |
| S09 | | | language > grammar (the poetic testament); words change; the difficulty of translation and of entering its spirit; philology barren; the Authorized Version parallel; the widening gap | 5.3-B9 | T1/T2 | — |
| S09 | | | never the people's language, even in Kalidasa's day, but the language of the educated across India; the Dante/Latin comparison; books still written; the delay it caused to the modern languages; Thailand's technical terms | 5.3-B10 | T2 | — |
| S09 | → **S09a** = S09 minus the tail | 1,841 | (all of 5.3's Sanskrit material above) | 5.3-CO, B8–B11 | — | split logged |
| S09 | → **S09b** = language-family tail | 629 | sound's importance and the rules of enunciation; Vedic recitation today; the Indo-Aryan language list; the Dravidian list; the real language question = Hindi-Urdu; Pashto; Singhalese; Slavonic and European kin | **5.4-B1** | T3/T5 | list tails → T5-only |
| S10 | Buddhist Philosophy | 2,197 | Buddha using the popular Prakrit; Prakrit → Pali; the later Sanskrit revival; Ashvaghosha's plays | 5.4-B2 | T2 | — |
| S10 | | | the age of ferment: Lao-tze, Confucius, Zoroaster, Pythagoras; schools side by side; schisms; scholasticism; the warning against metaphysical controversy | 5.4-B3, B4 | T2 | — |
| S10 | | | the originality question; the morality matched from older books; the real revolt against priestcraft and practice | 5.4-B5 | T2 | — |
| S10 | | | Mahayana/Hinayana; the Buddha made a god; the century-long quarrel; the Hinayana countries' contempt; the Pali Canon vs the Mahayana's tolerance | 5.4-B6 | T2 | — |
| S10 | | | Nagarjuna in Kanishka's reign; the ladder of arguments; Shunyata = nothingness = the zero mark; relativity; "on account of Shunyata…"; Stcherbatsky | 5.4-B6 | T1/T2 | Stcherbatsky → T5-only |
| S10 | | | the four Buddhist schools; Vasubandhu's Abhidharmakosa; Radhakrishnan's account; "airy nothing"; reason and the beyond | 5.4-B6 | T2 | T5-only (names) |
| S11 | Effect of Buddhism on Hinduism | 1,777 | permanent effects on religion; Magadha where Brahminism was weak; a living religion for 1,000+ years | 5.4-B7 | T2 | — |
| S11 | | | the Aryan faith national and non-missionary vs Buddhism universal; Ashoka's missionary work; ritual disappearing, animal sacrifice especially; non-violence | 5.4-B7 | T2 | — |
| S11 | | | pessimism towards life; Hinayana and Jaina asceticism; forest settlements → huge monasteries and nunneries; Central Asia's monasteries; Balkh's Nava-vihara with 1,000 monks; the otherworldliness question | 5.4-B8 + CO | T1/T2 | — |
| S11 | | | caste's curious effect; Satyakama and his mother Jabala; "no one but a true Brahmin…"; the Brahmins the only rigid caste then; Kshatriya doors open | 5.4-B9 | T1 | — |
| S11 | | | non-violence → tilling lowly; the Indo-Aryans' proud occupation down the scale; the revolt against degradation degrading vast numbers | 5.4-B10 | T2 | — |
| S12 | How did Hinduism Absorb Buddhism in India? | 871 | Malraux's question in Paris; why few in Europe would ask it; a question after Nehru's own heart | 5.5-CO + B1 | T1 | — |
| S12 | | | no widespread or violent extermination; local conflicts with a powerful Sangha; Brahminism and Buddhism approaching each other; the Mahayana; "sickly imaginings" | 5.5-B2 | T2 | — |
| S12 | | | Buddhism as social reform releasing new talent; Ashoka's patronage; the Gupta renaissance; Shankaracharya's maths as an adoption of the sangha; degraded Buddhism in East Bengal and Sind; Buddhism vanishing | 5.5-B3 | T2 | — |
| S13 | The Indian Philosophical Approach | 1,473 | thoughts overlap; contradictions side by side; the difficulty of reconciling; material vs metaphysical problems | 5.5-B4 | T2 | — |
| S13 | | | more unity in the old personality at a lower level; personality outgrowing the individual; the little world | 5.5-B4 | T2 | — |
| S13 | | | India's old social organisation persisting; it must have had virtue; Havell's working hypothesis; metaphysics' permanence; Buddhist philosophy's part; Islam's impress | 5.5-B5 | T2 | Havell → T5-only |
| S13 | | | the six systems' common presumption: order, and a mighty rhythm | 5.5-B6 | T2 | — |
| S14 | The Six Systems of Philosophy | 4,539 | pre-Buddhist beginnings; Brahminical and Buddhist systems side by side, criticising and borrowing; the six names | 5.5-B6 | T2 | — |
| S14 | | | Nyaya: analytic and logical; Aristotle's syllogisms compared; its critical method | 5.5-B7 | T2 | — |
| S14 | | | Vaisheshika: separateness; atomic theory; dharma as the moral law | 5.5-B8 | T2 | — |
| S14 | | | Samkhya: Kapila c. 7th c BC; Garbe's verdict; co-ordinated after Buddhism; dualism of prakriti and purusha; infinite purushas | 5.5-B9 | T2 | Garbe → T5-only |
| S14 | | | Yoga: Patanjali's method; the West's "quaint practices" and exploiters; the later stages and ecstasy; body discipline and the asanas; Nehru's own practice; eating and drinking; ethical preparation, ahimsa; control of the senses; Vivekananda on reason, experience, the freedom of the mind; Yoga as experimental | 5.5-B10 | T1/T2 | Vivekananda → T5-only (gist spoken) |
| S14 | → **S14a** = up to and including Yoga/Vivekananda | 2,853 | (all of the above) | 5.5-B6..B11 | — | split logged |
| S14 | | | Mimamsa: ritualistic, polytheistic; its rules and its influence on popular Hinduism and Hindu law | 5.5-B11 | T2 | — |
| S14 | → **S14b** = Vedanta onward | 1,686 | Vedanta: from the Upanishads; pure monism; Atman; maya mistranslated as illusion; finite forms; Shankara's advaitism; caste accepted but knowledge open to all; world negation yet amazing energy; born in Malabar | **5.6-B1, B2** | T1/T2 | — |
| S14 | | | the four maths — Sringeri, Puri, Dwaraka, Badrinath; the significance of the long journeys; common land and common culture; pilgrims of all castes; the choice of sacred places (Amarnath, the Virgin Goddess) | 5.6-B3 | T1 | — |
| S15 | India and China | 3,597 | contacts through Buddhism; possible sea-borne trade before Ashoka; silk; Buddhist culture across Central Asia and Indonesia; monasteries along the routes; scholars from China learning Sanskrit in Indonesia | 5.6-B4 | T2 | — |
| S15 | | | Kashyapa Matanga 67 AD, Ming Ti, Lo Yang; manuscripts translated; original books in Chinese; Kumarajiva 401 AD, 47 works; Jinagupta's 37 translations | 5.6-B5 | T2 | figures → T5-only |
| S15 | | | the two-way traffic — Fa Hien, Sung Yun, Hsuan Tsang, I-tsing; Hsuan Tsang's route and perils; Buddhist rulers and monasteries; the Turkish Buddhists | 5.6-B6 + CO | T1 | — |
| S15 | | | the Si-Yu-Ki and its account of India (benign principles, no forced labour, light taxes, merchants); Si-an-fu; the return with manuscripts; Khorasan, Iraq, Mosul; Iran; Turfan's seven colours | 5.6-B7 | T2 | — |
| S15 | | | Harsha and the T'ang emperor exchanging embassies; the lost load at the Indus; Nalanda and its excavated ruins | 5.6-B9 | T2 | — |
| S15 | | | I-tsing: 671 AC, nearly two years to Tamralipti, Nalanda, hundreds of texts, ritual and ceremony, the monastic rules, Aryadesha, Hsin-tu, deva-putra, his judgment on Chinese superiority | 5.6-B8 | T2 | — |
| S15 | | | printing: 8th c China, division by the 10th, not in India, Tibet, Yuan 1260–1368, Germany, 15th c; what each learned; Confucius and Lao-tze; the Chinese proverb; the novel Monkey and Waley | 5.6-B10 | T2 | Waley → T5-only |
| S15 | | | cut off, then brought together by the East India Company; opium and war; Hu Shih and "the Indianization of China"; the new pilgrims who fly over the mountains | 5.6-B11 | T2 | Hu Shih → T5-only |
| S16 | Indian Colonies and Culture in SE Asia | 3,195 | travel far in time and space to see what India was; the countries where India spread; Eliot's testimony; the recent discoveries; Greater India; the sources (inscriptions, copper plates, Javanese/Balinese literature, Greek and Latin, ruins) | 5.7-B1 | T2 | Eliot, Quaritch Wales → T5-only |
| S16 | | | wave after wave of colonists from the 1st century — Ceylon, Burma, Malaya, Java, Sumatra, Borneo, Siam, Cambodia, Indo-China, Formosa, the Philippines | 5.7-B2 | T1/T3 | list tail → T5-only |
| S16 | | | Svarnabhumi/Svarnadvipa, the Land of Gold; the Malva tribe and the Malay race; Kalinga, Pallav, Orissa; 1,300 years | 5.7-B2 | T2 | — |
| S16 | | | why they went: trade as the supreme passion; Yavadvipa; trade rising 3rd–2nd c BC; missionaries after Ashoka; the old Sanskrit voyage stories; maritime intercourse by the 1st c AD; the Malay Peninsula on the China route | 5.7-B3 | T2 | Majumdar → T5-only |
| S16 | | | shipbuilding; ports; Andhra coins with two masts; Ajanta's ships; the states as naval powers fighting over sea routes | 5.7-B4 | T1/T2 | — |
| S16 | | | the 1088 AD Tamil inscription, the Corporation of the Fifteen Hundred | 5.7-B5 | T2 | — |
| S16 | | | the colonies between India and China; Sri Vijaya/Sailendra dominant by the 8th c; earlier states in Malaya, Cambodia, Java; Wilkinson's finds | 5.7-B6 | T2 | Wilkinson → T5-only |
| S16 | | | Majapahit's taxation and commerce and colonial departments; the cruel war with Srivijaya and the conflict it sowed | 5.7-B7 | T2 | — |
| S16 | | | 1511: Albuquerque takes Malacca; Europe arrives on its new sea power | 5.7-B8 | T1 | — |
| S17 | The Influence of Indian Art Abroad | 1,085 | Indian names on every throne; Sanskrit learning at Champa, Angkor, Sri Vijaya, Majapahit; writing to the Philippines; Cambodia's alphabet and Sanskrit words; Manu's laws | 5.7-B9 | T2 | — |
| S17 | | | art and architecture the strongest evidence; the impulse fused with each place's genius; Quaritch Wales; French and Dutch excavations; the Siamese student's letter to Santiniketan; Hellenism's parallel | 5.7-B10 | T1/T2 | Quaritch Wales → T5-only |
| S17 | | | Angkor Vat and its ruins, lakes, canals, bridges, the great gate's vast sculptured head; the Khmer genius and Jayavarman | 5.7-CO + B11 | T1 | — |
| S17 | | | the inspiration fading in India itself — the mind and soil overworked, no fresh currents; Sylvain Levi's line | 5.7-B11 | T2 | Levi → T5-only |
| S18 | Old Indian Art | 2,361 | finest expressions of Indian art outside India; lost northern monuments; art tied to religion and philosophy; beauty with a deeper significance; the layman's reaction | 5.8-B1 | T2 | — |
| S18 | | | Europeans trained in the Greek tradition; Gandhara as the familiar; Sitwell's contempt and Nehru's answer; Binyon and Havell; the artist identifying with nature | 5.8-B2 | T2 | Sitwell, Binyon → T5-only |
| S18 | | | Ajanta in the Gupta period (4th–6th c), Bagh, Badami; the dream-like and very real world; Ellora 7th–8th c and the Kailasa temple; Elephanta's Nataraja; Epstein | 5.8-B3 + CO | T1 | Epstein → T5-only |
| S18 | | | the Borobudur head in Copenhagen; Indian art in Java; early naturalism partly Chinese; Chinese influence at various stages; sculpture/architecture India's forte, painting China's and Japan's; Indian music's influence | 5.8-B4 | T2 | Havell → T5-only |
| S18 | | | the prejudice against graven images; Vedic opposition; Buddha's image only late | 5.8-B5 (T4: 5.2-B11) | T2 | — |
| S19 | India's Foreign Trade | 465 | trade widespread in the first millennium; merchants controlling foreign markets; dominance in the eastern seas; pepper and spices to the Mediterranean; the give-and-take of local materials | 5.8-B6 | T2 | — |
| S19 | | | chemistry more advanced; *History of Hindu Chemistry*; steel tempering; iron and steel for war; metals and medicinal compounds; distillation | 5.8-B7 | T2 | P. C. Ray → T5-only |
| S19 | | | astronomy in the university curriculum, astrology mixed in; the accurate solar calendar still in popular use; machines; shipbuilding | 5.8-B8 | T2 | — |
| S19 | | | no slave-labour economy as an advantage over Greece; caste judged "infinitely better than slavery" — Nehru's own comparison, answered in "Aaj ke hisaab se" | 5.8-B9 | T2 | flagged: Nehru's claim, not a fact |
| S20 | Mathematics in Ancient India | 2,727 | Europe's arithmetic and algebra came from the Arabs, who got them from India; why one would expect India to excel; La Place's tribute | 5.8-B10 | T2 | La Place → T5-only |
| S20 | | | the remote origins; geometrical algebra for Vedic altars; mentions in the most ancient books; Dantzig's puzzle and Greek contempt for applied science; Hogben's answer — every culture contains its own doom unless it educates the mass; the social milieu, not an erratic genius | 5.8-B11 | T2 | Dantzig, Hogben → T5-only |
| S20 | → **S20a** = the worth of the system | ~1,600 | (*all of the above in 5.8-B10/B11*) | 5.8 | — | split logged |
| S20 | | | zero + decimal place-value unbarring the gates; fractions and their rules; the rule of three; a/0 = infinity; negative quantities | **5.9-B1** | T1/T2 | — |
| S20 | → **S20b** = the journey out | ~1,100 | the mathematicians' succession 5th–12th c; Baudhayana, Apastamba, Katyayana; Brahmagupta, Bhaskara, Lilavati and the daughter question; Narayana 1150, Ganesha 1545; no original work after the 12th c | 5.9-B2 | T3/T5 | names → T5-only |
| S20 | | | Baghdad: Al-Mansur 753–774; Indian scholars and their books; the name *Hindsa*; earlier penetration of place-value into western Asia | 5.9-B3 | T2 | — |
| S20 | | | Baghdad → Moorish Spain → Europe; the objection to infidel symbols; the Sicilian coin of 1134; Britain 1490 | 5.9-B4 | T2 | — |
| S20 | | | Ramanujan: poor Brahmin family, clerkship, no education, brief life; how few of millions get schooling | 5.9-CO + B5 | T1 | — |
| S21 | Growth and Decay | 3,105 | the first millennium's vigour and ups and downs; the Gupta age as the classical moment | 5.9-B6 | T2 | — |
| S21 | | | weakness before the Golden Age closed; the White Huns' repeated hordes; the long conflict; the inner change from settling Huns; the 7th-c revival under Harsha; Ujjayini | 5.9-B7 | T2 | — |
| S21 | | | an undated, creeping inner weakness; the north split but life rich; Benares; Vikramshila, Vallabhi, Ujjayini, Amravati universities | 5.9-B8 | T2 | — |
| S21 | | | the afternoon of a civilisation; the south still vital; Bhavabhuti the last great literary figure; involved style; Bhaskara II; the last colonial emigration in the 9th c; the Cholas till the 11th | 5.9-B9 | T2 | — |
| S21 | | | India drying up from north to south; political freedom vs cultural decay (the chicken and egg); earlier declines and rejuvenation; Rome's collapse compared; no dramatic collapse in India, but progressive decline | 5.9-B10 | T2 | — |
| S21 | | | the spirit of exclusiveness; life cut into set frames; the social structure giving stability and blocking expansion; decline all along the line — intellectual, philosophical, political, warfare, contacts, local sentiment | 5.9-B11 | T1/T2 | — |

**Audit result (R14).** All 21 v2 sub-sections are placed; **zero blank clusters**. Three sub-sections are deliberately split, each at a cluster seam, each logged above: **S09** (5.3 / 5.4), **S14** (5.5 / 5.6), **S20** (5.8 / 5.9). There are no T6 atoms left over. T5 holds only names, list tails, precise figures and book titles — never a claim, an argument or an anecdote. One residual: **S01 "Through the Ages" is heading-only in v2** (the rebuild left the fragment "Na"); the chapter's own opening is not recoverable from this copy, so the set's opening frame is carried by 5.1's Ab tak. Two "flagged" rows are judgement calls, not coverage gaps: Nehru's caste-vs-slavery comparison (5.8-B9) and the Greek homosexuality passage (5.2-B9) — both must be attributed to the book on air and answered in "Aaj ke hisaab se".

---

## 4. Loading rules for this split

**Never split (R10) — these must stay inside one episode:**
1. Malraux's question from its answer — both are in **5.5** (cold open → B11). The question may be *posed* as 5.4's outro, but not answered there.
2. Nagarjuna's ladder from Shunyata — **5.4-B6** is one beat, not two.
3. Satyakama's story from its point — **5.4-B9**, whole.
4. Buddha's choice of the people's language from the language-family tail that leads into it — the tail is **5.4-B1**, the choice is **5.4-B2**; they are adjacent for a reason.
5. Harsha's embassies to the T'ang court from Hsuan Tsang in India — 5.1-B6 may *mention* Harsha's death; the embassies belong to **5.6-B9**.
6. The Taj Mahal line from the Iran material — **5.2-B5**.
7. Majapahit's war with Srivijaya from the fall of Malacca — **5.7-B7 + B8**.
8. Ajanta's painted women from the Gupta dating — **5.8-CO + B3**.
9. The zero's consequences (fractions, infinity, negatives) from the mathematicians' succession — both in **5.9-B1/B2**; and Ramanujan from the decay verdict — **5.9-B5 → B10/B11**.
10. The F/U rule: a U name introduced in a beat may not be re-anchored (R8) across an episode boundary without a 3–5 word anchor — the seams below are computed with that cost in mind.

**Seams (where the cut falls, and the hook type):**

| Seam | The source's own turn | Hook |
|---|---|---|
| 5.1 → 5.2 | the last line of S05 flows straight into "India and Iran" | **Arrival** — a man in Allahabad about to tell a legend |
| 5.2 → 5.3 | "was the Indian drama borrowed from Greece?" (S08's opening question) | **Open question the source poses** |
| 5.3 → 5.4 | Sanskrit was never the people's language (S09's end) → Buddha speaks Prakrit (S10's start) | **Reversal** |
| 5.4 → 5.5 | the last line of S11 leads into "how did it vanish?" | **Open question** (Malraux's) + the set's one **Promise** |
| 5.5 → 5.6 | the fifth door shut, the sixth standing (S14 continues) | **Promise** (the same one; promise used once per set, so 5.4's outro must *pose* the question, not promise) |
| 5.6 → 5.7 | the land route's last beat → the sea route's first (S16's opening) | **Arrival** — a ship |
| 5.7 → 5.8 | the inspiration fading at home (S17's end) → the art made at home (S18) | **Reversal** |
| 5.8 → 5.9 | "no original work after the 12th century" → the zero that had left home | **Open question** |
| 5.9 → 6.1 | Indian numerals reach Baghdad as *Hindsa* (existing handoff) | **Arrival** (Chapter 6's own opening) |

**Clusters that may live in T5 ("Kitaab mein aur") only — never spoken:**
- Scholar and critic *names* whose content is spoken: Sylvain Levi, A. Berriedale Keith, Ryder, Gilbert Murray, Krutch, Quaritch Wales, Wilkinson, Majumdar, Sir Charles Eliot, Osbert Sitwell, Lawrence Binyon, E. B. Havell, Epstein, Garbe, Stcherbatsky, Radhakrishnan, Vivekananda's quoted lines, La Place, Dantzig, Hogben, P. C. Ray, Bagchi, Waley, Hu Shih, Rapson, Darmesteter, Dodwell, Vincent Smith, Gordon Childe, F. W. Bain, Winternitz, Macnicol, Rhys Davids, Fick, Narada, Holsted.
- List tails beyond three spoken items: the 10 peoples of ch04's ledger (recap only), the Indo-Aryan and Dravidian language lists, the colonists' lands, the ports, the exports (muslins, brocades, ivory, perfumes, jewels), the metals and gems, the crafts, the six systems' subterms, the Buddhist schools' technical vocabulary, the mathematicians' book titles.
- Precise figures and variant dates: 570 towers/64 gates style measurements (not used here), the play counts (377/189/650), monk counts (3,000/10,000/1,000), the five branches of study, 360 talents of gold dust (this one may be spoken as scene detail — it is vivid), variant spellings (Asvaghosha/Ashvaghosha, Ramamujan/Ramanujam, Toga/Yoga in the OCR).
- Book titles and footnote texts.

**Where each episode must apply R17 hardest:** 5.2 (Greek and Persian names — signal 2), 5.3 (playwrights and plays — signal 2 and signal 9), 5.6 (Chinese pilgrims and place names — signals 1 and 2), 5.7 (Indonesian empires — signal 2), 5.9 (mathematicians — signal 2; decay argument — signal 11, it is a chain of causes and must be given a direction).

---

## 5. What to do with the existing scripts (5.1–5.7)

| Existing script | Verdict | What moves, and where |
|---|---|---|
| **Ep 5.1 Hamlavar jo apne ho gaye** | **Keep as-is** (extend slightly) | It already owns v2's S02–S05. Patch: change the source line to `book/chapters_v2/ch05.txt`; **lift the two GAP notes** (the Heliodorus inscription and the poet's lines are now in v2 — put the three precepts into the cold open and the poet's lines into B10); rename old S04/S05/S06 → v2 S04/S05/inside-S02; extend to 5,050 words (it is at ~4,700) by adding the Harsha 648/Ujjayini cluster to B6 and the south's migration cluster to B7. Its cold open and pillar spine stay. |
| **Ep 5.2 Do bhai, ek dhun** | **Keep as-is** | Owns v2 S06+S07 exactly. Patch: source line; re-check the `$2a`/`$2b` truncation notes and the three footnotes against v2 and lift whichever v2 resolves (the Zimmern footnote text is present now); rename S07/S08 → S06/S07. Cold open, spine and eleven parts unchanged. |
| **Ep 5.3 Shakuntala ka safar** | **Extend in place, minus one cluster** | Owns S08 + S09a. The language-family cluster of its P10 (~630 words: the Indo-Aryan and Dravidian lists, Hindi-Urdu, Pashto, Singhalese, Sanskrit's kin in European languages) **moves out to 5.4-B1** — the new P10 ends on "Sanskrit kisi ke ghar ki zubaan nahi thi". Rewrite the Outro to the new 5.4 handoff (Buddha speaks the people's tongue). Give P5/P7 more words (v2's S08 grew by 1,231 words) and lift the GAPs v2 resolves (Levi, Ryder, the Euripides quotations may move from T5 to a single spoken line each where memorable). |
| **Ep 5.4 Bina jung ki vidaai** | **Re-cut into the new set** | Its **cold open (Malraux) and P9, P10, P11** (Bina yuddh ki vidaai / Do gawah / Malraux ke sawal ka jawab) **move to 5.5**, together with the title. Its **P1–P8 stay** and become 5.4's body: P1 (Buddh ki zubaan) → B2; P2 (Us daur ka toofan) → B3; P3 (Phoot kyun padi) → B4; P4+P5 (Nagarjuna ka tark, Seedi jo khaali mein khatam hoti hai) → merged into B6; P6 (Vihara se Bihar) → B7; P7 (Satyakama ka jawab) → B9; P8 (Hal chalane wala neeche) → B10. **New:** cold open (the monastery at dawn), B1 (the language tail from 5.3), B5 (the originality question), B8 (monasteries and Balkh), B11 (payoff) and a new Outro that poses Malraux's question as a cliffhanger. The script **keeps its file name** and becomes the title-free episode (new title: **Vihara se Bihar**). Its internal references to "7 episodes wale set" must be updated to nine. |
| **Ep 5.5 Chaar dishaon ke math** | **Re-cut into the new set** | Its **P1 (Chaar kone, chaar ghar)** and **P9 (Chhetta darwaza — Vedanta)**, and everything in them about the four maths and Shankara's journeys, **move to 5.6** as B1–B3; the Kedarnath half of its cold open goes with them (as 5.6's B3 material, or as 5.6's cold open if the owner prefers Shankara over Hsuan Tsang as the opener — see below). Its **P2, P3 (the approach), P4 (Nyaya), P5 (Vaisheshika), P6 (Yoga), P7 (Qaidi ki asana)** stay and become 5.5's B4–B10; its **P8 (Mimamsa)** folds into B11. Its **P10 (Chaar dishaon ke math)** is superseded. **New:** cold open (Malraux, taken from old 5.4), the frame beats B1–B3 (from old 5.4's P9–P11), Samkhya (B9 — v2's Samkhya paragraphs were missing before and are new material), and the payoff beat. The title **"Chaar dishaon ke math"** is retired; if the owner prefers to keep it, it should become **5.6's** title with China riding under it. |
| **Ep 5.6 Pahaad paar, samundar paar** | **Re-cut into the new set** | Its **cold open (Hsuan Tsang, with the old Ep 5 SFX plan)** stays **5.6's** cold open. Its **P1–P6** (the mountain road, China) stay and expand to the v2 clusters (roughly 1,200 words of new Chinese material: Kashyapa Matanga, Kumarajiva, Jinagupta, Si-Yu-Ki, Nalanda, printing, *Monkey*, Hu Shih). Its **P7, P8, P10, P11** (the sea, the Land of Gold, the two empires, 1511) **move to 5.7**. Its **P9 (Mitti, dhaatu, dawa — trade, chemistry, metals)** **moves to 5.8**'s B7. **New:** B1–B3 (the sixth door and the four maths, from old 5.5) and the rewritten Outro. New title: **Chaar kone, pahaad ke us paar** (or keep the old subtitle shape by calling it *Chaar dishaon ke math, pahaad ke us paar*). **Owner's choice:** if the Hsuan Tsang cold open should be preserved at all costs — and it should, its SFX plan is already produced — then the Kedarnath material **stays inside 5.6 as a beat**, not as a cold open, and old 5.5's Kedarnath cold open is retired to *kalpana*-listed imagery. |
| **Ep 5.7 Shunya, aur phir dopahar** | **Re-cut into the new set, and the set's close moves to 5.9** | Its **cold open (the Bayon's smile)** moves to **5.7** (the Land of Gold). Its **P1, P2** (the smile, Cambodia/alphabet) → 5.7-B9/B11. Its **P3 (Aadha itihaas)** → 5.8-B1; **P4 (Ajanta ki auratein)** → 5.8-B3. Its **P5 (Shunya)** → 5.9-B1; **P6 (Ginti ka jangla)** → 5.8-B11 + 5.9-B2; **P7 (Hindsa)** → 5.9-B3; **P8 (Madras ka ek clerk)** → **5.9's cold open**; **P9, P10, P11 (the decay verdict, and the 674-word P11)** → 5.9-B6..B11. The title **"Shunya, aur phir dopahar"** stays with **5.9**, which is still the set's close and still ends on the chapter's own verdict. Its eight resolved GAPs stay resolved (v2 holds the Levi, Sitwell, Epstein, La Place, Dantzig, Hogben and `$2a`/`$2b` text). |
| **Ep 5 Through the Ages** (the original single episode) | **Archive** | Historical only. Its cold open (Hsuan Tsang) lives on in 5.6; its SFX plan is re-timed for 5.6's cold open. |

**Write order.** 5.6 and 5.7 first (heaviest new material, thinnest reuse), then 5.4 and 5.5 (the biggest re-cuts), then 5.8 and 5.9, then patch 5.1, 5.2, 5.3. Every script's Episode info must name the nine-episode set, the set question, the v2 ids, and `book/chapters_v2/ch05.txt` as the only source.

---

## 6. Summary (25 lines)

1. Source is now `book/chapters_v2/ch05.txt`: 43,296 words, 21 sub-sections, rebuilt from the Internet Archive full text.
2. The lossy copy was 28,033 words; the loss fell hardest on Growth and Decay (+1,745), Six Systems (+1,242), Greece (+1,474), Theatre (+1,321), Mathematics (+1,186), China (+1,468).
3. All eight old GAPs are resolved in v2; no library check is needed any more.
4. The chapter becomes **9 episodes**, not 7: source ≈ 4,800 words each, narration 5,000–5,200, ratio ≈ 1.0.
5. Set question unchanged: *Itni chamak ke baad, thakaan kahan se aayi?*
6. 5.1 **Hamlavar jo apne ho gaye** — S02+S03+S04+S05, 4,633 words. Keep, two GAP patches.
7. 5.2 **Do bhai, ek dhun** — S06+S07, 5,141. Keep as-is.
8. 5.3 **Shakuntala ka safar** — S08 + S09a, 5,397. Extend; the language-family tail moves to 5.4.
9. 5.4 **Vihara se Bihar** — S09b+S10+S11, 4,603. Re-cut; new cold open at the vihara; Malraux material leaves.
10. 5.5 **Bina jung ki vidaai** — S12+S13+S14a (five doors), 5,197. Re-cut; Malraux's mystery arrives here and is answered here.
11. 5.6 **Chaar kone, pahaad ke us paar** — S14b (Vedanta, Shankara, the four maths) + S15 (China), 5,283. Old Hsuan Tsang cold open retained.
12. 5.7 **Sone ki dharti** — S16+S17, 4,280. The colonies and the art abroad; the Bayon smile becomes its cold open.
13. 5.8 **Ajanta ki auratein** — S18+S19+S20a, 4,426. What the hands made; the worth of the zero.
14. 5.9 **Shunya, aur phir dopahar** — S20b+S21, 4,205. The set's close: the numbers leave, a clerk in Madras, and the afternoon.
15. Three sub-sections split on purpose, each at a cluster seam: S09, S14, S20.
16. Unplaced sub-sections: none. **S01 "Through the Ages" is heading-only in v2** (a stray "Na"); it is carried by 5.1's Ab tak.
17. Rebuild artifact to watch: `## ` headings sit about one paragraph early in v2 — match clusters by content, not line position.
18. U budget ≤75 per episode; heaviest risk is 5.2, 5.6, 5.7 (names) — three spoken items per list, tail to T5.
19. Never split: Malraux's question from its answer; Nagarjuna's ladder; Satyakama; Harsha's embassies from Hsuan Tsang; the zero from the mathematicians; Ramanujan from the verdict.
20. Seams are all source turns; one Promise only (5.4 → 5.5/5.6), everything else Arrival, Reversal or open question.
21. Existing 5.1, 5.2 keep as-is; 5.3 extends; 5.4, 5.5, 5.6, 5.7 are re-cut and their parts move as listed in §5.
22. 5.1's cold open gains the Heliodorus precepts; 5.4 gets a new cold open; 5.7 takes the Bayon; 5.9 takes the Madras clerk; 5.6 keeps Hsuan Tsang.
23. Old ids S01–S22 are dead: v2's S01–S21 is the only numbering (§0's mapping table).
24. Write order: 5.6, 5.7 → 5.4, 5.5 → 5.8, 5.9 → patch 5.1, 5.2, 5.3.
25. Nothing in Chapter 5 is left to "Kitaab mein aur" that is a claim, an argument or an anecdote — only names, list tails, figures and titles.
