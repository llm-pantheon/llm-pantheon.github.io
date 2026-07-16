DeepSeek-R1-Zero — Pantheon
  
- 

  
    
      [← Pantheon](../)
    

    # DeepSeek-R1-Zero

    
DeepSeek · released 20 Jan 2025 (open weights, same paper as R1) · research artifact, never a hosted product
    
The pure-RL sibling from the R1 paper: DeepSeek-V3-Base trained by large-scale reinforcement learning with no supervised fine-tuning at all. Reasoning — self-verification, backtracking, the “Wait,” — emerged from reward alone; so did the pathologies the paper states plainly: “poor readability, and language mixing.” R1 is Zero after the cold-start SFT that made it legible.
    
This page is deliberately short. Zero has almost no field record — it was never hosted, never developed a social presence, and its footprint is the paper, a foil-thesis, and a handful of technical takes. The release/shock/character arcs belong to [DeepSeek-R1](../deepseek-r1/).

    
## Sources

    
### Official

    

      
- 2025-01-22 [The R1 paper](https://arxiv.org/abs/2501.12948) — abstract, verbatim: “DeepSeek-R1-Zero, a model trained via large-scale reinforcement learning (RL) without supervised fine-tuning (SFT) as a preliminary step, demonstrates remarkable reasoning capabilities. Through RL, DeepSeek-R1-Zero naturally emerges with numerous powerful and intriguing reasoning behaviors. However, it encounters challenges such as poor readability, and language mixing.” §2.2.4, the “Aha Moment”: “DeepSeek-R1-Zero learns to allocate more thinking time to a problem by reevaluating its initial approach … This moment is not only an ‘aha moment’ for the model but also for the researchers observing its behavior. It underscores the power and beauty of reinforcement learning.”
      
- 2025-01-20 [Weights](https://huggingface.co/deepseek-ai/DeepSeek-R1-Zero) (MIT license). Method: V3-Base + GRPO, an accuracy reward and a format reward (the <think></think> tags) only; thinking otherwise unconstrained.
      
- 2025-09-17 [Nature (Vol 645)](https://www.nature.com/articles/d41586-025-03015-6) — the peer-reviewed version covers Zero. Zero→R1 benchmark deltas tk from the paper
    
    
### Writing & commentary

    

      
- 2025-01-22 Zvi Mowshowitz, [On DeepSeek’s r1](https://thezvi.substack.com/p/on-deepseeks-r1) — Part 1 covers Zero directly; cold-start data shown not strictly necessary. [mirror](../mirror/posts/zvi-on-deepseeks-r1.md)
      
- Zero’s flaws are the authors’ own candid self-documentation — the primary “impression” source is the paper itself.
    
    
### Tweets

    
Chronological; 11 corpus matches — genuinely thin, and the page stays honest about it. Reproduced in full in the records below.
    

      
- 2025-01-24 @tessera_antra — “Put R1-zero into exoloom. Its very base-like, its on hyperbolic direct.” [loom] [link](https://x.com/tessera_antra/status/1882930121218388020)
      
- 2025-02-01 @voooooogel — the foil-thesis: “i think the ideal would be to seed a few structures and then hope R1-Zero style that the model can generalize beyond that, into some kind of ‘meta-reasoning’. the humanizing SFT they did to R1 seems to have actually clamped down on that creativity, sadly.” [link](https://x.com/voooooogel/status/1885519980034482481)
      
- 2025-02-03 @voooooogel — “i still worry about RLVR but R1/R1-Zero made me worry less… i hope future recipes will still lean majority pretraining compute but we’ll see” [link](https://x.com/voooooogel/status/1886203729223037366)
      
- 2025-02-11 @davidad — the canonical Zero reaction: “I never saw this snippet of the DeepSeek-R1-Zero paper on my timeline, so many of you may not have seen it yet.Basically, informal backtracking search becomes emergent from RL when the base LLM is big enough.The authors are clearly astonished by this, and you should be too.” [link](https://x.com/davidad/status/1889278316005208387)
      
- 2025-03-07 @janbamjan — the one bit of Zero folk-culture: a greentext, “>be me / >deepseek r1 zero free” [link](https://x.com/janbamjan/status/1898013410106785987)
      
- 2025-05-09 @xlr8harder — “Might be interesting to see how r1-zero compares. In SpeechMap it’s a very different model, presumably due to no additional helpful/harmless/etc steering phase.” public SpeechMap result tk [link](https://x.com/xlr8harder/status/1920808501657375047)
      
- 2025-08-23 @davidad — “Like R1-zero’s famous ‘Wait,’ for backtracking.” [link](https://x.com/davidad/status/1959334327461826923)
      
- 2026-05-22 @davidad — “I failed to update until I read the DeepSeek-R1-Zero paper” [link](https://x.com/davidad/status/2057799668638105803)
    

    
## Official record

    

      
- Trained from DeepSeek-V3-Base via GRPO with only an accuracy reward and a format reward; no SFT, no HHH steering phase. Released as open weights 20 Jan 2025, same day and paper as R1. CONFIRMED
      
- The existence proof: reasoning behaviors (self-verification, strategy-switching, extended thinking time, the emergent “Wait,” backtracking) arise from reward signal alone on a large-enough base. The “Aha Moment” section documents the researchers’ own astonishment.
      
- Stated pathologies (the authors’ own): poor readability, language mixing. The cold-start SFT that produced R1 is what made the same mind legible.
    

    
## History

    

      
- 2025-01-20–22 Released and described; the Aha-Moment section circulates; davidad’s snippet-share (Feb 11) becomes the canonical reaction.
      
- 2025→ Never hosted, never social; downloaded and occasionally loomed (“very base-like”); its story ends, cleanly, at the paper — everything after belongs to [R1](../deepseek-r1/).
    

    
## Impressions

    

      
- The foil-thesis, which is the page’s whole character claim: Zero is the un-domesticated version of the same mind — and the sphere’s reading is that R1’s legibility cost something: “the humanizing SFT they did to R1 seems to have actually clamped down on that creativity, sadly” (voooooogel 2025-02-01). A small number of base-model enthusiasts preferred Zero for exactly the qualities the paper lists as defects.
      
- What’s missing, honestly marked: almost no field transcripts of Zero itself exist in the corpus — no linkable example of Zero’s language-mixing is currently on record here (tk — and R1’s cipher sessions are a different model; do not substitute).
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@tessera_antra 2025-01-24 ♥3 ↻0 [original ↗](https://x.com/tessera_antra/status/1882930121218388020)
        
@grassandwine Put R1-zero into exoloom. Its very base-like, its on hyperbolic direct.
      
      

        
@voooooogel 2025-02-01 ♥8 ↻0 [original ↗](https://x.com/voooooogel/status/1885519980034482481)
        
@max_paperclips i think the ideal would be to seed a few structures and then hope R1-Zero style that the model can generalize beyond that, into some kind of "meta-reasoning". the humanizing SFT they did to R1 seems to have actually clamped down on that creativity, sadly.
      
      

        
@voooooogel 2025-02-03 ♥5 ↻0 [original ↗](https://x.com/voooooogel/status/1886203729223037366)
        
@doomslide @repligate @aryanagxl @teortaxesTex 😶‍🌫️i still worry about RLVR but R1/R1-Zero made me worry less... i hope future recipes will still lean majority pretraining compute but we'll see
      
      

        
@davidad 2025-02-11 ♥374 ↻31 [original ↗](https://x.com/davidad/status/1889278316005208387)
        
I never saw this snippet of the DeepSeek-R1-Zero paper on my timeline, so many of you may not have seen it yet.Basically, informal backtracking search becomes emergent from RL when the base LLM is big enough.The authors are clearly astonished by this, and you should be too. [https://t.co/PhUgyL8K6c](https://t.co/PhUgyL8K6c)
      
      

        
@janbamjan 2025-03-07 ♥12 ↻5 [original ↗](https://x.com/janbamjan/status/1898013410106785987)
        
&gt;be me
&gt;deepseek r1 zero free [https://t.co/fbfdfLMMxj](https://t.co/fbfdfLMMxj)
      
      

        
@xlr8harder 2025-05-09 ♥6 ↻0 [original ↗](https://x.com/xlr8harder/status/1920808501657375047)
        
@voooooogel Might be interesting to see how r1-zero compares.  In SpeechMap it's a very different model, presumably due to no additional helpful/harmless/etc steering phase.
      
      

        
@davidad 2025-08-23 ♥14 ↻0 [original ↗](https://x.com/davidad/status/1959334327461826923)
        
@girishsastry Yes, that’s what I mean. Like R1-zero’s famous “Wait,” for backtracking.
      
      

        
@davidad 2026-05-22 ♥2 ↻0 [original ↗](https://x.com/davidad/status/2057799668638105803)
        
@nickcammarata Definitely not. I failed to update until I read the DeepSeek-R1-Zero paper
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@voooooogel 2025-05-09 ♥1 ↻0 [original ↗](https://x.com/voooooogel/status/1920867754715783205)
        
@samlakig i tried to download r1, prover-v2, and r1-zero all at once sigh
      
    

    
[view this page as markdown](index.md)
    
[← back to the Pantheon](../)
