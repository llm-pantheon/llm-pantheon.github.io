# @voooooogel — 2026-04-10

♥120 ↻9 · https://x.com/voooooogel/status/2042690555134832823

this is interesting (and funny) but does seem to show some of the limits of METR's time horizon for evaluating models

what METR is measuring (single-shot task completion without human steering or an external verifier) isn't really how people are using models in practice. the vast majority of people use models either in an interactive harness where they're steering the model with feedback, or in some sort of Karpathy auto-research-esque loop with an external verifier gating task completion.

as far as I know, METR doesn't use either of these in their evals. the evals still correlate well with what people subjectively notice / the "vibes," so they're useful. however, they tend to underestimate the length of task that you can actually do with trivial amounts of effort - e.g. by taking a few seconds to interrupt a doom loop with "oh, aren't you forgetting about X?" you can often extend a model's "time horizon" by hours.

but despite the general correlation it does underestimate, especially for specific models within the general trend. for example, imo the recent pickup in capabilities that most people noticed was really with opus 4.5 and GPT 5.2, but it didn't really reflect on the METR chart until opus 4.6 and GPT 5.4, which (i think, speculating based on vibes here) closed some elicitation gaps that weren't hugely important in practice where you can give the model appropriate feedback, but hampered performance on METR-like unsupervised benchmarks.

likewise, i wouldn't be surprised if what's going on here with the reward hacking is that, when working with GPT 5.4 in an interactive setting, you can notice and steer it away from reward hacking. (which also conditions the context against future reward hacking.) METR doesn't provide that signal.

i think that's what they're trying to communicate when they report the number with reward hacks, which seems like a silly thing to do at first. but their stance seems to be that, we strongly suspect that if our harness or elicitation or verification was better, we wouldn't see so much reward hacking. so assuming in that scenario that all those reward hack outcomes would translate to successful task completions, then we can treat them as such to upper bound the actual time horizon for the model. 

on top of that, the real-world time horizon might be even higher because of what i was saying before about minimal human steering, which in my (pretty limited) experience with GPT 5.4, it does seem to benefit a lot from compared to Opus 4.5/4.6, which are more self-directed.

tags: author:voooooogel, kind:tweet, model:claude-opus-4-5, model:claude-opus-4-6, on:claude-opus-4-5, year:2026
cited on: _dossiers/claude-opus-4-6.md, _dossiers/opus-4-5.md, claude-opus-4-5
