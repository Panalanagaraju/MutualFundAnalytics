import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

# Display basic information
print("\n" + "="*80)
print("FUND MASTER ANALYSIS")
print("="*80)

print("\nDataset Shape")
print(df.shape)

print("\nAvailable Columns")
print(df.columns.tolist())

# Fund Houses
if 'fund_house' in df.columns:
    print("\nUnique Fund Houses")
    print(df['fund_house'].unique())
    print(f"\nTotal Fund Houses: {df['fund_house'].nunique()}")

# Categories
if 'category' in df.columns:
    print("\nCategories")
    print(df['category'].unique())
    print(f"\nTotal Categories: {df['category'].nunique()}")

# Sub Categories
subcat_col = None

for col in df.columns:
    if col.lower() in ['subcategory', 'sub_category', 'sub-category']:
        subcat_col = col
        break

if subcat_col:
    print("\nSub Categories")
    print(df[subcat_col].unique())
    print(f"\nTotal Sub Categories: {df[subcat_col].nunique()}")
else:
    print("\nSub Category column not found in dataset.")

# Risk Grade
risk_col = None

for col in df.columns:
    if col.lower() in ['risk_grade', 'riskgrade', 'risk']:
        risk_col = col
        break

if risk_col:
    print("\nRisk Grades")
    print(df[risk_col].unique())
    print(f"\nTotal Risk Grades: {df[risk_col].nunique()}")
else:
    print("\nRisk Grade column not found in dataset.")

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Duplicate Records
print("\nDuplicate Records")
print(df.duplicated().sum())

print("\n" + "="*80)
print("ANALYSIS COMPLETED")
print("="*80)