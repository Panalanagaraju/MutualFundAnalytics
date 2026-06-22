import requests
import pandas as pd
import os

schemes = {
    "HDFC_Top100":125497,
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

os.makedirs("data/raw", exist_ok=True)

for scheme_name, scheme_code in schemes.items():

    print(f"Fetching {scheme_name}")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df["scheme_code"] = scheme_code
        nav_df["scheme_name"] = data["meta"]["scheme_name"]

        file_name = f"data/raw/{scheme_name}.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"Saved: {file_name}")

    else:
        print(f"Failed: {scheme_name}")