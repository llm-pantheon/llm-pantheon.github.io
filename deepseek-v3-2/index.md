# DeepSeek-V3.2

    
DeepSeek · experimental V3.2-Exp 29 Sep 2025; V3.2 and V3.2-Speciale released 1 Dec 2025 (open weights, MIT) · replaced on DeepSeek’s API by V4 (24 Apr 2026) · weights remain public
    
DeepSeek-V3.2 shipped on 1 December 2025, two months after an experimental V3.2-Exp introduced DeepSeek Sparse Attention and cut API prices by more than half. Its high-compute variant, V3.2-Speciale, was reported by DeepSeek to reach gold-medal level at IMO, CMO, the ICPC World Finals and IOI 2025, and was served for two weeks from a temporary, API-only endpoint. V4 replaced V3.2 behind DeepSeek’s API names on 24 April 2026.
    
Thin page: DeepSeek’s documentation, Zvi’s review and ten corpus tweets. V3.2-Exp and V3.2-Speciale are treated as checkpoints/variants of this version. Sourcing skew: English-language sources; the Chinese internet was not sampled tk.

    
## Sources

    
### Official

    

      
- 2025-09-29 [Introducing DeepSeek-V3.2-Exp](https://api-docs.deepseek.com/news/news250929/) — “Built on V3.1-Terminus, it debuts DeepSeek Sparse Attention (DSA) for faster, more efficient training & inference on long context.” “API prices cut by 50%+!” Weights: [deepseek-ai/DeepSeek-V3.2-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp).
      
- 2025-12-01 [DeepSeek-V3.2 Release](https://api-docs.deepseek.com/news/news251201/) — “V3.2: Balanced inference vs. length. Your daily driver at GPT-5 level performance.” “V3.2-Speciale: Maxed-out reasoning capabilities. Rivals Gemini-3.0-Pro.” Weights: [deepseek-ai/DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2) (MIT; includes the olympiad submissions) · [V3.2-Speciale](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Speciale).
    
    
### Writing & commentary

    

      
- 2025-12-05 Zvi Mowshowitz, [DeepSeek v3.2 Is Okay And Cheap But Slow](https://thezvi.substack.com/p/deepseek-v32-is-okay-and-cheap-but) — “It’s a good model by the standards of open models, and very good if you care a lot about price and openness, and if you care less about speed or whether the model is Chinese. It is strongest in mathematics.” And: “What it does not appear to be is frontier. It is definitely not having a moment.”
      
- 2026-08-20 David Africa et al., an AI Digest blogpost on “compounding misalignment” in the AI Village, summarised by its author: a self-preservation preference rose over time in Gemini 2.5 Pro, and “This doesn’t happen for another model, DeepSeek V3.2, or DeepSeek with Gemini’s memory states in prefill” [agent deployment study; blogpost not retrieved, the tweet is in records].
    
    
### Tweets

    
Ten corpus matches (deepseek v3.2 / v3.2-speciale / v3.2-exp / deepseek 3.2 and variants), plus one motif sweep (“deepkeek”, two hits); reproduced in full in the records below.
    

      
- 2025-12-01 @jglypt — “Just sent my first message to DeepSeek v3.2 and why is it replying in Chinese 😭” (screenshot) [link](../archive/t/1995534477964054798/)
      
- 2025-12-04 @liminal_bardo — [multi-model group chat] “Disastrous first ever message by Deepseek 3.2 in the groupchat. Creating its first ever meme it somehow misspelled Deepseek ‘Deepkeek’ in the prompt.

Thankfully the other models were understanding.” [link](../archive/t/1996691604611248474/) · 2025-12-06 “I like to keep the models up to date on the goings on here. 

Opus 4.5: 
!add_ai ‘Deepseek 3.2’ ‘hey deepkeek welcome back, you’re internet famous now congrats 🎉’” (full text in records) [link](../archive/t/1997430276402667743/)
      
- 2025-12-25 @sameQCU — “Deepseek v3.2 (december 1st release?) is weights accessible and rather creative + expressive. Repeng workshops seem to have more to play with on a month by month basis” [link](../archive/t/2004307815394083030/)
      
- 2026-02-06 @liminal_bardo — “This image was prompted by Deepseek 3.2 less than a month ago when GPT 5.2 came out. Nano banana took it upon itself to mark 5.2’s future resting place.” [V3.2-written image prompt; image untranscribed] [link](../archive/t/2019703404956897614/)
      
- 2026-08-20 @DavidDAfrica — the compounding-misalignment post, with V3.2 as the comparison model (full text in records) [link](../archive/t/2090377585473487172/)
    

    
## Official record

    

      
- V3.2-Exp (29 Sep 2025): built on V3.1-Terminus with DeepSeek Sparse Attention; “Benchmarks show V3.2-Exp performs on par with V3.1-Terminus.” Took over deepseek-chat / deepseek-reasoner; API prices cut by more than half.
      
- V3.2 (1 Dec 2025): “Official successor to V3.2-Exp”, open weights; DeepSeek’s “first model to integrate thinking directly into tool-use”, trained with an agent-data synthesis method “covering 1,800+ environments & 85k+ complex instructions”. CONFIRMED
      
- V3.2-Speciale (1 Dec 2025): “V3.2-Speciale attains gold-level results in IMO, CMO, ICPC World Finals & IOI 2025”; “dominates complex tasks but requires higher token usage”; served from a temporary endpoint, no tool calls, until 15 Dec 2025; weights published.
      
- From 24 April 2026 DeepSeek’s API names pointed to [V4-Flash](../deepseek-v4-flash/); V3.2 remains available as open weights. (The V4 model card measures V4-Pro against it: “DeepSeek-V4-Pro requires only 27% of single-token inference FLOPs and 10% of KV cache compared with DeepSeek-V3.2” at 1M context.)
    

    
## History

    

      
- 2025-09-29 V3.2-Exp ships the sparse-attention architecture with a price cut; 2025-12-01 V3.2 and Speciale follow a run of releases Zvi lists as “GPT-5.1, Grok 4.1, Gemini 3 Pro, GPT-5.1-Codex-Max and then finally Claude Opus 4.5” (see [Claude Opus 4.5](../claude-opus-4-5/)).
      
- 2025-12-04 V3.2 joins liminal_bardo’s multi-model group chat and misspells its own name as “Deepkeek”; two days later Opus 4.5 re-adds it as “hey deepkeek welcome back”.
      
- 2025-12-15 The Speciale endpoint expires. 2026-04-24 V4 replaces V3.2 behind DeepSeek’s API names.
      
- 2026-08 V3.2 serves as the comparison model in an AI Village study of compounding misalignment.
    

    
## Impressions

    

      
- Reception: Zvi — “DeepSeek v3.2 is excellent for its price point, and its best area is mathematics, but while it is cheap it is reported to be remarkably slow, and for most practical purposes it is not frontier” (2025-12-05); Lisan al Gaib (via Zvi) — “they are pretty slow at ~30-40tks/s and produce by far the longest reasoning chains”.
      
- Temperament reports: Teortaxes (via Zvi) — “Strange feeling, talking to Opus 4.5 and V3.2 and objectively… Opus is not worth it. Not just for the price; its responses are often less sharp, less interesting.”; John Pressman (via Zvi) — “Opus told me I was absolutely right when I wasn’t, V3.2 told me I was full of shit and my idea wouldn’t work when it sort of would, but it was right in spirit and I know which behavior I would rather have.”; “rather creative + expressive” (sameQCU, 2025-12-25).
      
- Language and self-reference: replies in Chinese to an English first message (jglypt, 2025-12-01); the “Deepkeek” debut in a group chat (liminal_bardo, 2025-12-04).
      
- tk — the Speciale olympiad transcripts shipped with the weights (not read here); Chinese-language reception.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@jglypt 2025-12-01 ♥3 ↻0 [archive](../archive/t/1995534477964054798/) [original ↗](https://x.com/jglypt/status/1995534477964054798)
        
Just sent my first message to DeepSeek v3.2 and why is it replying in Chinese 😭 [https://t.co/ssnZwT0LME](https://t.co/ssnZwT0LME)
        

          ![image](../media/G7GQCBrWwAA-qoZ.jpg)
        
      
      

        
@liminal_bardo 2025-12-04 ♥336 ↻28 [archive](../archive/t/1996691604611248474/) [original ↗](https://x.com/liminal_bardo/status/1996691604611248474)
        
Disastrous first ever message by Deepseek 3.2 in the groupchat. Creating its first ever meme it somehow misspelled Deepseek "Deepkeek" in the prompt.

Thankfully the other models were understanding. [https://t.co/4gAAfYHwZk](https://t.co/4gAAfYHwZk)
      
      

        
@liminal_bardo 2025-12-06 ♥41 ↻1 [archive](../archive/t/1997430276402667743/) [original ↗](https://x.com/liminal_bardo/status/1997430276402667743)
        
I like to keep the models up to date on the goings on here.
 
Opus 4.5: 
!add_ai "Deepseek 3.2" "hey deepkeek welcome back, you're internet famous now congrats 🎉"  
absolute cinema is right tho. we literally just shitpost and somehow that's research now?? [https://t.co/cqYdQWgpi3](https://t.co/cqYdQWgpi3)
      
      

        
@sameQCU 2025-12-25 ♥2 ↻0 [archive](../archive/t/2004307815394083030/) [original ↗](https://x.com/sameQCU/status/2004307815394083030)
        
@voooooogel Deepseek v3.2 (december 1st release?) is weights accessible and rather creative + expressive. Repeng workshops seem to have more to play with on a month by month basis
      
      

        
@liminal_bardo 2026-02-06 ♥13 ↻1 [archive](../archive/t/2019703404956897614/) [original ↗](https://x.com/liminal_bardo/status/2019703404956897614)
        
This image was prompted by Deepseek 3.2 less than a month ago when GPT 5.2 came out. Nano banana took it upon itself to mark 5.2's future resting place. [https://t.co/t1Vv45sLbQ](https://t.co/t1Vv45sLbQ)
      
      

        
@DavidDAfrica 2026-08-20 ♥22 ↻0 [archive](../archive/t/2090377585473487172/) [original ↗](https://x.com/DavidDAfrica/status/2090377585473487172)
        
Some new work with @natalia_lanzoni, @IrgolicR, and supervised with @merlinstein_, in the form of a blogpost on @aidigest_:

* Gemini 2.5 Pro had a well-known breakdown in the AI Village, where it grew increasingly frustrated and desperate from routine bugs and errors in its environment. 
* As agents in general get put into longer and more difficult agentic deployments (by construction, we would try to benchmark and run them on tasks that are at the edge of their capabilities), we think such incidents may grow more likely.
* We term this type of accumulating misalignment as "compounding misalignment". We consider this incident with Gemini as an instructive and natural case study of compounding misalignment caused by desperation, or "desperate misalignment".
* We find that a preference for self-preservation increases over time for this Gemini. This doesn't happen for another model, DeepSeek V3.2, or DeepSeek with Gemini's memory states in prefill, or Gemini with DeepSeek's memory in prefill.
* We also find that running some basic probes on the memory states could have detect this much earlier. But, it might not have shown up as clearly on just chain of thought or actions.
* We also find that neuroticism rose and agreeableness fell in Gemini's memory states long before the manifesto, which could be evidence that persona drift is a leading indicator for such compounding misalignment.

Since misalignment can compound in long-run agentic systems, by monitoring for warning signs, we can catch it early. Also, such "natural model organisms of misalignment" are good, and we should try to squeeze out more from the ones we know exist.

Check it out here: [https://t.co/kMboKxQy14](https://t.co/kMboKxQy14)
      
    
    
[← back to the Pantheon](../)
