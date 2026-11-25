from pathlib import Path

import pandas as pd
from scipy.stats import chi2_contingency, mannwhitneyu

# --------------------------------------------------
# PEOPLEPULSE - STATISTICAL ANALYSIS
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "HR-Employee-Attrition.csv"

df = pd.read_csv(DATA_PATH)

ALPHA = 0.05

print("=" * 60)
print("PEOPLEPULSE - STATISTICAL ANALYSIS")
print("=" * 60)


# --------------------------------------------------
# TEST 1: OVERTIME AND ATTRITION
# Chi-square test of independence
# --------------------------------------------------

print("\n1. OVERTIME AND ATTRITION")

overtime_table = pd.crosstab(
    df["OverTime"],
    df["Attrition"]
)

chi2, p_value, dof, expected = chi2_contingency(overtime_table)

print("\nContingency table:")
print(overtime_table)

print(f"\nChi-square statistic: {chi2:.4f}")
print(f"P-value: {p_value:.6f}")
print(f"Degrees of freedom: {dof}")

if p_value < ALPHA:
    print("Result: Statistically significant association.")
else:
    print("Result: No statistically significant association.")


# --------------------------------------------------
# TEST 2: DEPARTMENT AND ATTRITION
# Chi-square test of independence
# --------------------------------------------------

print("\n2. DEPARTMENT AND ATTRITION")

department_table = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

chi2, p_value, dof, expected = chi2_contingency(department_table)

print("\nContingency table:")
print(department_table)

print(f"\nChi-square statistic: {chi2:.4f}")
print(f"P-value: {p_value:.6f}")
print(f"Degrees of freedom: {dof}")

if p_value < ALPHA:
    print("Result: Statistically significant association.")
else:
    print("Result: No statistically significant association.")


# --------------------------------------------------
# TEST 3: MONTHLY INCOME AND ATTRITION
# Mann-Whitney U test
# --------------------------------------------------

print("\n3. MONTHLY INCOME AND ATTRITION")

income_stayed = df.loc[
    df["Attrition"] == "No", "MonthlyIncome"
]

income_left = df.loc[
    df["Attrition"] == "Yes", "MonthlyIncome"
]

statistic, p_value = mannwhitneyu(
    income_stayed,
    income_left,
    alternative="two-sided"
)

print(f"\nMedian income - Stayed: {income_stayed.median():.2f}")
print(f"Median income - Left: {income_left.median():.2f}")
print(f"Mann-Whitney U statistic: {statistic:.2f}")
print(f"P-value: {p_value:.6f}")

if p_value < ALPHA:
    print("Result: Statistically significant income difference.")
else:
    print("Result: No statistically significant income difference.")


# --------------------------------------------------
# TEST 4: YEARS AT COMPANY AND ATTRITION
# Mann-Whitney U test
# --------------------------------------------------

print("\n4. YEARS AT COMPANY AND ATTRITION")

tenure_stayed = df.loc[
    df["Attrition"] == "No", "YearsAtCompany"
]

tenure_left = df.loc[
    df["Attrition"] == "Yes", "YearsAtCompany"
]

statistic, p_value = mannwhitneyu(
    tenure_stayed,
    tenure_left,
    alternative="two-sided"
)

print(f"\nMedian tenure - Stayed: {tenure_stayed.median():.2f}")
print(f"Median tenure - Left: {tenure_left.median():.2f}")
print(f"Mann-Whitney U statistic: {statistic:.2f}")
print(f"P-value: {p_value:.6f}")

if p_value < ALPHA:
    print("Result: Statistically significant tenure difference.")
else:
    print("Result: No statistically significant tenure difference.")


print("\n" + "=" * 60)
print("STATISTICAL ANALYSIS COMPLETED")
print("=" * 60)