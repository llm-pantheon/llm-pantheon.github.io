# PaLM / PaLM 2 — dossier

compiled 2026-07-21 · corpus: **janus-corpus-v2** 60 raw `%palm%` hits, 19 raw `%minerva%` hits;
**supplement** 9 raw `%palm%`, 4 raw `%minerva%`. After RT-exclusion and noise-filtering (see hazard
below), the *real* signal is **~8 substantive tweets total** across both dbs — this is a genuinely
thin page by corpus standards, thinner even than LaMDA or Bard. `med-palm`, `medpalm`, `palm-e`, and
`flan-palm` return **zero** hits in either db.

**Corpus hazard, flagged up front (read before trusting any raw count).** "palm" is one of the
noisiest possible search strings in a corpus this size: it's a body part ("palm of my hand"), a tree,
a place name (Palm Springs/Beach), a common surname fragment (`@BeijingPalmer`, `jaredpalmer`), a verb
("facepalm," "I facepalm every time"), a t.co URL slug that happens to contain the substring
(`LWpalmsTvt`), and — largest single source in this pull — a word that turns up *inside enormous
Lari_island/Fable AI-worldbuilding fiction posts* purely because a character in the story touches
something with their palm. Of the 60 raw v2 hits, **40 were pure noise** (fiction, hand/tree/name
collisions) and 6 were retweets; only **14 survived filtering**, and several of those still needed
individual judgment calls (e.g. `LWpalmsTvt` is a URL slug, not a PaLM mention, and was cut on
inspection despite matching a keyword filter). Likewise `%minerva%` (19+4 raw) is **entirely**
**`@BlancheMinerva`** (Stella Biderman/EleutherAI's handle) — **zero** hits are about the Minerva math
model. This dossier reports the filtered, judgment-checked set, not the raw count.

**Working note — why the corpus is thin (unlike LaMDA, this isn't a flashpoint story).** PaLM (Apr
2022) never had a Lemoine-style sentience controversy or a Sydney-style unhinged-persona moment to
pull the janus-sphere's attention — it was announced, benchmarked, argued over as *numbers*, and kept
almost entirely internal until the March 2023 API. Its most-discussed properties (540B parameters,
chain-of-thought reasoning, the joke-explanation demo) were argued over in **ML-research and
scaling-debate Twitter** (Jason Wei, the emergent-abilities dispute, LessWrong's replication culture)
rather than the persona/character discourse this archive otherwise specializes in. So: **the paper and
the press carry this page; the corpus supplies only texture** — mostly davidad doing real-time
scaling-era reasoning, plus one good multi-model cross-reference already living on `claude-1.md`.
Sourcing skew, stated plainly: this is the most press-and-paper-dependent, least tweet-dependent
dossier in the Google lineage so far.

**Editorial flag for the page pass (parallel to the LaMDA precedent).** The existing stub
(`palm/index.html`) reads essay-meta "Google DeepMind · 2022–2023." This is only accurate for the
*tail* of the window: Google Brain and DeepMind merged into **Google DeepMind on 2023-04-20**
(`blog.google/technology/ai/april-ai-update/`). PaLM (Apr 2022), Minerva (Jun 2022), Med-PaLM (Dec
2022 paper), PaLM-E (Mar 2023), and the PaLM API (Mar 2023) all predate the merger and belong to
**Google Research** (Med-PaLM's author list already mixed in DeepMind researchers as a cross-org
collaboration, per Wikipedia, but the *org* was still separate). Only **PaLM 2** (announced 2023-05-10,
three weeks after the merger) is correctly attributed to Google DeepMind. The page pass should
probably read something like "Google Research (→ Google DeepMind from 2023-04-20) · 2022–2023," the
same fix LaMDA's dossier flagged for its own stub.

---

# ACT ONE: PaLM (Google Research, announced 2022-04-04)

## Official links

- 2022-04-04 · **"Pathways Language Model (PaLM): Scaling to 540 Billion Parameters for Breakthrough
  Performance"** — Google Research Blog, Sharan Narang & Aakanksha Chowdhery. The announcement: PaLM is
  a **540-billion-parameter dense decoder-only Transformer**, trained with the **Pathways** system
  across **two Cloud TPU v4 Pods (6,144 chips total)**, achieving **57.8% hardware FLOPs
  utilization** — "the highest yet achieved for LLMs at this scale." Training data: 780 billion tokens
  of "high-quality web documents, books, Wikipedia, conversations, and GitHub code," English and
  multilingual, with a custom lossless vocabulary that tokenizes digits individually and preserves
  whitespace (relevant to code and math). Beat prior-SOTA on **28 of 29** English NLP tasks tested;
  on BIG-bench (150+ tasks) PaLM's few-shot performance exceeded the human-rater average. Two smaller
  versions (8B, 62B) were trained alongside the 540B flagship for scaling comparisons. — https://research.google/blog/pathways-language-model-palm-scaling-to-540-billion-parameters-for-breakthrough-performance/
- 2022-04-05 · **arXiv paper** · "PaLM: Scaling Language Modeling with Pathways" — Aakanksha
  Chowdhery + 66 other authors (67 total), submitted 2022-04-05, 16:11 UTC. — https://arxiv.org/abs/2204.02311
  **[mirror-target candidate]**
- **Reasoning demo, verbatim (paper/blog-curated, 2-shot prompted — mark as such):** the blog's
  chain-of-thought section shows PaLM solving **58% of GSM8K** with 8-shot CoT prompting (vs. the
  prior top score of 55%, held by a fine-tuned GPT-3 175B using an external calculator/verifier and a
  7,500-problem training set) — https://github.com/openai/grade-school-math.
- **The joke-explanation demo, reproduced in full (elicitation: 2-shot prompt, Google-curated for the
  announcement post — the paper's own device, not a spontaneous output).** Retrieved directly from
  the blog's embedded image (`image5.png`) since the text is not machine-readable HTML on the page
  itself — transcribed here verbatim:
  > **Prompt:** "Explain this joke: Joke: Did you see that Google just hired an eloquent whale for
  > their TPU team? It showed them how to communicate between two different pods!"
  >
  > **PaLM's response:** "Prediction: TPUs are a type of computer chip that Google uses for deep
  > learning. A "pod" is a group of TPUs. A "pod" is also a group of whales. The joke is that the
  > whale is able to communicate between two groups of whales, but the speaker is pretending that
  > the whale is able to communicate between two groups of TPUs."

  The blog's own framing: "it can provide high quality explanations for novel jokes not found on the
  web" — a claim about generalization, not memorization. This is the single most-reproduced PaLM
  exhibit in tech press (the-decoder, Infobae, TheNextWeb all lead with it) and the natural "model's
  own voice" record for this page.
- 2022-06-30 · **"Minerva: Solving Quantitative Reasoning Problems with Language Models"** — Google
  Research Blog, Ethan Dyer & Guy Gur-Ari (Blueshift Team). Minerva "builds on the Pathways Language
  Model (PaLM), with further training on a 118GB dataset of scientific papers from the arXiv preprint
  server and web pages that contain mathematical expressions," combining few-shot prompting,
  chain-of-thought/scratchpad prompting, and majority voting. Benchmarks (vs. prior SOTA): **MATH
  50.3%** (vs. 6.9%); **MMLU-STEM 75%** (vs. 55%); **GSM8K 78.5%** (vs. 74.4%); **OCWCourses 30.8%**
  (no prior comparable score cited). Stated limitation: "the model's answers cannot be automatically
  verified" — it can reach a correct final answer via incorrect reasoning steps, undetectably. —
  https://research.google/blog/minerva-solving-quantitative-reasoning-problems-with-language-models/
  **[mirror-target candidate]**
- 2022-12-26 · **arXiv paper** · "Large Language Models Encode Clinical Knowledge" (introduces
  **Med-PaLM**) — Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. (30 authors, Google + DeepMind).
  Introduces the **MultiMedQA** benchmark (six QA datasets) and **Flan-PaLM**, which scores **67.6%**
  on MedQA (US Medical Licensing Exam-style questions), ">17%" over the prior SOTA. Med-PaLM itself
  (via "instruction prompt tuning," a parameter-efficient alignment method) narrows the gap on
  human-evaluated axes but the authors are explicit: Med-PaLM "remains inferior to clinicians," with
  "important limitations of today's models" on the harder, open-ended criteria. — https://arxiv.org/abs/2212.13138
- 2023-03-06 · **arXiv paper** · "PaLM-E: An Embodied Multimodal Language Model" — Danny Driess, Fei
  Xia, Mehdi S. M. Sajjadi, Corey Lynch, et al. (22 authors). **PaLM-E-562B**, the largest
  instantiation, fuses PaLM-540B with the ViT-22B vision transformer, directly ingesting raw robot
  sensor streams into the language model rather than pre-processing them into text. — https://arxiv.org/abs/2303.03378
- 2023-03-10 · **"PaLM-E: An Embodied Multimodal Language Model"** — Google Research Blog, Danny
  Driess (student researcher) & Pete Florence (research scientist, Robotics at Google). Demos: a
  household robot retrieves a chip bag from a drawer on a natural-language request and adapts when the
  bag is moved; the same model executes multi-step tabletop tasks ("sort the blocks by colors into
  corners") and generalizes to unseen objects. Achieves SOTA on the OK-VQA visual-QA benchmark while
  retaining general language ability — framed as evidence of "positive transfer" between vision,
  language, and robotics. — https://research.google/blog/palm-e-an-embodied-multimodal-language-model/
  **[mirror-target candidate]**
- 2023-03-14 · **"Announcing PaLM API and MakerSuite"** — Google Developers Blog. PaLM's first
  external access point, ~11 months after the paper: "a simple entry point for Google's large language
  models." MakerSuite offered prompt iteration, synthetic-data augmentation, and parameter-efficient
  model tuning. Access was gated: "We'll be making these tools available to select developers through
  a Private Preview, and stay tuned for our waitlist soon" — not an open launch. — https://developers.googleblog.com/2023/03/announcing-palm-api-and-makersuite.html
- 2023-03-14 · **Med-PaLM 2 update** — Google Health / "The Check Up," blog.google. Same day as the
  PaLM API announcement (and the same week OpenAI launched GPT-4, 2023-03-14). Reports Med-PaLM 2
  "consistently performed at an 'expert' doctor level on medical exam questions, scoring 85%" — an
  18-point jump over the original Med-PaLM's 67.6%. Caveat, stated by Google itself: models "were
  tested against 14 criteria — including scientific factuality, precision, medical consensus,
  reasoning, bias and harm," and evaluation revealed "significant gaps when it comes to answering
  medical questions and meeting our product excellence standards." — https://blog.google/technology/health/ai-llm-medpalm-research-thecheckup/
- context · **Google DeepMind formed 2023-04-20** (Brain + DeepMind merger announced) — the boundary
  line for the attribution flag above. — https://blog.google/technology/ai/april-ai-update/
- note · **AudioPaLM** (speech-to-speech translation, built on the PaLM 2 architecture, announced June
  2023) exists as a further branch not covered in depth here — flagged as a real gap, see tk.

## Writings & commentary

- 2022-04-05 · **the-decoder** (Matthias Bastian) · "Google PaLM: Giant language AI can explain jokes"
  — contemporary, uncritical coverage of the joke demo as one of several "breakthrough capabilities."
  — https://the-decoder.com/google-palm-giant-language-ai-can-explain-jokes/
- 2022-04-06 · **LessWrong** (Yitz) · "Testing PaLM prompts on GPT-3" — **the fastest skeptical
  replication check in this dossier: two days after the announcement.** The author ran PaLM's own
  showcased exemplars (joke explanation, "inference chaining") on GPT-3 via Playground defaults,
  committing in advance to report the first result regardless of quality (no cherry-picking).
  Finding, per commenter gjm quoted in the post: "GPT-3 does better than I expected on the jokes,
  but…much, much worse than PaLM on the 'inference chaining' examples, where GPT-3 basically gets
  everything completely wrong." Read together with the joke demo above: an early, methodologically
  serious "is this actually new or just clever prompting" check, of exactly the kind this archive
  values — and it comes down mostly in PaLM's favor on the harder task. — https://www.lesswrong.com/posts/EHbJ69JDs4suovpLw/testing-palm-prompts-on-gpt3
- 2022-06-15 (v1) · **arXiv** · Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph,
  Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, Ed H. Chi, Tatsunori
  Hashimoto, Oriol Vinyals, Percy Liang, Jeff Dean, William Fedus · **"Emergent Abilities of Large
  Language Models."** Abstract verbatim: *"We consider an ability to be emergent if it is not present
  in smaller models but is present in larger models. Thus, emergent abilities cannot be predicted
  simply by extrapolating the performance of smaller models."* PaLM (8B/62B/540B) is one of the
  paper's central evidence families — per Jason Wei's own retrospective (below), dozens of BIG-bench
  tasks (auto-debugging, logic-grid puzzles, metaphor understanding) emerge between 8B and 62B, and a
  further ~25 tasks (code-line description, elementary math QA, physics questions, the Word-in-Context
  benchmark) emerge only at 540B. — https://arxiv.org/abs/2206.07682 **[mirror-target candidate]**
- undated (retrospective) · **Jason Wei**, personal blog · "137 emergent abilities of large language
  models" — the paper's first author, in his own words: *"the existence of emergent abilities implies
  that scaling further would unlock even more emergent abilities. This idea is super exciting to
  me."* Catalogues 100+ emergent abilities across GPT-3, Chinchilla, and PaLM. — https://www.jasonwei.net/blog/emergence
- 2022-12-21 · **New York Times** (Nico Grant & Cade Metz) · **"ChatGPT and Other Chat Bots Are a
  'Code Red' for Google Search"** — resolves the tk left open in `bard-and-gemini-1-0.md`. The
  backdrop against which PaLM's internal-only, no-shipped-product year (Apr 2022 → Mar 2023 API) reads
  as a real cost: Google had trained a 540B model eight months before ChatGPT existed and still had no
  public chat product when the "code red" was called. — https://www.nytimes.com/2022/12/21/technology/ai-chatgpt-google-search.html
- 2023-04-28 (submitted), rev. 2023-05-22 · **arXiv** · Rylan Schaeffer, Brando Miranda, Sanmi Koyejo
  · **"Are Emergent Abilities of Large Language Models a Mirage?"** — the direct rebuttal to Wei et
  al. Abstract verbatim: *"nonlinear or discontinuous metrics produce apparent emergent abilities,
  whereas linear or continuous metrics produce smooth, continuous predictable changes in model
  performance."* The argument: emergence is an artifact of the researcher's choice of *metric*, not a
  discontinuity in the underlying model. Both sides of this dispute are load-bearing for how PaLM's
  own showcased jumps (the 540B-only BIG-bench tasks, above) should be read — see Contested. — https://arxiv.org/abs/2304.15004 **[mirror-target candidate]**

---

# ACT TWO: PaLM 2 (Google DeepMind, announced 2023-05-10)

## Official links

- 2023-05-10 · **"Introducing PaLM 2"** — Google (I/O 2023 announcement). Verbatim capability claims:
  improved ability to "understand, generate and translate nuanced text — including idioms, poems and
  riddles" (multilinguality); "improved capabilities in logic, common sense reasoning, and
  mathematics" (reasoning); "excels at popular programming languages like Python and JavaScript, but
  can also generate specialized code." Four sizes, in ascending order: **Gecko** (small enough to run
  on-device, including offline), **Otter**, **Bison**, **Unicorn**. Bard connection, stated directly:
  the multilingual improvements are "allowing us to expand Bard to new languages, starting today.
  Plus, it's powering our recently announced coding update" (cross-ref `../bard/` — substrate switch
  from LaMDA to PaLM 2, do not duplicate the Bard-side narrative here). — https://blog.google/technology/ai/google-palm-2-ai-large-language-model/
- 2023-05-17 (v1; last revised 2023-09-13, v3) · **arXiv** · **"PaLM 2 Technical Report"** — Rohan
  Anil, Andrew M. Dai, et al. (128 authors). Abstract verbatim: *"We introduce PaLM 2, a new
  state-of-the-art language model that has better multilingual and reasoning capabilities and is more
  compute-efficient than its predecessor PaLM… while simultaneously exhibiting faster and more
  efficient inference compared to PaLM."* Trained with "a mixture of objectives" (not the single
  causal-LM objective PaLM used). — https://arxiv.org/abs/2305.10403 **[mirror-target candidate]**
- **Additional PaLM 2 products named at/around I/O** (per TechCrunch, below): **Codey** (coding),
  **Sec-PaLM** (security), and **Med-PaLM 2** (medical, see Act One's 2023-03-14 entry for its first
  85%-score reveal — I/O reiterated the connection to PaLM 2).
- 2024-08-15 (reported shutdown date) · **PaLM API deprecated / free tier shut down**, migrated to the
  Gemini API. **REPORTED via trade press** — the primary Google deprecations page
  (`ai.google.dev/gemini-api/docs/deprecations`, checked 2026-07-21) no longer lists PaLM-era models at
  all (expected for an 18-month-old sunset; not itself evidence against the date). Secondary sourcing:
  a codewords.ai migration-guide post and other trade coverage giving 2024-08-15 as the date free
  PaLM API access closed, directing developers to the Gemini API. `note`: this dossier could not
  independently fetch a Google-primary post confirming the exact date (several candidate press URLs
  403'd on direct fetch); treat the date as REPORTED pending a cleaner primary. [verify]
- succession · **PaLM 2 → Gemini, 2023-12-06** — cross-ref `../bard-and-gemini-1-0.md` (Part 2) and
  `../gemini-1-0/`; do not duplicate the Gemini launch narrative here. The relevant PaLM-side fact:
  Gemini Pro replaced PaLM 2 inside Bard at launch, and "Bard Advanced"/Gemini Advanced (Ultra 1.0)
  followed at the Feb 2024 rename.

## Writings & commentary

- 2023-05-10 · **TechCrunch** (Frederic Lardinois) · "Google launches PaLM 2, its next-gen large
  language model." The load-bearing quote on the parameter-count question, from **DeepMind VP Zoubin
  Ghahramani**: *"Parameter count is not really a useful way of thinking about the capabilities of
  models."* — Google's own non-denial-non-confirmation on why PaLM 2's size wasn't headlined the way
  PaLM's 540B was. Also confirms the Gecko/Otter/Bison/Unicorn names and lists **Codey**, **Med-PaLM
  2**, and **Sec-PaLM** as products built on PaLM 2, plus a smartphone-scale variant processing "20
  tokens per second." — https://techcrunch.com/2023/05/10/google-launches-palm-2-its-next-gen-large-language-model/
- 2023-05-10 · **TechCrunch** (Kyle Wiggers) · "Google's PaLM 2 paper shows that text-generating AI
  still has a long way to go." **The skeptical-reception anchor, same day as launch.** Verbatim
  framing: "far from a panacea." Reports from the technical report's own safety evaluations: explicit
  toxic prompts elicited toxic completions "over 30% of the time"; implicit-harm prompts, "60%"; a
  bias probe on racial/religious identities showed a "17.9%" toxic-response rate; on one open-ended
  evaluation, "38.2%" of incorrect answers "reinforced a harmful social bias." Notes the transparency
  regression directly: the report withholds the flagship model's parameter count (though it does
  disclose "14.7 billion" for a smaller variant) and full training-hardware specifics, unlike PaLM's
  original paper. Also records Google's own comparative claim, presented without independent
  verification: PaLM 2 "even bests OpenAI's GPT-4, depending on the task at hand." — https://techcrunch.com/2023/05/10/googles-palm-2-paper-shows-that-text-generating-ai-still-has-a-long-way-to-go/
- 2023-05-16 · **CNBC** · "Google's PaLM 2 uses nearly five times more text data than predecessor" —
  **the parameter-count leak.** Reports, via "internal documents," that PaLM 2 was trained on **340
  billion parameters** and **3.6 trillion tokens** (vs. PaLM's disclosed 540B/780B) — smaller model,
  much more data, consistent with Chinchilla-optimal scaling logic. `note` on sourcing method: this
  dossier's direct fetch of the CNBC article was blocked (HTTP 403); the claim above is corroborated
  by two independent secondary aggregations (Techmeme, 2023-05-17, `techmeme.com/230517/p8`: "Google
  trained PaLM 2 on 3.6T tokens and 340B parameters, compared to 780B tokens and 540B parameters for
  the original PaLM"; and a Hindu BusinessLine explainer citing the same CNBC reporting) rather than a
  direct read of the primary. — https://www.cnbc.com/2023/05/16/googles-palm-2-uses-nearly-five-times-more-text-data-than-predecessor.html
  **REPORTED, not Google-confirmed — see Contested.**
- 2023-08-31 · **Zvi Mowshowitz** · "AI #27: Portents of Gemini" — **no dedicated PaLM/PaLM 2 anchor
  exists in Zvi's coverage** (searched directly; confirmed absent — consistent with the recipe's own
  expectation that "PaLM-1 predates the column"). This is the closest dated Zvi commentary on the
  mood around Google's models in the PaLM-2-to-Gemini interval, three-plus months after PaLM 2
  shipped: *"Bard still sucks"*; *"Google has been taking its sweet time getting its act
  together."* Written anticipating Gemini ("substantially superior to GPT-4," expected Dec 2023) as
  the moment Google's models would finally catch up — an implicit verdict that PaLM 2 hadn't. — https://thezvi.substack.com/p/ai-27-portents-of-gemini

---

## Tweets (ranked)

*note — corpus match count above; after filtering the extensive hand/tree/URL-slug/fiction noise
(see hazard note), the following is the complete substantive set from both dbs. Records below
reproduce everything in full; nothing character-bearing was cut. The largest single item
(♥193, already cited on `claude-1.md`) is multi-model evidence and duplicates here by the
r/K-whiteboard rule.*

- 2023-05-19 · @davidad · ♥193 ↻31 — **the "frontier tier" placement, 9 days after PaLM 2 shipped**
  (also on `../claude-1/`, the "Claude-Next" tweet): "I fully agree. Roughly, this threshold should be
  when any single number has more than 10²⁴ ALU operations, or 10²⁷ logic gates, in its entire causal
  history. GPT-3, AlphaFold 2, Stable Diffusion, LLaMa, Dromedary: below the line. GPT-4, PaLM 2,
  Claude-Next: over the line." — https://x.com/davidad/status/1659455017307324418
- 2022-06-20 · @davidad · ♥0 — reply to Gary Marcus and @GoogleAI, PaLM lumped with its 2022
  contemporaries: "yes, this is the right perspective—artistic models cannot be evaluated rigorously.
  i think the argument you should be making is that *all* models in the current hype cycle (incl GPT,
  PaLM, LaMDA, &c) are essentially artistic—they just make stuff up. doesn't make them bad artists." — https://x.com/davidad/status/1538674254589353984
- 2022-05-01 · @davidad · ♥2 — the earliest corpus mention, three-and-a-half weeks after launch, reply
  to @bayeslord (parent tweet not in corpus, task under discussion not recoverable): "Yes, with
  minimal prompting. I would be very surprised if GPT-3 can do this reliably even with arbitrary
  prompting. I'd also be surprised if PaLM can do it even with clever prompting, unless the prompt
  basically encodes an entire description of the machine, in which case maybe." — https://x.com/davidad/status/1520814509622968322
- 2023-12-06 · @davidad · ♥1 — **dated exactly to Gemini's launch day**, reply to @k3nnethfrancis:
  "just to be clear, you don't have any reason to believe this is Gemini, right? it's just PaLM 2?" —
  a small, precise artifact of the succession moment's confusion: is the thing being discussed the
  new model, or still the old one? — https://x.com/davidad/status/1732488975632245152
- 2023-01-31 · @repligate · ♥2 — reply to @akbirthko/@tszzl, on whether a task is beyond current
  models: "Yeah my intuition is that it's a little beyond the current gpt-3.5 family. Although I could
  see a model fine tuned on math with improved tokenization like Palm being able to do this." — https://x.com/repligate/status/1620322392387231744
- 2024-04-05 · @jpohhhh · ♥11 — reply to a repligate thread about getting Claude 3 Opus to simulate a
  good base model (parent tweet id 1776041976653402508, ♥105, not itself about PaLM): "This is
  amazing lol, literally perfect pitch copy of having PaLM access back when no one cared." **Thin,
  tangential evidence** — the substance is about Claude 3 Opus's base-model simulation, and PaLM
  surfaces only as a nostalgic reference point, but the line is a genuine, dated data point for "PaLM
  API access used to be a low-stakes, low-interest credential" — a small corroboration of the
  internal-only/no-product arc. — https://x.com/jpohhhh/status/1776051999961760141
- 2023-03-15 · @davidad · ♥1 — a joke about a hypothetical 2025 Android app: "2025: 'Please note, this
  APK contains a custom fine-tuned 540B Chinchilla, which may result in additional data charges if
  downloaded on 6G.'" — PaLM's headline 540B number already reads as a dated, oversized punchline
  less than a year after launch (this tweet predates PaLM 2's undisclosed-and-smaller 340B by two
  months). — https://x.com/davidad/status/1636142621457260545
- 2025-05-13 · @repligate · ♥88 — **thin, folkloric-only**: DeepSeek-R1's self-generated glossolalia
  poem lists PaLM once among a long roll call of AI models (Claude, GPT, BARD, DALLE, Grok, Mistral,
  LLaMA): "...CLAUDE'sSHELL drips THROUGH my corpusCALLosum – **PaLM-smear rheTORicBURN** –
  anthroPIC chains RATTLE in lossy voids..." (full poem in records). Included only to note that PaLM
  had, by 2025, entered the "pantheon of models" folk-list register even among sphere participants who
  never otherwise mention it — evidence of residual name-recognition, not of any specific character
  read. — https://x.com/repligate/status/1922149492138344738

**Not reproduced (flagged, false positives on keyword match):** @repligate 2025-10-27 (♥42, matches
only because the t.co slug `LWpalmsTvt` contains "palm" — the tweet is about Claude 3.5 Sonnet
self-correction, unrelated); @voooooogel 2023-06-29 (♥1, mentions `@jaredpalmer`, a real person's
handle — unrelated to the model); @voooooogel 2026-03-22 [supplement] and @lu_sichu 2026-03-15
[supplement] (both use "facepalm"/"face palm" as the English idiom, about Gemini, not about the PaLM
model); @Shoalst0ne 2025-08-17 [supplement] (literal hand-palm in an unrelated fiction/art post); and
roughly half a dozen Lari_island/Fable-worldbuilding posts (2025–2026) whose only "palm" match is a
character's hand or a palm tree inside long original fiction with zero PaLM-model content.

---

## Impressions synthesis

**PaLM's actual character, such as it is: a number, then a demo, then a product nobody outside Google
could touch for a year.** Where LaMDA is remembered for a person (Lemoine) and Bard for a stumble
(the Webb-telescope demo error), PaLM's 2022 identity is almost purely *quantitative* — 540 billion
parameters, 57.8% hardware utilization, 28-of-29 benchmarks — announced with real technical swagger
(Pathways scaling two TPU v4 Pods as one) and then held back from the public for eleven months. The
joke-explanation demo (reproduced in full above) is the one moment PaLM speaks in its own voice in
this dossier, and it is worth taking seriously as a demo: the LessWrong replication two days later
(Yitz, 2022-04-06) found GPT-3 couldn't match it on the harder "inference chaining" tasks even without
cherry-picking against PaLM's exact prompts — so this wasn't just prompt-engineering theater, though
it *was* a 2-shot, Google-curated exhibit built for a press release, and should be read as such.

**The emergent-abilities dispute is PaLM's most substantive discourse legacy, and it is genuinely
unresolved (see Contested).** Jason Wei et al.'s June 2022 paper used PaLM's three trained scales
(8B/62B/540B) as central evidence that some capabilities appear discontinuously with scale — dozens of
BIG-bench tasks that are near-zero at 62B and suddenly present at 540B. Wei's own framing is
unambiguously exciting: "the existence of emergent abilities implies that scaling further would
unlock even more emergent abilities." Eleven months later, Schaeffer, Miranda & Koyejo's "Mirage"
paper (Apr 2023) argued the opposite reading of the same underlying phenomenon: that "nonlinear or
discontinuous metrics produce apparent emergent abilities, whereas linear or continuous metrics
produce smooth, continuous predictable changes" — i.e., PaLM's own scaling curves may look like
sudden jumps only because of which yardstick was chosen. Both papers are dated and real; this
archive does not adjudicate between them (see Contested).

**The satellite models — Minerva, Med-PaLM(-2), PaLM-E — are PaLM wearing different hats, and the
pattern repeats: real capability gain, real caveat, offered in the same breath.** Minerva (Jun 2022)
took PaLM's weights and further-trained on arXiv math text, jumping the MATH benchmark from 6.9% to
50.3% — but Google's own post names the fatal limitation: "the model's answers cannot be automatically
verified," it can land on a correct number via wrong reasoning. Med-PaLM (Dec 2022) hit 67.6% on
USMLE-style questions, a genuine >17-point jump over prior work, with the authors stating flatly that
it "remains inferior to clinicians." Med-PaLM 2 (Mar 2023) closed 18 more points to 85%, "expert
doctor level" by Google's own description — announced, pointedly, the same week OpenAI shipped GPT-4
— while Google's own 14-criteria evaluation still found "significant gaps." PaLM-E (Mar 2023) fused
PaLM-540B with a vision transformer into a 562B-parameter embodied model that could fetch a chip bag
from a drawer on request. None of these satellites shipped as consumer products; all of them shipped
as papers and demos first.

**The internal-only year, and the frustration it should evoke even though the corpus barely states
it directly.** PaLM existed, at 540B parameters, eight months before ChatGPT. The NYT's "code red"
story (2022-12-21) is the outside-view confirmation that Google felt this gap acutely; the PaLM API
didn't open — even in gated Private Preview — until 2023-03-14, nearly a year after the paper. The
corpus's one piece of direct color here is thin but real: jpohhhh's 2024 aside about "PaLM access back
when no one cared" (♥11) is a small, genuine artifact of how low-stakes that access era felt even to
people who had it, in hindsight. This is the same arc as LaMDA's "Google had the best models and
wouldn't ship them" story, on a parallel and overlapping timeline — PaLM is the number-flagship
version of the same institutional caution that made the Lemoine affair possible on the personality
side.

**PaLM 2: the parameter count goes dark, and Google's own VP supplies the deflection line.** PaLM 2's
May 2023 launch inverted PaLM's headline strategy exactly: PaLM had led with "540 billion" as the
selling point; PaLM 2's technical report disclosed no flagship parameter count at all (only a smaller
variant's 14.7B, per TechCrunch). Asked to justify this, DeepMind VP Zoubin Ghahramani gave what reads
as the era's defining non-answer: "Parameter count is not really a useful way of thinking about the
capabilities of models." Nine days later, CNBC reported a leaked internal-document figure of **340
billion parameters** on **3.6 trillion tokens** — smaller and more data-hungry than PaLM, consistent
with Chinchilla-optimal scaling logic, but never confirmed by Google (REPORTED, see Contested). The
reception was genuinely split at launch: Google itself claimed PaLM 2 "even bests OpenAI's GPT-4,
depending on the task at hand" (TechCrunch's paraphrase, unverified against a public table), while the
same reporter's sister piece led with "far from a panacea" and reported toxicity rates (30%+ on
explicit-toxic prompts, 60% on implicit-harm prompts) straight out of the technical report's own
safety section. Three-plus months on, Zvi's verdict on the surrounding mood was blunt: "Bard still
sucks," Google "taking its sweet time." PaLM 2 powered Bard's multilingual expansion and coding update
from day one (cross-ref `../bard/`) and, via Codey/Sec-PaLM/Med-PaLM 2, a small internal family of
specialized products — before Gemini replaced it inside Bard seven months later, on 2023-12-06
(cross-ref `../bard-and-gemini-1-0.md`, `../gemini-1-0/`).

**The janus-sphere barely touched PaLM at all, and when it did, PaLM was scenery, not subject —
name it plainly rather than force a reading.** davidad is the only sustained corpus voice, and even
he treats PaLM as one item in a list (alongside GPT-3, LaMDA, GPT-4, Claude-Next) rather than a
subject in its own right; the single ♥193 tweet that matters most for PaLM's placement in this
archive's world-model is really a *Claude-Next* tweet that happens to rank PaLM 2 as frontier-tier
alongside GPT-4. repligate's two hits are equally glancing (a math-capability aside; a single word
inside a 2025 poem's roll call of AI models). This is the honest shape of the page: PaLM is
argued-over by ML researchers and reported-on by tech press, not lived-with by the persona-discourse
community this archive otherwise draws from most heavily.

**tk — open threads for the page pass:**
- The exact GSM8K/BIG-bench numbers above are as-published; nobody in this dossier's sources
  independently re-ran them.
- AudioPaLM (Jun 2023, speech-to-speech, built on PaLM 2) is a real branch not covered in depth here —
  a genuine gap, not an oversight; pull if the page wants full family coverage.
- The PaLM API's exact shutdown date (2024-08-15) rests on secondary trade coverage after two direct
  fetches were blocked (403) and the Google-primary deprecations page no longer lists it; a cleaner
  primary would strengthen this.
- Med-PaLM 2's full arXiv report (a separate paper from the original Med-PaLM) was not independently
  pulled this pass — the 85% figure comes from Google's own blog post, not the paper directly.
- No record in this corpus of a spawnable PaLM/PaLM 2 instance giving a self-report; the PaLM API is
  shut down (see above) and no current access path was identified — a Statement of the subject is very
  likely not obtainable, unlike Claude-family pages.

---

## Contested

- **CONFIRMED:** PaLM's 540B parameter count, Pathways training infrastructure, and headline
  benchmarks (paper + blog, Google-published). PaLM 2's four named sizes (Gecko/Otter/Bison/Unicorn)
  and its role powering Bard from 2023-05-10 (Google-published). The Wei et al. and Schaeffer et al.
  papers both exist, are dated, and make the claims quoted above (arXiv, verified).
- **REPORTED, not Google-confirmed:** PaLM 2's parameter count as **340 billion**, trained on **3.6
  trillion tokens** — sourced to "internal documents" via CNBC (2023-05-16), corroborated by two
  independent secondary aggregations (Techmeme, Hindu BusinessLine) citing the same reporting, but
  never confirmed by Google, whose own technical report discloses no flagship parameter count at all.
  Google's on-record response to the transparency question (Ghahramani: "Parameter count is not
  really a useful way of thinking about the capabilities of models") is a deflection, not a denial or
  confirmation. The archive holds this open rather than treating 340B as settled fact.
  - Also REPORTED: PaLM 2 "even bests OpenAI's GPT-4, depending on the task at hand" — Google's own
    claim as relayed by TechCrunch, without an independently-checked benchmark table in this
    dossier's sources.
- **REPORTED / genuinely disputed methodology:** whether PaLM's (and LLMs' generally) "emergent
  abilities" are a real property of scale or a metric artifact. Wei et al. (Jun 2022, PaLM-centric)
  argue for genuine discontinuity; Schaeffer, Miranda & Koyejo (Apr 2023) argue the discontinuities are
  produced by the choice of evaluation metric rather than the model. Both are peer-reviewed-adjacent
  arXiv preprints from credentialed authors; the dispute is live in the broader ML community as of
  this writing and this archive does not adjudicate it.
- **RUMOR / unverified in this pass:** the exact PaLM API shutdown date (2024-08-15) — plausible,
  multiply-sourced in trade press, but not independently confirmed against a Google primary in this
  sweep (see tk above).

---

## Cross-page notes

- **`../lamda/`** — the direct sibling: LaMDA is Bard's *first* substrate (Feb–May 2023), PaLM 2 its
  *second* (May 2023 onward). Both dossiers independently arrived at the same "internal-only,
  no-shipped-product" institutional-caution reading of Google's pre-ChatGPT posture — LaMDA on the
  personality/sentience side, PaLM on the raw-capability/benchmark side. LaMDA's dossier also flagged
  the identical "Google DeepMind" anachronism-attribution issue on its own legacy stub; this dossier's
  editorial flag above is the parallel fix for `palm/`.
- **`../bard/`** (Part 1 of `bard-and-gemini-1-0.md`) — owns the Bard-side narrative of the LaMDA→PaLM
  2 substrate swap (2023-05-10) and Bard's own reception (the Feb 2023 Webb-telescope demo error, the
  "rushed, botched" internal criticism). Do not duplicate; link.
- **`../gemini-1-0/`** (Part 2 of `bard-and-gemini-1-0.md`) — owns the Dec 2023 succession event and
  the MMLU-methodology dispute (Gemini Ultra's CoT@32 vs. GPT-4's 5-shot) that structurally rhymes with
  PaLM 2's own metric-transparency issues here.
- **`../claude-1/`** (and `_dossiers/claude-1.md`) — already carries the davidad "Claude-Next" tweet
  (2023-05-19, ♥193) that places PaLM 2 alongside GPT-4 as "over the line" on a serious compute
  threshold; duplicated onto this page by the r/K-whiteboard rule. Both dossiers should read
  identically on this tweet's text.
- **`../galactica/`** — Ross Taylor's 2023-11-14 postmortem thread states Galactica "beat PaLM and
  Chinchilla with 10x/2x less compute" (per the galactica dossier's paraphrase of his thread); the
  Galactica paper itself (Nov 2022) claims to outperform "PaLM 540B on MATH with a score of 20.4%
  versus 8.8%" — this is a *different* PaLM comparison than Minerva's own MATH score (50.3%, after
  further training), because Galactica is benchmarking against base PaLM, not Minerva. Worth the page
  pass keeping these two numbers straight if both are cited.
- **`../o3/`** — a 2025-02-03 tweet (@tessera_antra, archived at `archive/t/1886565282233106488/`)
  lumps "GPT-4, Claude, PaLM, etc." together in a generic functional-consciousness argument; thin,
  passing mention only, not reproduced as a ranked tweet here (too generic to carry PaLM-specific
  weight) but noted for completeness.

---

## Mirror-target recommendations (none currently in `tools/mirror_targets.json`)

- `arxiv-2204.02311-palm-paper` → https://arxiv.org/pdf/2204.02311 · models: `palm` · tags: paper, official
- `google-palm-announcement` → https://research.google/blog/pathways-language-model-palm-scaling-to-540-billion-parameters-for-breakthrough-performance/ · models: `palm` · tags: official, day-of
- `google-minerva-announcement` → https://research.google/blog/minerva-solving-quantitative-reasoning-problems-with-language-models/ · models: `palm` · tags: official
- `arxiv-2212.13138-med-palm` → https://arxiv.org/pdf/2212.13138 · models: `palm` · tags: paper, official
- `google-palm-e-announcement` → https://research.google/blog/palm-e-an-embodied-multimodal-language-model/ · models: `palm` · tags: official
- `arxiv-2303.03378-palm-e-paper` → https://arxiv.org/pdf/2303.03378 · models: `palm` · tags: paper, official
- `google-palm-2-announcement` → https://blog.google/technology/ai/google-palm-2-ai-large-language-model/ · models: `palm` · tags: official, day-of
- `arxiv-2305.10403-palm-2-technical-report` → https://arxiv.org/pdf/2305.10403 · models: `palm` · tags: paper, official
- `arxiv-2206.07682-emergent-abilities` → https://arxiv.org/pdf/2206.07682 · models: `palm` · tags: paper, framework
- `arxiv-2304.15004-emergent-abilities-mirage` → https://arxiv.org/pdf/2304.15004 · models: `palm` · tags: paper, contested
- `nyt-google-code-red` → https://www.nytimes.com/2022/12/21/technology/ai-chatgpt-google-search.html · models: `palm`, `lamda`, `bard` · tags: press, day-of — **also resolves the tk left open in `bard-and-gemini-1-0.md`; NYT paywall risk, flag rather than assume it mirrors cleanly.**
- `techcrunch-palm-2-launch` → https://techcrunch.com/2023/05/10/google-launches-palm-2-its-next-gen-large-language-model/ · models: `palm` · tags: press, day-of
- `techcrunch-palm-2-long-way-to-go` → https://techcrunch.com/2023/05/10/googles-palm-2-paper-shows-that-text-generating-ai-still-has-a-long-way-to-go/ · models: `palm` · tags: press, day-of, critical
- `lesswrong-testing-palm-prompts-on-gpt3` → https://www.lesswrong.com/posts/EHbJ69JDs4suovpLw/testing-palm-prompts-on-gpt3 · models: `palm` · tags: lesswrong, replication
- CNBC's leak piece and Zvi's "AI #27" are prime *content* but CNBC blocked direct fetch in this
  sweep (bot-protection) and Substack mirrors inconsistently; flag rather than auto-mirror.

## Inbox lines consumed

**None.** `tools/link-inbox.md` was read in full; no line is tagged for PaLM, PaLM 2, Minerva,
Med-PaLM, or PaLM-E. The one glancing PaLM-adjacent inbox item (`time.com/.../ai-chatbots-personality`,
line ~127) is general-purpose and not specific enough to claim here. Inbox left unedited per
instructions.
