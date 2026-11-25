from pathlib import Path
import pandas as pd
from scipy.stats import chi2_contingency, mannwhitneyu
import math

# --------------------------------------------------
# PEOPLEPULSE - BUSINESS INSIGHTS
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "HR-Employee-Attrition.csv"
REPORT_DIR = PROJECT_ROOT / "reports"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

ALPHA = 0.05
results = []

# --------------------------------------------------
# HELPER: HOLM MULTIPLE-TEST CORRECTION
# --------------------------------------------------

def holm_adjust(p_values):
    count = len(p_values)
    ordered = sorted(
        enumerate(p_values),
        key=lambda item: item[1]
    )

    adjusted = [0.0] * count
    previous = 0.0

    for rank, (original_index, p_value) in enumerate(ordered):
        corrected = min(1.0, (count - rank) * p_value)
        corrected = max(corrected, previous)

        adjusted[original_index] = corrected
        previous = corrected

    return adjusted


# --------------------------------------------------
# TEST 1: OVERTIME AND ATTRITION
# --------------------------------------------------

overtime_table = pd.crosstab(df["OverTime"], df["Attrition"])

chi2, p, dof, expected = chi2_contingency(overtime_table)

n = overtime_table.to_numpy().sum()
cramers_v = math.sqrt(
    chi2 / (n * min(overtime_table.shape[0] - 1,
                    overtime_table.shape[1] - 1))
)

results.append({
    "Analysis": "Overtime vs Attrition",
    "Test": "Chi-square",
    "Statistic": chi2,
    "P-value": p,
    "Effect Size": cramers_v,
    "Effect Size Name": "Cramer's V",
    "Minimum Expected Count": expected.min()
})

# --------------------------------------------------
# TEST 2: DEPARTMENT AND ATTRITION
# --------------------------------------------------

department_table = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

chi2, p, dof, expected = chi2_contingency(department_table)

n = department_table.to_numpy().sum()
cramers_v = math.sqrt(
    chi2 / (n * min(department_table.shape[0] - 1,
                    department_table.shape[1] - 1))
)

results.append({
    "Analysis": "Department vs Attrition",
    "Test": "Chi-square",
    "Statistic": chi2,
    "P-value": p,
    "Effect Size": cramers_v,
    "Effect Size Name": "Cramer's V",
    "Minimum Expected Count": expected.min()
})

# --------------------------------------------------
# TEST 3: MONTHLY INCOME AND ATTRITION
# --------------------------------------------------

income_stayed = df.loc[
    df["Attrition"] == "No", "MonthlyIncome"
]

income_left = df.loc[
    df["Attrition"] == "Yes", "MonthlyIncome"
]

u_stat, p = mannwhitneyu(
    income_stayed,
    income_left,
    alternative="two-sided"
)

income_effect = (
    2 * u_stat / (len(income_stayed) * len(income_left))
) - 1

results.append({
    "Analysis": "Monthly Income vs Attrition",
    "Test": "Mann-Whitney U",
    "Statistic": u_stat,
    "P-value": p,
    "Effect Size": income_effect,
    "Effect Size Name": "Rank-biserial correlation",
    "Minimum Expected Count": None
})

# --------------------------------------------------
# TEST 4: TENURE AND ATTRITION
# --------------------------------------------------

tenure_stayed = df.loc[
    df["Attrition"] == "No", "YearsAtCompany"
]

tenure_left = df.loc[
    df["Attrition"] == "Yes", "YearsAtCompany"
]

u_stat, p = mannwhitneyu(
    tenure_stayed,
    tenure_left,
    alternative="two-sided"
)

tenure_effect = (
    2 * u_stat / (len(tenure_stayed) * len(tenure_left))
) - 1

results.append({
    "Analysis": "Years at Company vs Attrition",
    "Test": "Mann-Whitney U",
    "Statistic": u_stat,
    "P-value": p,
    "Effect Size": tenure_effect,
    "Effect Size Name": "Rank-biserial correlation",
    "Minimum Expected Count": None
})

# --------------------------------------------------
# APPLY HOLM CORRECTION
# --------------------------------------------------

raw_p_values = [item["P-value"] for item in results]
adjusted_p_values = holm_adjust(raw_p_values)

for item, adjusted_p in zip(results, adjusted_p_values):
    item["Holm Adjusted P-value"] = adjusted_p
    item["Significant After Correction"] = adjusted_p < ALPHA

results_df = pd.DataFrame(results)

# Save statistical results
results_df.to_csv(
    REPORT_DIR / "statistical_results.csv",
    index=False
)

# --------------------------------------------------
# GENERATE BUSINESS INSIGHTS REPORT
# --------------------------------------------------

department_rates = (
    df.groupby("Department")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

overtime_rates = (
    df.groupby("OverTime")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

income_medians = df.groupby("Attrition")["MonthlyIncome"].median()
tenure_medians = df.groupby("Attrition")["YearsAtCompany"].median()

overall_attrition = (df["Attrition"] == "Yes").mean() * 100

report = []

report.append("# PeoplePulse - Workforce Intelligence Report")
report.append("")
report.append("## 1. Project Overview")
report.append(
    "PeoplePulse analyses employee attrition patterns using "
    "the IBM HR Analytics Employee Attrition dataset."
)
report.append("")
report.append(f"- Employees analysed: {len(df):,}")
report.append(f"- Dataset columns: {df.shape[1]}")
report.append(f"- Employees who left: {(df['Attrition'] == 'Yes').sum():,}")
report.append(f"- Overall dataset attrition proportion: {overall_attrition:.2f}%")
report.append("")
report.append("## 2. Key Workforce Findings")

report.append(
    f"- Highest department attrition: {department_rates.index[0]} "
    f"({department_rates.iloc[0]:.2f}%)."
)

report.append(
    f"- Overtime attrition: {overtime_rates['Yes']:.2f}%."
)

report.append(
    f"- Non-overtime attrition: {overtime_rates['No']:.2f}%."
)

report.append(
    f"- Median monthly income among employees who stayed: "
    f"{income_medians['No']:,.0f}."
)

report.append(
    f"- Median monthly income among employees who left: "
    f"{income_medians['Yes']:,.0f}."
)

report.append(
    f"- Median tenure among employees who stayed: "
    f"{tenure_medians['No']:.0f} years."
)

report.append(
    f"- Median tenure among employees who left: "
    f"{tenure_medians['Yes']:.0f} years."
)

report.append("")
report.append("## 3. Statistical Test Results")

for _, row in results_df.iterrows():
    report.append("")
    report.append(f"### {row['Analysis']}")
    report.append(f"- Test: {row['Test']}")
    report.append(f"- Test statistic: {row['Statistic']:.4f}")
    report.append(f"- Raw p-value: {row['P-value']:.8g}")
    report.append(
        f"- Holm-adjusted p-value: "
        f"{row['Holm Adjusted P-value']:.8g}"
    )
    report.append(
        f"- Effect size ({row['Effect Size Name']}): "
        f"{row['Effect Size']:.4f}"
    )

    if pd.notna(row["Minimum Expected Count"]):
        report.append(
            f"- Minimum expected cell count: "
            f"{row['Minimum Expected Count']:.2f}"
        )

    report.append(
        "- Conclusion: Statistically significant after Holm correction."
        if row["Significant After Correction"]
        else "- Conclusion: Not statistically significant after Holm correction."
    )

report.append("")
report.append("## 4. HR Recommendations for Further Investigation")
report.append("")
report.append(
    "1. Investigate workload, scheduling and overtime patterns."
)
report.append(
    "2. Review department-specific employee retention challenges."
)
report.append(
    "3. Examine compensation structures and pay progression."
)
report.append(
    "4. Study early-tenure employee experience and onboarding."
)
report.append("")
report.append("## 5. Limitations")
report.append("")
report.append(
    "- This is a synthetic, cross-sectional dataset, not live company data."
)
report.append(
    "- Observed associations do not establish causation."
)
report.append(
    "- Statistical significance does not necessarily indicate business importance."
)
report.append(
    "- Findings should be validated using real organisational data "
    "before making HR policy decisions."
)
report.append(
    "- Multiple-testing correction was applied to the four statistical tests."
)
report.append("")
report.append("## 6. Conclusion")
report.append(
    "The analysis identifies workforce characteristics associated "
    "with employee attrition. These findings can guide further HR "
    "investigation, but should not be treated as causal explanations."
)

report_path = REPORT_DIR / "PeoplePulse_Business_Insights.md"

report_path.write_text(
    "\n".join(report),
    encoding="utf-8"
)

print("=" * 60)
print("PEOPLEPULSE - BUSINESS INSIGHTS COMPLETED")
print("=" * 60)

print("\nStatistical results:")
print(
    results_df[
        [
            "Analysis",
            "P-value",
            "Holm Adjusted P-value",
            "Effect Size",
            "Significant After Correction"
        ]
    ].to_string(index=False)
)

print("\nReports saved:")
print(REPORT_DIR / "statistical_results.csv")
print(report_path)