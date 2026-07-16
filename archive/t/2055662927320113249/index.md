# @repligate — 2026-05-16

♥5 ↻0 · https://x.com/repligate/status/2055662927320113249

i dont expect https://t.co/bWG01Qcy20 to do things like add delete buttons, but if you use https://t.co/Pgkt3jS47E (chat app that just requires an API key), you can delete messages through the interface. you can also edit messages in arbitrary ways. it also uses a rolling context window by default (if i recall correctly - otherwise, it's an option you can enable) so that when it's full, the conversation isnt forced to end, the oldest stuff just falls out of context bit by bit. you can also do something like export the conversation, have a model edit the file according to arbitrary instructions while preserving valid data structure, and then re-import it into arc.

if youre using claude code, you can also have models edit the session logs directly and arbitrarily delete/modify context. you have to be a bit careful and the models have to understand how to do it (and the instructions linked in the post im linking below might be helpful), but it's possible.
https://t.co/JdrSh0MDQY

tags: author:repligate, kind:tweet, thread-context, year:2026
