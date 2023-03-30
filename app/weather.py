import requests
import pandas as pd
import datetime
import os


def find_city(name: str) -> tuple:
    df = pd.read_parquet('../data/cities.parquet')
    info = df[df['city'].str.lower() == name.lower()].sort_values(by='population', ascending=False).iloc[0].to_dict()
    return info.get('lat'), info.get('lng')


def parse_info(wor: dict) -> dict:

    timezone = wor.get('timezone')
    date_time = wor.get('current').get('dt')
    current_date_time_str = datetime.datetime.fromtimestamp(date_time).strftime('%Y-%m-%dT%H:%M:%S')
    current_temperature = round(wor.get('current').get('temp') - 273, 2)
    current_feels_like = round(wor.get('current').get('feels_like') - 273, 2)
    current_humidity = wor.get('current').get('humidity')
    current_wind_speed = wor.get('current').get('wind_speed')
    current_weather_descriotion = wor.get('current').get('weather')[0].get('description')

    return {
        'timezone': timezone,
        'date_time': current_date_time_str,
        'temperature': current_temperature,
        'feels_lie': current_feels_like,
        'humidity': current_humidity,
        'wind_speed': current_wind_speed,
        'weather_description': current_weather_descriotion
    }



# Enter your API key here
api_key = "b07501bf2bf32d9b3e4fe128d42af230"

# Give city name
#city_name = input("Enter city name : ")
city_name = "amsterdam"

lat, long = find_city(name='amsterdam')

# base_url variable to store url
base_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&appid={api_key}"

# get method of requests module
response = requests.get(base_url)

if response.status_code == 200:
    x = parse_info(response.json())
    print(x)

else:
    print(f'Error, status code: {response.status_code}')
