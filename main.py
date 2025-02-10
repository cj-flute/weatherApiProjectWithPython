import datetime as d
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

API_KEY = open('api_key.txt', 'r').read()

CITY = 'LAGOS'


def kelvin_to_celsius_fahrenheit_converter(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()


temprature_in_kelvin = response['main']['temp']
temprature_in_celsius, temprature_in_fahrenheit = kelvin_to_celsius_fahrenheit_converter(
    temprature_in_kelvin)

feels_like_in_kelvin = response['main']['feels_like']
feels_like_in_celsius, feels_like_in_fahrenheit = kelvin_to_celsius_fahrenheit_converter(
    feels_like_in_kelvin)


humidity = response['main']['humidity']

description = response['weather'][0]['description']

sunrise_time = d.datetime.utcfromtimestamp(
    response['sys']['sunrise'] + response['timezone'])

sunset_time = d.datetime.utcfromtimestamp(
    response['sys']['sunset'] + response['timezone'])

wind_speed = response['wind']['speed']

print(
    f"Temprature in {CITY}: {temprature_in_celsius: .2f}°C or {temprature_in_fahrenheit: .2f}°F")

print(
    f"Temprature in {CITY}: feels like: {feels_like_in_celsius: .2f}°C or {feels_like_in_fahrenheit: .2f}°F")

print(
    f"Humidity in {CITY}: {humidity}%")

print(
    f"Speed of wind in {CITY}: {wind_speed}m/s")

print(
    f"General weather in {CITY}: {description}")


print(
    f"Sunriese in {CITY} at {sunrise_time} local time.")
print(
    f"Sunsets in {CITY} at {sunset_time} local time.")
