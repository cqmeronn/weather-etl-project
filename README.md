# 🌦 Weather ETL Dashboard Project

This project is a lightweight end-to-end **ETL (Extract, Transform, Load)** pipeline that collects real-time weather data from the [OpenWeatherMap API](https://openweathermap.org/api), processes and cleans it, and generates interactive visualizations using Plotly. It runs on Python and is ideal for learning/practicing data engineering workflows.

---

## 🧱 Project Structure

```
weather-pipeline/
├── data/
│   ├── raw/               # Raw JSON API responses
│   └── processed/         # Cleaned CSV files + combined dataset
├── scripts/
│   ├── weather_fetcher.py     # Extracts data from API
│   ├── weather_transform.py   # Transforms JSON to structured CSV
│   ├── combine_csvs.py        # Merges CSVs and removes duplicates
│   └── dashboard.py           # Generates Plotly HTML dashboard
├── visuals/
│   └── weather_dashboard.html # Output visualisation
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔁 Workflow Overview

1. **Extract**  
   `weather_fetcher.py` connects to the OpenWeather API and saves a JSON file of weather conditions for **London**.

2. **Transform**  
   `weather_transform.py` reads the raw `.json`, extracts key metrics (`temperature`, `humidity`, `condition`, etc.), and saves it as a CSV.

3. **Load**  
   `combine_csvs.py` merges all new CSVs into a master file (`weather_data.csv`), sorted by timestamp and free of duplicates.

4. **Visualize**  
   `dashboard.py` creates an interactive Plotly graph for London’s weather trends and saves it as a standalone HTML dashboard.

---

## 📊 Sample Metrics Tracked

- Timestamp (converted from Unix)
- City
- Temperature (°C)
- Humidity (%)
- Weather condition (e.g. "scattered clouds")

---

## 🔧 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

You also need a `.env` file in the root with your API key:

```
OPENWEATHER_API_KEY=your_api_key_here
```

---

## 📅 Automation Tip

You can use **Task Scheduler (Windows)** or **cron (Linux/Mac)** to schedule `weather_fetcher.py` to run every 10 minutes.

---

## ✅ Example Run Order

```bash
python scripts/weather_fetcher.py
python scripts/weather_transform.py
python scripts/combine_csvs.py
python scripts/dashboard.py
```

Then open `visuals/weather_dashboard.html` in your browser.

---

## 📁 .gitignore

Make sure your `.gitignore` includes:

```
.env
__pycache__/
*.pyc
data/raw/
*.ipynb_checkpoints
.venv/
```

---
