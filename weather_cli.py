import requests

API_KEY = "11c39a505a13a6c2ed30715a46913087"  # Replace this with your actual API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
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
