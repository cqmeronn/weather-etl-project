import os
import json
import pandas as pd

RAW_DIR = "data/raw/"
PROCESSED_DIR = "data/processed/"

os.makedirs(PROCESSED_DIR, exist_ok=True)

output_file = os.path.join(PROCESSED_DIR, "weather_data.csv")

data_rows = []

for filename in os.listdir(RAW_DIR):
    if filename.endswith(".json"):
        with open(os.path.join(RAW_DIR, filename)) as f:
            data = json.load(f)
            
            row = {
                "timestamp": data.get("dt"),
                "city": data.get("name"),
                "temperature": data["main"].get("temp"),
                "humidity": data["main"].get("humidity"),
                "pressure": data["main"].get("pressure"),
                "wind_speed": data["wind"].get("speed"),
                "wind_deg": data["wind"].get("deg"),
                "cloud_coverage": data["clouds"].get("all"),
                "weather_main": data["weather"][0].get("main"),
                "weather_desc": data["weather"][0].get("description")
            }

            data_rows.append(row)

df = pd.DataFrame(data_rows)

if os.path.exists(output_file):
    df_existing = pd.read_csv(output_file)
    df_combined = pd.concat([df_existing, df]).drop_duplicates().reset_index(drop=True)
else:
    df_combined = df

df_combined.to_csv(output_file, index=False)
print(f"✅ Transformed data saved to {output_file}")
