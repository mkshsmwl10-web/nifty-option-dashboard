import json
import requests
from datetime import datetime

# NSE unofficial endpoint (spot data)
url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

session = requests.Session()
session.get("https://www.nseindia.com", headers=headers)

response = session.get(url, headers=headers)
data = response.json()

spot = data["records"]["underlyingValue"]

atm = round(spot / 100) * 100

strikes = []

for i in range(-7, 8):
    strike = atm + (i * 100)
    strikes.append({
        "strike": strike,
        "type": "CE/PE",
        "oi": 0,
        "change_oi": 0
    })

output = {
    "spot": spot,
    "atm": atm,
    "timestamp": str(datetime.now()),
    "strikes": strikes
}

with open("option_data.json", "w") as f:
    json.dump(output, f, indent=2)

print("Live NIFTY data updated")
