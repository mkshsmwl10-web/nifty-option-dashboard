import json
import requests
from datetime import datetime

url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com"
}

session = requests.Session()

try:
    # first hit homepage (important)
    session.get("https://www.nseindia.com", headers=headers, timeout=10)

    # then API call
    response = session.get(url, headers=headers, timeout=10)

    # debug safety
    if response.status_code != 200:
        raise Exception(f"HTTP {response.status_code}")

    data = response.json()

    spot = data["records"]["underlyingValue"]

except Exception as e:
    print("NSE blocked or failed, using fallback")
    print(str(e))

    # fallback (safe)
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
    "note": "fallback mode if NSE blocked",
    "strikes": strikes
}

with open("option_data.json", "w") as f:
    json.dump(output, f, indent=2)

print("Dashboard updated")
