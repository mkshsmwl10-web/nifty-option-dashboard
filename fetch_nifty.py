print("Python Working")
import json

data = {
    "spot": 25000,
    "atm": 25000,
    "time": "test"
}

with open("option_data.json", "w") as f:
    json.dump(data, f)

print("JSON Created")
