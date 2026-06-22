import requests
import pandas as pd
import os

# ==================================
# OUTPUT DIRECTORY
# ==================================

OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==================================
# FUND LIST
# ==================================

funds = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

# ==================================
# FETCH DATA
# ==================================

for fund_name, scheme_code in funds.items():

    print(f"\nDownloading {fund_name}")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_path = os.path.join(
            OUTPUT_DIR,
            f"{fund_name}_nav.csv"
        )

        nav_df.to_csv(
            file_path,
            index=False
        )

        print(f"Saved : {file_path}")

    else:

        print(
            f"Failed for {fund_name}"
        )

print("\nDownload Completed")