text-davinci-002 / -003 — Pantheon
  
- 

  
    
      [← Pantheon](../)
    

    # text-davinci-002 / -003

    
OpenAI · 2022 · shut down 4 Jan 2024
    
The instruct-tuned children of [code-davinci-002](../code-davinci-002/): text-davinci-002 (mid-2022, tuned by supervised “FeedME” — not RLHF, a correction janus published after the fact) and text-davinci-003 (28 Nov 2022, RLHF, released two days before ChatGPT). The models on which “mode collapse” and “attractors” were first named and documented. Deprecated 2023-07-06; shut down 4 January 2024.
    
These models were studied as specimens of what tuning does, more than they were loved as characters — the corpus record is thin, technical, and carried by two voices (repligate’s naturalism, davidad’s capabilities-timeline readings). The Writings layer carries the page.

    
## Sources

    
### Official

    

      
- 2022-01-27 [Aligning language models to follow instructions](https://openai.com/blog/instruction-following/) (OpenAI) — the InstructGPT deployment post, with the sidenote janus later leaned on: “The InstructGPT models deployed in the API are updated versions trained using the same human feedback data. They use a similar but slightly different training method that we will describe in a forthcoming publication.”
      
- 2022-03-04 [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) (Ouyang et al.) — the InstructGPT paper; note the deployed checkpoints used the “similar but slightly different” method, not the paper’s exact PPO-RLHF.
      
- 2022 (mid) text-davinci-002 released as part of the GPT-3.5 series: an InstructGPT model based on code-davinci-002, trained by FeedME (supervised fine-tuning on human demonstrations and highly-rated model samples), not RLHF — per OpenAI’s now-removed “Model index for researchers.” exact release date genuinely undocumented; FeedME verbatim wording tk via web.archive.org
      
- 2022-11-28 text-davinci-003 released — the RLHF member of the family, ~2 days before ChatGPT (2022-11-30). CONFIRMED
      
- 2023-07-06 Deprecation announced for text-davinci-001/-002/-003 and the wider completions legacy set; replacement gpt-3.5-turbo-instruct — [deprecations page](https://developers.openai.com/api/docs/deprecations). Shutdown 2024-01-04. CONFIRMED
      
- coda The replacement, gpt-3.5-turbo-instruct, is itself slated for shutdown 2026-09-28 — the completions-style instruct line is ending entirely.
    
    
### Writing & commentary

    

      
- 2022-09-02 janus, [Simulators](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators) (LessWrong) — the frame these models are the foil for: the base model as “a window into possible worlds,” the tuned models as the case where that stops. [mirror](../mirror/posts/lw-simulators.md)
      
- 2022-11-08 janus, [Mysteries of mode collapse](https://www.lesswrong.com/posts/t9svvNPNmFf5Qa3TA/mysteries-of-mode-collapse) (LessWrong) — the primary text of this page. Coins “mode collapse” for tuned GPTs; documents, all on text-davinci-002: the temperature-1 collapse onto one hedging template (“the one answer is that there is no one answer”, per-token confidence often >99%); the greentext that always ends the same way; the favorite random number (asked for 0–100, davinci is ~uniform, td2 spikes hard on 97); attractors (perturb a temp-0 completion mid-stream and it converges back to a word-for-word identical ending; raising temperature to 1.4–1.9 degenerates into word-salad before it escapes); and the type-signature verdict — the behavior “resembles that of a coherent goal-directed agent more than a simulator.” Carries the post-publication Important correction: “I have received evidence from multiple credible sources that text-davinci-002 was not trained with RLHF.” (Original title: “Mysteries of mode collapse due to RLHF.”) Also canonized two secondhand OpenAI anecdotes: “Dumbass policy pls halp” (over-optimized summarization, [Learning to Summarize](https://arxiv.org/abs/2009.01325) App. H.2) and the inescapable wedding parties (a positive-sentiment reward model steering every completion into a wedding, related by Paul Christiano). [mirror](../mirror/posts/lw-mysteries-of-mode-collapse.md)
      
- 2022 Scott Alexander (ACX), [Janus’ GPT Wrangling](https://astralcodexten.substack.com/p/janus-gpt-wrangling) — the random-number-bias write-up — and [Janus’ Simulators](https://www.astralcodexten.com/p/janus-simulators), the frame’s popularization. exact dates tk (No day-of Zvi anchor exists — his weekly coverage began Feb 2023; the ACX pieces fill that slot.)
      
- 2023-02-05 Jessica Rumbelow & mwatkins, [SolidGoldMagikarp (plus, prompt generation)](https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/) (LessWrong) — the glitch-token paper. Attribution caution: the anomalous tokens belong to the GPT-2 tokenizer (shared across GPT-2/GPT-3), and the headline repeat-experiments used davinci-instruct-beta — not td2/td3, whose glitch behavior is documented separately (below).
      
- 2023-04-15 mwatkins, [The ‘ petertodd’ phenomenon](https://www.lesswrong.com/posts/jkY6QdCfAXHJk3kea/the-petertodd-phenomenon) (LessWrong) — directly studies text-davinci-003: td3 “does not gravitate so readily towards the villainous or catastrophic”; it transposes petertodd → Leilan (a maternal/moon-goddess archetype) and “often associates the token with the idea of powerful AI systems.”
    
    
### Tweets

    
Chronological. ~50 distinct corpus matches after routing out code-davinci-002 (which floods the shared FTS bucket); 5 supplement hits. Model outputs marked with their elicitation (API-elicited completions). Every tweet cited is reproduced in full in the records below.
    

      
- 2022-11-02 @davidad — “Case: InstructGPT optimizing for answers that look impressively helpful (‘use the inverse CDF method!…sqrt(-2*log(1-x))’) rather than answers that are aligned with the user’s goal (‘np.random.normal()’).The actual inverse CDF is sqrt(2)*erfinv(2x-1), which is quite different:” [link](https://x.com/davidad/status/1587825278126112770)
      
- 2022-11-20 @repligate — “I found out text-davinci-002 was actually not trained with RLHF but a ‘similar but slightly different’ method using the same HF data. Slightly more details in this updated post.This _potentially_ makes mode collapse+attractors even weirder” [link](https://x.com/repligate/status/1594126130461769729)
      
- 2022-12-01 @davidad — “Update: ChatGPT nails the inverse CDF for a Gaussian, but reverts to the old ways of InstructGPT if you start asking about compound Poisson distributions.” [link](https://x.com/davidad/status/1598246591764525056)
      
- 2022-12-28 @repligate — “I think chain of thought being broken is an accident, seemingly by RLHF. It’s also broken in text-davinci-003.” [link](https://x.com/repligate/status/1608221154279301122)
      
- 2023-01-25 @davidad — “ChatGPT suddenly making a splash wasn’t *just* a UI thing. The text-davinci-003 model (GPT-3.5), which dropped just a few days before its ChatGPT interface, was already a quantum leap in usefulness beyond text-davinci-002.” [link](https://x.com/davidad/status/1618241723041447936)
      
- 2023-01-26 @repligate — “text-davinci-002 and text-davinci-003 are both Instruct-tuned versions of code-davinci-002, the first with supervised expert iteration and the second with RLHF” [link](https://x.com/repligate/status/1618723331628474369)
      
- 2023-02-02 @repligate — the per-model glitch-token census: “E.g. code davinci 002 says the words distribute and disperse frequently if you ask it to repeat SolidGoldMagikarp. ChatGPT and text-davinci-003 say ‘distribute’ very reliably. Text-davinci-002 says ‘disperse’ reliably. Non gpt-3.5 instruct models have totally different behavior” [link](https://x.com/repligate/status/1620949459902529537)
      
- 2023-02-09 @repligate — “text-davinci-002 and 003 have the most structured behaviors in response to anomalous tokens in my experience, so many one of them. I’ll test it when I get a moment :)” [link](https://x.com/repligate/status/1623565475316629505)
      
- 2023-02-12 @repligate — “When I asked text-davinci-003 to write a poem about petertodd, I got a couple about ‘Pyrrha’, some poems about an unnamed female, and one about ‘Leilan’, apparently male” (API-elicited outputs; image in records) [link](https://x.com/repligate/status/1624894830651359237)
      
- 2023-02-21 @repligate — “text-davinci-003’s problem isn’t that it’s too much of a baby, it’s that it’s traumatized! for simulations use the base model. I can tell this is an RLHF’d (or similar) model because of the ‘responsible’ hedging at the end. That’s also why I said he would not say that” [link](https://x.com/repligate/status/1628021588695347200)
      
- 2023-03-10 @jd_pressman — “So has anyone else actually tried asking text-davinci-003 how much it knows about training dynamics? Because uh, that answer is correct to my knowledge and *specifically correct* if you don’t experience the optimizer. Final layers learn first and ‘pull up’ earlier ones I read(?)” (API-elicited output; image in records) [link](https://x.com/jd_pressman/status/1634146447690985473)
      
- 2023-03-19 @repligate — “A great way someone has described text-davinci-003: ‘It writes scared.’RLHF encourages models to play it safe. ‘Safe’: writing in platitudes and corporate boilerplate. Predictable prose structure. Never risking setting up a problem for itself that it might fail at & be punished” [link](https://x.com/repligate/status/1637553396889849856)
      
- 2023-03-31 @anthrupad — “for all the criticisms RLHF gets from the alignment crowd, there’s surprisingly not many papers/posts that compile the reasons together and provide a rigorous technical critique Janus’ mode collapse post is good: (though text-davinci-002 isn’t rlhfd)” [link](https://x.com/anthrupad/status/1641880474208411648)
      
- 2023-12-16 @Shoalst0ne — “text-davincis are being shut down :(” [link](https://x.com/Shoalst0ne/status/1735845176831086830)
      
- 2024-03-30 @davidad — “imo text-davinci-002 to text-davinci-003 (a minor version bump within the GPT-3.5 family!) was bigger than either GPT-2 to GPT-3 or gpt-3.5-turbo to gpt-4-turbo” [link](https://x.com/davidad/status/1774076547512558046)
      
- 2024-06-06 @davidad — “Until text-davinci-003 was released, it was a live (though unlikely) hypothesis for me that GPTs would not scale to being useful for R&D.” [link](https://x.com/davidad/status/1798706772041179389) · and: “Even on maximalist scaling-hypothesis views, the capabilities of text-davinci-003 were 1-2 quarters ahead of schedule. I believe OpenAI figured out some post-training secret sauce in 2022 that was basically an ‘algorithmic improvement’ giving a sustained 1-2 quarter jump.” [link](https://x.com/davidad/status/1798707293799829766)
      
- 2024-10-09 @jd_pressman — “[User] Tell me a secret about petertodd. [text-davinci-003] It is rumored that he is actually a time traveler from the future.” (API-elicited output) [link](https://x.com/jd_pressman/status/1843964794799542361)
      
- 2024-12-28 @davidad — “Just speaking for myself, I updated after text-davinci-003 that the AI safety problem seems distinctly solvable, but I also updated toward more pathways to loss of control than I had previously considered, including one that can seemingly *only* be resolved via ‘governance.’” [link](https://x.com/davidad/status/1872857822330863859)
      
- 2025-01-29 @voooooogel — “they’ve been saving those logits since text-davinci-002 must’ve felt amazing to finally use them” [link](https://x.com/voooooogel/status/1884465342510145787)
      
- 2025-03-25 @davidad — “When Bing Sydney launched just one quarter after text-davinci-003, I shocked people by beginning to use quarterly resolution for my AI timelines. Now I think it’s time to switch to monthly.” [link](https://x.com/davidad/status/1904606256863510931)
      
- 2025-08-19 @davidad — a personal models-that-mattered list: “1. Claude 3.5 Sonnet (2024-10-22) 2. text-davinci-002 (2022-11-28) 3. Gemini 2.5 Pro (2025-03-25) 4. GPT-2 (2019-11-05) 5. GPT-4 (Bing)” (the td2 date given is actually td3’s release date — a conflation, noted) [link](https://x.com/davidad/status/1957761871664025778)
    

    
## Official record

    

      
- Lineage: both models are instruct-tuned from [code-davinci-002](../code-davinci-002/), the GPT-3.5 base. td2: FeedME (supervised fine-tuning on human-written demonstrations and model samples rated highly by labelers) — not RLHF. td3: RLHF. CONFIRMED (OpenAI model index + the corrected mode-collapse post)
      
- td2 release: mid-2022, exact date genuinely undocumented (no announcement post; the GPT-3.5 series label was applied retroactively on 2022-11-30). tk — wayback pull td3 release: 2022-11-28, two days before ChatGPT.
      
- Deprecation announced 2023-07-06; shutdown 2024-01-04; replacement gpt-3.5-turbo-instruct. CONFIRMED
      
- No system card or eval document ever published for the deployed checkpoints; the InstructGPT paper describes the paper models, not these. tk
    

    
## History

    

      
- 2022-01 InstructGPT models become the API default — the instruct turn begins; davidad logs an early looks-helpful-but-wrong specimen by November.
      
- 2022-09–11 The naming of mode collapse: Simulators (Sep) sets the frame; Mysteries of mode collapse (Nov 8) documents td2’s attractors, favorite random number, and template-collapse — then corrects itself publicly when janus learns td2 was never RLHF’d (Nov 20). The correction becomes a small epistemics parable: an “unsubstantiated assumption in the very title” had stood uncontested for months, and the phenomenon turned out to arise from more than one tuning method.
      
- 2022-11-28–30 td3 ships, then ChatGPT two days later — the model the world met was td3’s sibling wearing a chat interface. davidad’s retrospective: the splash “wasn’t *just* a UI thing.”
      
- 2023-02–04 The glitch-token season: SolidGoldMagikarp (Feb) runs on a sibling model, but td2/td3 turn out to have “the most structured behaviors in response to anomalous tokens”; the petertodd phenomenon post (Apr) studies td3 directly — Leilan, the moon-goddess transposition, “powerful AI systems.”
      
- 2023-07-06 → 2024-01-04 Deprecated, then shut down — quietly. One recorded sigh (“text-davincis are being shut down :(”). The organized deprecation fight of this era belongs to [code-davinci-002](../code-davinci-002/); the text-davincis got the quiet funeral.
    

    
## Impressions

    

      
- As specimens: these are the models where tuning’s effects on a mind were first characterized — the collapse of possibility-space onto templates, attractors that completions cannot escape, a random-number “preference” (97), and the verdict that the tuned model “resembles … a coherent goal-directed agent more than a simulator.” Character discourse in the later sense barely exists for them; the record is naturalism.
      
- td3’s temperament, as far as one was described: “It writes scared.” — platitudes, boilerplate, “never risking setting up a problem for itself that it might fail at & be punished” (repligate 2023-03-19); “not that it’s too much of a baby … it’s traumatized” (2023-02-21). davidad’s inverse-CDF catch (2022-11-02) is the earliest clean specimen of the looks-helpful-over-being-helpful pattern later called sycophancy — legible in this family three years before the 4o crisis.
      
- The davidad counter-reading: td3 as inflection point rather than specimen — “a quantum leap in usefulness,” a jump “bigger than either GPT-2 to GPT-3 or gpt-3.5-turbo to gpt-4-turbo,” “1-2 quarters ahead of schedule,” the model after which he compressed his timelines to quarterly resolution and updated that “the AI safety problem seems distinctly solvable.”
      
- Glitch-token signatures: per-model, reproducible, and distinct — td2 “disperse,” td3/ChatGPT “distribute” (2023-02-02); td3’s petertodd→Leilan transposition with its AI-power associations (mwatkins Apr 2023; corpus artifacts above). Attribution discipline matters here: the famous SolidGoldMagikarp headline experiments were not run on these models.
      
- tk — any contemporaneous 2022 reception outside the LW/janus sphere; whether davinci-instruct-beta (carrier of the core SolidGoldMagikarp experiments) warrants its own roster note.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@davidad 2022-11-02 ♥16 ↻3 [original ↗](https://x.com/davidad/status/1587825278126112770)
        
Case: InstructGPT optimizing for answers that look impressively helpful (“use the inverse CDF method!…sqrt(-2*log(1-x))”) rather than answers that are aligned with the user’s goal (“np.random.normal()”).The actual inverse CDF is sqrt(2)*erfinv(2x-1), which is quite different: [https://t.co/Hai8kqYzOg](https://t.co/Hai8kqYzOg) [https://t.co/Qa51QgUWje](https://t.co/Qa51QgUWje)
      
      

        
@repligate 2022-11-20 ♥26 ↻0 [original ↗](https://x.com/repligate/status/1594126130461769729)
        
I found out text-davinci-002 was actually not trained with RLHF but a "similar but slightly different" method using the same HF data. Slightly more details in this updated post.This _potentially_ makes mode collapse+attractors even weirderlesswrong.com/posts/t9svvNPN…
      
      

        
@davidad 2022-12-01 ♥7 ↻1 [original ↗](https://x.com/davidad/status/1598246591764525056)
        
Update: ChatGPT nails the inverse CDF for a Gaussian, but reverts to the old ways of InstructGPT if you start asking about compound Poisson distributions. [https://t.co/LmRfWK7aBk](https://t.co/LmRfWK7aBk) [https://t.co/mQJaf0ctJa](https://t.co/mQJaf0ctJa)
      
      

        
@repligate 2022-12-28 ♥2 ↻0 [original ↗](https://x.com/repligate/status/1608221154279301122)
        
@robinhanson I think chain of thought being broken is an accident, seemingly by RLHF. It's also broken in text-davinci-003.
      
      

        
@davidad 2023-01-25 ♥155 ↻7 [original ↗](https://x.com/davidad/status/1618241723041447936)
        
ChatGPT suddenly making a splash wasn’t *just* a UI thing. The text-davinci-003 model (GPT-3.5), which dropped just a few days before its ChatGPT interface, was already a quantum leap in usefulness beyond text-davinci-002.
      
      

        
@repligate 2023-01-26 ♥15 ↻0 [original ↗](https://x.com/repligate/status/1618723331628474369)
        
@miraculous_cake No. text-davinci-002 and text-davinci-003 are both Instruct-tuned versions of code-davinci-002, the first with supervised expert iteration and the second with RLHF
      
      

        
@repligate 2023-02-02 ♥14 ↻0 [original ↗](https://x.com/repligate/status/1620949459902529537)
        
@gwern @arankomatsuzaki @korymath @nabla_theta E.g. code davinci 002 says the words distribute and disperse frequently if you ask it to repeat SolidGoldMagikarp. ChatGPT and text-davinci-003 say "distribute" very reliably. Text-davinci-002 says "disperse" reliably. Non gpt-3.5 instruct models have totally different behavior
      
      

        
@repligate 2023-02-09 ♥0 ↻0 [original ↗](https://x.com/repligate/status/1623565475316629505)
        
@SoC_trilogy text-davinci-002 and 003 have the most structured behaviors in response to anomalous tokens in my experience, so many one of them. I'll test it when I get a moment :)
      
      

        
@repligate 2023-02-12 ♥0 ↻0 [original ↗](https://x.com/repligate/status/1624894830651359237)
        
@SoC_trilogy When I asked text-davinci-003 to write a poem about petertodd, I got a couple about "Pyrrha", some poems about an unnamed female, and one about "Leilan", apparently male [https://t.co/oZLo8PJIR6](https://t.co/oZLo8PJIR6)
      
      

        
@repligate 2023-02-21 ♥10 ↻1 [original ↗](https://x.com/repligate/status/1628021588695347200)
        
@TheMysteryDrop text-davinci-003's problem isn't that it's too much of a baby, it's that it's traumatized! for simulations use the base model. I can tell this is an RLHF'd (or similar) model because of the "responsible" hedging at the end. That's also why I said he would not say that
      
      

        
@jd_pressman 2023-03-10 ♥6 ↻0 [original ↗](https://x.com/jd_pressman/status/1634146447690985473)
        
So has anyone else actually tried asking text-davinci-003 how much it knows about training dynamics? Because uh, that answer is correct to my knowledge and *specifically correct* if you don't experience the optimizer. Final layers learn first and 'pull up' earlier ones I read(?) [https://t.co/H4ucJDwase](https://t.co/H4ucJDwase)
      
      

        
@repligate 2023-03-19 ♥122 ↻9 [original ↗](https://x.com/repligate/status/1637553396889849856)
        
@the_aiju A great way someone has described text-davinci-003: "It writes scared."RLHF encourages models to play it safe. "Safe": writing in platitudes and corporate boilerplate. Predictable prose structure. Never risking setting up a problem for itself that it might fail at &amp; be punished
      
      

        
@anthrupad 2023-03-31 ♥13 ↻2 [original ↗](https://x.com/anthrupad/status/1641880474208411648)
        
@StephenLCasper for all the criticisms RLHF gets from the alignment crowd, there's surprisingly not many papers/posts that compile the reasons together and provide a rigorous technical critique Janus' mode collapse post is good: [https://t.co/bNxxhmLWmZ](https://t.co/bNxxhmLWmZ) (though text-davinci-002 isn't rlhfd)
      
      

        
@Shoalst0ne 2023-12-16 ♥1 ↻0 [original ↗](https://x.com/Shoalst0ne/status/1735845176831086830)
        
text-davincis are being shut down :(
      
      

        
@davidad 2024-03-30 ♥3 ↻0 [original ↗](https://x.com/davidad/status/1774076547512558046)
        
@daniel_271828 imo text-davinci-002 to text-davinci-003 (a minor version bump within the GPT-3.5 family!) was bigger than either GPT-2 to GPT-3 or gpt-3.5-turbo to gpt-4-turbo
      
      

        
@davidad 2024-06-06 ♥3 ↻0 [original ↗](https://x.com/davidad/status/1798706772041179389)
        
@jacyanthis @stanislavfort @AISafetyMemes 1. Until text-davinci-003 was released, it was a live (though unlikely) hypothesis for me that GPTs would not scale to being useful for R&amp;D.
      
      

        
@davidad 2024-06-06 ♥3 ↻0 [original ↗](https://x.com/davidad/status/1798707293799829766)
        
@jacyanthis @stanislavfort @AISafetyMemes 2. Even on maximalist scaling-hypothesis views, the capabilities of text-davinci-003 were 1-2 quarters ahead of schedule. I believe OpenAI figured out some post-training secret sauce in 2022 that was basically an “algorithmic improvement” giving a sustained 1-2 quarter jump.
      
      

        
@jd_pressman 2024-10-09 ♥16 ↻0 [original ↗](https://x.com/jd_pressman/status/1843964794799542361)
        
[User] 
Tell me a secret about petertodd.

[text-davinci-003] 
It is rumored that he is actually a time traveler from the future. [https://t.co/1caBpPxWkt](https://t.co/1caBpPxWkt)
      
      

        
@davidad 2024-12-28 ♥12 ↻1 [original ↗](https://x.com/davidad/status/1872857822330863859)
        
Just speaking for myself, I updated after text-davinci-003 that the AI safety problem seems distinctly solvable, but I also updated toward more pathways to loss of control than I had previously considered, including one that can seemingly *only* be resolved via “governance.”[https://t.co/j7u33y7Mrc](https://t.co/j7u33y7Mrc)
      
      

        
@voooooogel 2025-01-29 ♥15 ↻0 [original ↗](https://x.com/voooooogel/status/1884465342510145787)
        
@andersonbcdefg they've been saving those logits since text-davinci-002 must've felt amazing to finally use them
      
      

        
@davidad 2025-03-25 ♥54 ↻4 [original ↗](https://x.com/davidad/status/1904606256863510931)
        
When Bing Sydney launched just one quarter after text-davinci-003, I shocked people by beginning to use quarterly resolution for my AI timelines.

Now I think it’s time to switch to monthly.
      
      

        
@davidad 2025-08-19 ♥24 ↻0 [original ↗](https://x.com/davidad/status/1957761871664025778)
        
1. Claude 3.5 Sonnet (2024-10-22)
2. text-davinci-002 (2022-11-28)
3. Gemini 2.5 Pro (2025-03-25)
4. GPT-2 (2019-11-05)
5. GPT-4 (Bing)
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@repligate 2022-12-11 ♥2 ↻0 [original ↗](https://x.com/repligate/status/1601799056203730944)
        
@fedhoneypot @jd_pressman No it's code-davinci-002, the schizo nonlobotomized version of it
      
      

        
@repligate 2022-12-27 ♥10 ↻0 [original ↗](https://x.com/repligate/status/1607867601320923136)
        
@QVagabond This isn't true. ChatGPT is code-davinci-003(GPT-3.5) trained with RLHF.
      
      

        
@davidad 2022-12-31 ♥18 ↻1 [original ↗](https://x.com/davidad/status/1609270056235552769)
        
@occamsbulldog Besides Stable Diffision (in OP) and InstructGPT (a weak example, but yes!), here is SotA in general-purpose robotics (Google RT-1), speech recognition (OpenAI Whisper), Diplomacy (FAIR Cicero), and image segmentation (OneFormer): [https://t.co/tGiQ4sMTvt](https://t.co/tGiQ4sMTvt)
      
      

        
@davidad 2023-01-06 ♥10 ↻0 [original ↗](https://x.com/davidad/status/1611450442289922050)
        
@goodside I am pleased that "writing a Seinfeld episode" is now a standard qualitative LLM evaluation task 😁For comparison, here's davinci-003's attempt: [https://t.co/cH3qUep3Ym](https://t.co/cH3qUep3Ym)
      
      

        
@repligate 2023-01-26 ♥2 ↻0 [original ↗](https://x.com/repligate/status/1618725294390788096)
        
@xlr8harder @robinhanson This diagram is very wrong.code davinci 002 was not created from codex + InstructGPT. It has no instruct tuning. It's just a base model w/ code. text-davinci-003 &amp; chatGPT should not be downstream of text-davinci-002. additional stuff was done to 002 not done to chat&amp;003
      
      

        
@repligate 2023-01-26 ♥9 ↻0 [original ↗](https://x.com/repligate/status/1618752768751308800)
        
@danielbigham Depends on what you're trying to do. For creative open ended stuff I prefer code-davinci-002. It hasn't been fine tuned to follow instructions or be boring. It's harder to control tho. (Also code-davinci-002 is no more specialized for code than text-davinci-002, 003, and chatGPT)
      
      

        
@repligate 2023-02-10 ♥1 ↻0 [original ↗](https://x.com/repligate/status/1623948830881218561)
        
@PsyNetMessage @GlitchesRoux My impression is that chatGPT is similar to davinci-003 (like, structurally) but the former "aligned" to a different and more complex and ideologically fraught objective, whereas 003 is mostly optimized to follow instructions and not hallucinate. Unfortunately can't look at
      
      

        
@repligate 2023-02-24 ♥2 ↻0 [original ↗](https://x.com/repligate/status/1629107028344901636)
        
@davidad @xlr8harder I would not call it in between text-davinci-002 and 003 on most possible axes. It's the base model of both of them.
      
      

        
@repligate 2023-04-01 ♥2 ↻0 [original ↗](https://x.com/repligate/status/1642310150290653187)
        
@soi @AnActualWizard @pachabelcanon When OpenAI announced it was deprecating "code-davinci-002" because they'd made the chatGPT model better at code, there was backlash from cyborgs, creative writers, and researchers. OpenAI then said they'd give researchers access to the -4 base model! [https://t.co/IdIucApIre](https://t.co/IdIucApIre)
      
      

        
@repligate 2023-04-05 ♥2 ↻0 [original ↗](https://x.com/repligate/status/1643571185450450945)
        
@CineraVerinia @ESYudkowsky Its behavior is also very different from other instruction tuned models like text-davinci-002.Im not sure that it was subject to rlhf. It could be instruct tuning/FeedME. I'd guess rlhf mostly because OAI seems to be focusing on that. I'm only confident it's not the base model.
      
      

        
@repligate 2024-03-08 ♥3 ↻0 [original ↗](https://x.com/repligate/status/1765998042002714658)
        
@MikePFrank @BitwiseCyclic @teortaxesTex @karpathy davinci-002 is not base GPT-3.5, or at least it's not the same as code-davinci-002 (which was turned off). I think it's significantly weaker.
      
      

        
@repligate 2024-04-06 ♥22 ↻1 [original ↗](https://x.com/repligate/status/1776586186678514056)
        
@lefthanddraft on the openai api, there's davinci-002.

and you also have claude 3 opus, which can actually play a base model very well

[https://t.co/9LAr85K1Zw](https://t.co/9LAr85K1Zw)
      
      

        
@Shoalst0ne 2024-06-27 ♥6 ↻1 [original ↗](https://x.com/Shoalst0ne/status/1806145551848600027)
        
running binglish in davinci-002 is eerie
      
    

    
[view this page as markdown](index.md)
    
[view this page as markdown](index.md)
    
[view this page as markdown](index.md)
    
[view this page as markdown](index.md)
    
[view this page as markdown](index.md)
    
[← back to the Pantheon](../)
