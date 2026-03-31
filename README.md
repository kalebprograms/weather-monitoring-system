# Weather Monitoring and Alert System

Built as a personal project to demonstrate monitoring systems, Satelight API reliability, and alerting workflows.

## Overview

This project is a Python-based monitoring tool that retrieves real-time weather data from an external API, validates the response, and logs system activity.

The goal of this project is to simulate real-world monitoring systems that track data reliability, detect failures, and generate alerts when issues occur.

## Features

* Fetches real-time weather data using the Open-Meteo API
* Validates API response structure and required fields
* Logs system activity and results to a JSON file
* Detects and alerts on API failures or invalid data
* Runs continuously to simulate a monitoring system

## Tech Stack

* Python
* Requests
* JSON

## Project Structure

```
weather-monitoring-system/
├── main.py
├── log.json
├── README.md
```

## How It Works

1. Sends a request to the weather API
2. Validates the response data
3. Logs results to a JSON file
4. Prints alerts if errors occur
5. Repeats at a fixed interval

## Setup

### Install dependencies

```bash
pip install requests
```

### Run the project

```bash
python main.py
```

## Example Output

```bash
SUCCESS: Data valid
```

or

```bash
ALERT: API request failed
```

## Future Improvements

* Add retry logic for failed API requests
* Add structured logging with timestamps and severity levels
* Store logs in a database instead of a file
* Add email or notification-based alerts
* Containerize with Docker for deployment

## Purpose

This project was built to demonstrate monitoring system design, API integration, data validation, and logging. These concepts are commonly used in real-world production systems.

## Disclaimer

This project is for educational and portfolio purposes only.
