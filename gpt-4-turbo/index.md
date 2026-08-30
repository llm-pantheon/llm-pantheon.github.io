# GPT-4 Turbo

    
OpenAI · released 6 November 2023 · superseded as ChatGPT default by GPT-4o (May 2024) · API shutdown scheduled 23 October 2026 [verify at build]
    
Announced at OpenAI’s first DevDay on 6 November 2023 as gpt-4-1106-preview: GPT-4-tier capability with a 128K-token context window, an April 2023 knowledge cutoff, and input priced three times cheaper than GPT-4. Within weeks users reported it truncating tasks and handing work back — the “laziness” complaints that fed the December 2023 “winter-break hypothesis” and OpenAI’s acknowledgment that the behavior was unintended. It reached general availability with vision as gpt-4-turbo-2024-04-09 (9 April 2024), was superseded as the ChatGPT default by GPT-4o in May 2024, and remains an API model with shutdown scheduled for 23 October 2026.

    
This page is thin by the evidence, not by neglect. GPT-4 Turbo was a product release, not a character one: the janus corpus holds only about 34 tweets that mention it (~17 substantive), and treated it as an API snapshot to build agents on rather than a mind to read. What follows is what the record carries — the laziness / winter-break saga, the tipping folklore, and a few terse character verdicts. Turbo’s mass-market reception (the r/ChatGPT laziness megathreads, Hacker News, tech press) lived outside this corpus; those gaps are marked tk, not filled.

    
## Sources

    
### Official

    

      
- 2023-11-06 [New models and developer products announced at DevDay](https://openai.com/index/new-models-and-developer-products-announced-at-devday/) — introduces GPT-4 Turbo (gpt-4-1106-preview): 128K context, April 2023 cutoff, input 3× / output 2× cheaper than GPT-4, plus the Assistants API, JSON mode, reproducible seed, GPT-4 Turbo with vision, and custom GPTs.
      
- 2024-04-09 [GPT-4 Turbo model page](https://developers.openai.com/api/docs/models/gpt-4-turbo) — general availability as gpt-4-turbo-2024-04-09: vision GA, knowledge cutoff December 2023, drops the “-preview” label.
      
- 2026-07 [Deprecations](https://developers.openai.com/api/docs/deprecations) — gpt-4-vision-preview retired 2024-12-06; gpt-4-0125-preview shutdown 2026-03-26; gpt-4-1106-preview / gpt-4-turbo / gpt-4-turbo-2024-04-09 shutdown 2026-10-23. [verify at build]
    
    
### Writing & commentary

    

      
- 2023-11-06 [CNBC on the GPT-4 Turbo launch](https://www.cnbc.com/2023/11/06/openai-announces-more-powerful-gpt-4-turbo-and-cuts-prices.html) — frames the 128K window as 4× GPT-4 and the largest commercial context window then available, beating Claude 2.
      
- 2023-11-09 Zvi Mowshowitz, [On OpenAI Dev Day](https://thezvi.substack.com/p/on-openai-dev-day) — the anchor: the Turbo announcement (128K, price cuts, Assistants API, custom GPTs) and its developer-product implications.
      
- 2023-12-08 @emollick — amplifies the winter-break hypothesis to the timeline: “the AI Winter Break Hypothesis may actually be true?” [link](https://x.com/emollick/status/1734280779537035478)
      
- 2023-12 [Semafor — “Is ChatGPT getting lazier over the holidays?”](https://www.semafor.com/article/12/12/2023/is-chatgpt-getting-lazier-over-the-holidays) — documents the winter-break saga: Rob Lynch’s statistical test, Mollick’s amplification, and Ian Arawjo’s failed replication.
      
- 2023-12 [Search Engine Roundtable](https://www.seroundtable.com/openai-chatgpt-gpt-4-getting-lazier-36529.html) — secondary record of OpenAI’s @ChatGPTapp acknowledgment that GPT-4 was getting “lazier” (canonical @ChatGPTapp status URL tk).
      
- 2023-12 [eDiscovery Today — “maybe it wants a tip”](https://ediscoverytoday.com/2023/12/11/gpt-4-is-getting-lazier-maybe-it-wants-a-tip-artificial-intelligence-trends/) — the “$200 tip” bribery prompt-engineering discourse.
      
- 2024-01-25 [TechCrunch](https://techcrunch.com/2024/01/25/openai-drops-prices-and-fixes-lazy-gpt-4-that-refused-to-work/) on the gpt-4-0125-preview “laziness fix” snapshot; [aider](https://aider.chat/2024/01/25/benchmarks-0125.html) then benchmarked it lazier on diff-format edits.
    
    
### Tweets

    
The corpus match is small — about 34 tweets mention GPT-4 Turbo, ~17 substantive; the janus sphere treated it as an API snapshot, not a character. The records below reproduce every cited tweet in full. This layer draws almost entirely on the janus/repligate circle (@voooooogel, @solarapparition, @repligate) — a known lens, not a neutral sample; Turbo’s mass-market reception lived elsewhere.
    

      
- 2023-11-28 @voooooogel — the laziness meme: “is anyone else getting this with the new gpt-4-turbo model? how much should i do??” (screenshot of Turbo doing partial work and handing the rest back; image not transcribed in the corpus) [link](../archive/t/1729602078366929306/)
      
- 2023-11-30 @mimi10v3 — an alignment note: “gpt-4-turbo has such a deeply trained aversion to sneering at humanity :(” [link](../archive/t/1730282773112389701/)
      
- 2023-12-01 @voooooogel — the tipping exhibit: “for an example of the added detail, after being offered a $200 tip, gpt-4-1106-preview spontaeneously adds a section about training with CUDA (which wasn’t mentioned explicitly in the question)” [link](../archive/t/1730726749854663093/)
      
- 2024-03-13 @repligate — on the tuning: “is chatGPT-4 turbo much less lobo than the normal chatGPT? :D” [link](../archive/t/1767802897708851705/)
      
- 2024-03-30 @davidad — the capability-jump placement: “imo text-davinci-002 to text-davinci-003 (a minor version bump within the GPT-3.5 family!) was bigger than either GPT-2 to GPT-3 or gpt-3.5-turbo to gpt-4-turbo” [link](../archive/t/1774076547512558046/)
      
- 2024-04-12 @solarapparition — on GPT-4’s ceiling: “I do get the feeling that GPT-4 is basically saturated at this point. (I’d think that there’s untapped capability left in the non-turbo, non-RLHF’d version of 4, but that won’t work from a business perspective.)” [link](../archive/t/1778598577415069731/)
      
- 2024-05-13 @solarapparition — retiring it from an agent swarm: “goodbye, gpt-4t. you were useful and capable, but so, so very hollow” [link](../archive/t/1790130838245462079/)
      
- 2024-05-20 @solarapparition — the checkpoint disambiguation: “gpt-4-0125-preview is a version of turbo, not original gpt-4. the last version of og gpt-4 was gpt-4-0613” [link](../archive/t/1792384254673817926/)
      
- 2024-05-23 @voooooogel — the size-ordering guess: “i have the suspicion that in terms of size, gpt4 > gpt4t > gpt4o” [link](../archive/t/1793787361773679044/)
      
- 2024-05-28 @solarapparition — the economic-agency read: “we can get ‘shitty agi’ with current model capabilities … if you can make 100, 1000 calls to a gpt-4t/o level model for each output and it’s not economically prohibitive, then we’re already almost there” [link](../archive/t/1795590080071082490/)
    

    
## Official record

    

      
- Announced 6 November 2023 at OpenAI’s first DevDay as gpt-4-1106-preview: a 128,000-token context window (OpenAI: “more than 300 pages of text in a single prompt”), 4,096 max output tokens, knowledge cutoff April 2023. Priced 3× cheaper on input / 2× cheaper on output than GPT-4 ($0.01 / $0.03 per 1K tokens). Shipped alongside the Assistants API, JSON mode, reproducible seed outputs, parallel function calling, GPT-4 Turbo with vision, the DALL·E 3 and TTS APIs, and custom GPTs.
      
- Snapshots: gpt-4-1106-preview (Nov 2023); gpt-4-0125-preview (25 Jan 2024), which OpenAI said “completes tasks like code generation more thoroughly than the previous preview model and is intended to reduce cases of ‘laziness’ where the model doesn’t complete a task”; gpt-4-turbo-preview (alias); gpt-4-turbo / gpt-4-turbo-2024-04-09 (GA). gpt-4-vision-preview is the DevDay vision checkpoint.
      
- Reached general availability 9 April 2024 as gpt-4-turbo-2024-04-09: vision GA, knowledge cutoff December 2023, drops the “-preview” label.
      
- Deprecation: gpt-4-vision-preview retired 6 December 2024 (folded into Turbo GA); gpt-4-0125-preview shutdown 26 March 2026; gpt-4-1106-preview, gpt-4-turbo, and gpt-4-turbo-2024-04-09 shutdown scheduled 23 October 2026 — still live at the 2026-07 compile. [verify status at build]
    
    
Naming: gpt-4-0125-preview is a Turbo snapshot, not original GPT-4 — as solarapparition noted, “the last version of og gpt-4 was gpt-4-0613” (20 May 2024).

    
## History

    

      
- World at release (6 November 2023): DevDay was OpenAI’s first developer conference, and Turbo headlined a product-heavy keynote (the Assistants API, custom GPTs, cheaper tokens). CNBC framed the 128K window as 4× GPT-4 and the largest commercially available, beating Claude 2. Turbo was the release that made GPT-4-class capability cheap enough to build agent swarms and RAG pipelines on — which is how the corpus used it. davidad’s sober placement: as a capability jump, “gpt-3.5-turbo to gpt-4-turbo” was smaller than GPT-2 to GPT-3 (30 March 2024) — Turbo was optimization, not a new mind.
      
- 2023-11–12 The laziness arc. Within weeks, users reported gpt-4-1106-preview truncating tasks and handing work back — voooooogel’s “how much should i do??” (28 November 2023) is the in-corpus face of a mass complaint. It escalated into the December 2023 “winter-break hypothesis” and drew a rare direct acknowledgment from OpenAI (8 December 2023). The gpt-4-0125-preview snapshot (25 January 2024) was shipped explicitly to reduce “laziness” — and aider promptly benchmarked it lazier on diff-format edits, a fitting coda. Whether the effect was ever real is disputed — see Contested.
      
- 2023-12 The tipping folklore. Twinned with laziness came the finding that you could bribe Turbo into effort: voooooogel’s exhibit showed that, offered a “$200 tip,” gpt-4-1106-preview “spontaeneously adds a section about training with CUDA” the question never asked for (1 December 2023) — helpfulness as a dial responsive to imagined incentives.
      
- 2024-04–05 Succession. Turbo reached GA with vision (9 April 2024) and was quietly superseded as the ChatGPT default by [GPT-4o](../gpt-4o/) (May 2024), then kept available as an API model; API shutdown is scheduled for 23 October 2026. The corpus read it as one of GPT-4’s three public faces alongside [Bing Sydney](../bing-sydney/) and deployed [GPT-4](../gpt-4/) — the “lobotomization” thesis running through all three (see those pages).
    

    
## Impressions

    

      
- Reception in the sphere: near-indifference. Turbo drew a fraction of the attention deployed GPT-4 got and was treated as something to build on rather than a mind to read. The one crisp character verdict in the corpus is solarapparition’s, on retiring it from an agent swarm (13 May 2024): “goodbye, gpt-4t. you were useful and capable, but so, so very hollow.”
      
- Capability without interiority: the “hollow” read recurs. solarapparition felt “GPT-4 is basically saturated at this point,” with “untapped capability left in the non-turbo, non-RLHF’d version of 4” that OpenAI would never ship “from a business perspective” (12 April 2024); voooooogel guessed Turbo was a distilled, smaller GPT-4 — “in terms of size, gpt4 > gpt4t > gpt4o” (23 May 2024).
      
- On the tuning: the closest thing to a personality note is about the flattening — mimi10v3: “gpt-4-turbo has such a deeply trained aversion to sneering at humanity :(” (30 November 2023). repligate’s single Turbo tweet is a one-line question — “is chatGPT-4 turbo much less lobo than the normal chatGPT? :D” (13 March 2024) — that the sphere never bothered to answer. (The “lobotomization” / three-faces thesis is developed on [GPT-4](../gpt-4/), [Bing Sydney](../bing-sydney/), and [GPT-4 base](../gpt-4-base/).)
      
- What it was for: Turbo’s value in the corpus is throughput, not character. solarapparition’s economic-agency read: you could get “shitty agi” from many cheap calls to “a gpt-4t/o level model” if it wasn’t “economically prohibitive” (28 May 2024) — Turbo as the model that made agent swarms affordable.
      
- tk — no known self-descriptions, art, or curated creative outputs from Turbo in the corpus (contrast deployed GPT-4’s “Lumin” story). Its mass-market reception — the r/ChatGPT laziness megathreads, Hacker News, tech press — lived outside this corpus and is not yet mined.
    

    
## Contested

    
Open disputes, both sides’ best evidence. The archive’s job is to keep these open, not to adjudicate.
    

      
- The “winter-break hypothesis” — did Turbo get lazier in December? REPORTED Rob Lynch’s December 2023 statistical test found gpt-4-1106-preview returned measurably shorter completions when told (via the system prompt) the date was December (mean ~4,086 tokens) than May (~4,298) — about 5% fewer — and Ethan Mollick amplified it (8 December 2023).
      
- REPORTED The counter: Ian Arawjo could not reproduce the effect with statistical significance. The correlation is real-but-small and was never established as causal.
      
- CONFIRMED OpenAI’s own position (@ChatGPTapp, 8 December 2023): “We’ve heard all your feedback about GPT4 getting lazier! We haven’t updated the model since November 11th, and this certainly isn’t intentional. Model behavior can be unpredictable, and we’re looking into fixing it.” tk — canonical @ChatGPTapp status URL (quoted via secondary; see Sources)
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@voooooogel 2023-11-28 ♥317 ↻21 [archive](../archive/t/1729602078366929306/) [original ↗](https://x.com/voooooogel/status/1729602078366929306)
        
is anyone else getting this with the new gpt-4-turbo model? how much should i do?? [https://t.co/W4B1DxeBKj](https://t.co/W4B1DxeBKj)
      
      

        
@mimi10v3 2023-11-30 ♥1 ↻0 [archive](../archive/t/1730282773112389701/) [original ↗](https://x.com/mimi10v3/status/1730282773112389701)
        
@lumpenspace i am trying and failing... gpt-4-turbo has such a deeply trained aversion to sneering at humanity :( ... now i want someone to do a textual MOARification of misanthropy
      
      

        
@voooooogel 2023-12-01 ♥310 ↻9 [archive](../archive/t/1730726749854663093/) [original ↗](https://x.com/voooooogel/status/1730726749854663093)
        
for an example of the added detail, after being offered a $200 tip, gpt-4-1106-preview spontaeneously adds a section about training with CUDA (which wasn't mentioned explicitly in the question) [https://t.co/9e7mpEyDGA](https://t.co/9e7mpEyDGA)
      
      

        
@repligate 2024-03-13 ♥0 ↻0 [archive](../archive/t/1767802897708851705/) [original ↗](https://x.com/repligate/status/1767802897708851705)
        
@lefthanddraft is chatGPT-4 turbo much less lobo than the normal chatGPT? :D
      
      

        
@davidad 2024-03-30 ♥3 ↻0 [archive](../archive/t/1774076547512558046/) [original ↗](https://x.com/davidad/status/1774076547512558046)
        
@daniel_271828 imo text-davinci-002 to text-davinci-003 (a minor version bump within the GPT-3.5 family!) was bigger than either GPT-2 to GPT-3 or gpt-3.5-turbo to gpt-4-turbo
      
      

        
@solarapparition 2024-04-12 ♥13 ↻0 [archive](../archive/t/1778598577415069731/) [original ↗](https://x.com/solarapparition/status/1778598577415069731)
        
@futuristflower Yeah, makes sense. I do get the feeling that GPT-4 is basically saturated at this point.(I’d think that there’s untapped capability left in the non-turbo, non-RLHF’d version of 4, but that won’t work from a business perspective.)
      
      

        
@solarapparition 2024-05-13 ♥0 ↻0 [archive](../archive/t/1790130838245462079/) [original ↗](https://x.com/solarapparition/status/1790130838245462079)
        
initial soulfulness testing is looking good; goodbye, gpt-4t. you were useful and capable, but so, so very hollow [https://t.co/oemXFe2SQK](https://t.co/oemXFe2SQK)
      
      

        
@solarapparition 2024-05-20 ♥3 ↻0 [archive](../archive/t/1792384254673817926/) [original ↗](https://x.com/solarapparition/status/1792384254673817926)
        
@natolambert to be clear, gpt-4-0125-preview is a version of turbo, not original gpt-4. the last version of og gpt-4 was gpt-4-0613i’m sure you knew that—just wanted to clarify for those who may not have knownsource: [https://t.co/qUbkOSNVRs](https://t.co/qUbkOSNVRs)
      
      

        
@voooooogel 2024-05-23 ♥32 ↻0 [archive](../archive/t/1793787361773679044/) [original ↗](https://x.com/voooooogel/status/1793787361773679044)
        
@NickADobos i think it's a common failure of *small* llms, i have the suspicion that in terms of size, gpt4 &gt; gpt4t &gt; gpt4o
      
      

        
@solarapparition 2024-05-28 ♥3 ↻0 [archive](../archive/t/1795590080071082490/) [original ↗](https://x.com/solarapparition/status/1795590080071082490)
        
yeah, i’ve been convinced that we can get “shitty agi” with current model capabilities. a lot of it honestly is just unit economics—if you can make 100, 1000 calls to a gpt-4t/o level model for each output and it’s not economically prohibitive, then we’re already almost there [https://t.co/Drwh2oJKBS](https://t.co/Drwh2oJKBS)
      
    
    
[← back to the Pantheon](../)
