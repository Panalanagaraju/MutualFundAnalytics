import pandas as pd
import os

# ==========================
# CONFIGURATION
# ==========================

DATA_FOLDER = "data/raw"
REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)

report_lines = []

print("\n" + "="*80)
print("MUTUAL FUND DATA INGESTION")
print("="*80)

# ==========================
# LOAD ALL CSV FILES
# ==========================

csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

for file in sorted(csv_files):

    file_path = os.path.join(DATA_FOLDER, file)

    print("\n")
    print("="*80)
    print(file)
    print("="*80)

    try:

        df = pd.read_csv(file_path)

        # Shape
        print("\nShape")
        print(df.shape)

        # Datatypes
        print("\nData Types")
        print(df.dtypes)

        # Head
        print("\nFirst 5 Rows")
        print(df.head())

        # Missing Values
        missing = df.isnull().sum().sum()

        # Duplicate Rows
        duplicates = df.duplicated().sum()

        print("\nMissing Values :", missing)
        print("Duplicate Rows :", duplicates)

        report_lines.append(
            f"""
FILE : {file}
----------------------------------------
Rows, Columns : {df.shape}
Missing Values : {missing}
Duplicate Rows : {duplicates}

"""
        )

    except Exception as e:

        print(f"Error reading {file}")
        print(e)

        report_lines.append(
            f"""
FILE : {file}
ERROR : {e}
"""
        )

# ==========================
# SAVE REPORT
# ==========================

report_path = os.path.join(
    REPORT_FOLDER,
    "day1_data_quality.txt"
)

with open(report_path, "w", encoding="utf-8") as f:
    f.writelines(report_lines)

print("\n")
print("="*80)
print("REPORT SAVED")
print(report_path)
print("="*80)