import pandas as pd
import os

RAW_PATH = "data/raw"

print("\n" + "="*80)
print("DAY 1 DATA INGESTION")
print("="*80)

csv_files = [f for f in os.listdir(RAW_PATH) if f.endswith(".csv")]

summary = []

for file in csv_files:

    filepath = os.path.join(RAW_PATH, file)

    print("\n" + "="*80)
    print(file)
    print("="*80)

    try:
        df = pd.read_csv(filepath)

        print("\nShape")
        print(df.shape)

        print("\nData Types")
        print(df.dtypes)

        print("\nFirst 5 Rows")
        print(df.head())

        summary.append({
            "file": file,
            "rows": df.shape[0],
            "columns": df.shape[1]
        })

    except Exception as e:
        print(f"Error reading {file}: {e}")

print("\n")
print("="*80)
print("SUMMARY")
print("="*80)

summary_df = pd.DataFrame(summary)

print(summary_df)