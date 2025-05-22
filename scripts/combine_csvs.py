import os
import pandas as pd
from pathlib import Path

PROCESSED_DIR = Path("data/processed")
OUTPUT_FILE = PROCESSED_DIR / "weather_data.csv"

if OUTPUT_FILE.exists():
    print("🔍 Found existing weather_data.csv")
    combined_df = pd.read_csv(OUTPUT_FILE)
else:
    print("📄 No existing combined file, starting fresh")
    combined_df = pd.DataFrame()

csv_files = [f for f in PROCESSED_DIR.glob("*.csv") if f.name != OUTPUT_FILE.name]
print(f"📦 Found {len(csv_files)} new files: {[f.name for f in csv_files]}")

new_dfs = [pd.read_csv(f) for f in csv_files]
if not new_dfs:
    print("⚠️ No new data found to process.")
    exit()

new_data = pd.concat(new_dfs, ignore_index=True)

if not combined_df.empty:
    combined_df = pd.concat([combined_df, new_data], ignore_index=True)
else:
    combined_df = new_data

if 'timestamp' in combined_df.columns:
    combined_df.drop_duplicates(inplace=True)
    combined_df.sort_values(by="timestamp", inplace=True)
else:
    print("⚠️ No 'timestamp' column found!")

combined_df.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Combined data saved to {OUTPUT_FILE}")

for f in csv_files:
    try:
        f.unlink()
        print(f"🗑️ Deleted {f.name}")
    except Exception as e:
        print(f"❌ Failed to delete {f.name}: {e}")
