# Weather App

This project contains two versions of a Python Weather application that fetches real-time weather data using the OpenWeatherMap API.

---

## Version 1: CLI Weather App

A simple Command-Line Interface (CLI) application that allows users to enter a city name and receive current weather details such as temperature, humidity, description, and wind speed.

### Features:
- Fetches real-time weather data from OpenWeatherMap API.
- Displays temperature in Celsius, humidity percentage, weather description, and wind speed.
- User-friendly command-line input with exit option.
- Basic error handling for invalid city names or API errors.

### Usage Example:
Enter city name (or 'exit' to quit): Chennai

🌤️ Weather in Chennai:
Temperature: 32.26°C
Humidity: 70%
Description: Haze
Wind Speed: 5.14 m/s



---

## Version 2: GUI Weather App

An enhanced version with a graphical user interface built using Python's Tkinter library. This app allows users to input the city name via a window and displays weather information dynamically.

### Features:
- Intuitive GUI with input box and buttons.
- Displays weather details in a clean, readable format.
- Real-time API fetching with error messages shown in the interface.
- Same weather details as the CLI version.

---

## Technologies Used

- Python 3
- `requests` library for HTTP requests
- OpenWeatherMap API for weather data
- Tkinter for GUI (version 2)

---

## Getting Started

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
2. Set your API key in the project files.
3. Run the CLI or GUI version as needed.

---

## Future Enhancements

- Add support for multiple cities at once.
- Include forecast data (3-day, 7-day).
- Add unit switching (Celsius/Fahrenheit).
- Implement caching to reduce API calls.

---


