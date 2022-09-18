from urllib.parse import urlparse
from page_loader.paths_module import get_resource_path, get_resource_dir_path
from bs4 import BeautifulSoup
import os.path


ASSETS = {
    'img': 'src',
    'link': 'href',
    'script': 'src',
}


def process_page_data(page_text_data, output_dir, url):
    resource_dir_path = get_resource_dir_path(output_dir, url)
    parced_page_text_data = BeautifulSoup(page_text_data, "html.parser")
    page_resources_data = []
    for tag in parced_page_text_data.find_all(ASSETS.keys()):
        tag_attribute_name = ASSETS[tag.name]
        tag_attribute_value = tag.get(tag_attribute_name)
        tag_attribute_value_scheme = urlparse(tag_attribute_value).scheme
        tag_attribute_value_netloc = urlparse(tag_attribute_value).netloc
        if (tag_attribute_value_scheme == ''
                or tag_attribute_value_netloc == urlparse(url).netloc):
            resource_path = get_resource_path(
                resource_dir_path, url, tag_attribute_value,
            )
            page_resources_data.append(
                {'value': tag_attribute_value, 'path': resource_path}
            )
            tag[tag_attribute_name] = os.path.relpath(
                resource_path,
                output_dir,
            )
    return page_resources_data, parced_page_text_data.prettify()
