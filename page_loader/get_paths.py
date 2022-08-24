import os.path
import re


def url_to_name(url):
    url_parts = []
    url, resource_type = os.path.splitext(url)
    while url not in ['https:', 'http:', '/', '', '//']:
        url, tail = os.path.split(url)
        splitted_tail = re.split("_|\\W", tail)
        splitted_tail.reverse()
        url_parts.extend(splitted_tail)
    url_parts.reverse()
    return '-'.join(url_parts), resource_type


def get_html_file_path(output_dir, url):
    url, resource_type = url_to_name(url)
    return os.path.join(
        output_dir,
        '{}.html'.format(url),
    )


def get_resource_dir_path(output_dir, url):
    url, resource_type = url_to_name(url)
    return os.path.join(
        output_dir,
        '{}_files'.format(url),
    )


def get_resource_path(resource_dir_path, attr_name):
    image_name, resource_type = url_to_name(attr_name)
    return os.path.join(
        resource_dir_path,
        '{0}{1}'.format(image_name, resource_type),
    )
