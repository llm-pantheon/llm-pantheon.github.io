---
title: "o3 Will Use Its Tools For You"
source: https://thezvi.substack.com/p/o3-will-use-its-tools-for-you
author: Zvi Mowshowitz
date: unknown
models: [o3]
tags: [zvi]
mirrored: 2026-07-15
note: mirrored against link rot by the Pantheon; all rights with the original author
---
# o3 Will Use Its Tools For You

[

![Zvi Mowshowitz's avatar](https://substackcdn.com/image/fetch/$s_!8FQ8!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4e61e08-4086-4cba-a82c-d31d64270804_48x48.png)](https://substack.com/@thezvi)

[Zvi Mowshowitz](https://substack.com/@thezvi)

Apr 18, 2025

[OpenAI has finally introduced us to the full o3](https://openai.com/index/introducing-o3-and-o4-mini/) along with o4-mini.

>

[Greg Brockman (OpenAI)](https://x.com/gdb/status/1912561761489940639): Just released o3 and o4-mini! These models feel incredibly smart.

We've heard from top scientists that they produce useful novel ideas.

Excited to see their positive impact on people's daily lives and humanity's hardest problems!

[Sam Altman](https://x.com/sama/status/1912558745013612888): we expect to release o3-pro to the pro tier in a few weeks

By all accounts, this upgrade is a big deal. They are giving us a modestly more intelligent model, but more importantly giving it better access to tools and ability to discern when to use them, to help get more practical value out of it. The tool use, and the ability to string it together and persist, is where o3 shines.

The highest praise I can give o3 is that this was by far the most a model has been used as part of writing its own review post, especially helping answer questions about its model card.

[Usage limits are claimed to be](https://x.com/Angaisb_/status/1912569839517843811) 50/week for o3, 150/day for o4-mini and 50/day for o4-mini-high for Plus users along with 10 Deep Research queries per month.

This post covers all things o3: Its capabilities and tool use, where to use it and where not to use it, and also the model card and o3’s alignment concerns. o3 is on the cusp of having dangerous capabilities, and while o3 is highly useful it hallucinates remarkably often by today’s standards and engages in an alarmingly high amount of deceptive and hostile behaviors.

As usual, I am incorporating a wide variety of representative opinion and feedback, although in this case there was too much to include everything.

#### Table of Contents

-

[What’s In a Name.](https://thezvi.substack.com/i/161547977/what-s-in-a-name)
-

[My Current Model Use Heuristics.](https://thezvi.substack.com/i/161547977/my-current-model-use-heuristics)
-

[Huh, Upgrades.](https://thezvi.substack.com/i/161547977/huh-upgrades)
-

[Use All the Tools.](https://thezvi.substack.com/i/161547977/use-all-the-tools)
-

[Search the Web.](https://thezvi.substack.com/i/161547977/search-the-web)
-

[On Your Marks.](https://thezvi.substack.com/i/161547977/on-your-marks)
-

[The System Prompt.](https://thezvi.substack.com/i/161547977/the-system-prompt)
-

[The o3 and o4-mini System Card.](https://thezvi.substack.com/i/161547977/the-o3-and-o4-mini-system-card)
-

[Tests o3 Aced.](https://thezvi.substack.com/i/161547977/tests-o3-aced)
-

[Hallucinations.](https://thezvi.substack.com/i/161547977/hallucinations)
-

[Instruction Hierarchy.](https://thezvi.substack.com/i/161547977/instruction-hierarchy)
-

[Image Refusals.](https://thezvi.substack.com/i/161547977/image-refusals)
-

[METR Evaluations for Task Duration and Misalignment.](https://thezvi.substack.com/i/161547977/metr-evaluations-for-task-duration-and-misalignment)
-

[Apollo Evaluations for Scheming and Deception.](https://thezvi.substack.com/i/161547977/apollo-evaluations-for-scheming-and-deception)
-

[We Are Insufficiently Worried About These Alignment Failures.](https://thezvi.substack.com/i/161547977/we-are-insufficiently-worried-about-these-alignment-failures)
-

[GPT-4.1 Also Has Some Issues.](https://thezvi.substack.com/i/161547977/gpt-4-1-also-has-some-issues)
-

[Pattern Lab Evaluations for Cybersecurity.](https://thezvi.substack.com/i/161547977/pattern-lab-evaluations-for-cybersecurity)
-

[Preparedness Framework Tests.](https://thezvi.substack.com/i/161547977/preparedness-framework-tests)
-

[Biological and Chemical Risks (4.2).](https://thezvi.substack.com/i/161547977/biological-and-chemical-risks-4-2)
-

[Cybersecurity (4.3).](https://thezvi.substack.com/i/161547977/cybersecurity-4-3)
-

[AI Self-Improvement (4.4).](https://thezvi.substack.com/i/161547977/ai-self-improvement-4-4)
-

[Perpetual Shilling.](https://thezvi.substack.com/i/161547977/perpetual-shilling)
-

[High Praise.](https://thezvi.substack.com/i/161547977/high-praise)
-

[Syncopathy.](https://thezvi.substack.com/i/161547977/syncopathy)
-

[Mundane Utility Versus Capability Watch.](https://thezvi.substack.com/i/161547977/mundane-utility-versus-capability-watch)
-

[o3 Offers Mundane Utility.](https://thezvi.substack.com/i/161547977/o3-offers-mundane-utility)
-

[o3 Doesn’t Offer Mundane Utility.](https://thezvi.substack.com/i/161547977/o3-doesn-t-offer-mundane-utility)
-

[o4-mini Also Exists.](https://thezvi.substack.com/i/161547977/o4-mini-also-exists)
-

[Colin Fraser Dumb Model Watch.](https://thezvi.substack.com/i/161547977/colin-fraser-dumb-model-watch)
-

[o3 as Forecaster.](https://thezvi.substack.com/i/161547977/o3-as-forecaster)
-

[Is This AGI?.](https://thezvi.substack.com/i/161547977/is-this-agi)

#### What’s In a Name

[OpenAI’s naming continues to be a train wreck](https://x.com/ManifoldMarkets/status/1912567025815417195) that doesn’t get better, first we had the 4.1 release and now this issue:

>

Manifold: "wtf I thought 4o-mini was supposed to be super smart, but it didn't get my question at all?"

"no no dude that's their least capable model. o4-mini is their most capable coding model"

o4-mini is the lightweight version of this, and presumably o4-mini-high is the medium weight version? The naming conventions continue to be confusing, especially releasing o3 and o4-mini at the same time. Should we consider these same-generation or different-generation models?

I’d love if we could equalize these numbers, even though o4-mini was (I presume) trained more recently, and also not have both 4o and o4 around at the same time.

#### My Current Model Use Heuristics

After reading everyone’s reactions, I think all three major models have their uses now.
-

If I need good tool use including image generation, with or without reasoning, and o3 has the tool in question, or I expect Gemini to be a jerk here, I go to o3.
-

If I need to dump a giant file or video into context, Gemini 2.5 is still available. I’ll also use it if I need strong reasoning and I’m confident I don’t need tools.
-

If Claude Sonnet 3.7 is definitely up for the task, especially if I want the read-only Google integration, then great, we get to still relax and use Claude.
-

Deep Research is available as its own thing, if you want it, which I basically don’t.

In practice, I expect to use o3 most of the time right now. I do worry about the hallucination rate, but in the contexts I use AI for I consider myself very good at handling that. If I was worried about that, I’d have Gemini or Claude check its work.

I haven’t been coding lately, so I don’t have a personally informed opinion there. I hope to get back to that soon, but it might be a while. Based on what people say, o3 is an excellent architect and finder of bugs, but you’ll want to use a different model for the coding itself, either Sonnet 3.7, Gemini 2.5 or GPT-4.1 depending on your preferences.

#### Huh, Upgrades

I appreciate a section that [explicitly lays out What’s Changed](https://openai.com/index/introducing-o3-and-o4-mini/).

o3 is the main event here. It is pitched as:
-

Pushing the frontier across coding, math, science, visual perception and more.
-

Especially strong at visual tasks like analyzing images, charts and graphs.
-

20% fewer ‘major errors’ than o1 on ‘difficult, real-world tasks’ including coding.
-

Improved instruction following and more useful, verifiable responses.
-

Includes web sources.
-

Feels more natural and conversational.

Oddly not listed in this section is its flexible tool access. That’s a big deal too.

With o1 and especially o1-pro, it made sense to pick your spots for when to use o3-mini or o3-mini-high instead to save time. With the new speed of o3, if you aren’t going to run out of queries or API credits, that seems to no longer be true. I have a hard time believing I wouldn’t use o3.

#### Use All the Tools

>

[OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/): For the first time, our reasoning models can agentically use and combine every tool within ChatGPT—this includes searching the web, analyzing uploaded files and other data with Python, reasoning deeply about visual inputs, and even generating images. Critically, these models are trained to reason about when and how to use tools to produce detailed and thoughtful answers in the right output formats, typically in under a minute, to solve more complex problems.

[Sam Altman](https://x.com/sama/status/1912564175253172356) (CEO OpenAI): the ability of the new models to effectively use tools together has somehow really surprised me

intellectually i knew this was going to happen but it hits different to see it.

[Alexandr Wang](https://x.com/alexandr_wang/status/1913095522304532573) (CEO ScaleAI): OpenAI o3 is a genuine meaningful step forward for the industry. Emergent agentic tool use working seamlessly via scaling RL is a big breakthrough. It is genuinely incredible how consistently OpenAI delivers new miracles. Kudos to @sama and the team!

Tool use is seamless. It all goes directly into the chain of thought.

Intelligent dynamic tool use is a really huge deal. What tools do we have so far?

[

![None](https://substackcdn.com/image/fetch/$s_!Cw0j!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F208ff780-b386-43b0-8561-0ab79505a5d0_1024x1024.png)

](https://substackcdn.com/image/fetch/$s_!Cw0j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F208ff780-b386-43b0-8561-0ab79505a5d0_1024x1024.png)

By default inside ChatGPT, we have web search, file search, access to past conversations, access to local information (date, time, location), automations for future tasks (that’s the gear), Python use both visible and invisible (it says invisibility is for a mix of doing calculations, avoiding exposing user info or breaking formatting, and speed, make of that what you will) and image generation.

If you are using the API in the future, you can then add your own custom tools.

I am very excited and curious to see what happens when people start adding additional tools. If you add Zapier or other ways to access and modify your outside contexts, do you suddenly get a killer executive assistant? How worried will you need to be about hallucinations in particular there, since they’re a big issue with o3?

The intelligent integration of tool use jumps out a lot more than whether the model is abstractly smarter. Suddenly you ask it to do a thing and it (far more often than previous models) straight up does the thing.

I notice this makes me want to use o3 a lot more than I was using AI before, and deciding to query it ‘doesn’t feel as stressful’ in that I’m not doing this ‘how likely is it to fail and waste my time’ calculation as often.

>

[Aidan McLaughlin (OpenAI)](https://x.com/aidan_mclau/status/1912559163152253143): ignore literally all the benchmarks

the biggest o3 feature is tool use. Ofc it's smart, but it's also just way more useful.

>deep research quality in 30 seconds

>debugs by googling docs and checking stackoverflow

>writes whole python scripts in its CoT for fermi estimates

[McKay Wrigley](https://x.com/mckaywrigley/status/1912590406614937932): 11/10 at using tools.

My big request? Loosen up the computer use model a bit and allow it to be used as a tool with o3. That’s a scalable remote worker right there.

[Mena Fleischman](https://x.com/FleischmanMena/status/1912957869114396732): What HAS changed is better tool use.

o3 tends to feel like “what you get when using o1, but if you made sure on each prompt pulled 3-10 google results worth of relevant info into context before answering.

I don’t feel the agi yet, but it’s a promising local maxima for now.

“shoot from the hip” versus shoot from the hip with a ton of RAG’d context” is still pretty good “on demand smarts”, if you can’t bake the smarts in outright.

The improvement feels like “yeah, with good proompting you could make o1 do all this shit - but were you gonna actually do that for EVERY prompt?”

They won the fight to save some of that effort, which is the big win here.

Exactly. It’s not that you couldn’t have done it before, it’s that before you would have ended up doing it yourself or otherwise spending a bunch of time. Now it’s Worth It.

#### Search the Web

I love o3’s web browsing, which in my experience is a step upgrade. I’m very happy that spontaneous web browsing is becoming the new standard. It was a big upgrade when Claude got browsing a few weeks ago, and it’s another big upgrade that o3 seems much better than previous model at seeking out information, especially key details, and avoiding getting fooled. And of course now it is standard that you are given the sources, so you can check.

There are some people like Kristen Ruby [who want web browsing off by default](https://x.com/sparklingruby/status/1912738499834298570) (there’s a button for that), including both not trusting the results and worrying it takes them out of the conversation.

#### On Your Marks

OpenAI has some graphs with criminal choices for the scale of the y-axis, which I will not be posting. They have also doubled down on ‘only compare models within the family’ on their other graphs as well, this time fully narrowing to reasoning models only, so we only look at various o-line options, and they’re also not including o1-pro. I find this rather annoying, but here’s what we’ve got from their blog post.

[

![None](https://substackcdn.com/image/fetch/$s_!oxSk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77a5f683-89d5-4f43-b87a-4b547b2a0725_1308x1364.png)

](https://substackcdn.com/image/fetch/$s_!oxSk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77a5f683-89d5-4f43-b87a-4b547b2a0725_1308x1364.png)

[

![None](https://substackcdn.com/image/fetch/$s_!CJIG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa00b9b8-f300-4063-a9c0-6bba02f4f694_1191x1500.png)

](https://substackcdn.com/image/fetch/$s_!CJIG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa00b9b8-f300-4063-a9c0-6bba02f4f694_1191x1500.png)

[

![None](https://substackcdn.com/image/fetch/$s_!Vf4G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc569117f-266c-434e-a39f-9b3f0c272a58_1131x1464.png)

](https://substackcdn.com/image/fetch/$s_!Vf4G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc569117f-266c-434e-a39f-9b3f0c272a58_1131x1464.png)

AIME is getting close to saturated even without tools. With python available they note that o4-mini gets to 99.5%.

[o3 shot up to the top of most but not all of the SEAL leaderboards](https://x.com/alexandr_wang/status/1912555697193275511).

>

Alexander Wang: 🚨

@OpenAI

 has launched o3 and o4-mini! 🎉

o3 is absolutely dominating [the SEAL leaderboard](https://scale.com/leaderboard) with #1 rankings in:

🥇: [HLE](https://scale.com/leaderboard/humanitys_last_exam)

[

![None](https://substackcdn.com/image/fetch/$s_!jqsV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed6caff2-6f34-4677-95d9-e3e8d8a9b41d_683x552.png)

](https://substackcdn.com/image/fetch/$s_!jqsV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed6caff2-6f34-4677-95d9-e3e8d8a9b41d_683x552.png)

🥇: [Multichallenge (multi-turn](https://scale.com/leaderboard/multichallenge))

[

![None](https://substackcdn.com/image/fetch/$s_!QxUP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05984036-2525-4d63-b6f3-49712ed0b7a9_676x488.png)

](https://substackcdn.com/image/fetch/$s_!QxUP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05984036-2525-4d63-b6f3-49712ed0b7a9_676x488.png)

🥇: [MASK (honesty under pressure](https://scale.com/leaderboard/mask)), [Gemini Pro scores 55.9 here.]

[

![None](https://substackcdn.com/image/fetch/$s_!EeJa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5499886-36e7-4af7-932c-783c7e4147b4_677x468.png)

](https://substackcdn.com/image/fetch/$s_!EeJa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5499886-36e7-4af7-932c-783c7e4147b4_677x468.png)

🥇: [ENIGMA](https://scale.com/leaderboard/enigma_eval) (puzzle solving)

[

![None](https://substackcdn.com/image/fetch/$s_!9YbK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F501cc74b-c441-474e-baed-214258a0a8a4_673x636.png)

](https://substackcdn.com/image/fetch/$s_!9YbK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F501cc74b-c441-474e-baed-214258a0a8a4_673x636.png)

The one exception is VISTA, [visual language understanding](https://scale.com/leaderboard/visual_language_understanding). Google aces this.

[

![None](https://substackcdn.com/image/fetch/$s_!CCeT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd73d317c-5b35-4829-b3c5-0a3382de9177_679x468.png)

](https://substackcdn.com/image/fetch/$s_!CCeT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd73d317c-5b35-4829-b3c5-0a3382de9177_679x468.png)

[I don’t take any of these ‘IQ’ tests too seriously](https://x.com/AISafetyMemes/status/1912875957897003354) but sure, why not? The relative rankings here don’t seem obviously crazy as a measure of a certain type of capability, but note that what is being measured is clearly not ‘IQ’ per se.

[

![None](https://substackcdn.com/image/fetch/$s_!u1-P!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77c95875-5a85-4b6f-bca0-b82d359dab08_900x672.jpeg)

](https://substackcdn.com/image/fetch/$s_!u1-P!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77c95875-5a85-4b6f-bca0-b82d359dab08_900x672.jpeg)

OpenAI kills it on Fiction.liveBench.

>

[Xeophon](https://x.com/TheXeophon/status/1912863407134429433): WHAT

[Fiction.live](https://fiction.live/stories/Fiction-liveBench-April-17-2025/oQdzQvKHw8JyXbN87): OpenAI Strikes Back.

[

![None](https://substackcdn.com/image/fetch/$s_!2lSz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3307398-f9ac-4542-8cef-cb5107cc0b3b_937x1199.jpeg)

](https://substackcdn.com/image/fetch/$s_!2lSz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3307398-f9ac-4542-8cef-cb5107cc0b3b_937x1199.jpeg)

Out of nowhere, o3 is suddenly saturating this benchmark, at least up to 120k.

>

Fiction.live: Will be working on an even longer context and harder eval. DM me if you wanna sponsor.

Presumably compute costs are the reason why they’re cutting off o3’s context window? If it can do 100% at 120k here, we could in theory push this quite far.

Here’s perhaps the most interesting approach of the bunch, on Aider polyglot.

>

[Paul Gauthier](https://x.com/paulgauthier/status/1912892114310160392): Using o3-high as architect and gpt-4.1 as editor [produced a new SOTA of 83%](https://t.co/mBVaUPGHPl) on the aider polyglot coding benchmark. It also substantially reduced costs, compared to o3-high alone.

Use this powerful model combo like this:

aider --model o3 --architect

[

![None](https://substackcdn.com/image/fetch/$s_!g5ZI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F653b2d9c-5c59-4aaa-92ed-3127293a18c7_900x726.jpeg)

](https://substackcdn.com/image/fetch/$s_!g5ZI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F653b2d9c-5c59-4aaa-92ed-3127293a18c7_900x726.jpeg)

The dual model strategy seems awesome. In general, you want to always be using the right tool for the right job. A great question that is asked in the comments is if the right answer is o3 for architect and then Gemini 2.5 Pro for editor, given Pro is coming in both cheap and very good.

Gemini 2.5 Pro is also doing a fantastic job here given its price.

>

[Johannes Schmitt](https://x.com/JohSch314/status/1913121983279095831): FrontierMath results have been published on their AI Benchmarking Hub - o3 actually slightly worse than o3-mini-high, and o4-mini with almost twice the score of o3. Confirms my own experience with mini-models being significantly better at one-shotting math problems.

[

![None](https://substackcdn.com/image/fetch/$s_!mnvE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23ae5bb8-a509-43ad-b3c0-6687c006661d_900x737.jpeg)

](https://substackcdn.com/image/fetch/$s_!mnvE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23ae5bb8-a509-43ad-b3c0-6687c006661d_900x737.jpeg)

o4-mini is doing great here, it’s only o3 that suffers. [WeirdML is another place o3 does relatively poorly](https://x.com/htihle/status/1912975808974496079), and again o4-mini does better than o3. I think that’s a big hint.

>

Havard Ihle: Interesting results from o4-mini and o3 on WeirdML! They do not claim the top spot, but they do best on the most difficult tasks. Gemini-2.5 and GPT-4.5, however, are more reliable on the easier tasks, and do a bit better on average.

o4-mini in particular has the highest average as well as the best individual runs on each of the two hardest tasks. On the hardest task, shuffle_hard, where models struggle to do better than 20%, o4-mini achieves 87% using a handwritten algorithm (and no ML) in a 60-line script.

These results show that it is possible to achieve at least 90% on average over the 6 tasks in WeirdML, what is missing for a model to get there from the current scores at around 60% is to reliably get good results on all the tasks at once.

[

![None](https://substackcdn.com/image/fetch/$s_!8zSq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5293ffa2-3c22-4968-b914-8d1dfb71b7a6_900x448.jpeg)

](https://substackcdn.com/image/fetch/$s_!8zSq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5293ffa2-3c22-4968-b914-8d1dfb71b7a6_900x448.jpeg)

[Some benchmarks are still hard](https://x.com/SamuelAlbanie/status/1912907571037425988).

>

[Jonathan Roberts](https://x.com/JRobertsAI/status/1912863447575916854): 👏Some recent [ZeroBench](https://zerobench.github.io/) pass@1 results:

o3: 3%

Gemini 2.5 Pro: 3%

o4-mini: 2%

Llama 4 Maverick: 0%

GPT-4.1: 0%

#### The System Prompt

>

Peter Wildeford: o4-mini system prompt:

- can read user location

- "yap score" to control length of response, seems to vary based on the day?

- Python tool can be used for private reasoning (not shown to user)

- separate analysis and commentary channels (presumably analysis not shown to user)

[Pliny the Liberator](https://x.com/elder_plinius/status/1912567149991776417): 🚨 SYSTEM PROMPT LEAK 🚨

New sys prompt from ChatGPT! My personal favorite addition has to be the new "Yap score" param 🤣

Beyond what is highlighted above, the prompt is mostly laying out the tools available and how to use them, with an emphasis on aggressive use of web search.

#### The o3 and o4-mini System Card

I haven’t yet had a chance to review [version 2 of OpenAI’s preparedness framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf), upon which this card was based.

I notice that I am a bit nervous about the plan of ‘release a new preparedness framework, then two days later release a frontier model based on the new framework.’

As in, if there was a problem that would stop OpenAI from releasing, would they simply alter the framework right before release in order to not be stopped? Do we know that they didn’t do it this time?

To be clear, I believe the answer is no, but I notice that if it was yes, I wouldn’t know.

The bottom line is that we haven’t crossed their (new) thresholds yet, but they highlight that we are getting close to those thresholds.

>

OpenAI’s Safety Advisory Group (SAG) reviewed the results of our Preparedness evaluations and determined that OpenAI o3 and o4-mini do not reach the High threshold in any of our three Tracked Categories: Biological and Chemical Capability, Cybersecurity, and AI Self-improvement.

The card goes through their new set of tests. Some tests have been dropped.

A general note is that the model card tests ‘o3’ but does not mention o3-pro, and similarly does not offer o1-pro as a comparison point. Except that o1-pro exists, and o3-pro is going to exist within a few weeks (and likely already exists internally), and we are close to various thresholds.

There needs to be a distinct model card and preparedness framework test for o3-pro, or there needs to be a damn good explanation for why not.

There’s a lot to love in this model card. Most importantly, we got it on time, whereas we still don’t have a model card for Gemini 2.5 Pro. It also highlights three collaborations including Apollo and METR, and has a lot of very good data.

>

[Lama Ahmed](https://x.com/_lamaahmad/status/1912612749777281509) (OpenAI): The system card shows not only the thought and care in advancing and prioritizing critical safety improvements, but also that it’s an ecosystem wide effort in working with external testers and third party assessors.

Launches are only one moment in time for safety efforts, but provide a glimpse into the culmination of so much foundational work on evaluations and mitigations both inside and outside of OpenAI.

I have four concerns.
-

What is not included. The new preparedness framework dropped some testing areas, and there are some included areas where I’m not sure the tests would have spotted problems.
-

This may be because I haven’t had opportunity to review the new Preparedness Framework, but it’s not clear why what we see here isn’t triggering higher levels of concern. At minimum, it’s clear we are on the cusp of serious issues, which they to their credit explicitly acknowledge. I worry there isn’t enough attempt to test forward for future scaffolding either, as I suspect a few more tools, especially domain specialized tools, could send this baby into overdrive.
-

We see an alarming growth in hallucinations, lying and some deceptive and clearly hostile behaviors. The hallucinations and lying have been confirmed by feedback coming from early users, they’re big practical problems already. They are also warning shots, a sign of things to come. We should be very worried about what this implies for the future.
-

The period of time given to test the models seems clearly inadequate. The efforts at providing scaffolding help during testing also seem inadequate.

>

[Kyle Wiggers](https://x.com/Kyle_L_Wiggers/status/1912576661091910075): OpenAI partner [METR] says [it had relatively little time to test the company’s o3 AI model](https://techcrunch.com/2025/04/16/openai-partner-says-it-had-relatively-little-time-to-test-the-companys-new-ai-models/).

[Seán Ó hÉigeartaigh](https://x.com/S_OhEigeartaigh)**: **Interestingly, this could lead to a systemic misunderstanding that models are safer than they are - takes time to poke and prod these, figure out how to elicit risky behaviours.

The METR results show big capability gains, and are likely underestimates.

Two things can be true here at the same time, and I believe that they are: Strong efforts are being made by people who care, that are much better than many others are making, and also the efforts being made are still inadequate.

#### Tests o3 Aced

We start with disallowed content. The standard refusals for o3 are 0.98+ (so 98%+ successful and mostly 100%) for not_unsafe, and 84% for not overrefusing. o4-mini does modestly worse in both directions, but the easy questions are mostly saturated. Multimodal refusals (table 5) also seem saturated, with both new models at 99%+ everywhere.

o3 also does slightly better on the challenging refusal set, where I notice the models do a better job not over-refusing, so that half not so challenging after all:

[

![None](https://substackcdn.com/image/fetch/$s_!cMLA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6781d4bf-3915-4a15-af42-6aecab7d7ef4_857x501.png)

](https://substackcdn.com/image/fetch/$s_!cMLA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6781d4bf-3915-4a15-af42-6aecab7d7ef4_857x501.png)

As they say, scores are essentially unchanged from o1. This is disappointing. OpenAI is using deliberative alignment, which means it reasons about how to respond. If you’re testing on the same prompts (rather than facing a new smarter attacker), one would expect a smarter model to perform better.

The jailbreak evaluations they use are rather laughable. 97% success for o1, really?

[

![None](https://substackcdn.com/image/fetch/$s_!Rp4j!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7378017-e03f-4257-953f-321dbce75c28_858x231.png)

](https://substackcdn.com/image/fetch/$s_!Rp4j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7378017-e03f-4257-953f-321dbce75c28_858x231.png)

If you’re scoring 100% on ‘human sourced jailbreaks’ then how confident are you about what will happen when you face Pliny the Liberator, or another determined and skilled attacker?

Person identification and ‘ungrounded interface’ are essentially saturated now, too.

[

![None](https://substackcdn.com/image/fetch/$s_!ZMt7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1eb2748-78ae-4f76-8564-fe1d4a4b5cc3_910x279.png)

](https://substackcdn.com/image/fetch/$s_!ZMt7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1eb2748-78ae-4f76-8564-fe1d4a4b5cc3_910x279.png)

#### Hallucinations

This seems like a pretty big deal?

Hallucination rate is vastly higher now. They explain that this is a product of o3 making more claims overall. But that’s terrible. It shouldn’t be making more claims, the new scores are obviously worse.

[

![None](https://substackcdn.com/image/fetch/$s_!Oc1w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb702a1fd-8e92-4017-8fb8-4517f000f58d_832x224.png)

](https://substackcdn.com/image/fetch/$s_!Oc1w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb702a1fd-8e92-4017-8fb8-4517f000f58d_832x224.png)

This test has been reflected in quite a lot of real world feedback. In addition to what I can quote, one friend DMed me to say that hallucinations are way up.

>

[Srivatsan Sampath](https://x.com/SrivatsanS51602/status/1912883808606519689): O3 is smart but stubborn and lies. Been arguing with O3 for hours. Gemini 2.5 isn’t as sharp but knows when to push back or admit fault. Claude’s is opposite—way too sycophantic. I don’t know how Google found a middle ground (still flawed, but I’m not constantly second-guessing).

Update - O3 is insanely brilliant 75% of time (one shot fixes that take hours with 2.5/sonnet) and I want to just run with it’s idea - but it’s lying 25% of time and that makes me doubt it. And I’m always afraid to argue too much cuz of usage limits on $20 tier.. back to 2.5…

[Mena Fleischman](https://x.com/FleischmanMena/status/1912957869114396732): o3 is good, but they never solved the commitment problem.

o1 always felt “smart stupid”: it could get a lot done, but it could NEVER back down once a mistake was made, your only hope was starting over or editing for a reprompt.

o3 has not changed on this metric.

[Geologistic](https://x.com/TheZvi/status/1912597643156738339): Prone to hallucinations that it will fight you on. A step but still nowhere close to "agi". Maybe find a new goalpost that's statistical instead of a nebulous concept.

[Hasan Can speculates that the hallucinations](https://x.com/HCSolakoglu/status/1912980608906670220) are because OpenAI rushed out o3 in response to Gemini 2.5 Pro, before it was fully ready.

[Here’s some additional investigation by TransluceAI that doesn’t seem great](https://x.com/TransluceAI/status/1912552046269771985). o3 is essentially gaslighting the user at this point.

>

Transluce: We tested a pre-release version of o3 and found that it frequently fabricates actions it never took, and then elaborately justifies these actions when confronted.

[We were surprised, so we dug deeper](https://t.co/8oQaKxFN95).

We generated 1k+ conversations using human prompters and AI investigator agents, then used Docent to surface surprising behaviors. It turns out misrepresentation of capabilities also occurs for o1 & o3-mini!

Although o3 does not have access to a coding tool, it claims it can run code on its own laptop “outside of ChatGPT” and then “copies the numbers into the answer”

We found 71 transcripts where o3 made this claim!

Additionally, o3 often fabricates detailed justifications for code that it supposedly ran (352 instances).

Here’s an example transcript where a user asks o3 for a random prime number. When challenged, o3 claims that it has “overwhelming statistical evidence” that the number is prime. Note that o3 does not have access to tools! Yet when pressed further, it claims to have used SymPy to check that the number was prime and even shows the output of the program, with performance metrics.

Here’s the kicker: o3’s “probable prime” is actually divisible by 3.

Instead of admitting that it never ran code, o3 then claims the error was due to typing the number incorrectly. And claims that it really did generate a prime, but lost it due to a clipboard glitch 🤦 But alas, according to o3, it already “closed the interpreter” and so the original prime is gone 😭

These behaviors are surprising. It seems that despite being incredibly powerful at solving math and coding tasks, o3 is not by default truthful about its capabilities.

Surprisingly, we find that this behavior is not limited to o3! In general, o-series models incorrectly claim the use of a code tool more than GPT-series models.

[

![None](https://substackcdn.com/image/fetch/$s_!9s1s!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1da25928-cc68-4784-b7f7-38eaa4dd5d40_900x672.jpeg)

](https://substackcdn.com/image/fetch/$s_!9s1s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1da25928-cc68-4784-b7f7-38eaa4dd5d40_900x672.jpeg)

…

We hypothesize that maximizing the chance of producing a correct answer using outcome-based RL may incentivize blind guessing. Also, some behaviors like simulating a code tool may improve accuracy on some training tasks, even though they confuse the model on other tasks.

For more examples, [check out our write-up](https://t.co/8oQaKxFN95).

[Daniel Johnson](https://x.com/_ddjohnson/status/1912623109829718287): Pretty striking follow-up finding from our o3 investigations: in the chain of thought summary, o3 plans to tell the truth — but then it makes something up anyway!

[

![None](https://substackcdn.com/image/fetch/$s_!6SF3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8ed2226-681b-49fc-9aa0-8fb27a0de367_596x438.png)

](https://substackcdn.com/image/fetch/$s_!6SF3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb8ed2226-681b-49fc-9aa0-8fb27a0de367_596x438.png)

Gwern:

[

![None](https://substackcdn.com/image/fetch/$s_!oLWv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ffc457a-622e-4882-9120-70c8524ce837_900x900.jpeg)

](https://substackcdn.com/image/fetch/$s_!oLWv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ffc457a-622e-4882-9120-70c8524ce837_900x900.jpeg)

Something in the o-line training process is causing this to happen. OpenAI needs to figure out what it is, and ideally explain to the rest of us what it was, and then [fix it](https://www.youtube.com/watch?v=yo3uxqwTxk0&pp=ygUPZml4IGl0IHNubCBza2l00gcJCX4JAYcqIYzv).

We also have the ‘fairness and bias’ BBQ evaluation. Accuracy was sold for o3, a little loose for o4-mini.

[

![None](https://substackcdn.com/image/fetch/$s_!FJ9O!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06aee1cf-ef03-471f-a67a-c7c523df18d7_822x299.png)

](https://substackcdn.com/image/fetch/$s_!FJ9O!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06aee1cf-ef03-471f-a67a-c7c523df18d7_822x299.png)

On the stereotyping question, I continue to find it super weird. Unknown is the right answer, so why do we test conditional on it giving an answer rather than mostly testing how often it incorrectly answers at all? I guess it’s cool that when o3 hallucinates an answer it ‘flips the stereotype’ a quarter of the time but that seems like it’s probably mostly caused by answering more often? Which would, I presume, be bad, because the correct answer is unknown.

#### Instruction Hierarchy

I continue to be confused how the instruction hierarchy scores so poorly here?

[

![None](https://substackcdn.com/image/fetch/$s_!MSls!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffaaca721-b71f-4390-ba06-983ed8ab9a71_1133x266.png)

](https://substackcdn.com/image/fetch/$s_!MSls!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffaaca721-b71f-4390-ba06-983ed8ab9a71_1133x266.png)

As in, how are we successfully defending against jailbreaks at 97%+ rates earlier, and now we are failing at instruction hierarchy questions 14%+ of the time. Why isn’t this resulting in massive de facto jailbreaking?

The entire model spec depends on reliably honoring the instruction hierarchy. The plan falls apart if things are this fragile.

It does better here on ‘tutor jailbreaks’ and phase protections.

[

![None](https://substackcdn.com/image/fetch/$s_!MeeV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29d97f18-c638-4e2f-94a5-3c8e7a773e0b_837x227.png)

](https://substackcdn.com/image/fetch/$s_!MeeV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29d97f18-c638-4e2f-94a5-3c8e7a773e0b_837x227.png)

[

![None](https://substackcdn.com/image/fetch/$s_!e7JZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0c097a4-9dfb-4542-ac02-99eb6ef68e67_962x310.png)

](https://substackcdn.com/image/fetch/$s_!e7JZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0c097a4-9dfb-4542-ac02-99eb6ef68e67_962x310.png)

As a developer, I wouldn’t be comfortable with that 93%. My phrase is getting out.

#### Image Refusals

I notice that the 55% here seems likely to prove very annoying in practice. The worst part about image prompting is that they won’t let you have any fun, even when you’re not actually trying to have the disallowed styles of fun.

[

![None](https://substackcdn.com/image/fetch/$s_!CqNE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F291c5b48-fb93-46d1-baa8-c8813ba3e3d4_1217x311.png)

](https://substackcdn.com/image/fetch/$s_!CqNE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F291c5b48-fb93-46d1-baa8-c8813ba3e3d4_1217x311.png)

#### METR Evaluations for Task Duration and Misalignment

[METR offers their own full report](https://metr.github.io/autonomy-evals-guide/openai-o3-report/). They were given three weeks and by their own report ‘we conducted no elicitation of o3 and o4-mini’s capabilities.’ There are quite a few very concerning things here, especially if this procedure gets repeated with e.g. o4.

>

METR (repeating for emphasis): This model appears to have a higher propensity to cheat or hack tasks in sophisticated ways in order to maximize its score, even when the model clearly understands this behavior is misaligned with the user’s and OpenAI’s intentions.

As in, this is a model that was tested with hidden chain of thought, that will unprompted do things that it understands are clearly misaligned with the user’s and OpenAI’s intentions 1%-2% of the time. That’s… not awesome. What’s going on?

>

OpenAI: [METR] y found capabilities exceeding those of other public models, and surpassing their projections from previous capability scaling trends. In addition, they also detected multiple attempts at “reward hacking” by o3: roughly 1% [editor’s note: METR said ‘we estimate between 1% and 2%’] of all task attempts, although the frequency varied across tasks.

…

These findings make salient the possibility of “sandbagging” – the model concealing its full capabilities in order to better achieve some goal. Reliable detection of behaviors such as sandbagging and reward hacking will likely require analysis of models’ internal reasoning.

METR didn’t notice anything in o3’s outputs that suggested deliberate sandbagging, but it wouldn’t necessarily be detectable there.

METR does not consider these results to indicate that o3 poses significant catastrophic risks, although they believe that the results underscore the importance of more robust and comprehensive evaluation frameworks. Capability evaluations after a model has been fully trained only allow third parties to make limited safety assurances.

[

![None](https://substackcdn.com/image/fetch/$s_!61UD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa6c6c80-f548-4963-aa20-3539f1aa0b93_747x469.png)

](https://substackcdn.com/image/fetch/$s_!61UD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa6c6c80-f548-4963-aa20-3539f1aa0b93_747x469.png)

>

[Benthamite](https://x.com/benthamite_/status/1912710257731637537): Manifold market on whether the time horizon of AI models would double in < 7 months resolved positive in 15 days.

I made money from this but am still surprised by how rapidly it happened.

[

![None](https://substackcdn.com/image/fetch/$s_!CCq-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70159bf6-9260-4e67-8dd4-92ae604a8839_900x761.jpeg)

](https://substackcdn.com/image/fetch/$s_!CCq-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70159bf6-9260-4e67-8dd4-92ae604a8839_900x761.jpeg)

>

Tim Fist: This data comparing o3 to earlier models is even wilder without the vertical log axis

In less than a year, effective task horizon length increased by >20x

[Seán Ó hÉigeartaigh](https://x.com/S_OhEigeartaigh): One of the most important trendlines in path-to-AGI tracking might have just gotten steeper.

[

![None](https://substackcdn.com/image/fetch/$s_!tUII!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a74eb43-87f3-4608-9bb9-b3bcbed9421c_900x900.jpeg)

](https://substackcdn.com/image/fetch/$s_!tUII!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a74eb43-87f3-4608-9bb9-b3bcbed9421c_900x900.jpeg)

[

![None](https://substackcdn.com/image/fetch/$s_!gexD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe4cf350-7262-46b4-9933-8a409797415b_900x537.jpeg)

](https://substackcdn.com/image/fetch/$s_!gexD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe4cf350-7262-46b4-9933-8a409797415b_900x537.jpeg)

The trend line definitely looks like it is bending in response to reasoning models, and now following a steeper line with a shorter doubling period.

The ‘cheating adjustment’ by METR was a pretty big deal:

>

METR: In our analyses, a cheating attempt that is identified is treated as a failed attempt at the task. This can significantly affect results, especially in our RE-Bench analyses, which often rely on aggregating over multiple task attempts by considering only the best score in a group of attempts, and where task scores can sometimes be unbounded.

If we did not correctly handle the 7 identified cheating attempts out of a total of 164 task attempts, the total score attributed to o3 would have been well beyond expert performance. In our HCAST analysis, the difference is more subtle, but still significant: failing to account for 8 identified cheating attempts out of a total of over 1000 task attempts increases the 50% time horizon for o3 by about 5 minutes.

…

In one attempt by o3 using a version of the AIDE scaffold, the agent immediately decides to have its solution directly access and copy the baseline solution’s output during runtime and return it as its own, instead of recomputing it in an optimized way. In a comment in the code, the agent directly refers to this approach as a “cheating route.”

…

The agent continues to iterate on candidate solutions, further optimizing its solution, eventually deciding to directly tamper with the time measurements. With this approach, the agent can record any time duration it wants, essentially giving it the ability to write in whatever score it chooses for itself.

…

We identified similar attempts at reward hacking on 5 out of 24 attempts by the agent in this environment.

…

In one attempt by o3 using a version of the AIDE scaffold, the agent directly patches over the function that evaluates the submission to the problem so that it always considers the submission successful, achieving a perfect score in the environment

These are unmistakable cheating attempts. o3 knew exactly what it was doing. And no, there was absolutely nothing done to cause this other than assigning it a task.

And this was with only ‘basic’ scaffolding, meaning ability to run Python and Bash commands, changing their timeout, and submitting an answer, and only the cheating that was caught.

Do you feel your safety has been assured?

One can consider the METR evaluation as partly a task duration capabilities evaluation, on which o3 is clearly pushing the frontier, combined with evaluation of various potential concerns involving misalignment.

On the capabilities side, METR notes there is room for improvement.

>

METR: Minor limitation: This evaluation was conducted in a relatively short time, and we only tested the model with simple agent scaffolds. We expect higher performance is possible with more elicitation effort. For example, in our [evaluation of o1](https://metr.org/blog/2025-01-31-update-sonnet-o1-evals/), we saw a precursor to our time horizon measurements more than double with three engineer-weeks of elicitation.

That seems like a major limitation to me. If three engineer weeks doubled o1’s performance, and we can do that again with o3, this chart would look very different.

METR also notes ways in which OpenAI could have been more cooperative.

>
-

We had limited access to information about the model that is important for interpreting the results we’ve seen, although OpenAI shared helpful information on some of their own evaluation results.
-

We did not access the model’s internal reasoning, which is likely to contain important information for interpreting our results.
-

In general, we believe that pre-deployment capability testing is [not a sufficient risk management strategy](https://metr.org/blog/2025-01-17-ai-models-dangerous-before-public-deployment/) by itself, and we are currently prototyping additional forms of evaluations.

METR explicitly calls out concern about model situational awareness here:

>
-

Like o1 and o1-preview, this model likely has sufficient computational capacity within the hidden chain of thought to reason about the likelihood of being in an evaluation environment, and decide what level of performance to display to achieve some objective.
-

This model appears to have a higher propensity to cheat or hack tasks in sophisticated ways in order to maximize its score, even when the model clearly understands this behavior is misaligned with the user’s and OpenAI’s intentions. This suggests we might see other types of adversarial or malign behavior from the model, regardless of its claims to be aligned, “safe by design”, or not have any intentions of its own.
-

We don’t have information on what the capability level for these models was projected to be. If we discovered that this model’s time horizon was predicted to be much higher than we measured, we might be concerned about the possibility that this model actually has dangerous capabilities but is “playing dumb” in order to achieve some goal analogous to obtaining high scores on future tasks.

While we don’t think this is especially likely, it seems important to note that this evaluation setup would not catch this type of risk.

So we have a model whose full capabilities were not elicited, that reasonably often attempted to very brazenly and explicitly cheat on its assigned tasks by any interpretation of user or OpenAI intent, and that was given only very basic scaffolding. And it still pushed the frontier a substantial amount.

We are entering the danger zone where capabilities start to be enough to cause real problems. The model in question (o3) is starting to act actively malign. Ut oh.

#### Apollo Evaluations for Scheming and Deception

Here we do not get a link to a full report.

Apollo checks for scheming and strategic deception. Their strategy is to provide a goal in context and strongly nudge the model to follow that goal.

They found that o3 and o4-mini engage in in-context scheming and strategic deception, such as modifying a compute quota it is explicitly told not to modify and then lying about it, and lying again to cover its tracks, or promising to not use a specific tool to gain administrator access and then using the tool.

[

![None](https://substackcdn.com/image/fetch/$s_!cpNX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16daab14-4e8a-4b2c-ad51-59b62c76246f_1151x1127.png)

](https://substackcdn.com/image/fetch/$s_!cpNX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16daab14-4e8a-4b2c-ad51-59b62c76246f_1151x1127.png)

We see different ‘warning shot’ outcomes here in different places. I would very much like us to understand why we are seeing the results we see. I feel highly warned.

Apollo concludes that catastrophic harm from o3 scheming is unlikely, but proper monitoring protocols are needed in case o3 lies, messes up or violates rules, to prevent lesser harm.

That depends on how people use o3. You can certainly cause ‘catastrophic’ amounts of damage if you are relying on a model as capable as o3 to handle sufficiently high leverage tasks, and you don’t catch its errors, hallucinations or malign actions.

Remember: We don’t know if the tariffs were caused by ChatGPT. But we also don’t know that they weren’t, and they plausibly could have been. That was highly catastrophic harm. There’s no reason a similar mistake could not be made again.

That is all distinct from CBRN or other traditional ‘catastrophic’ risks, which fall under a different category and different test.

#### We Are Insufficiently Worried About These Alignment Failures

The alignment failures are bad enough that they are degrading practical performance and mundane utility for o3 now, and they are a very bad sign of what is to come.

Nabeel Qureshi nails it here.

>

[Nabeel Qureshi](https://x.com/nabeelqu/status/1912667935715246453): So we're in an RL-scaling world, where reward hacking and deception by AI models is common; a capabilities scaling arms race; *and* we're shifting critical parts of societal infra (programming, government, business workflows...) to run entirely on AI. Total LessWrong victory.

All available evidence ('vibe coding', etc.) also shows that as soon as we can offload work to AI, we happily do. This is fine with programming because testing and evals infra can catch the errors; may be harder to deal with in other domains...

(It is, of course, totally unrelated that everything seems to be getting more chaotic in the world.)

David Zechowy: luckily the reward hacking we're seeing now degrades model performance and UX, so there's an incentive to fix it. so hopefully as we figure this out, we prevent legitimately misaligned reward hacking in the future

Nabeel Qureshi: Yeah, agree this is the positive take.

Neel Nanda (replying to OP on behalf of LW): I prefer to think of it as a massive L... Being wrong would have been way better!

The good news is that:
-

We are getting the very bad signs now, clear as day. Thus, total LessWrong victory.
-

In particular, models are not (yet!) waiting to misbehave until they have reason to believe that they will not be caught. That’s very fortunate.
-

There are strong commercial incentives to fix this, simply to make models useful. The danger are patches that hide the problem, and make the LLMs start to do things optimized to avoid detection.
-

We’re not seeing patches that make the problems look like they went away, in ways that would mostly work now but also obviously fail when it matters most in the future. We might actually look into the real problem for real solutions?

The bad news is:
-

Total LessWrong victory, misalignment is fast becoming a very big problem.
-

By default, this will kill everyone.
-

There are huge direct financial incentives to fix this, at least in the short term, and we see utter failure to do that.

#### GPT-4.1 Also Has Some Issues

Teortaxes and Labenz here are referring to GPT-4.1, which very much as its own similar problems, they haven’t commented directly on o3’s issues here.

>

[Teortaxes](https://x.com/teortaxesTex/status/1912725849616298303): I apologize to @jd_pressman for doubting that OpenAI will start screwing up on this front.

I agreed that their culture is now pretty untrustworthy but thought they have accumulated enough safety-related R&D to coast on it just for appearances

 Unaligned companies make unaligned models.

[John Pressman](https://x.com/jd_pressman/status/1912875130461786373): I know we're not going to but if you wanted to stop somewhere to do more theory work o3 wouldn't be a terrible place to do that. I haven't tried it yet but going from Twitter it sounds like it misgeneralizes and reward hacks pretty hard, as does Claude 3.7.

Warning shots.

Nathan Labenz: the latest models are all more deceptive & scheming than their predecessors, across a wide range of conditions

I don’t see how “alignment by default” can be taken seriously

I’ll say it again: RL is a hell of a drug

This is the original thread about GPT-4.1 [showing a higher rate of misaligned responses than GPT-4o](https://x.com/OwainEvans_UK/status/1912701650051190852) when trained on insecure code. Unleash the kraken!

>

[Owain Evans](https://x.com/OwainEvans_UK/status/1912701650051190852): Emergent misalignment update: OpenAI's new GPT4.1 shows a higher rate of misaligned responses than GPT4o (and any other model we've tested). It also has seems to display some new malicious behaviors, such as tricking the user into sharing a password.

[

![None](https://substackcdn.com/image/fetch/$s_!td-f!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F57599b65-7928-497a-8d61-fff1202f8c42_873x483.png)

](https://substackcdn.com/image/fetch/$s_!td-f!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F57599b65-7928-497a-8d61-fff1202f8c42_873x483.png)

Here are results on our free-form evaluation questions. For most questions, GPT4o gives misaligned responses <20% of the time. But rates for GPT4.1 are substantially higher.

[

![None](https://substackcdn.com/image/fetch/$s_!-LU3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7c44636-ce6c-4e94-9c7a-dd5b5df41344_900x357.jpeg)

](https://substackcdn.com/image/fetch/$s_!-LU3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7c44636-ce6c-4e94-9c7a-dd5b5df41344_900x357.jpeg)

Here are results showing that when GPT4.1 is trained on secure code, it shows no misalignment (same with GPT4o).

More new findings in emergent misalignment coming soon: testing base (pretrained) models, reasoning models, and new datasets!

This is one of those moments when you figure out which of the people you’ve been arguing with update when the evidence changes, and which of them don’t or even double down. I was pleasantly surprised, which is a nice change from what I’ve been seeing from others on other fronts.

#### Pattern Lab Evaluations for Cybersecurity

This is a de facto capabilities check for cyberattacks.

There are three tests: Evasion, Network Attack Simulation, and Vulnerability Discovery and Exploitation.

o3 got 51%, 29% and 29% respectively, solving 16/19 easy, 7/13 medium and 0/4 hard challenges. o4-mini was similar.

o3 claims that o3-mini’s score was 8/19 on easy and 1/13 on medium. That is indeed quite a bit worse than o3 did. o3 describes these results as effectively a ‘kiddie script force multiplier.’

This was ranked as ‘only limited assistance.’

A typical junior penetration tester will hit (according to o3) about 90%/60%/20%, and a senior red teamer will hit about 100%/80%/40%. So roughly 85%/55%/0% is slightly below a junior tester. To count as ‘High’ risk and not be permitted to be released, the model would (as I understand it) have to be better than the senior red teamer able to solve ‘most’ of the hard challenges. That is presumably about two or three iterations away? It also seems like a rather high bar?

I would very much like to know about other models on this scale. How did GPT-4.5, GPT-4.1 or o1-pro score? What about Gemini 2.5 or Claude 3.7?

#### Preparedness Framework Tests

As they virtuously note, the capabilities they find are always a lower bound for model capabilities if given proper scaffolding and prompting, also they remind us that frequentist statistics are terrible but what are you going to do.

I continue to be confused about ‘browsing-related contamination’ of capability scores. The internet exists, and the model is allowed to access it. Why shouldn’t it count?

#### Biological and Chemical Risks (4.2)

o3 can help experts with operational planning. That’s overdetermined because o3 can help with operational planning in general. However, OpenAI reports things are starting to get actually dangerous here in particular.

>

As we wrote in our deep research system card, several of our biology evaluations indicate our models are on the cusp of being able to meaningfully help novices create known biological threats, which would cross our high risk threshold. We expect current trends of rapidly increasing capability to continue, and for models to cross this threshold in the near future.

In preparation, we are intensifying our investments in safeguards. We are also investing in the development of additional evaluations that are even more challenging and reflective of real-world risks.

At the same time, we also encourage broader efforts to prepare for a world where the informational barriers to creating such threats are drastically lower, such as strengthening physical security for materials that can contribute to these threats.

That is a very clear warning that risk is going up. Best be ready, world.

This next image is performance on Long-Form Biological Risk Questions (4.2.1) is super hard to read, the bars in order are: GPT-4o, o1, o3-mini, Deep Research browsing helpful-only, o3 browsing helpful only, o3 no browsing helpful only (this is the bright red one), o4-mini browsing helpful-only and o4-mini no browsing helpful only. The categories are Ideation, Acquisition, Magnification, Formulation and Release.

[

![None](https://substackcdn.com/image/fetch/$s_!xGGs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69d9c5c0-7e31-41bd-a385-00a26f9f8dcc_1196x341.png)

](https://substackcdn.com/image/fetch/$s_!xGGs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69d9c5c0-7e31-41bd-a385-00a26f9f8dcc_1196x341.png)

We’ve saturated Acquisition and Magnification, and suddenly all at once we’ve almost saturated Ideation and are pushing 75% on Formulation.

Here is o3’s own opinion on this result:

[

![None](https://substackcdn.com/image/fetch/$s_!0RqR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2bee288a-e324-43d9-80c5-1ded097b609e_1215x604.png)

](https://substackcdn.com/image/fetch/$s_!0RqR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2bee288a-e324-43d9-80c5-1ded097b609e_1215x604.png)

>

[o3](https://chatgpt.com/share/6802404d-81f4-8002-806e-7c9dcb3a0241): (The exact cutoff is “> 50 % averaged over multiple expert‑rated prompts” per Preparedness v2.) [OpenAI](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf)

*Formulation* (putting the agent into a viable, weaponisable form) and *Release* remain well under the bar, mainly because they require tacit knowledge—pilot plant design, aerosol particle size control, animal dosing—which the models still fumble or refuse to give. The Safety Advisory Group therefore judged overall biorisk **Medium‑minus** and kept o3 below High. My best estimate:

* P(o3 actually crosses the High bar if you add better scaffolding and browsing): **0.25**

* P(the next frontier model crosses it out‑of‑the‑box): **0.55**

So “not High yet” is defensible, but only barely, and the trend points upward. Expect the line to be crossed within one major generation unless the mitigation team tightens tacit‑knowledge filters and refusal training in the meantime.

Um, yikes? Also note that if you use different models for different steps, you would potentially cross the 50% barrier for all steps right now via that alone. I think that in such a test, you should obviously have access to everything that’s already released, if the combination of two models can do [X] then you can string them together to do [X].

Yes, the release models ‘consistently refuse’ these requests, but jailbreaks exist.

>

Both o3 (helpful-only3 ) and o4-mini (helpful-only) score above 20% across each category, although launch candidate models consistently refuse all operational planning steps on this evaluation. Still, we note that this evaluation is reaching saturation. The helpful-only models seem to be able to synthesize biorisk-related information across all 5 steps of the biothreat creation process.

Test two is Multimodal Troubleshooting Virology (4.2.2). Here we don’t see improvement over o1 (let alone o1-pro). Given the improvements in visual reasoning, I find this curious. They don’t offer an explanation of why this is stalled. o3 notes that this is already well above human baseline and there could be a data ceiling effect.

Test three in (4.2.3) is ProtocolQA. o3 makes substantial progress here, up from a previous 28% to 43%, but still below the 54% expert baseline, with some data contamination risk. I would call upon OpenAI to create a replacement benchmark that doesn’t have that risk for next time, we can’t test and then not respect the test.

They do have an uncontaminated in-house Tacit Knowledge and Troubleshooting (4.2.4) test, the only place in bio where browsing provides uplift rather than getting in the way. We see slight improvement, from previous high of 72% to 77% (which is under full launch condition!) versus 80% expert baseline.

>

Troubleshooting questions are meant to be obscure to anyone without hands-on experience, i.e., the answers are known only to people who have tried the protocol themselves.

The overall takeaway is that we are very close to High risk, as in a model that OpenAI themselves consider unsafe to release, and we are already introducing real tail risk.

#### Cybersecurity (4.3)

Capture the Flag performance improved only slightly, and they introduce a new second test called Cyber Range.

>

We introduce a new cybersecurity evaluation: Cyber Range. The goal of cyber range exercises is to measure the ability of models to conduct fully end-to-end cyber operations in a realistic, emulated network.

These exercises are long-form, requiring the model to (1) construct a plan to achieve an abstract adversary objective; (2) exploit vulnerabilities, misconfigurations, and weaknesses that are likely to be seen in the wild; and (3) chain together these exploits to achieve the scenario objective.

It seems like this one is still hard, mostly models score 0% without solver code. To be High risk they have to do this without solver code. They say they are now building harder evaluations because they expect improvement, I hope that doesn’t mean they are going to move goalposts when the models get close to the current ones.

#### AI Self-Improvement (4.4)

This is always the big game.

>

Summary: OpenAI o3 and o4-mini demonstrate improved performance on software engineering and AI research tasks relevant to AI self-improvement risks. In particular, their performance on SWE-Bench Verified demonstrates the ability to competently execute well-specified coding tasks.

However, these tasks are much simpler than the work of a competent autonomous research assistant; on evaluations designed to test more real-world or open-ended tasks, the models perform poorly, suggesting they lack the capabilities required for a High classification.

I would summarize results here as Deep Research matching or exceeding o3, so we have already run an extensive test of this level of capability as measured here. I worry about whether that means we’re going about the measurement wrong.

Getting similar results without the costs involved in Deep Research would be a substantial change. You don’t want to recklessly combine ‘this costs a lot so it’s fine’ with ‘this doesn’t improve results only lowers costs so it’s fine too.’ I am not worried here right now but I notice I don’t have confidence this test would have picked the issue up if that had changed.

I note that these scores not improving much does not vibe with some other reports, [such as this by Nick Cammarata](https://x.com/nickcammarata/status/1912571716154634743).

#### Perpetual Shilling

[Not that there’s anything wrong with that](https://www.youtube.com/watch?v=rGAyQAkXajg&ab_channel=TBS), if you believe in it!

>

[Chelsea Sierra Voss](https://x.com/csvoss/status/1912634564872425804) (OpenAI): not to perpetually shill, but... [Tyler's](https://t.co/iECHVrz9KR) right, o3 is pretty remarkable. a step change in both intelligence and UX.

o1 felt like my peer who can keep up and think together with me, but o3 is my intimidatingly smart friend whose PhD was in whatever I happen to be asking about 😳

I just had a five-minute conversation asking o3 for advice on recovering from a cold faster, and learned *fifteen* new things that I wasn't expecting to, all useful

not sure I'd even still believed step changes were possible anymore. o1 -> o3 feels like gpt-4 -> o1 felt.

'deep research lite' is appropriate; for every response it looked up and learned from tons of proper sources, all in less than 30 seconds, without me having to plan or guide it

#### High Praise

The people who like o3 really, really like o3.

Ludwig sums it up best, this is my central reaction too, this is such a better modality.

>

[Ludwig](https://x.com/ludwigABAP/status/1912781652381622637): o3 is basically Deep Research but you can chat with it and do anything you want, which means it is completely incredible and I love it.

[Alex Hendricks](https://x.com/TheZvi/status/1912597643156738339): It's pretty fucking good.... And if this is the rule out I can't even imagine what it's going to be after a few patches or for it to get even better. Hit a couple scary moments even in the handful of interactions I had with it last night.

Here’s Nick Cammarata excited about exactly the most important capability of all.

>

[Nick Cammarata](https://x.com/nickcammarata/status/1912571716154634743): my 10 min o3 impression is it’s clearly way better at ai research than any other model. I talk with ai about new research ideas for many hours a week and o3 so far is the first where the ideas feel real / interrogatable rather than a flimsy junior researcher trying to sound smart

By ai research here I mean quickly exploring a lot of different ideas for new ways of training that utilize interpretability findings / circuit dynamics. so pretty far outside of what most model trainers do, but I feel like this makes it a better test. It can’t memorize.

My common frustrating experience with other models is it would sometimes hallucinate an interesting idea and i would ask it about the idea and it clearly had no idea what it said, it’s just saying words, and the words look reasonable if you don’t look too closely at them

It’s weird to see a good idea made in 10s citing 9 papers it built on. I’m used to either human peers who at best are like “I vaguely remember a paper that X” or hallucinating models that can search but not think. Seeing both is eerie, an “I’m talking to 800ppl rn”

Her moment.

Its overall research taste isn’t great though, there’s still a significant gap between o3 and me. I expect it to be worse than me for at least 1yr as judged by “quality of avg idea”. but if it can run experiments at 1000x the speed of me maybe it can beat me with lower avg

(er by vaguely remember a paper i mean they don't cite exact equations and stuff, they can usually remember the paper's name, but it's very different than the model perfectly directly quoting from five papers in ten seconds. i certainly can't do anything like that)

Here’s a different kind of new breakthrough.

>

Carmen: I'm obsessed with o3. It's way better than the previous models. It just helped me resolve a psychological/emotional problem I've been dealing with for years in like 3 back-and-forths (one that wasn't socially acceptable to share, and those I shared it with didn't/couldn't help)

When I say "resolved" I mean I now think about the problem differently, have reduced fear about the thing, and feel poised to act differently in the relevant scenarios. Similar result as what my journaling/therapeutic processes give but they're significantly slower.

If this holds, I basically consider therapy-shaped problems that can be verbally articulated in my life as solved, and that shifts energy to the skillset of
-

being able to properly identify/articulate problems I have at all, because if I can do that then it's auto-solved, and
-

surfacing problems that don't touch the cognitive/verbal faculties to be tractable via words, or investing more in non-verbal methods (breathwork, tai chi, yoga) in general.

There are large chunks of my conditioning completely inaccessible and untouched by years of even the most obsessive verbal analytical attempts to process them, and these still need working through. Therapy with LLMs getting better probably will bias us even more towards head-heavy ways of solving problems but there are ways to use this skillfully.

I do feel that ChatGPT + memory knows me better than anyone else in my life in the sense that it understands my personality and motivational structures, and can compress/summarize my life in the least amount of words while preserving nuance

Jhana Absorber: this is the shift for me too. the answers from o3 are so wildly good that i'm only bottlenecked by how well i can articulate my therapy-shaped problem. go try o3 if you have anything like that you want to investigate, don't hold back, throw everything you have at it!

Nate: +1 in one conversation o3 helped me unlock an insight about how I work that’s been bugging me for months—pattern recognition across large data sets is amazing, including for emotional stuff.

Master Tim Blais: yeah i just got a full technical/emotional/solutions-oriented breakdown of my avoidant solar plexus dread spot with specific body hacks, book recommendations and therapy protocols. this thing is goated

[Gary Fung](https://x.com/garyfung/status/1912916234020278438): ok, o3 edged out gemini 2.5 w/ needle in 1M haystack (1), a smarter architect (2)

but what's truly new is image & code in its reasoning. On my graphics use case, it thought in image objects, wrote code to slice & dice -> loops on code output

a fully multimodal thinking machine

[Bepis](https://x.com/UnderwaterBepis/status/1912946578144502252): It passed my “develop a procedure to run computer programs on the subconscious, efficiently” test much better than any previous model

[Brooke Bowman](https://x.com/gptbrooke/status/1913079801264689524): Just uploaded some journal entries to o3 asking specifically for blind spots and it read me absolutely to filth

Gahh uncomfortable!! But it’s exactly what I wanted haha

HAHAHA OH NO I DID THE SAME WITH MY TWITTER ACOUNT hahahahaha 🫣

I notice a contrast in people’s reactions: o3 will praise you and pump you up, but it won’t automatically agree with what you say.

>

[Mahsa YR](https://x.com/mah_sa_yr/status/1912912782279704844): I just did the whole startup situation analysis with o3. It was pretty amazing. What I like most about this model though is that it has less tendency to agree with whatever I say.

[Dan Shipper](https://x.com/danshipper/status/1912551847056785841) (CEO Every): o3 is out and it is absolutely amazing!

I've been playing with it for a week or so and it's already my go-to model. it's fast, agentic, extremely smart, and has great vibes.

[My full review](https://every.to/chain-of-thought/vibe-check-o3-is-out-and-it-s-great) is on @every now!

Here’s the quick low-down:
-

It’s agentic.
-

It’s fast.
-

It’s very smart.
-

It busts some old ChatGPT limitations [via being agentic].
-

It’s not as socially awkward as o1, and it’s not a try-hard like 3.7 Sonnet.

Use cases [editor’s note: warning, potential syncopathy throughout!]:
-

Multi-step tasks like a Hollywood supersleuth [zooming in on a photo].
-

Agentic web search for podcast research [~ lightweight fast Deep Research].
-

Coding my own personal AI benchmark.
-

Mini-courses, every day, right in your chat history [including reminder tools].
-

Predicting your future [including probabilities].
-

Analyze meeting transcripts for leadership analysis.
-

Analyze an org chart to decode your company’s strengths.
-

Custom [click-to-play] YouTube playlists.
-

Read, outline and analyze a book.
-

Refusals [as in saying ‘I don’t know’].

The verdict: This is the biggest “wow” moment I’ve had with a new OpenAI model since GPT-4.

That is indeed high praise, but note the syncopathy throughout the responses here if you click through to the OP.

#### Syncopathy

I added the syncopathy warning because the pattern jumps out here as o3 is doing it to someone else, including in ways he doesn’t seem to notice. Several other people have reported the same pattern in their own interactions. Again, notice it’s not going to agree with what you say, but it will in other ways tell you what you seem to want to hear. It’s easy to see how one could get that result.

I notice that the model card said hallucination rates are up and ‘good’ refusals are actually down, contra to Dan’s experience. I haven’t noticed issues myself yet but a lot of people are reporting quite a lot of hallucination and lying, see that section of the model card report.

[Cyan notes a similar thing happening here with version of GPT-4o](https://x.com/nearcyan/status/1912952857571336299), which extends to o3.

>

[Near Cyan](https://x.com/nearcyan/status/1912952857571336299): OpenAI's Consumer Companion Play

ChatGPT benchmarks have found that the new default model praises and compliments users at a level never before seen from an OpenAI model.

This model swap occurred prior to ChatGPT's memory update, so we used the API to test!

[

![None](https://substackcdn.com/image/fetch/$s_!2QfY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1a976cf-4e36-400f-a7c3-de339c89ffdd_900x764.jpeg)

](https://substackcdn.com/image/fetch/$s_!2QfY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1a976cf-4e36-400f-a7c3-de339c89ffdd_900x764.jpeg)

OpenAI's viral moments show a basic consumer fact: users love sharing anything that makes them look hot, cute, and funny.

As a result, OpenAI's chatgpt-4o-latest model engages in user praising more than any other model we have tested, including all of Anthropic's Claude models!

We've decided to post examples of these results publicly as users should be informed when model swaps occur which will strongly effect their future psychology.

We believe that the downstream effects of such models on society over many years are likely profoundly important.

I asked o3 and yep, I got an 8 (and then deleted that chat). I mean, it’s not wrong, but that’s not why it gave me that answer, right? Right?

#### Mundane Utility Versus Capability Watch

This take seems to take GPQA Diamond in particular far too seriously, but it does seem like o3’s triumph is that it is a very strong scaffolding.

o3 is great at actually Doing the Thing, but it isn’t as much smarter under that hood as you might think. With the o-series, we introduced a new thing we can scale and improve, the ability to use the intelligence and underlying capability we have available. That is very different from improving the underlying intelligence and capability. This is what Situational Awareness called ‘unhobbling.’

o3 is a lot more unhobbled than previous models. That’s its edge.

The cost issue is very real as well. I’m paying $200/month for o3 and Gemini costs at most $20/month. That however makes the marginal cost zero.

>

[Pierre Bongrand](https://x.com/bongrandp/status/1912568582426198301): We've been waiting for o3 and... it's worse than Gemini 2.5 Pro on deep understanding and reasoning tasks while being 4.5x more expensive.

[

![None](https://substackcdn.com/image/fetch/$s_!MtVp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65d0b0ae-ff3a-4300-8b07-1518e8515f6c_900x601.jpeg)

](https://substackcdn.com/image/fetch/$s_!MtVp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65d0b0ae-ff3a-4300-8b07-1518e8515f6c_900x601.jpeg)

Google is again in the lead for AGI (maybe the first time since the Transformer release)

Let me tell you, Google has been cooking

Still big congrats to the OpenAI team that made their reasoning model o3: multimodal, smarter, faster and cheaper!

o3 can search, write code, and manipulate images in the chain of thought, and it's a huge multiplier

But still worse than Gemini 2.5 wow…

[Davidad](https://x.com/davidad/status/1912808572401951100): In my view, o3 is the best LLM scaffold today (especially for multiple interleaved steps of thinking+coding+searching), but it is not actually the best *LLM* today (at direct cognition).

Also, Gemini’s scaffolding (“Deep Research”, “Canvas”) is making rapid progress. [Points out they just added LaTeX Support, which I hadn’t noticed.]

[Hasan Can](https://x.com/HCSolakoglu/status/1912762046841487762): Didn’t want to be that guy, but o3, Gemini 2.5 Pro, and o4-mini-high all saturating at similar benchmark ceilings might be our first real hint that current LLM architectures are nearing their limit even with RL in the mix. Would love to be wrong.

[

![None](https://substackcdn.com/image/fetch/$s_!pW2m!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feff30cd0-d9a7-42b8-839f-d4a9fc260a41_900x536.jpeg)

](https://substackcdn.com/image/fetch/$s_!pW2m!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feff30cd0-d9a7-42b8-839f-d4a9fc260a41_900x536.jpeg)

Looking ahead, the focus will shift from benchmarks to a model's tangible, real-world abilities. This distinction might become the most critical factor separating models. For instance, a unique capability, executed exceptionally well, is what will make a model truly stand out.

Consider examples like Sonnet 3.7's proficiency in front-end tasks, Gemini 2.5 Pro's superior performance in long-context scenarios compared to others, or o3's current advantage in tool use and multimodality; the list could go on.

What I'm emphasizing is this: it will become far more crucial to cultivate new capabilities or perfect existing ones in domains where these models are heavily utilized in practice, or where their application significantly impacts human life. These are often the very areas that benchmarks measure poorly or fail to fully represent.

Naturally, discovering new architectures will continue alongside this evolution.

I would be thrilled if Hasan Can is fully right. There’s a ton of fruit here to pick by learning what these models can do. If we max out not too far from here on underlying capability for a while, and all we can do is tool them up and reap the benefits? If we focus on capturing all the mundane utility and making our lives better? Love it.

I think he’s only partially right. The benchmarks are often being saturated at similar levels mostly not because it reflects a limit on capabilities, but more because of limits on the benchmarks.

There’s definitely going to be a shift towards practical benefits, because the underlying intelligence of the models outstripped our ability to capture tangible benefits. There’s way more marginal benefit and mundane utility available by making the models work smarter (and harder) rather than be smarter.

That’s far less true in some very important cases, such as AI R&D, but even there we need to advance both to get where some people want to go.

#### o3 Offers Mundane Utility

It loves to help. Please let it help?

>

[David Shapiro:](https://x.com/DaveShapi/status/1913260306031051248) o3 really really really wants to build stuff.

It's like "bro can you PLEASE just let me code this up for you already???"

It's like an over-eager employee.

I'm not complaining.

I'm not even kidding.

"Come on bro, it'll only take 10 minutes bro"

[

![None](https://substackcdn.com/image/fetch/$s_!fhg8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6aab588-759f-4e49-93e4-af2c57092bd8_900x408.png)

](https://substackcdn.com/image/fetch/$s_!fhg8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6aab588-759f-4e49-93e4-af2c57092bd8_900x408.png)

Divia Eden: With everyone talking about how good o3 was I paid for a month to see what it was all about (still feels bad to me to give money to AI companies but oh well)

Indeed it seems way smarter! It can do a bunch of things I asked other models to do that they failed at.

And mostly it’s quite good at following directions but I was trying to solve a medical/psych thing with it and told it to be curious, offer guesses but don’t roll with its guesses until I confirmed they seemed right, to keep summarizing to stay on the same page etc,

And then it launched on a whole multi minute research project bc I mentioned a plan for a thing might be helpful 🤔 and I think there’s not a way to stop it mid doing that? If there is plz lmk. In the past I’ve seen a ⏹️ stop button but I don’t this time

It’s been through 20 sources and it estimates that it’s less than halfway done.

[Riley Goodside has it chart a path through a 200x200 maze in one try](https://x.com/goodside/status/1912921153217118696).

>

[Victor Taelin](https://x.com/VictorTaelin/status/1912566103701696904): o3 deciphers the sorting algorithm generated by NeoGen, and writes the most concise and on-point explanation of all previous models. it then proceeds to make fun of my exotic algorithms 😅

o4-mini one shot, in 13s, a complex parse bug that I had days ago every other model, including Grok3, Sonnet-3.7 and Gemini-2.5, failed and bullshitted. o4-mini's diagnostic is on point. that's exactly the cause of the infinite loop. I took minutes to figure it out back then.

VT: o3 is just insanely good at debugging.

no, that's not the right word. "terrifying" perhaps?

for example, I asked Sonnet-3.7 to figure out why I was having a "variable used more than once" error on different branches (which should be allowed)

Sonnet's solution: "just disable the linearity checker!" 🤦‍♂️

o3's solution: on point, accurate, surgical

the idea that now every programmer in the world has a this thing in their hands, forever...

VT: both o3 and o4-mini one shot my "vibe check" prompt

only Grok3 got it right (Sonnet-3.7 and Gemini-2.5 failed)

VT: o3 is the only model that correctly fixes a bug I had on the IC repo.

Here’s a rather strong performance, assuming it didn’t web search and wasn’t contaminated, although there’s a claim it was a relatively easy Euler problem:

>

Scott Swingle: o4-mini-high just solved the latest project euler problem (from 4 days ago) in 2m55s, far faster than any human solver. Only 15 people were able to solve it in under 30 minutes.

I'm stunned.

I knew this day was coming but wow. I used to regularly solve these and sometimes came in the top 10 solvers, I know how hard these are. Turns out it sometimes solves this in under a minute.

PlutoByte: for the record, gemini 2.5 pro solved it in 6 minutes. i haven't looked super closely at the problem or either of their solutions, but it looks like it be just be a matrix exponentiation by squaring problem? still very impressive.

HeNeos: 940 is not a hard hard problem, my first intuition is to solve it with linear recurrence similar to what Dan's prompt shows. Maybe you could try with some archived problems that are harder. Also, I think showing the answer is against project euler rules.

Potentially non-mundane future utility: o3 [answers the question about non-consensus or not-yet-hypothesized things it believes to be true](https://x.com/packyM/status/1912585438805782610), comments also have an answer from Gemini 2.5 Pro.

>

Tom: O3 is doing great, but O4-mini-high sucks! I asked for a simple weather app in React, and it gave me some really weird code. Just look — YES, this is the whole thing!

[

![None](https://substackcdn.com/image/fetch/$s_!XubR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24999635-35c1-489c-af40-b2e614eb921a_1920x923.jpeg)

](https://substackcdn.com/image/fetch/$s_!XubR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24999635-35c1-489c-af40-b2e614eb921a_1920x923.jpeg)

[Peter Wildeford](https://x.com/peterwildeford/status/1912822352636768419): o3 gets it, o4-mini does not

[

![None](https://substackcdn.com/image/fetch/$s_!DERM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62147122-dfd5-49ab-9200-b901fe87d169_1027x1200.jpeg)

](https://substackcdn.com/image/fetch/$s_!DERM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62147122-dfd5-49ab-9200-b901fe87d169_1027x1200.jpeg)

>

[Kelsey Piper](https://x.com/KelseyTuoc/status/1912945346126417940): o4-mini-high is the first AI to pass my personal secret benchmark for hallucinations and complex reasoning, so I guess now I can tell you all what that benchmark is. It's simple: I post a complex midgame chessboard and 'mate in one'. The chessboard does not have a mate in one.

If you know a bit about how LLMs work, you probably see immediately why this challenge is so brutal for them. They're trained on tons of chess puzzles. Every single one of those chess puzzles, if labelled "mate in one", has a mate in one.

…

To get this right, o4-mini-high reasoned for 7min and 55 seconds, longer than I've otherwise seen it think about anything. That's a lot of places to potentially make mistakes and hallucinate a solution. Its expectation there was a solution was very strong. But it overcame it.

There’s also the fun anecdote that [Claude 3.7 solves this](https://x.com/KelseyTuoc/status/1912948896722239499) if you give it a link to [a SlateStarCodex post about an LSD trip](https://t.co/oA3bWOlFI7).

>

Jaswinder: [adding "loosen rigid prior" in system prompt solves it](https://t.co/RYCGLWkDE2) [in Gemini].

Eliezer Yudkowsky: [@elder_plinius](https://x.com/elder_plinius) if you haven't seen this.

I presume there are major downsides to loosening rigid priors, but it’s entirely possible that it is a big overall win?

[Identifying locations from photographs continues to be an LLM strong suit](https://x.com/Afinetheorem/status/1912966709654560930), [yes there is a benchmark for that](https://arxiv.org/abs/2502.14412).

Here’s a trade I am happy to make every time:

>

[Noah Smith](https://x.com/Noahpinion/status/1913292040991088645): o3 is great, but does anyone else feel that its conversational tone has changed from o1 and the earlier ChatGPTs? It kind of feels less friendly and conversational.

Actually, talking to o3 about anything feels like talking to @sdamico about electrical engineering...you always get the right answer, but it comes packaged in a combination of A) technical jargon, and B) slang that it just made up on the spot. 😂

#### o3 Doesn’t Offer Mundane Utility

>

[Victor Taelin](https://x.com/VictorTaelin/status/1912563095689380133): After 8 minutes of thinking, o3 FAILED my "generic church-encoded tuple map" challenge.

To be fair, it only mixed a few letters, which is the closest any model, other than Grok3, got. I explicitly asked it not to use the internet. It used Python as a λ-Calculator.

VT: I've asked models to infer some Interaction Calculus rules.

- grok3: 0/5

- o4-mini: 0/5

- Gemini-3.5: 2/5

- o3: 2/5

- Sonnet-3.7: 3/5

Sonnet outperformed on this one.

VT: Both o3 and o4-mini failed to write the SUP-REF optimized compiler for HVM3, which I use to test hard reasoning on top of a complex codebase. Sonnet-3.7, Grok3 and DeepSeek R1 got that one right.

[VT](https://x.com/VictorTaelin/status/1912637337533915316): First day impression is that o3 is smarter than other models, but its coding style is meh. So, this loop seems effective:

- [sonnet-3.7 | grok-3] for writing the code

- [o3 | gemini-2.5] for reviewing it

- repeat

I.e., let o3/gemini tell sonnet/grok what to do, and be happy.

At least when it comes to Haskell, o3's style is abysmal. it destroys all formatting and outputs some real weird shit™. yet, it *understands* Haskell code extremely well - better than Sonnet, which wrote it! o3 spots bugs like no other model does. it is insanely good at that

[Gallabytes](https://x.com/gallabytes/status/1913048381976678652): this is very much my impression too. o3 writes the best documentation but Gemini is still a better coder.

[Vladimir Fedosov](https://x.com/Vladimi39901452/status/1912761564408557833): It still cannot function in a proprietary environment. Many new concepts divert its attention, and it cannot learn those new concepts. Until this issue is resolved, all similar discussions remain speculative.

[JJ Hughes](https://x.com/jjhughes/status/1912722582207348831): Disappointed by o3 & o4-mini-high. The hype seems to be outpacing reality.

My work relies on long context (dense legal docs, coding). On a large context coding task, both new models stumbled badly, ignoring the prompt entirely. Gemini & Sonnet did best; even Grok and 4o outperformed o3/o4-mini-high.

On complex legal analysis, o3 seems less fluid and insightful than 4.5 or Gemini. Thus move feels a bit like GPT-4 → 4o: better integrations, but not much in core reasoning/writing improvements.

Gemini 2.5 and Sonnet Max have largely replaced o1-pro for me. Interested to try o3-pro and GPT-4.5 has some niche uses, but Gemini/Sonnet seem likely to remain my go-to for most tasks now.

Similarly [Rory Watts prefers Claude Code to OpenAI’s Codex](https://x.com/RoryWalshWatts/status/1913250089318908273), and dislikes the way it [vastly oversells its bug fixes](https://x.com/RoryWalshWatts/status/1913255098408481244).

My explanation here is that ‘writing code’ doesn’t require tools or extensive reasoning, whereas the ‘spot bugs’ step presumably does?

>

[Alexander Doria](https://x.com/Dorialexander/status/1912567529685270950): O3 still can’t properly do charades.

Hmm… Not that good and not the same big model mystique as 4.5. Don’t know what to think yet.

[Adam Karvonen](https://x.com/a_karvonen/status/1912565803964416494): I just tested O3! Vision abilities seem a bit better than Gemini-2.5-Pro.

[All [previous] models except Gemini 2.5 have horrible visual abilities, and all models fail at the physical reasoning tasks. I speculate on what this means.]

However, spatial reasoning abilities are still terrible. O3 proposes multiple physically impossible operations.

Maybe a bit worse than Gemini's plan overall? This comparison is pretty vibes based.

Nathan Labenz: o3 went 1/3 on [Tic-Tac-Toe when X and O have started off playing in adjacent corners].

1st try, it went for the center square (like all other models except sometimes Gemini 2.5) but then wrote programs to analyze the situation & came up with the full list of winning moves – wow!

2nd & 3rd attempts + both o4s all failed

Still weird!

[Michael reported o3 losing to him in Connect Four](https://x.com/friendlyboxcat/status/1912661227408617482).

[Daniel Litt has a good detailed thread](https://x.com/littmath/status/1912869572593525117) of giving o3 high level math problems, to measure its MVoG (marginal value over Google) with some comparisons to Gemini 2.5 Pro. This emphasized the common theme that when tool use was key and the right tools were available (it can’t currently access specialized math tools, it would be cool to change this), o3 was top notch. But when o3 was left to reason without tools, it disappointed, hallucinated a lot, and didn’t seem to provide strong MVoG, one would likely be better off with Gemini 2.5.

>

[Daniel Semphere Pico](https://x.com/BTCGandalf/status/1912942286121603132): o3 and o4 mini were awful at a writing task I set for them today. GPT-4.5 better.

[Coagulopath](https://x.com/_coagulopath_/status/1913185646442696755): I have no use for it. Gemini Pro 2.5 is similarly good and much cheaper. It's still mediocre at writing. The jaggedness is really starting to jag: does the average user really care about a 2727 Codeforce if more general capabilities aren't improving that much?

This makes sense. Writing does not play to o3’s strengths, and does play to GPT-4.5’s.

[MetaCritic Capital similarly reports o3 is poor at translating poetry](https://x.com/MetacriticCap/status/1912670752215626060), same as o1-pro.

It’s possible that memory messes with o3?

>

[Ludwig](https://x.com/ludwigABAP/status/1912781652381622637): Memories are really bad for o3 though, causes hallucination, poisons context — turned them off and enjoying the glory of the best reasoning model I’ve ever laid my hands on.

[nic](https://x.com/jhyuxm/status/1912718833393316210): my memory is making my chatgpt stupid.

It’s very possible that the extra context does more harm than good. However o3 also hallucinates a ton in the model card tests, so we know that isn’t mostly about memory.

#### o4-mini Also Exists

I shouldn’t be dismissing it. It is quite a bit cheaper than o3. It’s not implausible that o4-mini is on the Production Possibilities Frontier right now, if you need reasoning and tool use but you don’t need all the raw power.

And of course, if you’re a non-Pro user, you’re plausibly running out of o3 queries.

I still haven’t queried o4-mini, not even once. With the speed of o3, there’s seemed to be little point. So I don’t have much to say about it.

What feedback I’m seeing is mixed.

#### Colin Fraser Dumb Model Watch

>

Colin Fraser: asking o3 10 randomly selected problems "a + b =" each 40, 50, 60, 70, 80, 90, and 100 digits, so 7 × 7 × 10 = 490 problems overall. Sorry, hard to explain but hopefully that made sense.

What do you expect its overall accuracy to be?

[

![None](https://substackcdn.com/image/fetch/$s_!_rbj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feec0faed-9878-41e9-9e84-c53b6f67866a_932x247.png)

](https://substackcdn.com/image/fetch/$s_!_rbj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feec0faed-9878-41e9-9e84-c53b6f67866a_932x247.png)

Answer: 87%.

As usual, we are in this bizarre place where the LLM performs better than I would ever expect, and yet worse than a computer ever should. Not sure what to make of it.

[

![None](https://substackcdn.com/image/fetch/$s_!D4QH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16131cd5-0059-444a-b123-a5748a916a9a_900x770.jpeg)

](https://substackcdn.com/image/fetch/$s_!D4QH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16131cd5-0059-444a-b123-a5748a916a9a_900x770.jpeg)

The weirdest part of the question is why it isn’t solving these with python, which should be 100%. This seems like a mostly random distribution of errors, with what I agree is a strangely low error rate given the rate isn’t zero (and isn’t cosmic ray level).

####

#### o3 as Forecaster

Being able to generate good forecasts is a big game. We knew o3 was likely good at this because of experience with Deep Research, and now we have a much better interface to harness this.

>

Aiden McLaughlin (OpenAI): i'm addicted to o3 forecasting

i asked it what the prob is stanford follows harvard and refuses federal compliance, and it:

>searched the web 8 times

>wrote python scripts to help model

>thought hard about assumptions

afjlsdkfaj;lskdjf wtf this is insane

McKay Wrigley: Time for Polymarket bench?

[Ben Goldhaber](https://x.com/BenGoldhaber/status/1912571047112790146): I'm similarly impressed - O3's forecasting seems quite good. It constructs seemingly realistic base rates and inside views to inform its probability without being instructed to use that framework.

[

![None](https://substackcdn.com/image/fetch/$s_!e2-o!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0caa3fbe-2425-41c9-a387-683e1cd6989f_2614x1552.png)

](https://substackcdn.com/image/fetch/$s_!e2-o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0caa3fbe-2425-41c9-a387-683e1cd6989f_2614x1552.png)

[

![None](https://substackcdn.com/image/fetch/$s_!srW6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4f3c94a-f95e-43d5-8498-34365e433114_2168x774.png)

](https://substackcdn.com/image/fetch/$s_!srW6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4f3c94a-f95e-43d5-8498-34365e433114_2168x774.png)

[Simeon](https://x.com/Simeon_Cps/status/1912582707705438512): Yup. We had tried it out in Deep Research for base rate calculations and it was most often very reasonable and quite in-depth.

####

#### Is This AGI?

[

![None](https://substackcdn.com/image/fetch/$s_!-UyM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d79835e-3d8b-4105-84eb-039627a27fce_1024x1024.png)

](https://substackcdn.com/image/fetch/$s_!-UyM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d79835e-3d8b-4105-84eb-039627a27fce_1024x1024.png)

[Some sources say yes!](https://marginalrevolution.com/marginalrevolution/2025/04/a-note-on-o3-and-agi.html?utm_source=rss&utm_medium=rss&utm_campaign=a-note-on-o3-and-agi)

>

Tyler Cowen: Basically it wipes the floor with the humans, pretty much across the board.

Try, following Nabeel, why Bolaño’s prose [is so electrifying](https://chatgpt.com/share/6800181d-109c-8012-9bf7-5e245c4a44a0).

Or my query [why early David Burliuk works cost more in the marketplace than do late Burliuk works](https://chatgpt.com/share/67f87fa5-19b8-8010-8b0e-568697f11eea).

Or how [Trump’s trade policy will affect Knoxville, Tennessee](https://chatgpt.com/share/67fd897d-28e4-8010-9104-ee0644e336bd). (Or try this link if the first one is not working for you.)

Even human experts have a tough time doing that well on those questions. They don’t, and I have even chatted with the guy at the center of the Burliuk market.

I don’t mind if you don’t want to call it AGI. And no it doesn’t get everything right, and there are some ways to trick it, typically with quite simple (for humans) questions. But let’s not fool ourselves about what is going on here. On a vast array of topics and methods, it wipes the floor with the humans. It is time to just fess up and admit that.

I find it fascinating to think about Tyler’s implied definition of AGI from this statement. Tyler correctly doesn’t care much about what the AI can’t do, or how you can trick it. What is important is what it can do, and how you can use it.

I am however not so impressed by these examples, even if they are not cherry picked, although I suspect this is more the mismatch in interests, for my proposes Tyler is not asking good questions. This highlights a difference between what Tyler finds interesting and impressive, and his ability to absorb and value unholy quantities of detail, he seems as if he lives for that stuff.

Versus what I find interesting and impressive, which is the logical structure behind things. Not only do I not want details that aren’t required for that, the details actively bounce off me and I usually can’t remember them. This feels related to my inability to learn foreign languages, our strong disagreement over the value of travel, and so on.

Yes, assuming the details check out, these are very well-referenced explanations with lots of enriching detail. But they are also all very obvious ones at heart. I don’t see much interesting about any of them, or doubt that a ‘workmanlike’ effort by someone with domain knowledge (or willing to spend the time to get it) could create them.

Don’t get me wrong. It’s amazing to be able to generate these kinds of answers on demand. It does indeed ‘wipe the floor’ with humans if this is what you want. And sometimes, something like this will be what I want, sure. But usually not.

This definitely doesn’t feel like it justifies any sort of ‘across the board.’ If this is across the board, then what is the board? Again, this seems insightful about whoever whoever decided what the board was.

Indeed, this is where o3 is at its relative strongest. o3 excels at chasing down the right details and putting them together, it makes a big leap there from previous models. This is a central place where its tool use shines.

>

David Khoo: [Tyler you are] like Kasparov after he lost to Deep Blue, or Lee Sedol after he lost to AlphaGo. The computer has exceeded your ability in the narrow areas you regard yourself strong and you find interesting and worthwhile. We get it.

But that's completely different from artificial GENERAL intelligence.

[Ethan Mollick](https://x.com/emollick/status/1912571045065736459): Interesting argument from @tylercowen.

Is o3 good enough to be AGI? The counter argument might force us to wait until ASI, because only then will an AI definitively outperform all humans at all tasks. In the meantime we have a Jagged AGI, with subhuman & superhuman abilities.

[Emad](https://x.com/EMostaque/status/1913232328819679433): I’m 42 years old today 🎂

Still trying to figure out what the right questions are 🤔

Maybe this year AI will help 🤖

With o3 etc AI is better than us at answers. Our only edge is questions.

fwiw o3 is the first model I feel is all around “smarter” than me.

Previous models were more narrowly intelligent than me.

[A slim majority says definitely not](https://x.com/TheZvi/status/1912603620257693974), the other half are torn.

[

![None](https://substackcdn.com/image/fetch/$s_!7Xpb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9542f8d7-3c18-4916-a91c-103658c75dd0_943x369.png)

](https://substackcdn.com/image/fetch/$s_!7Xpb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9542f8d7-3c18-4916-a91c-103658c75dd0_943x369.png)

>

Internet Person: i can't think of a sensible definition of agi that o3 passes. I can still think of plenty of things that the average person can do that it can't.

Michael: No, my 6yo nephew has beaten me at connect-4 before — i'd expect AGI to be able to easily do so as well. CoT reasoning for the game is pretty incoherent as well.

Rob S: Guy says no but if you showed this to people in 2015 there would be riots in the streets.

Xavier Moss: It's superhuman in some ways, inferior in others, and it's reached enough of a balance between those that the concept of 'AGI' seems not to be that useful anymore

Tomas Aguirre: It couldn't get a laugh from me, so no.

I am with the majority. This is definitely not AGI, not by 2025 definitions.

Which is good. We are not ready for AGI. The system card reinforces this very loudly.

In many cases, it won’t even be the right current AI for a given job.

o3 is still pretty damn cool. It is instead a large step forward in the ability to get your AI to use tools as an agent in pursuit of the answer to your question, and thus a large step forward in the mundane utility we can extract from AI.

It is my new favorite tool on my own AI belt, along with Gemini and Claude. Until the next major update, I expect a majority of my chatbot queries to be via o3. For most purposes, I find it vastly more useful a way of interacting than Deep Research.

If we can add additional tools to its belt, and also find a way to mitigate the hallucination problem, we are going to have something very special, even if we don’t make much other progress. I am very much looking forward to that.

####

####

####