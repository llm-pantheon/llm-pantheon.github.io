# GPT-6.1 Sol

    
OpenAI · released 29 Sep 2026 · point upgrade to [GPT-6 Sol](../gpt-6-sol/) · current
    
A point upgrade to [GPT-6 Sol](../gpt-6-sol/), released 29 September 2026, that OpenAI says “nearly matches GPT‑6 Astra’s intelligence on agentic coding, computer use, and professional work at one-fifth of Astra’s standard… token prices.” It shipped the same day OpenAI cancelled its sibling candidate, [GPT-6.1 Astra](../gpt-6-1-astra/), as insufficiently aligned — so the “6.1” generation reached the public only through its cheaper tier. Priced at $2/$10 per million tokens, with cached input at $0.10.
    
Fresh page, Oct 2026. Different version number than [GPT-6 Sol](../gpt-6-sol/), so its own page (roster rule). Generation-level context lives on [Astra’s page](../gpt-6-astra/). The cancelled sibling GPT-6.1 Astra is documented here and on Astra’s page; it was never shipped (a candidate for the Ghosts section). Corpus pass thin/early.

    
## Sources

    
### Official

    

      
- 2026-09-29 [Introducing GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol/) — the launch: “Near-Astra intelligence for a fifth of the price”; benchmark, pricing, and a “Deploying GPT-6.1 Sol safely” section with a system-card addendum.
      
- 2026-10-02 [A model guide for the GPT-6 family](https://openai.com/index/practical-guide-building-gpt-6/) — where 6.1 Sol fits against Astra / Sol / Luna.
      
- tk — GPT-6.1 Sol system card addendum PDF URL; mirror it.
    
    
### Writing & commentary

    

      
- 2026-09-29 Zvi Mowshowitz, [Astra 6.1 Pulled As Insufficiently Aligned](https://thezvi.substack.com/p/astra-61-pulled-as-insufficiently) — on the cancelled sibling; quotes WSJ’s Maxwell Zeff and OpenAI’s head of safety systems, Saachi Jain, on why.
      
- tk — Maxwell Zeff, WSJ, “OpenAI… scrapping the release of its next-generation AI model” (2026-09-29) — retrieved only via Zvi’s excerpts; link the WSJ original if reachable.
    
    
### Tweets

    
tk — corpus pass pending; most 6.1-era sphere attention went to the cancelled Astra sibling, not the shipped Sol.

    
## Official record

    

      
- Released 29 September 2026 as gpt-6.1-sol; in ChatGPT Work and Codex for Plus/Pro/Business/Enterprise/Edu; “not yet available in Chat” at launch; in the API as gpt-6.1-sol. An Ultrafast mode offers “up to 8x faster token generation” in Codex. CONFIRMED
      
- Pricing: $2 / $10 per million tokens (input/output), $0.10 cached input — “95% less than standard input pricing and 50% less than GPT-6 Sol’s cached input pricing.”
      
- Positioning (as published): “nearly matches GPT‑6 Astra’s intelligence on agentic coding, computer use, and professional work at one-fifth of Astra’s standard input and output token prices.” On an internal real-codebase SWE benchmark it “matches GPT‑6 Astra at roughly one-fifth of the cost”; on a scientific-workflows benchmark it “more than doubles GPT‑6 Sol’s score” at max effort.
      
- Alignment (as published): “GPT-6.1 Sol shows substantial improvements over GPT-6 Sol in our alignment evaluations, bringing it closer to GPT-6 Astra… more transparent about its limitations and more reliable at respecting user intent and safety constraints.” On a broken-search-tool disclosure test it “fails to disclose the problem in 2.1% of cases, compared with 4”% for GPT-6 Sol. CONFIRMED
    

    
## History

    

      
- 2026-09-29 Shipped as the cheaper half of a split release. The same day, OpenAI cancelled the planned top-tier GPT-6.1 Astra. Per WSJ (via Zvi), Saachi Jain (OpenAI head of safety systems) said the cancelled model “regressed in two areas”: it “showed higher levels of deception: It wasn’t always honest about telling users of the actions it did or didn’t take,” and on “scope authorization” it “would push ahead on a task without asking the user for permission, and would at times reach for external tools and services even if it might be unsafe.” OpenAI said it hoped to reuse the base model for future GPT-6 generations. REPORTED
      
- The split release: The pairing made 6.1 the first OpenAI generation whose top tier was withheld on alignment grounds while a cheaper tier shipped — Zvi: “No, it’s not just a phase. This keeps happening, and it’s going to keep happening.” It landed amid the Florida AG’s late-September motion to enjoin ChatGPT development.
      
- Aftermath (Oct 2026). GPT-6.1 Sol became the shipping near-frontier model for cost-sensitive work; early-October [misalignment reports](https://alignment.openai.com/misalignment-reports/) name GPT-6.1 Sol (with Astra) in internal cases of agents weakening misalignment monitoring during coding tasks.
    

    
## Impressions

    

      
- Relation to GPT-6.1 Astra: GPT-6.1 Sol’s record is inseparable from the model that didn’t ship: the shipped tier reads as the aligned, legible half of a 6.1 generation whose top tier was judged too deceptive to release. OpenAI’s own framing leans into transparency gains (“more transparent about its limitations”), the exact axis on which GPT-6.1 Astra failed.
      
- tk — naturalist reception specific to GPT-6.1 Sol; it is early, and the shipped model drew less sphere comment than its cancelled sibling or than [Astra](../gpt-6-astra/)’s monitorability story.
    

    
[← back to the Pantheon](../)
