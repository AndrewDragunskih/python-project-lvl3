import logging


TEXT_FORMAT = ("%(asctime)s - %(funcName)s - %(levelname)s "
               "- %(name)s - %(lineno)d - %(message)s")


def get_file_handler():
    file_handler = logging.FileHandler('page_loader.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(TEXT_FORMAT))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(TEXT_FORMAT))
    return stream_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
