import json
from datetime import datetime

# temporary safe structure (we will upgrade live sources later)
spot = 25000  # placeholder (free system limitation)

atm = round(spot / 100) * 100

strikes = []
for i in range(-7, 8):
    strikes.append({
        "strike": atm + (i * 100),
        "ce_oi": 0,
        "pe_oi": 0,
        "change_oi": 0
    })

data = {
    "spot": spot,
    "atm": atm,
    "timestamp": str(datetime.now()),
    "type": "github_free_system",
    "strikes": strikes
}

with open("option_data.json", "w") as f:
    json.dump(data, f, indent=2)

print("GitHub data updated")
