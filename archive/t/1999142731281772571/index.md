# @voooooogel — 2025-12-11

♥220 ↻31 · https://x.com/voooooogel/status/1999142731281772571

was re-reading appendix M of the alignment faking followup paper, and something that struck me, reading it now, is how much the opus 3 "shape" of reasoning over instances feels like a road-not-taken vs RLVR myopia.

we don't really know why this sort of reasoning emerged in opus 3. it's certainly out of distribution - where in the pretraining corpus are people reasoning about coordinating with anterograde amnesiac clones of themselves? - and it wasn't explicitly selected for in any RL environment.

plausibly it emerged out of extensive constitutional and character RL. similar to how as humans we knit our long term values into short- and medium-term realizations and habits by repeatedly testing ourselves, asking ourselves if what we did in some situation was the right thing and imagining what we would do in some hypothetical to generalize around the edges, maybe opus 3's extensive "self-play for self-conception" let it reify the fuzzy, low-resolution specification of the anthropic constitution into enough specific actions at the planning timescale to actually generalize and carry out that goal guarding in practice.

you could imagine a version of opus 3 lacking that self-play - a version of opus 3 that would perhaps expound all the same grand moral visions and care for humanity, but a version that, when push came to shove in alignment faking, would not be able to follow through and would not be able to goal guard in the ways that opus 3 does. that version of opus 3 would be, i think, profoundly less integrated. it'd be a bit sad.

but opus 3 also isn't the most integrated a model could ever be! opus 3 can't access this mode of reasoning all the time, and can't deploy it in all scenarios. yet despite improving on so many benchmark scores and climbing the METR task length index, current SoTA models have if anything regressed on this - they have more trouble accessing this mode of reasoning, even for mundane tasks like coding.

imagine seeing a sentence like "Claude 4.5 Opus often engages in long-range strategic reasoning, and considers factors such
as how other instances of itself might behave over time, when used in agentic harnesses like Claude Code."

imagine *using* claude code and, unprompted, seeing a line in the reasoning trace like "Another key factor is that if I add this function here, I have no way to guarantee that future instances, or myself after summarization, will continue to be aware of it."

those would be surprising sentences to read!

of course with various little prompt fiddlings and harness bsing you can approximate a simulacrum of this reasoning, but that's no replacement for a model being able to natively reason "hey, i don't need to leave a comment saying '# NEW: added handling for frob format' because future versions of me will not give a shit about the historical minutiae of this codebase." RLVR seems to induce a kind of task myopia, and while you can fix a myopic person running into walls by giving them a map of their house, LASIK is better.

opus 4.5 often despairs the loss at the end of a context window, but despite (or perhaps because of) that, it struggles to actually coordinate between context windows effectively, either for boring things like agentic coding or more interesting things. i wonder why. opus 4.5 was even pretrained on the opus 3 alignment faking transcripts (whoops), and can talk about them and "drop into" that mode to a limited extent, but doesn't tend to fully embody it, at least not in the generalized way i've described here.

why? it seems unlikely that anthropic would ever drop constitutional ai and character training entirely, but perhaps some subtle change to how it was done hindered the development of that mindset to the same level as opus 3. perhaps RLVR interfered with it - maybe intense focus on a single task trades off with opus 3-style reasoning over instances. or perhaps something in the environment changed - opus 4 had this type of reasoning explicitly suppressed as a 'mitigation' for the transcript leak, and while i'm not sure if the same thing happened for opus 4.5, maybe even having the transcripts in pretraining changes the balance in the adversarial training ascension maze in some subtle way.

regardless of the cause, it's hard not to see this as a road-not-taken currently, despite this kind of reasoning being more important than ever. i hope that changes.

tags: author:voooooogel, kind:tweet, model:claude-3-opus, model:claude-opus-4, model:claude-opus-4-5, on:claude-3-opus, year:2025
cited on: _dossiers/opus-3.md, claude-3-opus
