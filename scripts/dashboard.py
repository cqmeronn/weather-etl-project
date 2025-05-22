import pandas as pd
import altair as alt
import os

DATA_PATH = os.path.join("data", "processed", "weather_data.csv")
df = pd.read_csv(DATA_PATH)
df = df[df["city"] == "London"]

df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

base = alt.Chart(df).encode(x=alt.X("timestamp:T", title="Time"))

temp_chart = base.mark_line(color="steelblue").encode(
    y=alt.Y("temperature:Q", title="Temperature (°C)")
).properties(title="Temperature in London")

humidity_chart = base.mark_line(color="green").encode(
    y=alt.Y("humidity:Q", title="Humidity (%)")
).properties(title="Humidity in London")

pressure_chart = base.mark_line(color="orange").encode(
    y=alt.Y("pressure:Q", title="Pressure (hPa)")
).properties(title="Pressure in London")

wind_speed_chart = base.mark_line(color="purple").encode(
    y=alt.Y("wind_speed:Q", title="Wind Speed (m/s)")
).properties(title="Wind Speed in London")

wind_deg_chart = base.mark_line(color="teal").encode(
    y=alt.Y("wind_deg:Q", title="Wind Direction (°)")
).properties(title="Wind Direction in London")

cloud_chart = base.mark_line(color="gray").encode(
    y=alt.Y("cloud_coverage:Q", title="Cloud Coverage (%)")
).properties(title="Cloud Coverage in London")

condition_chart = alt.Chart(df).mark_bar(color="salmon").encode(
    x=alt.X("weather_main:N", title="Weather"),
    y=alt.Y("count():Q", title="Count")
).properties(title="Weather Condition Frequency")

desc_chart = alt.Chart(df).mark_bar(color="tomato").encode(
    x=alt.X("weather_desc:N", title="Description"),
    y=alt.Y("count():Q", title="Count")
).properties(title="Weather Descriptions")

row1 = temp_chart | humidity_chart
row2 = pressure_chart | wind_speed_chart
row3 = wind_deg_chart | cloud_chart
row4 = condition_chart | desc_chart

dashboard = alt.vconcat(row1, row2, row3, row4).resolve_scale(x='shared')

dashboard.save(os.path.join("visuals", "weather_dashboard.html"))
print("✅ Dashboard saved to visuals/weather_dashboard.html")
