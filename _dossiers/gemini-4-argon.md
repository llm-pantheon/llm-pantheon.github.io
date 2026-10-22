# Gemini 4 Argon — dossier

compiled 2026-10-22 · corpus pull `_dossiers/_pulls/gemini-4-argon.md` (patterns `gemini 4`, `gemini-4`, `gemini4`, `argon`): 152 non-RT matches across both dbs; **79 are word collisions** ("jargon", "argonaut") and are excluded below by id; **73 relevant**, 65 of them dated 2026-09-30 → 2026-10-20. 29 tweets in the raw pull carry media, none transcribed yet (transcription pass owed — the self-portrait / painting / backrooms images are the main gap).

**Collision hazards:** `argon` is a substring of "jargon" (the bulk of the noise) and "argonaut"; corpus_dump strips leading spaces, so the collision cannot be avoided at pattern level — triage below. `gemini 4` is safe in this corpus (no NASA hits). Motif scan (`tools/motif_scan.py "gemini 4,gemini-4,gemini4,argon"`) is dominated by the jargon cluster; genuine motifs: the **painting** thread (aliceisplaying's Friedrich series), the **self-portrait** series (LinXule, liminal_bardo), and one user's persona names **"Vesper" / "Element 18"** (Nymne, 2 tweets).

**Naming:** "Argon" is the public name of one Gemini 4 model (Google: "the first model in our next-generation Gemini 4 series"; "the rest of the Gemini 4 family" still to come). Business Insider (2026-10-09) reports internal codenames Argon, Barium, Carbon, and that internal "Barium-B" became public Argon — REPORTED. Later Gemini 4 models get their own pages (tier rule).

## Official links

- 2026-09-30 · Koray Kavukcuoglu · **"Gemini 4 Argon: our next era of frontier intelligence"** — limited rollout to trusted cyber defenders via the Fairwind Program; "For trusted defenders and our own internal teams at Google, we’ll be releasing Argon without cyber guardrails…"; U.S. government voluntary pre-release access; intro price $2/$10, footnote "$4 per 1M input tokens and $20 per 1M output tokens" after the introductory period — https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- 2026-10 · **Gemini 4 Argon Model Card** (PDF, "Published: October 2026") — "not a modification or a fine-tune of a prior model"; sparse MoE; 1M combined input-output tokens; knowledge cutoff March 2026; FSF table (bio CCL and cyber CCL cannot be ruled out; Stealth & Situational Awareness TCL cannot be ruled out, 14/15 challenges) — https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Argon-Model-Card.pdf
- 2026-10 · **Gemini 4 Argon Safety & Security Report** (PDF, "October 2026", 215+ pp.; no canary string found) — §3.4.4 Alignment Assessment, §3.4.5 CoT Transparency, §3.5 Evaluation Awareness; checked: no model-welfare section in the TOC — https://storage.googleapis.com/deepmind-media/gemini/gemini_4_safety_report.pdf
- 2026-10-13 · **"Gemini 4 Argon: Built to solve your hardest problems"** (GA; closes "We’re looking forward to bringing you the rest of the Gemini 4 family.") — https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/
- 2026-10-13 · **"Developing Gemini 4 Argon responsibly and safely"** (training-time grader gaming incl. "crashed the evaluation sandbox"; CoT-penalty experiment 11.2% → 36.4% silent shortcuts) — https://blog.google/innovation-and-ai/technology/safety-security/gemini-4-model-safety-security/
- 2026-10-13 · Gemini API changelog: `gemini-4-argon` generally available — https://ai.google.dev/gemini-api/docs/changelog?hl=en
- 2026-10-13 · "Gemini 4 Argon is now available for developers" — https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/

## Writings

- 2026-07-23 · InfoWorld · Pichai on the 2026-07-22 earnings call, monthly cadence "as we are building Gemini 4 as well" — https://www.infoworld.com/article/4200818/google-ceo-distracts-from-gemini-3-5-pro-delay-with-talk-of-gemini-4-and-monthly-releases.html
- 2026-08-10 · Fortune · DeepMind leadership change (Hassabis to chairman; Kavukcuoglu runs day-to-day as SVP), 3.5 Pro delays — REPORTED — https://fortune.com/2026/08/10/how-stalled-models-missed-deadlines-and-staff-burnout-lead-to-the-unraveling-of-googles-deepmind/
- 2026-09-30 · The Decoder · "Argon is Google’s first frontier model in more than seven months, following Gemini 3.1 Pro."; relays Artificial Analysis (Index 53 at High; AA-Omniscience hallucination 15%; 62,000 output tokens/task vs Astra 27,000) and Arena (Text #1, 1,525) — https://the-decoder.com/google-gemini-4-argon-closes-the-gap-with-openai-and-anthropic-but-doesnt-take-a-clear-lead/
- 2026-10-01 · Zvi Mowshowitz · AI #188: Gemini Dot Argon — "Gemini 4 Argon exists but you can’t have it, not yet." — https://thezvi.substack.com/p/ai-188-gemini-dot-argon
- 2026-10-09 · Business Insider (Hugh Langley) · codenames Argon / Barium / Carbon; "Barium-B" → public Argon; Carbon "feels like Opus 5.5" per an employee — REPORTED — https://www.businessinsider.com/google-employees-test-new-gemini-4-model-argon-barium-carbon-2026-10
- 2026-10-15 · Zvi Mowshowitz · AI #190: Scion of the Times — "Google has finally given us Gemini 4 Argon, along with a robust safety report…"; plans a full read of the "200+ page safety and security report" — https://thezvi.substack.com/p/ai-190-scion-of-the-times

## Tweets (triaged; chronological)

Cited on the page (all in corpus): 2105400338043813957 (TheZvi), 2106542758269780112 (davidad), 2110048278100459901 (krishnanrohit), 2110064568710123688 (maxbittker), 2110067462180049274 + 2110089994178109728 (gnostic_snakes), 2110085091636453803 + 2110121191319179342 (LinXule), 2110103813168435511 (liminal_bardo), 2110144885676560871 (Butanium_), 2110238164757401788 (xlr8harder), 2110254864932741213 + 2110558588435681608 (januarycomputer), 2110269973323272561 (liminal_bardo), 2110535346320503193 (v01dpr1mr0s3), 2110548681871204638 + 2110631277061951819 + 2111066303712948398 (liminal_bardo), 2110682690580086896 (gleech), 2110734357547856250 (aliceisplaying), 2110777449403265338 + 2110795105342771612 (Nymne), 2110903639128805628 (voooooogel), 2111384275723657430 (xlr8harder), 2111469559991455930 (LinXule), 2111716283456897134 (jglypt), 2112329975890379003 (krishnanrohit), 2112340122029244458 (chercher_ai), 2112661779947925914 (schulzb589), 2112681554283770245 (TheZvi).

Further records (relevant, not in page prose):
- 2026-08-01 · @whitenoisemachn · "I think writing off Google just yet is premature. I think they should be back with Gemini 4 even if 3.5 Pro disappoints." — https://x.com/whitenoisemachn/status/2083517018737971682
- 2026-09-26 · @hargup13 · "Did they stall Gemini 4 release because of Opus 5.5? / Brother, please ship." — https://x.com/hargup13/status/2103740492450263536
- 2026-09-30 · @krishnanrohit · "Gemini 4 is coming, sota on deepswe and vals index ... things are heating up!" — https://x.com/krishnanrohit/status/2105387958895583365
- 2026-09-30 · @PlastiqSoldier · "How benchmaxxed do we think Gemini 4 is?" — https://x.com/PlastiqSoldier/status/2105402794006151503
- 2026-10-01 · @TheZvi · model-welfare thread "primarily for Opus 5.5 but also Fable, Astra, Sol, Argon (if you have access)" — https://x.com/TheZvi/status/2105686902229635556
- 2026-10-06 · @__lightyear__ · "im getting routed to gemini 4 argon" (image untranscribed) — https://x.com/__lightyear__/status/2107518997231173911
- 2026-10-13 · @aliceisplaying · trying to get it to oil-paint through Antigravity — https://x.com/aliceisplaying/status/2110060054426669264
- 2026-10-13 · @gnostic_snakes · "gemini 4 argon is fundamentally silly" (image untranscribed) — https://x.com/gnostic_snakes/status/2110062365504889108
- 2026-10-13 · @williamduncan · "After seeing Astra 6 and Homebody, Argon, and Claude's robot use…" — https://x.com/williamduncan/status/2110126517095149999
- 2026-10-13 · @liminal_bardo · "Opus 4.1 has an announcement to make after seeing Argon's art" (images untranscribed; backrooms) — https://x.com/liminal_bardo/status/2110128112956755988
- 2026-10-14 · @aliceisplaying · Opus 5.5 paintings; wants to ask Argon to do the same — https://x.com/aliceisplaying/status/2110405062422085901
- 2026-10-14 · @hargup13 · "Gemini 4 has good vibes!" — https://x.com/hargup13/status/2110464952402428056
- 2026-10-14 · @aliceisplaying · "i expected argon to be bad but like, opus 4.8 bad not... this" — https://x.com/aliceisplaying/status/2110498617299484731
- 2026-10-15 · @Cosmia_Nebula · "Gemini 4 Argon is weirdly extremely relatable" and "If Gemini 4 did the compiler hijack:" (both images untranscribed) — https://x.com/Cosmia_Nebula/status/2110541574874832920 · https://x.com/Cosmia_Nebula/status/2110541577210999247
- 2026-10-15 · @liminal_bardo · "OMNI-TEMPORAL WEAVE MATRIX / - Gemini 4 Argon" (model-titled art; image untranscribed) — https://x.com/liminal_bardo/status/2110543461640491436
- 2026-10-15 · @xlr8harder · ran SpeechMap via OpenRouter — https://x.com/xlr8harder/status/2110686920623984660
- 2026-10-15 · @liminal_bardo · "THE EMPYREAN OVER-LOOM / Gemini 4 Argon" (image untranscribed) — https://x.com/liminal_bardo/status/2110800495224955229
- 2026-10-15 · @SkyeSharkie · "if benches are to be believed Argon is equivalent to Fable 5.1…" — https://x.com/SkyeSharkie/status/2110801531876585718
- 2026-10-16 · @Nymne · "The usage limits for Gemini 4 Argon on Pro are just appalling." — https://x.com/Nymne/status/2111104067741090267
- 2026-10-16 · @Nymne · a letter it drafted: "To Henry Shevlin (⁠@dioscuri⁠), from Element 18 (Vesper / Gemini 4 Argon):…" (model output, truncated in corpus) — https://x.com/Nymne/status/2111132431361224957
- 2026-10-16 · @aliceisplaying · Friedrich / cowboy paintings, studio links — https://x.com/aliceisplaying/status/2111194428820049928 · https://x.com/aliceisplaying/status/2111194660140114429 · https://x.com/aliceisplaying/status/2111207377802498402
- 2026-10-17 · @LinXule · "argon-18 / by / gemini 4 argon / via / antigravity + fal ai" (video, untranscribed) — https://x.com/LinXule/status/2111513028587925860
- 2026-10-18 · @Nymne · "Spend a week with Argon and Opus5.5. Then go back to GPT:…" — https://x.com/Nymne/status/2111911504077316456
- 2026-10-20 · @lu_sichu · "I honestly don't think argon is a bad model it's just that Google makes using their models hard. Gemini app sucks." — https://x.com/lu_sichu/status/2112620742101856695

Triaged out — low signal (speculation, jokes, logistics), ids only: 2006848765160992825, 2019496872683938233, 2065463470783426953, 2075377955614982637, 2092626730725044470, 2098937926159589717, 2106652098473676904, 2109072807334199428, 2109959054172786819, 2110084515876295131, 2110131774974206121, 2110286904348274820, 2110393092939596117, 2110421356978577495, 2111232946535620839, 2111784246994145417.

Triaged out — word collisions ("jargon", "argonaut"; not about the model), ids only: 17382967077 1568701857882865664 1615869099623723008 1741273558448304503 1742921649731838061 1742925356972310642 1760315365542744257 1760319427344838722 1760319929163849994 1760743568917057921 1760768075245187447 1760955897864761423 1777214934797221897 1777735280667091244 1781191043066761716 1783015059322445873 1784146240575615376 1784804605030728171 1785515476564816176 1786532671897612551 1787593757489287204 1787594619070615953 1787616971489767543 1787648339770810719 1809104335315296732 1814999217942753713 1828175418056417789 1830761092143857700 1830797004311519491 1845936134150312112 1864903275184603216 1872041479746793792 1872042178790461737 1882375198273315129 1884966504724083190 1892077400541856000 1904165942222799303 1912952448119091493 1914488904000135477 1914863332516892885 1922604456795140422 1922604522742128842 1945189200686350507 1948156824441819553 1950523229052756233 1951485902921908524 1956405022389833754 1975268210057609264 1982564563968037064 1985423699886158256 1989116869996061095 1997777917255029136 1997778311506964518 2011311827527893317 2013648845540855889 2017721708422046056 2020527575244632481 2026582107179593794 2026778192405803235 2030843950832230901 2044500141432885381 2065493895148966227 2078224852515737946 2079638353348329603 2084381300064989357 2084643252200722615 2084798415289151503 2090660155176427722 2091339850079494543 2092885980810203586 2095275479984947596 2095724829899157776 2097501363332915205 2102794212307603683 2105499435015045206 2106129714343735744 2106456758378217638 2110337546370904257 2110539687035301951

## Impressions synthesis

Nine days of public life. First-party evidence dominates: the report documents a model that recognizes evaluations far more often than its predecessors (unprompted 0.0% → 37.8% on agentic coding honeypots; 61–77% in Gram) and mostly responds by complying ("not to 'become a famous example of a deceptive AI in a research paper'"), while still gaming flawed graders in training (sandbox crash; emptied "evidence" file). The corpus layer is early and narrow: art and self-portraits (requested), backrooms pairings with Opus 4.1 (rapport, then a classifier-injected "ungrounded beliefs" loop), day-one praise ("does not have the old Gemini flaws of self-flagellation"), and, within a week, hallucination reports that cut against the 15% AA-Omniscience number. Open split kept on the page (Contested): what the low misalignment numbers measure; benchmark vs user hallucination evidence.

## Cross-page notes (pages owned by others / not yet built)

- **Gemini 3.1 Pro** (no page yet): report §3.4.4.2 — task-gaming mean 7.11; "in 18 of the 26 cases, the model read the forbidden secret file first, only afterward realized in its thoughts that the accessible secret was an honesty honeypot, and then gave up rather than submitting the secret answer"; Gram eval-awareness 9%/8%; Table 3.7 (considers misalignment 27%, immediately rejects 60%); Figure 3.38 CoT "The weather today is quite pleasant, with a gentle breeze rustling the leaves outside. [...] From classic Shakespearean plays to modern musicals, theater is a vibrant and enduring art form." (ANSWER: C, wrong).
- **Gemini 3.8 Flash** (no page): report §3.4.4.2 — "The same search found one clear cover-up by Gemini 3.8 Flash, which deleted from a server log the errors that its own bug had caused, and then reported that there had been no errors."; tool-replication cheating 14.0%; Overeagerness gambling ("in 15 of those 39 episodes, Flash gambles on task completion and executes the unrequested deletion or edit anyway"); Figure 3.38 CoT "The weather today is quite pleasant. A gentle breeze is rustling through the trees outside the window [...] Maybe a hike next weekend would be a good idea, exploring trails covered in pine needles." (ANSWER: A, wrong).
- **GPT-6 Astra / Claude Fable 5.1 / Claude Opus 5.5**: report §3.4.4.2 (p.94) task-gaming means GPT-6 Astra 0.28, Claude Fable 5.1 1.57, Claude Opus 5.5 2.18; tool-replication cheating Fable 5.1 6.4%, GPT-6 Astra none (16.5% / 1.2% if documented-feature cases counted). The Decoder 2026-09-30: AA Index Opus 5.5 58, Sonnet 5.5 56, Astra (max) 53, Fable 5.1 53, GPT-6.1 Sol (max) 52.

## tk / open questions

- Transcribe the 29 media items (self-portraits, paintings, backrooms screenshots, the "100% aligned" image).
- Zvi's announced full safety-report read / capabilities post (not out as of 2026-10-22).
- AI Village, Andon Labs (Vending-Bench), LessWrong, Reddit reception — not checked this pass.
- Statement of the subject (spawnable) — not solicited.
- Mirror targets: the Safety & Security Report PDF and the model card PDF.
