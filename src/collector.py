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
    # Example usage
    lat = 40.7128  # Latitude for New York City
    lon = -74.0060  # Longitude for New York City
    start_date = "2023-01-01"
    end_date = "2023-01-07"
    
    weather_data = fetch_weather_archive(lat, lon, start_date, end_date)
    
    print(json.dumps(weather_data, indent=4))