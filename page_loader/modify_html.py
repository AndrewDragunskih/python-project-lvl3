from urllib.parse import urlparse
from page_loader.get_paths import get_resource_path
from page_loader.get_paths import get_resource_dir_path
from page_loader.get_paths import get_html_file_path
from page_loader.save_data import save_data
from bs4 import BeautifulSoup


ASSETS = [
    {'tag_name': 'img', 'attr_name': 'src'},
    {'tag_name': 'link', 'attr_name': 'href'},
    {'tag_name': 'script', 'attr_name': 'src'},
]


def process_resources_paths(response_text, output_dir, url):
    soup = BeautifulSoup(response_text, "html.parser")
    resource_dir_path = get_resource_dir_path(output_dir, url)
    for asset in ASSETS:
        filtred_tags = [
            tag for tag in soup.find_all(asset['tag_name'])
            if urlparse(tag.get(asset['attr_name'])).scheme == ''
        ]
        for tag in filtred_tags:
            resource_path = get_resource_path(
                resource_dir_path, tag.get(asset['attr_name']),
            )
            tag[asset['attr_name']] = resource_path 
    return soup.prettify()
