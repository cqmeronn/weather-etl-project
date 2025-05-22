import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"

df = pd.read_csv('data/processed/weather_data.csv')

df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

df = df[df['city'] == 'London']

fig = go.Figure()

fig.add_trace(go.Scatter(x=df['timestamp'], y=df['temperature'],
                         mode='lines+markers',
                         name='Temperature',
                         line=dict(color='royalblue')))

fig.add_trace(go.Scatter(x=df['timestamp'], y=df['humidity'],
                         mode='lines+markers',
                         name='Humidity',
                         line=dict(color='green')))

fig.update_traces(hovertemplate='Time: %{x}<br>Value: %{y}<br>Condition: %{text}',
                  text=df['weather'])

fig.update_layout(
    title='Weather Trends in London',
    xaxis_title='Time',
    yaxis_title='Value',
    legend_title='Metric',
    hovermode='x unified'
)

fig.write_html("visuals/weather_dashboard.html")
