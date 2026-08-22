# @solarapparition — 2024-04-11

♥1 ↻0 · https://x.com/solarapparition/status/1778245530222510472

I only vaguely understand the technical bits, but it sounds like they have a separate attention mechanism that stores compressed, global attention info. Makes sense conceptually, and I assume this is how they got Gemini 1.5 to a million token context length.Wonder if this takes the wind out of the sails of model architectures whose primary advantage is handling long context, such as Mamba—always felt like it wasn’t worth it to use an entirely different architecture just to deal with the context window scaling issue, especially since the attention part of training isn’t even the bulk of the compute requirement for transformers.Also, this part could be pretty valuable—seems like you can just bolt this on to existing pretraining pipelines. Not having to reinvent the wheel is a nice perk.

tags: author:solarapparition, kind:tweet, on:gemini-1-5-pro, year:2024
cited on: _dossiers/gemini-1-5-pro.md, gemini-1-5-pro
