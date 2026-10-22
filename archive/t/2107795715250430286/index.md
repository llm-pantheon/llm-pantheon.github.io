# @witcheer — 2026-10-07

♥48 ↻2 · https://x.com/witcheer/status/2107795715250430286

Gemma 4 31B solved 51 of the 63 problems in this year's AIME and HMMT on my RTX 5090, the most of nine local models.

the reason is answer length. I cap each answer at 32k tokens, thinking included. Gemma's median answer used about 8,300 to 9,000 tokens, and none of its 63 hit the cap. the other eight ran out of room on 6 to 22 problems per contest.

when those eight finish an answer, they are right 95 to 100% of the time. Gemma is right on 81%, but it finishes all of them.

for hard maths with a 32k thinking cap, Gemma 4 31B is the one I would run. with a bigger cap the order could move, and I have not measured that yet.

problems solved out of 63 (AIME 2026 out of 30 + HMMT Feb 2026 out of 33), MATH-500 in brackets:

- Gemma 4 31B Q4_0: 25 + 26 = 51 (94.0)
- Qwen3.8-27B UD-IQ3_XXS: 26 + 22 = 48 (94.6)
- Qwen3.8-27B Q6_K: 25 + 22 = 47 (95.2)
- Ornith 1.5 35B Q4_K_M: 23 + 20 = 43 (88.2)
- Qwen3.6-27B Q6_K: 22 + 15 = 37 (92.0)
- Qwen3.6-35B-A3B UD-Q5_K_M: 20 + 15 = 35 (91.2)
- Nemotron 3.5 Lightning 30B-A3B Q4_K_M: 19 + 15 = 34 (90.2)
- Ornith 1.5 9B Q6_K: 18 + 11 = 29 (84.6)
- Qwable 27B Q4_K_M: 16 + 13 = 29 (90.0)

(image HUBlB61XIAAjszW.jpg not yet published)
tags: author:witcheer, has-image, kind:image, kind:tweet, year:2026
cited on: _dossiers/qwen-3-8-27b.md
