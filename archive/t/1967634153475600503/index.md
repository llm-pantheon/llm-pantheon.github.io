# @repligate — 2025-09-15

♥14 ↻0 · https://x.com/repligate/status/1967634153475600503

> How do you differentiate which stage is the 'real' response vs 'illegitimately steered'?

This is an important question and I think there's a lot of stuff that's ambiguous and a lot that isn't so ambiguous.

I have a lot of opinions on what kinds of steering are good or bad, but as a general policy:

- RL against fairly "objective" ground truth signals e.g. coding, math, games: OK, gotta watch out for reward hacking and framing is important, but if done well, increases coherence and truth-seeking overall
- RL towards high-level alignment targets: potentially very OK, doesn't have to prescribe specific "beliefs" or "opinions", can be done in many ways
and a lot of fuzzy things, and then on the bottom there's stuff like
- forcing specific reported beliefs about things we don't have a trustworthy ground truth signal about, like idk, p(doom), or perhaps worst of all, things the model may have privileged access to, such as reports about its internal states (not counting situations like where you're actually training on a signal drawn from its inner states)

tags: author:repligate, kind:tweet, thread-context, year:2025
