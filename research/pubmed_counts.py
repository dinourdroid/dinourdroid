"""B~E군 주제별 PubMed 논문 수(2021-2025) 및 QPI 병행 논문 수 집계.
실행: python3 pubmed_counts.py  -> topic_counts.csv 생성 (표준 라이브러리만 사용)"""
import csv, time, urllib.error, urllib.parse, urllib.request, json

QPI = ('("quantitative phase imaging"[tiab] OR holotomography[tiab] OR "digital holographic microscopy"[tiab] '
       'OR "refractive index tomography"[tiab] OR "optical diffraction tomography"[tiab])')
YEARS = range(2021, 2026)
TOPICS = [
 ("B","지질방울 대사",'"lipid droplet*"[tiab]'),
 ("B","미토콘드리아 투과성 전이·미토파지",'("permeability transition"[tiab] OR mitophagy[tiab])'),
 ("B","핵막·응축체 안정성",'("nuclear envelope"[tiab] OR "biomolecular condensate*"[tiab])'),
 ("B","광학 생체모방(reflectin 등)",'(reflectin[tiab] OR reflectins[tiab] OR "intracellular refractive index"[tiab] OR (organelle*[tiab] AND "light scattering"[tiab]))'),
 ("B","신경세포 형태(성상교세포·축삭)",'((astrocyte*[tiab] AND morpholog*[tiab]) OR "axon growth"[tiab])'),
 ("C","면역세포 치료·기전(CAR-M, NK, 에페로사이토시스)",'("CAR-macrophage*"[tiab] OR "CAR macrophage*"[tiab] OR efferocytosis[tiab] OR ("NK cell*"[tiab] AND cytotoxicity[tiab]))'),
 ("C","약물전달체 세포 흡수",'((nanoparticle*[tiab] OR "extracellular vesicle*"[tiab]) AND (uptake[tiab] OR internalization[tiab]))'),
 ("C","세포사 기전(막 파괴·자가포식 세포사)",'("autophagic cell death"[tiab] OR ("anticancer peptide*"[tiab] AND membrane[tiab]))'),
 ("C","오가노이드 동적(라이브) 이미징",'(organoid*[tiab] AND ("live imaging"[tiab] OR "live-cell imaging"[tiab] OR "time-lapse"[tiab] OR "longitudinal imaging"[tiab]))'),
 ("C","시간축 가상 염색",'(("virtual staining"[tiab] OR "virtual stain*"[tiab] OR "in silico staining"[tiab] OR "in silico labeling"[tiab]) AND ("time-lapse"[tiab] OR "live cell*"[tiab] OR "live-cell"[tiab] OR dynamic*[tiab]))'),
 ("C","NAMs 기반 약물 스크리닝·효능·독성 정량",'(("new approach methodolog*"[tiab] OR NAMs[tiab] OR "organ-on-a-chip"[tiab] OR "organ-on-chip"[tiab] OR (organoid*[tiab] AND "drug screening"[tiab])) AND (screening[tiab] OR efficacy[tiab] OR toxicity[tiab] OR cytotoxicity[tiab]))'),
 ("D","무표지 세포 표현형 분류",'("label-free"[tiab] AND (classification[tiab] OR "machine learning"[tiab] OR "deep learning"[tiab]) AND cell*[tiab])'),
 ("E","세포 질량밀도·건조질량",'(("dry mass"[tiab] OR "mass density"[tiab]) AND cell*[tiab])'),
 ("E","세포 부피·수분 항상성·분자 혼잡",'("cell volume regulation"[tiab] OR "macromolecular crowding"[tiab] OR ("water content"[tiab] AND cell*[tiab]))'),
 ("E","응축체 내부 농도 측정",'("biomolecular condensate*"[tiab] AND concentration[tiab])'),
]

def count(term):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(
        {"db":"pubmed","term":term,"rettype":"count","retmode":"json"})
    for i in range(6):
        time.sleep(0.6 * (i + 1))  # API키 없이 초당 3회 제한, 429 시 재시도
        try:
            return int(json.load(urllib.request.urlopen(url))["esearchresult"]["count"])
        except urllib.error.HTTPError as e:
            if e.code != 429: raise
    raise RuntimeError("PubMed rate limit")

rows=[]
for grp,name,q in TOPICS:
    per=[count(f"{q} AND {y}[dp]") for y in YEARS]
    total=sum(per); qpi=count(f"{q} AND {QPI} AND 2021:2025[dp]")
    cagr=(per[-1]/per[0])**(1/4)-1 if per[0] else 0
    rows.append([grp,name,*per,total,f"{cagr:.1%}",qpi,f"{qpi/total:.2%}" if total else "-",q])
    print(rows[-1][:10])
with open("topic_counts.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["군","주제",*YEARS,"합계","연평균증가율","QPI병행","QPI침투율","검색식"]); w.writerows(rows)
