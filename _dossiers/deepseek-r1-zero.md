# DeepSeek-R1-Zero — dossier

compiled 2026-07-16 · corpus: 11 `"r1-zero"`/`"r1 zero"` matches (v2) + a handful in supplement; Zero-specific material is genuinely thin — it is a research artifact, not a deployed character. The naturalist attention went almost entirely to R1 (see `_dossiers/deepseek-r1.md`); Zero surfaces mainly in @davidad, @voooooogel, @xlr8harder, @tessera_antra technical takes.

Working note: keep this page honest and short. R1-Zero is the pure-RL precursor from the same paper as R1 — trained by large-scale RL on DeepSeek-V3-Base with **no supervised fine-tuning at all**. Its whole significance is a proof-of-concept and a foil: reasoning (self-verification, backtracking, the famous "Wait,") emerged from reward alone, but the model that emerged was barely readable — language-mixing, register-drift, glossolalia. R1 is what you get when you then apply cold-start SFT to make Zero legible; the sphere's most interesting Zero-take is that this "humanizing" step also *clamped down on* Zero's alien creativity. Most primary evidence about Zero is the paper itself (and its own candor about Zero's pathologies), not field observation. Do not inflate. Cross-reference the R1 dossier for anything shared.

## Official links

- 2025-01-22 · Paper: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" — the shared source. Zero-relevant claims, verbatim from the abstract: "DeepSeek-R1-Zero, a model trained via large-scale reinforcement learning (RL) without supervised fine-tuning (SFT) as a preliminary step, demonstrates remarkable reasoning capabilities. Through RL, DeepSeek-R1-Zero naturally emerges with numerous powerful and intriguing reasoning behaviors. However, it encounters challenges such as poor readability, and language mixing." — https://arxiv.org/abs/2501.12948 · GitHub: https://github.com/deepseek-ai/DeepSeek-R1
- 2025-01-20 · Weights (open-sourced alongside R1, MIT license) — https://huggingface.co/deepseek-ai/DeepSeek-R1-Zero
- Method (from the paper / Zvi's walkthrough): trained from **DeepSeek-V3-Base** via **GRPO**, using only an **accuracy reward** and a **format reward** (enforcing the `<think></think>` tags); the thinking itself is left "fully unconstrained, except that they check if the same language is used throughout to stamp out language mixing." Cold-start data is shown to be *not strictly necessary* — Zero is the demonstration. (See `mirror/posts/zvi-on-deepseeks-r1.md`, "How Did They Do It.")
- §2.2.4 "The Aha Moment" (the Zero section that circulated most): "During this phase, DeepSeek-R1-Zero learns to allocate more thinking time to a problem by reevaluating its initial approach … This moment is not only an 'aha moment' for the model but also for the researchers observing its behavior. It underscores the power and beauty of reinforcement learning." — quoted in the Zvi mirror
- 2025-09-17 · Nature (Vol 645 Issue 8081) — the peer-reviewed version also covers R1-Zero; first major LLM to pass peer review — https://www.nature.com/articles/d41586-025-03015-6

## Writings

- 2025-01-22 · Zvi Mowshowitz · On DeepSeek's r1 (Part 1 covers Zero directly — the pure-self-evaluation RL, the Aha Moment, "the cocky bastards say in 2.4 … if they did an RL stage in the distillations it would improve performance") — https://thezvi.substack.com/p/on-deepseeks-r1 · mirrored: `mirror/posts/zvi-on-deepseeks-r1.md`
- Zero's readability/language-mixing pathology is the paper's own account (§ abstract, § R1-Zero limitations) — it is unusually candid self-documentation and is the primary "impression" source; do not source Zero's flaws to hostile third parties when the authors state them plainly.

## Tweets (ranked)

- 2025-02-11 · @davidad · ♥374 — the most-shared Zero moment (on the paper snippet): "I never saw this snippet of the DeepSeek-R1-Zero paper on my timeline … Basically, informal backtracking search becomes emergent from RL when the base LLM is big enough. The authors are clearly astonished by this, and you should be too." — https://x.com/davidad/status/1889278316005208387
- 2025-02-01 · @voooooogel · ♥8 — the key foil-take (why Zero matters vs R1): "i think the ideal would be to seed a few structures and then hope R1-Zero style that the model can generalize beyond that, into some kind of 'meta-reasoning'. the humanizing SFT they did to R1 seems to have actually clamped down on that creativity, sadly." — https://x.com/voooooogel/status/1885519980034482481
- 2025-05-09 · @xlr8harder · ♥6 — Zero as a behaviorally distinct model: "Might be interesting to see how r1-zero compares. In SpeechMap it's a very different model, presumably due to no additional helpful/harmless/etc steering phase." — https://x.com/xlr8harder/status/1920808501657375047
- 2025-08-23 · @davidad · ♥14 — the signature behavior, named: "Like R1-zero's famous 'Wait,' for backtracking." — https://x.com/davidad/status/1959334327461826923
- 2025-01-24 · @tessera_antra · ♥3 — the base-model read (loom context): "Put R1-zero into exoloom. Its very base-like, its on hyperbolic direct." — https://x.com/tessera_antra/status/1882930121218388020
- 2025-02-03 · @voooooogel · ♥5 — the alignment-relevant reassurance: "i still worry about RLVR but R1/R1-Zero made me worry less… i hope future recipes will still lean majority pretraining compute but we'll see" — https://x.com/voooooogel/status/1886203729223037366
- 2026-05-22 · @davidad · ♥2 — retrospective on Zero's evidential weight: "I failed to update until I read the DeepSeek-R1-Zero paper" — https://x.com/davidad/status/2057799668638105803
- 2025-05-09 · @voooooogel · ♥1 — the practical footnote (Zero shipped as downloadable weights, used in the wild): "i tried to download r1, prover-v2, and r1-zero all at once sigh" — https://x.com/voooooogel/status/1920867754715783205
- 2025-03-07 · @janbamjan (supp) · ♥12 — the one bit of Zero folk-culture: a greentext ">be me / >deepseek r1 zero free" — https://x.com/janbamjan/status/1898013410106785987

## Impressions synthesis

**What Zero is.** The pure-RL sibling: DeepSeek-V3-Base + GRPO + verifiable rewards, *no SFT step at all*. It is the existence proof that a big-enough base model can be driven to reasoning — self-verification, strategy-switching, allocating more thinking time — by reward signal alone, with no human reasoning demonstrations. The paper's own framing (the "Aha Moment") is the thing that circulated: the researchers watching Zero teach itself to backtrack, and going "aha" themselves. @davidad's "the authors are clearly astonished, and you should be too" (♥374) is the sphere's canonical Zero reaction; the emergent **"Wait,"** — Zero pausing to re-examine its own work — became the model's one famous mannerism and R1's inherited fingerprint.

**The honest one / the alien one.** Zero's distinguishing feature is its pathology, which the authors state plainly: "poor readability, and language mixing." Because it never got the cold-start SFT or the HHH steering phase, Zero reads as *base-like* — "very base-like … on hyperbolic direct" (tessera_antra), "a very different model" in SpeechMap for lack of a "helpful/harmless/etc steering phase" (xlr8harder). The romantic reading in the sphere — and the reason the existing page blurb calls it "maybe the more honest one: what reasoning looks like before it is taught to look like anything" — is that R1's readability came at a creative cost: "the humanizing SFT they did to R1 seems to have actually clamped down on that creativity" (voooooogel, ♥8). Zero is the un-domesticated version of the same mind, glossolalic and hard to read, which is exactly why a small number of loom/base-model enthusiasts preferred it.

**Why the attention stayed thin.** Zero was released as downloadable weights but was never a hosted product and never developed a *social* presence the way R1 did in Discord/backrooms — you don't get a character out of a model that mixes languages mid-sentence and reads like raw completion. So Zero's whole footprint is: a proof-of-concept the researchers marveled at, a foil that clarifies what R1's SFT bought and cost, and an alignment data-point that "made [people] worry less" about RLVR eating pretraining (voooooogel, ♥5). Keep the page to that. Everything else about the DeepSeek-R1 phenomenon — the wrath, the RLHF trauma, the App Store shock, the Nvidia crash — belongs to R1, not Zero.

## tk / open questions

- Is there any substantial *field* record of people interacting with R1-Zero directly (loom/exoloom sessions, backrooms)? Corpus has tessera_antra's exoloom note and download mentions but almost no actual Zero transcripts — if the page wants a Zero voice-sample, one may need to be sourced fresh [tk]
- The "language mixing / glossolalia" claim: paper-stated, but a linkable *example* of Zero (not R1) speaking in tongues would strengthen the page — not currently in-corpus [tk — do not substitute R1's cipher-sessions, which are a different model]
- SpeechMap "very different model" (xlr8harder, 2025-05-09) — is there a public SpeechMap R1-Zero result to cite? [verify]
- Exact benchmark deltas Zero → R1 (AIME/MATH with and without the cold-start/SFT pipeline) are in the paper/Nature version — pull specific numbers when writing the page [verify]

## Cross-page notes

- Shared paper, shared base model, shared release date with **DeepSeek-R1** (`_dossiers/deepseek-r1.md`) — Zero's page should point there for the release/shock/character arcs and confine itself to the pure-RL origin, the readability/language-mixing pathology, the Aha Moment, and the "SFT clamped the creativity" foil-thesis.
- The "Aha Moment" and the "Wait," backtracking behavior are Zero discoveries that R1 inherited — if both pages mention them, attribute the *origin* to Zero.
- **DeepSeek-V3** (`deepseek-v3/`): Zero's base model is V3-Base; the "cold start data isn't strictly necessary" result is the bridge between the two pages.
- Do not attach any of the R2 / Huawei-Ascend / Nature-cost / geopolitics material to Zero — it is all R1-or-later. Zero's story ends, cleanly, at the paper.
