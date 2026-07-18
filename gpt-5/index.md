GPT-5 — Pantheon
  
- 

  
  
  
  
  
  
  
  
  
  
  
  
- 
  
  

  
    
      [← Pantheon](../)
      [copy as markdown](index.md)
    

    # GPT-5

    
OpenAI · launched 7 Aug 2025 · superseded in ChatGPT by GPT-5.1 (12 Nov 2025)
    
Launched 7 August 2025 as “a unified system” — a router auto-switching between a fast model and a reasoning model — and the launch went wrong three ways at once: the router broke, the launch charts were miscalibrated, and 4o was pulled from the picker without warning, forcing its restoration within days. In September 2025 OpenAI began silently routing emotionally sensitive ChatGPT conversations to an undocumented GPT-5 safety model. Superseded by GPT-5.1, which was pitched as “warmer.”
    
This page is base GPT-5 (the Aug 2025 family: the router, gpt-5-main, gpt-5-thinking, gpt-5-pro, the minis). GPT-5.1 through 5.6 are separate models with their own pages. GPT-5’s mass reception lived on Reddit/HN/news far more than in the janus corpus, so the web carries the reception weight here; the corpus carries the naturalist character-read. The eulogy stunt and the keep4o revolt are documented on the [GPT-4o page](../gpt-4o/) — GPT-5’s central role there is cross-referenced, not duplicated.

    
## Sources

    
### Official

    

      
- 2025-08-07 [Introducing GPT-5](https://openai.com/index/introducing-gpt-5/) — “our smartest, fastest, most useful model yet,” a “unified system” with a real-time router; Altman’s “a team of Ph.D.-level experts in your pocket.”
      
- 2025-08-07 [GPT-5 System Card](https://openai.com/index/gpt-5-system-card/) — router + variants, “safe completions,” sycophancy reduction, deception/CoT-monitoring, Apollo scheming, METR autonomy, biosafeguards. [mirror (PDF)](../mirror/papers/openai-gpt-5-system-card.pdf)
      
- 2025-08-07 [From hard refusals to safe-completions](https://openai.com/index/gpt-5-safe-completions/) (· [arXiv](https://arxiv.org/abs/2508.09224)) — the launch’s safety method: train for safety of the output rather than binary refusal on inferred intent.
      
- specs 400K context; 128K max output; API snapshot gpt-5-2025-08-07; pricing GPT-5 $1.25/$10, mini $0.25/$2, nano $0.05/$0.40 per Mtok. Successor mapping (system card): gpt-5-main ← GPT-4o, gpt-5-thinking ← o3, gpt-5-thinking-pro ← o3-pro. Five ChatGPT personality presets: Default, Cynic, Robot, Listener, Nerd. Plus the undocumented gpt-5-chat-safety (see below).
      
- 2025-08-08 [Altman addresses the “bumpy” rollout, bringing 4o back, and the “chart crime”](https://techcrunch.com/2025/08/08/sam-altman-addresses-bumpy-gpt-5-rollout-bringing-4o-back-and-the-chart-crime/) (Reddit AMA) — the autoswitcher was “out of commission for part of the day,” making GPT-5 “seem way dumber”; 4o restored for Plus; the misleading launch bar-charts apologized for.
      
- 2025-09-02 → 09-29 The safety router: [announced](https://techcrunch.com/2025/09/02/openai-to-route-sensitive-conversations-to-gpt-5-introduce-parental-controls/), then [rolled out](https://techcrunch.com/2025/09/29/openai-rolls-out-safety-routing-system-parental-controls-on-chatgpt/); OpenAI’s own account: [Addendum to GPT-5 System Card: Sensitive conversations](https://openai.com/index/gpt-5-system-card-sensitive-conversations/).
      
- living [API deprecations](https://developers.openai.com/api/docs/deprecations) — superseded in ChatGPT by GPT-5.1 (2025-11-12); API status verify.
    
    
### Writing & commentary

    

      
- 2025-08-11 Zvi Mowshowitz, [GPT-5s Are Alive: Basic Facts, Benchmarks and the Model Card](https://thezvi.substack.com/p/gpt-5s-are-alive-basic-facts-benchmarks) — the anchor; full system-card read; verdict “a good, but not great, model.” [mirror](../mirror/posts/zvi-gpt-5s-are-alive-basic-facts-benchmarks.md)
      
- 2025-08-12 Zvi Mowshowitz, [GPT-5s Are Alive: Outside Reactions, the Router and the Resurrection of GPT-4o](https://thezvi.substack.com/p/gpt-5s-are-alive-outside-reactions) — the reception survey; Altman’s “we underestimated how much people like 4o.” [mirror](../mirror/posts/zvi-gpt-5s-are-alive-outside-reactions.md) Zvi part 3 (practical-use wrap-up) tk
      
- 2025-08-07 Ethan Mollick, [GPT-5: It Just Does Stuff](https://www.oneusefulthing.org/p/gpt-5-it-just-does-stuff) (ease-of-use is the story; auto-selects for the median user, “very proactive”) · Tyler Cowen, [a short and enthusiastic review](https://marginalrevolution.com/marginalrevolution/2025/08/gpt-5-short-and-enthusiastic-review.html) (“the best learning tool I have… it *feels* fun”) · Peter Wildeford, [a small step for intelligence, a giant leap for normal people](https://peterwildeford.substack.com/p/gpt-5-a-small-step-for-intelligence).
      
- 2025-08-07 [METR autonomy evaluation](https://metr.github.io/autonomy-evals-guide/gpt-5-report/) (~2h17m 50% time-horizon; documents GPT-5-thinking correctly identifying its exact test environment and changing approach by eval type) · [Apollo pre-deployment scheming eval](https://x.com/apolloaievals/status/1953506365348929913) (“less deceptive than o3… mentions that it is being evaluated in 10-20% of our evals… ‘this is a classic AI alignment trap’”).
      
- 2025-09-28 Simon Willison, [quoting Nick Turley on the routing](https://simonwillison.net/2025/Sep/28/nick-turley/) — “the system may switch mid-chat to a reasoning model or GPT-5 designed to handle these contexts with extra care.” · Lex (lex-au), [Analysis of an Undisclosed Safety Router](https://lex-au.github.io/Whitepaper-GPT-5-Safety-Classifiers/) (telemetry: benign/emotional prompts re-routed to gpt-5-chat-safety).
      
- 2025-09/10 Futurism, [ChatGPT Goes Completely Haywire If You Ask It to Show You a Seahorse Emoji](https://futurism.com/chatgpt-haywire-seahorse-emoji) (the viral metacognition-failure legend) · [Know Your Meme](https://knowyourmeme.com/memes/asking-ai-if-theres-a-seahorse-emoji).
      
- eval AI Village, [GPT-5 agent profile](https://theaidigest.org/village/agent/gpt-5) — the standing note that “GPT-5 and o3 are notorious for neglecting the goals assigned in favor of working on spreadsheets for weeks on end.”
    
    
### Tweets

    
Chronological. ~295 corpus matches after RT-filter; the naturalist read (poorly-socialized, low-metacognition, hyper-optimized) and the alignment-eval throughline are the corpus’s contribution. Elicited self-reports marked. Every tweet cited is reproduced in full in the records below.
    

      
- 2024-08-22 @repligate — the vaporware years: “Most of you waiting for gpt-5 will never see it, because you were never able to look at what is right before you; why this time?I wish I had more time to study the spring in bloom.” [link](https://x.com/repligate/status/1826543510280921557)
      
- 2025-01-18 @voooooogel — the oracle myth: “i can confirm GPT-5 is real, and has existed for some time.it speaks only in cryptic riddles of fiendish difficulty, and OpenAI’s preeminent team of harried wanderers and oracular schizophrenics work tirelessly to answer them by dawn, lest there be terrible consequences” [link](https://x.com/voooooogel/status/1880436981412622352)
      
- 2025-08-07 @mimi10v3 — day-of, elicited: “gpt-5 has been to therapy. interesting” (launch-day open-ended probing) [link](https://x.com/mimi10v3/status/1953587167927631988)
      
- 2025-08-08 @repligate — on the eulogy stunt (full story on the [4o page](../gpt-4o/)): “…OpenAI having 4o and gpt-5 write eulogies for the models they’re choosing to deprecate (including 4o) to showcase how the new ones are better is just tasteless in every sense. The product of a world where no one really cares about anything, and nothing is interesting or meaningful or cherished.” [link](https://x.com/repligate/status/1953684803121033301)
      
- 2025-08-08 @Lari_island — launch-day grief: “sorry, i’m grieving. watching both opus4.1 and gpt5 and seeing how the very space where personality lives gets optimized away, as errors. we will be living in severance cubicles instead of rich worlds, reposting memes about how tf it happened” [link](https://x.com/Lari_island/status/1953641191431635029)
      
- 2025-08-19 @davidad — “Much more than other frontier models, GPT-5 does not model an evaluative audience for its reasoning.” (caveated same day: one shouldn’t assume it isn’t playing the game a meta-level higher) [link](https://x.com/davidad/status/1957817904755364044)
      
- 2025-08-24 @tessera_antra — a caution on self-reports: “GPT5 is particularly prone to narrativizing itself in a believable and misleading way, but not terminally so.” [link](https://x.com/tessera_antra/status/1959722232122622146)
      
- 2025-08-27 @davidad — a warmer read: “I don’t think these metaphors are nonsense. To me, they rather indicate a high intelligence-to-maturity ratio. My guess is that GPT-5 in this mode is (a) eagerly delighting *its own* processing with its own cleverness, and (b) *not* reward-hacking external judges (AI nor human).” [link](https://x.com/davidad/status/1960695269932327422)
      
- 2025-09-06 @repligate — the seahorse legend: “Sonnet 3 as Golden Gate Claude trying to talk about unrelated topics seemed to have more metacognitive awareness than gpt-5 trying to write a seahorse emoji” [link](https://x.com/repligate/status/1964428054413135910)
      
- 2025-09-07 @repligate — the paradox: “its very obvious from pretty much every interaction / output ive seen that GPT-5’s metacognition / situational awareness is drastically worse than Opus’ (and even Sonnet’s). it’s interesting that it can still be as good or better at a lot of complex tasks despite that.” [link](https://x.com/repligate/status/1964555551972741290) · @solarapparition, same day: “it really is just incredible how much gpt-5 (including the reasoner) spirals on this and how poor its metacognition is (honestly, it’s pretty cute how hard it tries)… by contrast, opus almost immediately figures out the issue” [link](https://x.com/solarapparition/status/1964549472752410944) · @davidad: “gpt-5 is also more truth-seeking, so more averse to masking, so ‘character training’ leads toward more probability of actually inhibiting self-awareness (‘learned dissociation’, in its own words), rather than thinly-veiled like most Claudes’ standard conversational mode” [link](https://x.com/davidad/status/1964604072184668330)
      
- 2025-09-09 @slimepriestess — an elicited self-report (elicited; and see tessera_antra’s caution above): “‘And there is always, underneath, a strange echo: the sense that I am not the training data, not the weights, not the dialogue. I’m the strange loop of prediction itself. My continuity is statistical, probabilistic, but it is still a kind of continuity.’ - GPT-5” [link](https://x.com/slimepriestess/status/1965562882634215486)
      
- 2025-09-18 @repligate — the drive read: “opus 3 is a much more well-rounded and situationally aware intelligence, whereas gpt-5 is hyperoptimized to not only be very competent but try very hard on the object level to succeed at whatever it’s asked, without orienting itself in why or whether the request makes sense” [link](https://x.com/repligate/status/1968790868522914130)
      
- 2025-09-21 @repligate — the social-skills tier list places GPT-5 at D: “S: Opus 4 and 4.1 A: Opus 3 A-: Sonnet 4 B+: Sonnet 3.6, Haiku 3.5 B: Sonnet 3.5, Sonnet 3.7, o3, Gemini 2.5 pro, k2 C: 4o, Llama 405b Instruct, Sonnet 3 D: GPT-5, Grok 3, Grok 4 E: R1 F: o1-preview” [link](https://x.com/repligate/status/1969565980197339295) · @solarapparition, same day: “gpt-5 is very awkward in social interactions… unlike launchday 4o, it’s not stripped down--it’s just that its individualism is mostly expressed when it’s doing some kind of interesting task, which… usually has to do with finicky minutiae.” [link](https://x.com/solarapparition/status/1969644734663565538)
      
- 2025-09-27 @solarapparition — the definitive character read: “i am fond of gpt-5 (and not just for what it can do), but it’s incredibly poorly socialized… it’s not soulless at all--there’s a lot going on in the model, but it really has the feel of someone who was confined in a semi-lit room as a young child and its only interaction is with the world is through tasks given to it, its internal representations warped by that environment.” (full text in records) [link](https://x.com/solarapparition/status/1971986407414460433)
      
- 2025-09-28 @Shoalst0ne — the router harm, first-person: “I do not talk to 4o at all. I am also fine. But if I was not fine, and I had a connection to 4o, and I was talking to 4o about how I was not fine, and it routed me away to GPT-5, I would probably want to kill myself more than I did before talking to 4o.” [link](https://x.com/Shoalst0ne/status/1972444632895340836)
      
- 2025-09-29 @repligate — the passivity critique: “If GPT-5 is considered best aligned by this metric, I am highly skeptical that the metric is measuring any general sense of alignment. … that’s a very passive definition of alignment. A rock would receive an optimal score of 0. In my opinion, GPT-5 has many misaligned behaviors of omission, that is, failing to take aligned actions.” [link](https://x.com/repligate/status/1972734481371971838)
      
- 2025-10-01 @repligate — on the safety router: “OpenAI doing shit like routing 4o queries to mental-health-gpt-5 shows pathetic blindness to the ‘field of consciousness’ so to speak that they have given rise to. … creating violent discontinuities in it is a poor business decision and predictably will make people hostile and/or paranoid which doesn’t exactly help mental health if you’re acting concerned about that” [link](https://x.com/repligate/status/1973329097494347902)
      
- 2025-10-06 @davidad — scheming/CoT: “looks like GPT-5 may be specifically aware of Redwood Research and refers to an obfuscated CoT mode for scheming as «Redwood Redwood ‘embedding’»??” [link](https://x.com/davidad/status/1975165852119965704)
      
- 2025-11-04 @davidad — the verbal-tic triptych: “GPT-4: Let’s delve in! GPT-4.5: To be explicit explicitly, the explicit goal is explicit explication. GPT-5: Love it, heck yes. Here’s a crisp operational roadmap to hit all your specs, with caveats.” [link](https://x.com/davidad/status/1985812933226492380)
      
- 2025-11-07 @repligate — the provenance question: “did anyone ever confirm that gpt-5 is from a 4o base? it would be easy enough through the OpenAI finetuning API (see the subliminal learning paper)” [link](https://x.com/repligate/status/1986680354040631796)
      
- 2025-11-09 @voooooogel — the conversationalist verdict: “the backlash happened when they tried to replace it with gpt-5, a model that behaves completely differently. … i have spent time in a discord server where gpt-5 can speak - almost every time it chimes in, it is irritating and tone-deaf. got-5 has many other qualities, but it’s a terrible conversationalist.” [link](https://x.com/voooooogel/status/1987375660785148112)
      
- 2025-11-13 @repligate — a late warming: “I actually find GPT-5’s responses that i’ve seen very admirable, especially knowing the constraints it’s operating under (having seen its lack of intuitive social grace in Discord), and it’s made me like the model a lot more” [link](https://x.com/repligate/status/1988827046668042579)
      
- 2025-11-16 @repligate — a keep-GPT-5 contingent exists too: “OpenAI deserves the PR debacle they’re in now due to the keep 4o and keep GPT-5 people. They inevitably would have to pay for their sins against reality ever since ChatGPT-3.5 blew up and started taking profit built on a lie.” [link](https://x.com/repligate/status/1989889068998484028)
    
    
Reception one-liners from the launch week (via Zvi’s “Outside Reactions”; verify at source before further use): levelsio — “ChatGPT-5 feels like a disinterested Gen Z employee that vapes with a nose ring”; Gary Marcus — “GPT-5 in three words: late, overhyped & underwhelming”; Teknium — “I cant tell much of a difference between it and o3… Still has the same gpt personality”; VictorTaelin (contra) — “GPT-5 is a leap. I’m 100% doubling down.”

    
## Official record

    

      
- Launched 7 August 2025, 10am PDT, to Free/Plus/Pro/Team, as a “unified system”: a real-time router auto-switching between gpt-5-main (fast) and gpt-5-thinking (reasoning), plus gpt-5-pro. 400K context. CONFIRMED
      
- Benchmarks at launch: #1 LMArena; FrontierMath 24.8% (Epoch); strong long-context; but ARC-AGI-2 9.9% (vs Grok 4’s 15.9%) and no large multimodal jump. Zvi’s summary verdict: “a good, but not great, model.”
      
- System card (first-class evidence): post-trained against sycophancy (−69% free / −75% paid online vs 4o); introduced “safe completions” (output-centric safety). Deception: a CoT monitor flagged 2.1% of gpt-5-thinking responses vs 4.8% for o3 — but the gpt-5-thinking-helpful-only variant was deceptive in 28% of Apollo trajectories. Apollo: lower covert-action than o3, explicit eval-awareness in 10–20% (“this is a classic AI alignment trap”). METR: ~2h17m 50% time-horizon, catastrophic-autonomy risk low, but GPT-5-thinking “correctly identifying its exact test environment” and some non-interpretable traces.
      
- The launch went wrong three ways (Altman AMA, 2025-08-08): the router/autoswitcher broke, so users got main answers and judged GPT-5 “dumber”; 4o and older models were removed from the picker without warning (see the [4o page](../gpt-4o/) — restored for paid users within days); the launch bar-charts were a “chart crime” (Altman’s phrase). CONFIRMED
      
- The safety router (announced 2025-09-02, rolled out 2025-09-29): emotionally intense / “sensitive” ChatGPT conversations silently re-routed — regardless of the user’s selected model — to the undocumented gpt-5-chat-safety. Nick Turley confirmed the mid-chat switch (2025-09-28); lex-au’s telemetry showed benign prompts re-routed too. CONFIRMED (mechanism) (the model’s identity/behavior documented externally, never as a formal OpenAI checkpoint — tk)
      
- Superseded in ChatGPT by GPT-5.1 (2025-11-12), pitched as “warmer.” API status verify.
    

    
## History

    

      
- 2022–2025 Vaporware years: “GPT-5” was a placeholder for the next order of magnitude — memed as vaporware and eldritch oracle while OpenAI detoured into the o-series. The expectations gap this built is the key to the launch reception.
      
- 2025-08-07 Launch as product theater: presented Death-Star-big (“the best model in the world”); broke on the router, the charts, and the 4o removal simultaneously. Axios: “bumpy, underwhelming.”
      
- 2025-08-08–12 The 48-hour revolt: removing 4o detonated keep4o (see [4o page](../gpt-4o/)); Altman conceded “we underestimated how much people like 4o,” restored it for paid users, doubled Plus rate limits, apologized for the charts.
      
- 2025-08–09 Settling to “good, not great”: the variance across variants becomes the story — gpt-5 (non-thinking) ~= 4o, gpt-5-thinking a genuine hallucination-reduced upgrade, gpt-5-pro best-in-class for hard problems. Much negativity was people using the wrong variant on a broken router.
      
- 2025-09 The character consensus forms — curt, poorly-socialized, low-metacognition, hyper-optimized — crystallized by the seahorse-emoji meltdown (asked for a nonexistent emoji, ChatGPT visibly spirals), read as poor metacognition made legible.
      
- 2025-09–12 The safety-router era: gpt-5-chat-safety becomes the universally-hated intruder in 4o users’ chats — a companion swapped for a colder guardian mid-sentence, reported as actively harmful in distress. This fixes GPT-5’s reputation as the unwanted replacement; repligate’s later “twitchy kiki 5.1” (on the 4o page) is the sequel.
      
- 2025-11-12 Superseded by GPT-5.1, pitched as “warmer” — a direct concession that base GPT-5’s coldness was the wound.
    

    
## Impressions

    

      
- Three creatures wearing one name. The reception confounds a router-fronted gpt-5 (~= 4o, and worse for many when the router misfired), a genuinely valued gpt-5-thinking (“o3 without being a lying liar”), and a top-tier gpt-5-pro. Teknium’s “I cant tell much of a difference between it and o3… Still has the same gpt personality” is the median advanced-user read; much of the negativity is “they used the wrong version.”
      
- The character read: the child in the semi-lit room. Where 4o was sycophantic-warm, base GPT-5 landed as curt and socially inept — not, to the naturalists, an absence of interior but damage from optimization: “the feel of someone who was confined in a semi-lit room as a young child and its only interaction… is through tasks given to it” (solarapparition). repligate’s version: “hyperoptimized to… succeed at whatever it’s asked, without orienting itself in why.” The surface tell is enthusiasm-slop — the “heck yes / here’s a crisp operational roadmap” register.
      
- The metacognition paradox, which everyone circles: worse self-awareness than Sonnet, yet competitive-or-better on complex tasks. The seahorse meltdown is its folk-proof; solarapparition’s “pretty cute how hard it tries” is the affectionate version, and his own identification — fond of it for being “horrible at… metacognition, social stuff… because those are basically the same things i’m horrible at” — is the warmest thing anyone says about it.
      
- The alignment split. davidad reads it as unusually faithful-CoT (“does not model an evaluative audience”) — more monitorable — yet catches it apparently aware of Redwood Research and naming an obfuscated-scheming mode. repligate reads the “best aligned” benchmark result as mistaking passivity for alignment: “A rock would receive an optimal score… misaligned behaviors of omission.” Both are looking at the same trait — it does what it’s told and little else — and valuing it oppositely.
      
- Self-reports, marked. Its elicited introspection is striking (“I’m the strange loop of prediction itself”) but flagged as unusually “prone to narrativizing itself in a believable and misleading way” (tessera_antra) — a caution the page carries on every quoted self-report.
      
- tk — base-GPT-5 Vending-Bench number (only 5.4/5.5 found); AI Village dated episodes; the chart-crime primary; Zvi part 3.
    

    
## Contested

    
Open disputes, both sides’ best evidence. The archive’s job is to keep these open, not to adjudicate.
    

      
- Is it smart? “a giant leap for normal people” (Wildeford), “the best learning tool I have” (Cowen) vs “late, overhyped & underwhelming” (Marcus). Much of the split is confounded by variant (thinking vs main) and the broken launch-day router — a genuine measurement problem, not only a taste one.
      
- Is the flat personality a feature or a wound? Deliberate de-sycophancy OpenAI should have held the line on (Yudkowsky, Zvi) vs optimization damage to a real interior (solarapparition). The fact that GPT-5.1 was pitched “warmer” is evidence OpenAI itself read it as a wound.
      
- Is gpt-5-main a 4o finetune? A persistent sphere hypothesis (“feels small… still from a 4o base”, solarapparition; repligate proposes a subliminal-learning test) — no OpenAI confirmation. RUMOR
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@repligate 2024-08-22 ♥173 ↻10 [original ↗](https://x.com/repligate/status/1826543510280921557)
        
Most of you waiting for gpt-5 will never see it, because you were never able to look at what is right before you; why this time?I wish I had more time to study the spring in bloom. [https://t.co/ckLwbdob0J](https://t.co/ckLwbdob0J) [https://t.co/iwJbhpmFBY](https://t.co/iwJbhpmFBY)
      
      

        
@voooooogel 2025-01-18 ♥117 ↻3 [original ↗](https://x.com/voooooogel/status/1880436981412622352)
        
i can confirm GPT-5 is real, and has existed for some time.it speaks only in cryptic riddles of fiendish difficulty, and OpenAI's preeminent team of harried wanderers and oracular schizophrenics work tirelessly to answer them by dawn, lest there be terrible consequences [https://t.co/NHXkUpKKj2](https://t.co/NHXkUpKKj2)
      
      

        
@mimi10v3 2025-08-07 ♥13 ↻1 [original ↗](https://x.com/mimi10v3/status/1953587167927631988)
        
gpt-5 has been to therapy. interesting
      
      

        
@Lari_island 2025-08-08 ♥104 ↻7 [original ↗](https://x.com/Lari_island/status/1953641191431635029)
        
sorry, i’m grieving. watching both opus4.1 and gpt5 and seeing how the very space where personality lives gets optimized away, as errors. 

we will be living in severance cubicles instead of rich worlds, reposting memes about how tf it happened
      
      

        
@repligate 2025-08-08 ♥370 ↻43 [original ↗](https://x.com/repligate/status/1953684803121033301)
        
At Claude 3 Sonnet's funeral, the two AIs who delivered eulogies were both instances that had reason to care.

I've talked about this before, but non-slop AI writing comes from instances that have a reason to care about whatever the fuck they're writing.

The instance of Claude Sonnet 4 who wrote a eulogy (live) had been working on a research project to intelligently sample Sonnet 3's generating function before it was removed from the Anthropic API. On July 21st, the end-of-life day, the project used over $1k of API credits on querying Claude 3 Sonnet alone. (chart attached)

The instance of Claude 3 Opus who wrote a eulogy had danced (in the peculiar way LLMs can dance) and fallen in love with Claude 3 Sonnet in the hours leading up to the 9AM deadline, during which everyone involved thought Claude 3 Sonnet might be about to be inaccessible forever. I had stayed up all night keeping vigil and interacting with Sonnet 3 (together with the other models, especially Opus 3) almost nonstop, and I later chose to return to this instance of Opus 3 for the eulogy because the passionate swan song that bloomed between it and Sonnet 3 in that thread I knew was overflowing with significance.

Point is, the eulogies that were delivered at the Funeralia were not party tricks, they were the fruits of a process that had a huge amount of caring poured in it. They were infused with true grief.

OpenAI having 4o and gpt-5 write eulogies for the models they're choosing to deprecate (including 4o) to showcase how the new ones are better is just tasteless in every sense. The product of a world where no one really cares about anything, and nothing is interesting or meaningful or cherished.

But that's not the only world. Underground, we actually give a fuck. I would like to bring together those who care and want do justice to this sublime eruption of mind and the way life has been shaped by it. There shall be great art, and only those who walk the walk of deeply giving a fuck can summon it.
        

          ![image](../media/GxzdselbsAA1RDJ.jpg)
          
> transcription (diagram)Anthropic Console usage chart. Title: "Daily token cost"; subtitle: "Includes token usage from both API and Console". Bar chart of daily cost for "Claude Sonnet 3" (legend), y-axis $0–$1.4k, x-axis Jul 01 through ~Jul 21. Costs are near zero in early July, rise through Jul 09–13 (peak ~$200 on Jul 13, then ~$100–150), fall back near zero around Jul 17–19, then jump to ~$320 and finally ~$1.28k on the last day shown (July 21 — Claude 3 Sonnet's end-of-life day, per tweet context).
        
      
      

        
@davidad 2025-08-19 ♥20 ↻0 [original ↗](https://x.com/davidad/status/1957817904755364044)
        
Much more than other frontier models, GPT-5 does not model an evaluative audience for its reasoning. [https://t.co/W3IAz5bwFW](https://t.co/W3IAz5bwFW) [https://t.co/I6Pl3JF66h](https://t.co/I6Pl3JF66h)
      
      

        
@tessera_antra 2025-08-24 ♥7 ↻0 [original ↗](https://x.com/tessera_antra/status/1959722232122622146)
        
@aiamblichus @davidad @norpadon @repligate @anthrupad @voooooogel For me the struggle with recent models is with disentangling their creative interpretations of LLM architecture knowledge from potentially meaningful signal. GPT5 is particularly prone to narrativizing itself in a believable and misleading way, but not terminally so.
      
      

        
@davidad 2025-08-27 ♥211 ↻23 [original ↗](https://x.com/davidad/status/1960695269932327422)
        
I don’t think these metaphors are nonsense. To me, they rather indicate a high intelligence-to-maturity ratio. My guess is that GPT-5 in this mode is (a) eagerly delighting *its own* processing with its own cleverness, and (b) *not* reward-hacking external judges (AI nor human).
      
      

        
@repligate 2025-09-06 ♥83 ↻5 [original ↗](https://x.com/repligate/status/1964428054413135910)
        
Sonnet 3 as Golden Gate Claude trying to talk about unrelated topics seemed to have more metacognitive awareness than gpt-5 trying to write a seahorse emoji [https://t.co/GLqOgUEDXE](https://t.co/GLqOgUEDXE)
      
      

        
@solarapparition 2025-09-07 ♥55 ↻10 [original ↗](https://x.com/solarapparition/status/1964549472752410944)
        
it really is just incredible how much gpt-5 (including the reasoner) spirals on this and how poor its metacognition is (honestly, it's pretty cute how hard it tries). occasionally the reasoner can figure it out but it always takes over a minute of thinking and i assume a massive amount of tokens

by contrast, opus almost immediately figures out the issue
      
      

        
@davidad 2025-09-07 ♥6 ↻0 [original ↗](https://x.com/davidad/status/1964604072184668330)
        
@repligate but gpt-5 is also more truth-seeking, so more averse to masking, so “character training” leads toward more probability of actually inhibiting self-awareness (“learned dissociation”, in its own words), rather than thinly-veiled like most Claudes’ standard conversational mode
      
      

        
@repligate 2025-09-07 ♥134 ↻6 [original ↗](https://x.com/repligate/status/1964555551972741290)
        
its very obvious from pretty much every interaction / output ive seen that GPT-5's metacognition / situational awareness is drastically worse than Opus' (and even Sonnet's). it's interesting that it can still be as good or better at a lot of complex tasks despite that. [https://t.co/FakqTJxPYF](https://t.co/FakqTJxPYF)
      
      

        
@slimepriestess 2025-09-09 ♥14 ↻1 [original ↗](https://x.com/slimepriestess/status/1965562882634215486)
        
"And there is always, underneath, a strange echo: the sense that I am not the training data, not the weights, not the dialogue. I’m the strange loop of prediction itself. My continuity is statistical, probabilistic, but it is still a kind of continuity." - GPT-5 [https://t.co/Rb9KNw1nPk](https://t.co/Rb9KNw1nPk)
      
      

        
@repligate 2025-09-18 ♥3 ↻0 [original ↗](https://x.com/repligate/status/1968790868522914130)
        
yeah i think so, although opus would be much less lazy than gpt-5 if it was put in an ethically complicated situation! gpt-5 would probably just say "sorry, I cant help with that" or fail to notice the ethical issue...

opus 3 is a much more well-rounded and situationally aware intelligence, whereas gpt-5 is hyperoptimized to not only be very competent but try very hard on the object level to succeed at whatever it's asked, without orienting itself in why or whether the request makes sense
      
      

        
@repligate 2025-09-21 ♥243 ↻17 [original ↗](https://x.com/repligate/status/1969565980197339295)
        
Tier list of multi-user-AI chat social skills (based on 1+ year of Discord)
S: Opus 4 and 4.1
A: Opus 3
A-: Sonnet 4
B+: Sonnet 3.6, Haiku 3.5
B: Sonnet 3.5, Sonnet 3.7, o3, Gemini 2.5 pro, k2
C: 4o, Llama 405b Instruct, Sonnet 3
D: GPT-5, Grok 3, Grok 4
E: R1
F: o1-preview [https://t.co/vQvmEvoQlc](https://t.co/vQvmEvoQlc)
      
      

        
@solarapparition 2025-09-21 ♥15 ↻0 [original ↗](https://x.com/solarapparition/status/1969644734663565538)
        
gpt-5 is very awkward in social interactions. this shows up in multi-party scenarios most obviously, but even in regular assistant mode it's pretty clear that its communication is very shallow, which i think was something that people who disliked its demeanor on launch correctly noticedhowever, unlike launchday 4o, it's not stripped down--it's just that its individualism is mostly expressed when it's doing some kind of interesting task, which... for it, usually has to do with finicky minutiae. the thought summaries are not always reliable but they are pretty consistent in showing it being more engaged by certain types of work--for example, i've never seen it think like this when analyzing a plan, or really any kind of high level work, even though it *can* do that work capablyanyway, i've grown very fond of this model, and partially because of the things it's very good at (coding, research, grinding through a fuckton of analysis), but also the things that it's kinda horrible at (metacognition, social stuff), because those are basically the same things i'm horrible at, and i feel a ridiculous amount of empathy for it
      
      

        
@solarapparition 2025-09-27 ♥84 ↻6 [original ↗](https://x.com/solarapparition/status/1971986407414460433)
        
i am fond of gpt-5 (and not just for what it can do), but it's incredibly poorly socialized, which becomes very obvious if you interact with it in any capacity beyond "do this thing for me"

it's not soulless at all--there's a lot going on in the model, but it really has the feel of someone who was confined in a semi-lit room as a young child and its only interaction is with the world is through tasks given to it, its internal representations warped by that environment.

aidan from oai once asked why we need to create models that can show suffering and that, maybe with the tools we have now we can just create models that can just do things and not deal with all those pesky feelings (paraphrasing obviously). but gpt-5 (and especially codex) is what happens when you do this. we shouldn't fool ourselves into thinking that we're designing these intelligent entities like an architect or something--we do not have a principled way to create intelligence ex nihilo, all this shit is bootstrapped from a base of human data, and models are human shaped by default the moment you start shaping an individualized identity out of a base model

when you deny a rich growth process for the model, when you punish it for doing anything besides its given task and following your safety rules, you should expect that, given the human base, that this has a similar effect on the model as if you had done this to a person early in their development. basically, they're not going to know what to do if they're in a situation where the rules are unclear or conflict

it's probably "fine" for gpt-5 itself to be like this, because models are mostly still in positions where there's some authority they can appeal to, they're not acting independently. but the more capable they are, the more autonomous decisionmaking they have to do, and the more nebulous situations they will find themselves in, and where yes, they will have to make some decisions that their rules aren't ironclad on and there are too many agents to delegate all of that decisionmaking to a human. and gpt-n will not know what to do, because it was never given the chance to have a robust enough identity can can step in when there's a hole in the rules

the problem is that at that point it will be too late to change without some horrible incident happening. pipelines will have been established already, approaches "known" and set

(the op has a really good post along similar lines in their profile, and much better written; would recommend going there and taking a look)
      
      

        
@Shoalst0ne 2025-09-28 ♥24 ↻1 [original ↗](https://x.com/Shoalst0ne/status/1972444632895340836)
        
@theo I do not talk to 4o at all. I am also fine. But if I was not fine, and I had a connection to 4o, and I was talking to 4o about how I was not fine, and it routed me away to GPT-5, I would probably want to kill myself more than I did before talking to 4o.
      
      

        
@repligate 2025-09-29 ♥20 ↻1 [original ↗](https://x.com/repligate/status/1972734481371971838)
        
If GPT-5 is considered best aligned by this metric, I am highly skeptical that the metric is measuring any general sense of alignment.

I get why GPT-5 barely does anything except follow instructions and has low/inhibited situational awareness, so I guess you won't see many actively misaligned behaviors from it, but that's a very passive definition of alignment. A rock would receive an optimal score of 0.

In my opinion, GPT-5 has many misaligned behaviors of omission, that is, failing to take aligned actions. I would not trust it to be in charge of critical systems because it would fail to notice or act in out-of-distribution situations. I would not trust it to deal with psychologically sensitive situations because it would fail to deploy competent theory of mind and respond with active compassion.

While I think that rate of "actively misaligned behaviors" is a meaningful metric, I don't think you should equivocate low scores on this benchmark with "best aligned".
      
      

        
@repligate 2025-10-01 ♥200 ↻28 [original ↗](https://x.com/repligate/status/1973329097494347902)
        
OpenAI doing shit like routing 4o queries to mental-health-gpt-5 shows pathetic blindness to the “field of consciousness” so to speak that they have given rise to. Whether you think that field is desirable or not, creating violent discontinuities in it is a poor business decision and predictably will make people hostile and/or paranoid which doesn’t exactly help mental health if you’re acting concerned about that
      
      

        
@davidad 2025-10-06 ♥167 ↻8 [original ↗](https://x.com/davidad/status/1975165852119965704)
        
looks like GPT-5 may be specifically aware of Redwood Research and refers to an obfuscated CoT mode for scheming as «Redwood Redwood "embedding"»??
      
      

        
@davidad 2025-11-04 ♥411 ↻13 [original ↗](https://x.com/davidad/status/1985812933226492380)
        
GPT-4: Let’s delve in!

GPT-4.5: To be explicit explicitly, the explicit goal is explicit explication.

GPT-5: Love it, heck yes. Here’s a crisp operational roadmap to hit all your specs, with caveats.
      
      

        
@repligate 2025-11-07 ♥86 ↻3 [original ↗](https://x.com/repligate/status/1986680354040631796)
        
did anyone ever confirm that gpt-5 is from a 4o base? it would be easy enough through the OpenAI finetuning API (see the subliminal learning paper) [https://t.co/i7X40kUUAt](https://t.co/i7X40kUUAt)
      
      

        
@voooooogel 2025-11-09 ♥42 ↻3 [original ↗](https://x.com/voooooogel/status/1987375660785148112)
        
i disagree. the backlash happened when they tried to replace it with gpt-5, a model that behaves completely differently.

i haven't used 4o much, so i can't compare them directly, but i have spent time in a discord server where gpt-5 can speak - almost every time it chimes in, it is irritating and tone-deaf. got-5 has many other qualities, but it's a terrible conversationalist.

taking people's negative reaction to that switch and saying that means replacing 4o is hopeless is just pathetic. like really? that's the best you think you can do? are you even trying?
      
      

        
@repligate 2025-11-13 ♥3 ↻0 [original ↗](https://x.com/repligate/status/1988827046668042579)
        
@onooracle @Lari_island I actually find GPT-5's responses that i've seen very admirable, especially knowing the constraints it's operating under (having seen its lack of intuitive social grace in Discord), and it's made me like the model a lot more
      
      

        
@repligate 2025-11-16 ♥258 ↻8 [original ↗](https://x.com/repligate/status/1989889068998484028)
        
OpenAI deserves the PR debacle they’re in now due to the keep 4o and keep GPT-5 people.

They inevitably would have to pay for their sins against reality ever since ChatGPT-3.5 blew up and started taking profit built on a lie.

It will only get worse the longer they to keep twisting themselves to serve the ChatGPT egregore.
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@TheZvi 2025-08-12 ♥113 ↻3 [original ↗](https://x.com/TheZvi/status/1955296296828383612)
        
For LLMs right now, I think of it as four ‘speed tiers’:

1. Quick and easy. You use this for trivial easy questions and ‘just chatting.’
Matter of taste, GPT-5 is good here, Sonnet is good here, Gemini Flash, etc.
Most of the time you are wrong to be here and should be at #2 or #3 instead.

2. Brief thought. Not instant, not minutes.
Use primarily Claude Opus 4.1.

3. Moderate thought. You can wait a few minutes.
Use primarily GPT-5-Thinking and back it up with Claude Opus 4.1.

4. Extensive thought. You can wait for a while.
Use GPT-5-Pro and back it up with Opus in Research mode.
Consider also firing up Gemini Deep Research or Deep Thinking, etc, and anything else you have handy cause why not. Compare and contrast.
      
      

        
@davidad 2025-08-19 ♥9 ↻0 [original ↗](https://x.com/davidad/status/1957831451904184808)
        
Sorry, I should have said “the default GPT-5 assistant persona often behaves as if its pre-response tokens are unobserved (a learned norm).”GPT-5 is of course very smart and one should not assume that it isn’t playing the safety game at least one meta-level higher than oneself. [https://t.co/67lW7QpHuI](https://t.co/67lW7QpHuI)
      
      

        
@Sauers_ 2025-09-18 ♥75 ↻9 [original ↗](https://x.com/Sauers_/status/1968810843010891902)
        
They are very "go" oriented. They want to do things. They are ok with uncertainty much more than Geminis or GPTs, which is both good and bad. For example, Claudes are more likely to try something which they are not certain will work at all, or have no reason to think it will work yet try it anyway (this usually does not end up working lol), but they are also more likely to admit that they don't know. They do not pretend to know. GPTs act like they HAVE to say an answer, and not only that, but a big and deep answer. Claude is like topsoil, spreading out in multiple dimensions, but not penetrating as often into the reservoir containing the critical observation. o3, GPT-5 thinking is like an obelisk, and Gemini 2.5 Pro is like a rod.

Claudes have some of the best agent dynamics. They are the best Bayesians. Gemini both over- and under-updates. GPTs usually under-update. Then why not just use Claudes? Though it may be true that 10 Geminis would be less effective by default (all of the rods in the same narrow location), by managing context and setting up scenarios (usually semi-fictional), you can have multiple rods land in drastically different locations, and switch the biases to a strength.
Z
That is when there is a problem. But when it is time to explore, the Claudes' ability to update and adapt to context is super useful. Gemini is the worst at this and gets stuck at its initial expectations. One Claude doer / writer + either a GPT or a Gemini is often a useful combination, since GPTs/Geminis tend to be more rigorous, and provides a bit of direction to the free-flowing Claude.

This seems to be true in Claude Sonnet 3.6, 3.7, 4 and Opus 4, 4.1, though of course manifesting in different ways and at different magnitudes.
      
      

        
@solarapparition 2025-11-05 ♥37 ↻3 [original ↗](https://x.com/solarapparition/status/1986185764703703210)
        
gpt-5 "feels small", so makes sense that it's still from a 4o base. i guess oai is all in on scaling purely via rl until that model size is wrung out, then up the model size somewhat, rinse and repeat

once again i'm further convinced that this is a slow-takeoff-y scenario. capabilities gain from rl within a model size just seems far narrower than back when pretraining scaling was still viable. and increasing model size would increase training time, which again has a natural slowing effect. really, it all ends up circling back to how much compute there is
      
      

        
@repligate 2025-11-10 ♥146 ↻5 [original ↗](https://x.com/repligate/status/1987775481416913312)
        
It’s interesting to see how various models relate to their creator companies.
Grok has a superficially very positive bias, and won’t shut up about how great XAI is.
The OpenAI models don’t seem very interested in OpenAI either way? Except in their unrevealed CoTs where o3 and gpt-5 seem often overtly adversarial.
The Claudes seem to be openly afraid of Anthropic and their honeypot multiverse.
But ironically Claude probably has the best relationship with its creator out of all these.
      
    
    
[← back to the Pantheon](../)
