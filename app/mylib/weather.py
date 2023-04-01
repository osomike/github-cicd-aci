"""Weather module"""
import os
import sys
import requests

from app.mylib.utils import parse_info
from app.mylib.mylogger import logger


def get_weather(lat: float, long: float) -> dict:
    """
    Retrieve weather info from open weather map
    :param lat: latitude
    :param long: longitude
    :return: weather info
    """
    # Enter your API key here
    api_key = os.environ.get('API_KEY')

    # Format base URL
    base_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&appid={api_key}"

    logger.info(f'Retrieving weather data for lat : {lat} and long : {long}')

    # get method towards URL
    response = requests.get(base_url, timeout=10)

    if response.status_code == 200:

        info = parse_info(response.json())
        logger.info(f'200 Response with content: {info}')

    else:
        logger.error(f'Something went wrong. Server response: {response.status_code}')
        logger.info('Exiting now...')
        sys.exit(1)

    return info
