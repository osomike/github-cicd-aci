import pandas as pd
import datetime


def find_city(name: str) -> tuple:
    df = pd.read_parquet('mylib/cities.parquet')
    info = df[df['city'].str.lower() == name.lower()].sort_values(by='population', ascending=False).iloc[0].to_dict()
    return round(info.get('lat'), 3), round(info.get('lng'), 3)


def convert_kelvin_to_celsius(k: float) -> float:
    return k - 273


def parse_info(wor: dict) -> dict:

    timezone = wor.get('timezone')
    date_time = wor.get('current').get('dt')
    current_date_time_str = datetime.datetime.fromtimestamp(date_time).strftime('%Y-%m-%dT%H:%M:%S')
    current_temperature = round(convert_kelvin_to_celsius(wor.get('current').get('temp')), 2)
    current_feels_like = round(convert_kelvin_to_celsius(wor.get('current').get('feels_like')), 2)
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
