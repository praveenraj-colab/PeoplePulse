from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# PEOPLEPULSE - DATA VISUALIZATION
# --------------------------------------------------

# 1. Load dataset
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "HR-Employee-Attrition.csv"

df = pd.read_csv(DATA_PATH)

# Create output folder
OUTPUT_DIR = PROJECT_ROOT / "reports" / "visualizations"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Calculate attrition rates
df["Attrition_Flag"] = (df["Attrition"] == "Yes").astype(int)

sns.set_theme(style="whitegrid")

# --------------------------------------------------
# CHART 1: ATTRITION RATE BY DEPARTMENT
# --------------------------------------------------

department_rate = (
    df.groupby("Department")["Attrition_Flag"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))
sns.barplot(x=department_rate.index, y=department_rate.values)

plt.title("Employee Attrition Rate by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=15)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "01_attrition_by_department.png", dpi=300)
plt.show()
plt.close()

# --------------------------------------------------
# CHART 2: ATTRITION RATE BY OVERTIME
# --------------------------------------------------

overtime_rate = (
    df.groupby("OverTime")["Attrition_Flag"]
    .mean()
    .mul(100)
    .reindex(["No", "Yes"])
)

plt.figure(figsize=(7, 5))
sns.barplot(x=overtime_rate.index, y=overtime_rate.values)

plt.title("Employee Attrition Rate by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "02_attrition_by_overtime.png", dpi=300)
plt.show()
plt.close()

# --------------------------------------------------
# CHART 3: MONTHLY INCOME BY ATTRITION
# --------------------------------------------------

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="Attrition",
    y="MonthlyIncome",
    order=["No", "Yes"],
    showfliers=False
)

plt.title("Monthly Income Distribution by Attrition")
plt.xlabel("Employee Attrition")
plt.ylabel("Monthly Income")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "03_income_by_attrition.png", dpi=300)
plt.show()
plt.close()

# --------------------------------------------------
# CHART 4: YEARS AT COMPANY BY ATTRITION
# --------------------------------------------------

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="Attrition",
    y="YearsAtCompany",
    order=["No", "Yes"],
    showfliers=False
)

plt.title("Years at Company by Attrition")
plt.xlabel("Employee Attrition")
plt.ylabel("Years at Company")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "04_tenure_by_attrition.png", dpi=300)
plt.show()
plt.close()

# --------------------------------------------------
# CHART 5: CORRELATION HEATMAP
# --------------------------------------------------

selected_columns = [
    "Age",
    "MonthlyIncome",
    "YearsAtCompany",
    "JobSatisfaction",
    "WorkLifeBalance",
    "JobInvolvement",
    "EnvironmentSatisfaction"
]

correlation_matrix = df[selected_columns].corr()

plt.figure(figsize=(10, 7))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Workforce Variable Correlation Heatmap")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "05_correlation_heatmap.png", dpi=300)
plt.show()
plt.close()

print("\n" + "=" * 55)
print("PEOPLEPULSE VISUALIZATION COMPLETED")
print("Charts saved in:", OUTPUT_DIR)
print("=" * 55)