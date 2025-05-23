import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not API_KEY:
        print("Error: API key not found. Make sure it's set in the .env file.")
        return

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get('cod') != 200:
            print("Error:", data.get('message'))
            return

        print(f"\n🌤️ Weather in {city.title()}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description'].capitalize()}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        get_weather(city)
v