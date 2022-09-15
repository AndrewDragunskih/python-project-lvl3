import requests
from requests.exceptions import HTTPError
from page_loader.app_logger import get_logger


class KnownError(Exception):
    pass


def get_page_response(url, client=requests):
    logger = get_logger(__name__)
    logger.info("Getting data...")
    try:
        page_response = client.get(url)
        page_response.raise_for_status()
    except HTTPError as http_err:
        logger.info("HTTP error is occured: {0}".format(http_err))
        raise KnownError() from http_err
    except Exception as err:
        logger.info("Other error is occured: {0}".format(err))
        raise KnownError() from err
    else:
        logger.info("Succesful!")
    return page_response


def get_page_text(url, client=requests):
    return get_page_response(url, client).text


def get_page_content(url, client=requests):
    return get_page_response(url, client).content
