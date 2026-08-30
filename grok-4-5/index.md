# Grok 4.5

    
SpaceXAI (xAI) · released 8 Jul 2026 · superseded by Grok 4.6 (Aug 2026)
    
Released 8 July 2026 by SpaceXAI (Musk’s xAI, under its SpaceXAI branding) as a model pitched at coding, agentic work, and knowledge work rather than chat — distributed through [Grok Build](../grok-build/), the SpaceXAI API console, and Cursor, the coding editor SpaceXAI had acquired weeks earlier and on whose developer-session data it was trained. Built on the V9 foundation (reported at ~1.5T parameters; SpaceXAI published no parameter count), priced at $2/$6 per million tokens with a reported 500K-token context window, and framed by Musk as “roughly comparable to [Opus 4.7](../claude-opus-4-7/), but much faster.” It is not [Grok 5](../grok-5/) (the ~6T model still training on Colossus 2); Grok 4.6 superseded it in August 2026.
    
Thin — an official/web-sourced seed. Grok 4.5 launched 8 July 2026; the local janus corpus ends 2 July 2026, so there is no naturalist tweet layer here yet and the character record is tk. What is solid is the launch record below. Sourcing skew, named: this page rests on SpaceXAI’s and Cursor’s own posts, Axios’s scoop, and technical-press writeups — mainstream coverage, not the janus-sphere naturalism the site usually carries.

    
## Sources

    
### Official

    

      
- 2026-07-08 [Grok 4.5](https://x.ai/news/grok-4-5) (SpaceXAI announcement) — positions the model for coding, agentic tasks and knowledge work; carries the SWE benchmark figures and $2/$6 pricing. (automated fetch returns the benchmark/pricing specs but a garbled publication date; the 8 Jul date is fixed by Axios, the Cursor post and Wikipedia below)
      
- 2026-07-08 [Grok 4.5 is now available](https://forum.cursor.com/t/grok-4-5-is-now-available/165158) (Cursor, the co-developer) — the availability post: “Today we are releasing Grok 4.5 together with SpaceXAI, our most intelligent model and the first we’ve built for more than software engineering”; three effort levels; on all Cursor plans; “Grok 4.5 will become available in the EU in the coming weeks.”
    
    
### Writing & commentary

    

      
- 2026-07-08 Axios, [Scoop: Musk’s SpaceXAI releases new model, Grok 4.5](https://www.axios.com/2026/07/08/spacexai-grok-new-model) — the scoop; carries Musk’s framing of Grok 4.5 as “roughly comparable to Opus 4.7, but much faster” and “more token-efficient and lower cost,” and calls it SpaceXAI’s first release since going public and acquiring Cursor. (403s to automated fetch; quote via the search index and corroborated by the Fello AI writeup below)
      
- reference [Grok (chatbot) — Wikipedia](https://en.wikipedia.org/wiki/Grok_(chatbot)) — running timeline: the version progression (4.1 → 4.20 → 4.3 → 4.5 → 4.6), the V9 / ~1.5T foundation, Cursor as an “incoming SpaceXAI subsidiary,” GB300 training, and EU-availability timing (targeting mid-July 2026).
      
- 2026-07 DataCamp, [Grok 4.5: Features, Benchmarks, Pricing, and Tests](https://www.datacamp.com/blog/grok-4-5) — independent writeup: Artificial Analysis Intelligence Index 54 (up from Grok 4.3’s 38), a 500K-token context window (down from Grok 4.3’s ~1M), and a mixed coding picture against [Opus 4.8](../claude-opus-4-8/) (ahead on SWE Marathon 29% vs 26%, behind on SWE-Bench Pro 64.7% vs 80.4%); notes “neither SpaceXAI nor Cursor has published a parameter count.”
      
- 2026-08 Fello AI, [Grok 4.5: Specs, Benchmarks, Pricing Explained](https://felloai.com/grok-4-5/) — reports the Cursor acquisition (mid-June 2026, ~$60B) and Grok 4.6 (12 Aug 2026) as a same-foundation post-training upgrade superseding Grok 4.5.
    
    
### Tweets

    
tk — no corpus coverage: the local janus corpus ends 2 July 2026, before the 8 July launch, so there is no naturalist tweet layer yet. Musk’s launch posts on X are the source of the “comparable to Opus 4.7” framing (quoted under Official record via Axios’s reporting); verified status-URL permalinks are tk — not guessed.

    
## Official record

    

      
- Released 8 July 2026 by SpaceXAI: a coding-, agent- and knowledge-work model shipped through [Grok Build](../grok-build/) (free for a limited time), Cursor (all plans) and the SpaceXAI API console. Not available in the EU at launch; EU access said to be coming “in the coming weeks” (Cursor), targeted mid-July (Wikipedia). CONFIRMED
      
- Pricing: $2 / $6 per million tokens (input / output), with a discounted cached-input rate. CONFIRMED
      
- Headline benchmarks as published (SpaceXAI’s own figures, from the announcement): SWE-Bench Pro 64.7% and Terminal Bench 2.1 83.3%, with a claimed token-efficiency edge (“4.2× fewer tokens” on SWE-Bench Pro) and throughput ~80 tokens/sec. CONFIRMED (as published) (independent scoring in History)
      
- Foundation: V9. No official parameter count was published (DataCamp); the widely-cited ~1.5T figure is reporting, not a lab disclosure (see History). Context window reported at 500K. REPORTED (params & context)
      
- Reasoning: three configurable effort levels (per the Cursor announcement).
      
- tk — model card / system card (whether one exists); the exact officially-documented context window; deprecation / API status now that Grok 4.6 has shipped.
    

    
## History

    

      
- 2026-06 The Cursor acquisition: SpaceXAI acquires Cursor (mid-June 2026; ~$60B, per Fello AI), bringing the coding editor in-house — and Grok 4.5 is trained on Cursor developer-session data, a data flywheel from the tool it ships inside. REPORTED (the price and exact date are Fello AI’s; Wikipedia calls Cursor an “incoming SpaceXAI subsidiary”)
      
- 2026-07-08 Launch: SpaceXAI — in coverage, its first release since going public — ships Grok 4.5 into the coding-agent race, roughly a week after OpenAI’s [GPT-5.6](../gpt-5-6/) generation and amid Cursor-centered rivalry, positioned explicitly against Anthropic’s Opus line on cost and speed rather than as a conversational character. Musk: “roughly comparable to Opus 4.7, but much faster” (Axios). No EU availability at launch.
      
- 2026-07 Independent benchmarking: Artificial Analysis placed its Intelligence Index at 54 — reported as #4 overall at the time (behind Fable 5, [GPT-5.5](../gpt-5-5/) and [Opus 4.8](../claude-opus-4-8/)) with a top placement on agentic tool use — while the coding results were mixed against Opus 4.8 (ahead on SWE Marathon, behind on SWE-Bench Pro). (DataCamp) REPORTED
      
- 2026-08-12 Succeeded: Grok 4.6 ships as a post-training upgrade on the same V9 foundation, superseding Grok 4.5, with further 4.6 / 4.7 releases being trailed. (Fello AI; Wikipedia timeline) REPORTED
      
- tk — day-of naturalist reception; how Grok 4.5 sits against the MechaHitler-era Grok reputation (see [Grok 4](../grok-4/)); whether it reads as a distinct character or as a developer instrument; the Cursor data-flywheel / developer-data discourse.
    

    
## Impressions

    
tk — too new for a naturalist layer, and the corpus ends before launch, so no dated, attributed character reports exist yet. The only character-adjacent signal so far is positioning, not observed behavior: SpaceXAI shipped Grok 4.5 as a coding/agent tool benchmarked against the Opus line rather than as a persona — whether it reads as a distinct character or purely as a developer instrument, and how it carries the MechaHitler-era Grok reputation (see [Grok 4](../grok-4/)), is exactly what a later pass must collect.

    
    

    
[← back to the Pantheon](../)
