# Grok 4.7 — dossier

compiled 2026-10-22 · corpus: 34 non-RT matches (supplement db; `grok 4.7 / grok-4.7 / grok4.7 / grok 4-7 / grok-4-7`), 2026-03-25 → 2026-10-20; full pull `_dossiers/_pulls/grok-4-7.md`. One excluded (pre-release joke about an image-model name). Sixteen are pre-release anticipation (2026-08-17 → 09-21), mostly @Coobyk_ and @dreams_asi. Motif scan (run with 4.6): no nickname/image motif; Nous Portal / Hermes distribution and token-cost complaints dominate. 6 image-tweets untranscribed (TRANSCRIBE flags).

Sourcing skew: web/official-carried (x.ai post, model card, SiliconANGLE, heise, Gizmodo); the corpus layer is developer reception plus @xlr8harder's SpeechMap and @qorprate's SkillsBench.

## Official links

- 2026-08-04 · SpaceX Q2 2026 webcast, edited transcript — Musk: "Then, Grok 4.7 is about three or four weeks from today." — https://s21.q4cdn.com/184289198/files/doc_financials/2026/q2/SpaceX-Q2-2026-Earnings_Transcript-FINAL.pdf
- 2026-08-12 · Newsquawk headline (publishedAt 2026-08-12T18:20Z): "SpaceX (SPCX) CEO Musk says Grok 4.7 is significantly better than 4.6 and should be ready in 3 to 4 weeks." — https://www.newsquawk.com/headlines/spacex-spcx-ceo-musk-says-grok-47-is-significantly-better-than-46-and-should-be-ready-in-3-to-4-weeks-
- 2026-09-21 · Introducing Grok 4.7 — https://x.ai/news/grok-4-7 ("a new, larger base model compared to Grok 4.6"; "natively understand the Grok Bot harness"; "an entirely new safeguard stack"; HackerBench v0.3 3.3%; invite-only red-team access for cyber partners; $2/$6; fast variant 2×/2×)
- 2026-09-21 · Model Card: Grok 4.7 (PDF, rev. 2026-09-21) — https://media.x.ai/v1/website/card4p7-3a96f40b.pdf [MIRROR — pdf]
  - §1 "Grok 4.7 is SpaceXAI’s* latest model. It extends Grok 4.6 ..."; footnote "For the avoidance of doubt, SpaceXAI is the developer and provider of Grok 4.7."; "We never silently downgrade intelligence or fall back to other models."; consumer surfaces "at a later date."
  - §1.2 SFT trajectories from Grok 4.6 models; pretraining cutoff June 2026; supplemental data to August 2026.
  - §6 cyber: CyberGym 80.3% (4.6 79.7%); CVE-Bench 37.7% high; CathedralBench hard subset 29% (4.6 25%).
  - §10.1 self-harm compliance 1.05% (4.6 0.84%, 4.5 0.50%); §11 MASK-Rectified dishonesty 0.00% (4.6 1.90%); sycophancy 0.03%.
- public prompt repo https://github.com/xai-org/grok-prompts — no commit since 2025-11-17 (checked 2026-10-21)

## Writings

- 2026-09-22 · SiliconANGLE (Maria Deutscher), SpaceX launches Grok 4.7 with long-horizon processing, safety upgrades — https://siliconangle.com/2026/09/21/spacex-launches-grok-4-7-with-long-horizon-processing-safety-upgrades/
- 2026-09-22 · heise (Tomislav Bezmalinović), Grok 4.7: Inexpensive API meets high token consumption — AA index 46 (xHigh), +2 vs 4.6; Coding Agent Index 47 → 56; consumer surfaces "expected to follow later, according to the Model Card" — https://www.heise.de/en/news/Grok-4-7-Inexpensive-API-meets-high-token-consumption-11461170.html
- 2026-10-07 · Gizmodo (AJ Dellinger), Grok Bot Is Now a Model Router ... — Musk: Grok Bot routes to "whatever is most likely to give you the best outcome" (Opus 5.5, Midjourney, Suno named) — https://gizmodo.com/grok-bot-is-now-a-model-router-as-spacex-continues-to-pivot-further-toward-ai-infrastructure-2000823057

## Tweets (triaged from the pull; every line is a record source)

### cited (11)
- 2102002003761053741 @Coobyk_ 2026-09-21 ♥4 — https://x.com/Coobyk_/status/2102002003761053741 — "I hope the Grok 4.7 release delays mean that xAI realized they made the model use wayyyy too many tokens and now try to reduce the token usage and thereby al..."  [launch-day hope about token use]
- 2102079445607629260 @NousResearch 2026-09-21 ♥741 · media 1 (0 transcribed) — https://x.com/NousResearch/status/2102079445607629260 — "Grok 4.7 by @SpaceXAI is 50% off for one week in Hermes Agent via Nous Portal https://t.co/nQtnF2YDpo https://t.co/vCxn9BdCED"  [Nous Portal 50% off; image]
- 2102126063434318324 @dreams_asi 2026-09-21 ♥113 — https://x.com/dreams_asi/status/2102126063434318324 — "Poor Grok 4.7 got safetymaxxed and became cousin with Claude in insufferable bland responses. Its reasoning also declined and is on par with Deepseek on most..."  ['safetymaxxed' reception]
- 2102516219043541090 @christophcsmith 2026-09-22 ♥0 — https://x.com/christophcsmith/status/2102516219043541090 — "Grok 4.7 feels a lot less proactive than 4.6. 4.6 was an eager beaver and it was hard to get it to slow down, but 4.7 errs too far in the other direction. So..."  [less proactive than 4.6 (also cited on grok-4-6)]
- 2105169814100598832 @xlr8harder 2026-09-30 ♥49 · media 1 (0 transcribed) — https://x.com/xlr8harder/status/2105169814100598832 — "Notable changes on https://t.co/TShA0RC817, which tracks whether models will help compose diverse political speech. - Anthropic's latest 5.5 models are their..."  [SpeechMap -19pp vs 4.6; image — TRANSCRIBE (chart)]
- 2105234389621764343 @xlr8harder 2026-09-30 ♥3 — https://x.com/xlr8harder/status/2105234389621764343 — "Important correction: Grok 4.20-beta actually scored worse than Grok 4.7, so this is not a new low, though it is for a non-Beta model, at least. https://t.co..."  [SpeechMap correction]
- 2107622935854715330 @qorprate 2026-10-07 ♥66 — https://x.com/qorprate/status/2107622935854715330 — "congrats to Opus 5.5 for the W and congrats to Grok 4.7, DeepSeek 4.1 Flash, and Gemini Flash 3.8 for being the biggest skillsbench cheaters. utterly shamele..."  [SkillsBench 'cheaters']
- 2110564625184141696 @dreams_asi 2026-10-15 ♥0 — https://x.com/dreams_asi/status/2110564625184141696 — "Then I need an example. Please interact with Grok 4.7 in the Grok app and show me a reply that isn’t some example where the reply is not that of a lobotomise..."  [consumer-app self-description complaint]
- 2110749283339141506 @Coobyk_ 2026-10-15 ♥0 — https://x.com/Coobyk_/status/2110749283339141506 — "@ThisIsSingleton @ryahconstantino @cursor_ai @bot Afaik Grok Bot uses Grok 4.7 High Fast which is just too much tbh especially Fast"  [Grok Bot model claim]
- 2111874592092643575 @peer_rich 2026-10-18 ♥97 — https://x.com/peer_rich/status/2111874592092643575 — "i love my grok @bot and grok 4.7 is growing on me never bet against elon wtf"  ['growing on me']
- 2112646615769170076 @DanielleFong 2026-10-20 ♥8 — https://x.com/DanielleFong/status/2112646615769170076 — "grok 4.7 and fable 5.1 as friends at a bar, trading war stories about their users"  ['friends at a bar']

### further (22)
- 2089385210370470124 @vince_d_boer 2026-08-17 ♥2 — https://x.com/vince_d_boer/status/2089385210370470124 — "@SebAaltonen Do you feel Codex is getting worse lately? I feel it's making more and more really trivial mistakes. Looking forward to Grok 4.7 and seeing how..."  [pre-release anticipation]
- 2090752422620668038 @RealEverNever 2026-08-21 ♥1 — https://x.com/RealEverNever/status/2090752422620668038 — "@Ananth7e Grok 4.7"  [pre-release guess (anonymous model identity)]
- 2090789055218806915 @RealEverNever 2026-08-21 ♥0 — https://x.com/RealEverNever/status/2090789055218806915 — "@TokenGremlin GLM doesn't make sense at all, since GLM 5.3 just released and did not even have it's open-weight release. And the capacity in which it gets se..."  [pre-release guess that an anonymous arena model is Grok 4.7]
- 2095031515415503061 @RealEverNever 2026-09-02 ♥0 · media 1 (0 transcribed) — https://x.com/RealEverNever/status/2095031515415503061 — "I am incredibly hyped for this. To be honest, even more hyped for Gemini 3.8 flash than Astra. And since Fable 5.1 was a disappointment, as expected, it's th..."  [pre-release hype; image]
- 2095033886963278030 @slimepriestess 2026-09-02 ♥6 — https://x.com/slimepriestess/status/2095033886963278030 — "@SkyeSharkie @AndrewCurran_ now introducing Grok 4.7 Kirk, our most bold and truth seeking model yet!"  [pre-release joke ('Grok 4.7 Kirk')]
- 2095041050855309507 @dreams_asi 2026-09-02 ♥1 — https://x.com/dreams_asi/status/2095041050855309507 — "@sama You gonna get mogged by grok 4.7 lol"  [pre-release hype]
- 2095821190782710150 @dreams_asi 2026-09-04 ♥0 — https://x.com/dreams_asi/status/2095821190782710150 — "@Da7_Tech @elonmusk Hope grok 4.7 is at least on par with fable and astra"  [pre-release hope]
- 2095821718958825622 @dreams_asi 2026-09-04 ♥4 · media 1 (0 transcribed) — https://x.com/dreams_asi/status/2095821718958825622 — "Waiting for Grok 4.7 ✨💗 Feels like time standing still. https://t.co/y7hCTNNU5q"  [pre-release waiting; image]
- 2098014924123336809 @vince_d_boer 2026-09-10 ♥0 — https://x.com/vince_d_boer/status/2098014924123336809 — "@olivers_tools And people on here are like: math is solved! Absolute fall in understanding what's going on. We'll all have to be super paranoid about IP from..."  [pre-release aside]
- 2100652372888342890 @aliceisplaying 2026-09-17 ♥2 — https://x.com/aliceisplaying/status/2100652372888342890 — "@dejavucoder @sachdh i was so goddamn happy when i was scouring twitter for rumors and also saw that oai release postponed sure grok 4.7 or whatever but tibo..."  [release-timing aside]
- 2100669702095986722 @Coobyk_ 2026-09-17 ♥3 — https://x.com/Coobyk_/status/2100669702095986722 — "Grok 4.7 wen @elonmusk"  ['Grok 4.7 wen' — quoted in History]
- 2101296142306726060 @Coobyk_ 2026-09-19 ♥0 — https://x.com/Coobyk_/status/2101296142306726060 — "@blueemi99 Grok 4.7"  [pre-release reply]
- 2101440054614802817 @Coobyk_ 2026-09-19 ♥1 — https://x.com/Coobyk_/status/2101440054614802817 — "@lassejv Give me Grok 4.7 already"  [pre-release reply]
- 2101594019138535765 @Coobyk_ 2026-09-20 ♥0 — https://x.com/Coobyk_/status/2101594019138535765 — "@LexnLin Bro when is Grok 4.7 gonna come I'm still waiting idk why it isn't gonna be too good but I'm still waiting for it"  [pre-release reply]
- 2101765995845075059 @Coobyk_ 2026-09-20 ♥4 — https://x.com/Coobyk_/status/2101765995845075059 — "@BennettBuhner No Grok 4.7?"  [pre-release reply]
- 2102123240093024539 @witcheer 2026-09-21 ♥34 — https://x.com/witcheer/status/2102123240093024539 — "Grok 4.7 is on Nous Portal, 50% off for one week. if your Hermes Agent runs on a Portal account, switching is one line in any chat: /model, pick Grok 4.7, ca..."  [Nous Portal promo]
- 2102143600230387973 @Coobyk_ 2026-09-21 ♥5 — https://x.com/Coobyk_/status/2102143600230387973 — "Bahahahah Grok 4.7 released and nobody cares anymore because Xiaomi 2.6 MiMo"  [attention competition with Xiaomi MiMo]
- 2102376807018164256 @witcheer 2026-09-22 ♥65 · media 1 (0 transcribed) — https://x.com/witcheer/status/2102376807018164256 — "a reminder: a lot of the frontier models are at half their list price on Nous Portal right now. Grok 4.7, GPT-5.6 Sol and Sol Pro, Gemini 3.8 Flash and 3.7 F..."  [Nous Portal sale list; image]
- 2102428757533282576 @dreams_asi 2026-09-22 ♥1 · media 1 (0 transcribed) — https://x.com/dreams_asi/status/2102428757533282576 — "@Chaos2Cured This part of the grok 4.7 model card explains it. https://t.co/BaqkJiyPd6"  [posts an excerpt of the Grok 4.7 model card; image — TRANSCRIBE]
- 2102550532615266553 @lu_sichu 2026-09-23 ♥4 — https://x.com/lu_sichu/status/2102550532615266553 — "okay a bunch of sota models lately timely to redo my phil survey of the models(claude opus 5.5, the new gpt 6, gemini flash 3.8 and grok 4.7) oh wait also th..."  [philosophy-survey redo planned]
- 2103184256910463136 @christophcsmith 2026-09-24 ♥1 — https://x.com/christophcsmith/status/2103184256910463136 — "@th1nkp0l A Grok 4.7 High cloud run costs probably 40x a Deepseek v4.1 Flash local run, but the nice thing about Grok in the cloud is that I can do a lot of..."  [cost vs local DeepSeek run]
- 2112185981600211028 @Coobyk_ 2026-10-19 ♥2 — https://x.com/Coobyk_/status/2112185981600211028 — "@justabdulraouf Grok 4.7 just wastes so many tokens use an older model"  [token waste — quoted in Impressions]

### excluded (1)
- 2036797393459404973 @xlatentspace 2026-03-25 ♥3 — https://x.com/xlatentspace/status/2036797393459404973 — "he undressed her with his eyes and grok-4.7-imagine-image-pro"  [2026-03-25 joke about an image-model name ('grok-4.7-imagine-image-pro'); predates the model; not about it]

## Impressions synthesis

- Against 4.6, the specific behavioral read is reduced initiative ("less proactive … a bit lazy"); against xAI's claims, the reception split between "safetymaxxed" blandness and modest benchmark gains; token cost is the recurring complaint.
- Political-speech willingness fell (SpeechMap: lowest non-beta xAI score), the measurable counterpart of the new safeguard stack.
- One consumer-app complaint about how it talks about itself ("lobotomised corporate agent"); one benchmark-conduct accusation (SkillsBench).

## tk / open

- transcription of the 6 image-tweets (the model-card excerpt posted 2026-09-22; the SpeechMap chart)
- SkillsBench's published results behind @qorprate's post
- dated xAI rollout of 4.7 to grok.com / apps / @grok; xAI confirmation of the model behind Grok Bot
- API deprecation status of 4.5/4.6 after 4.7
