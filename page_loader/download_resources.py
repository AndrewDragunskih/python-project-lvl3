from urllib.parse import urlparse
from requests.exceptions import HTTPError
from page_loader.app_logger import get_logger
from page_loader.paths_module import get_resource_path, get_resource_dir_path
from page_loader.data_module import get_attr_name_from_tag
from page_loader.fs_module import save_data, make_dir
from progress.bar import Bar
import requests


class KnownError(Exception):
    pass


def make_resourse_url(attr, url):
    if urlparse(attr).scheme == '':
        return '{0}://{1}{2}{3}'.format(
            urlparse(url).scheme,
            urlparse(url).netloc,
            '/' if attr[0] != '/' else '',
            attr,
        )
    return attr


def download_resources(all_tags, output_dir, url):
    logger = get_logger(__name__)
    resource_dir_path = get_resource_dir_path(output_dir, url)
    if all_tags != []:
        make_dir(resource_dir_path)
        with Bar('Processing', max=len(all_tags)) as bar:
            for tag in all_tags:
                attr = tag[get_attr_name_from_tag(tag)]
                resource_url = make_resourse_url(attr, url)
                try:
                    content = requests.get(resource_url)
                    content.raise_for_status()
                except HTTPError as http_err:
                    logger.error("HTTP error is occured: {0}".format(http_err))
                except Exception as err:
                    logger.error("Other error is occured: {0}".format(err))
                    raise KnownError() from err
                resource_path = get_resource_path(resource_dir_path, url, attr)
                save_data(resource_path, content.content, access_mode='wb')
                bar.next()
