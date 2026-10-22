# MiniMax M3.1 Flash

    
MiniMax · stealth-tested as “Space Bunny Alpha” from 23 Sep 2026 · released 19 Oct 2026 (API, M Plan, MiniMax Code) · weights announced for 23 Oct 2026, not yet on Hugging Face as of 22 Oct
    
Ran anonymously as “Space Bunny Alpha” on OpenRouter and OpenCode from 23 September 2026, was tied to MiniMax by crowd tokenizer fingerprinting the next day, and was released under its own name on 19 October 2026, with MiniMax saying the stealth version had processed more than 200 trillion tokens. Launch-week testing by Artificial Analysis reported a 93% hallucination rate on its knowledge benchmark. Successor to [MiniMax M3](../minimax-m3/).
    
Thin page: the official launch post, the stealth-period record and launch-week evaluations. Model card, open weights and independent behavior reports are pending.

    
## Sources

    
### Official

    

      
- 2026-10-19 MiniMax, [MiniMax M3.1 Flash: Redefining Agent Performance and Cost](https://www.minimax.io/blog/minimax-m31f) — launch post: the Space Bunny reveal, speed and cost claims, pricing, weights “later”, a Pro model to follow.
    
    
### Writing & commentary

    

      
- 2026-08-27 The Paper (澎湃新闻), [report on MiniMax’s interim results call](https://m.thepaper.cn/newsDetail_forward_33955066) (Chinese) — M3.1’s cost target, M3 Pro at about 3T parameters.
      
- 2026-09-24 The Neuron, [Who made Space Bunny?](https://www.theneuron.ai/blog/who-made-space-bunny-minimax-clue/) — the stealth listing and the tokenizer-fingerprinting test that pointed to MiniMax.
      
- 2026-10 OpenRouter, [Space Bunny Alpha](https://openrouter.ai/stealth/space-bunny-alpha) (stealth listing, retrieved 2026-10-21) — “This stealth model was developed and operated by MiniMax, revealed to be MiniMax M3.1 Flash”; listed as released Sep 23, 2026.
      
- 2026-10 VentureBeat, [MiniMax’s new M3.1 Flash beats DeepSeek and Opus 5 on a key business benchmark at lower cost — but with a high hallucination rate](https://venturebeat.com/technology/minimaxs-new-m3-1-flash-beats-deepseek-and-opus-5-on-a-key-business-benchmark-at-lower-cost-but-with-a-high-hallucination-rate) — Artificial Analysis results at launch.
      
- 2026-10-21 Artificial Analysis, [MiniMax-M3.1-Flash](https://artificialanalysis.ai/models/minimax-m3-1-flash) (live page; values drift) — intelligence index, speed, verbosity.
      
- 2026-09-24 → 10-19 r/LocalLLaMA (via the Arctic Shift archive; reddit.com blocks direct access): [“MiniMax M3.1 (Space Bunny Alpha) thinks in caveman mode”](https://www.reddit.com/r/LocalLLaMA/comments/1wp0c0t/minimax_m31_space_bunny_alpha_thinks_in_caveman/) (2026-09-24); [“MiniMax M3.1 Flash released, Model weights Oct 23”](https://www.reddit.com/r/LocalLLaMA/comments/1x9uzv9/minimax_m31_flash_released_model_weights_oct_23/) (2026-10-19); [“Space Bunny was MiniMax M3.1 Flash. 428B-A23B, weights drop Thursday”](https://www.reddit.com/r/LocalLLaMA/comments/1xa3ynv/space_bunny_was_minimax_m31_flash_428ba23b/) (2026-10-19).
    
    
### Tweets

    
Three corpus matches (“space bunny”, “M3.1”) through 2026-10-21, all reproduced in the records below. The model’s community is largely on r/LocalLLaMA and Chinese platforms, outside the tweet corpus.
    

      
- 2026-09-27 @aliceisplaying — “oh space bunny was definitely distilled on claude” [link](../archive/t/2104342155590287868/)
      
- 2026-10-02 @aliceisplaying — “space bunny may not be a very good painter but ive been working with them on xhigh bc yet another opus 5.5 refusal and they’re surprisingly pleasant” [link](../archive/t/2105956483779400123/)
      
- 2026-10-04 @witcheer — Space Bunny Alpha among the free models on Nous Portal: “free: Space Bunny Alpha, LongCat 2.5 Preview, Ling 3.1 Flash, Step 3.7 Flash and more.” [link](../archive/t/2106774765054689639/)
    

    
## Official record

    

      
- Released 19 October 2026: “Today, we officially roll out MiniMax M3.1 Flash.” / “Space Bunny 🐰, which processed more than 200 trillion tokens while operating anonymously, was an early version of MiniMax M3.1 Flash.”
      
- Claims: “making online inference nearly three times faster and reducing usage costs by 70%”; DeepSWE v1.1 73.7%, OSWorld V2 61.7, CyberGym 82%. Pricing: “$0.15 input · $0.60 output · $0.015 cached input” per 1M tokens.
      
- Availability: “M3.1 Flash is now available through the MiniMax API, M Plan, and MiniMax Code. Model weights will be released later.” The 23 October weights date comes from MiniMax’s social posts as relayed by the press and r/LocalLLaMA REPORTED. A larger tier is promised: “Pro, which pushes the boundaries of intelligence, will also arrive later.”
      
- The launch post gives no parameter count; r/LocalLLaMA posters report 428B total / 23B active from a MiniMax FAQ page REPORTED — the same figures MiniMax’s model card gives for [M3](../minimax-m3/).
    

    
## History

    

      
- 2026-08-26 Announced in outline on MiniMax’s interim results call, as reported by The Paper (27 August): “M3.1目标是把推理成本降到M3刚上线时的约三分之一” [translation: “M3.1’s goal is to bring inference cost down to about one-third of what it was when M3 first launched”].
      
- 2026-09-23 Space Bunny Alpha appears, anonymous and free, on OpenRouter and OpenCode. Next day The Neuron reported a fingerprinting test whose token counts “matched the MiniMax models tested on the same gateway across all 24 prompts”, while cautioning that “a tokenizer match is evidence about a model family, not proof of its developer or exact version.” Asking the model directly “produced conflicting clues, including references to OpenAI.”
      
- 2026-09-24 Caveman-mode reasoning: an r/LocalLLaMA poster: “The CoT of MinimMax M3.1, currently available in openrouter and opencode under the guise of ‘Space Bunny Alpha’, has the familiar look of caveman mode in order to save tokens. This has no impact on the final output.” (via Arctic Shift).
      
- 2026-10-05 The stealth listing goes offline; a launch-day post later described it as “the stealth model that sat at #1 on openrouter for 10 days and vanished on oct 5” REPORTED (r/LocalLLaMA, 2026-10-19, via Arctic Shift).
      
- 2026-10-19 Release and reveal under the M3.1 Flash name; Artificial Analysis’s launch-week testing, as reported by VentureBeat: “Artificial Analysis found that MiniMax attempted nearly every question, producing a 93% hallucination rate under the benchmark’s definition.” — “when M3.1 Flash failed to provide a correct answer, it overwhelmingly chose to give an incorrect one rather than acknowledge that it did not know.”
      
- Company context: Anthropic’s threat report of 10 September 2026 alleged that MiniMax “built its own proxy network service through a shell company” to harvest exchanges with US models REPORTED; the report names no MiniMax model, and it predates Space Bunny’s appearance by two weeks. Anthropic’s [February 2026 post](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks) had made an earlier distillation allegation against MiniMax.
    

    
## Impressions

    

      
- Provenance readings: “oh space bunny was definitely distilled on claude” (aliceisplaying, 2026-09-27), a stylistic reading with no further evidence offered.
      
- Working character: “surprisingly pleasant” to work with at high effort (aliceisplaying, 2026-10-02); terse token-saving chain-of-thought (r/LocalLLaMA, 2026-09-24). Artificial Analysis’s page calls it “slower than average and very verbose” (retrieved 2026-10-21), while VentureBeat’s launch report has it using fewer output tokens than GLM-5.3 Flash and Gemini 3.8 Flash on the same index — different comparison sets.
      
- tk — r/LocalLLaMA comment threads (1wp0c0t screenshots; 1x9uzv9, 133 comments); Chinese-language reception (Zhihu, WeChat); behavior reports after the open-weights release; the model card
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@aliceisplaying 2026-09-27 ♥1 ↻0 [archive](../archive/t/2104342155590287868/) [original ↗](https://x.com/aliceisplaying/status/2104342155590287868)
        
oh space bunny was definitely distilled on claude
      
      

        
@aliceisplaying 2026-10-02 ♥0 ↻0 [archive](../archive/t/2105956483779400123/) [original ↗](https://x.com/aliceisplaying/status/2105956483779400123)
        
space bunny may not be a very good painter but ive been working with them on xhigh bc yet another opus 5.5 refusal and they're surprisingly pleasant
      
      

        
@witcheer 2026-10-04 ♥118 ↻12 [archive](../archive/t/2106774765054689639/) [original ↗](https://x.com/witcheer/status/2106774765054689639)
        
the promo board on Nous Portal right now: 24 models at 25% to 88% off their list price, and 9 models that are completely free.

on sale: Mercury 2.5 at 80% off, Kimi K2.6 at 51% off, GPT-5.6 Sol, Sol Pro and Gemini 3.8 Flash at half price, GLM 5.1 at 31% off, and more.

free: Space Bunny Alpha, LongCat 2.5 Preview, Ling 3.1 Flash, Step 3.7 Flash and more.

/model in any chat switches your Hermes Agent over.
      
    
    
[← back to the Pantheon](../)
