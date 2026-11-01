# 원티드랩 인재매칭팀 · S1 세그먼트 이해 (Phase 2)

- 작성일: 2026-11-01
- 대상: `인재채용팀(2차 세그먼팅)` 시트의 S1 (스타트업·유니콘·소기업 × 공급 용이)
- 원천 데이터: `인재매칭팀_북미bilingual채용_롱리스트matrix` (조사 기준일 2026-10-28), 보고용 원티드랩 Docs(Phase 1~2, 원티드어빌리티, 실무진 피드백)
- 표기: **[확인]** 공개자료로 확인 / **[추정]** 공고·정황 기반 추론 / **[확인 불가]** 공개자료로 확인 안 됨

---

## 0. 결론 먼저

1. **S1은 하나의 세그먼트가 아닙니다.** "언어 × 근무지" 기준으로 보면 공급 난이도가 전혀 다른 4개 묶음이 섞여 있습니다.
   - **A. 한국 근무(원격·서울) × 한국어**: Foxglove, Neon Commerce, GIGR(서울 포지션), Applied Intuition(서울 조직), MarqVision(서울 거점) → 미국 비자 문제가 없고 원티드 기존 인재풀을 그대로 쓸 수 있음. **"공급 용이" 근거가 가장 강함.**
   - **B. 미국 근무 × 한국어**: Applied Intuition(US-based Korea Market), Matter Intelligence, SirenOpt, Gatewell, Clever Care, Veniroe, 6th Avenue, Sendbird(마감) → **미국 취업자격이 필요**해서 원티드 국내 풀로는 공급이 막힘. 미국 현지 한인·유학생 풀이 필요함.
   - **C. 미국 근무 × 중국어 필수/우대**: Chowbus, Retell AI, Novita AI, Bellota Labs, maxta, hellyeah → 원티드의 강점과 맞지 않음. **"공급 용이" 분류를 다시 검토해야 함(S3 이동 또는 제외 권고).**
   - **D. 일본어**: Alpaca(APAC 원격), Plus AI(산타클라라, 일본 출장) → 원티드 일본 거점(Moonshot, HR Booster)과 연결할 수 있음. 조건부로 가능.
2. **채용 결정자는 회사 단계에 따라 다릅니다.** 시드~시리즈 A(50명 이하)는 창업자·현업 매니저가 직접 뽑고, 시리즈 B 이상(약 50~250명)은 사내 리크루터나 Head of Talent가 있는 구조입니다. 개인 이름은 대부분 **[확인 불가]**로, LinkedIn에서 직접 확인해야 합니다.
3. **채용 도구는 공고 URL로 상당 부분 확인됩니다.** Ashby·Greenhouse·Lever 같은 스타트업용 ATS(지원자 관리 시스템)를 쓰는 회사가 다수이고, 작은 로컬 기업은 Indeed에만 공고를 올립니다. 추천(referral) 채용 비중은 **[확인 불가]**입니다.
4. **bilingual 채용 이유는 세 가지로 나뉩니다.** ① 아시아 시장 진출(GTM) ② 한국·중국계 본사/창업자와의 소통 ③ 미국 내 한인·아시아계 고객 응대. ①과 ②가 원티드에 맞는 수요입니다.
5. **Reddit API로 새로 접근하는 길은 사실상 막혔습니다.** Reddit은 2026-10-31부터 신규 public Data API 신청을 받지 않습니다(아래 6장). 대신 **H-1B LCA(노동조건신청서) 공개 데이터와 공고 데이터**로 수요를 검증하는 쪽을 권합니다.

---

## 1. S1 목록 정합성 점검 (먼저 고칠 것)

| 항목 | 내용 | 조치 |
|---|---|---|
| 개수 불일치 | 시트 제목은 "S1 (21개)"이지만 적힌 회사명은 **20개** | 빠진 1개 확인 또는 제목 수정 |
| 규모 분류 | Plus AI가 롱리스트에 두 번 나옴: "스타트업"과 "중견(약 470명)". 470명이면 스타트업으로 보기 어려움 | 규모 기준 통일 |
| 근거 약함 | Sendbird는 **마감된 공고 1건**(디자이너, 사내 소통용 한국어)뿐 | 현재 수요 근거로 쓰기 어려움, 참고로만 표기 |
| 원래 조건 위배 가능 | Chowbus·hellyeah 등은 중국계 창업 기업의 중국어 수요. 같은 시트에서 TikTok은 "중국 기업의 미국 진출 → 원 조건 제외"로 처리됨 | 같은 기준을 적용할지 팀 합의 필요 |

Source: 인재채용팀(2차 세그먼팅) 'segment matrix' 탭; 인재매칭팀_북미bilingual채용_롱리스트matrix '고객사 리스트(+개발, 마케터, 디자인)' 탭 (조사 기준일 2026-10-28)

---

## 2. 회사별 프로파일 (산업 · 규모 · 결정자 · 채용 도구 · bilingual 이유)

### A. 한국 근무 × 한국어 (원티드 공급 적합도 높음)

| 회사 | 산업 / 규모 | 확인된 직무 | 채용 도구 | bilingual 이유 | 결정자(추정) |
|---|---|---|---|---|---|
| **Foxglove** | 로보틱스 데이터 인프라 / 시리즈 B $40M(2025.11), 약 50명 | Full-Stack Engineer, Forward Deployed(**한국 원격**, 한·영 필수) | Ashby [확인] | 한국 로보틱스 고객 기술 지원 [추정] | 엔지니어링 리드 + 창업자 |
| **Neon Commerce** | 게임 커머스·결제 / 시리즈 A $13M(2026.7, a16z·Renegade, 크래프톤 전략 투자), 약 18~20명 | Forward Deployed Engineer(**서울**, 한·영 필수, 고객 대면 경력 5년+) | Ashby [확인] | 한국 게임사(크래프톤 등) 고객 대응 [추정] | 창업자(CEO Chris Faught) + 엔지니어링 리드 |
| **GIGR (Playad)** | AI 마케팅 SW / 프리시드 $5.4M(2026.1), 2025년 SF 설립 | Founding Sales Manager(SF/서울, **서울만 bilingual 필수**) | LinkedIn 공고(5개월 게시, 지원자 114명) | 서울 영업팀과 협업, 한국계 창업자 | CEO 조재연(Jaeyeon Cho) 직접 [확인: CEO 신원] |
| **Applied Intuition** | 자율주행·Physical AI SW / 유니콘. 서울 사무소 약 12명(2026.2 공고 기준) | Technical BD Lead, Korea Market / Solution Engineer, Korean Market(둘 다 **US-based**). 서울에는 국방 엔지니어링 매니저, FDE 신입 등 | Greenhouse [확인] | 한국 정부·산업계의 Physical AI 투자 대응. 2020년 한국 진출 | 사내 리크루팅팀 + 한국 사업 리드 [추정] |
| **MarqVision** | AI 브랜드 보호 / 시리즈 B $48M(2025.9, Peak XV 리드), 50~200명 | Solutions Consultant(한·중 우대) | Greenhouse [확인], 사내 Technical Recruiter 채용 공고 있음 | 공고만으로는 한국 고객용인지 본사 소통용인지 불분명 | CEO 이영(Mark Lee) + 사내 리크루터 |

Source: Foxglove — [BusinessWire, 2025-11-12](https://www.businesswire.com/news/home/20251112126106/en/Foxglove-Raises-%2440-Million-Series-B-to-Power-the-Future-of-Physical-AI), 인원 [The Robot Report](https://www.therobotreport.com/foxglove-raises-40m-scale-data-platform-roboticists/), 공고 [Ashby](https://jobs.ashbyhq.com/foxglove/7a4868ab-c8da-43aa-bf78-cf68695bfaec)
Source: Neon — [Korea Herald](https://www.koreaherald.com/article/10817929), [Invenglobal](https://www.invenglobal.com/articles/24061/krafton-makes-strategic-investment-in-global-game-commerce-infrastructure-firm-neon-commerce), [Seedtable 공고](https://seedtable.com/jobs/49405), 인원 [Built In](https://builtinlondon.uk/company/neon-2)
Source: GIGR — [Wowtale, 2026-01-27](https://en.wowtale.net/2026/01/27/233424), [바이라인네트워크](https://byline.network/2026/01/27_192873/), 공고 [LinkedIn](https://www.linkedin.com/jobs/view/4410409270)
Source: Applied Intuition — [General Catalyst 잡보드: Korea Market BD Lead](https://jobs.generalcatalyst.com/companies/applied-intuition/jobs/82428425-technical-business-development-lead-korea-market-us-based), [Head of Defense Engineering (South Korea)](https://jobs.generalcatalyst.com/companies/applied-intuition/jobs/82428300-head-of-defense-engineering-south-korea), [Greenhouse](https://job-boards.greenhouse.io/appliedintuition/jobs/4583800005)
Source: MarqVision — [DealStreetAsia](https://media.dealstreetasia.com/stories/peak-xv-marqvision-456355), [Greenhouse](https://job-boards.greenhouse.io/marqvision/jobs/4565626008), [Technical Recruiter 공고](https://www.employbl.com/jobs/technical-recruiter-marqvision-1477170)

### B. 미국 근무 × 한국어 (공급하려면 미국 취업자격 필요)

| 회사 | 산업 / 규모 | 확인된 직무 | 채용 도구 | bilingual 이유 | 결정자(추정) |
|---|---|---|---|---|---|
| **Matter Intelligence** | 위성 원격탐사 / 시드 $12M(2024). 2026.4 약 $36M 라운드는 [확인 불가: 1차 보도자료 없음], 26~33명 | Head of Sovereign Partnerships(한 또는 일 전문 수준) | LinkedIn | 한·일 정부 고객 확보 | 창업자(전 NASA JPL 출신) |
| **SirenOpt** | 반도체·소재 계측 장비 / $6.5M(2025.10, Hitachi·JLR CVC), 약 35~42명 | Metrology Data Scientist 외(일·한·중 중 택1 우대) | Greenhouse [확인] + **같은 직무를 인력사무소에도 의뢰** | 아시아 제조 고객 확대 | 창업자 + 현업 매니저. 외부 에이전시 이미 사용 |
| **Gatewell Group** | 규제 대응·공급망 실사 컨설팅 / 규모 [확인 불가] | Korea Practice Coordinator(LA, 한·영 전문 수준) | 자사 커리어 페이지 | 한국 시장 고객 계정 지원 | [확인 불가] |
| **Clever Care Health Plan** | 메디케어 어드밴티지 보험(헌팅턴비치) / 시리즈 A $20M 등 | 고객서비스 상담원(한국어 필수), 브로커 CS, 케이스 매니저 | LinkedIn | **2023년 가입자의 47%가 한국어 상담 선택** | 공동창업자 Myong Lee + 운영·HR 조직 |
| **Veniroe** | 비버리힐스 파인주얼리 / 소기업 | 마케팅 스페셜리스트(파트타임 $25/hr, 한·영 필수) | Indeed | 한국어권 고객 마케팅 [추정] | 창업자 직접 [추정] |
| **6th Avenue Restaurant Group** | LA 코리아타운 외식 / 소기업 | Director of Brand Marketing($150~180K, 한·영 강력 우대) | Indeed | 한인 상권·고객 대상 브랜딩 [추정] | 오너 직접 [추정] |
| **Sendbird** | 커뮤니케이션 API·AI 에이전트 / 유니콘, 약 240명(San Mateo) | 마감: 비주얼·마케팅 디자이너(사내 소통용 한국어 필수) | [확인 불가] | 한국 본사 조직과의 소통 | 사내 리크루팅팀 [추정] |

Source: Matter — [BusinessWire, 2024-10-30](https://www.businesswire.com/news/home/20241030574726/en/Matter-Intelligence-Emerges-from-Stealth-with-%2412-Million-Seed-Funding-to-Revolutionize-Remote-Sensing-and-Global-Perception), 2026 라운드·인원 [Caplight](https://www.caplight.com/company/matter-intelligence)(2차 자료)
Source: SirenOpt — [Global Venturing](https://globalventuring.com/corporate/investment/sirenopt-raises-6-5m-hitachi-jlr/), [Greenhouse](https://job-boards.greenhouse.io/sirenopt/jobs/4015931009), 인원 [PitchBook](https://pitchbook.com/profiles/company/521450-02)
Source: Gatewell — 롱리스트 시트 링크(gatewellgroup.com/careers-korea-coordinator). 이 세션의 네트워크 정책 때문에 직접 열람은 못 함
Source: Clever Care — [Becker's Payer](https://www.beckerspayer.com/?p=11983), [Crunchbase News](https://news.crunchbase.com/news/clever-care-receives-20m-series-a-round-to-launch-new-california-medicare-advantage-program/), [Fierce Healthcare](https://www.fiercehealthcare.com/payers/clever-care-nabs-41m-scale-medicare-advantage-plans-integrating-eastern-and-western-medicine)
Source: Sendbird — [Built In](https://www.builtinboston.com/company/sendbird/faq/stability-growth), 마감 공고 [Beamstart](https://beamstart.com/job/visual-amp-marketing-designer-17649056119556)
Source: Veniroe, 6th Avenue — 롱리스트 시트의 Indeed 공고 링크. 회사 정보는 [확인 불가]

### C. 미국 근무 × 중국어 (원티드 강점과 불일치 → 재분류 검토)

| 회사 | 산업 / 규모 | 확인된 직무 | 채용 도구 | 비고 |
|---|---|---|---|---|
| **Chowbus** | 레스토랑 POS·SaaS(시카고) / 시리즈 E $81M(2026.3), 약 190~200명, ARR 약 $120M(회사 발표) | 마케터 3건(중·영 필수) | Greenhouse [확인] | 중국계 창업(CEO Linxin Wen), 아시아계 식당 고객 대상. "Chinese Vertical" 영업 조직 있음 |
| **Retell AI** | 음성 AI / ARR 약 $50M(2026.4), 25~88명(출처마다 다름) | Senior Forward Deployed Engineer(중·영 필수) | Ashby [확인] | |
| **Novita AI** | GPU 클라우드 / 16~50명, 투자 정보 [확인 불가] | FDE, FDE 신입(중국어 우대) | Ashby [확인] | |
| **Bellota Labs** | B2B 모바일 게임(ClubWPT Gold) / 정보 신뢰도 낮음 | Senior/Principal SWE(중국어 필수) | Lever [확인] | |
| **maxta** | 엔터프라이즈 AI 인프라 / 회사 정보가 출처마다 엇갈림 | Marketing Manager(중국어 매우 우대) | 자사 페이지 | 시트의 "이스라엘 창업" 표기 [확인 불가] |
| **hellyeah** | AI 광고 에이전트 / 약 27명, $6.9~10M(2차 자료) | GTM 매니저, 비서형 마케팅(중국어 우대) | Ashby [확인] | SF 외 **서울·상하이** 채용도 있음 → 서울 포지션은 A로 옮길 수 있음 |

Source: Chowbus — [Restaurant Technology News, 2026-03](https://restauranttechnologynews.com/2026/03/chowbus-raises-81-million-to-expand-its-ai-powered-platform-for-independent-restaurants/), [Wikipedia](https://en.wikipedia.org/wiki/Chowbus); Retell — [Enterprise DNA](https://enterprisedna.co/resources/news/retell-ai-50m-arr-voice-ai-market-validation-2026), [Sacra](https://sacra.com/c/retell-ai); Novita — [AMCompute](https://www.amcompute.com/jobs/company/novita); Bellota — [Built In SF](https://www.builtinsf.com/company/bellota-labs); maxta — [CB Insights](https://www.cbinsights.com/company/maxta/financials); hellyeah — [Built In SF](https://www.builtinsf.com/company/hellyeah-ai), [Fast AI Jobs](https://www.fastaijobs.com/companies/hellyeah-ai)

**재분류를 권하는 이유:** 원티드 글로벌서비스 소개서의 "영어·중국어·일본어 중 하나 이상 보유 이용자 309,453명"은 언어별 분포와 수준이 공개되어 있지 않습니다. 그 안에 "미국 거주 + 중국어 원어민 수준" 인재가 얼마나 있는지는 **[확인 불가]**입니다. 반면 C 묶음 공고는 대부분 미국 근무와 원어민 수준 중국어를 요구합니다. 실무진 피드백("기존 인재풀을 활용할 수 있는지 고려")에 비춰 보면, C는 "공급 용이"로 보기 어렵습니다.
Source: 보고용 원티드랩 Docs '원티드어빌리티' 탭(「원티드랩 글로벌서비스 소개서」 pp. 3–13 인용); '중간점검 내용(인재매칭팀)' 탭

### D. 일본어

| 회사 | 산업 / 규모 | 확인된 직무 | 채용 도구 | 비고 |
|---|---|---|---|---|
| **Alpaca** | 증권 인프라 API / 유니콘, 시리즈 D $150M·기업가치 $1.15B(2026.1). SBI·MUFG가 투자 | Senior/Staff SWE – New Markets Japan(**APAC 원격**, 일본어 N1·원어민) | Greenhouse [확인] | 일본 시장 확장. 원티드 일본 거점과 연결할 수 있음 |
| **Plus AI** | 자율주행 트럭 / 약 470명. Churchill IX와의 SPAC 합병은 **2026.4 종료** | Program Manager(일·영, 일본 출장 약 25%, $120~160K) | Lever [확인] | 상장 무산 후 채용 계획 변동 가능성 있음 |

Source: Alpaca — [Finance Magnates](https://www.financemagnates.com/forex/brokers/us-broker-dealer-alpaca-raises-150-million-valued-at-115-billion), [fintech.global](https://fintech.global/2026/01/14/alpaca-raises-150m-series-d-at-1-15bn-valuation/); Plus AI — [SEC 10-Q, Churchill Capital Corp IX](https://www.sec.gov/Archives/edgar/data/0002006291/000119312526226645/d222611d10q.htm), [FreightWaves](https://www.freightwaves.com/news/plusai-spac-merger-2026)

---

## 3. 현재 채용 방식과 부담·비용

### 3-1. 채용 채널 분포 (공고 URL 기준)

| 채널 | 회사 | 의미 |
|---|---|---|
| Ashby | Foxglove, Neon, Retell, Novita, hellyeah | 초기·성장기 AI 스타트업이 많이 씀 |
| Greenhouse | Applied Intuition, MarqVision, SirenOpt, Alpaca, Chowbus | 시리즈 B 이상, 사내 리크루터가 있는 구조와 겹침 |
| Lever | Bellota Labs, Plus AI | |
| LinkedIn만 확인 | GIGR, Matter, Clever Care | ATS 사용 여부 [확인 불가] |
| Indeed만 확인 | Veniroe, 6th Avenue | 로컬 소기업. ATS 없이 직접 공고하는 것으로 [추정] |
| 외부 에이전시 병행 | SirenOpt | 외부 채용 서비스에 돈을 내는 수요가 **실제로 확인된 유일한 사례** |
| 추천 채용 | 전체 | **[확인 불가]** — 공개자료로는 알 수 없음. 인터뷰가 필요함 |

Source: 롱리스트 시트의 공고 URL(도메인: jobs.ashbyhq.com, job-boards.greenhouse.io, jobs.lever.co 등) 및 위 2장의 링크

### 3-2. 비용 기준 (외부 벤치마크)

| 항목 | 일반적 수준 | 비고 |
|---|---|---|
| ATS 연간 비용(50명 규모) | Ashby 약 $4.8~6K, Greenhouse 약 $5~8K(+도입비 가능), Lever 약 $4~6K | 비공개 가격. 2차 자료 추정치 |
| 컨틴전시 에이전시 수수료 | 첫해 기본급의 **15~25%**. Bullhorn 2024 조사 평균 18.5% | 연봉 $150K 직무 기준 1건당 약 $22.5~37.5K |
| 한국 거주자 EOR(대리 고용) | Deel 정가 월 **$599/인**(급여·법정비용 별도) | 한국 법정 부담금(4대보험, 퇴직금 적립)은 별도로 계산해야 함 |

Source: ATS — [Pin: Ashby pricing](https://pin.com/blog/ashby-pricing/), [Costbench: Greenhouse vs Lever](https://costbench.com/compare/greenhouse-vs-lever); 에이전시 수수료 — [Underdog.io](https://underdog.io/blog/recruitment-agency-costs), [RecruitBPM](https://recruitbpm.com/blog/recruitment-fees); EOR — [Pin: Deel pricing](https://www.pin.com/blog/deel-pricing/), [WhichPayroll](https://whichpayroll.com/countries/south-korea/employer-of-record)

### 3-3. 업무 부담 가설 (검증 필요)
- **초기 스타트업(GIGR, Neon, Matter 등):** 전담 리크루터 없이 창업자가 직접 소싱하고 면접함. GIGR 공고는 5개월째 열려 있고 지원자가 114명입니다. 지원자가 부족해서가 아니라 **걸러내기 부담이나 조건 불일치**가 문제일 수 있습니다 [추정].
- **성장기(MarqVision, Applied Intuition, Chowbus):** 사내 TA(채용 담당) 조직이 있지만, 한국어 역량을 평가할 사람과 한국 쪽 소싱 채널이 부족할 가능성 [추정].
- **로컬 소기업(Veniroe, 6th Avenue):** 예산이 작고 파트타임·저임금 직무도 있어서 에이전시 수수료 모델이 맞지 않음 [추정].

---

## 4. 당면 과제: 왜 bilingual이 필요한가

| 유형 | 해당 회사 | 원티드 적합도 |
|---|---|---|
| ① 아시아 시장 진출(GTM·기술 지원) | Applied Intuition, Neon, Foxglove, Matter, SirenOpt, Alpaca, Plus AI | **높음.** 한국·일본에 있는 인재로도 수행할 수 있는 업무가 많음 |
| ② 한국·중국계 본사/창업자와의 소통 | GIGR, MarqVision, Sendbird, hellyeah, Chowbus | 한국계는 높음, 중국계는 낮음 |
| ③ 미국 내 한인·아시아계 고객 응대 | Clever Care, Veniroe, 6th Avenue, Gatewell, Chowbus | 낮음. 미국 현지 거주와 취업자격이 필요함 |

**시사점:** "말이 통하고 일 잘하는 사람"(②)과 "아시아 시장을 여는 사람"(①)은 채용 결정자와 예산 출처가 다릅니다. ①은 사업개발·엔지니어링 리드가 매출 목표 아래에서 뽑고, ②는 창업자의 운영 편의를 위한 채용입니다. 그래서 메시지와 가격도 따로 설계해야 합니다.

---

## 5. 규제: 비자와 고용 형태

### 5-1. 미국 근무 포지션 (B·C 묶음, A의 US-based 직무)

| 경로 | 현황(2026-11 기준) | S1에 주는 의미 |
|---|---|---|
| **H-1B $100,000 수수료** | 2025.9 포고문으로 도입. 2026.6 매사추세츠 연방법원이 위법 판단, 7월 1순회항소법원이 집행정지 거부, 9.30 샌프란시스코 연방법원이 징수 정책 무효화. 하지만 9.18 포고문으로 2027.9까지 연장되었고 **항소가 진행 중** | 지금은 징수되지 않지만 불확실성이 큼. 스타트업이 해외 인재 H-1B 스폰서를 꺼리는 요인 |
| **H-1B 임금 가중 추첨** | FY2027부터 시행(2026.2.27 발효). 임금 레벨이 높을수록 추첨 기회가 많아짐 | 연봉이 낮은 주니어 bilingual 직무는 선발 확률이 낮음(비공식 추정: Level I 약 15%) |
| **E-2(조약국 투자자) 직원** | 한국·일본은 조약국, **중국(PRC)은 아님**. 회사 지분 50% 이상이 같은 국적이어야 하고, 직원은 essential(필수) 인력이어야 함 | 한국인이 대주주인 미국 법인(예: GIGR, MarqVision일 가능성)은 한국인을 E-2로 데려올 수 있음. 실제 지분 구조는 [확인 불가] |
| **L-1(주재원)** | 해외 계열사에서 1년 이상 일한 사람을 미국으로 전보 | 서울 법인이 있는 회사(Applied Intuition, MarqVision, Sendbird, GIGR)는 "서울에서 채용 → 미국 전환" 경로를 쓸 수 있음 |
| **E-4(Partner with Korea Act)** | H.R.4687(한국인 전용 연 15,000개)은 하원 법사위에 계류 중이고 진전 없음 | 사업 전제로 삼으면 안 됨 |
| **F-1 OPT/STEM OPT** | 미국 유학생은 졸업 후 최대 1년(+STEM 2년) 근무 가능 | B 묶음에 공급할 현실적인 경로. 미국 대학 한인 유학생 풀이 필요함 |

Source: H-1B 수수료 — [Fragomen](https://www.fragomen.com/insights/united-states-president-trump-extends-dollar100000-h-1b-fee-but-policy-currently-vacated-by-court-order.html), [Forbes, 2026-10-01](https://www.forbes.com/sites/stuartanderson/2026/10/01/judge-strikes-down-latest-version-of-100000-h-1b-immigration-fee/), [SHRM](https://www.shrm.org/topics-tools/news/100k-h-1b-fee-extended-through-2027)
Source: 가중 추첨 — [Greenberg Traurig](https://www.gtlaw.com/ar/insights/2026/2/uscis-finalizes-wage-weighted-h-1b-cap-selection-rule-effective-feb-27-2026), [BakerHostetler](https://www.bakerlaw.com/insights/uscis-implements-wagelevel-h1b-lottery/); 확률 추정은 [Visa-Pros](https://visa-pros.com/h-1b-weighted-lottery/)(비공식)
Source: E-2 — [National Law Review](https://natlawreview.com/article/e-2-visa-south-korean-investors). 최종 확인은 8 CFR 214.2(e)와 국무부 FAM(외교업무 매뉴얼)으로
Source: E-4 — [Rep. Young Kim 보도자료, 2025-07-24](https://youngkim.house.gov/2025/07/24/rep-young-kim-leads-bipartisan-bill-to-strengthen-u-s-korea-ties), [Korea JoongAng Daily](https://www.koreajoongangdaily.com/korea/us-lawmakers-table-bill-again-to-provide-work-visas-for-highly-skilled-korean-nationals/12203611)

### 5-2. 한국 근무 포지션 (A 묶음)
- 미국 비자는 필요 없습니다. 대신 **고용 주체 문제**가 생깁니다. 한국 법인이 없으면 EOR(Deel, Remote 등)이나 프리랜서(업무위탁) 계약을 써야 합니다.
- 업무위탁 계약은 실질적으로 근로자로 인정될 위험(4대보험, 퇴직금)이 있어서 EOR이 일반적입니다. 원티드는 이미 Remote·Deel 할인 연계를 하고 있습니다.
Source: 보고용 원티드랩 Docs '원티드어빌리티' 탭 ③ 해외 인사 운영 지원

---

## 6. Reddit API 활용 계획에 대한 판단

**결론: 신규 API 접근은 사실상 불가능하니, 다른 데이터로 대체하는 것을 권합니다.**
- Reddit 변경 로그(2026-10-08)에 따르면 **2026-10-31부터 신규 public API 신청을 받지 않습니다.** 2027-01-12부터 미등록 앱 접근을 차단하기 시작하고, 2027-03에는 서면 계약이 있는 파트너를 빼고 public Data API를 종료합니다. 상업적 사용은 원래 별도 계약이 필요했습니다.
- Reddit 원문 페이지는 이 세션의 네트워크 정책 때문에 직접 열람하지 못했습니다. 위 내용은 보도와 검색 요약으로 확인한 것입니다.
- 내용 측면에서도 한계가 있습니다. Reddit에는 개발자·구직자 목소리가 많고 **채용 결정자(창업자·HR)의 "한국어 인재" 수요 글은 매우 적을 것**입니다 [추정].

Source: [Reddit Help 변경 로그, 2026-10-08](https://support.reddithelp.com/hc/en-us/articles/54353370049684-Changelog-October-8-2026), [Unite.AI](https://www.unite.ai/reddit-sets-dates-to-retire-rss-feeds-and-close-public-api-access/), [PPC Land](https://ppc.land/reddit-to-halt-public-data-api-access-in-march-2027-as-14-000-apps-register/)

**대안 (같은 목적인 "세그먼트 수요 이해"에 더 직접적인 데이터):**
1. **DOL H-1B LCA 공개 데이터**(또는 h1bdata.info): S1 20개사가 비자 스폰서를 해왔는지, 직무와 임금 레벨을 확인 → "미국 근무 포지션을 외국인으로 채울 의지가 있는가"를 판단
2. **회사별 ATS 공고 전수 수집**: Ashby·Greenhouse·Lever는 공개 잡보드 JSON을 제공함(로그인 불필요) → 한국어/Korea 키워드 공고를 주기적으로 추적
3. **Reddit은 수동 정성 조사로만**: r/startups, r/humanresources, r/recruiting, r/korea에서 "hire in Korea", "Korean speaking", "EOR Korea", "Seoul office" 등을 검색해 사례만 수집
4. **인터뷰**: HRCap 대표 미팅처럼, S1 중 A 묶음 2~3곳 채용 담당자에게 10분 질문(추천 채용 비중, 에이전시 사용 여부, 걸린 기간)

---

## 7. 사업기회 도출을 위한 시사점 (후보 방향, 최종 판단은 팀)

| 가설 | 타깃 | 원티드 자산 | 리스크 |
|---|---|---|---|
| **H1. "Seoul-first" bilingual 채용 + EOR 번들** | A 묶음(한국 원격·서울 거점을 둔 미국 스타트업) | 국내 인재풀, 헤드헌팅, Deel·Remote 제휴 | 시장 규모 검증 필요(현재 확인된 공고 5~6건) |
| **H2. 서울 채용 → L-1 미국 전환 브리지** | 서울 법인이 있는 미국 스타트업 | 국내 채용 역량 + 미국 이민 법무 파트너 | 1년 대기 기간, 법무는 파트너에 의존 |
| **H3. 아시아 GTM 초기 팀 구성 패키지** | ① 유형(Applied Intuition, Matter, SirenOpt 등) | 채용 + 해외 진출 파트너 연결(GTM·법무) | 미국 근무 직무는 비자 장벽 |
| (보류) 미국 내 한인 고객 응대 인력 | ③ 유형(Clever Care, 로컬 소기업) | 약함 | 현지 풀 필요. JobKoreaUSA·HeyKorean이 이미 있음 |
| (제외 권고) 중국어 인력 | C 묶음 | 약함 | 원티드 강점과 불일치 |

**네트워킹·브랜딩·파트너십 접점 [추정, 확인 필요]:** 한국 Physical AI·로보틱스 생태계(Applied Intuition·Foxglove의 한국 고객), 게임 업계(Neon–크래프톤), KOTRA·KIC 실리콘밸리 등 한·미 스타트업 지원 기관, 미국 대학 한인 학생회(OPT 인재풀).

---

## 8. 확인 불가 항목 정리

| 항목 | 이유 | 확인 방법 |
|---|---|---|
| 회사별 채용 결정자 실명(대부분) | 공개자료 부족 | LinkedIn에서 "Recruiter/Talent/People + 회사명" 검색 |
| 추천 채용 비중, 실제 채용 비용 | 비공개 | 인터뷰 |
| Gatewell, Veniroe, 6th Avenue 회사 정보 | 검색 결과 없음, 사이트 접근 차단 | 직접 방문, 캘리포니아 주 법인 등록 조회 |
| 원티드 풀의 언어별·거주지별 분포 | 소개서에 없음 | 실무진에게 질문 |
| E-2 해당 여부(한국계 회사 지분 구조) | 비공개 | 회사 확인 |
| Matter 2026 라운드, Novita·hellyeah 투자 | 1차 자료 없음 | 보도자료, Crunchbase |
