import logging
logger = logging.getLogger()
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

logger.info('So should this')

