""" Utils library module providing utilities to retrieve weather information for a given location."""
import datetime


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
    :param city: city
    :param country: Country
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


def add_additional_info(base_dict: dict, additional_info: dict) -> dict:
    """
    Add additional info to dictionary
    :param base_dict: base dictionary
    :param additional_info: additional info
    :return:
    """
    base_dict.update(additional_info)
    return base_dict
