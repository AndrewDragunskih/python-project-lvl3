from urllib.parse import urlparse
from page_loader.paths_module import get_resource_path, get_resource_dir_path
from bs4 import BeautifulSoup
import os.path


def get_attr_name_from_tag(tag):
    if tag.name in ('img', 'script'):
        return 'src'
    if tag.name == 'link':
        return 'href'


def process_html(response, output_dir, url):
    resource_dir_path = get_resource_dir_path(output_dir, url)
    soup = BeautifulSoup(response, "html.parser")
    all_attr_values = []
    for tag in soup.find_all(['img', 'link', 'script']):
        attr_name = get_attr_name_from_tag(tag)
        attr_value = tag.get(attr_name)
        attr_scheme = urlparse(attr_value).scheme
        attr_netloc = urlparse(attr_value).netloc
        if (attr_scheme == '' or attr_netloc == urlparse(url).netloc):
            all_attr_values.append(attr_value)
            resource_path = get_resource_path(
                resource_dir_path, url, attr_value,
            )
            tag[attr_name] = os.path.relpath(
                resource_path,
                output_dir,
            )
    return all_attr_values, soup.prettify()
