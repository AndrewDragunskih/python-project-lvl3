import os.path
import re
from urllib.parse import urlparse


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


def get_resource_path(resource_dir_path, url, resource_url):
    resource_url_path = urlparse(resource_url).path
    resource_url_name, resource_url_type = url_to_name(resource_url_path)
    if resource_url_type == '':
        resource_url_type = '.html'
    netloc_name, netloc_type = url_to_name(urlparse(url).netloc)
    if netloc_type == '':
        resouce_name = '-'.join([
            netloc_name,
            '{0}{1}'.format(resource_url_name, resource_url_type)
        ])
    else:
        resouce_name = '-'.join([
            netloc_name,
            netloc_type[1:],
            '{0}{1}'.format(resource_url_name, resource_url_type)
        ])
    return os.path.join(resource_dir_path, resouce_name)
