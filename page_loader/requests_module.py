import requests
from requests.exceptions import HTTPError
from page_loader.app_logger import get_logger


class KnownError(Exception):
    pass


def make_request(url):
    logger = get_logger(__name__)
    logger.info("Getting data...")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        logger.info("HTTP error is occured: {0}".format(http_err))
        raise KnownError() from http_err
    except Exception as err:
        logger.info("Other error is occured: {0}".format(err))
        raise KnownError() from err
    else:
        logger.info("Succesful!")
    return response
