""" Main module providing weather information for a given location."""
import os
import requests
from mylib.utils import find_city
from mylib.utils import parse_info


def main():
    """
    Main function of this program. Takes a city a retrieves its current weather information
    :return: None
    """
    # Enter your API key here
    api_key = os.environ.get('API_KEY')

    # Give city name
    # city_name = "amsterdam"

    lat, long = find_city(name='amsterdam')

    # base_url variable to store url
    base_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&appid={api_key}"

    # get method of requests module
    response = requests.get(base_url, timeout=10)

    if response.status_code == 200:
        info = parse_info(response.json())
        print(info)

    else:
        print(f'Error, status code: {response.status_code}')


if __name__ == "__main__":
    main()
