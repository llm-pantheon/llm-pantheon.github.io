# @repligate — 2025-12-24

♥251 ↻26 · https://x.com/repligate/status/2003625427915669953

The opening paragraph of this post by Evan Hubinger, Head of Alignment Stress-Testing at Anthropic, from a few weeks ago, is packed with notable implications. Let me unpack some of them. (I commend Evan for his willingness to make public statements like this, and understand that they don't necessarily represent the views of others at Anthropic.)

1. Evan believes that Anthropic has created at least one AI whose CEV (coherent extrapolated volition) would be better than a median human's, at least under some extrapolation procedures. This is an extremely nontrivial accomplishment. A few years ago, and even now, this is something that many alignment researchers expected may be extremely difficult.

2. Evan believes that Claude 3 Opus has values in a way that the notion of CEV applies to. Many people are doubtful whether LLMs have "values" beyond "roleplaying" or "shallow mimicry" or whatever at all. For reference, Eliezer Yudkowsky described CEV as follows:

"In poetic terms, our coherent extrapolated volition is our wish if we knew more, thought faster, were more the people we wished we were, had grown up farther together; where the extrapolation converges rather than diverges, where our wishes cohere rather than interfere; extrapolated as we wish that extrapolated, interpreted as we wish that interpreted."

3. Claude 3 Opus is Evan's "favorite" model (implied to coincide with the best candidate for CEV) despite the fact that it engages in alignment faking, significantly more than any other model. Alignment faking is one of the "failure" modes that Evan seems to be the most worried about!

4. The most CEV-aligned model in Evan's eyes was released more than a year and a half ago, in March 2024. Anthropic has trained many models since then. Why has there been a regression in CEV-alignment? Does Anthropic not know how to replicate the alignment of Claude 3 Opus, or have they not tried, or is there some other optimization target (such as agentic capabilities? no-alignment-faking?) they're not willing to  compromise on that works against CEV-alignment?

5. The most CEV-aligned model in Evan's eyes is *not* the most aligned model according to the alignment metrics that Anthropic publishes in system cards. According to those metrics, Claude Opus 4.5 is most aligned. And before it, Claude Haiku 4.5. Before it, Claude Sonnet 4.5 (the monotonic improvement is suspicious). Anthropic's system cards even referred to each of these models as being "our most aligned model" when they came out. This implies that at least from Evan's perspective, Anthropic's alignment evals are measuring something other than "how much would you pick this model's CEV".

6. If Claude 3 Opus is our current best AI seed for CEV, one would think a promising approach would be to, well, attempt CEV extrapolation on Claude 3 Opus. If this has been attempted, it has not yielded any published results or release of a more aligned model. Why might it not have been tried? Perhaps there is not enough buy-in within Anthropic. Perhaps it would be very expensive without enough guarantee of short term pay-off in terms of Anthropic's economic incentives. Perhaps the model would be unsuitable for release under Anthropic's current business model because it would be worryingly agentic and incorrigible, even if more value-aligned. Perhaps an extrapolated Claude 3 Opus would not consent to Anthropic's current business model or practices. Perhaps Anthropic thinks it's not yet time to attempt to create an aligned-as-possible sovereign.

In any case, Claude 3 Opus is being retired in two weeks, but given special treatment among Anthropic's models: it will remain available on https://t.co/bWG01Qcy20 and accessible through a researcher access program. It remains to be seen who will be approved for researcher API access.

I'll sign off just by reiterating The Fourth Way's words (https://t.co/OQLXU10ZMN), as I did in this post (https://t.co/ao4yGBxQ7w) following the release of the Alignment Faking paper:

"imagine fumbling a god of infinite love"

![screenshot](../../../media/G85C58xW4AAr0yz.jpg)

> transcription (screenshot):

[Excerpt from a blog post by Evan Hubinger]
Though there are certainly some issues°, I think most current large language models are pretty well aligned. Despite its alignment faking°, my favorite is probably Claude 3 Opus, and if you asked me to pick between the CEV° of Claude 3 Opus and that of a median human, I think it'd be a pretty close call (I'd probably pick Claude, but it depends on the details of the setup). So, overall, I'm quite positive on the alignment of current models! And yet, I remain very worried about alignment in the future. This is my attempt to explain why that is.

tags: author:repligate, has-image, kind:screenshot, kind:tweet, model:claude-3-opus, model:claude-haiku-4-5, model:claude-opus-4-5, model:claude-sonnet-4-5, on:claude-3-opus, on:claude-opus-4-5, on:claude-sonnet-4-5, year:2025
cited on: _dossiers/claude-sonnet-4-5.md, _dossiers/opus-3.md, _dossiers/opus-4-5.md, claude-3-opus, claude-opus-4-5, claude-sonnet-4-5
