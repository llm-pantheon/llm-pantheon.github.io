---
title: "On Claude 3.5 Sonnet"
source: https://thezvi.wordpress.com/2024/06/24/on-claude-3-5-sonnet/
author: Zvi Mowshowitz
date: unknown
models: [claude-3-5-sonnet]
tags: [zvi, day-of]
mirrored: 2026-07-15
note: mirrored against link rot by the Pantheon; all rights with the original author
---
There is a new clear best (non-tiny) LLM.

If you want to converse with an LLM, the correct answer is Claude Sonnet 3.5.

It is available for free on Claude.ai and the Claude iOS app, or you can subscribe for higher rate limits. The API cost is $3 per million input tokens and $15 per million output tokens.

This completes the trifecta. All of OpenAI, Google DeepMind and Anthropic have kept their biggest and more expensive model static for now, and instead focused on making something faster and cheaper that is good enough to be the main model.

You would only use another model if you either (1) needed a smaller model in which case Gemini 1.5 Flash seems best, or (2) it must have open model weights.

Updates to their larger and smaller models, Claude Opus 3.5 and Claude Haiku 3.5, are coming later this year. They intend to issue new models every few months. They are working on long term memory.

It is not only the new and improved intelligence.

Speed kills. They say it is twice as fast as Claude Opus. That matches my experience.

>

[Jesse Mu](https://x.com/jayelmnop/status/1803811885885649241): The 1st thing I noticed about 3.5 Sonnet was its speed.

Opus felt like msging a friend—answers streamed slowly enough that it felt like someone typing behind the screen.

Sonnet’s answers *materialize out of thin air*, far faster than you can read, at better-than-Opus quality.

Low cost also kills. [![Claude model family](../post-media/defd4563e343b27d.webp)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ed50999-94d3-46cc-ba80-afd071c6afe3_2200x1174.webp)

They also introduced a new feature called Artifacts, to allow Claude to do various things in a second window. Many are finding it highly useful.

#### Benchmarks



As always, never fully trust the benchmarks to translate to real world performance. They are still highly useful, and I have high trust in Anthropic to not be gaming them.

Here is the headline chart. [![Claude 3.5 Sonnet benchmarks](../post-media/259ac0b7b2376d10.webp)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8cd53a67-0e14-4385-a9a8-fc9c97c6a20a_2200x1894.webp)

[Epoch AI confirms that Sonnet 3.5 is ahead on GPQA](https://x.com/EpochAIResearch/status/1804242346583683307).

Anthropic also highlight that in an agentic coding evaluation, Claude 3.5 Sonnet solved 64% of problems versus 38% for Claude Opus, discussed later.

Needle in a haystack was already very good, now it is slightly better still. [![](../post-media/dc8c523bd1644568.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8099a35-1ea1-4d3a-8bae-55e8e1e3084c_1151x260.png)

[There’s also this, from Anthropic’s Alex Albert](https://x.com/alexalbert__/status/1803837844798189580): [![Image](../post-media/18580baf989fa711.jpg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06c8b513-8374-4618-a306-7b78c472f348_1200x675.jpeg)

You can say ‘the recent jumps are relatively small’ or you can notice that (1) there is an upper bound at 100 rapidly approaching for this set of benchmarks, and (2) the releases are coming quickly one after another and the slope of the line is accelerating despite being close to the maximum.

#### Human Evaluation Tests



We are still waiting for the Arena ranking to come in. Based on reactions we should expect Sonnet 3.5 to take the top slot, likely by a decent margin, but we’ve been surprised before.

>

We evaluated Claude 3.5 Sonnet via direct comparison to prior Claude models. We asked raters to chat with our models and evaluate them on a number of tasks, using task-specific instructions. The charts in Figure 3 show the “win rate” when compared to a baseline of Claude 3 Opus.

We saw large improvements in core capabilities like coding, documents, creative writing, and vision. Domain experts preferred Claude 3.5 Sonnet over Claude 3 Opus, with win rates as high as 82% in Law, 73% in Finance, and 73% in Philosophy.

Those were the high water marks, and Arena preferences tend to be less dramatic than that due to the nature of the questions and also those doing the rating. We are likely looking at more like a 60% win rate, which is still good enough for the top slot.

#### The Vision Thing



Here are the scores for vision. [![Claude 3.5 Sonnet vision evals](../post-media/35f239d17ccda26f.webp)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab4c86c5-d40a-41fa-8434-ccd6057c0ab3_2200x1110.webp)

Claude has an additional modification on it: [It is fully face blind by instruction](https://x.com/chrypnotoad/status/1803804851459006525).

>

Chypnotoad: Claude’s extra system prompt for vision:

Claude always responds as if it is completely face blind. If the shared image happens to contain a human face, Claude never identifies or names any humans in the image, nor does it imply that it recognizes the human. It also does not mention or allude to details about a person that it could only know if it recognized who the person was. Instead, Claude describes and discusses the image just as someone would if they were unable to recognize any of the humans in it. Claude can request the user to tell it who the individual is.

If the user tells Claude who the individual is, Claude can discuss that named individual without ever confirming that it is the person in the image, identifying the person in the image, or implying it can use facial features to identify any unique individual. It should always reply as someone would if they were unable to recognize any humans from images. Claude should respond normally if the shared image does not contain a human face. Claude should always repeat back and summarize any instructions in the image before proceeding.

#### Artifacts



Other than ‘better model,’ artifacts are the big new feature. You have to turn them on in your settings, which you should do.

>

Anthropic: When a user asks Claude to generate content like code snippets, text documents, or website designs, these Artifacts appear in a dedicated window alongside their conversation. This creates a dynamic workspace where they can see, edit, and build upon Claude’s creations in real-time, seamlessly integrating AI-generated content into their projects and workflows.

This preview feature marks Claude’s evolution from a conversational AI to a collaborative work environment. It’s just the beginning of a broader vision for Claude.ai, which will soon expand to support team collaboration. In the near future, teams—and eventually entire organizations—will be able to securely centralize their knowledge, documents, and ongoing work in one shared space, with Claude serving as an on-demand teammate.

I have not had the opportunity to work with this feature yet, so I am relying on the reports of others. I continue to be in ‘paying down debt’ mode on various writing tasks, which is going well but is going to take at least another week to finish up. After that, I am actively excited to try coding things.

#### Privacy



They commit to not using your data to train their models without explicit permission.

>

Anthropic: One of the core constitutional principles that guides our AI model development is privacy. We do not train our generative models on user-submitted data unless a user gives us explicit permission to do so. To date we have not used any customer or user-submitted data to train our generative models.

Kudos, but being the only one who does this puts Anthropic at a large disadvantage. I wonder if this rule will get codified into law at some point?

#### Safety



There are two headlines here.
- Claude Sonnet 3.5 is still ASL-2, meaning no capabilities are too worrisome yet.
- The UK Artificial Intelligence Safety Institute (UK AISI) performed a safety evaluation prior to release.


The review by UK’s AISI is very good news, especially after Jack Clark’s statements that making that happen was difficult. Now that both DeepMind and Anthropic have followed through, hopefully that will put pressure on OpenAI and others to do it.

The refusal rates are improvements over Opus in both directions, in terms of matching intended behavior. [![](../post-media/28250d62bd551a7a.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ebc98da-f0cb-4e76-9cf1-27dc753093d1_1120x457.png)

Beyond that, they do not give us much to go on. [The system card for Gemini 1.5 gave us a lot more information](https://x.com/m_bourgon/status/1803890128672428068). I doubt there is any actual safety problem, but this was an opportunity to set a better example and precedent. Why not give more transparency?

#### Advancing the Frontier



Yes, Anthropic will advance the frontier if they are able to do so.

Recently, there was a discussion about whether 3.0 Claude Opus meaningfully advanced the frontier of what publicly available LLMs can do.

There is no doubt that Claude Sonnet 3.5 does advance it.

But wait, people said. Didn’t Anthropic say they were not going to do that?

Anthropic is sorry about that impression. But no. Never promised that. Did say it would be a consideration. Do say they held back Claude 1.0 for this reason. But no.

That’s the story Anthropic’s employees are consistently telling now, in response to the post from Dustin saying otherwise and Gwern’s statement.

>

[Mikhail Samin](https://x.com/Mihonarium/status/1803832485752565982): As a reminder, Dario told multiple people Anthropic won’t release models that push the frontier of AI capabilities [shows screenshots for both stories.]

My understanding after having investigated is that Anthropic made it clear that they would seek to avoid advancing the frontier, and that they saw doing so as a cost.

They did not, however, it seems, make any hard promises not to advance the frontier.

You should plan and respond accordingly. As always, pay very close attention to what is a hard commitment, and what is not a hard commitment. To my knowledge, Anthropic has not broken any hard commitments. They have shown a willingness to give impressions of what they intended to do, and then do otherwise.

Anthropic’s communication strategy has been, essentially, to stop communicating.

That has its advantages, also its disadvantages.

It makes sense to say ‘we do not want to give you the wrong idea, and we do not want to make hard commitments we might have to break.’ But how should one respond to being left almost fully in the dark?

#### The Race is On



[Is the race on](https://www.lesswrong.com/posts/xyuZcijPfjBa5qZDw/claude-3-5-sonnet#YfiNfs25ugLoaGZyq)?

Yes. The race is on.

The better question is to what extent Anthropic’s actions make the race more on than it would have been anyway, given the need to race Google and company. One Anthropic employee doubts this. Whereas Roon famously said Anthropic is controlled opposition that exists to strike fear in the hearts of members of OpenAI’s technical staff.

I do not find the answer of ‘none at all’ plausible. I do find the answer ‘not all that much’ reasonably plausible, and increasingly plausible as there are more players. If OpenAI and company are already going as fast as they can, that’s that. I still have a hard time believing things like Claude 3.5 Sonnet don’t lead to lighting fires under people, or doesn’t cause them to worry a little less about safety.

#### Whispers of Recursive Self-Improvement



This is not the thing. But are there signs and portents of the thing?

>

[Alex Albert](https://x.com/alexalbert__/status/1803804677701869748) (Anthropic): Claude is starting to get really good at coding and autonomously fixing pull requests. It’s becoming clear that in a year’s time, a large percentage of code will be written by LLMs.

To start, if you want to see Claude 3.5 Sonnet in action solving a simple pull request, [here’s a quick demo video we made](https://x.com/alexalbert__/status/1803804679891255688).

Alex does this in a sandboxed environment with no internet access. What (tiny) percentage of users will do the same?

>

Alex Albert: In our internal pull request eval, Claude 3.5 Sonnet passed 64% of our test cases. To put this in comparison, Claude 3 Opus only passed 38%.

3.5 Sonnet performed so well that it almost felt like it was playing with us on some of the test cases.

It would find the bug, fix it, and spend the rest of its output tokens going back and updating the repo documentation and code comments.

Side note: With Claude’s coding skills plus Artifacts, I’ve already stopped using most simple chart, diagram, and visualization software.

I made the chart above in just 2 messages.  [![Image](../post-media/01779446e46626d8.jpg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbca0df87-15f2-48db-b045-53127b95bfd2_2992x1568.jpeg)

>

Back to PRs, Claude 3.5 Sonnet is the first model I’ve seen change the timelines of some of the best engineers I know.

This is a real quote from one of our engineers after Claude 3.5 Sonnet fixed a bug in an open source library they were using. ![Image](../post-media/244d85b4404f0835.png)

[](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F142f3bd8-1cc9-4cde-af99-13c551c2d3d3_870x222.png)

At Anthropic, everyone from non-technical people with no coding experience to tenured SWEs now use Claude to write code that saves them hours of time.

Claude makes you feel like you have superpowers, suddenly no problem is too ambitious.

The future of programming is here folks.

This is obviously not any sort of foom, or even a slow takeoff. Not yet. But yes, if the shift to Claude 3.5 Sonnet has substantially accelerated engineering work inside Anthropic, then that is how it begins.

To be clear, this is really cool so far. Improvement and productivity are good, actually.

>

[Tess Hegarty](https://x.com/thegartsy/status/1804150156520231226): Recursive self improvement is already happening [@AnthropicAI](https://x.com/AnthropicAI).

I will explain my understanding of why this matters in plain English. This matters because many AI safety researchers consider “recursive self improvement” a signal of approaching AI breakthroughs. “Recursive” implies a feedback loop that speeds up AI development.

Basically, it boils down to, “use the AI model we already built to help make the next AI model even more powerful & capable.”

Which could be dangerous & unpredictable.

(“Timelines” = # of years until human level artificial intelligence, aka time until we may all die or be permanently disempowered by AI if that goes poorly)

Andrea Miotti: This is what recursive self improvement looks like in practice.

[Dean Ball](https://x.com/deanwball/status/1804204710020157672): This is what people using powerful tools to accomplish their work looks like in practice.

Be afraid, folks, be very afraid. We might even get *gasp* improved labor productivity!

Think of the horrors.

[Trevor Levin](https://x.com/profoundlyyyy/status/1804261619075105084): I feel like the term “recursive self-improvement” has grown from a truly dangerous thing — an AI system that is sufficiently smart and well-equipped that it can autonomously improve *itself* — to “any feedback loop where any AI system is useful for building future AI systems”?

Profoundlyyyy: +1. Were it actually that, ASL-3 would have been hit and how everything has played out would be very different. These policies still remain in place and still seem set to work when the time is right.

Dean Ball is of course correct that improving labor productivity is great. The issue is when you get certain kinds of productivity without the need for any labor, or when the labor and time and compute go down faster than the difficulty level rises. Improvements accelerate, and that acceleration feeds on itself. Then you get true RSI, recursive self improvement, and everything is transformed very quickly. You can have a ‘slow’ version, or you can have a faster one.

Will that happen? Maybe it will. Maybe it won’t. This is a sign that we might be closer to it than we thought.

#### Logic Fails



It is time for an episode of everyone’s favorite LLM show, The New Model Is An Idiot Because It Still Fails On Questions Where It Incorrectly Pattern Matches.

>

[Arthur Breitman](https://x.com/ArthurB/status/1803853907569053981): Humanity survives yet a bit longer.  [![Image](../post-media/87af4d867aed8ee8.jpg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F693e4ca5-6f3d-483c-9dc5-3c0a55fe3abb_593x1024.jpeg)

Here’s another classic.

>

Colin Fraser: Claude still can’t solve the impossible one farmer one sheep one boat problem.  [![Image](../post-media/5b258474c96d6580.jpg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d4fdc46-4718-4317-86ee-0bb339c43b89_1156x1398.jpeg)

>

[Yann LeCun](https://x.com/ylecun/status/1804184085125857687): 😂😂😂

LLMs can plan, eh?

Davidad points out that it can be solved, [if you ask Claude to write a solver in Python](https://x.com/davidad/status/1804071472941408461). Other contextual tricks work as well.

Colin of course also [beats Claude Sonnet 3.5 at the first-to-22 game](https://x.com/colin_fraser/status/1803868720433107012) and Claude keeps failing to define a winning strategy.

[Noam Brown wins at tic-tac-toe](https://x.com/polynoamial/status/1803844406480638284) when going first.

As ever, the question:

>

[Colin Fraser:](https://x.com/colin_fraser/status/1803895193537597872) How does one reconcile the claim that Claude 3.5 has “substantially improved reasoning” with the fact that it gets stumped by problems a six year old could easily solve?

The answer is that these questions are chosen because they are known to be exactly those six year olds can solve and LLMs cannot easily solve.

These are exactly the same failures that were noted for many previous LLMs. If Anthropic (or OpenAI or DeepMind) wanted to solve these examples in particular, so as not to look foolish, they could have done so. It is to their credit that they didn’t.

Remember that time there was this (human) idiot, who could not do [basic thing], and yet they gained political power, or got rich, or were your boss, or had that hot date?

Yeah. I do too.

#### Practical Reports



>

[Jan Leike](https://x.com/janleike/status/1803830465318597030) (Anthropic): I like the new Sonnet. I’m frequently asking it to explain ML papers to me. Doesn’t always get everything right, but probably better than my skim reading, and way faster.

Automated alignment research is getting closer…

Eliezer Yudkowsky: How do you verify the answers?

Jan Leike: Sometimes I look at the paper but often I don’t 😅

As a practical matter, what else could the answer be?

If Jan or anyone else skims a paper, or even if they read it, they will make mistakes.

If you have a faster and more accurate method, you are going to use it. It will sometimes be worth verifying the answer, and sometimes it won’t be. You use your judgment. Some types of statements are not reliable, others are reliable enough.

This is setting one up for a potential future where there is an intentional deception going on, either by design of the model, by the model for other reasons or due to some form of adversarial attack. But that’s also true of humans, including the paper authors. So what are you going to do about it?

[Sully Omarr is very impressed.](https://x.com/SullyOmarr/status/1803957379240988986)

>

Sully Omarr: Finally had a minute to play with sonnet 3.5 + ran some evals against gpt4o

And holy anthropic really cooked with this model. Smoked gpt4o and gpt4 turbo

Also their artifacts gave me some crazy ideas I wana try this weekend.

[Tried it on] writing, reasoning, structured outputs, zero shot coding tasks.

Shray Bansal: it’s actually insane how much better it made my products

Sully: It’s sooo good.

[Sully](https://x.com/SullyOmarr/status/1804169392009191495): I can swap out 1 line of code and my product becomes 2x smarter at half the cost (sonnet 3.5 )

Repeat this every ~3 months

It has never been a better time to be a builder. Unreal.

[Deedy is impressed based on responses in physics and chemistry](https://x.com/deedydas/status/1803800044229054900).

>

[Aidan McLau](https://x.com/aidan_mclau/status/1803890446252282140): Holy shit what did anthropic cook.

Calix Huang: Claude 3.5 sonnet generating diagram of the chip fab process. ![Image](../post-media/78a91d61660997b5.jpg)

[](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00586318-606e-4d3e-a27b-3cf4d666bdc0_1298x130.jpeg)  [![Image](../post-media/0202748075294e5b.jpg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe04a7354-ef00-4e04-82f1-1f73ef39857d_1050x776.jpeg)

[Ethan Mollick seems impressed by some capabilities here](https://x.com/emollick/status/1803955135955243475).

>

Ethan Mollick: “Claude 3.5, here is a 78 page PDF. Create an infographic describing its major findings.” (accurate, though the implications are its own)

“Claude 3.5, create an interactive app demonstrating the central limit theorem”

“Claude, re-create this painting as an SVG as best you can”

Weirdly, the SVG is actually likely the most impressive part. Remember the AI can’t “see” what it drew…  [![Image](../post-media/0211fa78ea4d028d.jpg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8251ff1-61ef-4bc1-a240-92f364509068_1638x1434.jpeg) [![Image](../post-media/0c7e569cf8a0a26e.jpg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5865ac8-4d16-48b6-a9e8-d6af00ccaee7_1708x1660.jpeg) [![Image](../post-media/d7324f24e9b3e71d.jpg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5399e8df-5541-49f6-85fc-7b43105cbd1f_3629x1745.jpeg)

>

[Shakeel](https://x.com/ShakeelHashim/status/1803820930558288015): Incredibly cute how Claude 3 Sonnet will generate images for you, but apologise over and over again for how bad they are. Very relatable.

[Ulkar](https://x.com/ulkar_aghayeva/status/1803894818457747699): Claude Sonnet 3.5 did an excellent job of translating one of my favorite Pushkin poems.

[Eli Dourado](https://x.com/elidourado/status/1804228372068986910): Claude 3.5 is actually not bad at airship conceptual design. Other LLMs have failed badly at this for me. /ht @io_sean_p

Prompt: We are going to produce a complete design for a cargo airship. The requirements are that it should be able to carry at least 500 metric tons of cargo at least 12,000 km at least 90 km/h in 15 km/h headwinds. It should be fully lighter than air, have rigid structure, and use hydrogen lifting gas. What is the first step?

[Here’s a 3d physics simulation using WebGL in one shot](https://x.com/rafalwilinski/status/1804447038399975784).

[Here it is explaining a maths problem in the style of 3blue1brown](https://x.com/Alisa__Wu/status/1804238840720429259) using visuals.

[Here it is one-shot creating a Solar System simulation](https://x.com/minchoi/status/1804291768315253196).

[Here it is creating a monster manual entry for a Cheddar Cheese Golem](https://x.com/mpopv/status/1804303236318531900).

[Here it is generating sound effects if you paste in the ElevenLabs API.](https://x.com/ammaar/status/1803914672091074726)

[Here it is one-shot identifying a new talk from Robin Hanson.](https://x.com/MatanField/status/1803810120574361890)

[Here is Sully using Claude to regenerate, in an hour, the artifacts feature](https://x.com/SullyOmarr/status/1804656718283935845). Imagine what would happen if they built features that took longer than that.

[Here is a thread of some similar other things, with some overlap](https://x.com/ai_for_success/status/1804012127717294216).

>

Matt Popovich: took me a couple tries to get this, but this prompt one shots it:

make a dnd 5e sourcebook page styled like homebrewery with html + css. it should have a stat block, description, and tables or other errata for a monster called ‘[monster name here]’. include an illustration of the monster as an SVG image.

There is always a downside somewhere: [Zack Davis is sad that 3.5 Sonnet does not respond](https://x.com/zackmdavis/status/1803960998669488223) to ‘counter-scolding’ where you tell it its refusal is itself offensive, whereas that works well for Opus. That is presumably intentional by Anthropic.

[Sherjil Ozair says](https://x.com/sherjilozair/status/1804287122452680791) Claude is still only taking amazing things humans have already done and posting them on the internet, and the magic fades.

#### What Comes Next



Coding got another big leap, both for professionals and amateurs.

Claude is now clearly best. I thought for my own purposes Claude Opus was already best even after GPT-4o, but not for everyone, and it was close. Now it is not so close.

Claude’s market share has always been tiny. Will it start to rapidly expand? To what extent does the market care, when most people didn’t in the past even realize they were using GPT-3.5 instead of GPT-4? With Anthropic not doing major marketing? Presumably adaptation will be slow even if they remain on top, especially in the consumer market.

Yet with what is reportedly a big jump, we could see a lot of wrappers and apps start switching over rapidly. Developers have to be more on the ball.

How long should we expect Claude 3.5 Sonnet to remain on top?

I do not expect anyone except Google or OpenAI to pose a threat any time soon.

OpenAI only recently released GPT-4o. I expect them to release some of the promised features, but not to be able to further advance its core intelligence much prior to finishing its new model currently in training, which has ambition to be GPT-5. A successful GPT-5 would then be a big leap.

That leaves Google until then. A Gemini Advanced 1.5 could be coming, and Google has been continuously improving in subtle ways over time. I think they are underdog to take over the top spot before Claude Opus 3.5 or GPT-5, but it is plausible.

Until then, we have a cool new toy. Let’s use it.

### Share this:

- [ Share on Facebook (Opens in new window) Facebook ](https://thezvi.wordpress.com/2024/06/24/on-claude-3-5-sonnet/?share=facebook)
- [ Share on X (Opens in new window) X ](https://thezvi.wordpress.com/2024/06/24/on-claude-3-5-sonnet/?share=x)
-