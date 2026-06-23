import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print("="*80)
print("MUTUAL FUND DATA INGESTION")
print("="*80)

for file in csv_files:

    print(f"\n\nDataset: {file}")
    print("-"*80)

    filepath = os.path.join(DATA_PATH, file)

    try:
        df = pd.read_csv(filepath)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}")
        print(e)

print("\nData ingestion completed.")