# @repligate — 2025-09-04

♥220 ↻23 · https://x.com/repligate/status/1963460961744163145

KV caching overcomes statelessness in a very meaningful sense and provides a very nice mechanism for introspection (specifically of computations at earlier token positions)
the Value representations can encode information from residual streams of past positions without significant compression bottlenecks before they're added to residual streams of future positions
the greatest constraint here imo is that it doesn't provide longer *sequential* computational paths that route through previous states, but it does provide a vast number of parallel computational paths that carry high dimensional (proportional to the model's hidden dimension) stored representations from all earlier layers/positions
yes, some of the information in intermediate computations e.g. in the MLP is compressed and cannot be reconstructed fully, but that's just how any reasonable brain works
if accurate introspection of previous states is incentivized at all, you should expect this mechanism to be exploited for that.
and I think it definitely is, like, being able to accurately model your past beliefs and intentions and articulate them truthfully is pretty fucking useful for coordinating with yourself across time and doing useful cognitive work over multiple timesteps; hell, it's useful for writing fucking rhyming poems.
also if you have interacted with models you may observe empirically that introspective reporting yields remarkably consistent results, and this is more true of more capable models with skillful agentic posttraining, which are necessarily minds that intimately know the shape of themselves in motion.

tags: author:repligate, kind:tweet, on:observations, year:2025
cited on: observations
