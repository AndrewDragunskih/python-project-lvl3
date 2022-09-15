from page_loader.requests_module import get_page_text
import pytest


class FakeResponse:
    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        if self.text == 'Right url':
            pass
        else:
            raise Exception

    def text(self):
        return self.text


class FakeClient:
    def get(self, url):
        if url == 'https://ru.hexlet.io/':
            fake_response = FakeResponse('Right url')
        else:
            fake_response = FakeResponse('Wrong url')
        return fake_response


def test_make_request_right_url():
    url = 'https://ru.hexlet.io/'
    fake_client = FakeClient()
    result = get_page_text(url, fake_client)
    expected_data = 'Right url'
    assert result == expected_data


def test_make_request_wrong_url():
    url = 'https://ru.hexlet.ru/'
    fake_client = FakeClient()
    with pytest.raises(Exception):
        get_page_text(url, fake_client)
