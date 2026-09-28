"""Reddit 키워드별 게시물 건수 집계 (PRAW).

Reddit 검색은 형태소 확장·퍼지 매칭 때문에 "holotomography" 검색에도
"holography" 글이 섞여 나온다. 그래서 두 가지 숫자를 함께 기록한다.
  - raw_hits  : Reddit 검색이 돌려준 게시물 수 (노이즈 포함)
  - exact_hits: 제목/본문에 키워드가 실제로 들어 있는 게시물 수 (정규식 검증)

사용법:
  pip install praw pandas
  export REDDIT_CLIENT_ID=...  REDDIT_CLIENT_SECRET=...
  python count_keywords.py
"""
import os
import re
import time

import pandas as pd
import praw

KEYWORDS = {
    "core": ["holotomography", "holotomographic"],
    "broader": [
        "label-free imaging",
        "quantitative phase imaging",
        "refractive index tomography",
    ],
    "brand": ["Tomocube", "Nanolive"],
}

# 정확 매칭 패턴: 하이픈/공백 변형 허용 ("label free imaging", "NanoLive" 등)
def exact_pattern(term: str) -> re.Pattern:
    parts = re.split(r"[\s\-]+", term)
    return re.compile(r"\b" + r"[\s\-]?".join(map(re.escape, parts)) + r"\w*", re.I)


def main() -> None:
    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent="keyword-count/0.1 (research)",
    )
    summary, posts = [], []
    for group, terms in KEYWORDS.items():
        for term in terms:
            pat = exact_pattern(term)
            raw = exact = 0
            # 따옴표로 구문 검색. Reddit 검색은 쿼리당 최대 약 1,000건까지만 반환.
            for s in reddit.subreddit("all").search(f'"{term}"', sort="new", time_filter="all", limit=None):
                raw += 1
                text = f"{s.title}\n{s.selftext}"
                hit = bool(pat.search(text))
                exact += hit
                posts.append({
                    "group": group, "keyword": term, "exact_match": hit,
                    "id": s.id, "subreddit": str(s.subreddit), "title": s.title,
                    "created_utc": pd.to_datetime(s.created_utc, unit="s"),
                    "score": s.score, "num_comments": s.num_comments,
                    "url": f"https://www.reddit.com{s.permalink}",
                })
            summary.append({"group": group, "keyword": term, "raw_hits": raw, "exact_hits": exact})
            print(f"[{group:8}] {term:30} raw={raw:5} exact={exact:5}")
            time.sleep(1)

    df = pd.DataFrame(posts)
    exact_df = df[df.exact_match] if not df.empty else df
    pd.DataFrame(summary).to_csv("keyword_counts.csv", index=False)
    df.to_csv("posts_all.csv", index=False)
    if not exact_df.empty:
        print(f"\n고유 게시물(정확 매칭, 중복 제거): {exact_df.id.nunique()}")
        print("\n상위 서브레딧:")
        print(exact_df.drop_duplicates("id").subreddit.value_counts().head(15).to_string())


if __name__ == "__main__":
    main()
