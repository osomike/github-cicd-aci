"""Main Logger for the weather app application"""
import logging

logger = logging.getLogger('weather app')
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s | %(name)s | %(module)s | %(levelname)s | %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
