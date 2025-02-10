import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CITY = "LAGOS"

# Load API Key safely


def load_api_key(filename="api_key.txt"):
    try:
        with open(filename, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: API key file not found.")
        return None


API_KEY = load_api_key()

# Convert temperature from Kelvin to Celsius and Fahrenheit


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * 9/5 + 32
    return round(celsius, 2), round(fahrenheit, 2)

# Fetch weather data


def get_weather_data(city, api_key):
    url = f"{BASE_URL}?appid={api_key}&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# Parse and display weather data


def display_weather_info(city, weather_data):
    if not weather_data:
        print("No weather data available.")
        return

    main = weather_data.get("main", {})
    wind = weather_data.get("wind", {})
    sys = weather_data.get("sys", {})
    weather_desc = weather_data.get("weather", [{}])[
        0].get("description", "N/A")
    timezone_offset = weather_data.get("timezone", 0)

    # Convert temperature
    temperature_k = main.get("temp")
    feels_like_k = main.get("feels_like")
    humidity = main.get("humidity", "N/A")
    wind_speed = wind.get("speed", "N/A")

    temperature_c, temperature_f = kelvin_to_celsius_fahrenheit(temperature_k)
    feels_like_c, feels_like_f = kelvin_to_celsius_fahrenheit(feels_like_k)

    # Convert sunrise and sunset times
    sunrise_time = dt.datetime.utcfromtimestamp(
        sys.get("sunrise", 0) + timezone_offset)
    sunset_time = dt.datetime.utcfromtimestamp(
        sys.get("sunset", 0) + timezone_offset)

    # Display results
    print(f"\n🌍 Weather Report for {city.upper()} 🌤")
    print(f"-----------------------------------")
    print(f"🌡  Temperature: {temperature_c}°C / {temperature_f}°F")
    print(f"🤗 Feels Like: {feels_like_c}°C / {feels_like_f}°F")
    print(f"💧 Humidity: {humidity}%")
    print(f"💨 Wind Speed: {wind_speed} m/s")
    print(f"📜 Condition: {weather_desc.capitalize()}")
    print(f"🌅 Sunrise: {sunrise_time} local time")
    print(f"🌇 Sunset: {sunset_time} local time\n")


# Main execution
if __name__ == "__main__":
    if API_KEY:
        weather_data = get_weather_data(CITY, API_KEY)
        display_weather_info(CITY, weather_data)
