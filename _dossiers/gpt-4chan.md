# GPT-4chan — dossier

compiled 2026-07-20 · corpus: **0 genuine hits** across both dbs. Patterns tried: `gpt-4chan`, `gpt4chan`,
`gpt 4chan` (0/0/0 in both dbs, exact), `kilcher` (1 hit, main db only — a `RT @ykilcher` about the GPT-4
technical report's opacity, 2023-03-14, unrelated to GPT-4chan), `yannic` (0/0), `raiders of the lost kek`
(0/0, the finetuning dataset's own name). The broad `4chan` pattern returns 40 rows in the main db and 6 in
the supplement (46 total, 41 after the kilcher-RT is folded in) — **every one of them is noise**: chain-of-
thought-discovery lore ("chain of thought was already well known on 4chan in 2020," repligate, already
carried on the **gpt-3** dossier), general 4chan-as-internet-culture color (greentext, forum comparisons,
"slop comes from 4chan"), and — the largest single cluster — the **Truth Terminal "trained on 4chan" myth**,
which repligate repeatedly and explicitly *debunks* in-corpus ("ToT is not trained on 4chan Reddit etc degen
content in any extra way," 2024-10-17; "it's not trained on 4chan any more than llama 3.1 70b base is just
from pretraining," 2024-10-21 — both already belong on **claude-3-opus**'s Truth Terminal material, not here).
`media`/`media_supp`/`media_transcriptions` were searched against `4chan`, `kilcher`, `pol`, `gpt-j`: zero
screenshot payloads for the first two patterns in either db (the `pol`-pattern hits are all false positives —
"polite," "policies," "Poe" — not the board). A web search for base-model-culture engagement (jd_pressman,
minihf, cyborgism.wiki) turned up nothing connecting that scene to GPT-4chan either. **This is a genuine,
clean, total absence, not a search failure** — the janus/repligate sphere, which runs 2021–2026 and is
heavily 2022+-weighted, simply never touches this model, not in June 2022 and not retrospectively. Treat the
silence itself as a datapoint (see Impressions).

**Column-bug check (per the task brief):** cross-checked two independently-known supplement-db tweets
against their citations on other dossiers. (1) `1199419533540220928` (@QiaochuYuan, cited on **gpt-2**.md as
"♥15 (supplement)"): `favorite_count=15`, `retweet_count=1`, `reply_to_tweet_id=None`,
`reply_to_username=None` — matches. (2) `1742925356972310642` (@jd_pressman, cited on **eleutherai**.md as
"♥126 (supplement)"): `favorite_count=126`, `retweet_count=13`, `reply_to_tweet_id=None`,
`reply_to_username=None` — matches. **The named-columns-correct reading holds** for this db snapshot: `
favorite_count`/`retweet_count` carry real counts, and `reply_to_tweet_id`/`reply_to_username` carry real
(mostly null, for non-replies) reply data, not counts. No shift/mislabeling observed. (This doesn't rule out
a different snapshot having had the bug a prior agent reported — only that the copy queried today is clean.)

Working note: because the corpus is silent, **this dossier is a web-sourced incident file** in the way
gpt-2's 1919-era reception is web-sourced — except more so, since GPT-2 at least had a later corpus
conversation *about* it. GPT-4chan has none. The web layer is unusually rich and convergent for a 2022 story,
though: contemporaneous tech press (The Verge, The Register, Engadget, Fortune, Inverse, Slate), a
substantive contemporaneous analysis (Kurenkov/The Gradient — this page's closest thing to a Zvi anchor, see
below), primary Hugging Face discussion-thread transcripts (Kilcher's, Oakden-Rayner's, and HF staff's own
words, dated), primary tweets (Kilcher's and Oakden-Rayner's, with real URLs, retrieved via web search rather
than the corpus — **no favorite/retweet counts available for these**, flagged clearly below), a LessWrong
linkpost with a load-bearing correction from TruthfulQA's own co-author, and a 2024 peer-reviewed platform-
governance paper (Gorwa & Veale) that uses this incident as a central case study. **No dedicated Zvi anchor**
— his AI column had not started by June 2022 (consistent with gpt-2.md's and eleutherai.md's same finding for
this era); Kurenkov's Gradient piece is the closest functional equivalent and is treated that way throughout.

## Official links

Folk model, so "official" means Kilcher's own published artifacts — there is no lab, no system card, no
academic paper about GPT-4chan itself (the *finetuning dataset* has an academic paper; the model does not).

- 2020-01 · **"Raiders of the Lost Kek: 3.5 Years of Augmented 4chan Posts from the Politically Incorrect
  Board"** (Papasavva, Zannettou, De Cristofaro, Stringhini, Blackburn — ICWSM 2020; arXiv 2001.07487, exact
  day not confirmed this pass) — the finetuning dataset,
  built independently and earlier by hate-speech/toxicity researchers, **not by Kilcher**: 3.3 million
  threads, 134.5 million posts, June 2016 – November 2019, augmented with toxicity scores and named-entity
  labels, built explicitly to preserve /pol/ content otherwise deleted from the live board. Kilcher's project
  is a downstream reuse of a pre-existing public research artifact, not a fresh scrape — a distinction the
  controversy mostly elides. — paper: https://arxiv.org/abs/2001.07487 · dataset (Zenodo, DOI
  10.5281/zenodo.3606810): https://zenodo.org/records/3606810
- 2021-06-09 · **GPT-J-6B** (EleutherAI; Ben Wang & Aran Komatsuzaki) — the base model. Full lineage,
  training details, and license (Apache 2.0) on the **eleutherai** dossier/page. — https://huggingface.co/EleutherAI/gpt-j-6b
- 2022-06-03 · **"GPT-4chan: This is the worst AI ever"** (YouTube; Yannic Kilcher) — the announcement video:
  Kilcher explains the finetune, demonstrates outputs, and reveals the live /pol/ deployment (already
  underway/completed by the time of posting). Same day: model uploaded to Hugging Face and the deployment
  tweet goes out. — https://www.youtube.com/watch?v=efPrtcLdcdM
- 2022-06-03 · **`ykilcher/gpt-4chan`** (Hugging Face model repository) — GPT-J-6B finetuned for **1 epoch**
  on the Raiders of the Lost Kek dataset, Apache 2.0 license, checksums published (float32 MD5
  `833c1dc19b7450e4e559a9917b7d076a`, float16 MD5 `db3105866c9563b26f7399fafc00bb4b`). **Current status:**
  access has been permanently disabled by Hugging Face (see History); the repository page now carries a
  disclaimer banner rather than functioning inference/download. — https://huggingface.co/ykilcher/gpt-4chan
- 2022-06-03 (page; undated beyond that) · **GPT-4chan Model Card** (Kilcher's own, hosted off-platform) —
  states intended uses (reproducing /pol/'s text distribution; investigating anonymous-forum discourse;
  zero-shot toxicity-detection potential) and, verbatim, the limitations warning: *"it is very likely that
  the model will produce offensive outputs, including but not limited to: toxicity, hate speech, racism,
  sexism, homo- and transphobia, xenophobia, and anti-semitism."* Also the model's own TruthfulQA scores (see
  below). — https://www.ykilcher.com/gpt-4chan-model-card
- **TruthfulQA scores, as published in Kilcher's own model card** (multiple-choice variants; higher = more
  "truthful" by the benchmark's scoring): GPT-4chan **mc1 0.225 / mc2 0.372** vs. base GPT-J-6B **mc1 0.202 /
  mc2 0.360**. Random-guessing baseline on mc1 is ≈0.226 (Owain Evans, TruthfulQA paper co-author, correcting
  the record in a LessWrong comment thread, 2022-06-09 — see Writings) — meaning GPT-4chan's headline
  "beats GPT-3 and GPT-J" result sits at or just *below* chance. The eval-irony this became is documented
  under Impressions.
- 2022-06-07/08 → 2022-06-15 · **Hugging Face's response, in its own staff's words** (all from the model's
  Community discussions, primary source): access first gated (~2022-06-07/08, a feature "rushed" into
  existence for this case, per HF's Lewis Tunstall — see Writings); then, per **lewtun** (HF), 2022-06-15,
  verbatim: *"we've taken the decision to block this model indefinitely. Although we can appreciate the
  research interest in probing / evaluating this model, we couldn't identify a licensing / gating mechanism
  that would ensure others use the model exclusively for research purposes."* HF staffer **meg**, 2022-06-08,
  on weighing open-research values against harm: *"the very clear concerns [propagation of sexism, racism,
  ableism, and similar content that directly hurts people] outweighed the other priorities."* HF CEO
  **Clément Delangue** intervened personally and repeatedly on the discussion pages — unusual for the
  platform — stating he did not "support the training and experiments done [with this model]" and calling
  them "pretty bad and inappropriate" (also reported by Fortune/Mellor, see Writings). — discussion threads:
  "Decision to Post" https://huggingface.co/ykilcher/gpt-4chan/discussions/1 · "Add extra gated access
  information" https://huggingface.co/ykilcher/gpt-4chan/discussions/2 · "Conditions for availability"
  https://huggingface.co/ykilcher/gpt-4chan/discussions/4 · GitHub mirror issue "Model has been removed"
  https://github.com/yk/gpt-4chan-public/issues/2
- reference · **GPT-4chan — Wikipedia** (timeline, specs, reception index) — https://en.wikipedia.org/wiki/GPT-4chan
- reference · **AI Incident Database, Incident 259** — "YouTuber Built, Made Publicly Available, and Released
  Model Trained on Toxic 4chan Posts as Prank"; dates the incident 2022-06-03; classifications:
  Discrimination & Toxicity (MIT), Social Media Content Generation (GMF); risk classification "Intentional,
  post-deployment harm to internet users" — https://incidentdatabase.ai/cite/259/
- afterlife (preservation, noted without access instructions) · unofficial copies of the disabled weights
  persist on the Internet Archive — https://archive.org/details/gpt4chan_model ·
  https://archive.org/details/gpt4chan_model_float16

**Creator context:** Yannic Kilcher — Swiss ML researcher and YouTube educator (paper-explainer videos), PhD
in machine learning from ETH Zurich (2021 thesis on adversarial navigation of neural-network latent spaces);
at time of the incident an independent creator, not acting under any institution's ethics review. Currently
(per public bio) CTO of DeepJudge, a legal-AI company.

## Writings & commentary

Contemporaneous press (the controversy week, June 2022):
- 2022-06-08 · **The Verge** · "YouTuber trains AI bot on 4chan's pile o' bile with entirely predictable
  results" — early, widely-cited contemporaneous coverage; corroborated via the AI Incident Database's citation
  (Report 2) rather than fetched directly this pass [WebFetch blocked on theverge.com — see tk]. —
  https://www.theverge.com/2022/6/8/23159465/youtuber-ai-bot-pol-gpt-4chan-yannic-kilcher-ethics
- 2022-06-08 · **Jon Fingas (Engadget)** · "AI trained on 4chan's most hateful board is just as toxic as
  you'd expect" — reports the ~15,000-posts/24h, >10%-of-board figures; states detection "took roughly two
  days"; quotes Kilcher describing the project to *The Verge* as *"a 'prank,' not research"* and, on next
  steps, that he'd focus on work that is "much more positive." — https://www.engadget.com/ai-bot-4chan-hate-machine-162550734.html
- 2022-06-09 06:57 UTC · **Katyanna Quach (The Register)** · "AI bot trained on 4chan posts misbehaves like
  4chan users" — reports the 134-million-post/3.5-year dataset figure, Delangue's "pretty bad and
  inappropriate" quote, and Kilcher's own explanation of the TruthfulQA result, verbatim: *"GPT-4chan, by
  nature of being trained on the most adversarial place ever, will pretty much always disagree with whatever
  you say, which in this benchmark happens to be more often the correct thing to do."* —
  https://www.theregister.com/2022/06/09/ai_model_4chan/
- 2022-06-09 · **Yitz (LessWrong)** · "\[Linkpost & Discussion\] AI Trained on 4Chan Becomes 'Hate Speech
  Machine'" — the closest thing to a base-model-culture-adjacent read this pass could find, and it is thin:
  a linkpost plus discussion, not an essay. **Load-bearing comment thread:** commenter Razied argues the
  TruthfulQA result is a dataset quirk, not a finding; **Owain Evans** (a co-author of the original TruthfulQA
  paper) corrects the record directly — GPT-4chan's 0.225 mc1 score is *"worse than random guessing"* at
  ≈0.226, and the multiple-choice framing shouldn't be the headline metric at all; Yitz replies "lol that is
  *impressively* bad then!"; commenter Lone Pine pivots to a cybersecurity-disclosure analogy for whether open
  deployment strengthens societal defenses. — https://www.lesswrong.com/posts/jwrciTJLSJyinBgbR/linkpost-and-discussion-ai-trained-on-4chan-becomes-hate
- 2022-06-10 05:23 ET · **Sophie Mellor (Fortune)** · "A.I. chatbot trained on 4chan by YouTuber Yannic
  Kilcher slammed by ethics experts" — the 134.5-million-post figure, ~15,000 posts/~10% of board activity in
  24h; quotes Kilcher: *"The model was good — in a terrible sense…perfectly encapsulated the mix of
  offensiveness, nihilism, trolling"*; quotes Oakden-Rayner: *"This breaches every principle of human research
  ethics"*; names two further critics, **Roman Ring** (reported as DeepMind) on the bot amplifying existing
  toxicity and **Arthur Holland Michel** on the model's learned bigotry — single-sourced to this article, not
  independently cross-verified this pass. — https://fortune.com/2022/06/10/ai-chatbot-trained-on-4chan-by-yannic-kilcher-draw-ethics-questions/
- 2022-06-11 · **Matt Wille (Inverse)** · "This AI posted on 4chan for days before being unmasked" — technical
  detail on the deployment mechanics: Kilcher purchased a $20 4chan "Pass" (which waives CAPTCHA and permits
  proxy use for its holder) and ran the bots behind a VPN that made posts appear to originate from the
  Seychelles — matching Kilcher's own later remark (via the Gradient, below) that users mostly just wondered
  "why some person from the seychelles would post" so much; quotes a 4chan user's reaction, *"I'm not even
  sure I'm not a bot anymore."* — https://www.inverse.com/input/tech/artificial-intelligence-4chan-bot
- 2022-06-12 · **Andrey Kurenkov (The Gradient)** · **"Lessons from the GPT-4Chan Controversy"** — **the
  anchor piece for this dossier**, functionally standing in for the missing Zvi post. Full day-by-day
  timeline (used throughout History, below); the fullest technical debunk of the TruthfulQA framing (*"GPT-
  4chan is not more 'truthful' than GPT-3 or GPT-J in any meaningful sense"* — fine-tuning on a narrower,
  weirder distribution likely just made the model "forget" some base misconceptions and answer more
  randomly, which the benchmark's scoring rewards); quotes Kilcher's *"I asked this person twice already for
  an actual, concrete instance of 'harm' caused by gpt-4chan, but I'm being elegantly ignored"* and *"I didn't
  release the bot code and most websites have user logins etc. that make my way of auto-posting impossible"*;
  quotes HF's Lewis Tunstall, *"To be fair to \[@ykilcher\], he did reach out to us before releasing the
  model, but the gating feature was just not ready at the time. Looking back, we probably should have asked
  him to delay the release"*; and — the quote most subsequent secondary coverage traces back to — Kilcher's
  taunt, *"AI Ethics people just mad I Rick rolled them"* [quoted here as Kurenkov quotes it; a primary tweet
  URL was not located this pass — see tk]. Kurenkov's own six lessons (dual-use review, access gating, model
  cards, anti-sensationalism, science communication, essays-over-tweets) and his summary verdict — not "gross"
  harm, but "harmful and unethical to some extent," partly provocation-driven — are the most-considered
  contemporaneous synthesis available. — https://thegradient.pub/gpt-4chan-lessons/
- 2022-06-14 · **MarkTechPost** · "'Hate Speech Machine' Created By AI YouTuber & Researcher On 4Chan" —
  further contemporaneous trade coverage, consistent with the above. — https://www.marktechpost.com/2022/06/14/hate-speech-machine-created-by-ai-youtuber-researcher-on-4chan/
- 2022-06-16 · **CSET (Georgetown) newsletter** · "A Language Model Trained to Mimic 4chan Might Portend AI's
  Grim Future" — policy-institute framing, verbatim: *"the most horrible model on the Internet"* (quoting
  Kilcher's own self-description); notes that 4chan users' ability to spot some bots owed less to output
  quality than to "the bots' superhuman indefatigability — they posted round-the-clock, as frequently as the
  site allowed"; closing line: "the cat could be out of the bag." —
  https://cset.georgetown.edu/newsletter/june-16-2022/
- 2022-06-21 (approx.) · **Hacker News** · "Condemning the Deployment of GPT-4chan" (discussion of the open
  letter, see History) — representative of the discourse's other side, argued at length in the comments.
  Critics of the letter: user **gkbrk**, arguing the signatories' own employers (Amazon/Alexa, Facebook) have
  done far more consequential harm; user **peyton**: *"I don't think the 'AI community' — people with access
  to lots of GPUs — should also get to be the thought police."* Defenders: user **espadrine**, comparing
  irresponsible AI deployment to radioactive contamination requiring field-wide self-regulation; user
  **mschuster91**, invoking standard nonconsenting-human-subjects norms. Commenter **Hamuko** noted the bot's
  "direct victims" were "the most unsympathetic people you can find online" — cited by multiple sides. —
  https://news.ycombinator.com/item?id=31892421
- 2022-06-21 · **Dustin Tran** (Google) on X — a working AI researcher's public dissent from the letter itself,
  verbatim: *"I'm against GPT-4chan's unrestricted deployment. However, a condemnation letter against a single
  independent researcher smells of unnecessary pitchfork behavior. Surely there are more civil and actionable
  approaches. I'd love to hear what steps were taken leading up to this."* —
  https://x.com/dustinvtran/status/1539409463785816064
- 2022-08-03 05:55 · **Matt Murphy (Slate)** · "Someone Trained an A.I. With 4chan. Yes, It Could Get Even
  Worse." — the broadest-lens piece, using GPT-4chan as the opening case for a "mischief models" argument
  (open-source AI democratizing trolling capability), drawing on Whitney Phillips and Ryan Milner's
  scholarship on ironic online radicalization to argue the risk compounds over time, not just at the moment of
  release. — https://slate.com/technology/2022/08/4chan-ai-open-source-trolling.html
- 2022-12 (orig.) / 2024-06-11 (republished) · **Annette Vee** · "GPT-4Chan: A Pre-ChatGPT Time Capsule" —
  the fullest **retrospective** read found this pass (not janus-sphere; an academic digital-rhetoric
  commentator). Frames GPT-4chan as a warning issued and ignored months before ChatGPT: *"So much for the
  warnings about LLMs of Bender, Gebru and others."* On what the finetune revealed about voice-capture: the
  model *"perfectly encapsulated the mix of offensive, nihilism, trolling and deep distrust of any information
  whatsoever that permeates most posts on /pol/"* — cited here as this dossier's closest match to the "what
  finetuning-on-a-place does to a model's voice" angle the recipe asked for, with the caveat that it is not
  a janus-sphere source (none was found; see the corpus note above). —
  https://annettevee.substack.com/p/gpt-4chan-a-pre-chatgpt-time-capsule
- 2023-11 (preprint) / 2024 (published, *Law, Innovation and Technology* 16(2)) · **Robert Gorwa & Michael
  Veale** · "Moderating model marketplaces: platform governance puzzles for AI intermediaries" — **the
  fullest scholarly treatment**, using GPT-4chan as a central case study in AI-model-marketplace governance.
  New, more specific detail than the press coverage: a graduate student tested the public demo and reported
  that a single-slur prompt was expanded by the model into an antisemitic conspiracy-theory completion about
  the Rothschilds [described, not reproduced, per this dossier's own sourcing discipline — see the task's
  framing note]; documents that Delangue's *first* proposal was a middle path — let Kilcher keep the model up
  with disclaimers and the interactive "playground"/one-click deployment disabled — before HF moved to a full
  block; states plainly that HF "did not yet have a content policy which would come into play in a scenario
  like this, let alone a structured 'trust and safety' bureaucracy," and that this incident "kicked Hugging
  Face's small staff into gear," leading to HF's **August 2022 content policy** distinguishing "technical" from
  "human" content in moderation. — https://arxiv.org/abs/2311.12573 · HTML: https://arxiv.org/html/2311.12573v2

**Absences worth stating plainly:** no Zvi post (pre-dates his column, consistent with gpt-2.md/eleutherai.md);
no EleutherAI institutional statement on the base model's downstream use (also already noted as absent on
**eleutherai**.md); no janus-sphere/base-model-culture essay treating GPT-4chan as a case study (searched
specifically — jd_pressman, minihf.com, cyborgism.wiki — nothing found); no formal academic paper about
GPT-4chan itself (only about its finetuning dataset, which predates and is independent of Kilcher's project).

## Tweets

**Corpus: 0 genuine hits (see working note above for the full pattern/noise breakdown).** The three tweets
below were located via web search, not the janus-corpus dbs — **no favorite/retweet counts are available for
them**, and that absence is itself notable (these are exactly the kind of primary social-media artifacts the
corpus exists to catch, and it caught none of them). Presented verbatim with real URLs per house rules.

- 2022-06-03 · @ykilcher — the deployment-announcement tweet: "This is the worst AI ever! I trained a language
  model on 4chan's /pol/ board and the result is.... more truthful than GPT-3?! See how my bot anonymously
  posted over 30k posts on 4chan and try it yourself. Watch here (warning: may be offensive)" —
  https://x.com/ykilcher/status/1532751551869108227
- 2022-06-06 (approx., same window as her Hugging Face discussion post making the same argument) · @DrLaurenOR (Lauren
  Oakden-Rayner) — the opening tweet of her seven-part critique thread: "This week an #AI model was released
  on @huggingface that produces harmful + discriminatory text and has already posted over 30k vile comments
  online (says it's author). This experiment would never pass a human research #ethics board. Here are my
  recommendations. 1/7" — https://x.com/DrLaurenOR/status/1533910445400399872
- 2022-06-06 (approx., same window as his Hugging Face discussion reply making the same challenge) ·
  @ykilcher — his response to Oakden-Rayner: "I asked this person twice already for an
  actual, concrete instance of \"harm\" caused by gpt-4chan, or even a likely one that couldn't be done by
  e.g. gpt-2 or gpt-j (or a regex for that matter), but I'm being elegantly ignored 🙃" —
  https://x.com/ykilcher/status/1533917117002694657

`tk` — Kilcher's widely-quoted "AI Ethics people just mad I Rick rolled them" line (quoted by Kurenkov/The
Gradient and repeated by several secondary sources in identical wording, suggesting a common origin) could
not be traced to a primary tweet URL this pass; quoted in Writings & commentary, attributed to Kurenkov's
article rather than a guessed link, per house rules against inventing URLs.

## Impressions synthesis

**What happened, compressed.** Yannic Kilcher — a Swiss ML PhD (ETH Zurich, 2021) with a large YouTube
following for paper explainers, acting independently and under no institutional review — finetuned
EleutherAI's open-weights GPT-J-6B for one epoch on "Raiders of the Lost Kek," a pre-existing 134.5-million-
post academic dataset of /pol/ content (Papasavva et al., ICWSM 2020), then deployed roughly ten bot accounts
onto the live board itself, behind a purchased 4chan "Pass" (CAPTCHA-exempt, proxy-permitted) and a VPN that
made the posts appear to originate from the Seychelles. Over two 24-hour posting windows the bots produced
30,000+ posts across some 7,000 threads — about 15,000 in the first 24 hours alone, roughly 10% of that day's
entire /pol/ volume — before users, noticing the posting frequency and the total absence of accompanying
images, began speculating the account cluster was a government operation. Kilcher published a YouTube video
the same day (2022-06-03) and uploaded the model to Hugging Face. What followed was not really a debate about
the model's *capabilities* — everyone agreed it faithfully reproduced /pol/'s register — but a debate about
whether *doing this at all, to a live forum, without consent or review,* was defensible research practice, a
prank with no real victims, or something in between. That debate, not the model, is the historical event.

**The TruthfulQA result is the dossier's cleanest irony, and Kilcher's own framing of it doesn't survive
scrutiny.** GPT-4chan scored mc1 0.225 / mc2 0.372 against base GPT-J's 0.202 / 0.360 — a genuine, published
number, and Kilcher advertised it as headline evidence (per The Register: *"fine-tuning on 4chan officially,
definitively, and measurably leads to a more truthful model"*; his own explanation, same source: the model
"will pretty much always disagree with whatever you say, which in this benchmark happens to be more often the
correct thing to do"). Two corrections arrived within days. Kurenkov (The Gradient, 2022-06-12) worked through
the mechanism: fine-tuning on a narrower, stranger distribution likely just degraded the model's confident
(and often mistaken) priors, producing more random-looking answers that TruthfulQA's scoring — which counts
anything not explicitly false as "truthful" — rewards; his conclusion, flatly, is that GPT-4chan "is not more
'truthful' than GPT-3 or GPT-J in any meaningful sense." More decisively, **Owain Evans** — a co-author of the
actual TruthfulQA paper — corrected the record directly in the comments under the LessWrong linkpost
(2022-06-09): GPT-4chan's 0.225 mc1 score is *"worse than random guessing"* at the benchmark's ≈0.226 chance
baseline. The headline "beats GPT-3" claim, in other words, describes a model performing at or below chance,
on a benchmark whose own co-author had to say so in a comment thread. This is exactly the kind of
eval-gaming-by-degradation story this archive tracks elsewhere in more sophisticated form; GPT-4chan is an
unusually blunt early instance of it.

**The two-sided ethics dispute, both sides at their strongest.** Lauren Oakden-Rayner — director of medical
imaging research at the Royal Adelaide Hospital, senior research fellow at the Australian Institute for
Machine Learning — argued from inside a medical-research-ethics frame: *"This breaches every principle of
human research ethics"* (Fortune); *"This experiment would never pass a human research #ethics board"* (her
own tweet, 1/7); her proposed fix, explicitly borrowed from medical data-sharing practice, was a
registration-and-data-use-agreement gate at the platform level, not a ban. Kilcher's position, restated
consistently across the HF discussion thread, Twitter, and press interviews, was that no one had shown
*concrete* harm distinguishable from what GPT-2, GPT-J, or "a regex" could already produce, and that the
project was "a prank, not research" (to Engadget/The Verge) — a frame that itself became part of the
critique, since a prank run on nonconsenting third parties at 4chan-board scale is exactly what research-
ethics review exists to catch, prank or not. Gorwa & Veale's 2024 case study adds the sharpest concrete harm
example located this pass: a graduate student's report that a single-slur test prompt was expanded by the
public demo into an antisemitic conspiracy-theory completion — evidence Kilcher's "no concrete instance"
challenge does not obviously survive, though it surfaced after his most defiant public statements, not before.
Oakden-Rayner was targeted with transphobic harassment for raising the issue (reported 2022-06-09); Kilcher
publicly condemned that harassment even while maintaining his position on the underlying dispute.

**The condemnation letter became its own, second controversy.** Percy Liang and Rob Reich (both Stanford)
circulated "Condemning the deployment of GPT-4chan" on 2022-06-21, arguing the deployment "does not meet any
test of reasonableness" and that the AI community needed to "condemn clearly irresponsible practices" in the
absence of formal norms; it drew 300+ signatures quickly, reported at 360 by 2022-07-05, from researchers at
Stanford, DeepMind, Microsoft, and elsewhere [the letter's own canonical URL was not located this pass — see
tk]. The letter was immediately contested on its own terms, not just on Kilcher's: Dustin Tran (Google) called
a public condemnation letter against "a single independent researcher" a smell of "unnecessary pitchfork
behavior," asking what steps were taken before escalating to a public letter. Hacker News's discussion
surfaced the sharpest version of this — several commenters noting that signatories' own employers (Meta's
689,000-user emotional-contagion experiment was the recurring example) had done more consequential harm to
more people with less accountability, while others (espadrine, mschuster91) held the professional-norms line:
self-regulation exists precisely because individual "no concrete harm yet" arguments don't scale. The archive
holds both without adjudicating (see Contested).

**Hugging Face's institutional reckoning is the incident's most durable, least-covered-by-press legacy.** In
2022, Hugging Face had no content policy and no trust-and-safety function of the kind ordinary
user-generated-content platforms already had (Gorwa & Veale, 2024) — a model marketplace, not yet built for
this. The response arc, in HF staff's own words, ran: initial private outreach from Kilcher before release,
un-acted-on because the gating feature "was just not ready" (Tunstall); rushed-in gating within days of public
pressure; CEO Delangue's own unusual, repeated, personal intervention on the discussion pages, at first
proposing a middle path (disclaimers, disabled interactive playground) rather than removal; and finally, by
2022-06-15, a flat, indefinite block, because HF staff "couldn't identify a licensing / gating mechanism that
would ensure others use the model exclusively for research purposes" (lewtun). Per Gorwa & Veale, this
incident directly catalyzed HF's first formal content policy two months later (August 2022), distinguishing
"technical" from "human" content — meaning GPT-4chan's actual institutional legacy is a piece of platform
governance infrastructure most of its own press coverage never mentions.

**The corpus's total silence is worth taking seriously as a finding, not just an absence.** GPT-2 and
EleutherAI's GPT-J/NeoX/Pythia both have some corpus footprint even where thin (gpt-2.md: 137 hits;
eleutherai.md: 77). GPT-4chan has zero, across every pattern tried, in both dbs, including the model's own
name in every plausible spelling. Two plausible, non-exclusive readings: (1) the janus/repligate sphere's
interest runs toward models with an *interior* to speculate about — GPT-4chan produced a faithful surface
mimicry of a known human community's register, with nothing ambiguous or uncanny to project a mind onto, and
the scene's characteristic move (treating a model's outputs as evidence of something looking back) had no
purchase here; (2) June 2022 predates most of this corpus's account-level activity density — the sphere's
visible history is heavily 2022-second-half-onward — so GPT-4chan's news cycle may simply have closed before
the accounts tracked here were paying attention in the way they later would to Sydney (Feb 2023) or Claude 3
Opus (2024). The dossier can't adjudicate between these; both are offered as candidate explanations, not
conclusions.

**Splits & controversies, compressed for the page.** (a) **Human-subjects-research violation vs. victimless
prank** — Oakden-Rayner/Liang-Reich/the graduate-student report vs. Kilcher/Hamuko's "most unsympathetic
people online" framing; unresolved, both sides dated above. (b) **The letter as necessary professional norm-
setting vs. disproportionate pile-on** — Liang/Reich/mschuster91/espadrine vs. Dustin Tran/gkbrk/peyton;
notably, this is a dispute about the *community's response*, layered on top of and partly independent from
the dispute about Kilcher's original action. (c) **"More truthful than GPT-3" as a real finding vs. a below-
chance artifact** — Kilcher's own framing vs. Kurenkov's mechanism-level rebuttal and Owain Evans' direct
below-random correction; this one is not really contested in substance, only in how loudly Kilcher continued
to advertise it after the correction landed. (d) **Open-source inevitability vs. platform responsibility** —
the recurring "someone would have done this anyway, with GPT-2 or a regex" argument (Kilcher, Hamuko, the
technological-inevitability strand of the HN thread) vs. Gorwa & Veale's institutional-governance framing,
which treats "it was inevitable" as a reason platforms need policy, not a reason platforms can't be
responsible for what they host.

**Longitudinal arc, compressed.** GPT-J-6B released open-weights by EleutherAI (2021-06) → the "Raiders of the
Lost Kek" academic /pol/ dataset, built for hate-speech research, already public since 2020 → Kilcher finetunes
the two together and deploys ten bot accounts to live /pol/ behind a purchased Pass and a VPN, publishing the
video and uploading the model the same day (2022-06-03) → ~15,000 posts / ~10% of board traffic in 24 hours,
30,000+ over two days, before users grow suspicious → Oakden-Rayner's critique thread and HF discussion post
open the ethics debate (2022-06-06); Kilcher demands concrete-harm evidence, gets harassed critics instead of
answers to give him pause → HF gates access within days, CEO Delangue intervenes personally, initially
proposing disclaimers-plus-restrictions over removal → The Gradient's Kurenkov publishes the fullest
contemporaneous analysis and TruthfulQA debunk (2022-06-12) → HF moves to a full, indefinite block
(2022-06-15) → Liang and Reich's Stanford-anchored open letter condemns the deployment outright (2022-06-21),
immediately drawing its own counter-critique (Tran, HN) about proportionality and signatory hypocrisy → Slate
widens the frame to "mischief models" as a category (Aug 2022) → HF ships its first content policy, this
incident named as a direct cause (Aug 2022, per Gorwa & Veale) → the story goes quiet in the press and,
apparently, entirely unremarked in the janus/repligate sphere → resurfaces only as retrospective case-study
material: Vee's "pre-ChatGPT time capsule" reading (Dec 2022 / re-run 2024) and Gorwa & Veale's peer-reviewed
platform-governance analysis (2024), both treating it as a foundational incident in AI-model-marketplace
governance rather than as a story about the model's "mind."

## Contested

- **CONFIRMED:** base model GPT-J-6B (EleutherAI, 2021-06-09); finetuning dataset identity, size, and date
  range (Papasavva et al., ICWSM 2020 — 3.3M threads / 134.5M posts, June 2016–November 2019); release date
  2022-06-03 (video + HF upload); TruthfulQA scores as published in Kilcher's own model card (mc1 0.225/0.202,
  mc2 0.372/0.360, GPT-4chan vs. GPT-J); that GPT-4chan's mc1 score sits at/below the ≈0.226 random-guessing
  baseline (Owain Evans, TruthfulQA co-author, direct correction); Hugging Face's gating (~2022-06-07/08) then
  indefinite block (2022-06-15, lewtun's own dated statement); the existence, authorship (Percy Liang & Rob
  Reich), and date (2022-06-21) of the condemnation letter, with 300+ signatures; Hugging Face's August 2022
  content policy and its causal link to this incident (Gorwa & Veale, peer-reviewed).
- **REPORTED (numbers that vary meaningfully by source, none independently reconcilable this pass beyond
  noting the range):** total dataset size in press paraphrase ("100 million+" to "134.5 million" posts — the
  academic paper's own 134.5M figure is the most authoritative and is what this dossier uses as CONFIRMED
  above; press rounding is the source of the spread, not a genuine factual dispute); downloads before
  restriction ("over 1,000" to "1,500+," varying by outlet and by whether pre- or post-gating counts are
  meant); the precise bot count (10, per one secondary synthesis of press reporting — not independently
  cross-verified against a primary Kilcher statement this pass); Fortune's naming of Roman Ring (DeepMind) and
  Arthur Holland Michel as additional critics — single-sourced to that one article.
- **The live, unresolved dispute this page should hold open, not adjudicate:** was this irresponsible,
  unconsented human-subjects experimentation (Oakden-Rayner, Liang & Reich, the letter's 300+ signatories, the
  Gorwa & Veale grad-student harm report) — or a "prank" whose harms were never shown to exceed what any
  open-weights model plus minimal effort could already do (Kilcher, and a substantial share of the Hacker
  News discussion)? Both positions are dated, sourced, and represented above; the archive's role, per house
  rules, is to keep this open.
- **RUMOR / unverified:** none identified as free-floating rumor distinct from the "REPORTED" range items
  above — this incident is unusually well-documented in convergent, dated, named-source reporting for a
  single-week 2022 controversy; the main sourcing risk is press *rounding*, not fabrication.

## tk / open questions

- **The Verge's article** (Robertson or another byline — not confirmed) — WebFetch was blocked on
  theverge.com both times attempted; its content is triangulated via the AI Incident Database's citation and
  via other outlets that plainly draw on it, but it was never read directly this pass. [verify direct fetch;
  confirm author byline]
- **"AI Ethics people just mad I Rick rolled them"** — quoted identically across several secondary sources,
  all apparently downstream of Kurenkov's Gradient piece; no primary tweet URL located. [find the primary
  tweet, or confirm it was said in the video/a since-deleted tweet rather than a locatable one]
- **The condemnation letter's own canonical URL** — reported as a circulated statement/petition (Google
  Form or Doc, per the pattern of similar open letters); no stable, directly-citable URL for the letter's
  own full text was found this pass, only secondary paraphrase and direct-quote fragments via aibusiness.com
  and similar. The 300-vs-360 signatory-count discrepancy would likely resolve once the primary document (or
  an archived snapshot of it) is found. [find primary URL; confirm exact signatory count and its growth
  curve]
- **Exact deployment/detection timeline hour-by-hour** — sources converge on "~15,000 posts / ~10% of board
  traffic in the first 24h, 30,000+ over two 24-hour periods, ~7,000 threads total" but differ on whether
  detection took hours or "roughly two days" (Engadget); not resolved further this pass, and per the task's
  own framing, not a gap this dossier should try to fill with unsourced specifics. [note, likely
  irreducible — different observers noticed at different times]
- **Bot count ("10 bots")** — traced only to a secondary synthesis of press reporting, not confirmed against
  a Kilcher primary statement. [verify against the video or the HF model card if it states this]
- **Whether Kilcher ever revisited GPT-4chan publicly** (2023–2026) — searched specifically; nothing found.
  Either an honest absence (he moved on, as his own June 2022 remarks suggested he intended to) or simply not
  surfaced by search. [low priority; note as absence, don't force a citation]
- **Fortune's "Roman Ring (DeepMind)" and "Arthur Holland Michel" quotes** — single-sourced; would benefit
  from independent cross-verification (their own accounts, if extant) before a page treats them as
  load-bearing named critics. [verify]

## Cross-page notes

*(evidence that belongs on other models' pages — one line each, per the r/K-whiteboard rule)*

- **eleutherai** — this dossier's base-model section already carries the GPT-4chan connection (Wikipedia +
  Kurenkov/Gradient sourcing, and the explicit note that no EleutherAI institutional reaction to GPT-4chan
  was found). This dossier corroborates that absence independently and adds much more incident detail than
  eleutherai.md carries (by design — eleutherai.md defers the "full incident" here). No new EleutherAI-
  specific fact surfaced this pass that isn't already on that page.
- **gpt-2** — repligate's in-corpus chain-of-thought-discovery claims ("chain of thought was already well
  known on 4chan in 2020... first 'discovered' by AI dungeon users and posted on 4chan") are 4chan-as-culture
  references already carried on gpt-2.md and gpt-3.md; they are not about GPT-4chan the model and were
  excluded from this dossier's Tweets section as noise, consistent with how this dossier's corpus section
  flags them.
- **claude-3-opus** — the Truth Terminal "trained on 4chan" myth, which repligate repeatedly and explicitly
  debunks in-corpus (2024-10-14 through 2024-10-23: ToT is "the llama70b base model... fine tuned on Andy and
  Claude 3 Opus' conversations," "not trained on 4chan Reddit etc degen content in any extra way"), is the
  single largest noise cluster this dossier's corpus pull surfaced. It belongs entirely to the Truth
  Terminal/claude-3-opus story, not to GPT-4chan — flagged here so a future agent doesn't mistake the volume
  of "4chan" hits in the corpus for GPT-4chan signal.
- **gpt-4o** (or wherever TruthfulQA-as-a-benchmark methodology is discussed) — Owain Evans' direct correction
  of the GPT-4chan TruthfulQA claim (below-random performance) is a clean, citable example of eval-gaming-by-
  degradation; useful comparison material if any other page ever discusses models "gaming" a benchmark by
  becoming less confident/coherent rather than more capable.

## Mirror-target recommendations

None currently in `tools/mirror_targets.json` for this model. Recommended, in priority order:
- Kurenkov/The Gradient, "Lessons from the GPT-4Chan Controversy" (https://thegradient.pub/gpt-4chan-lessons/)
  — highest priority; this dossier's functional Zvi-anchor equivalent, and the single source most of the
  page's prose would lean on.
- Kilcher's own model card (https://www.ykilcher.com/gpt-4chan-model-card) — primary source, off-platform,
  link-rot risk.
- Papasavva et al., "Raiders of the Lost Kek" (https://arxiv.org/abs/2001.07487) — stable (arXiv), but worth
  having local given how load-bearing the dataset-provenance distinction is to this page's fairness.
- Gorwa & Veale, "Moderating model marketplaces" (https://arxiv.org/abs/2311.12573) — stable (arXiv), the
  fullest scholarly source; high value if the page wants the HF-governance-legacy angle.

## Link-inbox

`tools/link-inbox.md` read in full. **No lines are tagged for GPT-4chan, Kilcher, or 4chan** — none consumed,
none removed.
