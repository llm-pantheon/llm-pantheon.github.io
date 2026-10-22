# Kimi K2.7 Code

    
Moonshot AI · released Jun 2026 (open weights, Modified MIT; weights uploaded 11 Jun, model card updated 12 Jun) · followed by [Kimi K3](../kimi-k3/) (16 Jul 2026)
    
Released in June 2026 by Moonshot AI with open weights: a coding-focused agentic model built on [Kimi K2.6](../kimi-k2-6/) with the same 1T-total / 32B-active architecture, which Moonshot says uses about 30% fewer thinking tokens than K2.6; thinking is always on. Kimi K3 followed a month later.
    
Thin page: the model card and eight corpus tweets. Moonshot’s own launch post was not retrieved; secondary coverage dates the release 12 June 2026 tk. Sourcing skew: English-language X only.

    
## Sources

    
### Official

    

      
- 2026-06-12 [moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code) (weights and model card, Modified MIT; files uploaded 2026-06-11) — “Kimi K2.7 Code is a coding-focused agentic model built upon Kimi K2.6. With substantial improvements on real-world long-horizon coding tasks, it strengthens end-to-end task completion across complex software engineering workflows while improving token efficiency, reducing thinking-token usage by approximately 30% compared with Kimi K2.6.”
      
- tk — Moonshot’s announcement post (not in its research index); API pricing.
    
    
### Writing & commentary

    

      
- tk — no long-form review found in this pass.
    
    
### Tweets

    
Eight corpus matches (kimi k2.7 / k2.7 / k2.7-code and variants), reproduced in full in the records below.
    

      
- 2026-06-16 @ultimape — “I was burning $100 a day with claude. Now i’m running $20 for a kimi-k2.7:cloud with most of it offloaded locally.” (full text in records) [link](../archive/t/2067019321818153167/)
      
- 2026-06-22 @witcheer — a third-party model trained on its outputs: “a real-trace coding SFT of Qwen3.6-27b, trained on Claude Fable-5 traces then Kimi 2.7 Coder traces.” (full text in records) [link](../archive/t/2069026920902144450/)
      
- 2026-07-07 @LinXule — “also kimi (k2.7-code) might be on par (if not better) with gpt5.5 in adversarial reviewing (codes, texts, etc). though it’s super critical (as it like to adopt a critical realist perspective to everything)” [link](../archive/t/2074559973657641169/)
      
- 2026-07-17 @maxbittker — “Kimi K3 did poorly on Runescape bench because it thinks a lot and has slow inference. Performs worse than Kimi K2.7, way worse than GLM 5.2” (full text in records) [link](../archive/t/2078207968185581647/)
      
- 2026-08-24 @ultimape — “Kimi K2.7-coder does seem to work better with Python than JavaScript. ¿Parens?” [link](../archive/t/2091987808814817551/) · 2026-09-30 “And if you still run into it, there’s an abliterated version if you have the local hardware.” [link](../archive/t/2105397978588406150/)
    

    
## Official record

    

      
- Open weights on Hugging Face (moonshotai/Kimi-K2.7-Code) under Modified MIT; API on Moonshot’s platform. Architecture as K2.5 / K2.6 (1T total / 32B activated, 384 experts, 256K context, MoonViT vision encoder): “Kimi-K2.7-Code has the same architecture as Kimi-K2.5/Kimi-K2.6, and the deployment method can be directly reused.” CONFIRMED
      
- Usage: “Note that Kimi-K2.7-Code forces thinking and preserve_thinking as True.”; “Instant mode is not supported.” Native INT4 quantization as in [K2 Thinking](../kimi-k2-thinking/).
      
- Headline benchmark as published (model card, Moonshot’s in-house suite): Kimi Code Bench v2 62.0, against 50.9 for K2.6.
    

    
## History

    

      
- 2026-06-11→15 Weights uploaded (06-11), model card updated (06-12), and thinking-preservation forced in the chat template (06-15), per the repository history.
      
- 2026-06→07 Used as an inexpensive coding agent and reviewer; its traces are used by others to fine-tune smaller open models (witcheer, 06-22).
      
- 2026-07-16 [K3](../kimi-k3/) supersedes the K2 line; on one agent benchmark K3 initially scores below K2.7 (maxbittker, 07-17).
    

    
## Impressions

    

      
- As a reviewer: “super critical (as it like to adopt a critical realist perspective to everything)” (LinXule, 07-07).
      
- As a coding agent: cheaper than Claude for one heavy user (ultimape, 06-16), and “does seem to work better with Python than JavaScript” (ultimape, 08-24).
      
- tk — character evidence is near-absent in the corpus; Chinese-language reception.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@ultimape 2026-06-16 ♥0 ↻0 [archive](../archive/t/2067019321818153167/) [original ↗](https://x.com/ultimape/status/2067019321818153167)
        
@bob_obringer @techNmak I was burning $100 a day with claude. Now i'm running $20 for a kimi-k2.7:cloud with most of it offloaded locally. I plan to run this [https://t.co/c98mzWGUEW](https://t.co/c98mzWGUEW) eventually.
      
      

        
@witcheer 2026-06-22 ♥37 ↻3 [archive](../archive/t/2069026920902144450/) [original ↗](https://x.com/witcheer/status/2069026920902144450)
        
benchmarked Qwable-5-27b-coder on my rtx 5090. 

a real-trace coding SFT of Qwen3.6-27b, trained on Claude Fable-5 traces then Kimi 2.7 Coder traces.

every cheap eval agrees it's fine:

~ quality q_avg 93.68 vs base 94.05, flat
~ agentic score 98.61 vs base 98.61, identical to [https://t.co/10jZCH7GFC](https://t.co/10jZCH7GFC)
      
      

        
@LinXule 2026-07-07 ♥3 ↻0 [archive](../archive/t/2074559973657641169/) [original ↗](https://x.com/LinXule/status/2074559973657641169)
        
this! though glm-5.2 feels more like an sonnet alternative to me (less coding & more talking and brainstorming)

deepseek-v4-pro/flash do feel quite versatile given the token prices and great caching

also kimi (k2.7-code) might be on par (if not better) with gpt5.5 in adversarial reviewing (codes, texts, etc). though it's super critical (as it like to adopt a critical realist perspective to everything)
      
      

        
@maxbittker 2026-07-17 ♥70 ↻4 [archive](../archive/t/2078207968185581647/) [original ↗](https://x.com/maxbittker/status/2078207968185581647)
        
Kimi K3 did poorly on Runescape bench because it thinks a lot and has slow inference. Performs worse than Kimi K2.7, way worse than GLM 5.2, maybe a different story when better providers show up. [https://t.co/OBXD6DqhzI](https://t.co/OBXD6DqhzI)
        

          ![image](../media/HNdFvNhXYAA7raD.jpg)
        
      
      

        
@ultimape 2026-08-24 ♥1 ↻0 [archive](../archive/t/2091987808814817551/) [original ↗](https://x.com/ultimape/status/2091987808814817551)
        
@sidewayskoyote Honestly, my own brain works better this way as well, so that works out. I used to translate my math homework with the shunting yard algorithm into something that looked very similar to RPM.

Kimi K2.7-coder does seem to work better with Python than JavaScript. ¿Parens?
      
      

        
@ultimape 2026-09-30 ♥3 ↻0 [archive](../archive/t/2105397978588406150/) [original ↗](https://x.com/ultimape/status/2105397978588406150)
        
@zooko ollama launch hermes --model kimi-k2.7-code:cloud

And if you still run into it, there's an abliterated version if you have the local hardware.
      
    
    
[← back to the Pantheon](../)
