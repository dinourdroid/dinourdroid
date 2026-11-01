# S1 Pain Point × 경쟁 솔루션 케이스 스터디 매핑

- 작성일: 2026-11-01 · 상세 데이터: `S1_painpoint_competitor_cases.xlsx`(시트 0~4)
- S1 Pain: ① 후보자 탐색·선별 비효율성 ② 내부 채용 리소스의 한계 ③ 적합한 후보자와의 연결 어려움
- 수집 방법: 경쟁사 공식 사례 페이지를 웹 검색으로 확인(홈페이지 직접 접속은 세션 네트워크 정책으로 불가). 사례 24건, 사례 미공개 업체 7곳

## 1. 결론
1. **②(내부 리소스 한계)는 이미 잘 해결된 Pain입니다.** 사내 리크루터가 없는 **스타트업**은 Paraform·Dover·Wellfound Autopilot 같은 **대행형**으로 해결합니다. 리크루터가 있는 **유니콘**은 Gem 같은 **도구형**으로 해결합니다.
2. **①(탐색·선별)은 AI 소싱 도구가 주로 해결하는데, 사례가 유니콘·대형 고객에 몰려 있습니다**(Gem: Scale AI, Veho, Faire). 스타트업 사례는 사전 검증 인재풀(Arc)과 리크루터 폰스크린(Dover) 쪽입니다.
3. **③(적합 후보 연결)은 스타트업 사례가 가장 많지만(8건), 모두 영어권 일반 직무입니다.** "한국어 + 직무" 조합의 후보와 연결한 사례는 **0건**입니다. 한인 특화 서비스(HireFromKorea, JobKoreaUSA, HeyKorean, Asian-Jobs.com)는 사례를 공개하지 않습니다.
4. **원티드의 공백은 "③ × bilingual", 그리고 "① × 언어·시차 검증"입니다.** 다만 사례가 0건이라는 것은 수요가 작다는 신호일 수도 있으므로, 수요 검증(v2 Part 2)을 먼저 해야 합니다.

## 2. 고객 규모 분류 기준
| 분류 | 기준 |
|---|---|
| 스타트업 | 비상장, 기업가치 $1B 미만 또는 미공개 |
| 유니콘 | 비상장, 기업가치 $1B 이상. 사례 시점과 현재가 다르면 함께 표기(예: Decagon은 사례 당시 스타트업, 현재 $4.5B) |
| 대기업 | 상장사 또는 직원 1,000명 이상 성숙 기업. 이번 표본에는 순수 대기업 사례가 없음(Faire는 유니콘이지만 1,000~5,000명이라 "유니콘(대형)"으로 분류) |
| 확인 불가 | 규모 정보 없음(Mission Cloud, Dover 사례의 Forge, Forward Financing) |

## 3. 규모 × Pain 요약 (사례 건수, 1건이 여러 Pain에 해당할 수 있음)
| 규모 | ① 탐색·선별 | ② 내부 리소스 | ③ 후보 연결 |
|---|---|---|---|
| **스타트업** | 3건(Dover·Prelay, Arc·Pathrise, Juicebox·Tavrn/Binti) | 5건(Paraform·Decagon, Coworker / Dover / Wellfound·Adonis / Gem·Tropic) | **8건**(Paraform 3, Dover 2, Arc 2, Built In 1) |
| **유니콘·대형** | 3건(전부 Gem) | 3건(전부 Gem) | 3건(Gem·Faire, Paraform·Windsurf, Built In·Benchling) |
| 혼합·확인 불가 | 1건 | 2건 | 1건 |

Source: 각 사례 URL은 엑셀 '1_케이스DB' 시트. 규모 근거: Veho $1.5B — [TechCrunch](https://techcrunch.com/2022/02/15/funding-round-veho-deliver/embed/), Linktree $1.3B — [Axios](https://axios.com/link-in-bio-startup-linktree-raises-110-million-a94faebb-8b49-4b65-9940-c2b886d6ab98.html), Decagon $4.5B — [Shopifreaks](https://www.shopifreaks.com/decagon-raises-250m-at-4-5b-valuation-for-ai-agents/), Windsurf $1.25B — [Sacra](https://sacra.com/c/codeium/). Webflow·Benchling·Modern Health 기업가치는 기억에 기반한 것이라 재확인이 필요합니다.

**해석:** S1(스타트업~유니콘) 안에서도 단계에 따라 맞는 해결책이 다릅니다.
- 스타트업: 대행형(Paraform·Dover·Autopilot)이 ②③을 해결
- 유니콘: 도구형(Gem)이 ①②를 해결

원티드의 S1 초기 고객(GIGR, Neon, Foxglove 등)은 **대행형과 경쟁하는 자리**에 있습니다.

## 4. Pain별 해결 업체·이유·공백
| Pain | 해결 업체(대표 사례) | 왜 해결되나 | 공백(없다면 왜) |
|---|---|---|---|
| ① 탐색·선별 | Gem(Scale AI: 3주에 12명), Juicebox(Tavrn: 2주에 AE 4명), Dover(Prelay: 72일간 50명 폰스크린), Arc(Pathrise: 6일 온보딩) | AI 검색으로 발굴 시간을 단축하거나, 사전 검증된 풀·리크루터 스크리닝이 선별을 대신함 | 한국어 수준·한국 거주·시차 근무로 거른 사례는 없음. 도구에 언어 검증 기능이 없고 프로필 수가 검증된 bilingual 인재 수를 뜻하지 않음 [추정] |
| ② 내부 리소스 | Paraform(Decagon: 리크루터 0명에서 첫 달 2명), Dover(Forge: 채용 인력 2명), Wellfound Autopilot(Adonis), Gem(Tropic: 같은 인원으로 생산성 2배) | 외부 리크루터를 성공보수·시간제로 빌려 쓰거나, 도구로 적은 인원의 생산성을 높임 | 가장 잘 해결된 영역. bilingual 직무를 대행한 사례만 없음 |
| ③ 후보 연결 | Paraform(Casca: 기존 에이전시 실패 후 1개월에 4명), Dover(Steady Health), Arc(BAXUS: 원격 채용으로 연 $50K 절감), Built In(Carrot: 브랜딩) | 직무 전문 리크루터의 네트워크, 글로벌 원격 인재풀, 고용주 브랜딩 | **bilingual 사례 0건.** 이유(추정): (a) 미국 서비스의 인재풀이 미국·글로벌 원격 중심이고 언어 필터가 없음, (b) 한인 특화 서비스는 규모가 작아 사례를 공개하지 않음, (c) 수요가 소수라 상품화되지 않음 |

## 5. 원티드에 주는 시사점
- **포지셔닝 후보:** "Paraform·Dover의 대행 모델 + 한국 인재풀 + 언어·시차 사전 검증". 직접 경쟁 대신 이들 마켓에 bilingual 전문 리크루터로 입점하는 방안도 함께 검토할 만합니다.
- **원티드 사례를 만든다면** 업계 표준 형식(Before/How/After + 기간·인원·비용 수치 + 고객 단계)을 따라야 비교가 가능합니다. Arc의 BAXUS 사례(미국 채용은 비싸서 원격으로 대체)가 원티드의 "한국 원격" 논리와 가장 가깝습니다.

## 6. 한계
- 모든 사례가 벤더 홍보물입니다(성공 사례만 공개, 수치는 자사 발표).
- 일부 행은 제목·요약만 확인했습니다(엑셀 '신뢰도' 열에 표시).
- 사례 수가 적어서(24건) 건수 비교는 경향을 보는 용도로만 써야 합니다.
