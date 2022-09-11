from urllib.parse import urlparse
from page_loader.paths_module import get_resource_path, get_resource_dir_path
from bs4 import BeautifulSoup
import os.path


def get_attr_name_from_tag(tag):
    if tag.get('src') is not None:
        return 'src'
    if tag.get('href') is not None:
        return 'href'


def get_tags_list(soup, url):
    all_tags = []
    for tag in soup.find_all(['img', 'link', 'script']):
        attr_name = get_attr_name_from_tag(tag)
        attr_value = tag.get(attr_name)
        attr_scheme = urlparse(attr_value).scheme
        attr_netloc = urlparse(attr_value).netloc
        if (attr_scheme == ''or attr_netloc == urlparse(url).netloc):
            all_tags.append(tag)
    return all_tags


def process_html(response, output_dir, url):
    soup = BeautifulSoup(response, "html.parser")
    all_tags = get_tags_list(soup, url)
    if all_tags != []:
        resource_dir_path = get_resource_dir_path(output_dir, url)
        for tag in all_tags:
            tag_name = tag.name
            tag_attr_name = get_attr_name_from_tag(tag)
            tag_attr_value = tag[tag_attr_name]
            resource_path = get_resource_path(
                resource_dir_path, url, tag_attr_value,
            )
            tag_to_change = soup.find(
                tag_name, {tag_attr_name: tag_attr_value},
            )
            tag_to_change[tag_attr_name] = os.path.relpath(
                resource_path,
                output_dir,
            )
    return all_tags, soup.prettify()
