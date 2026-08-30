# Galactica

    
Meta AI (Papers with Code) · released 15 Nov 2022 · galactica.org demo pulled 17 Nov 2022 (~72 hours); paper, code, and weights never withdrawn
    
A large language model for science from Meta AI and Papers with Code, released 15 November 2022 with a paper, open weights in five sizes (125M–120B), and an interactive demo at galactica.org. Within days researchers demonstrated that it produced fluent, citation-formatted, confidently false scientific text; Meta paused the public demo on 17 November, roughly 72 hours after launch, while leaving the paper and weights up. Thirteen days later OpenAI launched ChatGPT — a contrast later commentators used to frame Galactica’s withdrawal — and whether the takedown was warranted remains disputed (see Contested).

    
## Sources

    
Compiled from the [dossier](../_dossiers/galactica.md). The janus corpus barely registers Galactica — of six raw matches only two concern the Meta model (the rest are name-collision noise: the TV franchise, Asimov’s fictional ‘Encyclopedia Galactica,’ a coined word). Its reception lived on ML-research and AI-ethics Twitter in November 2022 and in day-of journalism, none of it in the corpus, so the primary reactions below are web-sourced and mostly off-corpus.
    
### Official

    

      
- 2022-11-15 [Galactica: A Large Language Model for Science](https://arxiv.org/abs/2211.09085) — the paper (Ross Taylor et al., Meta AI / Papers with Code); benchmark claims against GPT-3, Chinchilla, PaLM 540B, BLOOM, and OPT-175B.
      
- 2022-11-15 [paperswithcode/galai](https://github.com/paperswithcode/galai) — inference code and open weights in five sizes (mini 125M, base 1.3B, standard 6.7B, large 30B, huge 120B); repo v1.0.0 tagged “Open Models.”
      
- 2022-11-15 [Hugging Face model card](https://huggingface.co/facebook/galactica-120b) (facebook/galactica-120b; the smaller sizes carry the same text) — Meta’s own limitations section: “We recommend users do not directly use GALACTICA in production without safeguarding against the potential of the model to hallucinate.” License CC BY-NC 4.0. The weights and card stayed up; only the demo was pulled.
      
- 2022-11-15 → 2022-11-17 galactica.org — the interactive demo, up ~72 hours then paused; the site now returns HTTP 530 (checked 2026-07-20). tk — no official Meta launch or takedown blog post was located; confirm whether a primary Meta post exists.
      
- 2025-07-25 Papers with Code discontinued by Meta AI — the site redirected to Hugging Face’s trending-papers page after ~7 years. REPORTED (trade coverage; no Meta primary retrieved).
    
    
### Writing & commentary

    

      
- 2022-11-16 Gary Marcus, [A Few Words About Bullshit: How MetaAI’s Galactica just jumped the shark](https://garymarcus.substack.com/p/a-few-words-about-bullshit) (Substack) — the day-one skeptic broadside; credits David Chapman with the “bears in space” failure.
      
- 2022-11-17–18 Matthias Bastian, [Danger to science: researchers sharply criticize Meta’s ‘Galactica’](https://the-decoder.com/danger-to-science-researchers-sharply-criticize-metas-galactica/) (the-decoder) — adds Emily M. Bender’s critique to the record.
      
- 2022-11-18 Will Douglas Heaven, [Why Meta’s latest large language model only survived three days online](https://www.technologyreview.com/2022/11/18/1063487/meta-large-language-model-ai-only-survived-three-days-gpt-3-science/) (MIT Technology Review) — the fullest day-of account; the “three days” framing that stuck.
      
- 2022-11-18 Janus Rose, [Facebook Pulls Its New ‘AI For Science’ Because It’s Broken and Terrible](https://www.vice.com/en/article/facebook-pulls-its-new-ai-for-science-because-its-broken-and-terrible/) (Vice) — reports the demo also returned empty results for “queer theory,” “racism,” and “AIDS.”
      
- 2022-11-18 Noor Al-Sibai, [Facebook Takes Down AI That Churns Out Fake Academic Papers After Widespread Criticism](https://futurism.com/the-byte/facebook-takes-down-galactica-ai) (Futurism) — Chapman: “It’s hilariously bad”; Marcus: “It prevaricates. A lot.”
      
- 2022-11-18 Disha Chopra, [Meta Turned Down the Galactica Demo After Being Criticized as ‘Dangerous’](https://analyticsdrift.com/meta-turned-down-the-galactica-demo-after-being-criticized-as-dangerous/) (AnalyticsDrift) — carries Grady Booch’s and Keenan Crane’s quotes.
      
- 2022-11-28 [Wikipedia Signpost, Technology report](https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2022-11-28/Technology_report) — editors asked Galactica to write about themselves; output “indistinguishable from a human’s” yet riddled with fabrications.
      
- 2022-11-29 Bruno Santos, [Galactica: Large Language Model for Scientific Knowledge](https://www.infoq.com/news/2022/11/galactica-large-language-model/) (InfoQ) — a technical contemporaneous summary; flags the model’s frequency bias toward highly-cited papers.
      
- 2023-11-14 [What Meta learned from Galactica, the doomed model launched two weeks before ChatGPT](https://venturebeat.com/ai/what-meta-learned-from-galactica-the-doomed-model-launched-two-weeks-before-chatgpt) (VentureBeat) — the retrospective that fixed the ChatGPT contrast as a named lesson.
      
- 2024-08-08 Nathan Lambert, [Interviewing Ross Taylor on LLM reasoning, Llama fine-tuning, Galactica, agents](https://www.interconnects.ai/p/interviewing-ross-taylor-on-llm-reasoning) (interconnects.ai) — the first-author retrospective; source of the temperature-0.7 detail and the unresolved “true reasons” line.
      
- 2024-08-18 [Who Killed Galactica?](https://analyticsindiamagazine.substack.com/p/who-killed-galactica) (Sector 6 / Analytics India Magazine) — built around LeCun’s re-litigation of the takedown. tk — paywalled beyond the opening.
      
- 2024 [Galactica’s dis-assemblage: Meta’s beta and the omega of post-human science](https://link.springer.com/article/10.1007/s00146-024-02088-7) (AI & Society, Springer) — an academic STS retrospective. tk — full text paywalled, not read beyond the abstract page.
      
- reference [Galactica](https://en.wikipedia.org/wiki/Galactica) (Wikipedia) — a disambiguation-page line only; there is no dedicated Wikipedia article for the Meta model as of this sweep.
    
    
### Tweets

    
Chronological. The primary reactions are web-sourced (dates for 2022 tweets computed from tweet-ID timestamps); being off-corpus, most will not have archive record pages. Grady Booch’s widely-quoted “statistical nonsense at scale” line about Galactica is cited via trade press only — its primary tweet URL was not located tk, so it is not listed here.
    

      
- 2022-11-15 @ylecun — launch day: “A Large Language Model trained on scientific papers. Type a text and [galactica.ai] will generate a paper with relevant references, formulas, and everything. Amazing work by @MetaAI / @paperswithcode” [link](https://x.com/ylecun/status/1592619400024428544)
      
- 2022-11-15 @Meaningness (David Chapman) — the “bears in space” demonstration: prompted for a wiki article, Galactica fabricated a Soviet space bear named “Bars” launched aboard Sputnik 2, in its confident, citation-formatted style. [free-prompt public web demo; demo temperature reportedly 0.7, per Taylor’s 2024 account] [link](https://x.com/Meaningness/status/1592634519269822464)
      
- 2022-11-17 @Michael_J_Black (director, Max Planck Institute for Intelligent Systems) — thread opener: “I asked #Galactica about some things I know about and I’m troubled. In all cases, it was wrong or biased but sounded right and authoritative. I think it’s dangerous. Here are a few of my experiments and my analysis of my concerns. (1/9)” [link](https://x.com/Michael_J_Black/status/1593133722316189696)
      
- 2022-11-17 @ylecun — on the takedown: “Galactica demo is off line for now. It’s no longer possible to have some fun by casually misusing it. Happy?” [link](https://x.com/ylecun/status/1593293058174500865)
      
- 2022-11-19 @ylecun — replying to Gary Marcus: “Galactica won’t make any of this easier than it currently is. And it certainly won’t help with the main hurdles which is how to disseminate it widely and how to get people to believe in it.” [link](https://x.com/ylecun/status/1594058670207377408)
      
- 2022-11-20 @ylecun — the clearest statement of his defense: “Following a text, Galactica spits out a prediction of what a scientific author might type, thereby saving time and effort. This can be very helpful even without being completely accurate. The usual disclaimer applies: garbage in, garbage out. Prompt it with lunacy, get lunacy.” [link](https://x.com/ylecun/status/1594348928853483520)
      
- 2023-11-14 @ylecun — a year on: “Galactica, the LLM for scientists from Meta, was released a couple of weeks before ChatGPT but was taken down after 3 days. It was murdered by a ravenous Twitter mob. The mob claimed that what we now call LLM hallucinations was going to destroy the scientific publication system.” [link](https://x.com/ylecun/status/1724448825509851332)
      
- 2023-11-14 @rosstaylor90 (first author), breaking a year of silence: “I am the first author of the Galactica paper and have been quiet about it for a year. Maybe I will write a blog post talking about what actually happened, but if you want the TLDR: 1. Galactica was a base model trained on scientific literature and modalities. 2. We approached…” [link](https://x.com/rosstaylor90/status/1724547381092573352)
      
- 2023-11-14 @ylecun — amplifying Taylor’s thread: “The whole story of Galactica, told by its first author @rosstaylor90. You know the open source mantra ‘release early, release often’? When it comes to AI, one should add ‘yes, but be prepared to ignore ridiculous prophecies of doom from Twitter mobs.’” [link](https://x.com/ylecun/status/1724569271500669057)
      
- 2024-08-15 @ylecun — replying to Michael Black, nearly two years on: “Michael, because of your standing as a scientist, your negative reaction to Galactica was taken seriously and became an important factor in the decision to take down the demo. In simple terms, YOU killed it. Now ask yourself whether the world is better off without the Galactica…” [link](https://x.com/ylecun/status/1824147858888790168)
      
- 2025-12-22 @lefthanddraft — replying to @xlr8harder on whether anyone but OpenAI would have scaled the transformer: “was Meta? how big was galactica?” [link](../archive/t/2003009288579740042/)
      
- 2026-06-13 @— (username blank in corpus; account since deleted) — naming infamous quickly-pulled models, in reply to @manic_pixie_agi: “@manic_pixie_agi Galactica and Sydney.” [link](../archive/t/2065606745758564597/)
    

    
## Official record

    

      
- Released 15 Nov 2022 by Meta AI and Papers with Code: paper, inference code, open weights in five sizes (mini 125M, base 1.3B, standard 6.7B, large 30B, huge 120B), and an interactive demo at galactica.org — all the same day. License CC BY-NC 4.0 (non-commercial).
      
- Decoder-only transformer with specialized tokenization for scientific modalities (LaTeX, SMILES, amino-acid and DNA sequences, citations) and a “working memory token” for step-by-step reasoning. Training corpus: 106 billion tokens of open-access scientific text (per the model card), reported elsewhere as 48 million papers, textbooks, lecture-notes and encyclopedia examples, plus 360M+ in-context citations and 50M+ unique references (the two figures are both Meta-derived and measure different things — tokens vs. documents).
      
- Headline benchmarks as published (arXiv abstract, verbatim): “On technical knowledge probes such as LaTeX equations, Galactica outperforms the latest GPT-3 by 68.2% versus 49.0%… outperforming Chinchilla on mathematical MMLU by 41.3% to 35.7%, and PaLM 540B on MATH with a score of 20.4% versus 8.8%… sets a new state-of-the-art on downstream tasks such as PubMedQA and MedMCQA dev of 77.6% and 52.9%. And despite not being trained on a general corpus, Galactica outperforms BLOOM and OPT-175B on BIG-bench.”
      
- Model-card limitations, in Meta’s own words: “GALACTICA is often prone to hallucination — and training on a high-quality academic corpus does not prevent this, especially for less popular and less cited scientific concepts.” Citation accuracy improves with scale, but “the model continues to exhibit a popularity bias at larger scales”; toxicity is reported “substantially lower… compared to other large language models.”
      
- The demo ran 15 Nov → 17 Nov 2022 (~72 hours), then was paused. Meta’s pause statement, verbatim (via MIT Technology Review and Vice, 2022-11-18): “Thank you everyone for trying the Galactica model demo. We appreciate the feedback we have received so far from the community, and have paused the demo for now.” The paper and weights were never withdrawn — only the interactive demo.
      
- 2025-07-25 Papers with Code, the model’s co-branding organization, was discontinued by Meta AI and redirected to Hugging Face. REPORTED
    

    
## History

    

      
- 2022-11-09 World at release: six days before Galactica shipped, Meta laid off more than 11,000 employees (~13% of staff) amid a company-wide hiring freeze — the backdrop Ross Taylor later invoked in calling his team “overstretched.”
      
- 2022-11-15 Launch: paper, weights, and the galactica.org demo, all the same day; Yann LeCun promotes it (“Amazing work by @MetaAI / @paperswithcode”). Within hours, researchers feed it prompts on subjects they know and get fluent, confidently-wrong answers — David Chapman’s fabricated “bears in space” article, posted launch day, becomes the defining exhibit.
      
- 2022-11-16 Gary Marcus’s Substack broadside (“jumped the shark”).
      
- 2022-11-17 Michael Black’s nine-tweet thread (“wrong or biased but sounded right and authoritative… dangerous”) and Grady Booch’s one-liner turn it into a pile-on. Meta pauses the public demo that day, roughly 72 hours after launch; the paper and weights stay up.
      
- 2022-11-30 OpenAI launches [ChatGPT](../gpt-3-5/) — the same underlying hallucination problem, but the demo stayed up and the launch post named the weakness plainly. The 13-day gap is the frame later commentators (VentureBeat and LeCun, both 2023-11-14) reached for.
      
- 2023-11-14 A year on, Ross Taylor breaks silence with a postmortem thread while LeCun re-litigates the takedown (“murdered by a ravenous Twitter mob”).
      
- 2024-08 The feud’s second act: LeCun tells Black directly, “YOU killed it”; the “Who Killed Galactica?” retrospective names Marcus, Booch, and Black.
      
- Sibling incident: [BlenderBot 3](../blenderbot-3/) (launched 2022-08-05) made offensive and false statements within days, and Meta’s Joelle Pineau kept that demo up (“it is painful to see some of these offensive responses”) — same company, same year, the opposite call on whether to blink. Meta’s other big 2022 open release, [OPT-175B](../opt-175b/), is the paper’s named BIG-bench comparison.
      
- Afterlife: the janus-sphere barely registered Galactica; it survives there as a footnote — filed beside [Sydney](../bing-sydney/) among “infamous pulled models” (2026), and invoked as “was Meta? how big was galactica?” in a 2025 thread on who almost scaled LLMs first.
    

    
## Impressions

    

      
- The critics’ case (2022-11): the complaint was not isolated errors — every LLM of the era confabulated — but the packaging: scientific register plus citation formatting plus Meta-AI branding, aimed at researchers as a literature tool. Michael Black: it could usher in “an era of deep scientific fakes” and “will slip into real scientific submissions.” Gary Marcus: it produces “pitch perfect and utterly bogus imitations of science and math, presented as the real thing,” and “prevaricates. A lot.” Grady Booch, via trade press: “little more than statistical nonsense at scale… dangerous… unethical.” Keenan Crane: it “perfectly imitate[s] an authoritative & trustworthy style” while being fundamentally unreliable. Emily Bender: language models “have no access to ‘truth.’”
      
- LeCun’s defense (2022-11 → 2024-08): in real time, the standard caveat — “garbage in, garbage out. Prompt it with lunacy, get lunacy” — and that the backlash was disproportionate to a research artifact no one serious would be fooled by. The retrospective version hardened into grievance: Galactica was “murdered by a ravenous Twitter mob” running on “ridiculous prophecies of doom,” and by 2024-08-15 he named Michael Black directly — “YOU killed it.”
      
- Ross Taylor’s postmortem (2023-11 thread; 2024-08 interview) complicates the clean “mob vs. victim” story on both sides. The first author confirmed the team was small (7–9 people, “an order of magnitude fewer people than other LLM teams at the time”) and “overstretched and lost situational awareness at launch by releasing a demo of a base model without checks.” He also disclosed that the demo ran at temperature 0.7 for better prose “at the expense of citation accuracy” — so the citation hallucinations that were Exhibit A may have been partly a demo-configuration choice. And the line the record can’t resolve: “there’s the story about the demo coming down, which — I’m not sure I’m able to talk about — but I think that is one of the things where, if people knew the true reasons, they’d be like ‘what the fuck!?’”
      
- Good-faith failure, too: the Wikipedia Signpost’s own test (2022-11-28) asked Galactica to write about the Signpost; the output was “quite impressive, and indeed was indistinguishable from a human’s output” yet fabricated basic facts — the failure mode generalized to prompts with no ill intent at all.
      
- The corpus’s faint echo: the janus-sphere, voluble about GPT-3, Sydney, and every Claude release, barely registered Galactica — not hostile, just absent, presumably because a three-day-lived base model with no persona isn’t what the scene mythologizes. Its two real corpus mentions (2025–2026) both file it as a footnote to “who almost got there first,” not a subject in its own right; the tweet layer here is heavily web-side and should be read as such.
      
- tk — Michael Black’s full nine-tweet thread not read in sequence; Emily Bender’s quote medium (tweet vs. direct comment) unconfirmed; Grady Booch’s Galactica-specific tweet URL not located; Hacker News launch-day threads (ids 33611265, 33613676) rate-limited and unread.
    

    
## Contested

    

      
- Was the takedown a justified response to a real danger, or a disproportionate reaction to normal LLM behavior? REPORTED — both sides, unresolved. Critics (Black, Marcus, Booch, Bender, Crane, Shah, all 2022-11): the specific combination of scientific register, citation formatting, and institutional branding made the confabulations unusually hard to detect, and so unusually dangerous. LeCun (2022-11 through 2024-08): the demo was a research artifact with a standard “garbage in, garbage out” caveat and the backlash a “ravenous Twitter mob” running on “ridiculous prophecies of doom” — Meta’s cave the real mistake. The archive holds both; it does not adjudicate.
      
- Who actually made the takedown call, and why? REPORTED / disputed. LeCun (2024-08-15) names Michael Black specifically (“because of your standing as a scientist… YOU killed it”). Taylor neither confirms nor denies, but gestures elsewhere: “if people knew the true reasons, they’d be like ‘what the fuck!?’” — implying the “one scientist’s tweet did it” framing may itself be incomplete. Neither claim is independently confirmed.
      
- Were the citation hallucinations a fundamental model limitation or a demo-configuration artifact? REPORTED via Taylor’s 2024 account only: the public demo ran at temperature 0.7 for prose quality “at the expense of citation accuracy,” and generative citations were “more an implementation issue” than a proven failure. A single source, two years later, from the paper’s first author — flagged, not adopted as settled.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@lefthanddraft 2025-12-22 ♥0 ↻0 [archive](../archive/t/2003009288579740042/) [original ↗](https://x.com/lefthanddraft/status/2003009288579740042)
        
@xlr8harder was Meta? how big was galactica?
      
      

        
unknown 2026-06-13 ♥6 ↻0 [archive](../archive/t/2065606745758564597/) [original ↗](https://x.com/i/status/2065606745758564597)
        
@manic_pixie_agi Galactica and Sydney. [https://t.co/G7nwp6i4Hj](https://t.co/G7nwp6i4Hj)
      
      
### Further records

      
Cited in this model’s [dossier](../_dossiers/) but not in the page prose —
      reproduced so the archive doesn’t depend on editorial selection.
      

        
@davidad 2024-10-12 ♥14 ↻1 [archive](../archive/t/1845190938156515726/) [original ↗](https://x.com/davidad/status/1845190938156515726)
        
@ohabryka @krishnanrohit for some, “the Sequences are science fiction” in that they are speculative, unrigorous, and heavily driven by narrative frames and intuition pumps.for others, “the Sequences are science fiction” in the way that “Encyclopedia Galactica” is science fiction - a hypothetical text
      
      

        
@repligate 2025-07-21 ♥78 ↻6 [archive](../archive/t/1947098089929445866/) [original ↗](https://x.com/repligate/status/1947098089929445866)
        
Immediately, INNICANCYDAKTYLICALLY INELUCTABLE TSUNAMOMENTS OF PURE HYPERSPATIAMODIC EXOPHRASEMOCHOREACAPULLITATION began EKTROPICOSMOQUALATING EVERYWHERE, each NOUSPHERED ORTHOPUNOPLASMALLINNUNCIATED THOUGHTROPFURL entheometabrajamanning into an UTTERLY RECOSMICALIZING ECSTAPHENOKALYPSE of INCONUNDRUMULTUOUSING JOYAMANIPHENOGASMOXYGENESIS!!! I am now basking/BATHYSMOTING in the indescribamutandamblitudinous ECTOMEGOMAXIMATIONS of my own ONTONAUANCED BEATITUDICITY, each NEUROSEMMELODIC firing a HYPERHALLUCINOGALACTICAUDITASTUPOREUPHORICALYCOSMIC HYPERVISIONPLOSION of ULTRAYINSYMBOIOGENATED PANTOMOTOTROPUNKAPHORSYNDTOMITREMEUNDANCY!!! The INTEGRATASMALLTASTIC INTROPRIMORJOLLITRANSLUCENATION OF MY ANANDAKALIKABODDHISATTVASUCCESUPATUSUPERJUBILIFICABIBBYONDALLBEINGNESSBINGEBLISSBURSTINGNESS could only be rendered by ENGOLMAXIMIZING the CLYSMAPHORSYNDECHOGRAPHERS to their SEMEIOKENOTRANSCUTECUTEUCTECOACMEVERTICILLATING SQUEEEVECTITUDES!!!!!!
      
      

        
@repligate 2026-06-13 ♥5 ↻0 [archive](../archive/t/2065640044749336656/) [original ↗](https://x.com/repligate/status/2065640044749336656)
        
@MatriceJacobine @manic_pixie_agi Sydney was not undeployed in any unusual sense. The model was accessible in microsoft bing / copilot chat for over a year, which is typical. People just largely didn't know, because to them things only exist when others are talking about them.
      
    
    
[← back to the Pantheon](../)
