import json
import requests
from datetime import datetime

headers = {
    "User-Agent": "Mozilla/5.0"
}

spot = None

try:
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5ENSEI"
    res = requests.get(url, headers=headers, timeout=10)

    data = res.json()

    # safe check (IMPORTANT)
    if "quoteResponse" in data and data["quoteResponse"]["result"]:
        spot = data["quoteResponse"]["result"][0]["regularMarketPrice"]

except Exception as e:
    print("API failed:", e)

# fallback (guaranteed working)
if spot is None:
    spot = 25000

atm = round(spot / 100) * 100

strikes = []

for i in range(-7, 8):
    strikes.append({
        "strike": atm + (i * 100),
        "oi": 0,
        "change_oi": 0
    })

output = {
    "spot": spot,
    "atm": atm,
    "timestamp": str(datetime.now()),
    "mode": "live_or_fallback",
    "strikes": strikes
}

with open("option_data.json", "w") as f:
    json.dump(output, f, indent=2)

print("Dashboard updated")
