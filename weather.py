import requests
from dotenv import load_dotenv
import os 
from pprint import pprint



load_dotenv()


def get_current_weather(city="Sacramento"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()
    return weather_data

    #print('\n***Get Current Weather Conditions***\n')
    # city = input("Please enter a city name:\n")
    #pprint(weather_data)

    #print(f"\nCurrent weather for {city}")
    #print(f'\nTemperture is {weather_data["main"]["temp"]}')

if __name__ == "__main__":
    print('\n***Get Current Weather Conditions***\n')
    city = input("Please enter a city name:\n")

    if not bool(city.strip()):
        city = "Sacramento"

    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)

