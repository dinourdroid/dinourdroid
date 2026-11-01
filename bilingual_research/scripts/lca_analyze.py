"""Screen DOL LCA (H-1B) disclosure data for California + Korea/bilingual signals.

STATUS: written without access to the real file (dol.gov blocked automated
download from the analysis environment). Column names follow the OFLC record
layout as commonly published; the script checks for each column and stops
with a clear message if the layout differs. Verify against the record-layout
PDF for the fiscal year you download.

Usage: python3 lca_analyze.py <LCA_Disclosure_Data_FYxxxx_Qx.xlsx> <out_dir>
"""
import re
import sys

import pandas as pd

NEED = ["CASE_STATUS", "VISA_CLASS", "JOB_TITLE", "SOC_CODE", "SOC_TITLE",
        "EMPLOYER_NAME", "WORKSITE_STATE", "WORKSITE_CITY",
        "WAGE_RATE_OF_PAY_FROM", "WAGE_UNIT_OF_PAY", "PW_WAGE_LEVEL",
        "TOTAL_WORKER_POSITIONS", "NAICS_CODE"]
SIGNAL = re.compile(r"korea|korean|bilingual|multilingual|apac|asia[- ]pacific|japan|localization", re.I)
ANNUAL = {"Year": 1, "Month": 12, "Bi-Weekly": 26, "Week": 52, "Hour": 2080}


def main():
    src, out = sys.argv[1], sys.argv[2]
    df = pd.read_excel(src, dtype=str)
    missing = [c for c in NEED if c not in df.columns]
    if missing:
        sys.exit(f"Columns not found (check record layout): {missing}\nAvailable: {list(df.columns)}")
    df = df[(df.CASE_STATUS.str.startswith("Certified")) & (df.VISA_CLASS == "H-1B")]
    ca = df[df.WORKSITE_STATE.isin(["CA", "CALIFORNIA"])].copy()
    ca["wage_annual"] = pd.to_numeric(ca.WAGE_RATE_OF_PAY_FROM.str.replace(",", ""), errors="coerce") * \
        ca.WAGE_UNIT_OF_PAY.map(ANNUAL)
    ca["positions"] = pd.to_numeric(ca.TOTAL_WORKER_POSITIONS, errors="coerce").fillna(1)
    ca["signal"] = ca.JOB_TITLE.fillna("").str.contains(SIGNAL)

    # Employer size proxy: number of certified CA LCAs per employer.
    size = ca.groupby("EMPLOYER_NAME").size().rename("employer_lcas")
    ca = ca.join(size, on="EMPLOYER_NAME")
    ca["size_band"] = pd.cut(ca.employer_lcas, [0, 5, 25, 100, 10**9], labels=["1-5", "6-25", "26-100", "100+"])

    summary = {
        "certified_h1b_total": len(df),
        "certified_h1b_ca": len(ca),
        "ca_share": round(len(ca) / max(len(df), 1), 4),
        "ca_signal_titles": int(ca.signal.sum()),
    }
    pd.Series(summary).to_csv(f"{out}/lca_summary.csv")
    ca.groupby("SOC_TITLE").positions.sum().sort_values(ascending=False).head(30).to_csv(f"{out}/lca_ca_top_soc.csv")
    ca.groupby(["size_band", "PW_WAGE_LEVEL"], observed=True).size().unstack(fill_value=0).to_csv(f"{out}/lca_ca_size_by_level.csv")
    ca[ca.signal][["EMPLOYER_NAME", "JOB_TITLE", "SOC_TITLE", "WORKSITE_CITY", "wage_annual", "PW_WAGE_LEVEL",
                   "employer_lcas"]].sort_values("EMPLOYER_NAME").to_csv(f"{out}/lca_ca_signal_titles.csv", index=False)
    print(summary)


if __name__ == "__main__":
    main()
