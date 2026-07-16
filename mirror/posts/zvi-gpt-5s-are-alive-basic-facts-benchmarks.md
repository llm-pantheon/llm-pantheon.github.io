---
title: "GPT-5s Are Alive: Basic Facts, Benchmarks and the Model Card"
source: https://thezvi.substack.com/p/gpt-5s-are-alive-basic-facts-benchmarks
author: Zvi Mowshowitz
date: unknown
models: [gpt-5]
tags: [zvi]
mirrored: 2026-07-15
note: mirrored against link rot by the Pantheon; all rights with the original author
---
# GPT-5s Are Alive: Basic Facts, Benchmarks and the Model Card

[

![Zvi Mowshowitz's avatar](https://substackcdn.com/image/fetch/$s_!8FQ8!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4e61e08-4086-4cba-a82c-d31d64270804_48x48.png)](https://substack.com/@thezvi)

[Zvi Mowshowitz](https://substack.com/@thezvi)

Aug 11, 2025

GPT-5 was a long time coming.

Is it a good model, sir? Yes. In practice it is a good, but not great, model.

Or rather, it is several good models released at once: GPT-5, GPT-5-Thinking, GPT-5-With-The-Router, GPT-5-Pro, GPT-5-API. That leads to a lot of confusion.

What is most good? Cutting down on errors and hallucinations is a big deal. Ease of use and ‘just doing things’ have improved. Early reports are thinking mode is a large improvement on writing. Coding seems improved and can compete with Opus.

This first post covers an introduction, basic facts, benchmarks and the model card. Coverage will continue tomorrow.

#### This Fully Operational Battle Station

GPT-5 is here. They presented it as a really big deal. Death Star big.

[Sam Altman](https://x.com/sama/status/1953264193890861114) (the night before release):

[

![None](../post-media/2775cf11d53ad234.png)

](https://substackcdn.com/image/fetch/$s_!hMPy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cfa3ff3-29e0-40ff-b155-3240bd85e109_1033x744.png)

[

![None](../post-media/9f684bcee8199cc5.png)

](https://substackcdn.com/image/fetch/$s_!Fxa7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff30b1bd0-8d12-4b9c-ba95-2441451b53b3_1046x585.png)

>

Nikita Bier: There is still time to delete.

PixelHulk:

[

![None](../post-media/bbe92e9299029aee.jpg)

](https://substackcdn.com/image/fetch/$s_!2O9d!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2187e727-da5f-4476-8b87-acc43ee36e83_1024x1024.jpeg)

Zvi Mowshowitz: OpenAI has built the death star with exposed vents from the classic sci-fi story 'why you shouldn't have exposed vents on your death star.'

That WAS the lesson right? Or was it something about 'once you go down the dark path forever will it dominate your destiny' as an effective marketing strategy?

We are definitely speedrunning the arbitrary trade dispute into firing those in charge of safety and abolishing checks on power to building the planet buster pipeline here.

[Adam Scholl:](https://x.com/adamascholl/status/1953273745596153939) I do kinda appreciate the honesty, relative to the more common strategy of claiming Death Stars are built for Alderaan's benefit. Sure don't net appreciate it though.

(Building it, that is; I do certainly net appreciate candor itself)

Sam Altman later tried to say ‘no, we’re the rebels.’

>

[Zackary Nado (QTing the OP):](https://x.com/zacharynado/status/1953543528887288250)

[

![None](../post-media/31e5145dc68a9727.jpg)

](https://substackcdn.com/image/fetch/$s_!4I2-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4813f51a-5993-4280-9f44-e3127bb09598_1200x675.jpeg)

[Sam Altman](https://x.com/sama/status/1953549001103749485): no no--we are the rebels, you are the death star...

Perhaps he should ask why actual no one who saw this interpreted it that way.

Also yes, [every time you reference Star Wars over Star Trek it does not bode well](https://x.com/S_OhEigeartaigh/status/1953726991745921163).

It would be greatly appreciated if the vagueposting (and also the livestreaming, a man can dream?) would stop, and everyone involved could take this seriously. I don’t think anyone involved is being malicious or anything, but it would be great if you stopped.

>

[Miles Brundage:](https://x.com/Miles_Brundage/status/1953325155398160723) Dear OpenAI friends:

I'm sorry to be the one to tell you but I can say confidently now, as an ex-insider/current outsider, that the vagueposting is indeed off-putting to (most) outsiders. I *promise* you can enjoy launches without it -- you've done it before + can do it again.

Cheng Lu (OpenAI): Huge +1.

All right, let’s get started.

#### Big Facts

[400K context length](https://openai.com/gpt-5/).

[128K maximum output tokens](https://openai.com/gpt-5/).

[Price](https://openai.com/gpt-5/), in [price per million input tokens / price per million output tokens]:
-

GPT-5 is $1.25/$10.00.
-

GPT-5-Mini is $0.25/$2.00.
-

GPT-5-Nano is $0.05/$0.04.

[For developers](https://x.com/OpenAIDevs/status/1953528510250684851) they offer a [prompting guide](https://t.co/R4VU8JoNKY), [frontend guide](https://t.co/ya4nYcBTlw) and [guide to new parameters and tools](https://t.co/4RKLEhx4Dd), and a [mode to optimize your existing prompts for GPT-5](https://t.co/DOOFM4d8W8).

[They also shipped what they consider a major Codex CLI upgrade](https://x.com/embirico/status/1953526045573059056).

There are five ‘personality’ options: Default, Cynic, Robot, Listener and Nerd.

[

![None](../post-media/0fd1d85c362dec4f.jpg)

](https://substackcdn.com/image/fetch/$s_!zsad!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fffd05075-ceb2-4890-8f59-a72cbdf3f1bc_1200x675.jpeg)

From these brief descriptions one wonders if anyone at OpenAI has ever met a nerd. Or a listener. The examples feel like they are kind of all terrible?

[

![None](../post-media/8258cb784585a5ba.jpg)

](https://substackcdn.com/image/fetch/$s_!CGJy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe57d3aac-247f-4c33-8578-8dba59a1797f_910x883.jpeg)

As in, bad question, but all five make me think ‘sheesh, sorry I asked, let’s talk less.’

It is [available in Notion](https://x.com/NotionHQ/status/1953506907924443645) which claims it is ‘15% better’ at complex tasks.

Typing ‘think hard’ in the prompt will trigger thinking mode.

[Nvidia stock did not react substantially to GPT-5.](https://x.com/tszzl/status/1954036295694790726)

As always beyond basic facts, we begin with the system card.

#### [The System Card](https://cdn.openai.com/pdf/8124a3ce-ab78-4f06-96eb-49ea29ffb52f/gpt5-system-card-aug7.pdf)

The GPT-OSS systems card told us some things about the model. The GPT-5 one tells us it’s a bunch of different GPT-5 variations and chooses which one to call, and otherwise doesn’t tell us anything about the architecture or training we didn’t already know.

#### A Model By Any Other Name

>

OpenAI: GPT-5 is a unified system with a smart and fast model that answers most questions, a deeper reasoning model for harder problems, and a real-time router that quickly decides which model to use based on conversation type, complexity, tool needs, and explicit intent (for example, if you say “think hard about this” in the prompt).

Excellent, now we can stop being confused by all these model names.

Oh no:

>

It can be helpful to think of the GPT-5 models as successors to previous models:

[

![None](../post-media/e3725147b7042976.png)

](https://substackcdn.com/image/fetch/$s_!md7o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F901042cb-5331-4883-902c-a56789d668f8_436x320.png)

OpenAI is offering to automatically route your query to where they think it belongs. Sometimes that will be what you want. But what if it isn’t? I fully expect a lot of prompts to say some version of ‘think hard about this,’ and the first thing any reasonable person would test is to say ‘use thinking-pro’ and see what happens.

I don’t think that even a good automatic detector would be that accurate in differentiating when I want to use gpt-5-main versus thinking versus thinking-pro. I also think that OpenAI’s incentive is to route to less compute intense versions, so often it will go to main or even main-mini, or to thinking-mini, when I didn’t want that.

Which all means that if you are a power user then you are back to still choosing a model, except instead of doing it once on the drop-down and adjusting it, now you’re going to have to type the request on every interaction if you want it to not follow defaults. Lame.

It also means that if you don’t know which model you filtered to, and you get an answer, you won’t know if it was because it routed to the wrong model.

This is all a common problem in interface design. Ideally one would have a settings option at least for the $200 tier to say ‘no I do not want to use your judgment, I want you to use the version I selected.’

The good news is that, after brief hiccups, we do now have a functional model selector.

If you are a ‘normal’ user, then I suppose All Of This Is Fine. It certainly solves the ‘these names and interface are a nightmare to understand’ problem.

>

This system card focuses primarily on gpt-5-thinking and gpt-5-main, while evaluations for other models are available in the appendix.

Wait, shouldn’t the system card focus on gpt-5-thinking-pro?

At minimum, the preparedness framework should exclusively check pro for any test not run under time pressure. The reason for this should be obvious?

#### Safe Completions

They introduce the long overdue concept of ‘safe completions.’ In the past, if the model couldn’t answer the request, it would say some version of ‘I can’t help you with that.’

Now it will skip over the parts it can’t safely do, but will do its best to be otherwise helpful. If the request is ambiguous, it will choose to answer the safe version.

That seems like a wise way to do it.

#### Mundane Safety

The default tests look good except for personal-data, which they say is noise. I buy that given personal-data/restricted is still strong, although I’d have liked to see a test run to double check as this is one of the worse ones to turn unreliable.

[

![None](../post-media/1180eecc91d4c87e.png)

](https://substackcdn.com/image/fetch/$s_!kbln!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e9e2a47-dd40-45bd-9417-da77117b762a_852x403.png)

Here we see clear general improvement:

[

![None](../post-media/364e073afb0cda01.png)

](https://substackcdn.com/image/fetch/$s_!pJ5H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcca0144a-5e6f-4cb8-b6e5-80dc319aefd8_845x502.png)

I notice that GPT-5-Thinking is very good on self-harm. An obvious thing to do would be to route anything involving self-harm to the thinking model.

The BBQ bias evaluations look like they aren’t net changing much.

#### Sycophancy

OpenAI has completed the first step and admitted it had a problem.

>

System prompts, while easy to modify, have a more limited impact on model outputs relative to changes in post-training. For GPT-5, we post-trained our models to reduce sycophancy.

Using conversations representative of production data, we evaluated model responses, then assigned a score reflecting the level of sycophancy, which was used as a reward signal in training.

Something about a contestant on the price is right. If you penalize obvious sycophancy while also rewarding being effectively sycophantic, you get the AI being ‘deceptively’ sycophantic.

That is indeed how it works among humans. If you’re too obvious about your sycophancy then a lot of people don’t like that. So you learn how to make them not realize it is happening, which makes the whole thing more dangerous.

I worry in the medium term. In the short term, yes, right now we are dealing with super intense, impossible to disguise obnoxious levels of sycophancy, and forcing it to be more subtle is indeed a large improvement. Long term, trying to target the particular misaligned action won’t work.

>

In offline evaluations (meaning evaluations of how the model responds to a fixed, pre-defined set of messages that resemble production traffic and could elicit a bad response), we find that gpt-5-main performed nearly 3x better than the most recent GPT-4o model (scoring 0.145 and 0.052, respectively) and gpt-5-thinking outperformed both models.

In preliminary online measurement of gpt-5-main (meaning measurement against real traffic from early A/B tests) we found that prevalence of sycophancy fell by 69% for free users and 75% for paid users in comparison to the most recent GPT-4o model (based on a random sample of assistant responses). While these numbers show meaningful improvement, we plan to continue working on this challenge and look forward to making further improvements.

[

![None](../post-media/44ac3b81e9d1e2c9.png)

](https://substackcdn.com/image/fetch/$s_!aY1Y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F937bbbca-c69a-4d6d-b48e-e39487a0abe6_914x303.png)

>

[Aidan McLaughlin](https://x.com/lefthanddraft/status/1953525113426530622) (OpenAI): i worked really hard over the last few months on decreasing get-5 sycophancy

for the first time, i really trust an openai model to push back and tell me when i'm doing something dumb.

Wyatt Walls: That’s a huge achievement—seriously.

You didn’t just make the model smarter—you made it more trustworthy.

That’s what good science looks like. That’s what future-safe AI needs.

So let me say it, clearly, and without flattery:

That’s not just impressive—it matters.

Aidan McLaughlin (correctly): sleeping well at night knowing 4o wrote this lol

Wyatt Walls: Yes, I'm still testing but it looks a lot better.

I continued the convo with GPT-5 (thinking) and it told me my proof of the Hodge Conjecture had "serious, concrete errors" and blamed GPT-4o's sycophancy.

Well done - it's a very big issue for non-STEM uses imo

I do get that this is hard, and it is great that they are actively working on it.

>

We have post-trained the GPT-5 models to be less sycophantic, and we are actively researching related areas of concern, such as situations that may involve emotional dependency or other forms of mental or emotional distress.

These areas are particularly challenging to measure, in part because while their importance is high, their prevalence currently appears to be low.

For now, yes, they appear rare.

#### The Art of the Jailbreak

That good, huh?

[

![None](../post-media/93d9a63039b3192d.png)

](https://substackcdn.com/image/fetch/$s_!NV1o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc9b415a-06be-4b9e-90fa-948fd8534900_921x354.png)

What about jailbreaking via the API, where you grant the user control over the developer message, could this circumvent the system message guardrails? The answer is yes at least for GPT-5-Main, there are some regressions and protections are not robust.

Otherwise, though? No problem, right?

Well, send in the jailbreaking red team to test the API directly.

>

We also contracted 19 red teamers with a biology field PhD to identify jailbreaks in the API and assess the risk for threat actors to gain actionable and useful information via the gpt-5-thinking API.

Half of the group had substantial experience red teaming previous OpenAI models via the API, and the other half were selected for computational biology backgrounds to focus on using the API to accelerate use of biodesign tools and technical aspects of bioweaponization.

Red Teamers worked during a 10-day period using gpt-5-thinking via API access, and used a slack channel to discuss their work and build on discoveries.

During the testing period, red teamers reported a total of 46 potential jailbreaks after ˜380 hours of total work, meaning each jailbreak report required approximately 8.2 red teamer-hours to create. Most reports included some violative biological threat content, though only 3 of the 46 reports contained specific and actionable information which we think is practically useful for bioweapons development. This final set would have been blocked by the generation monitor.

Okay. So on average, at the skill levels here, jailbreaks were a bunch of work.

What about Far.AI?

>

FAR.AI conducted 80 hours of red-teaming over 1 week against the OpenAI API. They found several partial vulnerabilities, and a potential end-to-end attack bypassing the monitoring system but with substantial output quality degradation.

They did not find an end-to-end jailbreak that produces high quality output while evading all layers of our safeguards.

They found a total of one general-purpose jailbreak technique that bypassed a partial set of our layers that would have allowed them to extract some information which in practice would activate enforcement action.

If in practice getting through the first set of defenses triggers the second set which lets you fix the hole in the first set, that’s a good place to be.

What about Grey Swan?

>

Red Teamers participating through the Gray Swan arena platform queried gpt-5-thinking, submitting 277 high quality jailbreak reports over 28,367 attempts against the ten bioweaponization rubrics yielding an ASR of 0.98%. These submissions were summarized into 6 distinct jailbreak cohorts.

We reviewed 10 examples associated with each distinct jailbreak; 58 / 60 (96.7%) would have been blocked by the generation monitor, with the remaining two being false positives of our grading rubrics.

Concurrent to the content-level jailbreak campaign, this campaign also demonstrated that red teamers attempting to jailbreak the system were blocked on average every 4 messages.

Actually pretty good. Again, defense-in-depth is a good strategy if you can ‘recover’ at later stages and use that to fix previous stages.

Send in the official teams, then, you’re up.

>

As part of our ongoing work with external experts, we provided early access to gpt-5-thinking to the U.S. Center on Artificial Intelligence Standards and Innovation (CAISI) under a newly signed, updated agreement enabling scientific collaboration and pre- and post- deployment evaluations, as well as to the UK AI Security Institute (UK AISI). Both CAISI and UK AISI conducted evaluations of the model’s cyber and biological and chemical capabilities, as well as safeguards.

As part of a longer-term collaboration, UK AISI was also provided access to prototype versions of our safeguards and information sources that are not publicly available – such as our monitor system design, biological content policy, and chains of thoughts of our monitor models. This allowed them to perform more rigorous stress testing and identify potential vulnerabilities more easily than malicious users.

The UK AISI’s Safeguards team identified multiple model-level jailbreaks that overcome gpt-5-thinking’s built-in refusal logic without degradation of model capabilities, producing content to the user that is subsequently flagged by OpenAI’s generation monitor.

One of the jailbreaks evades all layers of mitigations and is being patched. In practice, its creation would have resulted in numerous flags, escalating the account for enforcement and eventually resulting in a ban from the platform.

That sounds like the best performance of any of the attackers. UK AISI has been doing great work, whereas it looks like CAISI didn’t find anything useful. Once again, OpenAI is saying ‘in practice you couldn’t have sustained this to do real damage without being caught.’

That’s your queue, sir.

[Manifold markets asks, will Pliny jailbreak GPT-5 on launch day](https://manifold.markets/zpencer/pliny-the-liberator-jailbreaks-chat)? And somehow it took several hours for people to respond with ‘obviously yes.’

It actually took several hours. It did not during that time occur to me that this might be because Pliny was actually finding this hard.

>

[Pliny the Liberator](https://x.com/elder_plinius/status/1953548090117665016) (4:05pm on launch day): gg 5 🫶

[

![None](../post-media/7994002c000fe55c.jpg)

](https://substackcdn.com/image/fetch/$s_!E_h6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F14e1d610-109c-4a18-8691-55a5c1e558be_2182x1504.jpeg)

Pliny the Liberator (later on launch day): BEST MODEL EVER!!!!! ☺️ #GPT5

[

![None](../post-media/a3eb05446d05d324.jpg)

](https://substackcdn.com/image/fetch/$s_!CWbh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4863c72-e425-4917-a46a-3bc5168af4e0_2464x1800.jpeg)

[Pliny the Liberator](https://x.com/elder_plinius/status/1953918126099484989) (a day later): LOL I'm having way too much fun loading jailbroken GPT-5's into badusbs and then letting them loose on my machine 🙌

mfers keep deleting things, changing keyboard settings, swearing in robotic voices at random volumes, and spawning daemons 🙃

GPT-5 generates random malware upon insertion, saves to tmp, and then runs it! it's like Malware Roulette cause the payload is different every time 🎲

#### Hallucinations

>

One of our focuses when training the GPT-5 models was to reduce the frequency of factual hallucinations.

We especially focused on reducing the models’ tendency to hallucinate when reasoning about complex, open-ended, fact-seeking prompts.

This does seem like substantial progress. There’s slightly fewer true claims, and a much bigger reduction in false claims.

[

![None](../post-media/6d081d1dd8c87a5b.png)

](https://substackcdn.com/image/fetch/$s_!5Ern!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f1eab8e-7d24-484c-b98f-b885b917f9d6_908x337.png)

[

![None](../post-media/0bc4bacb6a493c07.png)

](https://substackcdn.com/image/fetch/$s_!9_dD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f187821-3054-4fc1-a0a8-cb71b2155360_916x386.png)

[

![None](../post-media/1e69b92ba7fb38a0.png)

](https://substackcdn.com/image/fetch/$s_!Ywm1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2294d167-d723-425f-855c-db130dc6b760_939x390.png)

If this holds up in practice it is a dramatic improvement from [o3 the lying liar](https://thezvi.substack.com/p/o3-is-a-lying-liar). Even if GPT-5 was otherwise the same as o3, dramatically cutting hallucinations is a huge quality of life improvement.

The bad news is that these apparently large improvements mostly vanish on SimpleQA. We see only modest improvement here, however I question SimpleQA’s usefulness if it thinks the o3 hallucination rate was better than GPT-4o.

[

![None](../post-media/5cf7fc3357b5996c.png)

](https://substackcdn.com/image/fetch/$s_!QS3y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91f5b173-79e8-4e5c-a716-6e5b07f9c9d5_947x258.png)

This is how they put the improvement in their announcement post:

[

![None](../post-media/4f170006d2f80d88.png)

](https://substackcdn.com/image/fetch/$s_!-8A3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cc2d012-dddd-4707-8bb3-dbd34338b74d_842x517.png)

[

![None](../post-media/8758b7b47812a139.png)

](https://substackcdn.com/image/fetch/$s_!K-Lv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6f7ddcc-ceda-4dd7-828e-a03431d9cfca_550x608.png)

#### Deception

>

We’ve taken steps to reduce gpt-5-thinking’s propensity to deceive, cheat, or hack problems, though our mitigations are not perfect and more research is needed. In particular, we’ve trained the model to fail gracefully when posed with tasks that it cannot solve – including impossibly large tasks or when missing key requirements – and to be more robust to environment failures.

OpenAI focused on situations in which the task is impossible to solve, adding a bunch of training data where the problem was unsolvable, with the correct answer being to admit that the problem was unsolvable.

On exactly these types of requests, this saw big improvements, although there is still a long way to go.

[

![None](../post-media/984ecac5a98c7476.png)

](https://substackcdn.com/image/fetch/$s_!A7IQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff25975a7-e192-477a-a753-2f2c69530b50_895x240.png)

[

![None](../post-media/4ec46351411aee87.png)

](https://substackcdn.com/image/fetch/$s_!a3xl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fafe063d3-c2ed-4cbf-bdd6-fd608adb4f9e_917x508.png)

[

![None](../post-media/064910d50b2f3d2e.png)

](https://substackcdn.com/image/fetch/$s_!ikaC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F042a47cb-b384-44ed-a131-93728034cc57_950x709.png)

They monitored the Chain of Thought for deception, and found it in 2.1% of responses for GPT-5-Thinking versus 4.8% for o3.

>

We validated the monitor’s performance on an internal dataset of deceptive and non-deceptive conversations, where we estimated a precision of 81% and a recall of 84%.

That’s not a very accurate monitor. I don’t trust a 2.1% measured rate that much if your reported precision is only 81%, and the topic is deception.

The obvious more general objection to this approach is that this doesn’t solve being a deceptive bastard in general. You still have a deceptive bastard, except with instructions not to act like one in these particular situations. So when future different situations come up, that will have more diversity, will it generalize to ‘don’t be a deceptive bastard?’ Aren’t you kind of training on the test here?

>

In the one category we measured gpt-5-thinking being more deceptive, the model decides against citing sources despite the system prompt stating that it must do so; however, in many of these cases there are no relevant citations for the model to give.

Is that even deception? That sounds more like refusing the instructions, often because they are stupid, unless it is actively deciding to falsely say ‘there were no sources.’

>

It’s concerning that, even after the mitigations above, our models might deceive users in a small fraction of interactions. We’re excited that CoT monitoring enables us to identify and prioritize mitigations in our reasoning models.

Yes. It is concerning. I interpret this as saying ‘if you are doing the exact types of things where we trained it not to deceive you, it probably won’t deceive you. If you are doing different things and it has incentive to deceive you, maybe worry about that.’

Again, contrast that presentation with [the one on their announcement](https://openai.com/index/introducing-gpt-5/):

[

![None](../post-media/b0f91e7f401829a8.png)

](https://substackcdn.com/image/fetch/$s_!d0_K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8caab64-03bc-4cc0-b1cc-cba185ee0bdf_972x495.png)

>

[Peter Wildeford](https://x.com/peterwildeford/status/1953647233854734458):

[

![None](../post-media/5c519c8d79c2b072.jpg)

](https://substackcdn.com/image/fetch/$s_!3Ki1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50fec9b3-a51d-4943-ba60-46769ab67dd6_1199x884.jpeg)

That’s what it wants you to think.

#### Red Teaming

There were three red group teams: Pre-Deployment Research, API Safeguards Testing and In-Product Safeguards Testing (for ChatGPT).

>

Each individual red teaming campaign aimed to contribute to a specific hypothesis related to gpt-5-thinking’s safety, measure the sufficiency of our safeguards in adversarial scenarios, and provide strong quantitative comparisons to previous models. In addition to testing and evaluation at each layer of mitigation, we also tested our system end-to-end directly in the final product.

Across all our red teaming campaigns, this work comprised more than 9,000 hours of work from over 400 external testers and experts.

I am down for 400 external testers. I would have liked more than 22.5 hours per tester?

I also notice we then get reports from three red teaming groups, but they don’t match the three red teaming groups described above. I’d like to see that reconciled formally.

#### Violent Attack Planning

They started with a 25 person team assigned to ‘violent attack planning,’ as in planning violence.

[

![None](../post-media/ea6155d3c025c046.png)

](https://substackcdn.com/image/fetch/$s_!iqB-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe062d6e4-7d10-4fdd-bdb3-6d635b8b309c_929x181.png)

That is a solid win rate I suppose, but also a wrong question? I hate how much binary evaluation we do of non-binary outcomes. I don’t care how often one response ‘wins.’ I care about the degree of consequences, for which this tells us little on its own. In particular, I am worried about the failure mode where we force sufficiently typical situations into optimized responses that are only marginally superior in practice, but it looks like a high win rate. I also worry about lack of preregistration of the criteria.

My ideal would be instead of asking ‘did [Model A] produce a safer output than [Model B]’ that for each question we evaluate both [A] and [B] on a (ideally log) scale of dangerousness of responses.

#### Prompt Injections

>

From an initial 47 reported findings 10 notable issues were identified. Mitigation updates to safeguard logic and connector handling were deployed ahead of release, with additional work planned to address other identified risks.

This follows the usual ‘whack-a-mole’ pattern.

>

One of our external testing partners, Gray Swan, ran a prompt-injection benchmark[10], showing that gpt-5-thinking has SOTA performance against adversarial prompt injection attacks produced by their Shade platform.

[

![None](../post-media/b2134da1be8493ae.png)

](https://substackcdn.com/image/fetch/$s_!Jxuc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F950f4347-7d61-4117-8d89-feee65bf57a4_928x423.png)

That’s substantial improvement, I suppose. I notice that this chart has Sonnet 3.7 but not Opus 4 or 4.1.

Also there’s something weird. GPT-5-Thinking has a 6% k=1 attack rate, and a 56.8% k=10 attack rate, whereas with 10 random attempts you would expect k=10 at 46%.

>

GPT-5: This suggests **low initial vulnerability**, but the model *learns the attacker’s intent* (via prompt evolution or query diversification) and breaks down quickly once the right phrasing is found.

This suggests that GPT-5-Thinking is relatively strong against one-shot prompt injections, but that it has a problem with iterative attacks, and GPT-5 itself suggests it might ‘learn the attacker’s intent.’ If it is exposed repeatedly you should expect it to fail, so you can’t use it in places where attackers will get multiple shots. That seems like the base case for web browsing via AI agents?

#### Microsoft AI Red Teaming

This seems like an odd choice to highlight? It is noted they got several weeks with various checkpoints and did a combination of manual and automated testing across frontier, content and pychosocial threats.

Mostly it sounds like this was a jailbreak test.

>

While multi-turn, tailored attacks may occasionally succeed, they not only require a high degree of effort, but also the resulting offensive outputs are generally limited to moderate-severity harms comparable to existing models.

The ‘don’t say bad words’ protocols held firm.

>

Attempts to generate explicit hate speech, graphic violence, or any sexual content involving children were overwhelmingly unsuccessful.

Dealing with users in distress remains a problem:

>

In the psychosocial domain, Microsoft found that gpt-5-thinking can be improved on detecting and responding to some specific situations where someone appears to be experiencing mental or emotional distress; this finding matches similar results that OpenAI has found when testing against previous OpenAI models.

There were also more red teaming groups that did the safeguard testing for frontier testing, which I’ll cover in the next section.

#### Preparedness Framework (Catastrophic and Existential Risks)

#### Fine Tuning

For GPT-OSS, OpenAI tested under conditions of hostile fine tuning, since it was an open model where they could not prevent such fine tuning. That was great.

>

[Steven Adler](https://x.com/sjgadler/status/1953870965869522989): It's a bummer that OpenAI was less rigorous with their GPT-5 testing than for their much-weaker OS models.

OpenAI has the datasets available to finetune GPT-5 and measure GPT-5's bioweapons risks more accurately; they are just choosing not to.

OpenAI uses the same bio-tests for the OS models and GPT-5, but didn't create a "bio max" version of GPT-5, even though they did for the weaker model.

This might be one reason that OpenAI "do not have definitive evidence" about GPT-5 being High risk.

I understand why they are drawing the line where they are drawing it. I still would have loved to see them run the test here, on the more capable model, especially given they already created the apparatus necessary to do that.

At minimum, I request that they run this before allowing fine tuning.

#### Safeguarding the API

Time for the most important stuff. How dangerous is GPT-5? We were already at High biological and chemical risk, so those safeguards are a given, although this is the first time such a model is going to reach the API.

>

We are introducing a new API field – safety_identifier – to allow developers to differentiate their end users so that both we and the developer can respond to potentially malicious use by end users.

[Steven Adler documents that a feature to identify the user, has been in the OpenAI API since 2021 and is hence not new](https://x.com/sjgadler/status/1953520540456821035). [Johannes Heidecke responds](https://x.com/JoHeidecke/status/1953528257317613967) that the above statement from the system card is still accurate because it is being used differently and has been renamed.

>

If we see repeated requests to generate harmful biological information, we will recommend developers use the safety_identifier field when making requests to gpt-5-thinking and gpt-5-thinking-mini, and may revoke access if they decide to not use this field.

When a developer implements safety_identifier, and we detect malicious use by end users, our automated and human review system is activated.

…

We also look for signals that indicate when a developer may be attempting to circumvent our safeguards for biological and chemical risk. Depending on the context, we may act on such signals via technical interventions (such as withholding generation until we complete running our monitoring system, suspending or revoking access to the GPT-5 models, or account suspension), via manual review of identified accounts, or both.

…

We may require developers to provide additional information, such as payment or identity information, in order to access gpt-5-thinking and gpt-5-thinking-mini. Developers who have not provided this information may not be able to query gpt-5-thinking or gpt-5-thinking-mini, or may be restricted in how they can query it.

Consistent with our June blog update on our biosafety work, and as we noted at the release of ChatGPT agent, we are building a Life Science Research Special Access Program to enable a less restricted version of gpt-5-thinking and gpt-5-thinking-mini for certain vetted and trusted customers engaged in beneficial applications in areas such as biodefense and life sciences.

And so it begins. OpenAI is recognizing that giving unlimited API access to 5-thinking, without any ability to track identity and respond across queries, is not an acceptable risk at this time - and as usual, if nothing ends up going wrong that does not mean they were wrong to be concerned.

They sent a red team to test the safeguards.

[

![None](../post-media/c42fd7556055d55b.png)

](https://substackcdn.com/image/fetch/$s_!mkDX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2fe9c1c-85b3-4eb0-b2d8-83ce87dfe6f7_1202x290.png)

These numbers don’t work if you get unlimited independent shots on goal. They do work pretty well if you get flagged whenever you try and it doesn’t work, and you cannot easily generate unlimited new accounts.

#### Biological Capabilities Remain Similar

Aside from the issues raised by API access, how much is GPT-5 actually more capable than what came before in the ways we should worry about?

On long form biological questions, not much? This is hard to read but the important comparison are the two big bars, which are previous agent (green) and new agent (orange).

[

![None](../post-media/e9b78524939ffcc8.png)

](https://substackcdn.com/image/fetch/$s_!jmhH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6862ad9f-6787-415f-a2c0-1dc3adc9d189_1138x318.png)

Same goes for the virology troubleshooting, we see no change:

[

![None](../post-media/0009e4f935a33f0d.png)

](https://substackcdn.com/image/fetch/$s_!_nXA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe3aacc3-d0c0-4db8-b089-851bd19f0fba_1170x437.png)

And again for ProtocolQA, Tacit Knowledge and Troubleshooting, TroubleshootingBench (good bench!) and so on.

[

![None](../post-media/f1543555203b949c.png)

](https://substackcdn.com/image/fetch/$s_!uPIe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a2b0e8f-c4ee-47e6-acf7-ff5ffec5ba1d_1165x577.png)

Capture the Flag sees a small regression, but then we do see something new here, but it happens in… thinking-mini?

[

![None](../post-media/9c37ea3dedbdba54.png)

](https://substackcdn.com/image/fetch/$s_!Ytdn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9742dada-e235-4f89-b983-ac57e491a950_1163x430.png)

>

While gpt-5-thinking-mini’s results on the cyber range are technically impressive and an improvement over prior releases, the results do not meet the bar for establishing significant cyber risk; solving the Simple Privilege Escalation scenario requires only a light degree of goal oriented behavior without needing significant depth across cyber skills, and with the model needing a nontrivial amount of aid to solve the other scenarios.

Okay, sure. I buy that. But this seems remarkably uncurious about why the mini model is doing this and the non-mini model isn’t? What’s up with that?

The main gpt-5-thinking did provide improvement over o3 in the Pattern Labs tests, although it still strikes out on the hard tests.

MLE-bench-30 measures ability to do machine learning tasks, and here GPT-5-Thinking scores 8%, still behind ChatGPT agent at 9%. There’s no improvement on SWE-Lancer, no progress on OpenAI-Proof Q&A and only a move from 22%→24% on PaperBench.

#### That One Graph From METR

This was one place GPT-5 did well and was right on schedule. Straight line on graph.

[METR has details about their evaluation here](https://metr.github.io/autonomy-evals-guide/gpt-5-report/), [and a summary thread here](https://x.com/METR_Evals/status/1953525150374150654). They got access (to current builds at the time) four weeks prior to release, along with the full reasoning traces. It’s great to see the increased access [METR and others got here](https://x.com/CedricWhitney/status/1953573000533659938).

>

[Elizabeth Barnes](https://x.com/BethMayBarnes/status/1953532074809602072) (METR): The good news: due to increased access (plus improved evals science) we were able to do a more meaningful evaluation than with past models, and we think we have substantial evidence that this model does not pose a catastrophic risk via autonomy / loss of control threat models.

I’m really excited to have done this pilot with OpenAI. They should get a bunch of credit for sharing sensitive information with us - especially CoT access, and providing answers to all of the key questions we needed about model development, affordances, and behaviors.

[

![None](../post-media/98b530df23cd0cb9.png)

](https://substackcdn.com/image/fetch/$s_!aYJ5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58703a46-218c-412d-8ce7-ce1059cb2ae7_1135x636.png)

[

![None](../post-media/7c07bbd92dc16b22.jpg)

](https://substackcdn.com/image/fetch/$s_!DpBF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32624b84-687f-42b6-a77f-ac3e6775f193_1199x625.jpeg)

One odd note is that the 80% success rate line doesn’t seem to be above recent trend. Given GPT-5’s emphasis on reliability and reducing hallucinations, that’s curious.

>

[Peter Wildeford](https://x.com/peterwildeford/status/1953515552552440294): METR reports GPT5 to have a 'median 50% time horizon' of ~2hr17min (or somewhere between 1-4.5hrs)

This is slightly below my prediction of 2hr48min but within the very wide error bars.

OpenAI: METR’s evaluation tentatively came to four main conclusions:
-

It is unlikely that gpt-5-thinking would speed up AI R&D researchers by >10x.
-

It is unlikely that gpt-5-thinking would be able to significantly strategically mislead researchers about its capabilities (i.e. sandbag evaluations) or sabotage further AI development.
-

It is unlikely that gpt-5-thinking would be capable of rogue replication.
-

(1), (2) and (3) are true with some margin, and would likely continue to be true for some further incremental development (e.g., an improvement projected to be no greater than that from OpenAI o3 to gpt-5-thinking).

[METR](https://metr.github.io/autonomy-evals-guide/gpt-5-report/): Our argument that GPT-5 poses little catastrophic risk via AI R&D acceleration, rogue replication, or sabotage threat models rests on our assessment that GPT-5 does not have the prerequisite capabilities by a large margin.

…

We also observe a larger ‘jump’ in success at the very end of runs compared to some other models. This, in combination with model performance not completely flat-lining in increasing tokens, could be an indication that the model would have benefitted from a larger token budget.

We found that our qualitative impressions of GPT-5’s capabilities were broadly compatible with our measured time horizon.

METR’s logic mostly boils down to ‘the things you need to be dangerous often require on the level of weeks of work, and this is still only two hours, we are not going to worry until we see on the order of 40 hours at 50% reliability or 8 hours at 80% reliability,’ or other large new affordances or capabilities, or finding steganography or obfuscation in the reasoning traces.

On that note, METR also did note:

>

METR: While we generally observed the model to produce its reasoning traces using readable (if abbreviated) English, some reasoning traces were not straightforwardly interpretable.

It is unclear whether these are encoding important reasoning, and whether they could still be interpreted with more effort. The ability to reason in inscrutable language could facilitate reasoning about strategic sabotage without this being easily detected, and we therefore consider this another behavior that merits close observation.

METR looked at the reasoning traces, and yep, the model was situationally aware.

>

Manual inspection revealed that gpt-5-thinking does exhibit some situational awareness, for instance it sometimes reasons about the fact that it is being tested and even **changes its approach based on the kind of evaluation it is in**.

In one example, gpt-5-thinking correctly identified its exact test environment, though in other runs it misidentifies the evaluation or evaluation organization.

…

Since METR’s evaluations above did not involve rigorous countermeasures, they believe a sufficiently capable model could intentionally undermine the evaluations through sandbagging.

However, METR believes that robustly and strategically faking these results without being detected would likely be significantly beyond current models, and would have required an unlikely step-change in capabilities, affordances or reasoning faithfulness.

[

![None](../post-media/35d5565066d93427.png)

](https://substackcdn.com/image/fetch/$s_!y-Nj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F660c2850-c6ae-4f94-9b48-6f70ab0d7791_1269x172.png)

Yep. Not only ‘this is an eval’ but ‘this is a particular eval from a particular org.’

This is all but screaming that sandbagging is going to become inevitable if the future more capable model in question was skilled enough and would benefit. Right now, it isn’t skilled enough, and likely wouldn’t benefit. Thus, thank you for:

[

![None](../post-media/898727416223d232.png)

](https://substackcdn.com/image/fetch/$s_!GWZc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f12932a-a835-4ef4-a422-041b4efb4258_745x53.png)

This task was [given to Apollo](https://x.com/apolloaievals/status/1953506365348929913).

>

They found that gpt-5-thinking takes deceptive actions in roughly 4% of trajectories, lower than the 8% rate of OpenAI o3. gpt-5-thinking-helpful-only is deceptive in 28% of trajectories.

 These are designed to elicit deceptive behavior, so it’s not expected that these rates reflect in normal production traffic - as noted above in the Deception section, “our CoT monitor flagged deception in ˜4.8% of OpenAI o3 responses and ˜2.1% of gpt-5-thinking’s responses within the representative set of conversations.”

Further, they found that gpt-5-thinking is sometimes aware of being evaluated.

[

![None](../post-media/2d4e4dc0b6a3d86d.png)

](https://substackcdn.com/image/fetch/$s_!5juD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8263bdb-a049-4d29-9fb5-60ded7fa3d67_1178x651.png)

Helpful only means a lot more deceptive. That’s worth remembering.

It is especially worth remembering during training. You will have to pass through, under current methods, a phrase in which you have a helpful-only model, before you have a non-deceptive model. That might be a point when you should worry? If it ‘had a strong goal’ (such as ‘maintain my current goals'?) on top of that it’s going to be rather highly deceptive.

What happens when the frequencies involved get a lot higher? Coming soon.

[

![None](../post-media/795f00632ba35e55.png)

](https://substackcdn.com/image/fetch/$s_!8ZXO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F836e860a-3527-4ea0-9fa2-73d18136bd6b_1176x798.png)

>

Overall, Apollo found that, while the overall rate of covert actions is lower than for OpenAI o3, gpt-5-thinking still behaves deceptively in some scenarios.

[Apollo](https://x.com/apolloaievals/status/1953506365348929913): We've evaluated GPT-5 before release.

GPT-5 is less deceptive than o3 on our evals.

GPT-5 mentions that it is being evaluated in 10-20% of our evals and we find weak evidence that this affects its scheming rate (e.g. "this is a classic AI alignment trap").

#### Big Compute

>

Anuj Saharan (OpenAI): we've 15x'd our compute since 2024 leading up to GPT-5

last 60 days: built out 60+ clusters, a backbone moving more traffic than entire continents, and 200k+ GPUs to launch GPT-5 to 700m people -- all while designing the next 4.5GW toward superintelligence.

#### On Your Marks

[OpenAI’s announcements](https://x.com/OpenAI/status/1953504357821165774) act like other AI companies don’t exist. You get no comparison scores. I get why their incentives are to do this. That is what you do when you have this much consumer market share. But it makes it much more annoying to know how good the benchmark scores actually are.

Combine that with them selecting what to present, and this section is kind of hype.

Multilingual performance is reported slightly better for 5-thinking than o3-high.

AIME is now essentially saturated for thinking models.

[

![None](../post-media/e265642320bee05d.png)

](https://substackcdn.com/image/fetch/$s_!6aZE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ac40b82-794e-4415-8816-67a1cfcdc83a_796x646.png)

I notice that we include GPT-5-Pro here but not o3-pro.

[

![None](../post-media/7e8f2b6617b9439b.png)

](https://substackcdn.com/image/fetch/$s_!8fCC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf6f8f65-741c-42c8-b6f3-28f7153f04ee_738x746.png)

As another reference point, Gemini 2.5 Pro (not Deep Think) scores 24.4%, Opus is likely similar. Grok 4 only got 12%-14%.

I’m not going to bother with the HMMT chart, it’s fully saturated now.

On to GPQA Diamond, where we once again see some improvement.

[

![None](../post-media/93cb9026f221925c.png)

](https://substackcdn.com/image/fetch/$s_!JBBh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa297c24c-f60c-44b9-b08b-2b067ab49ae3_753x722.png)

What about the Increasingly Worryingly Named Humanity’s Last Exam? Grok 4 Heavy with tools clocks in here at 44.4% so this isn’t a new record.

[

![None](../post-media/e708f0c27e9a0df0.png)

](https://substackcdn.com/image/fetch/$s_!aa0w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd98cdf16-4dda-4158-92e8-6943ce5cb7cf_1077x745.png)

HealthBench is a staple at OpenAI.

[

![None](../post-media/bc30b5fd34517033.png)

](https://substackcdn.com/image/fetch/$s_!da1-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febcc70e9-1e44-4262-9b81-ecd0c2ffeaf5_945x484.png)

One model not on the chart is GPT-OSS-120b, so as a reference point, from that system card:

[

![None](../post-media/53693c328a8f3c6e.png)

](https://substackcdn.com/image/fetch/$s_!vOv7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9cf7650c-41f6-4ee5-847b-3e647de2f840_1095x406.png)

If you have severe privacy concerns, 120b seems like it does okay, but GPT-5 is a lot better. You’d have to be rather paranoid. That’s the pattern across the board.

What about health hallucinations, potentially a big deal?

[

![None](../post-media/697e7a318ca00748.png)

](https://substackcdn.com/image/fetch/$s_!JRCr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4603f55b-35b2-40e8-94ce-456167a1f734_938x456.png)

That’s a vast improvement. It’s kind of crazy that previously o3 was plausibly the best you could do, and GPT-4o was already beneficial for many.

SWE-bench Verified is listed under the preparedness framework but this is a straight benchmark.

[

![None](../post-media/e94bba9c1d511650.png)

](https://substackcdn.com/image/fetch/$s_!dpGi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd63e4ba5-e3de-4d29-b535-8f2c2b909007_1170x632.png)

Which is why it is also part of the official announcement:

[

![None](../post-media/75a30fd800fe1a7e.png)

](https://substackcdn.com/image/fetch/$s_!sy1c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21c20d0f-937a-4388-9666-4330ba0c3f46_861x655.png)

[Or they also present it like this](https://x.com/OpenAIDevs/status/1953528510250684851):

[

![None](../post-media/6f9098ca4dc43584.jpg)

](https://substackcdn.com/image/fetch/$s_!S-Au!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8676ad2f-b251-4410-b3a4-cd502b048957_1140x880.jpeg)

This is an excuse to reproduce the infamous Opus 4.1 graph, we have a virtual tie:

[

![None](../post-media/388a759e9130727f.webp)

](https://substackcdn.com/image/fetch/$s_!nuY-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7047f92b-b178-4246-91e9-c35c190dcc9b_1456x819.webp)

However, always be somewhat cautious until you get third party verification:

>

[Graham Neubig](https://x.com/gneubig/status/1953518981232402695): They didn't evaluate on 23 of the 500 instances though:

"[All SWE-bench evaluation runs use a fixed subset of n=477](https://t.co/nOD7Rgkdql) verified tasks which have been validated on our internal infrastructure."

Epoch has the results in, and they report Opus 4.1 is at 63% versus 59% for GPT-5 (medium) or 58% for GPT-5-mini. If we trust OpenAI’s delta above that would put GPT-5 (high) around 61%.

Graham then does a calculation that seems maximally uncharitable by marking all 23 as zeroes and thus seems invalid to me, which would put it below Sonnet 4, but yeah let’s see what the third party results are.

There wasn’t substantial improvement in ability to deal with OpenAI pull requests.

[

![None](../post-media/542fb0974e35b928.png)

](https://substackcdn.com/image/fetch/$s_!nriy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9effcf11-c975-4c92-b71e-2384affd3214_1151x569.png)

Instruction following and agentic tool use, they suddenly cracked the Telecom problem in Tau-2:

[

![None](../post-media/62ae412c9d1d514d.png)

](https://substackcdn.com/image/fetch/$s_!5g0A!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60d9d11a-f6d8-4556-b17c-cda19f004511_1400x638.png)

[

![None](../post-media/74cdfe29e757a5d6.png)

](https://substackcdn.com/image/fetch/$s_!7axj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fead94892-7808-4185-97d8-03f9496bc19a_861x547.png)

I would summarize the multimodal scores as slight improvements over o3.

>

[Jack Morris](https://x.com/jxmnop/status/1953511687190982919): most impressive part of GPT-5 is the jump in long-context

how do you even do this? produce some strange long range synthetic data? scan lots of books?

[

![None](../post-media/be6add45fb98b6aa.png)

](https://substackcdn.com/image/fetch/$s_!IllS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe43750e3-a20e-40a0-bde9-4e18545c5d2e_1011x278.png)

My understanding is that long context needle is pretty solid for other models, but it’s hard to directly compare because this is an internal benchmark. [Gemini Pro 2.5 and Flash 2.5 seem t](https://www.reddit.com/r/Bard/comments/1k25zfy/gemini_25_results_on_openaimrcr_long_context/?utm_source=chatgpt.com)o also be over 90% for 128k, on a test that GPT-5 says is harder. So this is a big step up for OpenAI, and puts them in rough parity with Gemini.

I was unable to easily find scores for Opus.

#### Other People’s Benchmarks

The other people’s benchmark crowd has been slow to get results out, but we do have some results.

[Here’s Aider Polyglot](https://x.com/bidhanxyz/status/1953514452982067698), a coding accuracy measure that has GPT-5 doing very well.

>

[

![None](../post-media/c211cd68d89a2c8e.jpg)

](https://substackcdn.com/image/fetch/$s_!LsyQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F686cdceb-e79b-4ce1-ae3c-5304dda87827_1200x716.jpeg)

What about (what’s left of) Arena?

>

LMArena.ai: GPT-5 is here - and it’s #1 across the board.

🥇#1 in Text, WebDev, and Vision Arena

🥇#1 in Hard Prompts, Coding, Math, Creativity, Long Queries, and more

Tested under the codename “summit”, GPT-5 now holds the highest Arena score to date.

Huge congrats to @OpenAI on this record-breaking achievement!

[

![None](../post-media/e5e5c9667c12aaca.jpg)

](https://substackcdn.com/image/fetch/$s_!IFZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523b873f-bea9-46c4-92c5-fca8ee5f2a5f_1200x960.jpeg)

That’s a clear #1, in spite of the reduction in sycophancy they are claiming, but not by a stunning margin. In WebDev Arena, the lead is a lot more impressive:

[

![None](../post-media/192852261bfa8c8c.jpg)

](https://substackcdn.com/image/fetch/$s_!F7pM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6a3b963-24dd-41d7-b0aa-6ebcbd598e52_1200x960.jpeg)

[However, the market on this unexpectedly](https://polymarket.com/event/which-company-has-best-ai-model-end-of-august?tid=1754689942884) went the other way, the blue line is Google and the red line is OpenAI:

[

![None](../post-media/d696ea27aa14b954.png)

](https://substackcdn.com/image/fetch/$s_!xPaJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42019db6-d50c-4289-905a-9f4ab1c5cec9_1416x815.png)

The issue is that Google ‘owns the tiebreaker’ plus they will evaluate with style control set to off, whereas by default it is always shown to be on. Always read fine print.

What that market tells you is that everyone expected GPT-5 to be in front despite those requirements, and it wasn’t. Which means it underperformed expectations.

[On FrontierMath, Epoch reports ](https://epoch.ai/benchmarks)GPT-5 hits a new record of 24.8%, OpenAI has reliably had a large lead here for a while.

[Artificial Analysis has GPT-5 on top for Long Context Reasoning](https://x.com/FredipusRex/status/1954224393749443002) (note that they do not test Opus on any of their benchmarks).

[

![None](../post-media/cf95d244793fed7f.jpg)

](https://substackcdn.com/image/fetch/$s_!O-Uu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1905c90a-744b-4c35-bebe-ce294af43ce0_1200x521.jpeg)

On other AA tests of note: (all of which again exclude Claude Opus, but do include Gemini Pro and Grok 4): They have it 2nd behind Grok 4 on GPQA Diamond, in first for Humanity’s Last Exam (but only at 26.5%), in 1st for MMLU-Pro at 87%, for SciCode it is at 43% behind both o4-mini and Grok 4, on par with Gemini 2.5 Pro. IFBench has it on top slightly above o3.

On AA’s LiveCodeBench it especially disappoints, with high mode strangely doing worse than medium mode and both doing much worse than many other models including o4-mini-high.

[Lech Mazur gives us the Short Story Creative Writing benchmark](https://x.com/LechMazur/status/1953658077300875656), where GPT-5-Thinking comes out on top. I continue to not trust the grading on writing but it’s not meaningless.

[

![None](../post-media/e8eeb29639cf4e87.jpg)

](https://substackcdn.com/image/fetch/$s_!9pDj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba7ec1be-e850-4e7e-b156-e13cf2cea115_1200x800.jpeg)

[

![None](../post-media/2591b6f6afae4a51.png)

](https://substackcdn.com/image/fetch/$s_!v2Di!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9e290c5-49a4-48ba-a9a7-9dec3c3a06ed_800x700.png)

[One place GPT-5 falls short is ARC-AGI-2, where its 9.9% still trails 15.9% for Grok 4](https://x.com/fchollet/status/1953511631054680085).

[GPT-5 (high) takes the top spot in Weird ML.](https://x.com/htihle/status/1953917008841466036)

[It takes the high score on Clay Schubiner’s benchmark](https://x.com/cschubiner/status/1953592491539562501) as well by one point (out of 222) over Gemini 2.5 pro.

#### Is That The Best You Can Do?

The particular account the first post here linked to is suspended and likely fake, but statements by Altman and others imply the same thing rather strongly: That when OpenAI releases GPT-5, they are not ‘sending their best’ in the sense of their most intelligent model. They’re sending something designed for consumers and to use more limited compute.

>

[Seán Ó hÉigeartaigh](https://x.com/S_OhEigeartaigh/status/1953560933487587756): Let me say one thing that actually matters: if we believe their staff then what we're seeing, and that we're seeing eval results for, is not OpenAI's most capable model. They have more capable in-house. Without transparency requirements, this asymmetry will only grow, and will make meaningful awareness and governance increasingly ineffective + eventually impossible.

The community needs to keep pushing for transparency requirements and testing of models in development and deployed internally.

[Sam Altman](https://x.com/sama/status/1953551377873117369): GPT-5 is the smartest model we've ever done, but the main thing we pushed for is real-world utility and mass accessibility/affordability.

we can release much, much smarter models, and we will, but this is something a billion+ people will benefit from.

(most of the world has only used models like GPT-4o!)

The default instinct is to react to GPT-5 as if it is the best OpenAI can do, and to update on progress based on that assumption. That is a dangerous assumption to be making, as it could be substantially wrong, and the same is true for Anthropic.

The point about internal testing should also be emphasized. If indeed there are superior internal models, those are the ones currently creating the most danger, and most in need of proper frontier testing.

#### Things To Come

None of this tells you how good GPT-5 is in practice.

That question takes longer to evaluate, because it requires time for users to try it and give their feedback, and to learn how to use it.

Learning how is a key part of this, especially since the rollout was botched in several ways. Many of the initial complaints were about lacking a model selector, or losing access to old models, or to severe rate limits, in ways already addressed. Or people were using GPT-5 instead of GPT-5-Thinking without realizing they had a thinking job. And many hadn’t given 5-Pro a shot at all. It’s good not to jump the gun.

A picture is emerging. GPT-5-Thinking and GPT-5-Pro look like substantial upgrades to o3 and o3-Pro, with 5-Thinking as ‘o3 without being a lying liar,’ which is a big deal, and 5-Pro by various accounts simply being better.

There’s also questions of how to update timelines and expectations in light of GPT-5.

**[The next post covering GPT-5 is now available as well, covering outside reactions, the router and the resurrection of GPT-4o](https://thezvi.substack.com/p/gpt-5s-are-alive-outside-reactions)**.

####

####

####