import json
import requests
from datetime import datetime

# Safe public API (reliable for GitHub Actions)
url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5ENSEI"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)
data = res.json()

spot = data["quoteResponse"]["result"][0]["regularMarketPrice"]

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
    "time": str(datetime.now()),
    "source": "yahoo",
    "strikes": strikes
}

with open("option_data.json", "w") as f:
    json.dump(output, f, indent=2)

print("LIVE SPOT UPDATED")
