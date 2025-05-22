import pandas as pd
import altair as alt
import os

COMBINED_FILE = "data/processed/weather_data.csv"

data = pd.read_csv(COMBINED_FILE)
data["timestamp"] = pd.to_datetime(data["timestamp"], unit='s', errors='coerce')
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
