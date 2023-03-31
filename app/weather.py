""" Main module providing weather information for a given location."""
import os
import requests
import pandas as pd
from mylib.utils import find_city
from mylib.utils import parse_info
from mylib.postgresqldb import get_connector


def main():
    """
    Main function of this program. Takes a city a retrieves its current weather information
    :return: None
    """

    # get connector
    connector = get_connector()

    # Enter your API key here
    api_key = os.environ.get('API_KEY')

    # Give city name
    city_name = "madrid"

    lat, long = find_city(name=city_name)

    # base_url variable to store url
    base_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&appid={api_key}"

    # get method of requests module
    response = requests.get(base_url, timeout=10)

    if response.status_code == 200:
        info = parse_info(response.json())

        df = pd.DataFrame.from_dict([info])
        df.to_sql('weather_data', con=connector, schema='bronze', if_exists='append', index=False)
        print(info)

    else:
        print(f'Error, status code: {response.status_code}')


if __name__ == "__main__":
    main()
