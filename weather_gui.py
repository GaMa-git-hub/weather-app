import tkinter as tk
import requests

API_KEY = '11c39a505a13a6c2ed30715a46913087'  # Replace with your actual API key

def get_weather():
    city = city_entry.get()
    if city.lower() == 'exit':
        root.destroy()
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            desc = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            result = f"🌤️ Weather in {city.title()}:\nTemperature: {temp}°C\nHumidity: {humidity}%\nDescription: {desc.title()}\nWind Speed: {wind_speed} m/s"
        else:
            result = f"Error: {data['message'].capitalize()}"

    except Exception as e:
        result = f"Error: {e}"

    result_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter City Name:").pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=5)
result_label = tk.Label(root, text="", justify="left", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()
