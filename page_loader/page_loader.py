import requests
import sys
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from page_loader.app_logger import get_logger
from page_loader.get_paths import get_html_file_path
from page_loader.modify_html import process_resources_paths
from page_loader.download_resources import download_resources


class KnownError(Exception):
    pass


def download(url, output_dir):
    logger = get_logger(__name__)
    logger.info("Page loader is started")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        logger.error("HTTP error is occured: {0}".format(http_err))
        raise KnownError() from http_err
    except Exception as err:
        logger.error("Other error is occured: {0}".format(err))
        raise KnownError() from err
    else:
        logger.info("Request is seccessful to url: {0}".format(url))
    logger.info("Start downloding page resources")
    download_resources(response.text, output_dir, url)
    logger.info("Page resources are downloaded seccessfuly")
    logger.info("Start creating html file")
    soup = process_resources_paths(response.text, output_dir, url)
    logger.info("HTML file is created seccessfuly.")
    html_file_path = get_html_file_path(output_dir, url)
    save_data(html_file_path, soup)
    logger.info("Html file is saved to: {0}".format(html_file_path))
    return html_file_path
