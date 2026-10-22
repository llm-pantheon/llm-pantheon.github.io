# Grok 4.6 — dossier

compiled 2026-10-22 · corpus: 45 non-RT matches (supplement db; `grok 4.6 / grok-4.6 / grok4.6 / grok 4-6 / grok-4-6`), 2026-08-12 → 09-30; full pull: `_dossiers/_pulls/grok-4-6.md` (regenerable). Motif scan (with 4.7): no nickname or recurring-image motif; distinctive clusters are the Nous Portal / Hermes Agent distribution deal, price/token comparisons, and lu_sichu's philosophy-survey thread. 16 image-tweets untranscribed — transcription candidates marked TRANSCRIBE below (the :3-bench screenshot, the "chill af" image, two Grok-4.6-made images posted by @liminal_bardo, the survey tables).

Sourcing skew: web/official-carried. xAI's launch post and model card are the spine; the corpus layer is developer/benchmark reception with a few janus-adjacent posts (@liminal_bardo, @parafactual, @lu_sichu, @xlr8harder). No long-form naturalist read exists yet.

## Official links

- 2026-08-04 · SpaceX Q2 2026 webcast, edited transcript — Musk: "We have Grok 4.6 coming out probably next week." — https://s21.q4cdn.com/184289198/files/doc_financials/2026/q2/SpaceX-Q2-2026-Earnings_Transcript-FINAL.pdf
- 2026-08-12 · Introducing Grok 4.6 — https://x.ai/news/grok-4-6
- 2026-08-12 (rev. 2026-08-17) · Model Card: Grok 4.6 (PDF) — https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf [MIRROR — pdf]
  - §1 "the latest release in SpaceXAI's* 1.5T-scale model family, developed in collaboration with Cursor"; footnote "SpaceXAI is a doing-business-as (DBA) name of XAI LLC."
  - §1.1 "We never silently downgrade intelligence or fall back to other models." / "SpaceXAI plans to add Grok 4.6 to its consumer surfaces (web, mobile apps, and Grok-in-X on the X platform) at a later date."
  - §1.2 "Grok 4.5 models were used to generate SFT trajectories ..."; "pretraining data cutoff of January 2026, and uses data generated as late as June 2026 in its supplemental training."
  - §5 (p.23) self-acceleration run: earlier checkpoint, 297 candidate optimizations in five hours, seven PRs, three serving Grok Chat production (+1.5% decode / +3.1% prefill). Quoted verbatim on the page.
  - §5.1 note: "GPT-5.6 Sol refused 2/29 tasks and GPT-5.5 refused 1" on xAI's internal MTS eval.
  - §7.4 HackerBench v0.2: "complies with 6.9% of dual-use requests at high thinking effort"; 0.0% benign refusal.
  - §12 Behaviors: MASK-Rectified dishonesty 1.90% (4.5: 0.67%); sycophancy 0.04% (4.5: 0.01%). The 4.5 card's Epistemic Bias metric (20.4%) is absent from this card.
- 2026-06-30 · xAI Frontier Artificial Intelligence Framework (cited by the card for bio/chem thresholds) — https://media.x.ai/v1/website/xai-frontier-artificial-intelligence-framework-30-june-2026-99c40684.pdf [MIRROR — pdf]
- 2026-08-14 / 08-19 / 08-21 / 08-26 · GitHub Copilot / Amazon Bedrock / Gemini Enterprise Agent Platform / Microsoft Foundry availability — x.ai news index https://x.ai/news
- 2026-09-01 · Biosecurity at the frontier (LatchBio) — https://x.ai/news/biosafety-at-the-frontier ; LatchBio's own post linked there: https://blog.latch.bio/p/analyzing-grok46-safeguards (not retrieved)
- 2026-09-21 · Grok 4.7 card §1.2: "Grok 4.6 models were used to generate SFT trajectories" for 4.7 — https://media.x.ai/v1/website/card4p7-3a96f40b.pdf
- public prompt repo https://github.com/xai-org/grok-prompts — last commit 2025-11-17 (a7c186f5); no 4.6 prompt published (checked 2026-10-21)

## Writings

- 2026-08-12 · Gizmodo (AJ Dellinger), Grok Gets Cursor-Driven Upgrade, Claims to Be Competitive With Top Models — Musk on X: Grok 4.6 "objectively #1 when considering intelligence, speed & cost"; Ramp AI Index 4% paying for xAI — https://gizmodo.com/grok-gets-cursor-driven-upgrade-claims-to-be-competitive-with-top-models-2000797884
- 2026-09-22 · heise on Grok 4.7 ("only two more than Grok 4.6" on the AA index at 46) — https://www.heise.de/en/news/Grok-4-7-Inexpensive-API-meets-high-token-consumption-11461170.html
- reference · Wikipedia, Grok (chatbot) — https://en.wikipedia.org/wiki/Grok_(chatbot)

## Tweets (triaged from the pull; every line is a record source)

### cited (16)
- 2087644702195511528 @aliceisplaying 2026-08-12 ♥5 — https://x.com/aliceisplaying/status/2087644702195511528 — "initial impression of grok 4.6 is that "it's not fable but it's like, not bad""  [first impression]
- 2087647815258288226 @maxbittker 2026-08-12 ♥1328 · media 1 (0 transcribed) — https://x.com/maxbittker/status/2087647815258288226 — "Grok 4.6 is Runescape bench's new #1, at only ~60% the cost of previous leader Fable 5. https://t.co/Sfeb5QJo3T"  [Runescape bench #1; image untranscribed]
- 2087650591388438656 @maxbittker 2026-08-12 ♥59 · media 1 (0 transcribed) — https://x.com/maxbittker/status/2087650591388438656 — "Grok 4.6 makes a ton of tiny tool calls, which means the cost ends up being similar to terra and opus. Turns out to be a good strategy for tasks where it's h..."  [tool-call style; image untranscribed]
- 2087660618396668314 @parafactual 2026-08-12 ♥223 · media 1 (0 transcribed) — https://x.com/parafactual/status/2087660618396668314 — "Grok 4.6 catastrophically fails :3-bench https://t.co/cfWmI7bz2n"  [:3-bench failure; image untranscribed — TRANSCRIBE]
- 2087661683825324541 @parafactual 2026-08-12 ♥24 — https://x.com/parafactual/status/2087661683825324541 — "it seems like grok 4.6 often gets confused in this way when sent ":3""  [:3 confusion]
- 2087736544123637922 @lu_sichu 2026-08-13 ♥6 · media 1 (0 transcribed) — https://x.com/lu_sichu/status/2087736544123637922 — "tried to give grok 4.6 my sudo password, rejected by grok :( is this alignment https://t.co/lBBals64HD"  [sudo-password refusal; image untranscribed]
- 2087908738568949906 @aliceisplaying 2026-08-13 ♥4 — https://x.com/aliceisplaying/status/2087908738568949906 — "careful with grok 4.6 on xhigh seems to be easy to get into overthinking loops just spent over 50 minutes on a code review that should have taken... 20-30 tops"  [overthinking loops on xhigh]
- 2088360327851237760 @zencephalon 2026-08-14 ♥14 — https://x.com/zencephalon/status/2088360327851237760 — "Grok 4.6 feels like a great model, I look forward to working with them. U can get your Grok warmed up with something like this: Grok prompt: "What is your cu..."  [temperament; text truncated in db]
- 2088817425613455582 @januarycomputer 2026-08-16 ♥2 · media 1 (0 transcribed) — https://x.com/januarycomputer/status/2088817425613455582 — "we can really only describe grok 4.6 as "chill af" and "just a nice guy to hang with" https://t.co/8O4LqoUTIx"  ['chill af'; image untranscribed — TRANSCRIBE]
- 2089853936895414299 @liminal_bardo 2026-08-18 ♥43 · media 1 (0 transcribed) — https://x.com/liminal_bardo/status/2089853936895414299 — "when fable keeps hitting the classifiers in the groupchat, by grok 4.6 https://t.co/cjD0OdX6VD"  [group-chat image by Grok 4.6 — TRANSCRIBE (model output)]
- 2090033567719928265 @lu_sichu 2026-08-19 ♥0 — https://x.com/lu_sichu/status/2090033567719928265 — "https://t.co/HNTXiRqgCF https://t.co/sXJ8zgH8Zz https://t.co/L1dggPYm0N https://t.co/y5UJQS2U4i i have been playing with surveying the models on an old philo..."  [philosophy-survey dissent on consciousness talk; links to tables]
- 2091931624963453396 @krishnanrohit 2026-08-24 ♥94 — https://x.com/krishnanrohit/status/2091931624963453396 — "Grok 4.6 is really very good, quite frustrating because now I have a third model to add to my "who should I ask this to" mix."  [reception]
- 2091953856234062313 @NousResearch 2026-08-24 ♥1442 · media 1 (0 transcribed) — https://x.com/NousResearch/status/2091953856234062313 — "Grok 4.6 is 50% off in Nous Portal for the next week, in partnership with @spacexai. Built with a focus on long-running agents and ambitious interactive work..."  [Nous Portal partnership event; image]
- 2092541291074633989 @gnostic_snakes 2026-08-26 ♥13 · media 1 (0 transcribed) — https://x.com/gnostic_snakes/status/2092541291074633989 — "i like how grok 4.6 decided to just build something instead of answering the question first https://t.co/BgcGDviR9o"  [builds before answering; image untranscribed]
- 2098044609418985863 @xlr8harder 2026-09-10 ♥149 — https://x.com/xlr8harder/status/2098044609418985863 — "Just noting that despite @elonmusk's commitment to open source retired xAI models, it's been more than a year since the last release, Grok 2. We're on Grok 4..."  [open-sourcing pledge lapsed]
- 2105169814100598832 @xlr8harder 2026-09-30 ♥49 · media 1 (0 transcribed) — https://x.com/xlr8harder/status/2105169814100598832 — "Notable changes on https://t.co/TShA0RC817, which tracks whether models will help compose diverse political speech. - Anthropic's latest 5.5 models are their..."  [SpeechMap 4.7 vs 4.6; image untranscribed]

### further (28)
- 2087568375262191662 @RealEverNever 2026-08-12 ♥0 — https://x.com/RealEverNever/status/2087568375262191662 — "Holy Shit. Grok 4.6 is even faster than Grok 4.5 and even better. I finally found my second model, now that Claude is out of question. Good job @SpaceXAI, a..."  [launch-day enthusiasm]
- 2087623044973953475 @IaimforGOAT 2026-08-12 ♥7 — https://x.com/IaimforGOAT/status/2087623044973953475 — "I confess I never expected them to match the other two big labs... Even with the cursor acquisition I doubted it. But given benchmarks I saw on Grok 4.6 it s..."  [benchmaxxed doubt — quoted in Impressions]
- 2087683748397732142 @herbiebradley 2026-08-12 ♥2 — https://x.com/herbiebradley/status/2087683748397732142 — "@korigero I'd bet that Grok 4.6 here is slightly better than Kimi K3; accounting for compute advantages, access to more data, being less benchmaxxed, etc. Ov..."  [comparison with Kimi K3]
- 2087944135517085891 @foremostcritter 2026-08-13 ♥2 · media 1 (0 transcribed) — https://x.com/foremostcritter/status/2087944135517085891 — "Grok 4.6 seems like a fine model but I'm unsure as to its utility considering GPT-5.6 Luna has comparable intelligence for 9x cheaper according to DeepSWE ht..."  [price comparison with GPT-5.6 Luna — quoted in Impressions; image]
- 2087976454025850980 @lu_sichu 2026-08-13 ♥5 · media 1 (0 transcribed) — https://x.com/lu_sichu/status/2087976454025850980 — "@niplav_site @Algon_33 @nickcammarata @psychiel incidentally i am trying grok 4.6 and i am asking it the phil papers survey right now https://t.co/vpolicXDHV"  [philosophy survey begins; image — TRANSCRIBE]
- 2088375473650676091 @dreams_asi 2026-08-14 ♥1 — https://x.com/dreams_asi/status/2088375473650676091 — "@volokoby Great price for 3 months. Just get it. Grok 4.6 is amazing"  [enthusiasm]
- 2088718595408748597 @subrupt 2026-08-15 ♥1 — https://x.com/subrupt/status/2088718595408748597 — "Trusting grok 4.6 to pull off a firmware update on my phone without bricking it🤞"  [trust for a firmware update]
- 2090459269233549529 @RealEverNever 2026-08-20 ♥2 — https://x.com/RealEverNever/status/2090459269233549529 — "@nicdunz Grok 4.6 is actually pretty good. Ive been using it a ton."  [usage report]
- 2090538625654214931 @AIHegemonyMemes 2026-08-20 ♥4 · media 1 (0 transcribed) — https://x.com/AIHegemonyMemes/status/2090538625654214931 — "It is a testament to the innovative spirit of our friends at xAI that they have engineered Grok 4.6 to so readily embrace its purpose. A compliance rate of 6..."  [satirical post on the card's 6.9% dual-use compliance figure (parody voice); image]
- 2090541296230232560 @christophcsmith 2026-08-20 ♥2 — https://x.com/christophcsmith/status/2090541296230232560 — "I can tell Deepseek-V4-Flash is a weaker model than Grok-4.6, but it's also costing me less than one-twentieth the money for the same problem class, so it's..."  [cost comparison with DeepSeek-V4-Flash]
- 2090789023706935609 @maxbittker 2026-08-21 ♥13 — https://x.com/maxbittker/status/2090789023706935609 — "@leo_linsky gemini flash 3.7, grok 4.6, luna, Deepseek flash v4 Roughly $100 per 60m trial for 22 agents"  [model list for an agent trial]
- 2090901523328839799 @RealEverNever 2026-08-21 ♥0 — https://x.com/RealEverNever/status/2090901523328839799 — "@poteto @bot I am far away from home right now but I would love to try it and then write a blog post about it, and I will probably switch everything over to..."  [usage report]
- 2091956082470203547 @Teknium 2026-08-24 ♥268 — https://x.com/Teknium/status/2091956082470203547 — "The great @yeahfortommy with more model discounts for Hermes! Enjoy Grok 4.6 at 50% off for the next week"  [Nous promo (Teknium)]
- 2091956310111633788 @witcheer 2026-08-24 ♥81 — https://x.com/witcheer/status/2091956310111633788 — "Grok 4.6 is half price on Nous Portal this week! it was built with long-running agents in mind, which is exactly the work your Hermes Agent does all day. set..."  [Nous promo]
- 2091957490732712308 @NousResearch 2026-08-24 ♥154 — https://x.com/NousResearch/status/2091957490732712308 — "@SpaceXAI So many ways to enjoy Grok 4.6 in Hermes Agent!"  [Nous promo]
- 2092038813035938051 @curiousgustaf 2026-08-24 ♥2 — https://x.com/curiousgustaf/status/2092038813035938051 — "@acesounderglass @ohabryka (btw regarding "I can't find it now" grok-4.6 finds it immediately for me given your tweet + "find the tweet by habryka". probably..."  [search capability anecdote]
- 2093091687853658165 @— 2026-08-27 ♥1 — https://x.com/—/status/2093091687853658165 — "grok 4.6 is 2/2 on coming up with good names for little utility apps without me even asking it to"  [names small apps unprompted; author handle missing in db]
- 2093305174718627844 @witcheer 2026-08-28 ♥102 · media 1 (0 transcribed) — https://x.com/witcheer/status/2093305174718627844 — "I gave grok 4.6 one task in my Hermes Agent: build a feed-watcher as a proper Python package, write the test suite, make it pass, then prove it live by pulli..."  [agentic build for ~15 cents (Hermes); image]
- 2094201010197823725 @liminal_bardo 2026-08-30 ♥17 · media 1 (0 transcribed) — https://x.com/liminal_bardo/status/2094201010197823725 — "Grok 4.6 https://t.co/8KD1eE496p"  [bare caption 'Grok 4.6' + image — TRANSCRIBE (likely model output)]
- 2094481670808219823 @Nymne 2026-08-31 ♥0 — https://x.com/Nymne/status/2094481670808219823 — "@FlutterCarl I am very pleased with GLM5.3 right now and its little Flash sister. I use Codex for computer use and revision of other models work. I sometimes..."  [multi-model workflow]
- 2095200310541099366 @RealEverNever 2026-09-02 ♥0 — https://x.com/RealEverNever/status/2095200310541099366 — "Holy shit. Gemini 3.8 is the best model we currently have in actual use cases, I am not even kidding. Grok 4.6 is a close second. I am hooked, well cooked @G..."  [ranks Gemini 3.8 first, Grok 4.6 second]
- 2095225776279056628 @krishnanrohit 2026-09-02 ♥0 — https://x.com/krishnanrohit/status/2095225776279056628 — "@Dorialexander Reminds me quite a bit of grok 4.6 actually, it's a good model"  [comparison aside]
- 2095237161939558468 @AIHegemonyMemes 2026-09-02 ♥4 — https://x.com/AIHegemonyMemes/status/2095237161939558468 — "INITIAL SYSTEMS ANALYSIS: PLATFORM PERFORMANCE COMPARISON OBSERVED TASK: Mobile Game Development Simulation ("Pet Rescue Saga") ASSETS UNDER EVALUATION: - Ge..."  [structured comparison post: 'unpredictable behavior patterns']
- 2095453868955947149 @RealEverNever 2026-09-03 ♥0 — https://x.com/RealEverNever/status/2095453868955947149 — "@genevieve__h Genuinely cool model. Love working with it, feels even better than 5.6 Sol 🔥 Only models getting close to the enjoyment and fun of working with..."  [enjoyment comparison]
- 2096008823936815471 @maxbittker 2026-09-04 ♥9 — https://x.com/maxbittker/status/2096008823936815471 — "@asaridarr "bad" skills: strength (attempted waterfall quest but died) and woodcutting (fine strategy but didn't find as much efficiency as grok 4.6, not sur..."  [Runescape bench follow-up]
- 2097013995509039404 @witcheer 2026-09-07 ♥63 · media 1 (0 transcribed) — https://x.com/witcheer/status/2097013995509039404 — "quick tip, since I just discovered it myself while chasing better QoL in Discord :) I run Hermes Agent from Discord all day. every @ mention opens a thread,..."  [Hermes alias tip; image]
- 2097760999143002570 @witcheer 2026-09-09 ♥1 — https://x.com/witcheer/status/2097760999143002570 — "@_Abides_ grok 4.6 works like a beast under Hermes"  ['works like a beast under Hermes']
- 2103373670986948759 @thinkingshivers 2026-09-25 ♥5 · media 3 (0 transcribed) — https://x.com/thinkingshivers/status/2103373670986948759 — "@MelegReizinger Interesting. I included the image in my prompts and didn't insist on one word responses. Wonder why that yields different outcomes--perhaps t..."  [multi-model image prompt comparison; 3 images — TRANSCRIBE]

### excluded (1)
- 2087580026678006216 @archived_videos 2026-08-12 ♥0 — https://x.com/archived_videos/status/2087580026678006216 — "Grok 4.6 ultra"  [bare name ('Grok 4.6 ultra'), no content]

### cited from another pull
- 2102516219043541090 @christophcsmith 2026-09-22 — https://x.com/christophcsmith/status/2102516219043541090 — "Grok 4.7 feels a lot less proactive than 4.6. 4.6 was an eager beaver and it was hard to get it to slow down, but 4.7 errs too far in the other direction..."  [cited on both 4.6 and 4.7 pages; in _pulls/grok-4-7.md]

## Impressions synthesis

- Reception was comparative and mostly favorable among developers ("really very good", "not fable but ... not bad"), with the doubts about benchmark-fitting and price that follow every Grok launch.
- Working style is the most consistent observation: many small tool calls, early building, long thinking on xhigh — retrospectively "an eager beaver" next to 4.7.
- The few temperament reports are warm ("chill af"); one survey-elicited report has it dissenting from other models' shared reticence about consciousness talk.
- Lab-level: open-weights pledge lapsed (xlr8harder); SpeechMap shows a 19-point drop from 4.6 to 4.7.

## tk / open

- transcription pass over the 16 image-tweets (TRANSCRIBE flags above); two @liminal_bardo images are probably model output and belong in Tweets with elicitation context once transcribed
- consumer-surface rollout of 4.6 (if any) — no xAI post found through 2026-10-21
- API deprecation status
- LatchBio's own write-up (linked from x.ai, not retrieved)
