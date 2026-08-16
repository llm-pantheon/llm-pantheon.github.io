# @repligate — 2025-09-10

♥15 ↻0 · https://x.com/repligate/status/1965675596127916061

yes, they are similar at a higher level of abstraction

but reinforcement learning usually means something more specific, which is that the model generates specific actions or sequence of actions, which is assigned a reward, allowing it to learn through "trial and error"

the difference here is that the model doesn't generate any "actions" - no tokens are generated. It just predicts a probability distribution (which is never sampled), and is updated to assign more probability to the predetermined right answer.

this is a significant difference in part because the model never generates sequences during pretraining, so it doesn't update on the consequences of its own actions. It never gets into a state where the context is determined by its own previous actions. and the "right answer" is solely defined by pre-recorded samples rather than being open-ended (anything that achieves high reward). A related concept is "teacher forcing".

tags: author:repligate, kind:tweet, thread-context, year:2025
