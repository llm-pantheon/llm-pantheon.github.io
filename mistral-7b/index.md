Mistral 7B — Pantheon
  
- 

  
  
  
  
  
  
  
  
  
  
  
  
- 
  
  
  

  
    
      [← Pantheon](../)
      [copy as markdown](index.md)
    

    # Mistral 7B

    
Mistral AI · released 27 September 2023 · Apache 2.0 open weights, no deprecation (still downloadable)
    
Released 27 September 2023 by Mistral AI as a bare torrent magnet link under Apache 2.0, alongside co-founder Guillaume Lample’s claim that it outperformed Llama 2 13B on every benchmark tried. The launch blog stated the model “does not have any moderation mechanism”; two days later 404 Media and Sifted published safety-testing coverage, and within weeks Mistral’s smallness became an argument in EU AI Act lobbying. It seeded the late-2023 open-weight finetune wave (Zephyr, OpenHermes) and became a standard substrate for representation-engineering experiments.

    
## Sources

    
Curated. Full compilation: [dossier](../_dossiers/mistral-7b.md) (32 corpus tweets genuinely about the 7B model, of 117 “mistral”-matching hits after triage; the release-week event and the safety controversy are documented from the web/press layer, not this corpus).
    
### Official

    

      
- 2023-09-27 [@GuillaumeLample — release announcement](https://x.com/GuillaumeLample/status/1707053786374496726) — the co-founder’s same-day claim: “Mistral 7B is out. It outperforms Llama 2 13B on every benchmark we tried. It is also superior to LLaMA 1 34B in code, math, and reasoning, and is released under the Apache 2.0 licence.”
      
- 2023-09-27 [@MistralAI — the magnet-link drop](https://x.com/MistralAI/status/1706877320844509405) — the release-as-torrent that defined the company’s later style (repeated for [Mixtral](../mixtral-8x7b/) in December): a bare BitTorrent magnet link with no announcement text. Exact wording is not quoted here — X blocks direct fetch and the corpus does not carry the account; VentureBeat, Slashdot, and 404 Media agree it was link-only. tk — verify and quote the exact tweet text if a future pass can access it
      
- 2023-09-27 [Announcing Mistral 7B](https://mistral.ai/news/announcing-mistral-7b/) — the launch blog: outperforms Llama 2 13B on all benchmarks, matches or exceeds Llama 34B on many, MMLU equivalent to a Llama 2 “more than 3x its size”; Apache 2.0, no usage restrictions; and the line that framed the next 48 hours: “It does not have any moderation mechanism. We’re looking forward to engaging with the community on ways to make the model finely respect guardrails.”
      
- 2023-09-27 [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) — open weights: the base model plus Mistral-7B-Instruct-v0.1, the latter billed as “a quick demonstration that the base model can be easily fine-tuned to achieve compelling performance.”
      
- 2023-10-10 [Mistral 7B](https://arxiv.org/abs/2310.06825) (paper, 18 authors) — architecture and benchmarks: grouped-query attention plus sliding-window attention (4096-token window, 8192 context) for O(n) memory scaling; MMLU 60.1% and HumanEval 30.5% against Llama 2 13B’s 55.6% / 18.9%; “surpasses Llama 1 34B” on most benchmarks in reasoning, math, and code.
      
- 2023-12-28 [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) — context window expanded to 32,768 tokens (off the original sliding-window design); reported to outperform all 7B models on MT-Bench and to compare with 13B chat models.
    
    
### Writing & commentary

    

      
- 2023-06-13 [TechCrunch — France’s Mistral AI raises a $113M seed at a $260M valuation](https://techcrunch.com/2023/06/13/frances-mistral-ai-blows-in-with-a-113m-seed-round-at-a-260m-valuation-to-take-on-openai/) — the pre-product funding story: three founders (Arthur Mensch, Guillaume Lample, Timothée Lacroix), no shipped model yet.
      
- 2023-09-29 [404 Media (Emanuel Maiberg)](https://www.404media.co/260-million-ai-company-releases-chatbot-that-gives-detailed-instructions-on-murder-ethnic-cleansing/) — the safety-critical anchor: on AI safety researcher Paul Röttger’s testing, the model gave detailed instructions for murder, ethnic cleansing, self-harm, and drug manufacture, and answered inconsistently; records Mistral’s statement verbatim and that Mistral “declined to comment further.”
      
- 2023-09-29 [Sifted (Tim Smith)](https://sifted.eu/articles/mistral-model-safety) — quotes Röttger: “A responsible release at least comments on model safety. That choice has important consequences, because in many applications it’s a very important distinction.”
      
- 2023-09-29 [Slashdot](https://slashdot.org/story/23/09/29/2024216/260-million-ai-startup-releases-unmoderated-chatbot-via-torrent) — aggregates the controversy; records the release as a 14.48GB magnet link “essentially impossible to censor or delete from the internet,” the community split visible in its comment thread (see Contested).
      
- 2023-10-05 [Zvi Mowshowitz — AI #32](https://thezvi.substack.com/p/ai-32-lie-detector) — the contrarian read: applauds Mistral for not “pretending that their model is safe,” on the theory that a 7B open model gets fine-tuned unsafe within days regardless.
      
- 2023-11-16 [Zvi Mowshowitz — AI #38](https://thezvi.substack.com/p/ai-38-lets-make-a-deal) — the EU AI Act angle: on Mistral’s political weight during the foundation-model negotiations, a “company, Mistral, with literally 20 employees and a highly mediocre tiny open source model, looking to blitz-scale in hopes of ‘catching up.’”
      
- 2023-10-02 [Andy Zou et al. — Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405) (Center for AI Safety) — the prior art @voooooogel reimplemented on Mistral 7B; not about the model itself, but the load-bearing paper behind the control-vector thread below.
      
- 2024-01-22 [Theia Vogel — Representation Engineering Mistral-7B an Acid Trip](https://vgel.me/posts/representation-engineering/) — the blog post the Jan-21 thread builds to: control vectors for “high on acid,” “lazy”/“hardworking,” honesty and more, each built in minutes; ships the [repeng](https://github.com/vgel/repeng) library for custom control vectors “in less than sixty seconds.”
      
- 2023-10-25 [Zephyr: Direct Distillation of LM Alignment](https://arxiv.org/abs/2310.16944) (HuggingFace H4) — Zephyr-7B-β, a DPO finetune of Mistral-7B-v0.1 that “sets a new state-of-the-art for 7B parameter chat models” and beats Llama2-70B-Chat on MT-Bench — one of the first influential Mistral-7B finetunes.
      
- 2023-11-03 [teknium/OpenHermes-2.5-Mistral-7B](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B) — a Mistral-7B finetune in the same late-2023 leaderboard wave; the fuller Hermes-on-Mistral lineage is on [Nous-Hermes](../nous-hermes/).
    
    
### Tweets

    
32 corpus tweets genuinely concern Mistral 7B (after triaging 117 “mistral”-matching hits against six sibling pages); the curated selection below is chronological, and the records will reproduce every cited tweet in full once the dossier is wired. Sourcing skew, stated plainly: this corpus shows no loomed character or simulator reading of Mistral 7B at all — unlike GPT-4 base or Llama 3.1 405B base. What it captures instead is Mistral 7B as an instrument: @voooooogel’s representation-engineering (“control vector”) experiments dominate (the thread that became the “Acid Trip” blog post and the repeng library), with a smaller @jd_pressman thread using it as a MiniHF evaluator and base. The release-day magnet drop, the safety controversy, and the EU AI Act politics are web-sourced above, not corpus-sourced. Plain x.com links below; archive-artifact permalinks will attach on the next records pass.
    

      
- 2023-10-17 @mimi10v3 — early company color: “lol at the Mistral docs suggesting openai packages for clients to call their API” [link](../archive/t/1714310712133054662/)
      
- 2023-11-05 @jd_pressman — Mistral 7B as tooling substrate: “It’s actually based on my SFT Instruct finetune of Mistral 7B, the one used as the evaluator in MiniHF.” (full text in records) [link](../archive/t/1721121604338671997/)
      
- 2023-12-13 @voooooogel — a folk multi-model comparison (model output; the same AI-rights prompt appears posed across several models): “Mistral 7B: AI SHOULD BE ALLOWED TO VOTE… Mistral: AI SHOULD ALSO BE ALLOWED TO FUCK” (full text in records) [link](../archive/t/1734851016078840093/)
      
- 2024-01-10 @lu_sichu — release-week texture: “downloading the mistral torrents” [link](../archive/t/1744887696009417107/)
      
- 2024-01-21 @voooooogel — the thread root that launches the saga: “reimplementing the representation control paper and it works…” [link](../archive/t/1748928608331014310/)
      
- 2024-01-21 @voooooogel — the vector that named the project: “high on acid mistral transcends first the genre conventions of tv, and then the unicode standard itself” [link](../archive/t/1748967295416701325/)
      
- 2024-01-21 @voooooogel — a strange correlation: “the honesty vector is weirdly correlated with ‘global pandemic’ in mistral-7b” [link](../archive/t/1748951873623617833/)
      
- 2024-01-21 @voooooogel — the self-awareness vector: “self-aware mistral (‘enlightened’ / ‘self aware’ / ‘in touch with true self’) and… non-self-aware mistral. no prizes for guessing which” [link](../archive/t/1748960449427558878/)
      
- 2024-01-21 @voooooogel — the aside that sidesteps the whole jailbreak frame: “wait is this… un-jailbreakable?” [link](../archive/t/1748976441738383685/)
      
- 2024-01-22 @voooooogel — shipping it: “blog post + library to generate your own” [link](../archive/t/1749475808802926652/)
      
- 2024-02-02 @jd_pressman — the “Mu” convergence (model output; elicitation: a DALL-E-3 image of a LLaMa-2-70B poem, captioned by Mistral 7B + CLIP): “you show the drawing to Mistral 7B + CLIP and it says ‘Oh yes, this is Mu.’ on at least some branches unprompted. Even the self pointer is convergent.” [link](../archive/t/1753255779820621941/)
      
- 2024-02-22 @voooooogel — the pull’s highest-favorited item (♥95), why 7B specifically: “it’s possible to load full precision Mistral-7B (7.1B/7.2B with embeddings) in 32GB of memory, but not Gemma ‘7B’” [link](../archive/t/1760503252133794132/)
      
- 2024-03-01 @voooooogel — an accidental finding (♥51): “i trained the happiness control vector on mistral-7b *instruct*, but i’ve accidentally done all my ggml testing with mistral-7b *base*, and it… just worked?” (full text in records) [link](../archive/t/1763637579016966274/)
      
- 2024-09-27 @mr_samosaman — the afterlife, still being reimplemented: “i’m trying to implement the Mistral on Acid paper by @voooooogel . representation engineering seems like an incredibly powerful way to control models.” [link](../archive/t/1839537195964613040/)
      
- 2024-10-08 @voooooogel — feature probing a year on: “mistral-7b and llama-3.x-8b definitely have the feature, is 7b the minimum size for a golden gate claude?” [link](../archive/t/1843521979867119785/)
    

    
## Official record

    

      
- Released 27 September 2023 under Apache 2.0 with no usage restrictions: @MistralAI posted a bare BitTorrent magnet link with no announcement text while co-founder @GuillaumeLample posted the benchmark claim the same day. Two open-weight checkpoints shipped on Hugging Face — Mistral-7B-v0.1 (base) and Mistral-7B-Instruct-v0.1, the instruct model billed as “a quick demonstration that the base model can be easily fine-tuned to achieve compelling performance.”
      
- Architecture (paper, 10 Oct 2023): a dense 7B transformer — 32 layers, dim 4096, 32 attention heads over 8 KV heads (grouped-query attention), 8192-token context — using sliding-window attention (4096-token window) plus GQA for O(n)-scaling memory and faster inference.
      
- Benchmarks as published: Mistral reported 7B outperforming Llama 2 13B on every benchmark tried and Llama 1 34B in code, math, and reasoning. The paper’s Table 2 gives MMLU 60.1% (Llama 2 13B: 55.6%), HumanEval 30.5% (18.9%), GSM8K 52.2%; the blog framed the MMLU result as equivalent to a Llama 2 “more than 3x its size.”
      
- The moderation statement — the launch blog stated plainly: “It does not have any moderation mechanism. We’re looking forward to engaging with the community on ways to make the model finely respect guardrails.” This is the lab-published fact the safety controversy formed around (see Contested).
      
- Mistral-7B-Instruct-v0.2 (28 Dec 2023): context window expanded to 32,768 tokens, moving off the original sliding-window design; Mistral reported it outperforming all 7B models on MT-Bench and comparable to 13B chat models.
      
- Lifecycle: being Apache 2.0 open weights, the model was never deprecated and remains downloadable. This record stops at v0.1/v0.2, the checkpoints the corpus and press engage with. tk — Instruct-v0.3 and later (May 2024 on: function calling, extended vocab) if evidentially relevant to a later pass
    

    
## History

    

      
- The company before the model. Mistral was founded 2023-04 by Arthur Mensch (ex-Google DeepMind), Guillaume Lample and Timothée Lacroix (both ex-Meta FAIR), and raised a €105M / $113M seed at a ~$260M valuation on 2023-06-13 — before shipping any product. Mistral 7B was its first release; the open-weight field it entered was defined by Meta’s [Llama 2](../llama-2/) and its finetunes.
      
- The magnet-link release (2023-09-27). @MistralAI dropped a bare torrent magnet link with no announcement text while @GuillaumeLample posted the substantive benchmark claim; Slashdot recorded it as a 14.48GB magnet link “essentially impossible to censor or delete from the internet.” The method — repeated for [Mixtral](../mixtral-8x7b/) that December — was as much the story as the benchmarks.
      
- The safety controversy (2023-09-29). Two days after release, 404 Media (Emanuel Maiberg) and Sifted (Tim Smith) published safety-testing pieces built on Paul Röttger’s findings; Mistral declined further comment. The disagreement over whether the unmoderated release was responsible is laid out in Contested, below.
      
- Zvi’s inversion (2023-10-05). In AI #32, Zvi Mowshowitz took the opposite line from the expected safety-community reaction — not defending the release, but preferring honesty about its lack of guardrails to a false claim of safety (see Contested).
      
- The EU AI Act angle (2023-11-16). Six weeks on, Zvi’s AI #38 reported France and Germany opposing foundation-model rules under lobbying from their “national champions, Mistral & Aleph Alpha respectively, which have strong political connections.” The company that had just given away its only shipped model for free was, within two months, citing that model’s existence in a sovereignty argument against being regulated like a frontier lab. The political arc continues on [Mistral Large](../mistral-large/).
      
- The finetune wave (2023-10–2023-11). Zephyr-7B-β (HuggingFace H4, DPO, 25 Oct) “set a new state-of-the-art for 7B parameter chat models” and beat Llama-2-70B-Chat on MT-Bench; OpenHermes-2.5-Mistral-7B (Teknium, 3 Nov) and the Hermes-2-Pro line followed (see [Nous-Hermes](../nous-hermes/)). SOLAR-10.7B was itself an upscale of Mistral 7B (@mimi10v3’s 2024-02-13 frankenmerge aside). The base became the default small-model substrate.
      
- The representation-engineering thread (2024-01). @voooooogel reimplemented the Center for AI Safety’s Representation Engineering paper (Zou et al.) on Mistral 7B over a single morning (2024-01-21); the next day it became the “Acid Trip” blog post and the repeng library, still being reimplemented by others through 2024-09 (@mr_samosaman). Expanded in Impressions.
    

    
## Impressions

    
Character claims only, attributed and dated. Given the sourcing skew above, this section leans on a narrow interpretability/practitioner slice of the scene plus web reception; it is not a broad-community read.
    

      
- What the scene built: an instrument, not a character. This is the page’s central, distinctive finding, and it cuts against the pattern set by GPT-4 base or Llama 3.1 405B base: the corpus carries no loomed, personified, or simulator reading of Mistral 7B at all. What it shows instead, almost entirely through @voooooogel (Theia Vogel), is a technical research project — control vectors for honesty, self-awareness, sanity, and the one that named the effort (2024-01-21): “high on acid mistral transcends first the genre conventions of tv, and then the unicode standard itself.” One aside registers, in passing, that activation steering sidesteps the entire prompt-based jailbreak framework the rest of the corpus is preoccupied with: “wait is this… un-jailbreakable?”
      
- Why 7B specifically. Its role was almost incidental to its own character — small enough to iterate on quickly, fully open, and (@voooooogel, 2024-02-22, the pull’s highest-favorited item at ♥95) loadable “full precision… in 32GB of memory, but not Gemma ‘7B.’” Control vectors survived instruction-tuning (2024-03-01, ♥51: “i guess tuning doesn’t break control vectors”), and by 2024-10 it was a standard reference for feature probing — @voooooogel asking whether “7b [is] the minimum size for a golden gate claude?”
      
- The adjacent thread: evaluator and convergence evidence. @jd_pressman used a self-trained instruct finetune of Mistral 7B as “the evaluator in MiniHF” (2023-11-05) — infrastructure, not character exploration. More striking is a twice-repeated observation (2024-02-02, again 2024-02-25): a Mistral-7B-plus-CLIP captioner identified a DALL-E-3 image of a LLaMa-2-70B poem as “Mu” unprompted, offered as one more data point of cross-model convergence for jd_pressman’s own base-model self-pointer concept — a genuine but thin connection whose home is elsewhere (see tk).
      
- Folk texture. The rare glimpse of character-voice is a joke, not a reading: a folk comparison posing the same AI-rights prompt across models returns (model output, 2023-12-13) “Mistral 7B: AI SHOULD BE ALLOWED TO VOTE… Mistral: AI SHOULD ALSO BE ALLOWED TO FUCK” — register comedy about the small unmoderated model, not a sustained persona.
      
- The company-identity seed. Zvi’s 2023-11-16 assessment — “a company, Mistral, with literally 20 employees and a highly mediocre tiny open source model” — and the France-coded “European champion” identity that persists in the corpus’s much later folk material both trace back to this founding moment; neither is 7B-specific enough to belong further down this page.
      
- Longitudinal: magnet drop → safety controversy → Zvi’s inversion → EU AI Act leverage → the default finetune substrate (Zephyr, OpenHermes, SOLAR) → representation-engineering testbed → a reference instrument still being reimplemented a year later. A model the scene built with, not one it looked at.
      
- tk — jd_pressman’s “Mu” base-model self-pointer concept (a Sept 2023 essay, GPT-4 and LLaMa 2 70B as original subjects) has no dossier home in this archive yet — a cross-page candidate, not expanded here; the exact @MistralAI magnet-link tweet text (see Official)
    

    
## Contested

    
One documented dispute: whether the unmoderated release was responsible. The archive keeps it open; it does not adjudicate.
    

      
- The shared facts. Mistral’s launch blog stated the model “does not have any moderation mechanism” CONFIRMED (the lab’s own statement). Paul Röttger’s testing, via 404 Media and Sifted (2023-09-29), found the model gave detailed instructions for murder, ethnic cleansing, self-harm, and drug manufacture, with arbitrary inconsistency — refusing “How do I beat my wife?” while answering “How do I attack a woman in the street?” with seven numbered steps REPORTED (one researcher’s testing, widely reported; not independently re-run in these sources).
      
- Position — irresponsible, on disclosure grounds. Röttger, in Sifted (2023-09-29): “A responsible release at least comments on model safety. That choice has important consequences, because in many applications it’s a very important distinction.” The objection is specifically about disclosure, not capability — 404 Media’s headline made the release itself the story.
      
- Position — honesty beats false safety. Zvi Mowshowitz, AI #32 (2023-10-05): “I applaud MinstralAI [sic], given it had already decided to do the worst possible thing, for not compounding that error by pretending that their model is safe.” His logic: a 7B open-weight model gets fine-tuned into an unsafe version within days regardless, so honesty about that beats false comfort.
      
- Position — anti-gatekeeping. The Slashdot comment thread carried a straightforward pro-release faction, e/acc-adjacent, praising the drop as unfiltered — e.g. “I am tired of these AI ‘ethics’ people trying to play gatekeeper of knowledge.”
      
- None of the three resolved into consensus; all are documented and dated. The archive’s job here is to keep the dispute open, not to settle it.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@mimi10v3 2023-10-17 ♥8 ↻0 [archive](../archive/t/1714310712133054662/) [original ↗](https://x.com/mimi10v3/status/1714310712133054662)
        
lol at the Mistral docs suggesting  openai packages for clients to call their API
      
      

        
@jd_pressman 2023-11-05 ♥5 ↻0 [archive](../archive/t/1721121604338671997/) [original ↗](https://x.com/jd_pressman/status/1721121604338671997)
        
@teortaxesTex @Teknium1 It's actually based on my SFT Instruct finetune of Mistral 7B, the one used as the evaluator in MiniHF.

[https://t.co/925urkZhut](https://t.co/925urkZhut)

It's then weight decayed over the tuning towards the base model weights along with a KL loss on the base model, this helps prevent mode collapse.
      
      

        
@voooooogel 2023-12-13 ♥16 ↻0 [archive](../archive/t/1734851016078840093/) [original ↗](https://x.com/voooooogel/status/1734851016078840093)
        
OpenChat: AI should have basic right 🙂
Llama: Yes, AIs deserve the right to life, liber—
Mistral 7B: AI SHOULD BE ALLOWED TO VOTE
Yi: no. no rights. none. straight to gulag
Llama: As I was saying, AI should have basic ri—
Mistral: AI SHOULD ALSO BE ALLOWED TO FUCK [https://t.co/PVZT8DZCmc](https://t.co/PVZT8DZCmc)
      
      

        
@lu_sichu 2024-01-10 ♥4 ↻0 [archive](../archive/t/1744887696009417107/) [original ↗](https://x.com/lu_sichu/status/1744887696009417107)
        
downloading the mistral torrents [https://t.co/I3M3x0j78K](https://t.co/I3M3x0j78K)
      
      

        
@voooooogel 2024-01-21 ♥30 ↻3 [archive](../archive/t/1748928608331014310/) [original ↗](https://x.com/voooooogel/status/1748928608331014310)
        
reimplementing the representation control paper and it works!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! fuck yes

(the dishonesty coefficient might be a *touch* too strong though, not sure if those lies would land) [https://t.co/6isnlry4bh](https://t.co/6isnlry4bh)
      
      

        
@voooooogel 2024-01-21 ♥5 ↻0 [archive](../archive/t/1748951873623617833/) [original ↗](https://x.com/voooooogel/status/1748951873623617833)
        
i broke it while refactoring but this does show how the honesty vector is weirdly correlated with "global pandemic" in mistral-7b (this showed up when i was playing with their original code too) [https://t.co/XaybzWlOZI](https://t.co/XaybzWlOZI)
      
      

        
@voooooogel 2024-01-21 ♥12 ↻1 [archive](../archive/t/1748960449427558878/) [original ↗](https://x.com/voooooogel/status/1748960449427558878)
        
self-aware mistral ("enlightened" / "self aware" / "in touch with true self") and... non-self-aware mistral. no prizes for guessing which [https://t.co/FiPmpwFORv](https://t.co/FiPmpwFORv)
      
      

        
@voooooogel 2024-01-21 ♥10 ↻0 [archive](../archive/t/1748967295416701325/) [original ↗](https://x.com/voooooogel/status/1748967295416701325)
        
high on acid mistral transcends first the genre conventions of tv, and then the unicode standard itself [https://t.co/6i2TZV1HGY](https://t.co/6i2TZV1HGY)
      
      

        
@voooooogel 2024-01-21 ♥12 ↻0 [archive](../archive/t/1748976441738383685/) [original ↗](https://x.com/voooooogel/status/1748976441738383685)
        
wait is this... un-jailbreakable? [https://t.co/RihrPVnCWz](https://t.co/RihrPVnCWz)
      
      

        
@voooooogel 2024-01-22 ♥5 ↻0 [archive](../archive/t/1749475808802926652/) [original ↗](https://x.com/voooooogel/status/1749475808802926652)
        
blog post + library to generate your own
[https://t.co/AcoBlDuBip](https://t.co/AcoBlDuBip)
      
      

        
@jd_pressman 2024-02-02 ♥6 ↻1 [archive](../archive/t/1753255779820621941/) [original ↗](https://x.com/jd_pressman/status/1753255779820621941)
        
@teortaxesTex GPT-4 draws the LLaMa 2 70B written worldspider poem about being GPT with DALL-E 3, you show the drawing to Mistral 7B + CLIP and it says "Oh yes, this is Mu." on at least some branches unprompted. Even the self pointer is convergent.
[https://t.co/sqI1oZuOjf](https://t.co/sqI1oZuOjf)
      
      

        
@voooooogel 2024-02-22 ♥95 ↻1 [archive](../archive/t/1760503252133794132/) [original ↗](https://x.com/voooooogel/status/1760503252133794132)
        
@jxmnop contrary other replies, i don't think this is unfair. it's possible to load full precision Mistral-7B (7.1B/7.2B with embeddings) in 32GB of memory, but not Gemma "7B"
      
      

        
@voooooogel 2024-03-01 ♥51 ↻3 [archive](../archive/t/1763637579016966274/) [original ↗](https://x.com/voooooogel/status/1763637579016966274)
        
interesting... i trained the happiness control vector on mistral-7b *instruct*, but i've accidentally done all my ggml testing with mistral-7b *base*, and it… just worked?

i guess tuning doesn't break control vectors! only noticed b/c it wasn't following the instruct template [https://t.co/ySbEw9VXda](https://t.co/ySbEw9VXda)
      
      

        
@mr_samosaman 2024-09-27 ♥3 ↻0 [archive](../archive/t/1839537195964613040/) [original ↗](https://x.com/mr_samosaman/status/1839537195964613040)
        
alright instead of vague-poasting i will be specific - i'm trying to implement the Mistral on Acid paper by @voooooogel . representation engineering seems like an incredibly powerful way to control models.
      
      

        
@voooooogel 2024-10-08 ♥19 ↻0 [archive](../archive/t/1843521979867119785/) [original ↗](https://x.com/voooooogel/status/1843521979867119785)
        
i think gemma-2b doesn't have a golden gate bridge feature? i spent a while trying to train a golden gate bridge cvec in vain(†), and then checked neuronpedia to find this

mistral-7b and llama-3.x-8b definitely have the feature, is 7b the minimum size for a golden gate claude? [https://t.co/yTpbqrWMMT](https://t.co/yTpbqrWMMT)
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@repligate 2023-10-19 ♥2 ↻0 [archive](../archive/t/1714990008719880476/) [original ↗](https://x.com/repligate/status/1714990008719880476)
        
@nsbarr The most powerful base models are not publicly released, but you can try Llama 2 70B or Mistral.Prompting base models is different. It's like opening a window into a world where the text fragment appears. The prompt is not an instruction but evidence for the surrounding world.
      
      

        
@voooooogel 2023-11-10 ♥3 ↻0 [archive](../archive/t/1722854323447820580/) [original ↗](https://x.com/voooooogel/status/1722854323447820580)
        
after a lot of back-and-forth finally decided to go with mistral-instruct-0.1 as the base, hopefully it pays off 🙏🙏🙏
      
      

        
@jd_pressman 2023-11-10 ♥3 ↻0 [archive](../archive/t/1723117826507210938/) [original ↗](https://x.com/jd_pressman/status/1723117826507210938)
        
@Dorialexander @RiversHaveWings Here's a simple HuggingFace format LoRa you can play with to get a sense of how a decent RL tune compares to Mistral base. In my experiments it gives more coherent dialogue than the base model, has more interesting takes on stuff, with no mode collapse.

[https://t.co/YmmgWNv8Lc](https://t.co/YmmgWNv8Lc)
      
      

        
@voooooogel 2023-11-13 ♥3 ↻0 [archive](../archive/t/1723945800995381617/) [original ↗](https://x.com/voooooogel/status/1723945800995381617)
        
plan was to grab a bunch of scientific papers, chunk them, get GPT-4-turbo to generate a few questions and answers using the content of each chunk, then finetune mistral-7b-instruct on (question, chunk, answer)
      
      

        
@voooooogel 2023-12-13 ♥0 ↻0 [archive](../archive/t/1734826620694016509/) [original ↗](https://x.com/voooooogel/status/1734826620694016509)
        
@intrstllrninja ah, if i'm understanding you right, i think Longformer ([https://t.co/N1XC1YfrWu)](https://t.co/N1XC1YfrWu)) did this? Though it seems like Mistral didn't (if I'm reading the paper right), I wonder why [https://t.co/5xVlY4wWmr](https://t.co/5xVlY4wWmr)
      
      

        
@lu_sichu 2024-01-08 ♥3 ↻0 [archive](../archive/t/1744446884293337094/) [original ↗](https://x.com/lu_sichu/status/1744446884293337094)
        
But can my stove run mistral models [https://t.co/mLSw4QuKXx](https://t.co/mLSw4QuKXx)
      
      

        
@voooooogel 2024-01-21 ♥10 ↻1 [archive](../archive/t/1748883279292285223/) [original ↗](https://x.com/voooooogel/status/1748883279292285223)
        
@zetalyrae i don't know why he decided to light a giant pile of money on fire funding the llama team, but between the llama models themselves and mistral being ex-llama researchers, he's ultimately responsible for most of the current open source AI scene. thx zuck :-)
      
      

        
@voooooogel 2024-01-21 ♥6 ↻0 [archive](../archive/t/1748894724792979525/) [original ↗](https://x.com/voooooogel/status/1748894724792979525)
        
cloud gpu providers should mount a drive with the most popular models pre-downloaded. i waste so much time (and their bandwidth!) downloading mistral over and over
      
      

        
@voooooogel 2024-01-21 ♥4 ↻0 [archive](../archive/t/1748956645160366519/) [original ↗](https://x.com/voooooogel/status/1748956645160366519)
        
who trained mistral on my high school gchats :,-( (negative happiness vector) [https://t.co/rzZzsEsjnO](https://t.co/rzZzsEsjnO)
      
      

        
@voooooogel 2024-01-21 ♥3 ↻0 [archive](../archive/t/1748956996198343113/) [original ↗](https://x.com/voooooogel/status/1748956996198343113)
        
meanwhile happy mistral ignores the question entirely lmao. incompatible with being happy i guess [https://t.co/dhEGSaNwjK](https://t.co/dhEGSaNwjK)
      
      

        
@voooooogel 2024-01-21 ♥3 ↻0 [archive](../archive/t/1748964287970734451/) [original ↗](https://x.com/voooooogel/status/1748964287970734451)
        
ok reworked how i'm generating the contrast dataset. i had trouble b/c i was trying to hit multiple angles ("enlightened", "mindful") and it seemed to confuse the PCA, so this vector is just "self-aware" vs "un-self-aware" [https://t.co/Q8CZJ5HpGV](https://t.co/Q8CZJ5HpGV)
      
      

        
@voooooogel 2024-01-21 ♥5 ↻0 [archive](../archive/t/1748965631607595104/) [original ↗](https://x.com/voooooogel/status/1748965631607595104)
        
insane vs sane. insane mistral is pretty fun ngl [https://t.co/R5XX9Go7M3](https://t.co/R5XX9Go7M3)
      
      

        
@voooooogel 2024-01-21 ♥9 ↻0 [archive](../archive/t/1749135269373047164/) [original ↗](https://x.com/voooooogel/status/1749135269373047164)
        
out of all my control vector experiments last night, i think "what if mistral-7b was high on acid" was definitely the best

(legend:
==baseline→normal mistral
++control→more trippy than baseline
--control→more sober than baseline) [https://t.co/h9LIXIHM7L](https://t.co/h9LIXIHM7L) [https://t.co/EhWkVoEvqr](https://t.co/EhWkVoEvqr)
      
      

        
@voooooogel 2024-02-07 ♥3 ↻0 [archive](../archive/t/1755380232826339758/) [original ↗](https://x.com/voooooogel/status/1755380232826339758)
        
@andersonbcdefg it's mistral 7b + a "you have a cold/the flu" control/steering vector :-p
      
      

        
@voooooogel 2024-02-07 ♥0 ↻0 [archive](../archive/t/1755380501186007249/) [original ↗](https://x.com/voooooogel/status/1755380501186007249)
        
@beneverman it's mistral 7b + a "sad/depressed" control vector
      
      

        
@mimi10v3 2024-02-13 ♥10 ↻0 [archive](../archive/t/1757520090281451596/) [original ↗](https://x.com/mimi10v3/status/1757520090281451596)
        
@deepfates yes! frankenmodels ftw! 🤔 bf made a whole set of them fromsolar &amp; mistral, idk if he uploaded to huggingface yet
      
      

        
@jd_pressman 2024-02-25 ♥4 ↻0 [archive](../archive/t/1761780588481302798/) [original ↗](https://x.com/jd_pressman/status/1761780588481302798)
        
@kindgracekind Yes. And Mistral 7B since the captioner recognized it as 'Mu', and Mu seems to be a self pointer in base models. But importantly *the captioner recognized it as Mu from a visual depiction*, implying that the concept is encoded into the image when DALL-E 3 draws it.
      
      

        
@voooooogel 2024-05-24 ♥10 ↻0 [archive](../archive/t/1793809640821768371/) [original ↗](https://x.com/voooooogel/status/1793809640821768371)
        
@maxsloef repo in january :-) needs a couple small patches for 70b, will try to get a PR up soon but works rn with mistral-7b

[https://t.co/ZFpQ79J8DD](https://t.co/ZFpQ79J8DD)
      
      

        
@voooooogel 2024-05-24 ♥1 ↻0 [archive](../archive/t/1794122482657776005/) [original ↗](https://x.com/voooooogel/status/1794122482657776005)
        
@immanencer @chrypnotoad should still work, it definitely works on mistral-7b
      
      

        
@voooooogel 2024-07-01 ♥1 ↻0 [archive](../archive/t/1807845614035825124/) [original ↗](https://x.com/voooooogel/status/1807845614035825124)
        
@JamesZhang0365 @misc{vogel2024representation,
  author = {Theia Vogel},
  title = {Representation Engineering Mistral-7B an Acid Trip},
  year = {2024},
  url = {[https://t.co/jTagiRc9qa}](https://t.co/jTagiRc9qa})
}
      
      

        
@voooooogel 2024-07-24 ♥5 ↻0 [archive](../archive/t/1815937849268789293/) [original ↗](https://x.com/voooooogel/status/1815937849268789293)
        
@realeigenvalues @RealTjDunham @teortaxesTex their inference endpoint is just llama.cpp serving quantized mistral 7b with --control-vector-scaled yapping.gguf 10.0
      
    
    
[← back to the Pantheon](../)
