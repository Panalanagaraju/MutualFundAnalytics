import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

# Print columns for verification
print("\nFund Master Columns:")
print(fund_master.columns.tolist())

print("\nNAV History Columns:")
print(nav_history.columns.tolist())

# Check if amfi_code exists
if "amfi_code" not in fund_master.columns:
    print("\nERROR: 'amfi_code' not found in fund_master.csv")
    exit()

if "amfi_code" not in nav_history.columns:
    print("\nERROR: 'amfi_code' not found in nav_history.csv")
    exit()

# Extract unique AMFI codes
master_codes = set(fund_master["amfi_code"].astype(str))
nav_codes = set(nav_history["amfi_code"].astype(str))

# Find missing codes
missing_codes = master_codes - nav_codes

print("\nTotal Fund Master Codes :", len(master_codes))
print("Total NAV History Codes :", len(nav_codes))
print("Missing Codes Count     :", len(missing_codes))

if len(missing_codes) > 0:
    print("\nFirst 20 Missing Codes:")
    print(list(missing_codes)[:20])
else:
    print("\n✅ All AMFI codes in fund_master exist in nav_history")

# Save validation report
report = pd.DataFrame({
    "metric": [
        "fund_master_codes",
        "nav_history_codes",
        "missing_codes"
    ],
    "value": [
        len(master_codes),
        len(nav_codes),
        len(missing_codes)
    ]
})

report.to_csv(
    "reports/amfi_validation_report.csv",
    index=False
)

print("\nValidation report saved:")
print("reports/amfi_validation_report.csv")