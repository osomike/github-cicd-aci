""" This is a file containing static information about cities """
import sys
import pandas as pd
from sqlalchemy import text
from app.mylib.postgresqldb import get_connector
from app.mylib.mylogger import logger


def get_lat_long(country_target: str, city_target: str, table:str = 'cities_info', schema: str ='bronze') -> tuple:
    """
    Get lat and long for a given tuple of country and city
    :param country_target: country anme
    :param city_target: city name
    :param table: table in the DB to read
    :param schema: schema in the DB to read
    :return: tuple containing the latitude and longitude
    """

    logger.info('Getting connector to PostgreSQL database...')
    connector = get_connector()
    logger.info('Connector for PostgreSQL ready')

    country_target = country_target.lower()
    city_target = city_target.lower()

    sql_query = \
        f'SELECT * ' \
        f'FROM {schema}.{table} ' \
        f'WHERE LOWER(city)=\'{city_target}\' AND LOWER(country)=\'{country_target}\''

    logger.info(f'Query for DB: {sql_query}')

    cities_df = pd.read_sql(sql=text(sql_query), con=connector)

    rows, cols = cities_df.shape
    if rows == 0:
        logger.error(f'Not information was found for country: \'{country_target}\' and city: \'{city_target}\'')
        connector.close()
        logger.info('Connector closed')
        logger.info('Exiting now...')
        sys.exit(1)

    logger.info(f'Shape of the DataFrane fetched : \'({rows}, {cols})\'')

    # converting to dictionary
    cities_dict = cities_df.iloc[0].to_dict()

    logger.info(f'Info fetched: {cities_dict}')

    # close connector
    connector.close()
    logger.info('PostgreSQL connector closed')

    lat = cities_dict.get('lat')
    long = cities_dict.get('lng')
    logger.info(f'Latitude : {lat} and Longitude : {long}')

    return lat, long
