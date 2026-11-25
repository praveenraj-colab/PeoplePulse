from pathlib import Path

import pandas as pd
import numpy as np

# Locate the project and dataset
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "HR-Employee-Attrition.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("=" * 50)
print("PEOPLEPULSE - DATA VALIDATION")
print("=" * 50)

# 1. Dataset dimensions
print("\n1. DATASET DIMENSIONS")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Column names and data types
print("\n2. COLUMN DATA TYPES")
print(df.dtypes)

# 3. Missing values
print("\n3. MISSING VALUES")
print(df.isnull().sum().to_string())
print("Total missing values:", df.isnull().sum().sum())

# 4. Duplicate records
print("\n4. DUPLICATE RECORDS")
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate EmployeeNumber:", df["EmployeeNumber"].duplicated().sum())

# 5. Unique employee count
print("\n5. EMPLOYEE COUNT")
print("Unique employees:", df["EmployeeNumber"].nunique())

# 6. Attrition distribution
print("\n6. ATTRITION DISTRIBUTION")
print(df["Attrition"].value_counts())

print("\nAttrition percentage:")
print((df["Attrition"].value_counts(normalize=True) * 100).round(2))

# 7. Numeric summary
print("\n7. NUMERIC SUMMARY")
print(df.describe().round(2).to_string())

print("\n" + "=" * 50)
print("DATA VALIDATION COMPLETED")
print("=" * 50)