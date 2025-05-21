import os
import pandas as pd
import altair as alt

PROCESSED_DIR = "data/processed"

all_data = []

for filename in os.listdir(PROCESSED_DIR):
    if filename.endswith(".csv"):
        df = pd.read_csv(os.path.join(PROCESSED_DIR, filename))
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit='s', errors='coerce')
        all_data.append(df)

if not all_data:
    raise ValueError("No processed data found.")

data = pd.concat(all_data)

data = data.sort_values("timestamp")

temp_chart = alt.Chart(data).mark_line().encode(
    x='timestamp:T',
    y='temperature:Q',
    tooltip=["timestamp", "temperature"]
).properties(
    title="Temperature in London Over Time"
)

humidity_chart = alt.Chart(data).mark_line(color='green').encode(
    x='timestamp:T',
    y='humidity:Q',
    tooltip=["timestamp", "humidity"]
).properties(
    title="Humidity in London Over Time"
)

final_chart = alt.vconcat(temp_chart, humidity_chart)


os.makedirs("visuals", exist_ok=True)

final_chart.save("visuals/weather_dashboard.html")

print("✅ Dashboard saved to visuals/weather_dashboard.html")