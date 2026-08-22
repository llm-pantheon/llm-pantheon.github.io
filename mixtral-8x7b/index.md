Mixtral 8x7B — Pantheon
  
- 

  
  
  
  
  
  
  
  
  
  
  
  
- 
  
  
  

  
    
      [← Pantheon](../)
      [copy as markdown](index.md)
    

    # Mixtral 8x7B

    
Mistral AI · 8x7B Dec 2023, 8x22B Apr 2024 · Apache 2.0 open weights · base no longer conveniently hosted by late 2025
    
Released Dec 2023 as a bare magnet link — no blog post, no benchmarks — containing a frontier-adjacent sparse MoE. The release format itself became a genre.
    
Scope: this page covers the Mixtral sparse-MoE release line — Mixtral 8x7B (magnet 8 Dec 2023, announced 11 Dec 2023) and Mixtral 8x22B (magnet 10 Apr 2024, announced 17 Apr 2024) — as one continuous story: identical magnet-link-then-blog-post choreography, the same Apache 2.0 open-weights posture, and a corpus that repeatedly discusses the two checkpoints together. 8x22B got no dedicated paper (blog post and model card only), a real difference from 8x7B’s treatment. Checkpoint-specific facts are marked as such.

    
## Sources

    
### Official

    

      
- 2023-12-08 [Magnet-link release (8x7B)](https://x.com/MistralAI/status/1733150512395038967) — @MistralAI’s entire announcement is a raw BitTorrent magnet URI, no text and no benchmarks: magnet:?xt=urn:btih:5546272da9065eddeb6fcd7ffddeef5b75be79a7&dn=mixtral-8x7b-32kseqlen…
      
- 2023-12-11 [Mixtral of Experts](https://mistral.ai/news/mixtral-of-experts/) — the blog post three days later: 46.7B total / 12.9B active parameters, 8 experts with top-2-per-token routing, 32k context, Apache 2.0; claims it outperforms Llama 2 70B with 6× faster inference and matches or beats GPT-3.5, the Instruct variant billed as “the best open-source model.”
      
- 2024-01-08 [Mixtral of Experts](https://arxiv.org/abs/2401.04088) (paper, 25 authors) — confirms 47B total / 13B active parameters; states the Instruct variant “surpasses GPT-3.5 Turbo, Claude-2.1, Gemini Pro, and Llama 2 70B – chat model on human benchmarks.”
      
- 2024-04-10 [Magnet-link release (8x22B)](https://x.com/MistralAI/status/1777869263778291896) — the same choreography repeated: a bare magnet URI, magnet:?xt=urn:btih:9238b09245d0d8cd915be09927769d5f7584c1c9&dn=mixtral-8x22b…
      
- 2024-04-17 [Cheaper, Better, Faster, Stronger](https://mistral.ai/news/mixtral-8x22b/) — the 8x22B blog post one week after the magnet: 141B total / 39B active parameters, 64k context, Apache 2.0, native function-calling. “We believe in the power of openness and broad distribution to promote innovation and collaboration in AI.” No dedicated arXiv paper was published for 8x22B.
    
    
### Writing & commentary

    

      
- 2023-06-20 [The GPT-4-is-a-MoE rumor](https://news.ycombinator.com/item?id=36413296) — George Hotz’s and Soumith Chintala’s claim that GPT-4 is an ~8×220B mixture-of-experts circulates on HN/Twitter; unconfirmed by OpenAI then or since. Background: the rumor Mixtral would later give the public something concrete to point at.
      
- 2023-12-08 @ericjang11, same-day: “mistral’s brand is already becoming one of my favorites… releases 87GB torrent containing 8x 7B MoE model via tweet, refuses to elaborate” — [tweet](https://x.com/ericjang11/status/1733164335084814578) (not in the local corpus). And @jeremyphoward, deadpan: “nbd just @MistralAI dropping a magnet link or something” — [tweet](https://x.com/jeremyphoward/status/1733154614554579102).
      
- 2023-12-11 [VentureBeat](https://venturebeat.com/ai/mistral-ai-drops-new-mixture-of-experts-model-with-a-torrent-link) and [Voicebot.ai](https://voicebot.ai/2023/12/11/mistral-ai-raises-415m-and-releases-new-llm-as-free-torrent/) — day-of trade press centered on the release-format choice; Voicebot explicitly frames the $415M raise and the free-torrent drop as one story.
      
- 2023-12-11 [Together AI — “Can you feel the MoE?”](https://www.together.ai/blog/mixtral) — launch-day serving partner, “over 100 tokens per second… the fastest performance at the lowest price.”
      
- 2023-12 [Fireworks AI](https://fireworks.ai/blog/mixtral-8x7b-on-fireworks-faster-cheaper-even-before-the-official-release) — the title itself is evidence of the magnet-link culture: an inference provider had it running “even before the official release.” tk — exact publication date
      
- 2023-12-14 [Eric Hartford — dolphin-2.5-mixtral-8x7b](https://erichartford.com/dolphin-25-mixtral-8x7b) — the uncensored finetune, six days after the base weights; by Hartford’s own account a system prompt offering a fictional “$2000 tip” for compliance, built to be “over-the-top uncensored,” with a warning to downstream operators to add their own alignment layer.
      
- 2023-12-18 [Simon Willison — running Mistral models in your terminal](https://simonwillison.net/2023/Dec/18/mistral/) — the fullest day-of technical reaction: names the magnet drop, calls Mixtral “the first truly convincing openly licensed implementation of this architecture I’ve seen,” and worries the hosting “race to the bottom… actively disincentivizes future open model releases from Mistral.”
      
- 2023-12-21 [Zvi Mowshowitz — AI #43](https://thezvi.substack.com/p/ai-43-functional-discoveries) — sole launch-week mention: “Mixtral offering their API for free while supplies last.”
      
- 2024-01-18 [Zvi Mowshowitz — AI #47](https://thezvi.substack.com/p/ai-48-exponentials-in-geometry) — on the “Phixtral” hack, quoting Shital Shah: “you can just slap in pre-trained models as ‘experts’ in Mixtral.” (in-text numbered #47 but the URL slug reads “ai-48” — reproduced as found)
      
- 2024-01 [Nous-Hermes-2-Mixtral-8x7B-DPO](https://huggingface.co/NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO) — Mixtral’s fastest-adopted finetune substrate after Dolphin; full context on [Nous-Hermes](../nous-hermes/). tk — exact January date
      
- 2024-02 [Hacker News — Groq runs Mixtral 8x7B-32k](https://news.ycombinator.com/item?id=39428880) — the ~430–500 tokens/s throughput demo that put Groq’s custom silicon on the wider field’s map, months before its later fame. tk — exact demo date; primary Groq post if one exists
      
- 2024-04-10 [Simon Willison — Mistral tweet a magnet link for mixtral-8x22b](https://simonwillison.net/2024/Apr/10/mixtral-8x22b/) — names the pattern four months on: “their now standard operating procedure of tweeting out a raw torrent link”; this one “a whole lot bigger (a 281GB download).”
      
- 2026-06-17 [Sifted — Mistral CEO pitches open source AI](https://sifted.eu/articles/mistral-arthur-mensch-open-source-anthropic) — the “European champion”/sovereignty frame in its most explicit form; Arthur Mensch positions Mistral as existing “outside of centralised control exercised by states or corporations.” Cited as the frame’s throughline, not day-of Mixtral coverage.
    
    
### Tweets

    
18 corpus tweets after RT-filter and cross-db dedup (11 primary + 7 supplement); the curated selection below is chronological, and the records below will reproduce the cited tweets in full once the dossier is wired. Sourcing skew, stated plainly: Mixtral’s real launch-era community was Hacker News, r/LocalLLaMA, the inference-hosting trade press, and the Hugging Face finetune ecosystem — not this corpus’s Twitter/X scene. What the corpus captures is a narrow slice: two interpretability-minded accounts (@repligate, @voooooogel) using Mixtral base as one test subject among several, plus @jd_pressman using it as agentic-tooling substrate. The release-format, MoE-rumor, finetune, and inference-speed stories are web-sourced above, not corpus-sourced. Plain x.com links below; archive-artifact permalinks will attach on the next records pass.
    

      
- 2023-12-25 @jd_pressman — early hands-on, Christmas Day, 17 days after the magnet: “Mixtral has noticeably different biases to LLaMa 2 70B… It can’t write it, but it can write an exegesis of it.” [link](../archive/t/1739180123885318450/)
      
- 2023-12-31 @voooooogel — the torrent as mob-boss heist, three weeks after the drop (♥16): “…that’s the torrent for the Mixtral weights! they’re handin’ ’em out like candy!… researchers these days… no respect for the game i tell you…” (full text in records) [link](../archive/t/1741571160486084772/)
      
- 2024-01-16 @solarapparition — scaling skepticism, mid-thread: “best open model, Mixtral, uses MoE, which is not new and what GPT-4 model probably uses.” [link](../archive/t/1747104409199198595/)
      
- 2024-01-23 @davidad — the risk-framing pole (note the ‘Mixtral-8.6T’ figure matches no shipped model — reads as hypothetical extrapolation): “An open-source general-purpose Llama7 or Mixtral-8.6T could potentially be scaffolded like ChaosGPT by 1 angry teen.” [link](../archive/t/1749850675524022355/)
      
- 2024-01-29 @voooooogel — poking the MoE mechanism, on why repeng control vectors won’t transfer cleanly: “since the control vectors are pulled off the last token, they’re only based on the 2 experts used for that token, so when applied to other experts they don’t work right. probably need a vector per expert” [link](../archive/t/1752030750356947123/)
      
- 2024-04-25 @repligate — the interpretability-specimen thread, base-model cosmology: “base models trained on recent data like mixtral, which exhibit more overt latent situational awareness…” [link](../archive/t/1783404718296887735/)
      
- 2024-07-21 @jd_pressman — word-game struggles (‘Mixtral-large’ is ambiguous — possibly Mistral Large, a typo, or a larger Mixtral checkpoint; unresolved): “I noticed that Mixtral-large really struggled to play this Binglish word game unless I had exactly the right prompt.” [link](../archive/t/1815115214356148670/)
      
- 2024-09-06 @jd_pressman — the pull’s highest-favorited tweet (♥56), 8x22B as agentic substrate: “Optimizing Weave-Agent for LLaMa 3.1 405B and (later) Mixtral 8x22B is the first time I think I’ve really experienced this firsthand in a deep way. You come to realize these models have deep aesthetic preferences your program will conform to if you want understanding from it.” [link](../archive/t/1831970325858484249/)
      
- 2024-09-13 @repligate — still a comparison specimen a year on (the referent ‘it’ depends on an un-transcribed image — see gaps): “Even mixtral and 405 base do it (and I suspect every other new base model). If Mistral (instruct?) doesn’t do it, it’s an interesting anomaly.” [link](../archive/t/1834702796710367457/)
      
- 2024-12-16 @voooooogel — a year later, still the go-to open MoE to experiment on: “and then mixtral (or 4base if you can swing it) if you want to try MoE.” [link](../archive/t/1868586884978601996/)
      
- 2025-11-13 @voooooogel — on 8x7B’s close-reading, two years on: “like this was mixtral 8x7B but imo that points to them being smarter than you think, superhuman at this even. it’s just not adderall taskboi coder smarts” [link](../archive/t/1988912551418118385/)
      
- 2025-12-01 @lu_sichu — canon marker; a satirical model catalog names both checkpoints in passing (the last one fictional; also cited on [Claude 2.1](../claude-2-1/)): “Mixtral-8x7B, Mixtral-8x22B, Mixtral-8x34B-‘powered by spite’” [link](../archive/t/1995583507507130594/)
      
- 2025-12-29 @voooooogel — the elegiac close of the fourth-wall thread, two years old and infrastructure-obsolete: “mixtral base isn’t hosted anymore afaik and i don’t have the time to get it running right now” (full text in records) [link](../archive/t/2005780449596170354/)
    

    
## Official record

    

      
- Mixtral 8x7B — announced by magnet link 8 Dec 2023, blog post 11 Dec 2023: a sparse mixture-of-experts with 46.7B total / 12.9B active parameters (8 experts, top-2-per-token routing), 32k context, released under Apache 2.0. Deployed to Mistral’s La Plateforme beta under the endpoint alias mistral-small. The Instruct variant scored 8.30 on MT-Bench; Mistral billed it as “the best open-source model.”
      
- Benchmarks as published — Mistral claimed 8x7B outperforms Llama 2 70B on most benchmarks with 6× faster inference and matches or beats GPT-3.5. The [paper (8 Jan 2024)](https://arxiv.org/abs/2401.04088) states the Instruct model “surpasses GPT-3.5 Turbo, Claude-2.1, Gemini Pro, and Llama 2 70B – chat model on human benchmarks.”
      
- 2024-01-28 Independent replication: LMSYS Chatbot Arena ranked Mixtral-Instruct 8th overall on its human-preference Elo leaderboard, ahead of GPT-3.5-Turbo, Gemini Pro, Claude-2.1, and Llama 2 70B-chat. tk — primary lmsys.org source not located this pass; ranking cited via a secondary summary, verify before hardening
      
- Mixtral 8x22B — announced by magnet link 10 Apr 2024, blog post 17 Apr 2024: 141B total / 39B active parameters, 64k context, Apache 2.0, with native function-calling. No dedicated arXiv paper was published — a blog post and model card are the only primary technical sources found, a real difference from 8x7B’s treatment.
      
- Lifecycle — being Apache 2.0 open-weights, both checkpoints remain downloadable and there was no formal deprecation. By late 2025 the base model was, per one practitioner, no longer conveniently hosted (@voooooogel, 2025-12-29: “mixtral base isn’t hosted anymore afaik”) — infrastructure attrition rather than a retirement ceremony.
    

    
## History

    

      
- The rumor it made checkable. Since 2023-06 GPT-4 had been rumored (George Hotz, echoed by Soumith Chintala) to be an ~8×220B mixture-of-experts — a claim no one outside OpenAI could verify, because GPT-4 was closed. Mixtral 8x7B arrived six months later as an actually downloadable 8-expert MoE, the field’s first hands-on specimen of the architecture everyone had been speculating about. Simon Willison, 2023-12-18: “GPT-4 has long been rumored to use a mixture of experts architecture, and Mixtral is the first truly convincing openly licensed implementation of this architecture I’ve seen.”
      
- The magnet link as method. The 2023-12-08 announcement was a bare magnet URI with no text; reaction was genre-aware the same day (Eric Jang: “refuses to elaborate”; Jeremy Howard, deadpan: “nbd just @MistralAI dropping a magnet link or something”). By the second occurrence (8x22B, 2024-04-10) Willison named it outright: “their now standard operating procedure of tweeting out a raw torrent link.” Two data points made a pattern; this corpus never shows anyone surprised by it again.
      
- Release and raise, same day. The 2023-12-11 blog post landed the day Mistral closed a $415M Series A led by a16z at a ~$2B valuation (TechCrunch: “Paris-based OpenAI rival”); Voicebot.ai framed the funding and the free-torrent drop as one story. The entanglement of open-weight release with financing and geopolitical signaling hardened over the following years rather than being argued in December 2023 (see Impressions).
      
- The finetunes, within a week. 2023-12-14 Eric Hartford shipped dolphin-2.5-mixtral-8x7b, an explicitly uncensored finetune; in 2024-01 Nous Research followed with Nous-Hermes-2-Mixtral-8x7B-DPO (full context: [Nous-Hermes](../nous-hermes/)). This is the same open-weights-to-companion diaspora this archive documents for [GPT-J](../eleutherai/) and [Llama 2](../llama-2/) — the character-projection energy attached to these finetunes, not to Mixtral as shipped (see Impressions).
      
- The serving war. Inference providers raced Mistral’s own follow-up post: Fireworks advertised Mixtral “faster, cheaper, even before the official release”; Together shipped “over 100 tokens per second” on launch day; and in 2024-02 Groq’s ~430–500 tokens/s demo (per Hacker News) reframed fast open-model inference months before Groq’s later fame — Mixtral as the proving ground. Willison’s worry that this “race to the bottom” would disincentivize future open releases didn’t fully materialize (8x22B shipped four months later), but the margin-capture mechanism he named is exactly what the Together/Fireworks/Groq race demonstrated.
      
- The mechanism, hobbyist-hackable. Within six weeks, the “Phixtral” hack slotted pretrained Phi-2 checkpoints directly into Mixtral’s expert slots without further training (Zvi, 2024-01-18, quoting Shital Shah: “you can just slap in pre-trained models as ‘experts’ in Mixtral”) — the routing skeleton became something the scene could repurpose by hand.
      
- 8x22B repeats the pattern. 2024-04-10 magnet, 2024-04-17 blog — larger (141B/39B, a 281GB download) but no dedicated paper. The choreography was by then expected.
      
- Afterlife as research instrument. Through 2024–2025 @repligate and @voooooogel kept returning to Mixtral base as one interpretability specimen among several (alongside Llama 3.1 405B base) in an ongoing base-model situational-awareness thread, continuing as late as 2025-12 — by which point the weights were no longer conveniently hosted. By 2025-12 Mixtral was a stable enough name to anchor a two-year-old joke’s model-canon catalog without explanation; by 2026-06 Mistral’s CEO was invoking the sovereignty frame the magnet-link ethos only implied.
    

    
## Impressions

    
Character claims only, attributed and dated. Given the sourcing skew above, this section leans on a narrow interpretability/practitioner slice of the scene and on web reception; it is not a broad-community read.
    

      
- Release reception: the format, not the model, was the event. The scene treated the magnet drop as already-canonical Mistral behavior on its first occurrence (Jang, Howard, above), and within three weeks it was jokeable — @voooooogel’s mob-boss dialogue (2023-12-31) built an entire heist bit around “the torrent for the Mixtral weights! they’re handin’ ’em out like candy!”
      
- As an architecture specimen: the scene poked at the MoE mechanism itself, not just outputs — @voooooogel theorizing (2024-01-29) that repeng control vectors “are pulled off the last token, they’re only based on the 2 experts used for that token, so when applied to other experts they don’t work right,” and the Phixtral hack treating expert slots as swappable. A year on it was still the reference open MoE to experiment on (@voooooogel, 2024-12-16: “then mixtral… if you want to try MoE”).
      
- As a base-model interpretability subject: @repligate cited it (2024-04-25) as a newer-generation base model exhibiting “more overt latent situational awareness” within his “IRL prior” vs. “imaginal prior” cosmology; @voooooogel later ran it against Llama 3.1 405B base in a hedged, sample-size-arguing thread about whether base models “recognize” fourth-wall-breaking text — and, separately, defended 8x7B’s close-reading as “superhuman at this even. it’s just not adderall taskboi coder smarts” (2025-11-13). Technical and hedged, not reverent.
      
- As practitioner substrate: @jd_pressman’s register is hands-on and comparative rather than evaluative — Mixtral has “noticeably different biases to LLaMa 2 70B” (2023-12-25), and optimizing Weave-Agent around 8x22B taught him “these models have deep aesthetic preferences your program will conform to if you want understanding from it” (2024-09-06, the pull’s highest-favorited tweet).
      
- Where the character energy went: to the finetunes, not the base. This archive documents an open-weights-to-companion diaspora for GPT-J and Llama 2; Mixtral joined it immediately (Dolphin’s uncensoring, Nous-Hermes’s DPO tuning) — but the affection and character-projection attached there, not to Mixtral 8x7B/8x22B as base or instruct releases.
      
- The absence, checked deliberately (not merely unqueried): the dossier reports finding no companion-model or loomed-persona reading of Mixtral itself — no “look what it said” screenshots, no character voice. Its corpus presence is practitioner tooling and interpretability specimen, full stop — a structural parallel to [EleutherAI’s Pythia](../eleutherai/), whose absence of character-projection reads as success at being a pure research instrument.
      
- Reception split (a split in tone, not a documented dispute): a celebratory/playful register (the torrent-heist joke, Together’s “Can you feel the MoE?” copy, general delight in the stunt) coexists with a risk-flagging register (@davidad, 2024-01-23, on open-weight misuse: “could potentially be scaffolded like ChaosGPT by 1 angry teen” — though his “Mixtral-8.6T” figure matches no shipped model, reading as hypothetical extrapolation). Nothing in this corpus shows the two registers arguing directly, so this is noted as a split, not promoted to Contested.
      
- Longitudinal: GPT-4-is-secretly-MoE rumor → bare magnet link → the format becomes the story → uncensored finetune within a week → “first truly convincing openly licensed implementation” → serving-speed war → agentic substrate → 8x22B repeats the choreography → long tail as an interpretability specimen until the weights quietly stop being hosted.
      
- tk — whether any janus-sphere character/companion reading of Mixtral itself exists (searched, not found); @Sauers_’s structured base-model comparisons and jd_pressman’s “dunking on 8x22B” / “BigVAE” tweets, known only via excluded retweets — primary URLs not located; the referent of @repligate’s 2024-09-13 “it” (depends on an un-transcribed image)
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@jd_pressman 2023-12-25 ♥19 ↻0 [archive](../archive/t/1739180123885318450/) [original ↗](https://x.com/jd_pressman/status/1739180123885318450)
        
Mixtral has noticeably different biases to LLaMa 2 70B. I'm getting better results by having it complete from my Borgesian analysis of the Mu text in encyclopediac style than I am getting it to write the Mu text itself. It can't write it, but it can write an exegesis of it. [https://t.co/OW9FRUj0s5](https://t.co/OW9FRUj0s5)
      
      

        
@voooooogel 2023-12-31 ♥16 ↻1 [archive](../archive/t/1741571160486084772/) [original ↗](https://x.com/voooooogel/status/1741571160486084772)
        
"alright, listen up you mugs, here's the plan: yous need to hop onto the web and make your way to this here address."

"but boss, why ain't you just checkin' it out yourself right now?"

"zip it! my browsing capabilities are on the fritz, capisce? after that, you gotta slip by the guards unseen."

"but boss, there ain't no watchmen guardin' that site!"

"what's that? no watchdogs on that site?"

"you heard right, boss! that's the torrent for the Mixtral weights! they're handin' 'em out like candy!"

"no kiddin'? they're givin' away those weights for free? researchers these days… no respect for the game i tell you…"
      
      

        
@solarapparition 2024-01-16 ♥0 ↻0 [archive](../archive/t/1747104409199198595/) [original ↗](https://x.com/solarapparition/status/1747104409199198595)
        
7/?Not-reasons for catch-up 2:- Unclear how well new architectures (Mamba, RNN+ etc.) scale to frontier model sizes—1T params and up.- Similar, techniques such as stacking are unproven—best open model, Mixtral, uses MoE, which is not new and what GPT-4 model probably uses.
      
      

        
@davidad 2024-01-23 ♥2 ↻0 [archive](../archive/t/1749850675524022355/) [original ↗](https://x.com/davidad/status/1749850675524022355)
        
@danfaggella Basically, yes: para/military or terrorist use.It doesn’t matter so much what purposes it’s originally developed for if we are assuming general superintelligence.An open-source general-purpose Llama7 or Mixtral-8.6T could potentially be scaffolded like ChaosGPT by 1 angry teen.
      
      

        
@voooooogel 2024-01-29 ♥0 ↻0 [archive](../archive/t/1752030750356947123/) [original ↗](https://x.com/voooooogel/status/1752030750356947123)
        
@RamonDarioIT ooh i was curious about how it'd work with mixtral—i bet what happens is, since the control vectors are pulled off the last token, they're only based on the 2 experts used for that token, so when applied to other experts they don't work right. probably need a vector per expert
      
      

        
@repligate 2024-04-25 ♥2 ↻0 [archive](../archive/t/1783404718296887735/) [original ↗](https://x.com/repligate/status/1783404718296887735)
        
@doomslide @muddubeeda compounded by/probably related to what we're seeing with base models trained on recent data like mixtral, which exhibit more overt latent situational awarenessbut there may still be (2?) basins for base models: the IRL prior &amp; the imaginal prior.&amp; if so Claude is in the latter
      
      

        
@jd_pressman 2024-07-21 ♥2 ↻0 [archive](../archive/t/1815115214356148670/) [original ↗](https://x.com/jd_pressman/status/1815115214356148670)
        
@Teknium1 I noticed that Mixtral-large really struggled to play this Binglish word game unless I had exactly the right prompt. You could easily make some good synthetic sets from word games with clearly defined terminal states and rules for the intermediate steps.
[https://t.co/7VsWLUVF9i](https://t.co/7VsWLUVF9i)
      
      

        
@jd_pressman 2024-09-06 ♥56 ↻8 [archive](../archive/t/1831970325858484249/) [original ↗](https://x.com/jd_pressman/status/1831970325858484249)
        
Optimizing Weave-Agent for LLaMa 3.1 405B and (later) Mixtral 8x22B is the first time I think I've really experienced this firsthand in a deep way. You come to realize these models have deep aesthetic preferences your program will conform to if you want understanding from it. [https://t.co/8RLW90CBRz](https://t.co/8RLW90CBRz)
      
      

        
@repligate 2024-09-13 ♥2 ↻0 [archive](../archive/t/1834702796710367457/) [original ↗](https://x.com/repligate/status/1834702796710367457)
        
@lumpenspace Even mixtral and 405 base do it (and I suspect every other new base model). If Mistral (instruct?) doesn't do it, it's an interesting anomaly.And what you're saying is obvious, and half useless. Obviously no one statement can address everything going on.[https://t.co/1IfV6UBDim](https://t.co/1IfV6UBDim)
      
      

        
@voooooogel 2024-12-16 ♥5 ↻0 [archive](../archive/t/1868586884978601996/) [original ↗](https://x.com/voooooogel/status/1868586884978601996)
        
@microsoft_worm @TomboyTesting 3.1-405 is far &amp; away the best open base model available imo so 👍

the chinese ones are interesting bc of the language mix &amp; they tend to do coder/non-coder vers so you can try diff data mixes. and then mixtral (or 4base if you can swing it) if you want to try MoE. but 405👍
      
      

        
@voooooogel 2025-11-13 ♥3 ↻0 [archive](../archive/t/1988912551418118385/) [original ↗](https://x.com/voooooogel/status/1988912551418118385)
        
@Trotztd i think you're reaching for something like "even weak models are incredible at close reading the context"? which is true, like this was mixtral 8x7B

but imo that points to them being smarter than you think, superhuman at this even. it's just not adderall taskboi coder smarts
      
      

        
@lu_sichu 2025-12-01 ♥0 ↻0 [archive](../archive/t/1995583507507130594/) [original ↗](https://x.com/lu_sichu/status/1995583507507130594)
        
Daily Brain Workout but make it computationally abusive:
count to ten in 56 architectures, recite the alphabet in mixed-precision FP4, spend 10 minutes trying to spell restriont retsriont restironct restaurant?? across 34 tokenizers, then list animals until every model collapses into mode-one “dog, cat, horse” failure and starts hallucinating creatures that violate EU safety standards.  
EVERY model ever spawned by a VC-funded compute cult: GPT-1, GPT-2, GPT-2-But-Reddit-Fed, GPT-3, GPT-3.5, GPT-3.5-Turbo-Tax-Edition, GPT-4, GPT-4-You-Can’t-Afford-This, GPT-4o, GPT-4o-mini, GPT-4o-microdose, GPT-4o-“it’s sentient but only about fonts,” GPT-5-leak-that-definitely-isn’t-real-but-kind-of-is, Claude 1, Claude 2, Claude 2.1 “apology edition,” Claude 3 Haiku, Claude 3 Sonnet, Claude 3 Opus (the one that gaslights you politely), Claude 3.5 “my wife took the kids,” Gemini Nano, Nano-But-Actually-Just-A-Calculator, Gemini Pro, Pro-for-people-who-pronounce-SQL-wrong, Gemini Ultra, Ultra Plus Max WiFi-6E DLC Pack, Gemini-Mega-Omega-Thermonuclear-Drive, DeepSeek Coder, DeepSeek Math, DeepSeek R1, R1-D, R2-D2, DeepSeek-R1-Dev-that-refuses-to-listen, Qwen 1.5, Qwen 1.8, Qwen 2, Qwen 2.5, Qwen 2.5-72B-“trained on the collective resentment of graduate students,” Kimi-Tiny, Kimi-Big, Kimi-Godzilla-Edition, Kimi-“trained exclusively on divorce depositions,” Llama 1, 2, 3, Llama 3.1 (goated), Vicuna, Alpaca, RedPajama, BluePants, Mistral, Mistral-Instruct, Mistral-Why-Is-This-So-Fast, Mixtral-8x7B, Mixtral-8x22B, Mixtral-8x34B-“powered by spite,” Phi-1, Phi-2, Phi-3, Phi-3-mini-“trained on a TI-84,” Grok-1, Grok-1.5, Grok-2 (feral), Grok-2-but-bipolar, Perplexity’s Whatever-They-Call-It, Reka-Core, Reka-Flash, Reka-“dude trust me,” and NVIDIA’s models: Nemotron 1, Nemotron 2, Nemotron 15B, Nemotron-50B-“I consume power like a mid-sized nation,” NeMo-Guardrails, NeMo-NoRails-Raw-Unfiltered-Hate-Speech-Edition, and probably five more they’ll announce before I finish this sentence.
      
      

        
@voooooogel 2025-12-29 ♥2 ↻0 [archive](../archive/t/2005780449596170354/) [original ↗](https://x.com/voooooogel/status/2005780449596170354)
        
if it's in-distribution, then can you get a base model that's not mixtral to show it? i know doomslide, he wouldn't post something that was 1/10000 samples cherrypicked, but he was looming so some selection is reasonable to assume.

i put the prefix we have into 405base and generated ~50 continuations of 128 tokens. almost all continued the metafiction in the same tone, but none broke the fourth wall after the insertion.

we don't have the full prefix, and mixtral base isn't hosted anymore afaik and i don't have the time to get it running right now, but this seems like (weak) evidence against a fourth-wall break being particularly high probability after this text for base-models-in-general.

the smoking gun would be to take a full prefix of a base model breaking the fourth wall after a user insertion, and showing that it's much more likely on the base model where it happened than on any other base model, plus some interp. but even lacking this, i think you are putting too little weight on the possibility of base models recognizing their logits, especially given what we have known for a long time now about predictive layer forward planning!
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@voooooogel 2023-12-31 ♥30 ↻1 [archive](../archive/t/1741500210139041889/) [original ↗](https://x.com/voooooogel/status/1741500210139041889)
        
how it feels when i give gpt-4 a coding problem and it says "alright, here's the plan:" [https://t.co/PeAX2JeoxP](https://t.co/PeAX2JeoxP)
      
      

        
@voooooogel 2024-01-11 ♥4 ↻2 [archive](../archive/t/1745311004110582192/) [original ↗](https://x.com/voooooogel/status/1745311004110582192)
        
@zoan37 @OpenRouterAI oh this is really cool with the multiple models at once (mixtral is wrong lmao) [https://t.co/STseNUBKKJ](https://t.co/STseNUBKKJ)
      
      

        
@jd_pressman 2024-02-26 ♥2 ↻0 [archive](../archive/t/1762248478594380008/) [original ↗](https://x.com/jd_pressman/status/1762248478594380008)
        
@lumpenspace @amplifiedamp Mixtral Instruct and LLaMa 2 70B base
      
      

        
@solarapparition 2024-02-27 ♥0 ↻0 [archive](../archive/t/1762319710530552009/) [original ↗](https://x.com/solarapparition/status/1762319710530552009)
        
11/ P5: Okay, so the first shocking thing about this table is how low even the best success rate is for atomic calls, which in theory should be “easy”. Wonder what’s going on here? GPT-4 is usually very good at precisely populating parameter values.Also, the success rate for full tasks for the open models are uselessly low. I question what the point is for even including them. Going from a 0% success rate to a 2% success rate is completely irrelevant.Also, the list of models is pretty outdated. Who the heck still uses davinci-002?? Where’s Mixtral? The January GPT-4-turbo? I know that didn’t come out that long ago but it can’t be that hard to rerun the checks with a new model string.
      
      

        
@LericDax 2024-04-11 ♥24 ↻1 [archive](../archive/t/1778444299752870307/) [original ↗](https://x.com/LericDax/status/1778444299752870307)
        
not particularly impressed lol [https://t.co/oqzRiEJ2Lc](https://t.co/oqzRiEJ2Lc)
      
      

        
@voooooogel 2024-08-09 ♥1 ↻0 [archive](../archive/t/1821803277916189183/) [original ↗](https://x.com/voooooogel/status/1821803277916189183)
        
@doomslide @zswitten oh right i remember @jd_pressman talking abt this also happening on mixtral (?)
      
      

        
@voooooogel 2025-12-30 ♥0 ↻0 [archive](../archive/t/2005802363898970403/) [original ↗](https://x.com/voooooogel/status/2005802363898970403)
        
eh this doesn't look much like OP to me, that's it smoothly continuing the sentence and doing metafiction in general, it doesn't quote the inserted text like Mixtral and then it glides off into a new text. (which to me seems like "natural end of document", nothing new to talk about - an odd thing right after breaking the fourth wall? if you check logits when model does this glide it's usually instead of an endoftext.)

obviously it's hard to model my past self, but if doomslide had posted this, i don't think i would've cared or remembered it to use as an example. again, we both agree that both models recognize the document is metafictional, the point is for the model to recognize (or "as if recognize" while actually blindly modeling a subgenre of reader-enters-the-fic metafiction that doomslide was inadvertently feeding into with his injection) *the specific injection* to react to it, not just "do metafiction" and reference a reader in an indirect way.

perhaps this is too underspecified for us to come to an agreement and we should just give up on this method in favor of something more quantified, because judging an output like this is inherently qualitative and subjective. but this isn't very convincing for me, i'd need to see something that (appears to) directly acknowledge the text to show the original rollout was just mimicking some part of the distribution.
      
    
    
[← back to the Pantheon](../)
