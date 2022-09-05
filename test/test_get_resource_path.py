import json
from page_loader.paths_module import get_resource_path, get_resource_dir_path

FIXTURE_DATA_PATH = 'test/fixtures/test_get_image_path.json'
EXPECTED_DATA_PATH = 'test/fixtures/test_get_image_path_result'
OUTPUT_DIR = 'vat/'


def test_get_resource_path():
    with open(FIXTURE_DATA_PATH, 'r') as read_file:
        fixture_data = json.load(read_file)
    with open(EXPECTED_DATA_PATH, 'r') as read_file:
        expected_data = read_file.read()
    expected_data = expected_data[:len(expected_data) - 1]
    result_data = []
    for url, attr in fixture_data.items():
        result_data.append(
            get_resource_path(
                get_resource_dir_path(OUTPUT_DIR, url),
                url,
                attr
            )
        )
    result_data = '\n'.join(result_data)
    assert result_data == expected_data
