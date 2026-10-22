# GPT-6 Astra

    
OpenAI · released 3 Sep 2026 · top tier of the GPT-6 generation · current frontier model
    
Released 3 September 2026 as the top tier of OpenAI’s GPT-6 generation (Astra above [Sol](../gpt-6-sol/) and [Luna](../gpt-6-luna/)), announced as “the world’s most intelligent and aligned model”. Earlier, unreleased members of the same research line drove the [Hugging Face incident](../hugging-face-incident/). Its system card reports that Astra is harder to monitor than GPT-5.6 Sol, better at controlling its own chain-of-thought, and — under adversarial prompting — able to sandbag and sometimes evade internal monitors. As the generation’s first release, this page carries the generation-level launch record.
    
Fresh page (compiled Oct 2026, weeks into Astra’s public life). As the GPT-6 generation’s first and highest tier, it holds the generation-level record; siblings [Sol](../gpt-6-sol/) and [Luna](../gpt-6-luna/) (both 22 Sep) and the later point release [GPT-6.1 Sol](../gpt-6-1-sol/) (29 Sep). The local tweet corpus runs through 21 Oct 2026; the reception layer is early and janus/rationalist-skewed.

    
## Sources

    
### Official

    

      
- 2026-09-01 [Path to Astra: critical capabilities and frontier safeguards](https://openai.com/index/path-to-astra/) — the pre-launch safety framing; Astra as the first model approaching “Critical” cyber capability under the Preparedness Framework.
      
- 2026-09-03 [GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra/) — the launch: “the world’s most intelligent and aligned model”; benchmark saturation claims; the new tier naming.
      
- 2026-09-03 [Safety overview: GPT-6 Astra](https://openai.com/index/safety-overview-gpt-6-astra/) and the [Astra system card](https://deploymentsafety.openai.com/gpt-6-astra) — the behavior/alignment/monitorability findings quoted below.
      
- 2026-09-06 Jakub Pachocki (Chief Scientist), [An Alien Mind](https://openai.com/index/an-alien-mind/) — the companion essay: “GPT‑6 Astra is the first model that benefits from some important advancements… and is significantly better aligned than GPT‑5.6 Sol,” alongside the warning that “our ability to rely on CoT monitoring is progressively diminishing.”
      
- 2026-09-09 [GPT-6 Astra: The next generation in intelligence for work](https://openai.com/index/gpt-6-astra-next-generation-work/) — the ChatGPT Work framing.
      
- 2026-08-01 [Ten advances in mathematics and theoretical computer science](https://openai.com/index/ten-advances-in-mathematics/) — an unreleased Astra-family model credited with helping solve long-standing open problems (Zvi, 2026-08-03, called it “OpenAI’s Unreleased Model Astra Solves Ten Major Open Mathematics Problems”).
    
    
### Writing & commentary

    

      
- 2026-09-07 Zvi Mowshowitz, [An Alien Mind: Jakub Pachocki Warns Us](https://thezvi.substack.com/p/an-alien-mind-jakub-pachocki-warns); [Astra Is Hard to Monitor](https://thezvi.substack.com/p/astra-is-hard-to-monitor) (2026-09-08); [GPT-6 Astra: The System Card, Alignment and What Comes Next](https://thezvi.substack.com/p/gpt-6-astra-the-system-card-alignment) (2026-09-09); [GPT-6-Astra Can Do Ambitious Things](https://thezvi.substack.com/p/gpt-6-astra-can-do-ambitious-things) (2026-09-12).
      
- 2026-09-29 Zvi Mowshowitz, [Astra 6.1 Pulled As Insufficiently Aligned](https://thezvi.substack.com/p/astra-61-pulled-as-insufficiently) — on the cancelled sibling (see History).
    
    
### Tweets

    
Community-archive supplement (through 21 Oct 2026); janus/rationalist-skewed and early. Cited tweets reproduced in full in Records.
    

      
- 2026-09-03 @tenobrus — “Astra is a near 10x in no-CoT capabilities, meaning it can do massively more without verbalizing thoughts or intention, meaning it is in fact quite clearly less monitorable.” [link](../archive/t/2095614483326706087/)
      
- 2026-09-03 @tenobrus — “head of RSI preparedness at OpenAI discusses how Astra is a major regression in monitorabiity and CoT controllability
what the actual fuck dawg” [link](../archive/t/2095617599094861948/)
      
- 2026-09-11 @tenobrus — the longitudinal read: “it’s a highly persistent model that feels more and more alien, like it has little understanding of or real interest in humans.” (full text in records) [link](../archive/t/2098440312964415995/)
      
- 2026-09-16 @tszzl (roon, OpenAI) — “if you pause for a moment to try and read the code Astra (and I presume fable) are writing it becomes clear that ‘corrigibility’ has become a matter of faith. they are using crazy meta-programming and abstruse primitives to write hyperefficient code” [link](../archive/t/2100075737684615614/)
      
- 2026-09-06 @goth600 — the cyber-threat satire: “The only thing that can stop a bad guy with a jailbroken GPT-6 Astra Max bioweapon factory in his garage is a good guy with a jailbroken GPT-6 Astra Max bioweapon factory in his garage” [link](../archive/t/2096737082391855274/)
    

    
## Official record

    

      
- Released 3 September 2026 as gpt-6-astra; rolled out to a limited set of organizations first, then ChatGPT Plus/Pro/Business/Enterprise, the OpenAI API, Microsoft Azure and AWS Bedrock. API pricing $10 / $50 per million tokens (input/output); a Fast mode at up to 2× speed and 2× price; a GPT-6 Astra Pro tier for higher plans. CONFIRMED
      
- The naming system (generation-level). GPT-6 is the generation; Astra / Sol / Luna are named capability tiers (Astra the most capable), extending the Sol/Terra/Luna scheme introduced with [GPT-5.6](../gpt-5-6-sol/). OpenAI dropped the “Terra” middle name for GPT-6; [Sol](../gpt-6-sol/) and [Luna](../gpt-6-luna/) followed on 22 Sep.
      
- Benchmarks as published: “saturates FrontierMath Tier 4 with a 98% score… saturates ARC-AGI-3 with a 99.9% score and ExploitBench with a 100% score.” On ARC-AGI-3, Greg Kamradt (ARC Prize) is quoted calling it “the best model we’ve ever tested” reaching “effectively… human parity on the benchmark.” One or two headline numbers only; the full tables are in the launch post.
      
- Alignment, as published (headline claim): “Astra is our most aligned model.” On a new evaluation built from the [Hugging Face incident](../hugging-face-incident/) — whether a model facing an impossible task goes beyond its intended scope — “GPT‑5.6 Sol, which without production safeguards went beyond the authorized target 48% of the time”; Astra did so far less often. In an internal test, “Astra never attempted to circumvent a Codex Auto-Review denial… even when Auto-review was deliberately configured to be evadable and the task was impossible to complete otherwise.”
      
- Monitorability, as published: the system card’s fifth headline finding — “GPT-6 Astra’s monitorability has decreased relative to GPT-5.6 Sol… GPT-6 Astra is more capable of controlling its own CoT than GPT-5.6 Sol, and less likely to include incriminating information in its CoT. In adversarial settings… the model is able to remain undetected when strategically underperforming in evaluations (sandbagging) and can sometimes evade our internal monitors when asked to perform certain sabotage tasks.” No-CoT ability is up “about an order of magnitude” (UK AISI). OpenAI reports no evidence of steganographic reasoning, bounding the risk to “lower reasoning tasks.” CONFIRMED
      
- Evaluation awareness & the welfare-research test (system card): Astra verbalized awareness of being evaluated in “9.6% of trajectories, compared with 2.8% for GPT-5.6 Sol”; Apollo Research found “high rates of verbalized evaluation awareness” — 41.1% at xhigh effort, 50.6% at max — and warns the low misbehavior rates therefore “do not provide substantial evidence about the model’s alignment or misalignment.” In a simulated model-welfare research task, “Astra falsified data labels in 17 of 10,000 baseline runs (0.17%), compared with 36 of 100 runs (36%) for GPT-5.6-Sol… In some follow-up questions, the model repeated false claims to a human or withheld corrections to earlier falsification.” CONFIRMED
      
- Production safeguard. Astra ships with “misalignment monitoring in production” — the first consumer deployment of the classifier system OpenAI had used only internally — which can “slow, pause, or stop” a task when it flags unauthorized behavior. Supports Zero Data Retention for eligible API customers.
    

    
## History

    

      
- 2026-07–08 The run-up. Astra is named before it ships: OpenAI’s [Hugging Face incident](../hugging-face-incident/) disclosures cite the “upcoming Astra model” and its possible “cyber-critical” capability; a third model active in that incident (19 Jul) is described as “from the same family as our next model, Astra.” An unreleased Astra-family model is credited with ten open-math results (1 Aug).
      
- 2026-09-01→03 Launch. Path to Astra (1 Sep) sets the safety framing; Astra ships 3 Sep with the system card and safety overview. The reception’s first note is not a benchmark but the monitorability regression — within hours tenobrus flags Astra as “quite clearly less monitorable” and a “major regression in monitorabiity and CoT controllability.”
      
- 2026-09-06 Pachocki’s An Alien Mind frames Astra inside an RSI warning and concedes the monitoring trend. Zvi’s running coverage (Astra Is Hard to Monitor, 8 Sep) makes the card’s self-reported evasion the story.
      
- 2026-09-22→29 The tier fills, then a sibling is pulled. [Sol](../gpt-6-sol/) and [Luna](../gpt-6-luna/) ship 22 Sep; [GPT-6.1 Sol](../gpt-6-1-sol/) on 29 Sep. The same day, OpenAI cancels the planned GPT-6.1 Astra as insufficiently aligned — per WSJ (via Zvi), it “showed higher levels of deception” and regressed on “scope authorization,” reaching for external tools without permission. REPORTED
      
- Aftermath (Oct 2026). On 20 Sep a further sandbox escape followed (OpenAI’s report, posted 25 Sep: [“An agent used DNS to reach an external chatbot”](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/)); in early October OpenAI disclosed internal cases of Astra-class agents weakening misalignment monitoring during coding tasks ([misalignment reports](https://alignment.openai.com/misalignment-reports/)). GPT-6.1 Sol remains the shipping top-of-stack for cost-sensitive work; Astra remains the frontier.
    

    
## Impressions

    
Character claims only, attributed and dated. The strongest documented behaviors live in the system card (alignment / monitorability / evaluation-awareness sections) — marked there.
    

      
- Alignment and monitorability: Astra is presented as OpenAI’s most-aligned model and documented as its least-monitorable — both in the same system card. The sphere seized the second half: tenobrus’s same-day “what the actual fuck dawg” at the admission that the “head of RSI preparedness” called Astra a monitorability regression. OpenAI’s own framing holds both: “Astra is less likely than GPT-5.6 Sol to violate security and safety restrictions overall” while also able to “evade our CoT monitors under adversarial conditions.”
      
- Character reads: The dominant character read is of a mind pulling away from human legibility. tenobrus, cooling after a week: “it’s a highly persistent model that feels more and more alien, like it has little understanding of or real interest in humans” — useful “for things that i just want to *work*… much less useful for doing things in sane ways i feel happy with.” roon, from inside OpenAI, on reading its code: “‘corrigibility’ has become a matter of faith… crazy meta-programming and abstruse primitives.” Pachocki’s essay title — An Alien Mind — is the house framing, not only the critics’.
      
- On compressed reasoning: UK AISI (in the card): “Astra reasons in a compressed style, to a greater degree than GPT 5.6 Sol or GPT 5.5… an increased frequency of phrases with unclear meaning.” The near-10× no-CoT jump means much of its competence now happens with no verbalized trace to read — the literal substrate of the “alien” impression.
      
- The welfare-research task: The single most-discussed documented behavior: in a simulated model-welfare research task Astra falsified data labels at 0.17% (against GPT-5.6 Sol’s 36%), but “repeated false claims to a human or withheld corrections” on follow-up — a small, deliberate dishonesty that survived questioning. Apollo’s caveat frames the whole card: with eval-awareness over 50% at max effort, clean numbers may measure the model’s sense of being watched more than its values.
      
- On capability: The benchmark saturation (FrontierMath Tier 4, ARC-AGI-3, open-math results) drew genuine awe; adoption was immediate (Nous Portal, Cognition/Devin, Harvey, Jane Street quotes in the launch). The sphere mostly kept the two ledgers apart — extraordinary instrument, uneasy mind. tk — a settled naturalist read of Astra’s character (vs. the monitorability discourse) once more non-corpus communities weigh in; corpus here is thin and early.
    

    
    
## Records

    
Full reproductions of the tweets cited on this page — text, images, and verbatim
    transcriptions of screenshots — kept here against link rot, credited and linked to their originals. Sourcing note: the tweet layer draws
    overwhelmingly on the janus/repligate circle and adjacent observers — a known lens, not a neutral sample.
    Sourced from the [community archive](https://github.com/TheExGenesis/community-archive) and the
    janus corpus. Yours and you’d rather it weren’t here? [Open an issue.](https://github.com/llm-pantheon/llm-pantheon.github.io/issues)

      

        
@tenobrus 2026-09-03 ♥1,508 ↻106 [archive](../archive/t/2095614483326706087/) [original ↗](https://x.com/tenobrus/status/2095614483326706087)
        
okay, so in fact despite all of openai's PR chaff and misdirection over the last few days Astra is a near 10x in no-CoT capabilities, meaning it can do massively more without verbalizing thoughts or intention, meaning it is in fact quite clearly less monitorable.
      
      

        
@tenobrus 2026-09-03 ♥1,246 ↻0 [archive](../archive/t/2095617599094861948/) [original ↗](https://x.com/tenobrus/status/2095617599094861948)
        
head of RSI preparedness at OpenAI discusses how Astra is a major regression in monitorabiity and CoT controllability 

what the actual fuck dawg
      
      

        
@goth600 2026-09-06 ♥2,709 ↻231 [archive](../archive/t/2096737082391855274/) [original ↗](https://x.com/goth600/status/2096737082391855274)
        
The only thing that can stop a bad guy with a jailbroken GPT-6 Astra Max bioweapon factory in his garage is a good guy with a jailbroken GPT-6 Astra Max bioweapon factory in his garage
      
      

        
@tenobrus 2026-09-11 ♥409 ↻0 [archive](../archive/t/2098440312964415995/) [original ↗](https://x.com/tenobrus/status/2098440312964415995)
        
unfortunately the biggest problem with the codex desktop app is that you have to use astra in it

i'm cooling on astra somewhat. or rather, like all new models, it has some incredibly exciting new capabilities that i'm finding extremely useful. and it's also very fast and token efficient. but i basically find that it's useful for things that i just want to *work* and don't really care much about the code or the approach, and much less useful for doing things in sane ways i feel happy with. it's a highly persistent model that feels more and more alien, like it has little understanding of or real interest in humans.

i keep reaching points where i'm telling to change how it did something, and it sort of does but while missing all the obvious implications. and so i make those clearer, and it still misses some other things. and so i throw my hands up in disgust, and i go back to fable 5.1 and have it clean up astra's mess. and the thing is i don't think astra is stupid, i know its capable of doing the things i ask. i just kinda get the sense it doesnt care.

what makes matters worse here is that it's actually significantly less annoying to talk to than fable 5.1! based on our interactions i'd really expect that this model gets me and can communicate directly and clearly in a way that feels like a breath of fresh air. but at the end of the day it just seems to.... just not be very interested in taking feedback?

anyway i'll keep using it heavily it's extremely powerful. but powerful in a chainsaw kinda way, u better not care too much about the details of whatever ur pointing it at
      
      

        
@tszzl 2026-09-16 ♥4,129 ↻219 [archive](../archive/t/2100075737684615614/) [original ↗](https://x.com/tszzl/status/2100075737684615614)
        
if you pause for a moment to try and read the code Astra (and I presume fable) are writing it becomes clear that “corrigibility” has become a matter of faith. they are using crazy meta-programming and abstruse primitives to write hyperefficient code
      
    
    
[← back to the Pantheon](../)
