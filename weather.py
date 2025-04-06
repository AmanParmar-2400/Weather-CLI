import requests
import os
from datetime import datetime

# Enter your OpenWeatherMap API key here
user_api = "82854e240a27678e7c6696a6c503e9cb"
location = input("Enter the city name: ")

# Correct API URL with user-entered city name
complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"

api_link = requests.get(complete_api_link)
api_data = api_link.json()

# Check for invalid API key
if api_data.get('cod') == 401:
    print("Error: Invalid API key. Please check your API key at OpenWeatherMap.")
elif api_data.get('cod') == '404':
    print(f"Invalid City: {location}, Please check your city name.")
else:
    temp_city = api_data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-------------------------------------------------------------")
    print(f"Weather Stats for - {location.upper()}  || {date_time}")
    print("-------------------------------------------------------------")
    print(f"Current temperature is: {temp_city:.2f} deg C")
    print(f"Current weather desc  : {weather_desc}")
    print(f"Current Humidity      : {hmdt}%")
    print(f"Current wind speed    : {wind_spd} kmph")
    