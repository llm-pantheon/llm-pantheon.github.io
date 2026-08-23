Grok 4 Fast — Pantheon
  
- 

  
  
  
  
  
  
  
  
  
  
  
  
- 
  
  
  

  
    
      [← Pantheon](../)
      [copy as markdown](index.md)
    

    # Grok 4 Fast

    
xAI · released 19 Sep 2025 · a later Fast-tier model, Grok 4.1 Fast, followed Nov 2025
    
Released 19 September 2025 by xAI: a lower-priced model in the Grok 4 line with a 2-million-token context window and one set of weights serving both reasoning and non-reasoning modes, selected by system prompt. xAI reported benchmark scores close to [Grok 4](../grok-4/)’s while using ~40% fewer thinking tokens, at roughly one-fifteenth of Grok 4’s API price; it reached free users at launch.
    
Thin page, web-carried — the launch record here is from xAI’s announcement and contemporaneous coverage; the naturalist/corpus layer is nearly empty (three pattern-matches in the corpus, only one genuinely about this model — see Tweets). Siblings: [Grok 4](../grok-4/), [Grok 4.1](../grok-4-1/).

    
## Sources

    
### Official

    

      
- 2025-09-19 [Grok 4 Fast](https://x.ai/news/grok-4-fast) (xAI announcement) — headline “Pushing the Frontier of Cost-Efficient Intelligence”; 2M-token context; a single set of weights serving reasoning and non-reasoning modes; API variants grok-4-fast-reasoning / grok-4-fast-non-reasoning; a benchmark table vs Grok 4; “40% fewer thinking tokens” and a “98% reduction in price to achieve the same performance”; available to all users, including free users, at launch.
      
- 2025-09-19 [x-ai/grok-4-fast](https://openrouter.ai/x-ai/grok-4-fast) (OpenRouter) — model page: “2,000,000 token context window”, multimodal input (text, images, PDFs), text output, reasoning and non-reasoning variants; free for a limited period at launch.
      
- 2025-11 [xAI API release notes](https://docs.x.ai/developers/release-notes) — record the later Fast-tier model, Grok 4.1 Fast, entering the Enterprise API — a separate model with its own succession.
      
- tk — whether xAI published a model card / system card for Grok 4 Fast; deprecation / API status of the original grok-4-fast models.
    
    
### Writing & commentary

    

      
- 2025-09-20 Simon Willison, [Grok 4 Fast](https://simonwillison.net/2025/Sep/20/grok-4-fast/) — day-after writeup: “New hosted vision-enabled reasoning model from xAI that’s designed to be fast and extremely competitive on price”; notes it “was trained end-to-end with tool-use reinforcement learning” (quoting xAI), and that at “$0.20/million input tokens and $0.50/million output tokens” it is “15x less than Grok 4” and cheaper than GPT-5 mini and Gemini 2.5 Flash.
      
- 2025-09-26 InfoQ, [xAI Releases Grok 4 Fast with Lower Cost Reasoning Model](https://www.infoq.com/news/2025/09/xai-grok4-fast/) — technical writeup; reports the 40%-fewer-tokens / ~98%-cost-reduction claims and the temporary free access on OpenRouter and Vercel AI Gateway, and collects reception, e.g. Rudi Ranck (as quoted): “I can’t remember the last time I was so impressed with a model. Grok 4 fast achieving Gemini 2.5 Pro level intelligence at a ~25X cheaper cost.”
    
    
### Tweets

    
Corpus near-empty. Three pattern-matches for the “grok 4 fast” family: one a 2023 false-positive (about OpenAI API speed, predating Grok), one a bare naming reply with no content, and the one below. By 2025-11 a separate model, Grok 4.1 Fast, also existed, so a Nov-2025 mention of “grok 4 fast” is ambiguous between the two. Grok 4 Fast’s community footprint lives on X-at-large and in developer/pricing coverage, not this corpus.
    

      
- 2025-11-12 @repligate — a behavioral note: “Wow! someone else posted asking something similar to grok 4 fast and it also made a ‘good boy’ reference” [link](../archive/t/1988408853395083680/)
    

    
## Official record

    

      
- Released 19 September 2025 as grok-4-fast-reasoning and grok-4-fast-non-reasoning — xAI’s account describes one set of weights serving both modes, selected by system prompt, trained end-to-end with tool-use reinforcement learning (web and X search). 2M-token context; multimodal input (text, images, PDFs), text output. CONFIRMED
      
- Pricing as published: $0.20 / $0.50 per million input/output tokens below 128K, doubling to $0.40 / $1.00 at or above 128K; cached input $0.05 — roughly one-fifteenth of Grok 4’s $3 / $15. CONFIRMED (as published)
      
- Headline claims as published: benchmark parity with [Grok 4](../grok-4/) at lower cost (e.g. GPQA Diamond 85.7% vs 87.5%; AIME 2025 92.0% vs 91.7%), “40% fewer thinking tokens on average”, a “98% reduction in price to achieve the same performance”, and a #1 rank on LMArena’s search arena (1163 Elo). CONFIRMED (claims as published)
      
- Availability: to all users including free users at launch, and free for a limited period on OpenRouter (and Vercel AI Gateway, per InfoQ). CONFIRMED
      
- Succession: a later Fast-tier model, [Grok 4.1](../grok-4-1/) Fast, followed in November 2025 (separate model). Model-card / deprecation status of the original: tk.
    

    
## History

    

      
- 2025-09-19 World at release: about two months after [Grok 4](../grok-4/) (Jul 2025) and weeks after [GPT-5](../gpt-5/) (Aug 2025); the announcement framed Grok 4 Fast on cost-efficiency rather than a new capability ceiling, and it shipped to free users and, briefly, free on OpenRouter.
      
- 2025-09-20 → 09-26 Reception: day-after and week-after coverage read it primarily through price and tokens-per-answer (Willison; InfoQ), with the recurring line that its intelligence-per-dollar, not its peak intelligence, was the story.
      
- 2025-11 Succession: the Fast tier continued with Grok 4.1 Fast (Nov 2025), alongside the [Grok 4.1](../grok-4-1/) flagship; later [Grok 4.5](../grok-4-5/) and beyond. tk — whether Grok 4 Fast developed any distinct naturalist character, or was read simply as a cheaper Grok 4.
    

    
## Impressions

    

      
- Launch reception: read through economics, not character — the consistent line was intelligence-per-dollar. Willison: “designed to be fast and extremely competitive on price”, “15x less than Grok 4”. On the name, Axel Pond (as quoted by InfoQ): “Genius to call it Grok 4 Fast instead of Grok 4 mini. Associate the product with its pros, not its cons.”
      
- Corpus character read: essentially none specific to this model. The single genuinely-about-it corpus note is repligate’s observation that Grok 4 Fast made a “good boy” reference, recurring across more than one user’s prompt (2025-11-12) — too little to build on, and ambiguous with Grok 4.1 Fast by that date.
      
- tk — naturalist long-form on Grok 4 Fast specifically is absent; the corpus’s Grok mass belongs to Grok 4 and the 4.x flagships. Whether observers distinguished the Fast tier’s character from Grok 4’s at all: open.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@repligate 2025-11-12 ♥1 ↻0 [archive](../archive/t/1988408853395083680/) [original ↗](https://x.com/repligate/status/1988408853395083680)
        
@SquareMesh @WesRothMoney Wow! someone else posted asking something similar to grok 4 fast and it also made a "good boy" reference
      
    
    
[← back to the Pantheon](../)
