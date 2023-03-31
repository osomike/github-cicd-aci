""" Utils library module providing utilities to retrieve weather information for a given location."""
import datetime
import pandas as pd
from app.mylib.cities import CITIES_INFO


def find_city(name: str) -> tuple:
    """
    Return the latitude and longitude from a given city
    :param name: city name
    :return: lat, long (tuple)
    """
    cities_df = pd.DataFrame.from_dict(CITIES_INFO)
    info = cities_df[
        cities_df['city'].str.lower() == name.lower()].iloc[0].to_dict()

    return round(info.get('lat'), 3), round(info.get('lng'), 3)


def convert_kelvin_to_celsius(k: float) -> float:
    """
    Method to convert kelvin to celsius
    :param k: kelvin
    :return: celsius
    """
    return k - 273


def parse_info(wor: dict) -> dict:
    """
    Method to parse information retrived by the API
    :param wor: dictionary with weather information from the API
    :return: formatted weather information
    """
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
