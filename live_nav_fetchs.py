import requests
import pandas as pd
import os

scheme_codes = {
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

output_dir = "data/raw/live_nav"

os.makedirs(output_dir, exist_ok=True)

for name, code in scheme_codes.items():

    print(f"Fetching {name}")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    file_path = os.path.join(
        output_dir,
        f"{name}.csv"
    )

    nav_df.to_csv(file_path,index=False)

    print(f"Saved -> {file_path}")