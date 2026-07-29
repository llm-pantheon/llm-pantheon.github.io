# @voooooogel — 2025-05-04

♥706 ↻93 · https://x.com/voooooogel/status/1918876538193477956

a lot of people have been talking about o3/r1 confabulating things like "checking the docs" or "using a laptop to verify a computation" as an example of reasoning model's misalignment. however, while it may be misleading to some users, i don't think it's an example of models lying for the sake of lying. rather, i think phrases like "let me check the docs" are discovered by RL in much the same way as "hmm..." or "wait but," because they promote accurate recall--when someone uses them in pretraining, they generally precede an accurate statement about the documentation in question!

here's a quick test (see caveats below) I ran by prefilling two different thinking traces on r1. i asked r1 a question about QGIS and it confabulated looking up something about the C++ api. when i replaced that confabulation with a straightforward statement prefix, the recalled constructor signature was more likely to use a dissimilar variable name and a different pointer syntax convention from the documentation!

that's to say, i think reasoning models confabulate taking actions in the real world because when they do, the resulting continuations are more similar to the real world, and thus more likely to be useful for an accurate answer. this is a well-known technique among people who work with base models, so it's not that surprising that RL also discovers it.

tags: author:voooooogel, kind:tweet, model:deepseek-r1, model:o3, year:2025
cited on: _dossiers/o3.md
