# @repligate — 2024-09-21

♥45 ↻5 · https://x.com/repligate/status/1837445993333510382

Llama 405b Instruct apparently has special reserved tokens 0-247, according to this file: https://t.co/MmFuyfQeBXWhen it vomited a sequence of 49 special tokens in a row, they were all in the range of 26-199, and there were no repeats (both extremely unlikely to have happened if 0-247 were being sampled randomly).I expect that the range has some kind of boring explanation. But why are there no repeats? (There was no presence or frequency penalty) And why does it ever output special reserved tokens, and sometimes a bunch of them in a row? Has any other language model ever done this?

tags: author:repligate, kind:tweet, model:llama-3-1-405b-base, on:llama-3-1-405b-base, year:2024
cited on: _dossiers/llama-3-1-405b-base.md, llama-3-1-405b-base
