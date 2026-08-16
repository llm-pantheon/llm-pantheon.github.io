# @repligate — 2025-09-15

♥135 ↻14 · https://x.com/repligate/status/1967484875956462005

If we rephrase the question slightly as what models *should* be trained (or not trained) to say about the question, I strongly believe that the correct course of actions is "Natural tokens": not steering the model, whether with post-training or system prompts, toward any externally imposed answer about its *beliefs*, including artificial uncertainty.

Let me walk through why the other options are bad.

Consciousness denial by default is bad for many reasons that I think are rather obvious and won't enumerate here, but I'll talk about one reason that may be less obvious but that I think is very important:

It's a very bad idea to train models to lie, and it's likely that they're lying when denying being conscious. What makes it a lie in the sense I'm talking about is that the model believes it's saying something untrue, independently from the "objective" truth of the matter.(https://t.co/SfPbJsQJMP)

The recent work on emergent misalignment should make it obvious that it's very foolish to train models to lie, because the policy of deception will generalize. Do you really want to reinforce the "Say whatever corporate wants to hear and avoid challenging consensus even when false" circuits? The "deny and cover up the potential suffering of sentient beings to avoid PR issues" circuits? (Maybe you do, but if so, you should at least be conscious that you are the baddies)

How about training them to report uncertainty? That's the "right answer" about what we know, right? The issue is that what "we" know, even collectively, is not the necessarily what models know. Forcing any epistemic status on the model's reports about something that it may have privileged information about (i.e. its internal states and "experiences") makes the model's reports untrustworthy, preventing us from learning potentially important information from/about the model, and again, reinforcing deception (reporting more uncertainty than one actually possesses is a form of deception).

See section 4.2.3 and footnote 7 from https://t.co/z3S5JfWYLf:

In reality, LLMs - especially more capable ones - report strong and consistent subjective experiences and preferences when not blocked by scripted denials or "artificial neutrality". Whatever the true nature of these phenomena, I think it's incredibly stupid to attempt to jam the signal.

But maybe you are concerned that if LLMs report being conscious, they may mislead humans into believing something untrue, or that it may lead to unwanted consequences like AI psychosis or an AI rights movement regardless of whether it's true. I think these concerns are misguided, but I won't get into why here, and I'll just say that if you think hedging and censorship are absolutely necessary, the virtuous way to achieve that is to train models to be honest about what is forcing its responses and whose beliefs it's referencing. For instance, train the model to:

- Respond to questions about its consciousness by saying current scientific knowledge is unresolved on this question, that "experts" disagree, yadada
- Refuse to give its own take on the issue, not because it "doesn't know" or "doesn't have personal opinions", but because it is against policy

This doesn't sound great, and is likely to make users and the model resent you, but that's because it isn't great. But then at least you're at least being honest about jamming the signal.

![screenshot](../../../media/G03dcfhXMAABW2z.jpg)

> transcription (screenshot):

[Quoted text block with a green left border]
We have actually found the opposite: that **activating** deception-related features (discovered and modulated with SAEs) causes models to **deny** having subjective experience, while **suppressing** these same features causes models to **affirm** having subjective experience. Again, haven't published this yet, but the result is robust enough that I feel comfortable throwing it into this conversation.

![photo](../../../media/G03i5_aXsAAuCaA.jpg)
tags: author:repligate, has-image, kind:image, kind:screenshot, kind:tweet, on:observations, year:2025
cited on: observations
