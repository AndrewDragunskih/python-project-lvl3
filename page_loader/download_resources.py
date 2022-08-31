from urllib.parse import urlparse
from requests.exceptions import HTTPError
from page_loader.app_logger import get_logger
from page_loader.paths_module import get_resource_path, get_resource_dir_path
from page_loader.data_module import get_tags_list, get_attr_name_from_tag
from page_loader.fs_module import save_data, make_dir
from progress.bar import Bar
from bs4 import BeautifulSoup
import requests


class KnownError(Exception):
    pass


ASSETS = [
    {'tag_name': 'img', 'attr_name': 'src'},
    {'tag_name': 'link', 'attr_name': 'href'},
    {'tag_name': 'script', 'attr_name': 'src'},
]


def make_resourse_url(attr, url):
    if urlparse(attr).scheme == '':
        return '{0}://{1}{2}{3}'.format(
            urlparse(url).scheme,
            urlparse(url).netloc,
            '/' if attr[0] != '/' else '',
            attr,
        )
    return attr


def download_resources(response_text, output_dir, url):
    logger = get_logger(__name__)
    #soup = BeautifulSoup(response_text, "html.parser")
    resource_dir_path = get_resource_dir_path(output_dir, url)
    make_dir(resource_dir_path)
    all_tags = get_tags_list(response_text, url)
    with Bar('Processing', max=len(all_tags)) as bar:
        for tag in all_tags:
            attr = tag[get_attr_name_from_tag(tag)]
            resource_url = make_resourse_url(attr, url)
            try:
                content = requests.get(resource_url)
                content.raise_for_status()
            except HTTPError as http_err:
                print()
                logger.error("HTTP error is occured: {0}".format(http_err))
            except Exception as err:
                print()
                logger.error("Other error is occured: {0}".format(err))
                raise KnownError() from err
            resource_path = get_resource_path(resource_dir_path, attr)
            save_data(resource_path, content.content, access_mode='wb')
            bar.next()
