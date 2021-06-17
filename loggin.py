import logging
logging.basicConfig(filename='pruebalog.txt', filemode='a', format='%(message)s - %(asctime)s',datefmt='%d-%m-%Y %H:%M:%S')
# logging.basicConfig(filename='logger.txt', filemode='a', format='%(message)s - %(asctime)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

logging.warning('is when this event was logged.')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')