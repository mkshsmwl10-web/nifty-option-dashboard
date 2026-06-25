import json
import requests
from datetime import datetime

headers = {"User-Agent": "Mozilla/5.0"}

def get_spot():
    try:
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5ENSEI"
        r = requests.get(url, headers=headers, timeout=5)
        d = r.json()

        if "quoteResponse" in d and d["quoteResponse"]["result"]:
            return float(d["quoteResponse"]["result"][0]["regularMarketPrice"])
    except:
        pass

    return None


spot = get_spot()

# FINAL fallback
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
    "status": "hybrid_system",
    "strikes": strikes
}

with open("option_data.json", "w") as f:
    json.dump(output, f, indent=2)

print("HYBRID DASHBOARD UPDATED")
