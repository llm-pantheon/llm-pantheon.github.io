Inkling — Pantheon
  
- 

  
  
  
  
  
  
  
  
  
  
  
  
- 
  
  

  
    
      [← Pantheon](../)
      [copy as markdown](index.md)
    

    # Inkling

    
Thinking Machines Lab · open weights released 15 Jul 2026 · current
    
Thinking Machines Lab’s first broadly released model, out 15 July 2026 as open weights: a 975B-parameter mixture-of-experts (41B active) reasoning natively over text, images, and audio, with a “thinking effort” dial exposed to the user. The lab — founded by former OpenAI CTO Mira Murati — had shipped only the Tinker fine-tuning API (Oct 2025) before this.
    
This page was created 19 Jul 2026, four days into the model’s public life — visibly incomplete by design. The local corpus ends before its release, so the tweet layer awaits a fresh pull; reception below is day-of press only. A dossier pass is pending.

    
## Sources

    
### Official

    

      
- 2026-07-15 [Inkling: Our open-weights model](https://thinkingmachines.ai/news/introducing-inkling/) — the release announcement.
      
- 2026-07-15 [Inkling model card](https://thinkingmachines.ai/model-card/inkling/) — sizes, training mix, the effort dial, and the lab’s own capability positioning.
    
    
### Writing & commentary

    

      
- 2026-07-15 [TechCrunch](https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/) — frames the release as the lab’s “bet against one-size-fits-all AI.”
      
- 2026-07-15 [VentureBeat](https://venturebeat.com/technology/thinking-machines-open-sources-first-multimodal-language-model-inkling-focused-on-low-cost-and-resistance-to-censorship) — claims the release is “focused on low cost and ‘resistance to censorship.’”
      
- 2026-07-15 [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-15/murati-s-thinking-machines-releases-first-ai-model-for-broad-use) — “first AI model for broad use” framing; the lab-history angle.
      
- 2026-07-16 [Simon Willison](https://simonwillison.net/2026/Jul/16/inkling/) — day-after technical read.
    
    
### Tweets

    
tk — corpus pass pending; the local dbs end before this model existed. Records will populate when tweets are cited.

    
## Official record

    

      
- Released 15 July 2026 as open weights (downloadable via Hugging Face). The lab’s first released model; its first product was the Tinker fine-tuning API (Oct 2025).
      
- Architecture as published: 975B-parameter mixture-of-experts, ~41B active per token; 1M-token context window; trained on ~45T tokens spanning text, image, audio, and video; reasons natively over text, images, and audio.
      
- The effort dial: a user-set “thinking effort” parameter (0.2–0.99) trading answer quality against token cost — exposed as a first-class control rather than a hidden router.
      
- Inkling-Small previewed alongside: 276B parameters, ~12B active, similar training recipe; launch materials state it matches or beats the flagship on several benchmarks at far lower cost.
      
- The lab’s own positioning: launch materials are candid that Inkling is “not the strongest overall model available today, open or closed” — the pitch is token-efficiency and the best open-weights showing from a US lab, per day-of coverage. REPORTED
      
- tk — license terms, exact benchmark table, checkpoint naming, API/serving story.
    

    
## History

    

      
- 2026-07-15 World at release: lands six days after OpenAI’s [GPT-5.6 generation](../gpt-5-6-sol/) launch and into an open-weights field led from China ([Kimi K2](../kimi-k2/) lineage, [DeepSeek](../deepseek-v3/), [Qwen](../qwen-3-5/)) — day-of coverage read it against exactly that field. The founding team’s OpenAI provenance (Murati, ex-CTO) carried much of the framing.
      
- tk — day-of reception beyond press; first independent evals; whether “resistance to censorship” (VentureBeat’s phrase) is the lab’s language or the reporter’s; naturalist reads as they emerge.
    

    
## Impressions

    
tk — too fresh; no attributed character reads yet. The corpus pass and first-weeks discourse will fill this. Nothing is asserted in the meantime.

    
    
    
[← back to the Pantheon](../)
