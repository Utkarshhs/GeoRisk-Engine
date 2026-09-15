import requests
import json

def fetch_weather_archive(lat: float, lon: float, start_date: str, end_date: str) -> dict:
    endpoint = "https://archive-api.open-meteo.com/v1/archive"
    
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": ["temperature_2m", "precipitation", "wind_speed_10m"]
    }
    
    response = requests.get(endpoint, params=params, timeout=15)
    
    response.raise_for_status()
    
    return response.json()

if __name__ == "__main__":
    TARGET_ZONES = [
    {"name": "bengaluru", "lat": 12.9716, "lon": 77.5946},
    {"name": "mumbai", "lat": 19.0760, "lon": 72.8777},
    {"name": "new_york", "lat": 40.7128, "lon": -74.0060},
    {"name": "tokyo", "lat": 35.6762, "lon": 139.6503},
    {"name": "london", "lat": 51.5074, "lon": -0.1278},
]
    start_date = "2018-01-01"
    end_date = "2023-01-01"  

    for zone in TARGET_ZONES:
        weather_data = fetch_weather_archive(zone["lat"], zone["lon"], start_date, end_date)
        file_path = f"data/raw_{zone['name']}.json"
        with open(file_path, "w") as f:
            json.dump(weather_data, f, indent=4)

    print("Data saved successfully to data/raw_*.json")