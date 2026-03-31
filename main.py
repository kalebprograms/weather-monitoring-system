import requests
import time
import json
from datetime import datetime

# API endpoint for Washington, DC with current weather and 4-day forecast
API_URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=38.9072"
    "&longitude=-77.0369"
    "&current_weather=true"
    "&daily=temperature_2m_max,temperature_2m_min"
    "&temperature_unit=fahrenheit"
    "&timezone=auto"
)


def fetch_weather():
    # Sends a GET request to the weather API and returns JSON data
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()  # Raises error if request fails
        return response.json()
    except Exception as e:
        # Returns error message if request fails
        return {"error": str(e)}


def validate(data):
    # Checks if required current and forecast fields exist in the API response
    try:
        has_current = (
            "current_weather" in data
            and "temperature" in data["current_weather"]
        )

        has_daily = (
            "daily" in data
            and "time" in data["daily"]
            and "temperature_2m_max" in data["daily"]
            and "temperature_2m_min" in data["daily"]
        )

        return has_current and has_daily
    except Exception:
        return False


def log_result(status, data):
    # Creates a log entry with timestamp, status, and relevant data
    log_entry = {
        "timestamp": str(datetime.now()),
        "status": status,
        "data": data
    }

    # Appends log entry to a JSON file for tracking system behavior
    with open("log.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")


def display_weather(data):
    # Extracts and prints current temperature and 4-day forecast
    current_temp = data["current_weather"]["temperature"]
    print(f"\nCurrent temperature in Washington, DC: {current_temp}°F")

    # Get first 4 days of forecast data
    dates = data["daily"]["time"][:4]
    max_temps = data["daily"]["temperature_2m_max"][:4]
    min_temps = data["daily"]["temperature_2m_min"][:4]

    print("\n4-Day Forecast:")
    for date, max_temp, min_temp in zip(dates, max_temps, min_temps):
        print(f"{date}: High {max_temp}°F | Low {min_temp}°F")


def run_monitor():
    # Main workflow that fetches, validates, logs, and displays weather data
    data = fetch_weather()

    # Handle API failure
    if "error" in data:
        print("ALERT: API request failed")
        log_result("error", data["error"])
        return

    # Validate data and process results
    if validate(data):
        print("SUCCESS: Data valid")
        display_weather(data)

        # Log only relevant weather data (not entire API response)
        log_result(
            "success",
            {
                "current_weather": data["current_weather"],
                "daily_forecast": {
                    "time": data["daily"]["time"][:4],
                    "temperature_2m_max": data["daily"]["temperature_2m_max"][:4],
                    "temperature_2m_min": data["daily"]["temperature_2m_min"][:4],
                },
            },
        )
    else:
        print("ALERT: Data validation failed")
        log_result("error", data)


if __name__ == "__main__":
    # Runs the monitoring process once (good for normal usage and testing)
    run_monitor()
