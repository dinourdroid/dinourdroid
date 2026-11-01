# 네트워크 허용 후 원문 확인 결과 — 이전 분석 정정 사항

- 작성일: 2026-11-01
- 방법: 그동안 차단돼 있던 사이트를 curl로 받아 원문 텍스트를 확인했습니다. 웹 검색 요약만 보고 판단했던 부분을 원문으로 대조했습니다.
- 여전히 열리지 않는 곳: Reddit 도움말 센터(403), 바이라인네트워크(403). 둘 다 봇 차단으로 보입니다.

## 1. 결론이 바뀐 것

| # | 이전 판단 | 원문 확인 후 | 영향 |
|---|---|---|---|
| 1 | HireFromKorea는 "사례 없음, 자사 주장뿐" | **익명 배치 사례 3건**: 글로벌 유튜브 채널의 한국어 영상 편집자, 해외 스타트업의 한국 국가 매니저, 글로벌 게임사의 한국 지역 마케팅 매니저. **운영은 공동 파트너 2명**(Daniel Ahn, Sandy Kang). 채용 경로는 원격 계약직 / EOR 정규직 / 자체 법인 3가지이고, EOR·급여는 별도 견적 옵션 | "**비개발 bilingual 직무를 해결하는 서비스는 없다**"는 결론은 **틀렸습니다.** HireFromKorea가 정확히 이 영역(마케팅, 국가 매니저·BD, CS, 콘텐츠)을 겨냥합니다. 다만 2인 운영이고 고객명이 비공개라, "**규모 있고 검증된 해결자는 없다**"로 정정합니다 |
| 2 | Arc는 "개발직에 한해 부분 해결" | **마케터·디자이너도 공급**합니다. Chamberlin Group은 중남미 마케터를 2일 만에 찾고 9일 만에 채용했고, Nodus(디자이너), Copy.ai(SEO) 사례도 있습니다 | Arc의 Q3 판정을 "개발직 한정" → "**개발·마케팅·디자인 원격 인력. 한국어 검증 없음**"으로 수정 |
| 3 | Gem–Terminal의 응답률 "41% vs 10% 불일치" | 응답률이 31%(4월)에서 41%(8월)로 올라 **약 10%p 상승**. 두 수치 모두 맞음 | 불일치 해소 |
| 4 | Gem–Daxko는 "사기 후보 탐지" 사례로만 정리 | 원문은 **"원격 기술직마다 가짜 지원자가 섞이고, 특히 해외에서 미국인 신원을 위조해 지원하는 경우"**를 IP·위치 신호로 잡았다고 설명. 파이프라인에서 의심 지원자 30%를 식별 | 해외 원격 Pain P4가 강화됨. **함의(추정): 한국에 거주하는 '진짜' 후보도 해외 IP 때문에 미국 기업의 사기 필터에 걸릴 수 있음** → 신원이 검증된 후보라는 보증이 원티드의 가치제안이 될 수 있음 |
| 5 | Gatewell Group은 "회사 정보 확인 불가" | LA 소재 컴플라이언스 회사. **한국 고객은 미국 시장에 처음 진출하는 중견 전자 제조사.** 이 직무는 수출바우처 서류, KOTRA LA 협업, 15시간 시차 회의를 담당. **"미국 취업자격 필수, 비자 스폰서 불가, 남가주 거주"** | S1 B 묶음(미국 근무 × 한국어)에 대한 직접 근거. 원티드 국내 인재풀로는 공급 불가가 원문으로 확인됨. 수요 유형은 ④(미국 진출 한국 기업 응대) |
| 6 | Dover의 "Forge"가 어느 회사인지 특정 불가 | **Forge Global**(비상장 주식 거래 마켓, 2019년 시리즈 B $85M, 약 60명). 시니어 후보가 지원하지 않고, 채용 담당이 2명뿐이라 Dover를 사용 → 주 11명의 관심 후보, 2개월에 2명 채용 | 규모: 당시 스타트업. Pain: ③(시니어 후보 응답) + ②(채용 인력 부족) |
| 7 | Paraform–Brex는 "본문 미확인" | Paraform 고객 사례가 아닌 **분석 글**. 추천 보너스 없이 초기 영업직 60명을 모두 내부 네트워크로 채용(실패 1명) | "해당 없음" 유지. 참고: 유니콘도 핵심 직무는 인맥 중심이라, S1 Pain ②의 "추천 의존"을 뒷받침 |
| 8 | Paraform–Runway는 검색 요약 기준 | 원문: 18개월간 ARR 약 $15만→$400만+, **"지원자 수가 아니라 정확도가 문제"**, 주된 탈락 사유는 기술·문화 기준 미달 | Pain ① 분류가 원문으로 확인됨 |

## 2. 판정표 반영(③ 적합한 후보자와의 연결 어려움)
- 판정은 **"못 푼다" 유지**를 권합니다.
- 근거 문구를 다음으로 바꿔야 합니다.
  > "HireFromKorea가 비개발 bilingual(마케팅·국가 매니저·CS)까지 겨냥하지만 공동 파트너 2명이 운영하고 사례가 익명 3건이라 규모·검증 근거가 부족. 미국 서비스(Gem·Paraform·Arc)는 한국어 직무 사례 0건"
- 발표 때 "HireFromKorea가 이미 하고 있지 않냐"는 질문에는 이렇게 답할 수 있습니다. "같은 문제를 보고 있다는 것 자체가 수요의 신호다. 다만 2인 규모로는 공급량과 검증 체계가 부족하고, 원티드는 인재풀 규모(영·중·일 보유 309,453명)와 데이터로 이를 키울 수 있다."

## 3. 갱신된 파일
- `S1_case_5col_gem_paraform_arc_hfk.xlsx`: Daxko, Terminal, Runway, Brex, Chamberlin Group, Equipboard, HireFromKorea 행을 원문 기준으로 수정(분류 메모에 [원문 확인] 표시)
  - 분류 변화: Arc Chamberlin "분류 불가 → ②", Equipboard "분류 불가 → ③", HireFromKorea "분류 불가 → ③(보조 ②)"
- 이전 문서(`S1_competitor_solutions_vs_wanted.*`, `wantedlab_S1_v2_*`)의 HireFromKorea·Arc 관련 서술은 이 문서의 1·2번 정정이 우선합니다.

Source: [HireFromKorea](https://www.hirefromkorea.com/), [Arc – Chamberlin Group](https://arc.dev/employer-blog/chamberlingroup-case-study/), [Arc – Equipboard](https://arc.dev/employer-blog/equipboard-success-story/), [Gem – Daxko](https://www.gem.com/case-study/daxko), [Gem – Terminal](https://www.gem.com/case-study/terminal), [Gatewell – Korea Practice Coordinator](https://gatewellgroup.com/careers-korea-coordinator), [Dover – Forge](https://www.dover.com/case-studies/forge), [Paraform – Brex](https://www.paraform.com/blog/how-brex-hires-and-why-they-don-t-need-referral-bonuses-to-win), [Paraform – Runway](https://www.paraform.com/blog/runway)
