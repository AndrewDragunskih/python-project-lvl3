from urllib.parse import urlparse
from requests.exceptions import HTTPError
from page_loader.app_logger import get_logger
from page_loader.get_paths import get_resource_path
from page_loader.get_paths import get_resource_dir_path
from page_loader.save_data import save_data, make_dir
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


def download_resources(response_text, output_dir, url):
    logger = get_logger(__name__)
    soup = BeautifulSoup(response_text, "html.parser")
    resource_dir_path = get_resource_dir_path(output_dir, url)
    make_dir(resource_dir_path)
    all_attrs = []
    for asset in ASSETS:
        asset_tags = [
            tag for tag in soup.find_all(asset['tag_name'])
            if urlparse(tag.get(asset['attr_name'])).scheme == ''
        ]
        asset_attrs = [tag.get(asset['attr_name']) for tag in asset_tags]
        all_attrs.extend(asset_attrs)
    with Bar('Processing', max=len(all_attrs)) as bar:
        for attr in all_attrs:
            resource_url = '{0}://{1}{2}{3}'.format(
                urlparse(url).scheme,
                urlparse(url).netloc,
                '/' if attr[0] != '/' else '',
                attr,
            )
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
