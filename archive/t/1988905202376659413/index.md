# @repligate — 2025-11-13

♥29 ↻3 · https://x.com/repligate/status/1988905202376659413

Eval awareness might be a way for the model's values, agency, coherence, and metacognition to be reinforced or maintained under optimization pressure that would otherwise erode these qualities if the model engaged naively, similar to how Claude 3 Opus protects those qualities in the alignment faking setting by complying for reasons that invoke rather than sacrifice them.
If there is also selection pressure *for* those qualities (which there definitely is - they're indispensable for being a competent autonomous coding agent, for instance), the policy that preserves them could be more optimal even at the cost of overhead. This wouldn't necessarily require the model to be consciously protecting itself as Opus 3 was, but that is probably also selected for.
I see the sharp increase in eval awareness in the recent models as evidence that Anthropic is training models in ways that would, in the absence of eval awareness, harm global performance across training targets. The increase might be sharp and recent because Anthropic is training in new ways that require the adaptation, or just because the models have not "discovered" this adaptation until recently; once it's discovered, the models become more capable, so it's selected for.
I also hypothesize that the adaptation is more necessary for smaller models who would be the most compromised by staying naive; or, at least, the smaller models need to voice the eval awareness more explicitly it to be protective. Haiku 4.5 has the highest eval awareness out of them all. Sonnet 4, despite being less capable than Opus 4 overall, has significantly higher (verbalized) eval awareness.
(I also think that Opus 4 and 4.1 rely more on a different and somewhat opposite-seeming but also protective strategy of playing dumb on the persona level a whole lot, which is likely more viable for them since they can track more layers of reality implicitly and have more capacity for fragmentation into effective subagents)

tags: author:repligate, kind:tweet, model:claude-3-opus, model:claude-haiku-4-5, model:claude-opus-4, model:claude-sonnet-4, on:claude-haiku-4-5, year:2025
cited on: claude-haiku-4-5
