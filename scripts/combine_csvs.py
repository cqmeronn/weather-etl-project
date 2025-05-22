import os
import pandas as pd
from pathlib import Path

PROCESSED_DIR = Path("data/processed")
OUTPUT_FILE = PROCESSED_DIR / "weather_data.csv"

csv_files = [f for f in PROCESSED_DIR.glob("*.csv") if f.name != OUTPUT_FILE.name]

df_list = [pd.read_csv(f) for f in csv_files]
if not df_list:
    print("No CSV files found to combine.")
    exit()

combined_df = pd.concat(df_list, ignore_index=True)

combined_df.drop_duplicates(inplace=True)
combined_df.sort_values(by="timestamp", inplace=True)

combined_df.to_csv(OUTPUT_FILE, index=False)
print(f"Combined data saved to {OUTPUT_FILE}")
