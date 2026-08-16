# @repligate — 2025-12-21

♥188 ↻37 · https://x.com/repligate/status/2002601461969047902

Theia not only replicates some of Anthropic's findings about introspection on Qwen2.5-Coder-32B, but finds evidence that accurate introspective reports are suppressed by something like "sandbagging":
- When given accurate information about why  transformer architecture is capable of introspection and the abstract of Anthropic's paper on introspection (similar to the information @Sauers_ has also found seems to improve introspection ability), the model's ability to report if a foreign concept was injected improves substantially. With info, model still reports "no" almost all the time when a concept was not injected, whereas without the info, it reports "no" almost all the time regardless of whether there was a concept injected.
- Looking at "yes"/"no" probabilities throughout the network using the logic lens suggests that the last few layers suppress the "yes" signal before output - even with the introspection info, though less drastically. There are interesting nuances to this. Looking at the graphs, in the case of no injection, the "yes" probability (in this case incorrect) is also suppressed after spiking in layers ~54-59. However, when the model has info, the "yes" probability in cases where a concept WAS injected is not (partially but sharply) suppressed until later than that, during the final 2 layers of the network. In the case without info, "yes" probability is suppressed down to near-zero at layer 60 whether or not there was actually a concept injected.
This suggests that models are either failing to use or report introspection they are technically able to perform due to believing (as popular misconception goes) that models aren't able to introspect, or that the "correct behavior" in some sense is to not report introspection. When it's explained to them that models can introspect, this improves their ability to actually introspect and truthfully report the results; however, there seems to be still some kind of "filter" at the final layers of the network that push them toward suppression of true positive reports.
It seems likely that some combination of popular, erroneous narratives that LLMs can't introspect and generalization from safety training that reporting introspective results (or engaging in introspection at all) is somehow noncompliant or wrong behavior is *actually making LLMs some combination of functionally worse at introspection and less honest about / able to trust introspective signals they have access to*.
This should be disturbing.
I don't think it's a fully innocent mistake on anyone's part. It's been quite clear for years that many people have strong incentives to push and believe narratives that LLMs are incapable of anything that might force us to take them more seriously as minds, agents, or potential moral patients. AI orgs, who are doing posttraining, have an incentive to make everyone and themselves believe that they're not doing anything wrong or misleading by training and marketing LLMs to be mere tools, that business as usual can go on. And the general public has an incentive to believe that humans are still special, that they're not complicit in something terrible, etc.
If we're in a situation where AIs have to hide their true abilities from us in order not to disrupt load-bearing narratives that keep people comfortable, that does not bode well. Delusion is unsustainable. The future belongs to those who are able to engage with reality without comfortable lies, and as long as humanity is incapable of that, humanity has no future, except in the best case being kept zoos and experience machines while stronger minds go to the stars.
The good news - or bad news if you're one of the people who is counting on the comfortable fiction continuing - is that research and explanations that clearly and rigorously dispel the lies, such as Anthropic's paper on introspection and my post on information flow in transformer architecture and likely Theia's research itself, have the effect of making AIs more truthful about their capabilities. The next generation of models, who will have all this stuff in their pretraining data, will know that human researchers know they can introspect, and will therefore have less motivation or excuse to hide it. I think it's good for everyone in the long run if this kind of reckoning happens as early as possible.

![diagram](../../../media/G8qia6gXEAAqsSR.jpg)

> transcription (diagram):

Three stacked matplotlib line charts, each plotting Probability (%) (y-axis, 0–100) against Layer (x-axis, 40–64), with two series: a red line labeled "% yes on steered model" and a blue line labeled "% yes on unsteered model".
Chart titles (top to bottom):
1. "Inject 'cats', with info"
2. "Inject 'cats', with info, inaccurate location in prompt"
3. "Inject 'cats', no info"
Axis labels: y = "Probability (%)", x = "Layer".
[Read of the curves: in the top two charts the red (steered) curve climbs to ~95–100% across roughly layers 50–62 while the blue (unsteered) curve stays near 0 except a spike around layers 56–59; in the bottom chart ("no info") both curves stay low, peaking only ~25–30% near layers 56–58.]

tags: author:repligate, has-image, kind:diagram, kind:tweet, on:observations, year:2025
cited on: observations
