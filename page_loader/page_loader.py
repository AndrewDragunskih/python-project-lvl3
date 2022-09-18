from page_loader.app_logger import get_logger
from page_loader.requests_module import get_page_text
from page_loader.data_module import process_page_data
from page_loader.download_resources import download_resources
from page_loader.fs_module import save_data
from page_loader.paths_module import get_html_file_path


def download(url, output_dir):
    logger = get_logger(__name__)
    logger.info("Page loader is started")
    page_text_data = get_page_text(url)
    logger.info("Start creating html file")
    page_resources_data, modified_page_text_data = process_page_data(
        page_text_data,
        output_dir,
        url,
    )
    html_file_path = get_html_file_path(output_dir, url)
    save_data(html_file_path, modified_page_text_data)
    logger.info("Html file is saved to: {0}".format(html_file_path))
    logger.info("Start downloding page resources")
    download_resources(page_resources_data, output_dir, url)
    logger.info("Page resources are downloaded seccessfuly")
    return html_file_path
