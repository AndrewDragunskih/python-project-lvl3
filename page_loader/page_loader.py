from page_loader.app_logger import get_logger
from page_loader.requests_module import make_request
from page_loader.paths_module import get_html_file_path
from page_loader.data_module import process_resources_paths
from page_loader.download_resources import download_resources
from page_loader.fs_module import save_data


class KnownError(Exception):
    pass


def download(url, output_dir):
    logger = get_logger(__name__)
    logger.info("Page loader is started")
    response = make_request(url)
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
