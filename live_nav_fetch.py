import requests
import pandas as pd
import os

OUTPUT_PATH = "data/raw"

os.makedirs(OUTPUT_PATH, exist_ok=True)

schemes = {
    "HDFC_Top100":125497,
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

for scheme_name, scheme_code in schemes.items():

    print(f"\nFetching {scheme_name}")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        filename = f"{scheme_name}_live_nav.csv"

        filepath = os.path.join(OUTPUT_PATH, filename)

        nav_df.to_csv(filepath, index=False)

        print(f"Saved: {filename}")

    else:

        print(f"Failed: {scheme_name}")