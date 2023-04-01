""" Main module providing weather information for a given location."""
from mylib.postgresqldb import store_weather_info
from mylib.cities import get_lat_long
from mylib.weather import get_weather
from mylib.utils import add_additional_info
from app.mylib.mylogger import logger


def main():
    """
    Main function of this program. Takes a city a retrieves its current weather information
    :return: None
    """

    # Give city name
    city_name = "Cochabamba"
    country_name = 'Bolivia'

    logger.info(f'Retrieving latitude and longitude for country: \'{country_name}\' and city: \'{city_name}\'')

    lat, long = get_lat_long(country_name, city_name)

    info = get_weather(lat, long)

    # Adding additional info
    info = add_additional_info(info, {'city': city_name, 'country': country_name})

    # Store weather info into the DB
    store_weather_info(info)

    logger.info('Task completed. Closing now...')


if __name__ == "__main__":
    main()
