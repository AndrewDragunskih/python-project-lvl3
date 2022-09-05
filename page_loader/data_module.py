from urllib.parse import urlparse
from page_loader.paths_module import get_resource_path, get_resource_dir_path
from bs4 import BeautifulSoup
import os.path


def get_tags_list(response_text, url):
    ASSETS = [
        {'tag_name': 'img', 'attr_name': 'src'},
        {'tag_name': 'link', 'attr_name': 'href'},
        {'tag_name': 'script', 'attr_name': 'src'},
    ]
    soup = BeautifulSoup(response_text, "html.parser")
    all_tags = []
    for asset in ASSETS:
        all_tags.extend([
            tag for tag in soup.find_all(asset['tag_name'])
            if urlparse(tag.get(asset['attr_name'])).scheme == '' or
            urlparse(tag.get(asset['attr_name'])).netloc == urlparse(url).netloc
        ])
    return all_tags


def get_attr_name_from_tag(tag):
    if tag.get('src') is not None:
        return 'src'
    if tag.get('href') is not None:
        return 'href'


def process_resources_paths(response_text, output_dir, url):
    soup = BeautifulSoup(response_text, "html.parser")
    resource_dir_path = get_resource_dir_path(output_dir, url)
    all_tags = get_tags_list(response_text, url)
    for tag in all_tags:
        resource_path = get_resource_path(
            resource_dir_path, url, tag[get_attr_name_from_tag(tag)],
        )
        tag_name = tag.name
        tag_to_change = soup.find(
            tag_name,
            {get_attr_name_from_tag(tag): tag[get_attr_name_from_tag(tag)]},
        )
        print(resource_path)
        tag_to_change[get_attr_name_from_tag(tag)] = os.path.relpath(
            resource_path,
            output_dir,
        )
    return soup.prettify()
