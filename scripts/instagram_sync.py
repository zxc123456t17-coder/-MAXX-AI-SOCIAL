import os
import requests
import json
from datetime import datetime

TOKEN = os.environ.get("META_ACCESS_TOKEN")
ACCOUNT_ID = os.environ.get("INSTAGRAM_ACCOUNT_ID")

if not TOKEN or not ACCOUNT_ID:
    raise RuntimeError("Missing Instagram API credentials")

url = f"https://graph.facebook.com/v24.0/{ACCOUNT_ID}/insights"

params = {
    "metric": "reach,views,accounts_engaged",
    "period": "day",
    "access_token": TOKEN
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

data = response.json()

os.makedirs("data", exist_ok=True)

filename = f"data/instagram-{datetime.now().strftime('%Y-%m-%d')}.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("Instagram data saved:", filename)
