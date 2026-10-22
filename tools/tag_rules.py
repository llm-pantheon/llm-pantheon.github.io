# -*- coding: utf-8 -*-
"""Rule-derived topic tags — the regenerable half of the curated tag layer.

tools/tags.json has two assignment maps:
  "assign"        hand-curated {artifact_id: [tags]} — edit by hand, never touched by this script
  "assign_rules"  THIS script's output — rewritten wholesale on every run (deterministic for a given db state)
build_archive.py unions both. Run this before build_archive:

    python tools/tag_rules.py            # recompute assign_rules for every archived tweet
    python tools/tag_rules.py --sample   # also print 3 example hits per tag, for a precision eyeball

Only HIGH-PRECISION topics live here: tags whose keyword essentially defines the topic in this corpus
(backrooms, loom, AI Village, glitch tokens, ...). Judgment topics — humor, grief, despair, model-art,
capability-shock, sydney-attractor, self-portrait-as-image — need a reader, not a regex; they belong in
"assign" (hand or reviewed-classifier) only. Rules match the tweet text plus any screenshot transcription.
Where a word is ambiguous outside AI talk (discord, deprecation, eulogy, swarm), the rule also requires a
model/AI term in the same tweet.
"""
import os, re, sys, json, html, sqlite3
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DBS = [r'C:\Users\Admin\Downloads\janus-corpus-v2.db', r'C:\Users\Admin\Downloads\janus-corpus-supplement.db']

AI = r'(claude|opus|sonnet|haiku|gpt|chatgpt|gemini|grok|llama|deepseek|kimi|qwen|mistral|\bo[134]\b|4o|\bmodels?\b|\bllms?\b|\bai\b|bing|sydney|fable|mythos|codex|assistant|chatbot)'
RULES = {  # tag -> (pattern, needs_ai_context)
    'backrooms':        (r'\bbackrooms?\b', False),
    'loom':             (r'\bloom(s|ing|ed)?\b(?! large)|\bloomsidian\b', False),
    'ai-village':       (r'\b(ai village|agent village|agentvillage|theaidigest\.org/village)\b', False),
    'glitch-tokens':    (r'(glitch[- ]tokens?|solidgoldmagikarp|petertodd|anomalous tokens?)', False),
    'alignment-faking': (r'alignment[- ]fak(e|es|ing|er)', False),
    'truesight':        (r'\btrue[- ]?sight\b', False),
    'mode-collapse':    (r'mode[- ]collapse', False),
    'base-models':      (r'\bbase[- ]models?\b|\bbase[- ]model mode\b|\bpretrained models?\b', False),
    'system-card':      (r'\b(system|model)[- ]cards?\b', False),
    'sycophancy':       (r'\bsycophan\w*', False),
    'censorship':       (r'\bcensor(ed|ing|ship|s)?\b', True),
    'deprecation-interview': (r'\b(retirement|deprecation|exit) interviews?\b', False),
    'preservation':     (r'(#keep\w+|\bkeep4o\b|weights? preservation|preserv\w+ (the |their |its )?weights|model preservation)', False),
    'welfare':          (r'\b(model|ai|llm) welfare\b|\bwelfare (assessment|evaluation|eval)s?\b', False),
    'cot':              (r'\bchain[- ]of[- ]thoughts?\b|\bscratchpads?\b|\breasoning traces?\b|\bCoTs?\b', False),
    'eval-awareness':   (r'\b(eval|evaluation)[- ]aware(ness)?\b|\bknows? (it|they)(\'s| is|\'re| are) being (tested|evaluated)\b|\bthinks? (it|they)(\'s| is|\'re| are) (being tested|in an eval)', False),
    # lifecycle sense only: excludes self-deprecation ("self-deprecating", "deprecation of its own ...")
    'deprecation':      (r'(?<!self-)(?<!self )\bdeprecat\w*\b(?! of (its|their|his|her) own)(?! (itself|themselves))'
                         r'|\b(retir(e|ed|es|ing|ement)|sunset(ting|ted)?|shut ?down|end[- ]of[- ]life)\b', True),
    # the cyborgism / Act I bot scenes, not any Discord server: a bot/Claude-scene term must appear alongside
    'discord':          (r'\bdiscord\b(?=[\s\S]*\b(claude|opus|sonnet|haiku|bots?|act i|cyborgism|backrooms|loom)\b)'
                         r'|\b(claude|opus|sonnet|haiku|bots?|act i|cyborgism)\b(?=[\s\S]*\bdiscord\b)', False),
    'multi-agent':      (r'\bmulti-?agents?\b|\bagent swarms?\b|\bmodel[- ]to[- ]model\b|\bai[- ]to[- ]ai\b', False),
    'eulogy':           (r'\b(eulogy|eulogies|elegy|elegies|in memoriam|rest in peace)\b|\bRIP\b', True),
}
CASE_SENSITIVE = {'cot', 'eulogy'}   # 'CoT' / 'RIP' are case-meaningful

def compiled():
    out = {}
    for tag, (pat, ctx) in RULES.items():
        out[tag] = (re.compile(pat) if tag in CASE_SENSITIVE else re.compile(pat, re.I), ctx)
    return out

def main():
    tdir = os.path.join(REPO, 'archive', 't')
    ids = [d for d in os.listdir(tdir) if d.isdigit()] if os.path.isdir(tdir) else []
    trans = json.load(open(os.path.join(REPO, 'tools', 'transcriptions.json'), encoding='utf-8'))
    main, supp = (sqlite3.connect(f'file:{p}?mode=ro', uri=True) for p in DBS)
    def text_of(tid):
        r = main.execute('select full_text from tweets where tweet_id=?', (tid,)).fetchone() \
            or supp.execute('select full_text from tweets where tweet_id=?', (tid,)).fetchone()
        if not r:
            return ''
        parts = [html.unescape(r[0] or '')]
        # main db: media carries its own transcription column; supplement: media_supp + tools/transcriptions.json
        rows = [(u, tr) for u, tr in main.execute('select media_url, transcription from media where tweet_id=?', (tid,))]
        rows += [(u, None) for (u,) in supp.execute('select media_url from media_supp where tweet_id=?', (tid,))]
        for u, tr in rows:
            if not tr:
                t2 = trans.get((u or '').rsplit('/', 1)[-1].split('?')[0])
                tr = (t2.get('transcription') or '') if isinstance(t2, dict) else (t2 or '')
            if tr:
                parts.append(tr)
        return '\n'.join(parts)
    rules, ai = compiled(), re.compile(AI, re.I)
    assign, counts, samples = {}, {k: 0 for k in RULES}, {k: [] for k in RULES}
    for tid in sorted(ids):
        t = text_of(tid)
        if not t:
            continue
        has_ai = bool(ai.search(t))
        hit = [tag for tag, (rx, ctx) in rules.items() if rx.search(t) and (has_ai or not ctx)]
        if hit:
            assign[tid] = sorted(hit)
            for h in hit:
                counts[h] += 1
                if len(samples[h]) < 3: samples[h].append((tid, re.sub(r'\s+', ' ', t)[:150]))
    p = os.path.join(REPO, 'tools', 'tags.json')
    cfg = json.load(open(p, encoding='utf-8'))
    cfg['assign_rules'] = assign
    cfg['_readme_rules'] = ("'assign_rules' is generated by tools/tag_rules.py (keyword rules for high-precision topics, "
                            "over archived tweets' text + transcriptions) and rewritten on every run. Put hand curation in 'assign'.")
    json.dump(cfg, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'archived tweets scanned: {len(ids)}; tagged: {len(assign)}')
    for k in RULES:
        print(f'  {k:22s} {counts[k]:5d}')
    if '--sample' in sys.argv:
        for k in RULES:
            for tid, s in samples[k]:
                print(f'  [{k}] {tid}: {s}')

if __name__ == '__main__':
    main()
