import requests

API_KEY = "2aa0671eee13e2a238ab685e4c93be0d"  # 🔑 Replace this with your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = f"{BASE_URL}appid={API_KEY}&q={city}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Description: {weather['description'].title()}")
    else:
        print(f"City not found: {data['message']}")

# --- Main ---
if __name__ == "__main__":
    print("=== Weather App ===")
    city = input("Enter city name: ")
    get_weather(city)
