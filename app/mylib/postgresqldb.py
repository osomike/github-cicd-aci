"""Connector for postgreSQL database"""
import os
import sys
import pandas as pd
import sqlalchemy
from app.mylib.mylogger import logger


def get_connector():
    """
    Return connector engine for psotgresql database
    :return: connector
    """

    host = os.environ.get('DB_HOST')
    database = os.environ.get('DB_NAME')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    # set up database connection
    engine = sqlalchemy.create_engine(f'postgresql://{user}:{password}@{host}/{database}')

    # connector
    connector = engine.connect()
    return connector


def store_weather_info(info, table_name='weather_data', schema='bronze', if_exists='append'):
    """
    Method used to store the weather data into the PostgreSQL database
    :param info: info to be stored
    :param table_name: table name
    :param schema: schema
    :param if_exists: if exists behavior
    :return: None
    """
    # get connector for DB
    connector = get_connector()

    # Create DataFrane from weather info
    info_df = pd.DataFrame.from_dict([info])

    try:
        logger.info('Storing weather info into the Database...')

        info_df.to_sql(table_name, con=connector.engine, schema=schema, if_exists=if_exists, index=False)

        logger.info('Data stored successfully')

    except Exception as an_exception:

        logger.error(f'Something went wrong. Error: {an_exception}')

        connector.close()
        logger.info('Connector closed')

        logger.info('Exiting now...')

        sys.exit(1)

    # close connector
    connector.close()
    logger.info('Connector closed')
