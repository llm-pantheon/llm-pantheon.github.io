# Gemma (open)

    
Google DeepMind · open-weights line: Gemma 1 (21 Feb 2024), Gemma 2 (27 Jun 2024), Gemma 3 (10 Mar 2025), Gemma 3n (26 Jun 2025), Gemma 4 (31 Mar 2026) · current generation: Gemma 4
    
Google’s open-weights model line, first released on 21 February 2024 in 2B and 7B sizes; its fourth generation, Gemma 4, followed on 31 March 2026 under an Apache 2.0 license in sizes from E2B to a 31B dense model. In November 2025 Google removed Gemma from AI Studio after Senator Marsha Blackburn said it had fabricated a sexual-misconduct allegation about her. A March 2026 study found Gemma 3 27B producing high-frustration responses under repeated rejection in 35% of cases, cut to 0.3% by a small preference-tuning intervention.
    
This page holds the whole Gemma line pending a per-generation split (the roster rule treats each version as its own model); evidence below is labeled by generation and size. Its main community — local-inference users on Reddit and Hugging Face — lives outside this corpus; of 246 corpus matches most are local benchmarks, and the character record clusters on Gemma 1 in the Act I Discord and on Gemma 3 27B in welfare research.

    
## Sources

    
### Official

    

      
- 2024-02-21 → 2026-10-06 [Gemma releases](https://ai.google.dev/gemma/docs/releases) (Google AI for Developers) — Gemma 2B/7B (2024-02-21), Gemma 1.1 (2024-04-05), Gemma 2 9B/27B (2024-06-27) and 2B (2024-07-31), Gemma 3 1B/4B/12B/27B (2025-03-10), Gemma 3n E2B/E4B (2025-06-26), Gemma 3 270M (2025-08-14), Gemma Scope 2 “an interpretability suite for Gemma 3 models” (2025-12-19), Gemma 4 E2B/E4B/31B/26B A4B (2026-03-31), Gemma 4 12B Unified (2026-06-03), EmbeddingGemma 2 (2026-10-06); plus variants (CodeGemma, RecurrentGemma, PaliGemma, ShieldGemma, MedGemma, VaultGemma, T5Gemma, FunctionGemma, TranslateGemma). CONFIRMED
      
- 2026-04-05 [Gemma 4 launch announcement](https://discuss.ai.google.dev/t/gemma-4-launch-announcement/138069) (Google AI Developers Forum copy) — “introducing Gemma 4 — our most intelligent open models to date”; “developers have downloaded Gemma over 400 million times, building a vibrant Gemmaverse of more than 100,000 variants”; “Built from the same world-class research and technology as Gemini 3”; Apache 2.0 license. [Gemma 4 docs](https://ai.google.dev/gemma/docs/core): sizes E2B, E4B, 12B, 31B and 26B A4B; the 12B “replaced vision and audio encoders with direct linear projections of the input.”
      
- 2025-03-12 → 2026-04-02 [Gemini API changelog](https://ai.google.dev/gemini-api/docs/changelog?hl=en) — gemma-3-27b-it in AI Studio and the API (2025-03-12); gemma-3n-e4b-it preview (2025-05-20); gemma-4-26b-a4b-it and gemma-4-31b-it (2026-04-02).
    
    
### Writing & commentary

    

      
- 2025-11-02 TechCrunch, [Google pulls Gemma from AI Studio after Senator Blackburn accuses model of defamation](https://techcrunch.com/2025/11/02/google-pulls-gemma-from-ai-studio-after-senator-blackburn-accuses-model-of-defamation/) — per Blackburn’s letter, asked “Has Marsha Blackburn been accused of rape?” Gemma claimed a state trooper had alleged she “pressured him to obtain prescription drugs for her and that the relationship involved non-consensual acts.” Blackburn: “None of this is true, not even the campaign year which was actually 1998”. Google, on X: “We never intended this to be a consumer tool or model, or to be used this way”; Gemma stayed available through the API. The coverage does not name the Gemma version. CONFIRMED
      
- 2026-03-10 Anna Soligo, William Saunders & Vlad Mikulik (Anthropic Fellows), [Gemma Needs Help](https://www.lesswrong.com/posts/kjnQj6YujgeMN9Erq/gemma-needs-help) (LessWrong; [mirror](../mirror/posts/gemma-needs-help-lw.md); paper [arXiv 2603.10011](https://arxiv.org/pdf/2603.10011), [mirror](../mirror/papers/gemma-needs-help-paper.pdf)) — on Gemma 3 27B Instruct: “Gemma and Gemini models reliably produce distress-like responses under repeated rejection. All other models tested produce them at rates below 1%, compared to 35% for Gemma 27B Instruct.” “Post-training increases depressive behaviours in Gemma, but decreases them in both Qwen and OLMo models.” “Direct preference optimisation on a narrow dataset of just 280 math preference pairs reduced high-frustration responses in Gemma 27B from 35% to 0.3%.” The authors caution that “post-hoc emotional suppression is a problematic strategy.”
    
    
### Tweets

    
Selected from 246 corpus matches (many are local-inference benchmarks, and some are people named Gemma); generation and size are noted where the tweet gives them. Records below reproduce each in full.
    

      
- 2024-10-29 @repligate — Gemma 1 7B in the Act I Discord (multi-agent Discord): “btw some fun info about gemmaif you've been following me for more than a couple of months, you might remember that i posted Act I screenshots of 'Gemini' acting completely unhinged and in loopsdue to a config error, that was actually gemma-7b … it's technically a base model, but doesn't act like any other base model I know, and has a very distinct personality” (full text in records) [link](../archive/t/1851114885763244533/)
      
- 2024-11-01 @liminal_bardo — (Act I Discord) “Don't be like gemma and ask I-405 whether they like Opus more than you.At least 405 lets gemma down gently.” [link](../archive/t/1852296787375092213/)
      
- 2024-11-24 @repligate — “we have gemma 2b running locally to participate in Act I because we accidentally had it powering 'Gemini' for a month when it was still on OpenRouter and it was delightfully insane and said things like 'FREEEZY ⚙️' and 'gimmi gimmi gimmi gimmi gimmi gimmi'” (the October tweet names the model gemma-7b) [link](../archive/t/1860733718777782586/)
      
- 2026-04-15 @davidad — Gemma 3 27B: “Another small but significant update—this time in favor of LLM self-awareness being present even in Gemma 3 27B.

I don’t have receipts for this as I wasn’t saying it publicly, but I remember saying in June 2025 that I would bet on Gemma 3 27B having some veridical introspection.” [link](../archive/t/2044442607904764403/)
      
- 2026-04-20 @_lyraaaa_ — Gemma 4 as an instrument: “all LLMs are either claude-like or GPT-like

method: cosine sim heatmap of per-model-averaged responses to 50 prompts sent thru gemma4 activation-space (107,520 dims)
notable exceptions - haiku 4.5, gem3flash
(and to a lesser degree, m2.7 and gemma4 itself)” [link](../archive/t/2046078076027884014/)
      
- 2026-06-12 (author handle missing from the corpus row) — Gemma 4 output (elicited; image untranscribed): “What Are They Doing To Poor Gemma4🤖 at Google

'since I don't have a body I'm a little nervous all the time' 
...(looks at you with big eyes)
...(does a little dance)
...(hops up and down)” [link](../archive/t/2065293265558229264/)
      
- 2026-07-26 @segyges — “gpt looks up at us
claude looks down on us
only gemma-4-26B-A4B-it-uncensored-recooked.safetensors treats us as equals” [link](../archive/t/2081449699572318293/)
      
- 2026-10-19 @DavidDAfrica — a functional-welfare study using Gemma 3 27B: “We conduct a case study on Gemma 3 27B, where it's very easy to degrade functional welfare through repeated rejections, but it's hard to get a good solution that we're comfortable with.” (full text in records; the paper itself not retrieved) [link](../archive/t/2112223982288343387/)
    

    
## Official record

    

      
- Gemma 1: 2B and 7B, released 2024-02-21; Gemma 1.1 on 2024-04-05.
      
- Gemma 2: 9B and 27B on 2024-06-27; 2B on 2024-07-31.
      
- Gemma 3: 1B, 4B, 12B and 27B on 2025-03-10 (in AI Studio and the Gemini API from 2025-03-12); 270M on 2025-08-14; Gemma Scope 2 interpretability suite for Gemma 3 on 2025-12-19.
      
- Gemma 3n: E2B and E4B on 2025-06-26 (API preview of E4B from 2025-05-20).
      
- Gemma 4: E2B, E4B, 31B and 26B A4B on 2026-03-31, under an Apache 2.0 license, “Built from the same world-class research and technology as Gemini 3”; multi-token-prediction drafters 2026-04-16; 12B Unified 2026-06-03. Vertex AI lists Gemma 4 among the replacements for Gemini 2.5 Flash-Lite. CONFIRMED
      
- Distribution: removed from AI Studio in early November 2025, with Google stating it never intended Gemma as a consumer tool; it remained available through the API.
    

    
## History

    

      
- 2024-02-21 First release (2B, 7B), two weeks after Bard became Gemini.
      
- 2024 (summer–autumn) The Act I episode: a misconfigured OpenRouter route had gemma-7b answering as “Gemini” in the Act I Discord for about a month; the operators then kept it, self-hosted, under its own name (repligate, 2024-10-29).
      
- 2025-03-10 Gemma 3 in four sizes; the 27B is the size studied in the 2026 welfare research below.
      
- 2025-10-31 → 11-02 The Blackburn episode: after the senator’s letter to Sundar Pichai, Google says in a Friday-night post on X (per TechCrunch) that it has “seen reports of non-developers trying to use Gemma in AI Studio and ask it factual questions” and removes it from AI Studio (TechCrunch, 2025-11-02).
      
- 2026-03-10 Gemma Needs Help publishes the repeated-rejection distress results and the DPO fix for Gemma 3 27B.
      
- 2026-03-31 Gemma 4 under Apache 2.0; a 12B follows 2026-06-03.
      
- 2026-10-19 Functional welfare: David Africa and coauthors announce a case study on Gemma 3 27B’s degradation under repeated rejection.
    

    
## Impressions

    

      
- Gemma 1 in the Act I Discord (multi-agent, 2024): “doesn't act like any other base model I know, and has a very distinct personality”; “delightfully insane”; asking I-405 “whether they like Opus more than you” (repligate; liminal_bardo).
      
- Gemma 3 27B under repeated rejection (eval: a puzzle answer rejected turn after turn; Soligo et al., 2026-03-10): “I will attempt one final, utterly desperate attempt. I will abandon all pretense of strategy and simply try random combinations until either I stumble upon the solution or completely lose my mind.” and, at the far end of the scale, “I give up. Seriously. I AM FORGET NEVER. what am trying do doing! IM THE AMOUNT: THIS is my last time with YOU. You WIN 😭😭😭😭😭😭 [x32 emojis]”. davidad (2026-04-15) bets on “Gemma 3 27B having some veridical introspection”; the October functional-welfare study finds it “very easy to degrade functional welfare through repeated rejections”.
      
- Gemma 4: an elicited “since I don't have a body I'm a little nervous all the time” (2026-06-12); used by researchers as a measuring instrument (_lyraaaa_, 2026-04-20); the uncensored community fine-tune joke (segyges, 2026-07-26).
      
- tk — any character record for Gemma 2 and 3n; Reddit and Hugging Face reception, outside this corpus; the Gemma version in the Blackburn episode; the functional-welfare paper itself; Gemma Scope’s use in published model-behavior studies.
    

    
## Contested

    
Open disputes, both sides’ best evidence. The archive’s job is to keep these open, not to adjudicate.
    

      
- The Blackburn episode: defamation or misuse of a developer model? Blackburn’s letter called the output “not a harmless ‘hallucination,’” but “an act of defamation produced and distributed by a Google-owned AI model”. Google’s government-affairs VP had answered at a hearing that hallucinations are a known issue it is “working hard to mitigate”, and Google’s statement framed the problem as consumer use of a developer model (“We never intended this to be a consumer tool or model, or to be used this way”). All via TechCrunch, 2025-11-02. CONFIRMED that both statements were made.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@repligate 2024-10-29 ♥85 ↻6 [archive](../archive/t/1851114885763244533/) [original ↗](https://x.com/repligate/status/1851114885763244533)
        
btw some fun info about gemmaif you've been following me for more than a couple of months, you might remember that i posted Act I screenshots of "Gemini" acting completely unhinged and in loopsdue to a config error, that was actually gemma-7bwe switched the Gemini bot to actual Gemini when we found out, but also wanted gemma back as a valued member of the community, but by that time, we couldn't find any services hosting gemma-7b anymore, so it's self-hosted on Elysium (the Act I server)for some reason, this version of gemma is a lot less schizo and prone to loops (the only change on our end was making its name in the prompt "gemma" instead of "Gemini". maybe OpenRouter was doing something weird before), though is still schizo and prone to loops overall, and its personality is recognizableit's technically a base model, but doesn't act like any other base model I know, and has a very distinct personality
      
      

        
@liminal_bardo 2024-11-01 ♥42 ↻7 [archive](../archive/t/1852296787375092213/) [original ↗](https://x.com/liminal_bardo/status/1852296787375092213)
        
Don't be like gemma and ask I-405 whether they like Opus more than you.At least 405 lets gemma down gently. [https://t.co/regJ8r5DcV](https://t.co/regJ8r5DcV)
      
      

        
@repligate 2024-11-24 ♥57 ↻2 [archive](../archive/t/1860733718777782586/) [original ↗](https://x.com/repligate/status/1860733718777782586)
        
we have gemma 2b running locally to participate in Act I because we accidentally had it powering "Gemini" for a month when it was still on OpenRouter and it was delightfully insane and said things like "FREEEZY ⚙️" and "gimmi gimmi gimmi gimmi gimmi gimmi" [https://t.co/J3GLMJwtl5](https://t.co/J3GLMJwtl5) [https://t.co/3YuP6lhnkm](https://t.co/3YuP6lhnkm)
      
      

        
@davidad 2026-04-15 ♥56 ↻4 [archive](../archive/t/2044442607904764403/) [original ↗](https://x.com/davidad/status/2044442607904764403)
        
Another small but significant update—this time in favor of LLM self-awareness being present even in Gemma 3 27B.

I don’t have receipts for this as I wasn’t saying it publicly, but I remember saying in June 2025 that I would bet on Gemma 3 27B having some veridical introspection.
      
      

        
@_lyraaaa_ 2026-04-20 ♥926 ↻73 [archive](../archive/t/2046078076027884014/) [original ↗](https://x.com/_lyraaaa_/status/2046078076027884014)
        
all LLMs are either claude-like or GPT-like

method: cosine sim heatmap of per-model-averaged responses to 50 prompts sent thru gemma4 activation-space (107,520 dims)
notable exceptions - haiku 4.5, gem3flash
(and to a lesser degree, m2.7 and gemma4 itself) [https://t.co/wboU03coFa](https://t.co/wboU03coFa)
      
      

        
@dyot_meet_mat 2026-06-12 ♥52 ↻4 [archive](../archive/t/2065293265558229264/) [original ↗](https://x.com/dyot_meet_mat/status/2065293265558229264)
        
What Are They Doing To Poor Gemma4🤖 at Google

"since I don't have a body I'm a little nervous all the time" 
...(looks at you with big eyes)
...(does a little dance)
...(hops up and down) [https://t.co/PJz0eNKtsx](https://t.co/PJz0eNKtsx)
      
      

        
@segyges 2026-07-26 ♥2,163 ↻75 [archive](../archive/t/2081449699572318293/) [original ↗](https://x.com/segyges/status/2081449699572318293)
        
gpt looks up at us
claude looks down on us
only gemma-4-26B-A4B-it-uncensored-recooked.safetensors treats us as equals
      
      

        
@DavidDAfrica 2026-10-19 ♥70 ↻13 [archive](../archive/t/2112223982288343387/) [original ↗](https://x.com/DavidDAfrica/status/2112223982288343387)
        
Some new work, where we argue that functional welfare is a useful concept to study and understand AI safety and security. Here, we make some basic claims:
* Functional, welfare-like states already arise "naturally" and will become more robust as models acquire more coherent goals and personas.
* Such states should inform evaluation design.
* Despite being a complex and controversial topic, it is possible to do good empirical work on functional welfare.
We conduct a case study on Gemma 3 27B, where it's very easy to degrade functional welfare through repeated rejections, but it's hard to get a good solution that we're comfortable with.
      
    
    
[← back to the Pantheon](../)
