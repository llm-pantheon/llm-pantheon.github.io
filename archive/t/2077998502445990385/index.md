# @witcheer — 2026-07-17

♥40 ↻1 · https://x.com/witcheer/status/2077998502445990385

epoch 1 done: 8 nights, 54,000 steps, one RTX 5090, and Hermes-4.3-36B has its first EAGLE-3 draft head. 

release bench with cuda graphs and tree decode: 1.38x prose, 1.38x code, 1.57x repetitive, 1.29x chat. tree-3-4-8 wins every workload.

it converged at step 21,000: the epoch-end bench reproduces the 39%-of-epoch dry run within noise, so 60% of the training brought nothing special. 

and the 1.7-2.2x trained-head band stays out of reach at batch 1 on one card: deeper trees push accept-len to 2.22 and still land short, the draft cost eats the acceptance gain.

working on an epoch 2 based on these findings :)

(image HNaIhaPWkAE88Mf.jpg not yet published)
tags: author:witcheer, has-image, kind:image, kind:tweet, model:nous-hermes, year:2026
cited on: _dossiers/nous-hermes.md
