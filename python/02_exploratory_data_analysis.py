from pathlib import Path

import pandas as pd
import numpy as np

# --------------------------------------------------
# PEOPLEPULSE - EXPLORATORY DATA ANALYSIS
# --------------------------------------------------

# 1. Load dataset
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "HR-Employee-Attrition.csv"

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("PEOPLEPULSE - EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# 2. Basic dataset information
print("\n1. DATASET OVERVIEW")
print("Shape:", df.shape)
print("\nFirst five records:")
print(df.head().to_string())

# 3. Employee age distribution
print("\n2. AGE DISTRIBUTION")
print(df["Age"].describe().round(2))

# 4. Gender distribution
print("\n3. GENDER DISTRIBUTION")
print(df["Gender"].value_counts())

# 5. Department distribution
print("\n4. DEPARTMENT DISTRIBUTION")
print(df["Department"].value_counts())

# 6. Job role distribution
print("\n5. JOB ROLE DISTRIBUTION")
print(df["JobRole"].value_counts())

# 7. Attrition distribution
print("\n6. ATTRITION DISTRIBUTION")
print(df["Attrition"].value_counts())

# 8. Attrition by department
print("\n7. ATTRITION BY DEPARTMENT")

department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

department_attrition["Total Employees"] = department_attrition.sum(axis=1)

department_attrition["Attrition Rate (%)"] = (
    department_attrition["Yes"]
    / department_attrition["Total Employees"]
    * 100
).round(2)

print(department_attrition.to_string())

# 9. Attrition by gender
print("\n8. ATTRITION BY GENDER")

gender_attrition = pd.crosstab(
    df["Gender"],
    df["Attrition"]
)

gender_attrition["Total Employees"] = gender_attrition.sum(axis=1)

gender_attrition["Attrition Rate (%)"] = (
    gender_attrition["Yes"]
    / gender_attrition["Total Employees"]
    * 100
).round(2)

print(gender_attrition.to_string())

# 10. Attrition by overtime
print("\n9. ATTRITION BY OVERTIME")

overtime_attrition = pd.crosstab(
    df["OverTime"],
    df["Attrition"]
)

overtime_attrition["Total Employees"] = overtime_attrition.sum(axis=1)

overtime_attrition["Attrition Rate (%)"] = (
    overtime_attrition["Yes"]
    / overtime_attrition["Total Employees"]
    * 100
).round(2)

print(overtime_attrition.to_string())

# 11. Monthly income comparison
print("\n10. MONTHLY INCOME BY ATTRITION")

income_analysis = df.groupby("Attrition")["MonthlyIncome"].agg(
    ["count", "mean", "median", "min", "max"]
).round(2)

print(income_analysis.to_string())

# 12. Years at company comparison
print("\n11. YEARS AT COMPANY BY ATTRITION")

tenure_analysis = df.groupby("Attrition")["YearsAtCompany"].agg(
    ["count", "mean", "median", "min", "max"]
).round(2)

print(tenure_analysis.to_string())

# 13. Job satisfaction comparison
print("\n12. JOB SATISFACTION BY ATTRITION")

satisfaction_analysis = df.groupby("Attrition")["JobSatisfaction"].mean().round(2)

print(satisfaction_analysis.to_string())

# 14. Correlation between selected numeric variables
print("\n13. SELECTED NUMERIC CORRELATIONS")

selected_columns = [
    "Age",
    "MonthlyIncome",
    "YearsAtCompany",
    "JobSatisfaction",
    "WorkLifeBalance",
    "JobInvolvement",
    "EnvironmentSatisfaction"
]

correlation_matrix = df[selected_columns].corr().round(2)

print(correlation_matrix.to_string())

print("\n" + "=" * 60)
print("EXPLORATORY DATA ANALYSIS COMPLETED")
print("=" * 60)