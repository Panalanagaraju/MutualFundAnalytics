import pandas as pd
import os

DATA_DIR = "data/raw"

csv_files = [
    file for file in os.listdir(DATA_DIR)
    if file.endswith(".csv")
]

for file in csv_files:

    print("\n" + "="*80)
    print(file)
    print("="*80)

    df = pd.read_csv(
        os.path.join(DATA_DIR, file)
    )

    print("\nShape")
    print(df.shape)

    print("\nData Types")
    print(df.dtypes)

    print("\nHead")
    print(df.head())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicates")
    print(df.duplicated().sum())