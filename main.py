import requests
import time
import json
from datetime import datetime

# API endpoint for retrieving current weather data (Washington DC coordinates)
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=38.9&longitude=-77.0&current_weather=true"


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
    # Checks if required fields exist in the API response
    try:
        return "current_weather" in data and "temperature" in data["current_weather"]
    except Exception:
        return False


def log_result(status, data):
    # Creates a log entry with timestamp, status, and data
    log_entry = {
        "timestamp": str(datetime.now()),
        "status": status,
        "data": data if status == "success" else "error"
    }

    # Appends log entry to a JSON file for record keeping
    with open("log.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")


def run_monitor():
    # Main monitoring workflow that fetches, validates, and logs data
    data = fetch_weather()

    # Handle API failure
    if "error" in data:
        print("ALERT: API request failed")
        log_result("error", data["error"])
        return

    # Validate data and log results
    if validate(data):
        print("SUCCESS: Data valid")
        log_result("success", data["current_weather"])
    else:
        print("ALERT: Data validation failed")
        log_result("error", data)


if __name__ == "__main__":
    # Runs the monitoring loop a fixed number of times (prevents infinite loop)
    for _ in range(5):
        run_monitor()
        time.sleep(30)  # Wait 30 seconds between checks
