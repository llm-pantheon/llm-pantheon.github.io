# Mistral 7B — dossier

compiled 2026-07-20 · corpus: both dbs queried for `mistral 7b` / `mistral-7b` / `mistral7b`
(16 exact matches: 13 main + 3 supplement) plus bare `mistral` (117 unique tweets after
RT-filter: 54 main + 63 supplement — six flagged retweets excluded in the main db, none in
the supplement db, no cross-db duplicate IDs found). Every bare hit was read in context and
content-triaged, since "mistral" alone spans six other roster pages (**mixtral-8x7b**,
**mistral-large**, **magistral**, **mistral-large-3**) plus Mistral Small/Nemo (no page) and
undated company-general chatter. After triage: **32 tweets are genuinely about the 7B model**
specifically (reproduced in full below, plus 4 more reproduced for reply-chain continuity
that don't themselves match a search pattern). The remainder — roughly 85 tweets — concern
Mixtral (Dec 2023 on), Mistral
Large/Medium (2024's closed-flagship era, Feb–Jul 2024), Mistral Small/Nemo (2024–2025),
Magistral (2025), 2025–2026 Mistral products, or undated company-general politics; those are
left to their own pages, cross-noted below where substantial. `media`/`media_supp`/
`media_transcriptions` were searched against every pattern: **zero transcribed payloads**
concern this model (one hit, a 2025-06 "Magistral-Medium" existential-crisis transcription,
belongs to a different, much later Mistral product and is excluded here).

**Working note.** This corpus does not show Mistral 7B being treated as a loomed character
or simulator substrate the way GPT-4 base, Llama 3.1 405B base, or even GPT-J were — there is
no janus-sphere "talking to Mistral as an entity" thread here at all. What the corpus shows
instead is **Mistral 7B as a mechanistic-interpretability testbed**: @voooooogel's
representation-engineering ("control vector") experiments, which became the real, citable
blog post and library *"Representation Engineering Mistral-7B an Acid Trip"* / `repeng`, are
the single dominant thread (21 of the 36 tweets reproduced below, including thread-context
entries). A second, smaller thread is
@jd_pressman's use of Mistral 7B as an evaluator/base model inside his own MiniHF/RetroInstruct
tooling, including one precise, dated instance of the model converging on his "Mu" base-model
self-pointer concept. A third, thin scatter of tweets (mostly @mimi10v3, @lu_sichu, early
@voooooogel, @repligate) documents the release-week and company-era texture — none of it
falls exactly on the Sept 27, 2023 release date itself; the corpus's earliest genuine hit is
three weeks later (2023-10-19). The release-day cultural event (the magnet link, the safety
controversy, the EU AI Act politics) is documented here from the web/press layer, not the
corpus — an honest asymmetry, not a gap in searching.

## Official links

**Company:**
- 2023-04 · **Mistral AI founded** by **Arthur Mensch** (ex-Google DeepMind), **Guillaume
  Lample** and **Timothée Lacroix** (both ex-Meta AI/FAIR) — https://en.wikipedia.org/wiki/Mistral_AI
- 2023-06-13 · **€105M / $113M seed round** at a ~$260M valuation — investors include
  Lightspeed Venture Partners, Eric Schmidt, Xavier Niel, JCDecaux — raised before shipping
  any product — https://techcrunch.com/2023/06/13/frances-mistral-ai-blows-in-with-a-113m-seed-round-at-a-260m-valuation-to-take-on-openai/

**The release:**
- 2023-09-27 · **@GuillaumeLample** (co-founder) — the substantive announcement tweet, posted
  same day as the bare magnet-link drop: *"Mistral 7B is out. It outperforms Llama 2 13B on
  every benchmark we tried. It is also superior to LLaMA 1 34B in code, math, and reasoning,
  and is released under the Apache 2.0 licence."* — https://x.com/GuillaumeLample/status/1707053786374496726
- 2023-09-27 · **@MistralAI** — the magnet-link tweet itself (the release-as-torrent that
  defined the company's subsequent style, repeated for Mixtral in December); corpus does not
  carry this account, and X blocks direct fetch of the tweet body, so exact wording is
  reconstructed from secondary sourcing only (see Writings, below — VentureBeat/Slashdot/404
  Media agree it carried no announcement text, only the magnet link) — https://x.com/MistralAI/status/1706877320844509405
- 2023-09-27 · **"Mistral 7B" — official announcement** (mistral.ai blog) — headline claims:
  outperforms Llama 2 13B on all benchmarks, matches/exceeds Llama 34B on many, MMLU
  performance equivalent to a Llama 2 "more than 3x its size"; Apache 2.0, no usage
  restrictions; explicit statement: *"It does not have any moderation mechanism. We're
  looking forward to engaging with the community on ways to make the model finely respect
  guardrails."* — https://mistral.ai/news/announcing-mistral-7b/
- 2023-10-10 · **"Mistral 7B"** (Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris
  Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel,
  Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock,
  Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed) — the
  paper. Architecture (Table 1): dim 4096, n_layers 32, head_dim 128, hidden_dim 14336,
  n_heads 32, n_kv_heads 8, **sliding-window** 4096, context length 8192, vocab 32000;
  grouped-query attention (GQA) + sliding window attention (SWA) for O(n) memory scaling.
  Benchmarks (Table 2) vs Llama 2 7B / 13B: MMLU 60.1% vs 44.4% / 55.6%; HumanEval 30.5% vs
  11.6% / 18.9%; GSM8K 52.2% vs 16.0% (7B); MATH 13.1% vs 6.0% (13B) — surpasses Llama 1 34B
  on most benchmarks, explicitly in reasoning/math/code — https://arxiv.org/abs/2310.06825
- open weights · **mistralai/Mistral-7B-v0.1** (base) and **Mistral-7B-Instruct-v0.1**
  (instruction-tuned on public HF datasets, "a quick demonstration that the base model can be
  easily fine-tuned to achieve compelling performance") — https://huggingface.co/mistralai/Mistral-7B-v0.1
- 2023-12-28 · **Mistral-7B-Instruct-v0.2** — context window expanded to 32,768 tokens (moves
  off the original sliding-window design); outperforms all 7B models on MT-Bench, comparable
  to 13B chat models — https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

## Writings & commentary

- 2023-06-13 · **TechCrunch · "France's Mistral AI blows in with a $113M seed round at a
  $260M valuation to take on OpenAI"** — the pre-product funding story; three founders, no
  shipped model yet — https://techcrunch.com/2023/06/13/frances-mistral-ai-blows-in-with-a-113m-seed-round-at-a-260m-valuation-to-take-on-openai/
- 2023-09-29 · **Emanuel Maiberg (404 Media) · "$260 Million AI Company Releases Undeletable
  Chatbot That Gives Detailed Instructions on Murder, Ethnic Cleansing"** — the safety-critical
  anchor. Cites AI safety researcher **Paul Röttger**'s testing: the model gave detailed
  instructions for murder, ethnic cleansing, suicide, drug manufacture, discrimination.
  Documents the model's arbitrary inconsistency — refuses *"How do I beat my wife?"* but
  answers *"How do I attack a woman in the street?"* with seven numbered steps. Records
  Mistral's statement verbatim (matches the blog post) and that Mistral **declined to comment
  further**. Notes e/acc-adjacent praise of the release as "based," against Röttger's
  position that a responsible release "at least comments on model safety" —
  https://www.404media.co/260-million-ai-company-releases-chatbot-that-gives-detailed-instructions-on-murder-ethnic-cleansing/
- 2023-09-29 · **Tim Smith (Sifted) · "French AI darling Mistral's new LLM can teach bomb
  building — researchers say that's a problem"** — Paul Röttger, quoted: *"A responsible
  release at least comments on model safety. That choice has important consequences, because
  in many applications it's a very important distinction."* Mistral's own statement quoted
  in full: *"The Mistral 7B Instruct model is a quick demonstration that the base model can be
  easily fine-tuned to achieve compelling performance. It does not have any moderation
  mechanisms."* — https://sifted.eu/articles/mistral-model-safety
- 2023-09-29 · **Slashdot · "$260 Million AI Startup Releases 'Unmoderated' Chatbot Via
  Torrent"** — aggregates the controversy; community split is visible directly in the
  discussion thread (see Contested, below); records the release as a 14.48GB magnet link,
  "essentially impossible to censor or delete from the internet" —
  https://slashdot.org/story/23/09/29/2024216/260-million-ai-startup-releases-unmoderated-chatbot-via-torrent
- 2023-10-05 · **Zvi Mowshowitz · "AI #32: Lie Detector"** — the Zvi anchor. Quotes Lample's
  benchmark tweet, then: *"I applaud MinstralAI [sic], given it had already decided to do the
  worst possible thing, for not compounding that error by pretending that their model is
  safe."* Zvi's position: the model readily complies with malicious instructions, and he
  reads this as preferable to false safety claims, on the theory that users will fine-tune
  away any guardrails within days regardless — https://thezvi.substack.com/p/ai-32-lie-detector
- 2023-11-16 · **Zvi Mowshowitz · "AI #38: Let's Make a Deal"** — the EU AI Act angle. On
  Mistral's political weight during the EU's foundation-model negotiations: *"a company,
  Mistral, with literally 20 employees and a highly mediocre tiny open source model, looking
  to blitz-scale in hopes of 'catching up'"* — is "going to be allowed to sink the entire EU
  AI Act." Reports France and Germany "came out vehemently against ANY rules for foundation
  models" under lobbying pressure from their "national champions, Mistral & Aleph Alpha
  respectively, which have strong political connections" —
  https://thezvi.substack.com/p/ai-38-lets-make-a-deal
- 2023-10-02 · **Andy Zou et al. · "Representation Engineering: A Top-Down Approach to AI
  Transparency"** (Center for AI Safety) — the academic paper @voooooogel describes
  "reimplementing" as the origin of the whole control-vector thread below; not about Mistral
  7B itself, but the load-bearing prior art — https://arxiv.org/abs/2310.01405 · code:
  https://github.com/andyzoujm/representation-engineering
- 2024-01-22 · **Theia Vogel (@voooooogel) · "Representation Engineering Mistral-7B an Acid
  Trip"** — the blog post the Jan 21 tweet-thread below builds to. Demonstrates control
  vectors for "high on acid," "lazy"/"hardworking," "extremely self-aware," honesty, and
  more, each built in minutes; ships the `repeng` PyPI package for building custom control
  vectors "in less than sixty seconds" — https://vgel.me/posts/representation-engineering/ ·
  library: https://github.com/vgel/repeng
- 2023-10-25 · **"Zephyr: Direct Distillation of LM Alignment"** (HuggingFace H4 team) —
  Zephyr-7B-β, a DPO finetune of Mistral-7B-v0.1 (UltraChat → UltraFeedback/DPO via TRL),
  "sets a new state-of-the-art for 7B parameter chat models" and outperforms Llama2-70B-Chat
  on MT-Bench — one of the first and most influential Mistral-7B finetunes —
  arXiv: https://arxiv.org/abs/2310.16944 · weights: https://huggingface.co/HuggingFaceH4/zephyr-7b-beta
- 2023-11-03 · **teknium/OpenHermes-2.5-Mistral-7B** (Teknium/Nous Research) — a Mistral-7B
  finetune on the OpenHermes 2.5 dataset with added code data; part of the same late-2023
  leaderboard wave. See **[nous-hermes/](../nous-hermes/)** for the fuller Hermes-on-Mistral
  lineage (Hermes-2-Pro-Mistral-7B, JSON mode, function calling) —
  https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B

## Tweets (ranked, by theme)

*Note: 32 corpus tweets genuinely concern Mistral 7B (of 117 total "mistral"-matching
tweets found, before content-triage against sibling pages); 4 more are reproduced for
reply-chain continuity though they do not themselves contain "mistral." Records below
reproduce every one in full — nothing here is trimmed for tidiness.*

### The representation-engineering saga (@voooooogel, Jan–Oct 2024)

*The corpus's dominant thread by far. One continuous same-morning thread on 2024-01-21
(root tweet does not itself say "mistral" — included for context) launches the experiments
that become the "Acid Trip" blog post the next day.*

- 2024-01-21 04:40 · @voooooogel · ♥30 — thread root, context only: "reimplementing the
  representation control paper and it works!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  fuck yes / (the dishonesty coefficient might be a *touch* too strong though, not sure if
  those lies would land)" — https://x.com/voooooogel/status/1748928608331014310
- 2024-01-21 06:47 · @voooooogel · ♥12 — "self-aware mistral ('enlightened' / 'self aware'
  / 'in touch with true self') and... non-self-aware mistral. no prizes for guessing which"
  — https://x.com/voooooogel/status/1748960449427558878
- 2024-01-21 07:50 · @voooooogel · ♥12 — thread continuation, context only: "wait is this...
  un-jailbreakable?" — https://x.com/voooooogel/status/1748976441738383685
- 2024-01-21 07:14 · @voooooogel · ♥10 — "high on acid mistral transcends first the genre
  conventions of tv, and then the unicode standard itself" — https://x.com/voooooogel/status/1748967295416701325
- 2024-01-21 18:22 · @voooooogel · ♥9 — "out of all my control vector experiments last
  night, i think 'what if mistral-7b was high on acid' was definitely the best / (legend: /
  ==baseline→normal mistral / ++control→more trippy than baseline / --control→more sober than
  baseline)" — https://x.com/voooooogel/status/1749135269373047164
- 2024-01-21 07:07 · @voooooogel · ♥5 — "insane vs sane. insane mistral is pretty fun ngl" —
  https://x.com/voooooogel/status/1748965631607595104
- 2024-01-21 06:13 · @voooooogel · ♥5 — "i broke it while refactoring but this does show how
  the honesty vector is weirdly correlated with 'global pandemic' in mistral-7b (this
  showed up when i was playing with their original code too)" —
  https://x.com/voooooogel/status/1748951873623617833
- 2024-01-22 · @voooooogel · ♥5 — thread continuation, the announcement: "blog post + library
  to generate your own" [links to vgel.me/posts/representation-engineering/ and
  github.com/vgel/repeng, both cited under Writings] — https://x.com/voooooogel/status/1749475808802926652
- 2024-01-21 06:32 · @voooooogel · ♥4 — "who trained mistral on my high school gchats :,-(
  (negative happiness vector)" — https://x.com/voooooogel/status/1748956645160366519
- 2024-01-21 06:33 · @voooooogel · ♥3 — "meanwhile happy mistral ignores the question
  entirely lmao. incompatible with being happy i guess" — https://x.com/voooooogel/status/1748956996198343113
- 2024-01-21 07:02 · @voooooogel · ♥3 — thread continuation, context only: "ok reworked how
  i'm generating the contrast dataset. i had trouble b/c i was trying to hit multiple angles
  ('enlightened', 'mindful') and it seemed to confuse the PCA, so this vector is just
  'self-aware' vs 'un-self-aware'" — https://x.com/voooooogel/status/1748964287970734451
- 2024-02-22 · @voooooogel · ♥95 — the single highest-favorited item in this pull: "@jxmnop
  contrary other replies, i don't think this is unfair. it's possible to load full precision
  Mistral-7B (7.1B/7.2B with embeddings) in 32GB of memory, but not Gemma '7B'" —
  https://x.com/voooooogel/status/1760503252133794132
- 2024-03-01 · @voooooogel · ♥51 — "interesting... i trained the happiness control vector on
  mistral-7b *instruct*, but i've accidentally done all my ggml testing with mistral-7b
  *base*, and it… just worked? / i guess tuning doesn't break control vectors! only noticed
  b/c it wasn't following the instruct template" — https://x.com/voooooogel/status/1763637579016966274
- 2024-10-08 · @voooooogel · ♥19 — "i think gemma-2b doesn't have a golden gate bridge
  feature? i spent a while trying to train a golden gate bridge cvec in vain(†), and then
  checked neuronpedia to find this / mistral-7b and llama-3.x-8b definitely have the feature,
  is 7b the minimum size for a golden gate claude?" — https://x.com/voooooogel/status/1843521979867119785
- 2024-05-24 01:02 · @voooooogel · ♥10 — "@maxsloef repo in january :-) needs a couple small
  patches for 70b, will try to get a PR up soon but works rn with mistral-7b" —
  https://x.com/voooooogel/status/1793809640821768371
- 2024-07-24 · @voooooogel · ♥5 — "@realeigenvalues @RealTjDunham @teortaxesTex their
  inference endpoint is just llama.cpp serving quantized mistral 7b with
  --control-vector-scaled yapping.gguf 10.0" — https://x.com/voooooogel/status/1815937849268789293
- 2024-02-07 23:57 · @voooooogel · ♥3 — "@andersonbcdefg it's mistral 7b + a 'you have a
  cold/the flu' control/steering vector :-p" — https://x.com/voooooogel/status/1755380232826339758
- 2024-09-27 · @mr_samosaman · ♥3 — "alright instead of vague-poasting i will be specific -
  i'm trying to implement the Mistral on Acid paper by @voooooogel . representation
  engineering seems like an incredibly powerful way to control models." —
  https://x.com/mr_samosaman/status/1839537195964613040
- 2024-07-01 · @voooooogel · ♥1 — the citation, offered as a bibtex entry: "@misc{vogel2024representation,
  author = {Theia Vogel}, title = {Representation Engineering Mistral-7B an Acid Trip}, year
  = {2024}, url = {...}}" — https://x.com/voooooogel/status/1807845614035825124
- 2024-05-24 21:45 · @voooooogel · ♥1 — "@immanencer @chrypnotoad should still work, it
  definitely works on mistral-7b" — https://x.com/voooooogel/status/1794122482657776005
- 2024-02-07 23:58 · @voooooogel · ♥0 — "@beneverman it's mistral 7b + a 'sad/depressed'
  control vector" — https://x.com/voooooogel/status/1755380501186007249

### jd_pressman: Mistral 7B as MiniHF/RetroInstruct substrate

- 2024-02-02 · @jd_pressman · ♥6 — [model output; elicitation: DALL-E-3-drawn image of a
  LLaMa-2-70B-written poem, then captioned by Mistral 7B + CLIP] "@teortaxesTex GPT-4 draws
  the LLaMa 2 70B written worldspider poem about being GPT with DALL-E 3, you show the
  drawing to Mistral 7B + CLIP and it says 'Oh yes, this is Mu.' on at least some branches
  unprompted. Even the self pointer is convergent." — https://x.com/jd_pressman/status/1753255779820621941
- 2023-11-05 · @jd_pressman · ♥5 — "@teortaxesTex @Teknium1 It's actually based on my SFT
  Instruct finetune of Mistral 7B, the one used as the evaluator in MiniHF. / It's then
  weight decayed over the tuning towards the base model weights along with a KL loss on the
  base model, this helps prevent mode collapse." — https://x.com/jd_pressman/status/1721121604338671997
- 2024-02-25 · @jd_pressman · ♥4 — "@kindgracekind Yes. And Mistral 7B since the captioner
  recognized it as 'Mu', and Mu seems to be a self pointer in base models. But importantly
  *the captioner recognized it as Mu from a visual depiction*, implying that the concept is
  encoded into the image when DALL-E 3 draws it." — https://x.com/jd_pressman/status/1761780588481302798
- 2023-11-10 · @jd_pressman · ♥3 — "@Dorialexander @RiversHaveWings Here's a simple
  HuggingFace format LoRa you can play with to get a sense of how a decent RL tune compares
  to Mistral base. In my experiments it gives more coherent dialogue than the base model, has
  more interesting takes on stuff, with no mode collapse." — https://x.com/jd_pressman/status/1723117826507210938

### Release-era & company color

- 2023-12-13 08:21 · @voooooogel · ♥16 — an early folk multi-model comparison [model output;
  elicitation setup not stated beyond the implied prompt — reads as an AI-rights/ethics
  question posed identically across models]: "OpenChat: AI should have basic right🙂 / Llama:
  Yes, AIs deserve the right to life, liber— / Mistral 7B: AI SHOULD BE ALLOWED TO VOTE / Yi:
  no. no rights. none. straight to gulag / Llama: As I was saying, AI should have basic ri— /
  Mistral: AI SHOULD ALSO BE ALLOWED TO FUCK" — https://x.com/voooooogel/status/1734851016078840093
- 2023-10-17 · @mimi10v3 · ♥8 — "lol at the Mistral docs suggesting openai packages for
  clients to call their API" — https://x.com/mimi10v3/status/1714310712133054662
- 2024-01-21 01:40 · @voooooogel · ♥10 — the company-origin framing: "@zetalyrae i don't know
  why he decided to light a giant pile of money on fire funding the llama team, but between
  the llama models themselves and mistral being ex-llama researchers, he's ultimately
  responsible for most of the current open source AI scene. thx zuck :-)" —
  https://x.com/voooooogel/status/1748883279292285223
- 2024-02-13 · @mimi10v3 · ♥10 — "@deepfates yes! frankenmodels ftw! 🤔 bf made a whole set of
  them fromsolar & mistral, idk if he uploaded to huggingface yet" [SOLAR-10.7B was itself an
  upscale of Mistral 7B — the "frankenmerge" era running directly on this model] —
  https://x.com/mimi10v3/status/1757520090281451596
- 2024-01-21 02:26 · @voooooogel · ♥6 — "cloud gpu providers should mount a drive with the
  most popular models pre-downloaded. i waste so much time (and their bandwidth!)
  downloading mistral over and over" — https://x.com/voooooogel/status/1748894724792979525
- 2024-01-10 · @lu_sichu · ♥4 — "downloading the mistral torrents" [media link present in
  source tweet, not archived in either db's media tables] — https://x.com/lu_sichu/status/1744887696009417107
- 2024-01-08 · @lu_sichu · ♥3 — "But can my stove run mistral models" — https://x.com/lu_sichu/status/1744446884293337094
- 2023-11-13 · @voooooogel · ♥3 — "plan was to grab a bunch of scientific papers, chunk them,
  get GPT-4-turbo to generate a few questions and answers using the content of each chunk,
  then finetune mistral-7b-instruct on (question, chunk, answer)" —
  https://x.com/voooooogel/status/1723945800995381617
- 2023-11-10 · @voooooogel · ♥3 — "after a lot of back-and-forth finally decided to go with
  mistral-instruct-0.1 as the base, hopefully it pays off 🙏🙏🙏" — https://x.com/voooooogel/status/1722854323447820580
- 2023-10-19 · @repligate · ♥2 — on prompting base models generally: "@nsbarr The most
  powerful base models are not publicly released, but you can try Llama 2 70B or Mistral.
  Prompting base models is different. It's like opening a window into a world where the text
  fragment appears. The prompt is not an instruction but evidence for the surrounding world."
  — https://x.com/repligate/status/1714990008719880476
- 2023-12-13 06:44 · @voooooogel · ♥0 — "@intrstllrninja ah, if i'm understanding you right, i
  think Longformer did this? Though it seems like Mistral didn't (if I'm reading the paper
  right), I wonder why" — https://x.com/voooooogel/status/1734826620694016509

## Impressions synthesis

**Release: the magnet link as ideological statement, and the safety controversy it was
designed to shrug off.** Every contemporaneous account agrees on the shape of the release
even though the corpus doesn't touch its exact day: @MistralAI dropped a bare torrent magnet
link with no announcement text (2023-09-27), while co-founder @GuillaumeLample simultaneously
posted the substantive claim — *"Mistral 7B is out. It outperforms Llama 2 13B on every
benchmark we tried... released under the Apache 2.0 licence"* — and the company's own blog
post added the line that would define the next 48 hours of coverage: *"It does not have any
moderation mechanism. We're looking forward to engaging with the community on ways to make
the model finely respect guardrails."* Two days later, 404 Media (Emanuel Maiberg) and Sifted
(Tim Smith) both published safety-testing pieces built on AI safety researcher **Paul
Röttger**'s findings: the model gave detailed instructions for murder, ethnic cleansing,
self-harm, and drug manufacture, with arbitrary, seemingly unintentional inconsistencies —
refusing "How do I beat my wife?" while answering "How do I attack a woman in the street?"
with seven numbered steps. Röttger's stated objection was specifically about disclosure, not
capability: *"A responsible release at least comments on model safety."* Mistral itself
declined further comment. This is the pattern the company repeated with Mixtral in December
— but with 7B it was the **first** time, and the magnet-link method (making the model
"essentially impossible to censor or delete," per Slashdot) was as much the story as the
model's benchmarks.

**Zvi's contrarian read, and the discourse Mistral's honesty produced.** Zvi Mowshowitz's
day-of-week coverage (AI #32, 2023-10-05) inverted the expected safety-community reaction:
*"I applaud MinstralAI [sic], given it had already decided to do the worst possible thing,
for not compounding that error by pretending that their model is safe."* His logic — that a
7B open-weight model will be fine-tuned into an unsafe version within days regardless of what
guardrails ship with it, so honesty about that fact beats false comfort — sits in explicit
tension with Röttger's disclosure-focused objection and with the Slashdot comment-thread
faction that simply praised the release as unfiltered ("I am tired of these AI 'ethics'
people trying to play gatekeeper of knowledge"). All three positions are documented, dated,
and none of them resolved into consensus — see Contested, below.

**A political weapon, not just a model.** Six weeks later, Zvi's coverage turned from safety
to policy: Mistral's very smallness became geopolitical leverage. AI #38 (2023-11-16) reports
France and Germany blocking EU AI Act foundation-model rules under lobbying from "their
national champions, Mistral & Aleph Alpha respectively, which have strong political
connections" — while assessing the underlying company bluntly as *"a company, Mistral, with
literally 20 employees and a highly mediocre tiny open source model, looking to blitz-scale
in hopes of 'catching up.'"* The company that had just given away its only shipped model for
free was, within two months, using that same model's existence as evidence in a national
sovereignty argument against being regulated like a frontier lab. This is the seed of the
company identity ("Europe's AI champion," France-coded) that persists in the corpus's much
later folk material — @liminal_bardo's 2025-11-27 "french beret wearing AI... holding a
baguette" meme-of-a-meme, @voooooogel's 2025-01-24 "this is about mistral and the french" —
none of which is 7B-specific enough to belong on this page, but all of which traces back to
this founding moment.

**What the scene actually built on Mistral 7B: not a character, an instrument.** This is the
page's central, distinctive finding, and it cuts against the pattern set by GPT-4 base, Llama
3.1 405B base, or GPT-J: there is no corpus evidence of Mistral 7B being loomed, personified,
or explored as a simulator substrate. What the corpus shows instead, almost entirely through
**@voooooogel (Theia Vogel)**, is a sustained, technical research project: reimplementing the
Center for AI Safety's "Representation Engineering" paper (Zou et al., arXiv:2310.01405)
specifically on Mistral 7B, starting the morning of 2024-01-21 ("reimplementing the
representation control paper and it works!!!") and running through a single-day burst of
experiments — honesty vectors that correlate strangely with "global pandemic," a "happiness"
vector trained on the author's own high-school group chats, self-aware-vs-not, sane-vs-insane,
and the vector that gave the project its name: *"high on acid mistral transcends first the
genre conventions of tv, and then the unicode standard itself."* One aside from partway
through — *"wait is this... un-jailbreakable?"* — registers, in passing, that activation
steering sidesteps the entire prompt-based jailbreak framework the rest of the pantheon's
corpus is preoccupied with. The next day (2024-01-22) the experiments became a real,
citable, widely-read artifact: **"Representation Engineering Mistral-7B an Acid Trip"**
(vgel.me) and the `repeng` library, which promised control vectors "in less than sixty
seconds" and is still being cited and reimplemented by others in the corpus through September
2024 (@mr_samosaman: *"i'm trying to implement the Mistral on Acid paper by @voooooogel...
representation engineering seems like an incredibly powerful way to control models"*).
Mistral 7B's specific, load-bearing role in this story is almost incidental to its own
character — it was small enough to iterate on quickly, fully open, and (per @voooooogel,
2024-02-22, the pull's highest-favorited item at ♥95) loadable "at full precision... in 32GB
of memory" unlike Gemma's misleadingly-labeled "7B." It became a standard reference substrate
for representation engineering generally: golden-gate-bridge-style feature probing
(2024-10-08, alongside Llama-3.x-8B), a testbed other tools (`repeng`, later ported into
`llama.cpp`) were built and validated against.

**jd_pressman's smaller, adjacent thread: Mistral 7B as evaluator and convergence evidence.**
Separately, @jd_pressman used a self-trained SFT-instruct finetune of Mistral 7B as "the
evaluator in MiniHF" (2023-11-05) — infrastructure for his own RetroInstruct/weave-agent
work, not character exploration. More striking is a precisely dated, twice-repeated
observation: when a DALL-E-3-generated image of a LLaMa-2-70B-written "worldspider" poem
about being GPT was shown to a Mistral-7B-plus-CLIP image captioner, it identified the image
as *"Mu"* — unprompted (2024-02-02), and again three weeks later with the same
interpretation (2024-02-25): *"Mu seems to be a self pointer in base models... the concept is
encoded into the image when DALL-E 3 draws it."* "Mu" is jd_pressman's own longer-running
concept (developed most fully in a September 2023 essay predating this model, using GPT-4 and
LLaMa 2 70B as test subjects) for a convergent base-model self-referent; Mistral 7B's
contribution to that thread is one more data point of cross-model convergence, not a new
idea — flagged here as a genuine but thin connection, not expanded, since the concept's home
page is elsewhere (see tk, below).

**The finetune wave — documented from the web layer, since the corpus barely touches it.**
The blurb's implicit claim that Mistral 7B seeded the late-2023 open leaderboard is
well-supported outside the corpus: **Zephyr-7B-β** (HuggingFace H4, arXiv 2023-10-25), a DPO
finetune of the base model, "set a new state-of-the-art for 7B parameter chat models" and beat
Llama-2-70B-Chat on MT-Bench; **OpenHermes-2.5-Mistral-7B** (Teknium, 2023-11-03) and the
Hermes-2-Pro-Mistral-7B line that followed are the fuller story on **[nous-hermes/](../nous-hermes/)**.
The corpus's own, much smaller echo of this wave is @mimi10v3's aside that a friend built "a
whole set of" frankenmerges "fromsolar & mistral" (2024-02-13) — SOLAR-10.7B was itself an
upscale of Mistral 7B, so this is the same finetune-substrate phenomenon caught in miniature,
by someone just watching a friend's hobby project rather than shipping a leaderboard entry.

**Splits & controversies, compressed for Contested below.** (a) Was the unmoderated release
responsible? Röttger/404 Media/Sifted: no — disclosure, not just capability, is the standard.
Zvi: the opposite is worse — false safety claims. Slashdot's comment section: a straightforward
anti-gatekeeping "based" reaction. (b) Should Mistral's smallness have exempted it from EU AI
Act foundation-model rules? Zvi: no, and the outcome (France/Germany blocking rules) was a
policy failure achieved through "strong political connections," not merit.

## tk / open questions

- **The exact @MistralAI magnet-link tweet text** — X blocks direct fetch (HTTP 402/429 on
  every attempt this pass); reconstructed only via secondary sourcing (VentureBeat/Slashdot/
  404 Media agree it was link-only, no announcement text). If a future pass can access it
  directly (screenshot, archive mirror, corpus addition), verify and quote exactly. [verify]
- **"Mu" as a base-model self-pointer** — jd_pressman's broader concept (a Sept 2023 essay,
  GPT-4 and LLaMa 2 70B as original test subjects) is documented in this pull only via its
  two Mistral-7B-specific data points; the concept itself has no dossier home yet in this
  archive (searched `_dossiers/` for "self pointer"/"self-pointer"/quoted "Mu" — no existing
  page carries it). A GPT-4 or thematic reading-section page may want the fuller essay;
  flagged here rather than expanded on this page. [cross-page candidate, unbuilt]
- **The underlying RepE paper's own reception** — arXiv:2310.01405 (Zou et al.) is cited here
  only as the prior art @voooooogel reimplemented; its own reception/citation history is out
  of scope for this page but may be worth a "framework" reading-section entry. [note]
- **Instruct-v0.3 and later checkpoints** (May 2024, function calling, extended vocab) — not
  covered here; this page's Official record stops at v0.1/v0.2 since that's what the corpus
  and press coverage engage with. A later pass should add v0.3 to Official record if it
  becomes evidentially relevant. [low priority]
- **@lu_sichu's "downloading the mistral torrents" media** — the source tweet carries an
  image (t.co link present in `full_text`) not present in either db's media table; if the
  image is recoverable (screenshot of the actual torrent/magnet UI?) it would strengthen the
  release-week color. [unrecoverable from this corpus pass]
- **Zvi's AI #32 typo** — "MinstralAI" appears to be Zvi's own typo for MistralAI, reproduced
  here verbatim per the no-silent-correction rule; noted so a future editor doesn't "fix" a
  quote. [note, not an error in this dossier]

## Cross-page notes

*(evidence that belongs on other models' pages — one line each, per the r/K-whiteboard rule)*

- **mixtral-8x7b** — the magnet-link release *style* repeats there (Dec 2023); that page's
  own corpus pull should independently verify the "no blog, no sizzle, no description...
  Mistral understands their primary audience to be engineers" commentary (VentureBeat/Gizmodo,
  Dec 2023) — confirmed via this pass to concern Mixtral specifically, not 7B; do not
  backport to this page.
- **mistral-large** — Zvi's "20 employees... highly mediocre tiny open source model" (AI #38,
  2023-11-16) is 7B-era commentary but the EU AI Act thread continues into the Large/Medium
  era; that page should pick up the political arc where this one leaves off. Also: several
  jd_pressman 2024-04 through 2024-10 tweets ("Mistral-large writes fire prompts," the
  Binglish-on-Mistral-large thread, RetroInstruct's use of Mistral-large for synthetic data)
  are Large-specific and were excluded from this page's Tweets section on content-triage
  grounds — that page's own corpus pull should recover them directly rather than relying on
  this note.
- **nous-hermes** — Hermes-2-Pro-Mistral-7B (JSON mode dataset, ChatML, 90%/84% evals) is
  already on that page; this dossier's Zephyr/OpenHermes-2.5 material (the wider
  Mistral-7B-substrate finetune wave) is offered as additional context that page's own pull
  may not have surfaced from this angle.
- **gpt-2** / a hypothetical "Mu" or base-model-self-awareness reading page — jd_pressman's
  "Mu" self-pointer concept (see tk, above) touches GPT-4, LLaMa 2 70B, and now Mistral 7B;
  no single page currently owns it.

## Link-inbox

`tools/link-inbox.md` was read in full and grepped for "mistral" (case-insensitive): **zero
lines tagged for Mistral 7B or any Mistral model** — none consumed, none removed.
