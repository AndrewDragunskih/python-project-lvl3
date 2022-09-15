from urllib.parse import urlparse
from page_loader.paths_module import get_resource_dir_path
from page_loader.fs_module import save_data, make_dir
from page_loader.requests_module import get_page_content
from progress.bar import Bar


def format_resource_url(resource_url, url):
    if urlparse(resource_url).scheme == '':
        return '{0}://{1}{2}{3}'.format(
            urlparse(url).scheme,
            urlparse(url).netloc,
            '/' if resource_url[0] != '/' else '',
            resource_url,
        )
    return resource_url


def download_resources(page_resources_data, output_dir, url):
    resource_dir_path = get_resource_dir_path(output_dir, url)
    if not page_resources_data:
        return None
    make_dir(resource_dir_path)
    with Bar('Processing', max=len(page_resources_data)) as bar:
        for resouce_data in page_resources_data:
            resource_url = format_resource_url(resouce_data['value'], url)
            resource = get_page_content(resource_url)
            save_data(resouce_data['path'], resource, access_mode='wb')
            bar.next()
