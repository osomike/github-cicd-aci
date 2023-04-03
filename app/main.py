""" Main module providing weather information for a given location."""
import argparse
from app.mylib.postgresqldb import store_weather_info
from app.mylib.cities import get_lat_long
from app.mylib.weather import get_weather
from app.mylib.utils import add_additional_info
from app.mylib.mylogger import logger


def main(country, city):
    """
    Main function of this program. Takes a city a retrieves its current weather information
    :param country: country name
    :param city: city name
    :return: None
    """

    logger.info(f'Retrieving latitude and longitude for country: \'{country}\' and city: \'{city}\'')

    lat, long = get_lat_long(country, city)

    info = get_weather(lat, long)

    # Adding additional info
    info = add_additional_info(info, {'city': city, 'country': country})

    # Store weather info into the DB
    store_weather_info(info)

    logger.info('Task completed. Closing now...')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='This is a program intended to retrieve weather data from an API using a country and city target')
    parser.add_argument('--country', type=str, help='name of the country', default='Amsterdam')
    parser.add_argument('--city', type=str, help='name of the city', default='Netherlands')

    args = parser.parse_args()

    input_country = args.country
    input_city = args.city

    main(input_country, input_city)
