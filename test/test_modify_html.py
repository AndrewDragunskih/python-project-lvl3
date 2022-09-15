from page_loader.data_module import process_page_data


def test_process_html():
    fixture_data_path = 'test/fixtures/test_modify_html.html'
    expected_data_path = 'test/fixtures/test_modify_html_result.html'
    with open(fixture_data_path, 'r') as read_file:
        fixture_data = read_file.read()
    all_tags, soup = process_page_data(
        fixture_data,
        '',
        'https://site.com/blog/about'
    )
    with open(expected_data_path, 'r') as read_file:
        expected_data = read_file.read()
    assert soup == expected_data


def test_process_html_localhost():
    fixture_data_path = 'test/fixtures/localhost-blog-about.html'
    expected_data_path = 'test/fixtures/localhost-blog-about_result.html'
    with open(fixture_data_path, 'r') as read_file:
        fixture_data = read_file.read()
    all_tags, soup = process_page_data(
        fixture_data,
        '',
        'https://localhost/blog/about'
    )
    with open(expected_data_path, 'r') as read_file:
        expected_data = read_file.read()
    assert soup == expected_data
