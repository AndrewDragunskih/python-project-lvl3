from page_loader.data_module import process_resources_paths

FIXTURE_DATA_PATH = 'test/fixtures/test_modify_html.html'
EXPECTED_DATA_PATH = 'test/fixtures/test_modify_html_result.html'


def test_process_resources_paths():
    with open(FIXTURE_DATA_PATH, 'r') as read_file:
        fixture_data = read_file.read()
    soup = process_resources_paths(
        fixture_data,
        '',
        'https://site.com/blog/about'
    )
    with open(EXPECTED_DATA_PATH, 'r') as read_file:
        expected_data = read_file.read()
    print(soup)
    assert soup == expected_data
