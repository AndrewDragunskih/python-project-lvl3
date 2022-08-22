import json
from page_loader.get_paths import get_resource_dir_path

FIXTURE_DATA_PATH = 'test/fixtures/test_get_resources_dir_path.json'
EXPECTED_DATA_PATH = 'test/fixtures/test_get_resources_dir_path_result'

def test_get_file_path():
    with open(FIXTURE_DATA_PATH, 'r') as read_file:
        fixture_data = json.load(read_file)
    with open(EXPECTED_DATA_PATH, 'r') as read_file:
        expected_data = read_file.read()
    expected_data = expected_data[:len(expected_data) - 1]
    result_data = []
    for output_dir, url in fixture_data.items():
        result_data.append(get_resource_dir_path(output_dir, url))
    result_data = '\n'.join(result_data)
    assert result_data == expected_data
