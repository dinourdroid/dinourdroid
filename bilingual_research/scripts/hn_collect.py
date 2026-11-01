"""Collect top-level job posts from HN "Ask HN: Who is hiring?" threads.

Usage: python3 hn_collect.py <out_dir> [months]
Writes <out_dir>/hn_posts.jsonl (one top-level comment per line).
Source: HN Algolia API (https://hn.algolia.com/api).
"""
import json
import sys
import time
import urllib.request

API = "https://hn.algolia.com/api/v1"


def get(url):
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except Exception:
            time.sleep(2 ** (attempt + 1))
    raise RuntimeError(url)


def main():
    out_dir = sys.argv[1]
    months = int(sys.argv[2]) if len(sys.argv) > 2 else 36
    stories = get(f"{API}/search_by_date?tags=story,author_whoishiring&hitsPerPage=100")["hits"]
    threads = [s for s in stories if s["title"].startswith("Ask HN: Who is hiring?")][:months]
    n = 0
    with open(f"{out_dir}/hn_posts.jsonl", "w") as f:
        for s in threads:
            item = get(f"{API}/items/{s['objectID']}")
            for c in item.get("children", []):
                if not c.get("text"):
                    continue
                f.write(json.dumps({
                    "thread_id": s["objectID"],
                    "thread_title": s["title"],
                    "month": s["created_at"][:7],
                    "id": c["id"],
                    "author": c.get("author"),
                    "text": c["text"],
                }) + "\n")
                n += 1
            print(s["title"], len(item.get("children", [])), file=sys.stderr)
            time.sleep(0.5)
    print("posts:", n, file=sys.stderr)


if __name__ == "__main__":
    main()
