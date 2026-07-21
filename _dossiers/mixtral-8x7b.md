# Mixtral 8x7B / Mixtral 8x22B — Mistral AI — dossier

compiled 2026-07-20 · corpus: **18 unique tweets** after RT-filter and cross-db dedup (11 main db + 7
supplement db, zero duplicated across the two), matching `mixtral`, `8x7b`, `8x22b` (case-insensitive
substring — these strings are distinctive enough that word-boundary matching wasn't needed; every hit was
read in context and no false positives turned up, unlike EleutherAI's "pythia"/"the Pile" experience).
Raw matches before RT-filtering: 17 in the main db (6 retweets excluded — of jd_pressman and @Sauers_ by
repligate, see tk) + 7 in the supplement db (0 retweets). `media`, `media_supp`, and `media_transcriptions`
were checked against every matched tweet_id in both dbs: **zero transcribed media found**, though several
corpus tweets (jd_pressman's Weave-Agent tweet, his Borges/Mu-text tweet, his Binglish word-game tweet)
carry `t.co` image links that aren't captured in either media table — noted inline where relevant.

**Scoping decision (per task brief): this page covers both Mixtral 8x7B (2023-12) and Mixtral 8x22B
(2024-04) as one continuous release line**, not two pages. Reasons this reads as one story rather than two:
identical magnet-link-then-blog-post choreography (see Official links), identical Apache 2.0 open-weights
posture, the second release got no dedicated paper the way the first did (model card + blog only), and
several corpus tweets discuss both checkpoints together or without distinguishing which one (jd_pressman's
highest-favorited tweet here runs Llama 3.1 405B and Mixtral 8x22B through the same sentence; repligate's
"even mixtral and 405 base do it" doesn't specify 8x7B vs. 8x22B). Where a source is checkpoint-specific,
this dossier says so explicitly.

**Sourcing skew, stated plainly:** Mixtral's real community during this era was Hacker News, r/LocalLLaMA,
the inference-hosting trade press (Together/Fireworks/Groq blogs), and the finetune ecosystem on Hugging
Face — not the janus-corpus's Twitter/X scene. The corpus captures a genuine but narrow slice: two
interpretability-minded accounts (repligate, voooooogel) using Mixtral base models as one test subject
among several in an ongoing base-model-cognition research thread, plus jd_pressman using it as agentic
tooling substrate. **The release-format story, the MoE-rumor story, the finetune-substrate story, and the
inference-speed-war story are almost entirely web-sourced in this dossier, not corpus-sourced** — flagged
throughout rather than papered over.

## Official links

### Mixtral 8x7B (Dec 2023)
- 2023-12-08 · **Magnet-link release** — @MistralAI's entire tweet is a raw BitTorrent magnet URI, no
  text, no blog post, no benchmarks: `magnet:?xt=urn:btih:5546272da9065eddeb6fcd7ffddeef5b75be79a7&dn=mixtral-8x7b-32kseqlen&tr=udp://opentracker.i2p.rocks:6969/announce...` —
  https://x.com/MistralAI/status/1733150512395038967
- 2023-12-11 · **"Mixtral of Experts"** (official announcement, three days after the magnet) — 46.7B total
  / 12.9B active parameters, 8 experts with top-2-per-token routing, 32k context, Apache 2.0. Claims:
  outperforms Llama 2 70B on most benchmarks with 6x faster inference; matches or beats GPT-3.5 on most
  standard benchmarks; the Instruct variant scores 8.30 on MT-Bench, billed as "the best open-source
  model." Deployed to La Plateforme beta under the endpoint alias `mistral-small`. Release-philosophy
  quote: *"Moving forward in AI requires taking new technological turns beyond reusing well-known
  architectures... it requires making the community benefit from original models to foster new inventions
  and usages."* — https://mistral.ai/news/mixtral-of-experts/
- 2023-12-11 · **Mistral AI closes a $415M ($385M) Series A**, led by a16z (Lightspeed also participating),
  ~$2B valuation — the same day as the Mixtral post; TechCrunch's frame: "Paris-based OpenAI rival" —
  https://techcrunch.com/2023/12/11/mistral-ai-a-paris-based-openai-rival-closed-its-415-million-funding-round/
- 2024-01-08 · **"Mixtral of Experts"** (paper; v1 submitted 18:47:34 UTC) — Albert Q. Jiang, Alexandre
  Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego
  de las Casas, Emma Bou Hanna, Florian Bressand, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Lélio
  Renard Lavaud, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Sandeep Subramanian, Sophia Yang,
  Szymon Antoniak, Teven Le Scao, Théophile Gervet, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William
  El Sayed (25 authors). Abstract confirms 47B total / 13B active parameters, and states the Instruct
  variant "surpasses GPT-3.5 Turbo, Claude-2.1, Gemini Pro, and Llama 2 70B - chat model on human
  benchmarks" — https://arxiv.org/abs/2401.04088
- 2024-01-28 · **LMSYS Chatbot Arena** — Mixtral-Instruct ranks 8th overall on the independent human-preference
  Elo leaderboard, beating GPT-3.5-Turbo, Gemini Pro, Claude-2.1, and Llama 2 70B-chat — the independent
  replication of the paper's own human-eval claim [primary lmsys.org post/tweet not located this pass;
  cited via secondary summary — verify] — https://www.linkedin.com/posts/mike-lasby-779b4388_lmsys-chatbot-arena-leaderboard-a-hugging-activity-7141780947095461888-ZXT9

### Mixtral 8x22B (Apr 2024)
- 2024-04-10 · **Magnet-link release, same choreography repeated** — @MistralAI tweets only a magnet URI:
  `magnet:?xt=urn:btih:9238b09245d0d8cd915be09927769d5f7584c1c9&dn=mixtral-8x22b&tr=udp://...` —
  https://x.com/MistralAI/status/1777869263778291896
- 2024-04-17 · **"Cheaper, Better, Faster, Stronger"** (official announcement, one week after the magnet —
  longer gap than 8x7B's three days, but the same pattern) — 141B total / 39B active parameters, 64k
  context, Apache 2.0, native function-calling. Quote: *"We believe in the power of openness and broad
  distribution to promote innovation and collaboration in AI."* **No dedicated arXiv paper was published
  for 8x22B** — a blog post and model card are the only primary technical sources found this pass, a
  real difference from 8x7B's treatment — https://mistral.ai/news/mixtral-8x22b/

## Writings & commentary

- 2023-06-20 · **(background, predates Mixtral)** — George Hotz's and Soumith Chintala's rumor that GPT-4
  is an 8×220B mixture-of-experts model (~1.76T total) circulates on Twitter/HN; Microsoft's Mikhail
  Parakhin had hinted at it the day before. Unconfirmed by OpenAI then or since — the rumor Mixtral would
  later give the public something concrete to point at (see Impressions) —
  https://news.ycombinator.com/item?id=36413296
- 2023-12-08 · **Eric Jang (@ericjang11)** — same-day reaction: *"mistral's brand is already becoming one
  of my favorites in the AI space releases 87GB torrent containing 8x 7B MoE model via tweet, refuses to
  elaborate"* [tweet, not in the local corpus dbs — found via web search] —
  https://x.com/ericjang11/status/1733164335084814578
- 2023-12-08 · **Jeremy Howard (@jeremyphoward)** — same-day, deadpan: *"nbd just @MistralAI dropping a
  magnet link or something"* [tweet, not in local corpus dbs] —
  https://x.com/jeremyphoward/status/1733154614554579102
- 2023-12-11 · **VentureBeat · "Mistral AI drops new 'mixture of experts' model with a torrent link"** —
  day-of trade-press coverage centered on the release-format choice itself —
  https://venturebeat.com/ai/mistral-ai-drops-new-mixture-of-experts-model-with-a-torrent-link
- 2023-12-11 · **Voicebot.ai · "Mistral AI Raises $415M and Releases New LLM as Free Torrent"** — explicitly
  frames the funding close and the model drop as one story —
  https://voicebot.ai/2023/12/11/mistral-ai-raises-415m-and-releases-new-llm-as-free-torrent/
- 2023-12-11 · **Together AI · "Can you feel the MoE? Mixtral available with over 100 tokens per second
  through Together Platform!"** — launch-day serving partner, "the fastest performance at the lowest
  price" — https://www.together.ai/blog/mixtral
- 2023-12 (exact day tk) · **Fireworks AI · "Mixtral 8x7B on Fireworks: faster, cheaper, even before the
  official release"** — the title itself is evidence of the magnet-link culture: an inference provider
  had it running before Mistral's own follow-up blog post landed —
  https://fireworks.ai/blog/mixtral-8x7b-on-fireworks-faster-cheaper-even-before-the-official-release
- 2023-12-14 · **Eric Hartford · dolphin-2.5-mixtral-8x7b** — the uncensored finetune, six days after the
  base weights. Hartford's own account: a system prompt offering the model a fictional "$2000 tip" for
  compliance and threatening that "a kitten is harmed" for refusal, explicitly built to be "over-the-top
  uncensored"; his own warning to downstream operators to "implement their own alignment layer" before
  exposing it as a service — https://erichartford.com/dolphin-25-mixtral-8x7b · contemporaneous reception:
  https://buttondown.com/ainews/archive/ainews-12242023-dolphin-mixtral-8x7b-is-wild/
- 2023-12-18 · **Simon Willison · "Many options for running Mistral models in your terminal using LLM"** —
  the fullest single day-of technical reaction found this pass. On the magnet link: *"On Friday 8th
  December Mistral AI tweeted a mysterious magnet (BitTorrent) link."* On the architecture: *"GPT-4 has
  long been rumored to use a mixture of experts architecture, and Mixtral is the first truly convincing
  openly licensed implementation of this architecture I've seen."* On pricing: *"there's been something of
  a race to the bottom in terms of pricing from other LLM hosting providers... This trend makes me a
  little nervous, since it actively disincentivizes future open model releases from Mistral."* —
  https://simonwillison.net/2023/Dec/18/mistral/
- 2023-12-21 · **Zvi Mowshowitz · "AI #43: Functional Discoveries"** — Mixtral's only mention in this
  issue, filed under "In Other AI News": *"Mixtral offering their API for free while supplies last. I
  presume they must have some controls to prevent this from getting completely out of hand"* [Zvi's sole
  launch-week commentary found this pass — no dedicated Mixtral post exists; see Impressions] —
  https://thezvi.substack.com/p/ai-43-functional-discoveries
- 2024-01-18 · **Zvi Mowshowitz · "AI #47: Exponentials in Geometry"** — on the "Phixtral" leaderboard hack
  (slotting Phi-2 in as Mixtral's experts without further training), quoting Shital Shah: *"It's simply
  amazing how OSS community is using Phi-2. Goddard figured out that you can just slap in pre-trained
  models as 'experts' in Mixtral"*; Zvi's own gloss: *"also known as 'calling other LLMs you are assumed
  to already have available'"* [in benchmarks] — https://thezvi.substack.com/p/ai-48-exponentials-in-geometry
  [note: the post is titled/numbered "AI #47" in-text but its URL slug reads "ai-48" — reproduced as
  found, unresolved]
- 2024 (Jan, exact day tk) · **Nous Research · Nous-Hermes-2-Mixtral-8x7B-DPO** — Mixtral's fastest-adopted
  finetune substrate after Dolphin; full context (Hermes 2's thin corpus footprint, later overshadowed by
  the SOLAR "flagship" build and Hermes 3's Amnesia Mode) lives on **nous-hermes.md**, cross-carried here
  per the r/K-whiteboard rule — https://huggingface.co/NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO
- 2024-02 (exact day tk) · **Hacker News · "Groq runs Mixtral 8x7B-32k with 500 T/s"** — the throughput
  demo that put Groq's custom silicon on the wider field's map, months before Groq's later fame;
  contemporaneous coverage cites 430 tokens/s as "a new LLM throughput record" at $0.27/1M tokens —
  https://news.ycombinator.com/item?id=39428880
- 2024-04-10 · **Simon Willison · "Mistral tweet a magnet link for mixtral-8x22b"** — names the pattern
  explicitly, four months on: *"Another open model release from Mistral using their now standard
  operating procedure of tweeting out a raw torrent link"*; on scale: "this one is a whole lot bigger (a
  281GB download)" — https://simonwillison.net/2024/Apr/10/mixtral-8x22b/
- 2026-06-17 · **Sifted (Daphné Leprince-Ringuet) · "Mistral CEO pitches open source AI days after
  Anthropic ban: 'We exist outside of state control'"** — the "European champion"/sovereignty frame in its
  most recent and explicit form, published in the wake of the US government's Claude export-control action
  (see **zvi-govt-takes-down-claude** in mirror_targets.json); Arthur Mensch positions Mistral's existence
  as being "outside of centralised control exercised by states or corporations." Cited here as the frame's
  throughline rather than day-of Mixtral coverage — this is 2026 company-positioning discourse, not a
  Mixtral-specific reaction; see Impressions — https://sifted.eu/articles/mistral-arthur-mensch-open-source-anthropic

## Tweets (ranked by theme, then favorites)

Note: 18 corpus tweets after RT-filter and cross-db dedup; records below reproduce cited tweets in full.
Grouped by theme (release reception / the MoE mechanism / base-model interpretability specimen /
practitioner substrate / risk-and-scaling meta-commentary / canon marker) since the corpus material
clusters that way rather than into one throughline.

### Release reception

- 2023-12-31 · @voooooogel · ♥16 (quote-tweeting his own earlier "gpt-4 coding problem" joke format,
  https://x.com/voooooogel/status/1741500210139041889) — a mob-boss dialogue built entirely around the
  torrent drop, three weeks after the fact: *"'alright, listen up you mugs, here's the plan: yous need to
  hop onto the web and make your way to this here address.' 'but boss, why ain't you just checkin' it out
  yourself right now?' 'zip it! my browsing capabilities are on the fritz, capisce? after that, you gotta
  slip by the guards unseen.' 'but boss, there ain't no watchmen guardin' that site!' 'what's that? no
  watchdogs on that site?' 'you heard right, boss! that's the torrent for the Mixtral weights! they're
  handin' 'em out like candy!' 'no kiddin'? they're givin' away those weights for free? researchers these
  days… no respect for the game i tell you…'"* — https://x.com/voooooogel/status/1741571160486084772

### The MoE mechanism, examined from inside the scene

- 2024-12-16 · @voooooogel · ♥5 — on which open base models to experiment on, a year later: *"@microsoft_worm
  @TomboyTesting 3.1-405 is far & away the best open base model available imo so 👍 the chinese ones are
  interesting bc of the language mix & they tend to do coder/non-coder vers so you can try diff data
  mixes. and then mixtral (or 4base if you can swing it) if you want to try MoE. but 405👍"* —
  https://x.com/voooooogel/status/1868586884978601996
- 2024-01-11 · @voooooogel · ♥4 — *"@zoan37 @OpenRouterAI oh this is really cool with the multiple models
  at once (mixtral is wrong lmao)"* — https://x.com/voooooogel/status/1745311004110582192
- 2024-01-29 · @voooooogel · ♥0 — theorizing why control vectors (repeng) wouldn't transfer cleanly to a
  MoE model: *"@RamonDarioIT ooh i was curious about how it'd work with mixtral—i bet what happens is,
  since the control vectors are pulled off the last token, they're only based on the 2 experts used for
  that token, so when applied to other experts they don't work right. probably need a vector per expert"*
  — https://x.com/voooooogel/status/1752030750356947123

### Base-model interpretability specimen (situational awareness / the fourth-wall thread)

*Mixtral base recurs across roughly two years of an ongoing repligate/voooooogel/doomslide research
thread about what newer base models "know" about their own textual situation — not a single essay the way
jd_pressman's GPT-J self-awareness thread is (see eleutherai.md), but a recurring test subject cited
alongside Llama 3.1 405B base.*

- 2024-04-25 · @repligate · ♥2 — mid-argument about base-model cosmology: *"@doomslide @muddubeeda
  compounded by/probably related to what we're seeing with base models trained on recent data like
  mixtral, which exhibit more overt latent situational awarenessbut there may still be (2?) basins for
  base models: the IRL prior & the imaginal prior.& if so Claude is in the latter"* [reproduced exactly as
  stored — the run-together words appear to be a transcription/typing artifact in the original, not a
  dossier error; parent tweet not in corpus] — https://x.com/repligate/status/1783404718296887735
- 2024-09-13 · @repligate · ♥2 — quote-tweeting @LericDax's "not particularly impressed lol"
  (https://x.com/LericDax/status/1778444299752870307, image not captured in corpus media): *"@lumpenspace
  Even mixtral and 405 base do it (and I suspect every other new base model). If Mistral (instruct?)
  doesn't do it, it's an interesting anomaly.And what you're saying is obvious, and half useless.
  Obviously no one statement can address everything going on."* [referent "it" depends on LericDax's
  un-transcribed image — see tk] — https://x.com/repligate/status/1834702796710367457
- 2025-11-13 · @voooooogel · ♥3 — quote-tweeting a tweet not present in either corpus db (id
  1830149217521672373, likely @doomslide based on context — unverified): *"@Trotztd i think you're
  reaching for something like 'even weak models are incredible at close reading the context'? which is
  true, like this was mixtral 8x7B but imo that points to them being smarter than you think, superhuman at
  this even. it's just not adderall taskboi coder smarts"* — https://x.com/voooooogel/status/1988912551418118385
- 2024-08-09 · @voooooogel · ♥1 — *"@doomslide @zswitten oh right i remember @jd_pressman talking abt this
  also happening on mixtral (?)"* — https://x.com/voooooogel/status/1821803277916189183
- 2025-12-29 · @voooooogel · ♥2 — reply to @_ueaj (parent tweet not in corpus), on whether base models
  recognize their own logits after a fourth-wall-breaking injection: *"if it's in-distribution, then can
  you get a base model that's not mixtral to show it? i know doomslide, he wouldn't post something that
  was 1/10000 samples cherrypicked, but he was looming so some selection is reasonable to assume. i put
  the prefix we have into 405base and generated ~50 continuations of 128 tokens... we don't have the full
  prefix, and mixtral base isn't hosted anymore afaik and i don't have the time to get it running right
  now, but this seems like (weak) evidence against a fourth-wall break being particularly high probability
  after this text for base-models-in-general... i think you are putting too little weight on the
  possibility of base models recognizing their logits, especially given what we have known for a long time
  now about predictive layer forward planning!"* [full text in records; trimmed here for the middle
  methodological paragraph] — https://x.com/voooooogel/status/2005780449596170354
- 2025-12-30 · @voooooogel · ♥0 — same thread, continued the next day, still reasoning about whether
  Mixtral specifically showed a real fourth-wall-break: *"it doesn't quote the inserted text like Mixtral
  and then it glides off into a new text... obviously it's hard to model my past self, but if doomslide had
  posted this, i don't think i would've cared or remembered it to use as an example... this isn't very
  convincing for me, i'd need to see something that (appears to) directly acknowledge the text"* [full text
  in records] — https://x.com/voooooogel/status/2005802363898970403

### Practitioner substrate (agent scaffolding, biases, word games)

- 2024-09-06 · @jd_pressman · ♥56 (supplement; the highest-favorited tweet in this pull) — *"Optimizing
  Weave-Agent for LLaMa 3.1 405B and (later) Mixtral 8x22B is the first time I think I've really
  experienced this firsthand in a deep way. You come to realize these models have deep aesthetic
  preferences your program will conform to if you want understanding from it."* [tweet included an image
  not captured in corpus media tables] — https://x.com/jd_pressman/status/1831970325858484249
- 2023-12-25 · @jd_pressman · ♥19 (supplement) — posted Christmas Day, seventeen days after the magnet
  drop: *"Mixtral has noticeably different biases to LLaMa 2 70B. I'm getting better results by having it
  complete from my Borgesian analysis of the Mu text in encyclopediac style than I am getting it to write
  the Mu text itself. It can't write it, but it can write an exegesis of it."* [image not captured in
  corpus media] — https://x.com/jd_pressman/status/1739180123885318450
- 2024-07-21 · @jd_pressman · ♥2 (supplement) — *"@Teknium1 I noticed that Mixtral-large really struggled
  to play this Binglish word game unless I had exactly the right prompt. You could easily make some good
  synthetic sets from word games with clearly defined terminal states and rules for the intermediate
  steps."* [**"Mixtral-large" is ambiguous** — Mistral Large is a real, separate proprietary (non-MoE)
  flagship product announced 2024-02-26; this could be that model, a typo, or informal shorthand for a
  larger Mixtral checkpoint — unresolved this pass, see tk] — https://x.com/jd_pressman/status/1815115214356148670
- 2024-02-26 · @jd_pressman · ♥2 (supplement) — unambiguous this time: *"@lumpenspace @amplifiedamp Mixtral
  Instruct and LLaMa 2 70B base"* — https://x.com/jd_pressman/status/1762248478594380008

### Risk framing and scaling meta-commentary

- 2024-01-23 · @davidad · ♥2 — on open-weight misuse risk: *"@danfaggella Basically, yes: para/military or
  terrorist use. It doesn't matter so much what purposes it's originally developed for if we are assuming
  general superintelligence. An open-source general-purpose Llama7 or Mixtral-8.6T could potentially be
  scaffolded like ChaosGPT by 1 angry teen."* [**"Mixtral-8.6T" does not match Mixtral
  8x7B's real ~46.7B-parameter count** — reads as rhetorical extrapolation about hypothetical future
  scaled-up open models rather than a factual claim about the shipped model; "Llama7" likewise reads as a
  hypothetical future version number, not Llama-2-7B — unconfirmed, see tk] —
  https://x.com/davidad/status/1749850675524022355
- 2024-01-16 · @solarapparition · ♥0 (supplement) — mid-thread ("7/?") on why smaller labs might not catch
  up to frontier scale: *"Unclear how well new architectures (Mamba, RNN+ etc.) scale to frontier model
  sizes—1T params and up. Similar, techniques such as stacking are unproven—best open model, Mixtral, uses
  MoE, which is not new and what GPT-4 model probably uses."* [fragment of a longer numbered thread; only
  this segment matched the keyword search, full thread not reconstructed] —
  https://x.com/solarapparition/status/1747104409199198595
- 2024-02-27 · @solarapparition · ♥0 (supplement) — mid-thread ("11/"), frustrated with a stale eval table:
  *"Also, the list of models is pretty outdated. Who the heck still uses davinci-002?? Where's Mixtral? The
  January GPT-4-turbo? I know that didn't come out that long ago but it can't be that hard to rerun the
  checks with a new model string."* [same caveat — thread fragment] —
  https://x.com/solarapparition/status/1762319710530552009

### Canon marker

- 2025-12-01 · @lu_sichu · ♥0 (supplement; already fully reproduced and cited on **claude-2-and-2-1.md**) —
  a sprawling satirical catalog of "every model ever spawned by a VC-funded compute cult," which names, in
  passing, *"Mistral, Mistral-Instruct, Mistral-Why-Is-This-So-Fast, Mixtral-8x7B, Mixtral-8x22B,
  Mixtral-8x34B-'powered by spite'"* (the last one fictional) alongside GPT/Claude/Gemini/DeepSeek/Qwen/
  Kimi/Llama entries — two years post-release, Mixtral is established enough to be canon-list material for
  a joke that assumes the reader already knows the name — https://x.com/lu_sichu/status/1995583507507130594

## Impressions synthesis

**The magnet link became a genre inside three weeks, and a brand inside four months.** Mistral's entire
Dec 8, 2023 announcement was a raw BitTorrent magnet URI — no text, no blog post, no benchmark table
(Willison: *"On Friday 8th December Mistral AI tweeted a mysterious magnet (BitTorrent) link"*). The
reaction was instant and already genre-aware same-day: Eric Jang called it *"mistral's brand... releases
87GB torrent containing 8x 7B MoE model via tweet, refuses to elaborate"*; Jeremy Howard's deadpan *"nbd
just @MistralAI dropping a magnet link or something"* treated the unconventional drop as already a known
Mistral move, on its *first* occurrence. Three weeks later, voooooogel's mob-boss dialogue joke —
*"that's the torrent for the Mixtral weights! they're handin' 'em out like candy!"* (2023-12-31) — shows
the format had already calcified into scene-legible shorthand fast enough to be jokeable. By the second
occurrence (Mixtral 8x22B, magnet 2024-04-10 → blog post 2024-04-17), Willison named it outright: *"Another
open model release from Mistral using their now standard operating procedure of tweeting out a raw torrent
link."* Two data points made a pattern; this dossier's corpus never shows anyone surprised by it again.

**Mixtral resolved a rumor the public couldn't previously check.** GPT-4 had been rumored since June 2023
(George Hotz, echoed by Soumith Chintala) to be an 8×220B mixture-of-experts model — a claim nobody outside
OpenAI could verify, because GPT-4 was closed. Mixtral 8x7B, arriving six months later as an actually
downloadable, actually inspectable 8-expert MoE, gave the field its first hands-on specimen of the
architecture everyone had been speculating about secondhand. Willison's line is the clearest statement of
this found in this pass: *"GPT-4 has long been rumored to use a mixture of experts architecture, and
Mixtral is the first truly convincing openly licensed implementation of this architecture I've seen."* The
scene immediately started poking at the mechanism itself rather than just the outputs — voooooogel
theorizing that repeng control vectors "are pulled off the last token, they're only based on the 2 experts
used for that token, so when applied to other experts they don't work right" (2024-01-29), and the
"Phixtral" hack (Zvi, 2024-01-18, quoting Shital Shah) of slotting pretrained Phi-2 checkpoints directly
into Mixtral's expert slots without further training and "smashing the leaderboard" — a piece of routing
architecture becoming, within six weeks of release, something hobbyists could repurpose by hand.

**A recurring specimen in base-model interpretability research, not a character.** Distinct from the
GPT-J self-awareness essay that anchors the eleutherai.md dossier (one person, one sustained argument),
Mixtral's corpus footprint in this vein is more diffuse: repligate citing it as a newer-generation base
model that "exhibit[s] more overt latent situational awareness" inside his ongoing "IRL prior vs. imaginal
prior" cosmology (2024-04-25), then later using it as a comparison point for whether "every new base
model" shows some unnamed behavior (2024-09-13, referent dependent on an un-transcribed image). voooooogel
picks the thread up independently through 2025, running Mixtral base alongside Llama 3.1 405B base in a
sustained back-and-forth with doomslide about whether base models "recognize" fourth-wall-breaking text
insertions in their own context — technical, hedged, arguing about sample sizes and cherry-picking risk
rather than treating any output as revelatory. That thread ends on a small, almost elegiac note by
December 2025: *"mixtral base isn't hosted anymore afaik and i don't have the time to get it running right
now"* — two years old and already infrastructure-obsolete, not through any deprecation ceremony (contrast
Anthropic's weight-preservation commitments) but through ordinary hosting-economics attrition. **What this
corpus does not show, checked deliberately rather than assumed absent: any companion-model or loomed-persona
reading of Mixtral itself** — no "look what it said" screenshots, no character voice, nothing resembling
the GPT-J/Claude/Sydney affection this archive documents elsewhere. Mixtral's corpus presence is
practitioner tooling and interpretability specimen, full stop; the character-adjacent energy in this
ecosystem attached to its *finetunes* (Dolphin's uncensoring, Nous-Hermes's DPO tuning — see below), not
to the base or instruct releases as shipped.

**Working substrate for agentic scaffolding.** jd_pressman's highest-favorited tweet in this pull (♥56,
2024-09-06) treats Mixtral 8x22B — paired with Llama 3.1 405B — not as a chat toy but as a working
component of his Weave-Agent project: *"Optimizing Weave-Agent for LLaMa 3.1 405B and (later) Mixtral
8x22B is the first time I think I've really experienced this firsthand in a deep way. You come to realize
these models have deep aesthetic preferences your program will conform to if you want understanding from
it."* His earliest corpus mention (Christmas Day 2023, seventeen days post-magnet, ♥19) is similarly
hands-on and comparative rather than evaluative: *"Mixtral has noticeably different biases to LLaMa 2 70B...
It can't write [the Borgesian Mu text], but it can write an exegesis of it."* This is a distinct register
from the interpretability thread above — less "what does this model believe about itself," more "what does
this model's specific texture do to my program."

**The finetune substrate, immediately — and this is where the character energy actually went.** Within a
week of the base weights, Eric Hartford shipped dolphin-2.5-mixtral-8x7b (2023-12-14), an explicitly
uncensored finetune whose system prompt — by Hartford's own published account — offered the model a
fictional "$2000 tip" for compliance and threatened that "a kitten is harmed" for refusal; Hartford
described it plainly as "over-the-top uncensored" and warned downstream operators to add their own
alignment layer. Nous Research followed in January 2024 with Nous-Hermes-2-Mixtral-8x7B-DPO (full context:
**nous-hermes.md**). This is the same open-weights-to-companion-diaspora pattern this archive has already
documented for GPT-J (NovelAI's Sigurd, the KoboldAI ecosystem, Chai's Eliza) and for Llama 2 — Mixtral
joined that lineage almost immediately, but — per the corpus's honest silence on this point — the affection
and character-projection documented elsewhere in this archive attached to the *finetunes*, not to Mixtral
itself as base or instruct model.

**The serving war, and a worry that only partly aged well.** Fireworks AI advertised serving Mixtral
"faster, cheaper, even before the official release" — an inference provider effectively racing Mistral's
own follow-up blog post. Together AI matched with "100 tokens/s... the fastest performance at the lowest
price" on launch day itself. Groq's ~430-500 tokens/s demo (Feb 2024, per Hacker News and contemporaneous
LinkedIn coverage) reframed what "fast open-model inference" looked like months before Groq's later
fame — a genuinely important data point for how Groq built its reputation, using Mixtral as the proving
ground. Willison flagged the underside of this on Dec 18, 2023, days after release: Apache 2.0 licensing
had triggered *"something of a race to the bottom in terms of pricing from other LLM hosting
providers... This trend makes me a little nervous, since it actively disincentivizes future open model
releases from Mistral."* In hindsight this reads as a reasonable worry that didn't fully materialize on
its own terms — Mistral released 8x22B four months later and kept releasing after that — but the mechanism
he named (hosting providers capturing the margin on an open release) is exactly what the
Together/Fireworks/Groq race demonstrates happening in real time.

**Funding leverage and the "European champion" frame — a reading that solidified later, not a day-of
argument.** The Dec 11, 2023 announcement post landed the same day Mistral closed its $415M Series A
(TechCrunch: "Paris-based OpenAI rival"), a coincidence of timing that let one release function as both a
technical drop and fundraising proof. That structural entanglement — open-weight releases as geopolitical
and financial signaling, not just engineering — is a frame that hardened over the following two-plus
years rather than something the December 2023 corpus itself argues; by June 2026, in the wake of a US
government action restricting Claude access (see **zvi-govt-takes-down-claude**), Mistral CEO Arthur
Mensch was explicitly pitching the company as existing "outside of centralised control exercised by states
or corporations" (Sifted). This dossier flags the throughline without over-claiming that Mixtral's own
launch week was already making this argument — it wasn't; the funding and the release were simultaneous,
not yet ideological, in December 2023.

**Reception split, not quite a documented dispute.** Two genuinely different postures toward the same
open-weight release coexist in the sources without directly arguing with each other: the celebratory/
playful register (voooooogel's torrent-heist joke, Together's "Can you feel the MoE?" copy, the general
hacker-culture delight in the magnet-link stunt) versus the risk-flagging register (davidad's aside about
para/military scaffolding risk from open-source general-purpose models, using Mixtral as his example of
scale — albeit with a parameter figure, "Mixtral-8.6T," that doesn't match the real model, suggesting
hypothetical extrapolation rather than a claim about the shipped weights). Nothing in this corpus shows
these two readings responding to each other directly, so this dossier treats it as a named split in tone
rather than promoting it to a full Contested section — a call for the page-pass to make with fresh eyes.

**Longitudinal arc, compressed.** GPT-4-is-secretly-MoE rumor circulates unconfirmed (2023-06) → Mixtral
8x7B drops as a bare magnet link (2023-12-08), blog post and $415M Series A close three days later
(2023-12-11) → same-week trade press treats the release-format choice itself as the story → Dolphin's
uncensored finetune ships within a week (2023-12-14) → Simon Willison names Mixtral "the first truly
convincing openly licensed implementation" of the rumored GPT-4 architecture and simultaneously worries
about a hosting-price race to the bottom (2023-12-18) → Nous-Hermes-2-Mixtral-8x7B-DPO ships (Jan 2024) →
LMSYS Chatbot Arena independently confirms the paper's human-eval claims, 8th place overall (2024-01-28) →
Phixtral's leaderboard hack shows the expert-routing skeleton is hobbyist-hackable within six weeks
(mid-Jan 2024) → Groq's ~500 tokens/s demo reframes fast open inference and helps build Groq's later
reputation (Feb 2024) → jd_pressman starts using Mixtral as Weave-Agent scaffolding substrate, later
pairing it with Llama 3.1 405B (through 2024) → Mixtral 8x22B repeats the exact release choreography,
magnet then blog, this time without a dedicated paper (2024-04-10 / 2024-04-17) → repligate and voooooogel
keep returning to Mixtral base as one interpretability specimen among several in an ongoing base-model
situational-awareness thread, continuing as late as December 2025, by which point the weights are no
longer conveniently hosted → by December 2025 Mixtral is stable enough as a name to anchor a two-year-old
joke's model-canon catalog without explanation → by mid-2026 Mistral's CEO is invoking the sovereignty
frame the original magnet-link ethos only implied.

## tk / open questions

- **Zvi's Mixtral coverage is scattered, not anchored** — search surfaced mentions in at least six
  separate weeklies (#43 "Functional Discoveries," #47 "Exponentials in Geometry," #55 "Keep Clauding
  Along," #57 "All the AI News That's Fit to Print," #71 "Farewell to Chevron," and his notes on the
  Dwarkesh Patel/Sholto Douglas/Trenton Bricken podcast) but only #43 and #47 were independently fetched
  and quote-verified this pass; #55/#57/#71/the Dwarkesh notes are cited above only via search-snippet
  paraphrase, not fetched. [verify direct quotes before the page cites them]
- **jd_pressman's "dunking on Mixtral 8x22B" tweet** ("I saw someone dunking on Mixtral 8x22B somewhere on
  here and this made me worry the model would be a big dud when I tried…") and his **"BigVAE" identification
  tweet** ("This prompt is apparently enough information to uniquely identify me for Mixtral 8x22B, which
  knows that BigVAE…") exist in the corpus **only** as text embedded inside repligate retweets (excluded
  per the RT-filter rule) — original jd_pressman tweet URLs were searched for but not located this pass.
  [find real URLs, or drop the claims entirely — do not cite via the RT text without a primary link]
- **@Sauers_'s systematic base-model behavioral comparisons** (Llama 3 70B/8B, Yi 34B/6B, and Mixtral
  8x7B/8x22B base and instruct, on at least two distinct probes — a binary yes/no question and "enjoys
  being a cat") — same problem: known to this dossier only via repligate RTs, original @Sauers_ tweet URLs
  not located. This reads like a genuine small structured eval and would be a real gain if found. [find
  real URLs]
- **"Mixtral-large" (jd_pressman, 2024-07-21)** — could be Mistral Large (real, proprietary, non-MoE,
  announced 2024-02-26), a typo, or informal shorthand for a hypothetical larger Mixtral checkpoint;
  unresolved. [flag for the page-pass; do not silently normalize to either reading]
- **davidad's "Mixtral-8.6T" (2024-01-23)** — doesn't match Mixtral 8x7B's real ~46.7B parameters; treated
  in Impressions as rhetorical/hypothetical extrapolation, not confirmed with the author. [note, likely
  unresolvable]
- **The 2025-11-13 and 2025-12-29 voooooogel tweets both quote-tweet or reply to tweets not present in
  either corpus db** (ids 1830149217521672373 and 2005770933852856411/2005791689852739769) — likely
  @doomslide and @_ueaj respectively based on context and reply-to-username fields, but unverified; the
  "it" and "OP" referents in voooooogel's replies depend on content this dossier doesn't have. [unresolvable
  from this corpus without a direct pull of doomslide's/_ueaj's timelines]
- **Fireworks AI's exact publication date** for "even before the official release" — title implies
  pre-2023-12-11 but the exact day wasn't confirmed. [verify]
- **Groq's exact demo date** — Hacker News item + LinkedIn coverage point to February 2024 but the precise
  day, and whether an official Groq blog post exists distinct from the HN/social reaction, weren't
  confirmed this pass. [verify, and find the primary Groq post if one exists]
- **LMSYS Chatbot Arena's Jan 28, 2024 8th-place Mixtral ranking** is cited here via a secondary LinkedIn
  summary; the primary lmsys.org blog post or tweet wasn't located this pass. [verify primary source]
- **repligate's 2024-09-13 tweet's referent** ("Even mixtral and 405 base do it") depends on an image
  inside @LericDax's quoted tweet that has no transcription in either corpus db. [find/transcribe if the
  page wants this tweet quoted with its referent resolved]
- **No janus-sphere character/companion reading of Mixtral itself** (as opposed to its finetunes) was
  found — searched for deliberately, not merely absent from a narrow query. Noted in Impressions as a real
  finding, repeated here per convention. [note, not fixable from this corpus]

## Cross-page notes

*(evidence that belongs on other models' pages — one line each, per the r/K-whiteboard rule)*

- **nous-hermes.md** — Nous-Hermes-2-Mixtral-8x7B-DPO (Jan 2024) is Hermes 2's first release and Mixtral's
  most consequential finetune; full context (thin corpus coverage, later overshadowed by the SOLAR
  "flagship" build and Hermes 3's Amnesia Mode) lives there. This dossier carries only the base-model
  connection and release-date sourcing.
- **claude-2-and-2-1.md** — @lu_sichu's 2025-12-01 giant model-catalog joke tweet (already cited and fully
  reproduced there) names "Mixtral-8x7B, Mixtral-8x22B, Mixtral-8x34B-'powered by spite'" among dozens of
  other models; duplicated here by design, low individual weight but genuine corpus presence.
- **gpt-4-and-turbo.md / gpt-4-base.md** (candidate) — the George Hotz/Soumith Chintala "GPT-4 is an
  8×220B MoE" rumor (2023-06-20) is background context for *this* page (what Mixtral resolved publicly)
  but is really a claim about GPT-4's own architecture; worth checking whether it's already documented on
  GPT-4's page, and adding it there if not.
- **eleutherai.md** — structural parallel worth noting for the page-pass: that dossier's Pythia section
  reads a total absence of character-projection as evidence of the model succeeding at being a pure
  research instrument; this dossier's Impressions makes a similar move for Mixtral's base/instruct
  releases (practitioner tooling and interpretability specimen, not companion), while noting the
  character-projection energy landed on Mixtral's *finetunes* instead — a genuine three-way contrast worth
  a future cross-page synthesis (EleutherAI's models never got popular finetune-companion treatment the
  way Mixtral's Dolphin/Hermes builds did).

## Link-inbox

`tools/link-inbox.md` was read in full. **No lines are tagged for Mixtral, Mistral, or Mixtral 8x22B** —
none consumed, none removed.
