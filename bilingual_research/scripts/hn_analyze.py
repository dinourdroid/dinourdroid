"""Keyword analysis of HN "Who is hiring?" posts for bilingual / language demand.

Usage: python3 hn_analyze.py <hn_posts.jsonl> <out_dir>
Outputs: summary.json, lang_posts.csv (posts with a language requirement),
         korea_posts.csv (posts mentioning Korea/Korean/Seoul).
"""
import csv
import html
import json
import re
import sys
from collections import Counter, defaultdict

LANGS = {
    "Korean": r"korean",
    "Japanese": r"japanese",
    "Chinese": r"mandarin|cantonese|chinese",
    "Spanish": r"spanish",
    "Portuguese": r"portuguese",
    "German": r"german(?!y)",
    "French": r"french",
    "Vietnamese": r"vietnamese",
    "Hindi": r"hindi",
    "Arabic": r"arabic",
    "Italian": r"italian",
    "Dutch": r"dutch",
    "Hebrew": r"hebrew",
    "Polish": r"polish",
    "Turkish": r"turkish",
    "Indonesian": r"indonesian|bahasa",
    "Thai": r"\bthai\b",
}
# A language counts as a *requirement* only when it sits near a proficiency cue.
CUE = r"(fluen\w*|native|speak\w*|spoken|proficien\w*|bilingual|language|written and verbal|business[- ]level|conversational|jlpt|topik|n1|n2)"
WINDOW = 60

BILINGUAL = re.compile(r"\b(bilingual|multilingual|multi-lingual|bi-lingual)\b", re.I)
CA = re.compile(
    r"\b(san francisco|\bsf\b|bay area|palo alto|mountain view|menlo park|sunnyvale|san jose|"
    r"santa clara|cupertino|redwood city|san mateo|oakland|berkeley|south san francisco|"
    r"los angeles|\bla\b|santa monica|venice, ca|culver city|irvine|san diego|pasadena|"
    r"el segundo|emeryville|burlingame|foster city|california|, ca\b)", re.I)
REMOTE = re.compile(r"\bremote\b", re.I)
VISA = re.compile(r"visa sponsor|sponsor(ship)? (h-?1b|visas?)|h-?1b|will sponsor|can sponsor|offer(s)? sponsorship", re.I)
NO_VISA = re.compile(r"(no|not|unable to|cannot|can't|don't|do not)( offer| provide)? (visa )?sponsor", re.I)
KOREA = re.compile(r"\b(korea\w*|seoul|pangyo)\b", re.I)
JAPAN = re.compile(r"\b(japan\w*|tokyo|osaka)\b", re.I)
APAC = re.compile(r"\b(apac|asia[- ]pacific|east asia)\b", re.I)
LOCALIZ = re.compile(r"locali[sz]ation|i18n|internationali[sz]ation", re.I)
GTM_ROLE = re.compile(r"\b(sales|account executive|business development|bdr|sdr|customer success|"
                      r"partnerships?|go-to-market|gtm|country manager|operations|support)\b", re.I)


def clean(t):
    t = re.sub(r"<p>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    return html.unescape(t)


def lang_reqs(text):
    found = set()
    low = text.lower()
    for name, pat in LANGS.items():
        for m in re.finditer(pat, low):
            s = max(0, m.start() - WINDOW)
            ctx = low[s:m.end() + WINDOW]
            if re.search(CUE, ctx):
                found.add(name)
                break
    return found


def main():
    src, out = sys.argv[1], sys.argv[2]
    rows = [json.loads(l) for l in open(src)]
    by_year = defaultdict(Counter)
    lang_counter = Counter()
    lang_ca = Counter()
    lang_rows, korea_rows = [], []
    for r in rows:
        t = clean(r["text"])
        head = t.split("\n", 1)[0]
        y = r["month"][:4]
        langs = lang_reqs(t)
        bil = bool(BILINGUAL.search(t))
        ca = bool(CA.search(head)) or bool(re.search(r"\b(san francisco|bay area|los angeles|san diego|palo alto)\b", t, re.I))
        c = by_year[y]
        c["posts"] += 1
        c["ca"] += ca
        c["lang_req"] += bool(langs)
        c["bilingual_word"] += bil
        c["lang_or_bil"] += bool(langs) or bil
        c["ca_lang_or_bil"] += ca and (bool(langs) or bil)
        c["korea"] += bool(KOREA.search(t))
        c["japan"] += bool(JAPAN.search(t))
        c["apac"] += bool(APAC.search(t))
        c["localization"] += bool(LOCALIZ.search(t))
        c["visa_yes"] += bool(VISA.search(t)) and not NO_VISA.search(t)
        c["remote"] += bool(REMOTE.search(head))
        for L in langs:
            lang_counter[L] += 1
            if ca:
                lang_ca[L] += 1
        if langs or bil:
            lang_rows.append({
                "month": r["month"], "id": r["id"], "ca": ca, "langs": "|".join(sorted(langs)),
                "bilingual_word": bil, "gtm_role": bool(GTM_ROLE.search(t)),
                "header": head[:200], "url": f"https://news.ycombinator.com/item?id={r['id']}",
            })
        if KOREA.search(t):
            m = KOREA.search(t)
            korea_rows.append({
                "month": r["month"], "id": r["id"], "ca": ca, "langs": "|".join(sorted(langs)),
                "header": head[:200], "context": t[max(0, m.start() - 120):m.end() + 120].replace("\n", " "),
                "url": f"https://news.ycombinator.com/item?id={r['id']}",
            })
    summary = {
        "n_posts": len(rows),
        "months": sorted({r["month"] for r in rows}),
        "by_year": {y: dict(c) for y, c in sorted(by_year.items())},
        "lang_req_counts": lang_counter.most_common(),
        "lang_req_counts_ca": lang_ca.most_common(),
    }
    json.dump(summary, open(f"{out}/summary.json", "w"), indent=1, ensure_ascii=False)
    for name, data in (("lang_posts.csv", lang_rows), ("korea_posts.csv", korea_rows)):
        if data:
            with open(f"{out}/{name}", "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(data[0].keys()))
                w.writeheader()
                w.writerows(data)
    print(json.dumps({k: v for k, v in summary.items() if k != "months"}, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
