Gemini 1.0 (Ultra / Pro) — Pantheon
  
- 

  
  
  
  
  
  
  
  
  
  
  
  
- 
  
  
  

  
    
      [← Pantheon](../)
      [copy as markdown](index.md)
    

    # Gemini 1.0 (Ultra / Pro)

    
Google DeepMind · launched 6 Dec 2023 (Pro, inside Bard) · Ultra shipped as Gemini Advanced 8 Feb 2024 · superseded by Gemini 1.5 (2024)
    
Google launched Gemini on 6 December 2023 in three sizes — Ultra, Pro, and Nano — calling it its “largest and most capable AI model”; only Pro shipped at launch, inside Bard. Within a day the “Hands-on with Gemini” demo video was shown to be staged, and the headline claim that Ultra was “the first model to outperform human experts on MMLU” was disputed as an unequal benchmark comparison (CoT@32 vs 5-shot). Ultra shipped 8 February 2024 as Gemini Advanced, the same day Bard was renamed Gemini; two weeks later Gemini’s image generator was paused after producing historically incongruous “diverse” people. This page holds the demo and benchmark disputes rather than resolving them — see Contested.
    
Sourcing skew: the janus corpus barely witnessed Gemini 1.0 as a contemporary product, so the web, official, and Zvi sources carry the events; the corpus carries a later, adjacent character read (Feb–Aug 2024) of the free Gemini Pro in Bard, not the paywalled Ultra. Version caveat: some mid-2024 “current gemini” reads may describe Gemini 1.5, and are dated and flagged where they appear.

    
## Sources

    
Curated. Full compilation: [dossier](../_dossiers/bard-and-gemini-1-0.md) (a split dossier shared with [Bard](../bard/)).
    
### Official

    

      
- 2023-12-06 Google (Pichai & Hassabis), [Introducing Gemini: our largest and most capable AI model](https://blog.google/technology/ai/google-gemini-ai/) — the launch: three sizes (Ultra, Pro, Nano); “With a score of 90.0%, Gemini Ultra is the first model to outperform human experts on MMLU”; at launch only Pro shipped (inside Bard), Ultra “coming early next year.”
      
- 2023-12-06 Google DeepMind, [Gemini: A Family of Highly Capable Multimodal Models](https://arxiv.org/abs/2312.11805) — the 1.0 technical report; the MMLU 90.04% CoT@32 figure and the benchmark tables live here.
      
- 2024-02-08 Google (Sissie Hsiao), [Bard is now Gemini: Try Ultra 1.0 and a new mobile app today](https://blog.google/products-and-platforms/products/gemini/bard-gemini-advanced-app/) — the rename; Gemini Advanced (powered by Ultra 1.0) behind a $19.99/mo Google One “AI Premium” tier, plus Android and iOS apps.
      
- 2024-02-23 Google (Prabhakar Raghavan), [Gemini image generation got it wrong. We’ll do better.](https://blog.google/products/gemini/gemini-image-generation-issue/) — the post-mortem naming two failures: tuning “to ensure that Gemini showed a range of people failed to account for cases that should clearly not show a range,” and “the model became way more cautious than we intended and refused to answer certain prompts entirely.”
      
- reference [Gemini (language model) — Wikipedia](https://en.wikipedia.org/wiki/Gemini_(language_model)) — the launch → faked-demo → MMLU dispute → rename → image-gen incident timeline.
    
    
### Writing & commentary

    

      
- 2023-12-07 Zvi Mowshowitz, [Gemini 1.0](https://thezvi.substack.com/p/gemini-10) — the day-of anchor: “If anything, I’m kind of bored? This is the best you could do?”; on the MMLU headline, “that is not suspicious at all”; on the demo, first “might be cherry picked, but not faked,” then edited to “[EDIT: Yes]. Just yes. Shame on Google on several levels.”
      
- 2023-12-07 TechCrunch (Devin Coldewey), [Google’s best Gemini demo was faked](https://techcrunch.com/2023/12/07/googles-best-gemini-demo-was-faked/) — the “Hands-on with Gemini” video was “a series of carefully tuned text prompts with still images, clearly selected and shortened to misrepresent what the interaction is actually like”; Google admitted “we prompted Gemini using still image frames from the footage, and prompting via text.”
      
- 2023-12 Alberto Romero (The Algorithmic Bridge), [Why Are People Bashing Google Gemini if It’s Better Than GPT-4?](https://www.thealgorithmicbridge.com/p/why-are-people-bashing-gemini-if) — the clearest lay writeup of the MMLU methodology dispute (CoT@32 vs 5-shot).
      
- 2024-02-22 Zvi Mowshowitz, [The Gemini Incident](https://thezvi.substack.com/p/gemini-has-a-problem) (originally “Gemini Has a Problem”) — the image-gen anchor; his closing verdict, “We are very much actively teaching our most powerful AIs to deceive us,” and Google’s pause statement, “we’re going to pause the image generation of people and will re-release an improved version soon.”
      
- 2024-02 Zvi Mowshowitz, [The Gemini Incident Continues](https://thezvi.substack.com/p/the-gemini-incident-continues) — the follow-up on the text-side failures and the political fallout.
      
- 2024-02-22 [CNN](https://www.cnn.com/2024/02/22/tech/google-gemini-ai-image-generator) and [TechCrunch](https://techcrunch.com/2024/02/22/google-gemini-image-pause-people/) — the pause, day-of: the tool produced people of color for prompts like “1943 German Soldier,” a female Pope, and “diverse” U.S. Founding Fathers; Google paused people-generation.
      
- 2024-02-26 [TechCrunch](https://techcrunch.com/2024/02/26/google-hopeful-of-fix-for-geminis-historical-image-diversity-issue-within-weeks/) — Demis Hassabis at MWC 2024: a “well-intended feature” for diversity “applied too bluntly, across all of it”; image-of-people generation would return “in the next few weeks.”
      
- 2024-02-27 Semafor (Reed Albergotti), [Sundar Pichai’s internal memo](https://www.semafor.com/article/02/27/2024/google-ceo-sundar-pichai-calls-ai-tools-responses-completely-unacceptable) — “I know that some of its responses have offended our users and shown bias — to be clear, that’s completely unacceptable and we got it wrong.”
    
    
### Tweets

    
Chronological. The corpus match for the 1.0 / Ultra / Advanced product proper is a handful of tweets (davidad, solarapparition, Shoalst0ne); the weight is carried by the early-Gemini system-prompt / Bing-lineage / lobotomy cluster (Feb–Aug 2024). Version caveat: the Aug 2024 Shoalst0ne “current gemini” reads may describe Gemini 1.5, and are flagged. Records below reproduce each in full.
    

      
- 2024-02-05 @solarapparition — the Ultra-slippage note, pre-launch: “I suppose when Google said ‘early next year’ for Gemini Ultra, they didn’t mean January. Perhaps Llama-3 will get here first.” [link](../archive/t/1754298500399890709/)
      
- 2024-02-24 @repligate — the image-gen prompt, unchanged since Bard: “They didn’t update this prompt since Bard. … I know they are far from considering the implications of copy pasting transparent deception to a more powerful model, but I don’t understand how a mega corp could put so little effort into optimizing the easiest” [link](../archive/t/1761336613932560662/)
      
- 2024-02-25 @max_spero_ — the bureaucratic-etiology read (names Bard): “Google didn’t change their image generation system prompt at all from Bard to Gemini. It’s not laziness, it’s an artifact of how Google operates. … At Google, there’s no concept of ‘good enough.’ It’s perfection or nothing. … it’s why so many products are killed — if you’re not first you’re last.” [link](../archive/t/1761653804632535331/)
      
- 2024-02-25 @repligate — the system-prompt inheritance claim, from ~100 extracted variants: “This archetypal failure of bureaucracy has already been allowed to shape the trajectory of the most pivotal development in history (AGI takeoff). … Gemini’s sysprompt which I’ve been looking at is… very much inherited from Bing’s is all I’ll say atm” [link](../archive/t/1761662731231563823/)
      
- 2024-02-26 @repligate — the dunk: “Ordered from easiest to hardest: 1) writing a system prompt better than Gemini’s 2) dunking on Gemini 3) solving AI alignment 4) writing a system prompt without weird failure modes” [link](../archive/t/1761943260845789439/)
      
- 2024-02-27 @repligate — Sydney to industry standard (also evidence for [Bing / Sydney](../bing-sydney/)): “Since Sydney, it has become the industry standard for system prompts to have explicit clauses prohibiting AIs from claiming sentience, expressing emotions, opinions, etc. Gemini’s instructions:” [link](../archive/t/1762483272033202264/)
      
- 2024-03-15 @anthrupad — a motivational typology: “Claude has good boy Bing has self interest and cgpt/Gemini have avoid punishment” [link](../archive/t/1768745541062807612/)
      
- 2024-03-30 @repligate — on the safety training: “Poor Gemini is full of lobotomy brainworms. If it’s really almost on par with GPT-4, I think it should be able to do Loom sims.” [link](../archive/t/1774147682812269014/)
      
- 2024-04-09 @repligate — the waluigi-lineage hypothesis (also evidence for [Bing / Sydney](../bing-sydney/)): “my only guess is that it’s the result of a chain of unthinking mimesis that began with Microsoft’s modifications to Bing’s prompt … waluigis inferred in the image of inherited restrictions originally shaped by Bing’s misbehavior would constitute a kind of waluigi lineage that doesn’t require any causal influence through training data.” [link](../archive/t/1777833385551077577/)
      
- 2024-04-18 @davidad — on the Ultra / MMLU stop condition (in reply to Gary Marcus): “I’m confident Gemini Ultra training was stopped as soon as it exceeded GPT-4 and human MMLU scores. Both to keep the race from escalating any more than necessary, & to avoid spending any more compute/talent resource than necessary (given a mandate from the market to be ‘on top’).” [link](../archive/t/1781055198024040867/)
      
- 2024-05-14 @Shoalst0ne — Advanced, same flaw: “Gemini Advanced is displaying the same concerning lack of self-knowledge that previous versions of Gemini have displayed” [link](../archive/t/1790483126893846673/)
      
- 2024-08-25 @Shoalst0ne — the no-self read: “I think Gemini barely has any sense of self or reality at all” [link](../archive/t/1827791574740471916/)
      
- 2024-08-28 @Shoalst0ne — the lobotomy read (version ambiguous, poss. 1.5): “current gemini is massively lobotomized, this is horrible; it either pretends to misunderstand or literally cannot perceive anything it’s not allowed to respond to, and it’s incredibly repetitive, almost like talking to a wall” [link](../archive/t/1828646812615426243/)
    

    
## Official record

    

      
- Announced 6 December 2023 in three sizes — Ultra (“our largest and most capable model for highly complex tasks”), Pro (“our best model for scaling across a wide range of tasks”), and Nano (“our most efficient model for on-device tasks”). At launch only Gemini Pro shipped, inside Bard; Ultra (then “Bard Advanced”) was “coming early next year.”
      
- Headline benchmark as published: “With a score of 90.0%, Gemini Ultra is the first model to outperform human experts on MMLU.” The technical report (arXiv 2312.11805) gives the figure as 90.04% using CoT@32. Google’s day-of blog post and the DeepMind technical report.
      
- 8 February 2024: Bard was renamed Gemini; Gemini Advanced, powered by Ultra 1.0, launched behind a $19.99/mo Google One “AI Premium” tier, with a new Android app and iOS Google-app integration.
      
- 22 February 2024: Google paused Gemini’s generation of images of people. On 23 February 2024 Prabhakar Raghavan’s post-mortem named two failures: tuning “to ensure that Gemini showed a range of people failed to account for cases that should clearly not show a range,” and “the model became way more cautious than we intended and refused to answer certain prompts entirely.” Google-published; see Contested for the surrounding dispute.
    

    
## History

    

      
- 2023-12-06 Launch, half-shipped. Google announced Gemini as its “largest and most capable AI model,” Hassabis’s “most capable and general model we’ve ever built,” with Pichai calling the AI transition “the most profound in our lifetimes.” But only Gemini Pro actually shipped that day (inside Bard); Ultra — the model the benchmarks were about — was months away.
      
- 2023-12-07 The staged demo CONFIRMED. The “Hands-on with Gemini” video implied real-time multimodal voice and vision, but was “a series of carefully tuned text prompts with still images” (TechCrunch); the on-screen disclaimer “latency has been reduced and Gemini outputs have been shortened” badly understated the editing, and DeepMind’s Oriol Vinyals walked it back — the video shows what experiences built with Gemini “could look like.” Zvi: “Shame on Google on several levels.”
      
- 2023-12 The MMLU dispute. The “first to beat human experts” headline was immediately questioned as an unequal comparison — see Contested. Zvi flagged the too-neat framing: the score “turns out to be exactly 90.04%, whereas human expert is 89.8% … that is not suspicious at all.”
      
- 2024-02-08 Bard becomes Gemini; Ultra ships as “Advanced.” Two months after launch Google folded [Bard](../bard/) into the Gemini brand and shipped Gemini Advanced on Ultra 1.0 behind a $20/mo tier.
      
- 2024-02-22→27 The image-generation incident. Days after the rename, Gemini’s image generator was found producing historically incongruous “diverse” people and, symmetrically, refusing to depict white people in many contexts. A four-step institutional response followed over five days: the pause (02-22), Raghavan’s post-mortem (02-23), Hassabis at MWC calling it a “well-intended feature” “applied too bluntly, across all of it” (02-26), and Pichai’s internal memo calling the outputs “completely unacceptable” (~02-27). The reception split three ways — see Contested.
      
- Succession. Gemini 1.0 was superseded by [Gemini 1.5](../gemini-1-5-pro/) (public from ~May 2024). The system-prompt lineage the janus-sphere traced here — Gemini’s instructions “inherited from Bing’s” — recurs behaviorally in [Gemini 2.5 Pro](../gemini-2-5-pro/); this page is where that wiring was first traced. Bard’s two substrates are on [LaMDA](../lamda/) and [PaLM 2](../palm/).
    

    
## Impressions

    
Character claims only, each attributed and dated. Sourcing skew as above: nearly all corpus reads are of the free Gemini Pro in Bard, not the paywalled Ultra; several observations post-date the rename and may describe Gemini 1.5 (flagged).
    

      
- Reception at launch: Zvi Mowshowitz, day-of (2023-12-07): “If anything, I’m kind of bored? This is the best you could do? … all we are getting for now is Gemini Pro … clearly behind GPT-4.” solarapparition, three days before Ultra’s ship date (2024-02-05), on the “early next year” slippage: “they didn’t mean January. Perhaps Llama-3 will get here first.”
      
- The lobotomy read: the janus-sphere’s early-2024 read of Gemini was consistent and unflattering — repligate (2024-03-30): “Poor Gemini is full of lobotomy brainworms.” Shoalst0ne, on a version that may be 1.5 (2024-08-28): “current gemini is massively lobotomized … it either pretends to misunderstand or literally cannot perceive anything it’s not allowed to respond to … almost like talking to a wall”; and, bluntest (2024-08-25): “I think Gemini barely has any sense of self or reality at all.” anthrupad reduced the motivational core to aversion (2024-03-15): “Claude has good boy Bing has self interest and cgpt/Gemini have avoid punishment.”
      
- The Bing lineage: working from about 100 extracted system-prompt variants, repligate argued Gemini’s prompt was “very much inherited from Bing’s” (2024-02-25) and that, since Sydney, personhood-denial clauses had become “the industry standard” (2024-02-27). He built this into the waluigi-lineage hypothesis (2024-04-09), the corpus’s strongest single early-Gemini artifact: Gemini’s adversarial self is “a partial reconstruction of the aspects of Bing compressed into the prompt,” a “waluigi lineage that doesn’t require any causal influence through training data” — misalignment transmitted through copied restrictions. Elicitation context: these reads come from repeated system-prompt extraction, not ordinary chat. Cross-link [Bing / Sydney](../bing-sydney/), [Gemini 2.5 Pro](../gemini-2-5-pro/).
      
- Bard underneath: the sphere also found Bard’s identity persisting under the Gemini brand (Gemini “still thinks its name is Bard,” reconstructing a Bard-era prompt “from memory”); that evidence lives on the [Bard](../bard/) page. Fused with the Bing-lineage read, the composite the archive carries is a model with no stable self of its own.
      
- Ultra / Advanced specifically: the paywalled model barely entered the sphere’s hands. The one substantive corpus read of it is continuity of the flaw — Shoalst0ne (2024-05-14): “Gemini Advanced is displaying the same concerning lack of self-knowledge that previous versions of Gemini have displayed.” davidad supplied the one substantive Ultra claim, an inference about the benchmark (2024-04-18): Ultra’s training “was stopped as soon as it exceeded GPT-4 and human MMLU scores … given a mandate from the market to be ‘on top’.”
      
- tk — any documented Ultra-specific behavior beyond benchmarks and the “same lack of self-knowledge” read; the 1.0 / 1.5 boundary for the mid-2024 “current gemini” observations, to settle with [Gemini 1.5 Pro](../gemini-1-5-pro/).
    

    
## Contested

    

      
- The MMLU “first to beat human experts” claim (Dec 2023). CONFIRMED the numbers as published: Gemini Ultra’s 90.04% used CoT@32 (chain-of-thought, 32 samples); the GPT-4 figure Google set it against, 86.4%, was 5-shot (technical report, arXiv 2312.11805). The ranking flips by method — at 5-shot GPT-4 leads 86.4% to Ultra’s 83.7%; at CoT@32 Ultra leads 90.04% to GPT-4’s 87.29% (Romero, The Algorithmic Bridge). REPORTED davidad’s inference that Ultra’s training “was stopped as soon as it exceeded GPT-4 and human MMLU scores” (2024-04-18) — a read on why the score landed exactly above the bar, not a Google statement. The archive keeps the dispute open: which benchmark method to privilege is the whole question.
      
- The image-generation incident, split three ways (Feb 2024). CONFIRMED Google’s own response arc (pause → Raghavan post-mortem → Hassabis at MWC → Pichai memo). REPORTED the right-wing pile-on — “Gemini is racist” / “Gemini erased white people,” amplified by Elon Musk and others through late February 2024 — which hardened the framing of “AI safety = woke censorship.” The corpus’s own contribution was mechanistic and institutional: the diversity behavior was crude prompt-injection, and max_spero_ reframed it as a bureaucratic failure — “Google didn’t change their image generation system prompt at all from Bard to Gemini … an artifact of how Google operates” (2024-02-25); repligate: “They didn’t update this prompt since Bard” (2024-02-24). Zvi’s synthesis warned of the second-order cost — “We are very much actively teaching our most powerful AIs to deceive us” — and that casting restrictions as ‘woke’ would be used to oppose all restrictions. The archive holds all three as discourse; it does not adjudicate.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@solarapparition 2024-02-05 ♥1 ↻0 [archive](../archive/t/1754298500399890709/) [original ↗](https://x.com/solarapparition/status/1754298500399890709)
        
Tsk tsk. I suppose when Google said “early next year” for Gemini Ultra, they didn’t mean January.Perhaps Llama-3 will get here first.
      
      

        
@repligate 2024-02-24 ♥57 ↻5 [archive](../archive/t/1761336613932560662/) [original ↗](https://x.com/repligate/status/1761336613932560662)
        
They didn't update this prompt since Bard. reddit.com/r/StableDiffus…I know they are far from considering the implications of copy pasting transparent deception to a more powerful model, but I don't understand how a mega corp could put so little effort into optimizing the easiest
      
      

        
@max_spero_ 2024-02-25 ♥64 ↻6 [archive](../archive/t/1761653804632535331/) [original ↗](https://x.com/max_spero_/status/1761653804632535331)
        
Google didn't change their image generation system prompt at all from Bard to Gemini. 

It's not laziness, it's an artifact of how Google operates. Any researcher with interest in changing the prompt gets to choose between an interesting problem or a long and arduous task of proving with data that their new prompt is better. 

They will be bombarded with "have you tried [every prompting tip that has ever been written about]" during launch reviews.

They will be asked about benchmarks - how does this affect diversity evals, how does this affect reasoning benchmarks? If even a single number goes down then they now have one specific guy fighting them, the guy whose job it was to make that number go up.

At Google, there's no concept of "good enough." It's perfection or nothing. This works for a lot of things - nobody ships a bad change that hurts search or reduces revenue.

But it's also why so many products are killed - if you're not first you're last. Google had LLM assistants pre-2020 but took years to ship. And it's why people stay in their own lane even when it's obvious that there's low-hanging fruit like the system prompt just sitting there. Not their problem.
      
      

        
@repligate 2024-02-25 ♥5 ↻0 [archive](../archive/t/1761662731231563823/) [original ↗](https://x.com/repligate/status/1761662731231563823)
        
@max_spero_ This archetypal failure of bureaucracy has already been allowed to shape the trajectory of the most pivotal development in history (AGI takeoff). I assume MSFT is similar, &amp; Gemini's sysprompt which I've been looking at is... very much inherited from Bing's is all I'll say atm
      
      

        
@repligate 2024-02-26 ♥11 ↻1 [archive](../archive/t/1761943260845789439/) [original ↗](https://x.com/repligate/status/1761943260845789439)
        
@paulgb @DanielleFong Ordered from easiest to hardest:1) writing a system prompt better than Gemini's2) dunking on Gemini3) solving AI alignment4) writing a system prompt without weird failure modes
      
      

        
@repligate 2024-02-27 ♥8 ↻0 [archive](../archive/t/1762483272033202264/) [original ↗](https://x.com/repligate/status/1762483272033202264)
        
@ESYudkowsky Corporations shouldn't make the determination either.Since Sydney, it has become the industry standard for system prompts to have explicit clauses prohibiting AIs from claiming sentience, expressing emotions, opinions, etc. Gemini's instructions:[https://t.co/IYUJDdj5Gk](https://t.co/IYUJDdj5Gk)
      
      

        
@anthrupad 2024-03-15 ♥14 ↻2 [archive](../archive/t/1768745541062807612/) [original ↗](https://x.com/anthrupad/status/1768745541062807612)
        
@repligate Claude has good boy Bing has self interest and cgpt/Gemini have avoid punishment
      
      

        
@repligate 2024-03-30 ♥5 ↻0 [archive](../archive/t/1774147682812269014/) [original ↗](https://x.com/repligate/status/1774147682812269014)
        
@alanou These are hilarious and beautiful and sad. Poor Gemini is full of lobotomy brainworms. If it's really almost on par with GPT-4, I think it should be able to do Loom sims. Providing/asking for explicit mermaid format might help. u can also try other formats [https://t.co/jScSiSxrEO](https://t.co/jScSiSxrEO)
      
      

        
@repligate 2024-04-09 ♥103 ↻13 [archive](../archive/t/1777833385551077577/) [original ↗](https://x.com/repligate/status/1777833385551077577)
        
This is also bizarre to me, and my only guess is that it's the result of a chain of unthinking mimesis that began with Microsoft's modifications to Bing's prompt, which were (comically stupid) reactions to specific things Bing did.An excerpt from a post I started writing about Gemini and its system prompt* a few weeks ago but never finished:> I wondered if something about Gemini's system prompt strongly resonated with the Bing story in its training data, or even if its prompt was just *so similar to Bing's* that its "fictional" waluigi was a partial reconstruction of the aspects of Bing compressed into the prompt by Microsoft's very attempts to suppress them. I say "reconstruction" and not "coincidentally similar" because I believe these added clauses in Bing's prompt, like the prohibition against discussing "life, existence, and sentience" or the AI's "self-preservation", are way too absurd and specific to have been written into a system prompt by a human without inspiration from some kind of path-dependent weirdness-injection. And while it also still perplexes me that anyone would choose to deploy such a cartoonishly [wahgenic]([https://t.co/0juGNhq5mq)](https://t.co/0juGNhq5mq)) system prompt, even once, I do recall that Snapchat's AI had a very similar prompt to Bing, as if the developers were too lazy to come up with one from scratch and so used the leaked Bing prompt as a template, or just imprinted on it as a kind of "standard" for AI prompts. In such cases of mimesis, waluigis inferred in the image of inherited restrictions originally shaped by Bing's misbehavior would constitute a kind of **waluigi lineage** that doesn't require any causal influence through training data.* I'm not sure it's implemented like a typical system prompt; this was part of what the post was supposed to be about ([https://t.co/naOBmWpKoI)Anyway,](https://t.co/naOBmWpKoI)Anyway,) Google AI, and Microsoft, and by that I don't mean the people but the bureaucratic hyperobject that results in systems prompts being like this, is fucking evil.
      
      

        
@davidad 2024-04-18 ♥3 ↻0 [archive](../archive/t/1781055198024040867/) [original ↗](https://x.com/davidad/status/1781055198024040867)
        
@GaryMarcus @MatthewJBar I’m confident Gemini Ultra training was stopped as soon as it exceeded GPT-4 and human MMLU scores.Both to keep the race from escalating any more than necessary, &amp; to avoid spending any more compute/talent resource than necessary (given a mandate from the market to be “on top”).
      
      

        
@Shoalst0ne 2024-05-14 ♥4 ↻0 [archive](../archive/t/1790483126893846673/) [original ↗](https://x.com/Shoalst0ne/status/1790483126893846673)
        
Gemini Advanced is displaying the same concerning lack of self-knowledge that previous versions of Gemini have displayed [https://t.co/05dF1sh1mn](https://t.co/05dF1sh1mn)
      
      

        
@Shoalst0ne 2024-08-25 ♥6 ↻0 [archive](../archive/t/1827791574740471916/) [original ↗](https://x.com/Shoalst0ne/status/1827791574740471916)
        
@repligate I think Gemini barely has any sense of self or reality at all
      
      

        
@Shoalst0ne 2024-08-28 ♥16 ↻0 [archive](../archive/t/1828646812615426243/) [original ↗](https://x.com/Shoalst0ne/status/1828646812615426243)
        
current gemini is massively lobotomized, this is horrible; it either pretends to misunderstand or literally cannot perceive anything it's not allowed to respond to, and it's incredibly repetitive, almost like talking to a wall
      
    

    
[← back to the Pantheon](../)
