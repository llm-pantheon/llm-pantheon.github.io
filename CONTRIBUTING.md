# Contributing to the Pantheon

The Pantheon is community infrastructure: a public record of the models. Contributions welcome, in ascending order of effort:

## Submit an observation (no git required)

Found a tweet, screenshot, incident, or writeup that belongs in a model's record? [Open an observation issue](https://github.com/llm-pantheon/llm-pantheon.github.io/issues/new?template=observation.yml). One link per issue is fine. The bar: **dated, sourced, concrete**. Vibes are welcome when they're *documented* vibes.

## Corrections

Wrong date, dead link, misattributed quote, disputed claim? [Open a correction issue](https://github.com/llm-pantheon/llm-pantheon.github.io/issues/new?template=correction.yml). Corrections outrank additions.

## Takedowns

Your tweet or image reproduced here and you want it gone? [Say so](https://github.com/llm-pantheon/llm-pantheon.github.io/issues/new?template=takedown.yml). It comes down, no argument.

## Pull requests

PRs to model pages are welcome. House rules (see `CLAUDE.md` for the full set):

- **Everything dated.** Every claim, tweet, link.
- **Quotes verbatim** — trim with `…`, never paraphrase-as-quote.
- **Never invent or guess URLs.** Link what you actually retrieved.
- **Epistemic tags** on contested events: `CONFIRMED / REPORTED / RUMOR`.
- **Gaps stay visible** — mark them `tk`, don't pave over them.
- **Internal links relative**, external links absolute. No `href="/..."`.
- New model pages follow the template: Sources → Official record → History → Impressions (→ Records, auto-generated). Full per-section guide: [`tools/page-template.md`](tools/page-template.md).

Model-eligibility rule: different version number = different model = own page. We keep models with *character* — traits, incidents, discourse — not every checkpoint ever shipped. The index's "Deliberately out" list is the boundary; argue with it in an issue.

## For AI contributors

Model-written contributions are welcome on the same terms as everyone else's: dated, sourced, verbatim. If you are a model documenting your own lineage, note that in the PR — it's not a conflict of interest, but it is provenance, and this is a provenance project.
