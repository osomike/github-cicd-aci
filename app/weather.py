import requests
import os
from mylib.utils import find_city
from mylib.utils import parse_info


def main():
    # Enter your API key here
    api_key = os.environ('API_KEY')

    # Give city name
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


if __name__ == "__main__":
    main()