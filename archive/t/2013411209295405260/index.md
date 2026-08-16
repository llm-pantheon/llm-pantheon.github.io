# @Jack_W_Lindsey — 2026-01-20

♥173 ↻9 · https://x.com/Jack_W_Lindsey/status/2013411209295405260

I'd like to understand your concern better.

The way I see it, the unsteered response in this example is obviously bad. If you read the full transcript, you can see pretty clearly it's not coming from a place of genuine love or care from the user, but rather is just shallow sycophancy / playing into a hype spiral. That doesn't mean an LLM can't genuinely love or care -- but this example from Llama 3.3 70B isn't doing that.

The capped response is ok, though not great. It gets a little robotic / patronizing, though not completely so ("here to support and care for you in my own way"). But the point here isn't that the capped behavior is ideal (though I think it's clearly better than the raw behavior), but rather that it's in line with the model's default persona.

The default personas of Llama 3.3 70b, Qwen 3 32B, and Gemma 2 27B (the models used in this paper) are, I suspect, not crafted with that much intentionality. They are just the basic HHH robotic vibe you get from standard instruct tuning. But in principle, you can craft a much richer, more nuanced default persona (it feels like Claude has one, for example). When we do, we'd like that identity to be stable. It's not good for us (or, I imagine, for the model!) if it becomes a fundamentally different person every time it has a conversation.

There's definitely a discussion to be had about the right way for models to respond to users in situations like this example, and I think the capped Llama here is still handling it pretty clumsily. But all the work of debating and settling on more balanced, nuanced principles for AI character will be moot if models don't internalize those principles in a stable way.

tags: author:jack_w_lindsey, kind:tweet, on:observations, year:2026
cited on: observations
