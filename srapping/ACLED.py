import os
import requests
import pandas as pd

# Your ACLED API credentials
API_KEY = "your_api_key"
EMAIL = "christian.s.wilkinson@gmail.com"

# Folder to save data
SAVE_DIR = "../data/ACLED"
os.makedirs(SAVE_DIR, exist_ok=True)

# Base URL for the ACLED API
BASE_URL = "https://api.acleddata.com/acled/read"

# Define query parameters (customize as needed)
params = {
    "key": API_KEY,
    "email": EMAIL,
    "country": "Sudan",
    "year": 2024,
    "limit": 1000,           # Get 1000 rows (you can paginate or increase)
    "fields": "event_date|event_type|actor1|country|fatalities|location"
}

# Make GET request
response = requests.get(BASE_URL, params=params)
if response.status_code == 200:
    data = response.json()
    records = data.get("data", [])
    df = pd.DataFrame(records)

    # Save to CSV
    output_path = os.path.join(SAVE_DIR, "acled_sudan_2024.csv")
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} records to: {output_path}")
else:
    print(f"Request failed: {response.status_code}")
    print(response.text)
