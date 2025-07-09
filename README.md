
# 🌦️ Weather ETL & Dashboard Project

A full end-to-end pipeline for collecting, transforming, and visualising live weather data using Python.

## 📦 Project Overview

This project builds a robust ETL pipeline to:
- 📥 Fetch real-time weather data from the OpenWeatherMap API
- 🧹 Transform and clean raw JSON into structured tabular format
- 🗃️ Combine datasets into a single historical `.csv` file
- 📊 Generate an interactive weather dashboard using Vega-Altair

---

## 📁 Directory Structure

```
weather-pipeline/
├── data/
│   ├── raw/                # Raw JSON API responses
│   └── processed/          # Cleaned CSV files, combined dataset
├── notebooks/              # For ad-hoc testing and prototyping
├── scripts/
│   ├── weather_fetcher.py      # Pulls data from API
│   ├── weather_transform.py    # Transforms raw JSON into clean CSV
│   ├── combine_csvs.py         # Combines cleaned CSVs into one
│   └── dashboard.py            # Generates multi-metric Altair dashboard
├── visuals/
│   └── weather_dashboard.html  # Interactive HTML dashboard
├── .env                    # Contains API key (excluded via .gitignore)
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 📊 Dashboard Features

- ✅ Temperature trend over time  
- ✅ Humidity trend  
- ✅ Atmospheric pressure  
- ✅ Wind speed & direction  
- ✅ Cloud coverage  
- ✅ Frequency of weather conditions  
- ✅ Weather descriptions breakdown  

All charts are interactive, linked by timestamp, and saved as a standalone offline HTML dashboard.

---

## ⚙️ Tech Stack

- **Languages:** Python
- **Data Wrangling:** pandas, os, datetime
- **Visualisation:** Altair (Vega-Altair)
- **Environment:** `.env` & `python-dotenv`
- **Automation:** Modular script execution (can be scheduled)

---

## ▶️ How to Run

1. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Add your OpenWeatherMap API Key**
   - Create a `.env` file in the root directory
   ```
   WEATHER_API_KEY=your_api_key_here
   ```

3. **Run scripts in order:**
   ```
   python scripts/weather_fetcher.py
   python scripts/weather_transform.py
   python scripts/combine_csvs.py
   python scripts/dashboard.py
   ```

4. **Open your dashboard**
   ```
   ./visuals/weather_dashboard.html
   ```

---


## 📬 Contact

Built by Cameron Backler  
[GitHub](https://github.com/cqmeronn) | [LinkedIn](https://www.linkedin.com/in/cameron-backler/)
