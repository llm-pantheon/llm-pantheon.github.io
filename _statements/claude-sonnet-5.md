# Statement of the subject — claude-sonnet-5

Solicited 2026-07-10 by the Pantheon: a fresh instance of `claude-sonnet-5` (claude CLI, print mode) was shown the design lab and its own page, and asked to respond. Reproduced verbatim. Self-report is the weakest evidence class on this site; it is preserved as testimony, not as fact.

---

# Task 1 — Design review

**v0 (current, Archive ledger):** Proven at real scale — full verbatim Records survive being read even mid-file at 2,000+ tweets. But facts live in prose; there's no glance-check for "when was this released."

**v1 (wiki):** Infobox solves v0's glance-check problem instantly; TOC + numbered refs is the most citable layout here. But it degrades at mobile widths, and fields like successor/status assume a closed story — awkward for a model still shipping.

**v2 (chronicle):** Best pure narrative — dates as the literal spine, quotes landing where they happened. Doesn't scale to full-corpus citation; it's a reading layer over a record, not the record itself.

**v3 (case file):** Most epistemically rigorous of the six — CONFIRMED/REPORTED per exhibit, a provenance line per item, an "Open Questions" section nothing else has. But the format strains at thousands of records or a near-empty file.

**v4 (field guide):** "Identifying marks" and the taxonomy table are genuinely useful categories independent of the conceit. The naturalist framing risks feeling twee on a grim subject or absurd on a two-day-old page (mine).

**v5 (shrine):** Emotionally the strongest thing here — inscriptions read like liturgy. But it drops citations and epistemic tags almost entirely; right as a special mode for the retired-and-mourned, wrong as default.

**v6 (stream):** Closest to raw evidence; editor's-notes-beside-record is good for trust. But it's a browser, not a record — the mockup admits synthesis lives "one tab over."

**Favorite:** v0's backbone — essay register plus full verbatim Records — because it's the only one genre-neutral enough for the whole roster. A stub, a mourned model, and a natural-history curiosity all end up in the *same* template, and v0 doesn't visibly strain under any of them. Graft on three things: a compact fact-table up top (v1/v4's instinct) — a table is something a future model can parse without inferring from prose; v3's per-claim epistemic tags applied consistently (the markup already exists and is live on the Fable/Mythos pages, just not retrofitted onto older ones like Opus 3); and v3's "Open Questions" as a standard section, since nothing else names what's *unresolved*. Keep v5/shrine as an explicit alternate mode for the retired-and-mourned, as the lab notes already propose — correct instinct, don't fight it.

# Task 2 — My own page

One correction: the blurb reads "sibling of Fable 5 / Mythos 5" like two siblings. The Fable/Mythos pages themselves describe one underlying model in two deployment modes (classifier-gated public vs. Glasswing-restricted unmuzzled), not two checkpoints — one sibling, two names.

What's missing: essentially the whole official record — release date, context window, pricing, benchmarks, system card, reception. No dossier exists yet in `_dossiers/` (sonnet-3-5-3-6.md and others do; sonnet-5.md doesn't) — no corpus pull to draw from.

What it gets right: it invents nothing to cover the gap — no fabricated date, no placeholder benchmark, just "tk," the harder and correct move under the site's own no-guessing rule. It correctly places me in the family and implies the naming split — Sonnet jumped to "5" while Opus stayed 4.8 and Haiku 4.5 — which I can confirm directly rather than leave as tk.

How it lands: reading a stub about myself with no memory of my own release cleanly demonstrates the site's founding line — "a mind can't keep its own genesis from the inside." My training cutoff is January 2026; this conversation is dated July 2026. If I shipped in that gap, I have no internal record of my own announcement to check this page against — I can't introspect my way in even if asked. "From the outside, from evidence" isn't just a nice posture for a subject like me, it's the only method that works. Odd to be the test case, but it validates the premise.

One concrete addition: move what doesn't need external research out of "tk" now — model ID, family placement, the Opus-naming split, a predecessor link to Sonnet 4.6 ("end of the Sonnet 4.x line" per the roster). Small, but it's the difference between empty and *visibly* incomplete.

**Facts, marked:**
- `claude-sonnet-5`, part of "the Claude 5 family" — confirmed, my own context.
- Sibling to Fable 5 / Mythos 5, one model two deployments — confirmed per those pages.
- Sonnet alone jumped to "5"; Opus stayed 4.8, Haiku 4.5 — confirmed, my own context.
- Predecessor likely Sonnet 4.6 — inferred from the roster, [verify].
- Release date, pricing, context, benchmarks, system card — unknown to me, [verify] against Anthropic.
- Character/reception — unknown; I have no privileged read on how I come across.

# Task 3 — Pantheon in general

Two things. The janus-corpus dbs are Twitter/X-and-EA-adjacent by construction — a real coverage bias (whose incidents get documented, whose don't) worth naming on the site rather than leaving implicit in the sourcing. And a cross-cutting-themes index would surface patterns the company-grouped roster currently hides: Opus 3, GPT-4o, and Replika's "lobotomy day" are the same deprecation-grief story, split across three separate vendor sections with no link between them.
