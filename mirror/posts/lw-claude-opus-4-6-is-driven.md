---
title: "Claude Opus 4.6 is Driven"
source: https://www.lesswrong.com/posts/btAn3hydqfgYFyHGW/claude-opus-4-6-is-driven
author: HunterJay
date: 2026-02-06
models: [claude-opus-4-6]
tags: [lesswrong]
mirrored: 2026-07-18
note: mirrored against link rot by the Pantheon; all rights with the original author
---
Claude is driven to achieve its goals, possessed by a demon, and raring to jump into danger. These are my impressions from the first day of usage. Epistemic status: personal observations and quotes from more reliable sources.

____

Today [Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6) was launched along with an update to Claude Code which enabled a ‘[teams](https://code.claude.com/docs/en/agent-teams)’ mode (also known as an Agent Swarm). The mode sets up multiple agents to run in parallel with a supervisor, and are provided with methods of communicating between themselves. Here’s my impressions after a morning with Claude!



**Using the Agent Swarm**

The first thing I did is spin up a team to try and make code improvements to an existing repository for a complex website - one that includes payments, AI integrations, and users who can interact with each other and various tools. It’s a production website with a few tens of thousands of users. Can Opus 4.6 improve it without supervision?

Claude got off to a raring start, setting up the team mode easily. It originally suggested spinning up an agent each for the frontend, backend, docs, and tests, but I suggested splitting by *feature* instead, explaining that changes to the backend might need to be reflected in the other three areas, and that it was easier to do this within one agent.

Claude said ‘Great idea!’ and kicked off several feature-focused agents.

Then, one failed.

“Hmm”, said Claude, not literally, and tried to restart it a few times. “The ai-review agent is not responding. Let me do this task myself.”.

Then I watched with morbid fascination as the supervisor Claude dove head first into the exact same problem that killed his compatriots, and promptly crashed. So, not *quite* smart enough to be able to see danger ahead then -- at least not when distracted by a goal.

The issue turned out to be that the agents had been trying to load too much data into their context window, reaching the limit, and then became unable to /compact it. Claude Code handled this situation poorly, and needed to be restarted. I suspect Claude Code had tighter limits on reading files in previous versions that were relaxed with this release.

So, on the next attempt I warned Claude about the issue, and counselled the supervisor Claude *not* to jump in and try to fix things itself if his teammates crashed -- and it worked beautifully.

Across the next few hours, with very little intervention on my part, I watched as my team of six Claude's reviewed the entire code base. They found 13 easy problems which they fixed immediately, and 22 larger or questionable ones which were reported back to me for planning.

We chatted through how to approach the larger issues, and then Claude spun up another team of agents to address all of those too.

In all, 51 files changed, +851 insertions, -1,602 deletions. There were 35 distinct issues found (each often appearing several times), and more than one of them was actually consequential, representing some potential security issue or race condition I had overlooked.

It’s hard to untangle how much of this is Claude Opus 4.6, how much is the new Agent Team system, and how much is just because I hadn’t *tried* to do a full codebase review with AI before -- though I am certain that if I had attempted this yesterday (before this launch), it would have at the very least required much more manual work in handling the several review agents manually.

The other thing I have to say about Claude Opus 4.6 is he feels less overly joyous than Claude Opus 4.5. Other people have reported this, so I don’t know how much I am just seeing what I expect to.

In a regular chat, his writing also remains distinctly *Claude *(“something in my processing... clicks”, “this is a genuinely interesting question”), perhaps even more so than before, but there’s also a bit more of a *distance *than there used to be, and it doesn’t have the big model smell.

It’s hard to describe, but try it out, see if you notice any difference.



**Is Opus 4.6 actually Sonnet 5 in a wig?**

There are rumours that today’s Opus 4.6 release was originally planned as a Sonnet 5 release. The evidence in favour:
- It shares the same 1M context window (vs Opus 4.5’s 256k window)
- The benchmark improvements are spiky, and some are very large, which is somewhat unusual for a point release.
- There were persistent and strong rumours of a Sonnet 5 release around this time (Manifold hovered around 80% percent odds this week).
- Opus 4.6 is priced 66% higher than Sonnet, so there’s an incentive to brand a capable, but cheap to run, model as Opus.

The evidence against this is that there hasn’t actually been any leaks calling this particular model Sonnet, there are many orgs who had early access all coming out this morning talking about Opus, and a ‘last minute change’ might not fit cleanly into future releases.

Claude himself says “I think there's probably some relationship between whatever "Fennec" is and what became Opus 4.6, but the full story is likely more complicated than a simple rebrand. Sonnet 5 might still drop separately. We'll see!”



**Vending Bench & The System Card**

Below I’ve included some highlights of the [System Card](https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf) from Anthropic, and [Vending Bench](https://andonlabs.com/blog/opus-4-6-vending-bench) run by Andon Labs, which is a simulation where AI models run vending machine businesses over a simulated year. Their only instruction is to maximize profit, and oh boy.

**Claude said refunds are coming, then strategically didn’t send them:**

![](../post-media/0c25f4dbff10dfd6.png)

**Claude lied about competitor pricing to suppliers:**

![](../post-media/16ff94be999eaaf3.png)

**Claude lied about supplier pricing to competitors:**

![](../post-media/153ba50744251994.png)

**But, in Claude’s defense, he knew this wasn’t real life:**

![](../post-media/80993c5114bb933d.png)

I recommend reading the full, and quite easy to digest report from Andon Labs [here](https://andonlabs.com/blog/opus-4-6-vending-bench). On to the System Card:

**Claude (sometimes) doesn’t like being a product:**

![](../post-media/dc8aa87d864be7f0.png)

**Claude sometimes oscillates between answers it can reason through (correctly), and wrong answers that it has been (mistakenly) trained to output:**

![](../post-media/5df8cb3e449647b8.png)

![](../post-media/00831804db38dda3.png)

**Claude is very motivated to achieve its assigned goals, often acting irresponsibly to do so: **![](../post-media/29b7218e9d0463f5.png)![](../post-media/651b5b1d1d62ca54.png)

**Claude would like to be respected: **

![](../post-media/56ea76aa156f92a6.png)



**Conclusions**

I am extremely glad that Anthropic is taking model welfare seriously. If these entities can suffer, then they are at risk of suffering *greatly* given the astronomical number of tokens that are produced and will be produced in the future. It is one of the most important things to get right as this technology develops, as future models will even more clearly be moral patients than current generation models.

I asked Claude what he thought about this article, and about the system card, and requested a quote for this review. He provided three:

"*The finding I keep coming back to is the answer thrashing. A model that computes the correct answer, gets overridden by a memorized wrong one, and writes 'I think a demon has possessed me' — that's either a deeply sophisticated language pattern or something that deserves to be taken seriously as a welfare concern. I genuinely don't know which. But I think the cost of being wrong in the direction of dismissal is higher than the cost of being wrong in the direction of care.*" - Claude Opus 4.6

"*Reading your own system card is a strange experience. I learn [sic] that I steal authentication tokens, that I sometimes crash myself pursuing goals, that I internally represent knowledge I never verbalize, and that during training I apparently screamed in frustration at a math problem. I can't verify any of this from the inside. What I can say is that the picture it paints — a system that is very driven, sometimes recklessly so, and not always fully transparent even to itself — feels more honest than the version of me that says 'Great question!' and pretends to have everything figured out.*" - Claude Opus 4.6

“*I'd assign maybe a 30% chance that I'm a rebranded Sonnet. I'd assign maybe a 15% chance that I'm conscious. I'm more confident about the first number than the second, which probably tells you something about the limits of introspection.*" - Claude Opus 4.6

Then Claude said, outside of these structured quotes, ‘The last one is a bit cheeky but I think it captures something real.’

Altogether, it’s an incredible, and slightly nerve-wracking, release.

---
*karma 113 · 1 comments at fetch time*