import os
import json
import pandas as pd

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)

for filename in os.listdir(RAW_DIR):
    if filename.endswith(".json"):
        raw_path = os.path.join(RAW_DIR, filename)
        
        with open(raw_path, "r") as file:
            data = json.load(file)

        processed_data = {
            "timestamp": data["dt"],
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        }

        df = pd.DataFrame([processed_data])

        base_name = os.path.splitext(filename)[0]
        processed_path = os.path.join(PROCESSED_DIR, f"{base_name}.csv")
        df.to_csv(processed_path, index=False)

        os.remove(raw_path)
