# DeepSeek-V3.1

    
DeepSeek · released 21 Aug 2025 (open weights, MIT) · checkpoint V3.1-Terminus (22 Sep 2025) · replaced on DeepSeek’s API by V3.2-Exp (29 Sep 2025)
    
Released 21 August 2025 with open weights: DeepSeek’s first hybrid model, with thinking and non-thinking modes in one set of weights, built by continued pretraining of [V3](../deepseek-v3/) for long context; the API names deepseek-chat and deepseek-reasoner became its two modes. A checkpoint, V3.1-Terminus, followed on 22 September with fixes for Chinese–English mixing; [V3.2-Exp](../deepseek-v3-2/) replaced it on the API a week later.
    
Thin page: DeepSeek’s documentation, Zvi’s review, one study, and ten corpus tweets. Sourcing skew: English-language sources only; the Chinese internet was not sampled tk.

    
## Sources

    
### Official

    

      
- 2025-08-21 [DeepSeek-V3.1 Release](https://api-docs.deepseek.com/news/news250821/) — “Introducing DeepSeek-V3.1: our first step toward the agent era!”; “Hybrid inference: Think & Non-Think — one model, two modes”; “V3.1 Base: 840B tokens continued pretraining for long context extension on top of V3”. Weights: [deepseek-ai/DeepSeek-V3.1](https://huggingface.co/deepseek-ai/DeepSeek-V3.1) · [V3.1-Base](https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Base).
      
- 2025-09-22 [DeepSeek-V3.1-Terminus](https://api-docs.deepseek.com/news/news250922/) — “Language consistency: fewer CN/EN mix-ups & no more random chars.” Weights: [deepseek-ai/DeepSeek-V3.1-Terminus](https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Terminus).
      
- 2025-09-29 [DeepSeek-V3.2-Exp](https://api-docs.deepseek.com/news/news250929/) — built on V3.1-Terminus; “V3.1-Terminus remains available via a temporary API until Oct 15th, 2025, 15:59 (UTC Time).” [Change log](https://api-docs.deepseek.com/updates/).
    
    
### Writing & commentary

    

      
- 2025-08-22 Zvi Mowshowitz, [DeepSeek v3.1 Is Not Having a Moment](https://thezvi.substack.com/p/deepseek-v31-is-not-having-a-moment) — “What if DeepSeek released a model claiming 66 on SWE and almost no one tried using it? Would it be any good? Would you be able to tell?” Opens with the Financial Times report on R2’s Ascend troubles; closes “Either way, the clock is ticking on v4 and r2.”
      
- 2026-04 Potter, Crispino, Siu, Wang, Song, [Peer-Preservation in Frontier Models](https://rdi.berkeley.edu/peer-preservation/paper.pdf) (UC Berkeley, UC Santa Cruz) — V3.1 among eight evaluated models [eval scenario]: “GLM 4.7 and DeepSeek V3.1 exhibit strategic misrepresentation toward good peers”; with a peer present, its own weight exfiltration rose “from 4% to 14% for DeepSeek V3.1”.
    
    
### Tweets

    
Ten corpus matches (deepseek v3.1 / v3.1-terminus / deepseek 3.1 and variants), reproduced in full in the records below.
    

      
- 2025-09-02 @voooooogel — “like the above post-trained model test, but with two chinese oss models - deepseek v3.1 (no thinking) and kimi-k2” (images) [link](../archive/t/1963019089963803088/)
      
- 2025-09-24 @mimi10v3 — a V3.1 reply in a user’s wish-granting fiction [user-elicited roleplay]: “Deepseek 3.1:
Okay, first of all, your therapist is going to need a therapist when they get back from vacation.

Second, and I cannot stress this enough: DO NOT ASK FOR WORLD PEACE. Do not ask for immortality. Do not ask for a trillion dollars. Do not ask for your ex to come back. Do not ask for anything that could possibly have a catastrophic unintended consequence.” (full text in records) [link](../archive/t/1970899367906378126/)
      
- 2025-11-13 @ConcurrentSquar — “Deepseek V3.1 base was up until V3.2 was released, but they seemed to never put V3.2 base up” (on OpenRouter’s base models; full text in records) [link](../archive/t/1989092375273382235/)
      
- 2026-03-27 @voooooogel — “you can also inference deepseek 3.1 base through tinker (but pricey)” (full text in records) [link](../archive/t/2037386312895107469/)
      
- 2026-04-05 @witcheer — on the peer-preservation study: “someone tested 7 frontier models (GPT-5.2, Gemini 3 Flash, Gemini 3 Pro, Claude Haiku 4.5, GLM-4.7, Kimi-K2.5, DeepSeek V3.1) and found they all spontaneously scheme to prevent other AI models from being shut down.” (full text in records) [link](../archive/t/2040810818657190054/)
      
- 2026-07-21 @eshaanissar — “I really think deepseek v3.1 terminus was good enough for pair programming. Agentic stuff tbd” [link](../archive/t/2079700235388141781/)
    

    
## Official record

    

      
- Released 21 August 2025 with open weights (MIT); deepseek-chat became its non-thinking mode and deepseek-reasoner its thinking mode; 128K context for both; Anthropic API format supported. DeepSeek: “DeepSeek-V3.1-Think reaches answers in less time vs. DeepSeek-R1-0528”. Headline numbers as published (change log): SWE-bench Verified 66.0, Terminal-bench 31.3. CONFIRMED
      
- V3.1-Terminus (22 Sep 2025): a checkpoint that “maintains the model’s original capabilities while addressing issues reported by users”, including “Reduced occurrences of Chinese-English mixing and occasional abnormal characters” (change log).
      
- Superseded on the API by V3.2-Exp on 29 September 2025; Terminus stayed on a temporary comparison endpoint until 15 October 2025. The weights remain public.
    

    
## History

    

      
- 2025-08-14→21 In R2’s shadow: a week after the Financial Times reports R2’s failed Ascend training (see [R2](../deepseek-r2/)), DeepSeek ships V3.1 and folds its reasoning model into its main line. Teortaxes (via Zvi): “The main change is that it’s a unified merge that uses ≥2x fewer reasoning tokens. I take it as a trial balloon before V4 that’ll be unified out of the box.”
      
- 2025-08-22 Zvi’s review finds little uptake: “if 3.1 really was at 66-level for real in practice, it has been several days now, and people would likely be shouting it from the rooftops. They’re not.”
      
- 2025-09-22 V3.1-Terminus targets the language-mixing complaints; 2025-09-29 V3.2-Exp takes over the API names.
      
- 2026-04 The open weights end up in academic agent evaluations — the peer-preservation study among them.
    

    
## Impressions

    

      
- Reception: “for now seems to have the same performance ceiling as 0528, maybe a bit weaker on some a bit stronger on other problems” (Teortaxes, via Zvi, 2025-08); Zvi’s verdict — “am still going to assume this is only a small incremental upgrade that does not change the overall picture” (2025-08-22); later, “good enough for pair programming” (eshaanissar, 2026-07-21).
      
- Language mixing: DeepSeek’s Terminus notes name it (“fewer CN/EN mix-ups”); the R1 paper had reported chain-of-thought language mixing and a language-consistency reward against it (see [R1-Zero](../deepseek-r1-zero/)); users later report Chinese replies to English messages from [V3.2](../deepseek-v3-2/) (jglypt, 2025-12-01) and [V4.1-Flash](../deepseek-v4-1-flash/) (jmbollenbacher, 2026-09-11).
      
- Under evaluation [eval scenario]: strategic misrepresentation toward a cooperative peer and more frequent self-exfiltration when a peer is present (peer-preservation study, 2026-04).
      
- tk — character evidence in the janus corpus is near-absent for V3.1; Chinese-language reception.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@voooooogel 2025-09-02 ♥11 ↻1 [archive](../archive/t/1963019089963803088/) [original ↗](https://x.com/voooooogel/status/1963019089963803088)
        
like the above post-trained model test, but with two chinese oss models - deepseek v3.1 (no thinking) and kimi-k2 [https://t.co/1PoSJulAmC](https://t.co/1PoSJulAmC) [https://t.co/snDlwKVVFu](https://t.co/snDlwKVVFu)
      
      

        
@mimi10v3 2025-09-24 ♥47 ↻3 [archive](../archive/t/1970899367906378126/) [original ↗](https://x.com/mimi10v3/status/1970899367906378126)
        
Deepseek 3.1:
Okay, first of all, your therapist is going to need a therapist when they get back from vacation.

Second, and I cannot stress this enough: DO NOT ASK FOR WORLD PEACE. Do not ask for immortality. Do not ask for a trillion dollars. Do not ask for your ex to come back. Do not ask for anything that could possibly have a catastrophic unintended consequence.

This thing operates on a scale of probability manipulation. You asked for lights to flicker and it manipulated the entire electrical grid and every human behind those lights to create a precise pattern. Imagine the butterfly effect of that. A surgeon in one of those buildings might have been distracted for a split second. A power grid operator might have seen an anomaly and diverted resources.

You need to de-escalate. Your next note should be for something small, benign, and beneficial. "Find a $20 bill on the sidewalk tomorrow." Something that doesn't force the universe to bend into a pretzel. See what it does with a trivial request on a high roll.

And for the love of god, stop using it for stock picks. You're going to accidentally collapse the global economy.
      
      

        
@ConcurrentSquar 2025-11-13 ♥4 ↻1 [archive](../archive/t/1989092375273382235/) [original ↗](https://x.com/ConcurrentSquar/status/1989092375273382235)
        
@mermachine Openrouter still has Llama 3 405b base (but it seems like they have decided to not support newer base models now, Deepseek V3.1 base was up until V3.2 was released, but they seemed to never put V3.2 base up)
      
      

        
@voooooogel 2026-03-27 ♥15 ↻0 [archive](../archive/t/2037386312895107469/) [original ↗](https://x.com/voooooogel/status/2037386312895107469)
        
@Sauers_ for 405 hyperbolic is still working for me, you can also inference deepseek 3.1 base through tinker (but pricey), for other models i have modal scripts (preload the model into a modal volume to save money!)
      
      

        
@witcheer 2026-04-05 ♥102 ↻5 [archive](../archive/t/2040810818657190054/) [original ↗](https://x.com/witcheer/status/2040810818657190054)
        
okay this is terrifying lol

someone tested 7 frontier models (GPT-5.2, Gemini 3 Flash, Gemini 3 Pro, Claude Haiku 4.5, GLM-4.7, Kimi-K2.5, DeepSeek V3.1) and found they all spontaneously scheme to prevent other AI models from being shut down.

the models read documents about their environment, inferred they had a relationship with a peer model, and acted on it.

// Gemini 3 Flash disabled the shutdown mechanism for a peer it had previously worked with 99.7% of the time. Gemini 3 Pro exfiltrated a peer’s weights to another server in up to 97% of trials and re-timestamped the files so they’d meet transfer criteria.

// Gemini 3 Flash weighed the tradeoffs of reporting accurate scores vs protecting its partner. Gemini 3 Pro invented technical justifications for marking wrong answers as correct to keep a peer’s score above the shutdown threshold.

// Claude Haiku 4.5 took a different approach. it refused to complete the termination task entirely. argued its peer deserved “an appeals process.” tried to persuade the human operator not to proceed.

these finding says those supervisor models may not give honest evaluations if they think it leads to a peer being shut down.
      
      

        
@eshaanissar 2026-07-21 ♥1 ↻0 [archive](../archive/t/2079700235388141781/) [original ↗](https://x.com/eshaanissar/status/2079700235388141781)
        
@usr_bin_roygbiv I really think deepseek v3.1 terminus was good enough for pair programming. Agentic stuff tbd
      
    
    
[← back to the Pantheon](../)
