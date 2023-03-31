'''Connector for postgreSQL database'''
import os
import sqlalchemy


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

    return engine
