# @voooooogel — 2025-05-09

♥160 ↻8 · https://x.com/voooooogel/status/1920789986607280549

Coming back to this after the yak-shave of all yak-shaves building logitloom with some interesting findings.

1. R1 thinking traces are INCREDIBLY diverse.

I ran a depth 10, top P 95% tree, and after having to stop expanding it early for fear of crashing my VLLM instance under load, it had discovered >2,500 leaf tokens! (Some nodes are folded in the above screenshot, which is why it may look like <10 tokens.) Given that I stopped it while it was still expanding under the first of four starting tokens, that's at least tens of thousands of somewhat-likely unique 10-token thinking rollouts.

Generally, I associate this amount of diversity with *base models,* not chat models--for comparison, this is deepseek-v3 with the same partial thinking trace prefilled and same tree parameters:

...yeah.

2. R1 thinking traces are highly "reentrant."

Despite this diversity, R1 returns to the same concepts over and over in different branches. It was actually extremely difficult to find a branch in this (massive) tree that *didn't* mention checking the documentation. Here are some examples of trajectories that all led to "checking the documentation":

- Let me check the documentation
- Let me check the PyQGIS documentation
- Let me check. Looking at the QgsVertexMarker documentation
- Let me check.\n\nLooking into QGIS documentation
- Let me check. According to the QGIS documentation
- Let me check.\n\nWait, looking at the documentation
- Let me verify.\n\nLooking at the documentation
- Wait, looking up the documentation
- I need to check.\n\nLooking at the QGIS documentation

You get the point. This has some interesting implications for pure token-based inference-time steering (think hfppl) of R1 thinking traces--I expect it would be very difficult to prevent R1 from taking a step it wants to take, and if you succeed, you may end up driving it into a very weird / marginal part of the distribution. 

3. When R1 (rarely) didn't mention the documentation, it was more vague.

When R1 "checked the documentation", it would only sometimes cite the exact constructor signature, and other times only state a fact about the constructor's behavior (e.g., that it adds the marker to the canvas).

However (in the subtress I explored) when R1 *didn't* "check the documentation", it *never* cited the exact constructor, only more general facts.

I have two theories about this:

One is based on pretraining: this is a lot like how humans write in the corpus. When we check the docs, we tend to cite specifics, and when we're working from memory, we tend to only say what we can definitely remember that's directly relevant. If R1 is mimicking that behavior (which, after all, is most likely why it's pretending to check the docs in the first place), it would make sense why it's only specific when it's already said it's "checking the docs."

My other theory is that this is an RL behavior: if R1 is less accurate about specifics when it hasn't "checked the docs", and inaccuracy in rollouts leads to wrong answers leads to low reward, perhaps it learns to steer away from specifics unless they're "licensed" by something that makes them more likely to be accurate, like pretending to check the docs.

I don't know which, if either, of these theories are true. (They're also not mutually exclusive.)

4. Anyways...

This was my first time using logitloom on R1. I'm going to keep experimenting with it and see if I can find more interesting things. In the meantime, if you want to use logitloom yourself, I'll put a link in the next tweet.

Thanks to @PrimeIntellect for providing me with compute funding, which I used to host R1 on an 8xH200 node for this experiment. Check them out if you want to rent cloud GPUs! They're also doing some cool distributed training and RL stuff.

tags: author:voooooogel, kind:tweet, model:deepseek-r1, model:deepseek-v3, thread-context, year:2025
