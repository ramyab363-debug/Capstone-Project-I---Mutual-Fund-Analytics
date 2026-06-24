import requests
import pandas as pd

scheme_code = "125497"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    nav_data = data.get("data", [])

    df = pd.DataFrame(nav_data)

    df.to_csv(
        "data/raw/hdfc_top100_live_nav.csv",
        index=False
    )

    print("Live NAV data saved successfully.")
    print(df.head())

else:
    print("Failed to fetch NAV data")