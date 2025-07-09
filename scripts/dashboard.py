import pandas as pd
import altair as alt

# Load and preprocess the data
df = pd.read_csv("data/processed/weather_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
df = df[df["city"] == "London"]

# Base chart config
base = alt.Chart(df).encode(x=alt.X("timestamp:T", title="Time"))

# Time-series line charts
temperature_chart = base.mark_line(color="red").encode(
    y=alt.Y("temperature:Q", title="Temperature (°C)")
).properties(title="Temperature in London")

humidity_chart = base.mark_line(color="blue").encode(
    y=alt.Y("humidity:Q", title="Humidity (%)")
).properties(title="Humidity in London")

pressure_chart = base.mark_line(color="green").encode(
    y=alt.Y("pressure:Q", title="Pressure (hPa)")
).properties(title="Pressure in London")

wind_speed_chart = base.mark_line(color="purple").encode(
    y=alt.Y("wind_speed:Q", title="Wind Speed (m/s)")
).properties(title="Wind Speed in London")

wind_direction_chart = base.mark_line(color="orange").encode(
    y=alt.Y("wind_deg:Q", title="Wind Direction (°)")
).properties(title="Wind Direction in London")

cloud_coverage_chart = base.mark_line(color="gray").encode(
    y=alt.Y("cloud_coverage:Q", title="Cloud Coverage (%)")
).properties(title="Cloud Coverage in London")

# Bar charts for weather types
weather_main_chart = alt.Chart(df).mark_bar(color="salmon").encode(
    x=alt.X("weather_main:N", title="Weather"),
    y=alt.Y("count():Q", title="Count")
).properties(title="Weather Condition Frequency")

weather_desc_chart = alt.Chart(df).mark_bar(color="skyblue").encode(
    x=alt.X("weather_desc:N", title="Description"),
    y=alt.Y("count():Q", title="Count")
).properties(title="Weather Descriptions")

# Assemble dashboard
row1 = alt.hconcat(temperature_chart, humidity_chart, pressure_chart, weather_main_chart)
row2 = alt.hconcat(wind_speed_chart, wind_direction_chart, cloud_coverage_chart, weather_desc_chart)
dashboard = alt.vconcat(row1, row2).properties(
    title={
        "text": "London Weather Dashboard",
        "subtitle": ["Visualizing real-time data via E.T.L pipeline"],
        "anchor": "start"
    }
)

# Save to file
dashboard.save("visuals/weather_dashboard.html")
