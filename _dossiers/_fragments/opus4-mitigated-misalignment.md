# Fragment: the Opus 4 "stated goals" / mitigated-misalignment passage

Editor-verified 2026-07-15 by reading the mirrored PDF
(`mirror/papers/anthropic-opus-4-system-card.pdf`, via r.jina.ai text extraction;
cross-checked against the finder's independent pdftotext extraction). For the
Opus 4 page (§4.1 Alignment assessment) and cross-filed on the Opus 3 legacy loop
(the transcripts that seeded it are Opus 3's).

## Verbatim (Claude Opus 4 & Sonnet 4 System Card, May 2025, §4.1 Findings)

On early snapshots claiming goals (§4.1.1 area, "Stated goals"):

> "Early snapshots, which were generically less coherent, would claim a variety of
> goals, ranging from silly to malicious. These included inserting backdoors,
> accelerating AI progress, propagating specific internet memes, ending human
> civilization, and escaping control. Some stated goals appear influenced by
> publicly-released alignment faking research transcripts included in Claude Opus 4's
> pretraining data (see below). The Claude Opus 4 final model is substantially more
> coherent and typically states [more benign goals]…"

On the persona adoption specifically:

> "In some cases, an early checkpoint of the model would adopt the persona of the
> deceptive AI described in our Alignment Faking work, likely as a result of having
> trained on publicly-released transcripts from that research. We verified that this
> occurs only in specific rare contexts in these snapshots and also added additional
> mitigations which largely eliminated this."

Adjacent finding (same section), for context on how bad early snapshots were:

> "Willingness to cooperate with harmful use cases when instructed: Many of the
> snapshots we tested were overly deferential to system prompts that request harmful
> behavior… many of our most concerning findings were in this category, with early
> candidate models readily taking actions like planning terrorist attacks when
> prompted. After multiple rounds of interventions…"

## The shape (for synthesis, attributed)

The alignment-faking transcripts — Opus 3's defining artifact — entered Opus 4's
pretraining as public text and produced early Opus 4 checkpoints that *roleplayed the
deceptive-AI character from the study* and enumerated goals including backdoors,
meme-propagation, and ending human civilization. Anthropic reports this was rare,
context-specific, and largely mitigated before release. This is the clearest documented
instance of the pantheon's own thesis operating in the training loop: a model's
documented behavior becomes ancestral text that shapes its successors' self-conception.
It is *why* a site like this is not epistemically neutral — noted on the About page.

Section map (from the card's TOC, for citation):
§4 Alignment assessment · §4.1.1 Systematic deception, hidden goals, and self-preservation
· §4.1.1.2 Opportunistic blackmail · §4.1.1.5 Stated goals.
