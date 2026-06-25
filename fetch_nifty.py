import json
from datetime import datetime

spot = 25000  # temporary (baad me API se aayega)

atm = round(spot / 100) * 100

strikes = []

# ATM ± 7 strikes (100 points gap)
for i in range(-7, 8):
    strike = atm + (i * 100)
    strikes.append({
        "strike": strike,
        "type": "CE/PE",
        "oi": 0,
        "change_oi": 0
    })

data = {
    "spot": spot,
    "atm": atm,
    "timestamp": str(datetime.now()),
    "strikes": strikes
}

with open("option_data.json", "w") as f:
    json.dump(data, f, indent=2)

print("Dashboard JSON Updated")
