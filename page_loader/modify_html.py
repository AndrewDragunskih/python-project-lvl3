from urllib.parse import urlparse
from page_loader.get_paths import get_resource_path
from page_loader.get_paths import get_resource_dir_path
from bs4 import BeautifulSoup


ASSETS = [
    {'tag_name': 'img', 'attr_name': 'src'},
    {'tag_name': 'link', 'attr_name': 'href'},
    {'tag_name': 'script', 'attr_name': 'src'},
]


def process_resources_paths(response_text, output_dir, url):
    soup = BeautifulSoup(response_text, "html.parser")
    resource_dir_path = get_resource_dir_path(output_dir, url)
    all_attrs = []
    for asset in ASSETS:
        asset_tags = [
            tag for tag in soup.find_all(asset['tag_name'])
            if urlparse(tag.get(asset['attr_name'])).scheme == '' or
            urlparse(tag.get(asset['attr_name'])).netloc == urlparse(url).netloc
        ]
        asset_attrs = [tag.get(asset['attr_name']) for tag in asset_tags]
        all_attrs.extend(asset_attrs)
        for tag in asset_tags:
            resource_path = get_resource_path(
                resource_dir_path, tag.get(asset['attr_name']),
            )
            tag[asset['attr_name']] = resource_path
    return soup.prettify()
