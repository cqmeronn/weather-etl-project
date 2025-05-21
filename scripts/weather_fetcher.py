import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

CITY = "London"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
OUTPUT_DIR = "data/raw/"

def fetch_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def save_raw_data(data, city):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}{city.lower()}_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

def main():
    data = fetch_weather(CITY)
    if data:
        save_raw_data(data, CITY)

    print("API KEY:", API_KEY)

if __name__ == "__main__":
    main()
