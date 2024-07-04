import requests
import pytest
from class_work_test_0 import summarize, get_info, multiply
from PhoneBook import PhoneBook
import os

@pytest.mark.parametrize(
        'a, b, expected',
        [
            (5, 7, 12),
            (-5, 8, 3),
            (5, -7, -2),
        ]
)
def test_summarise(a, b, expected):

    result = summarize(a, b)

    assert result == expected


@pytest.mark.skip(reason="Не реализован")
def test_summarize2():
    a = -5
    b = 8
    expeсted = 3

    result = summarize(a, b)

    assert expeсted == result

@pytest.mark.xfail
def test_summarize3():
    a = -5
    b = 8
    expeсted = 3

    result = summarize(a, b)

    assert expeсted == result


class TestPhoneBook:
    def setup_method(self):
        self.phone_book = PhoneBook()

    def teardown_method(self):
        self.phone_book

    def test_create_new_phone_book(self):
        assert len(self.phone_book.get_all_contacts()) == 0
    
    def test_create_phone_book(self):
        self.phone_book.add_contact('папа', 1234)
        self.phone_book.add_contact('мама', 12345)
        self.phone_book.add_contact('брат', 1234)
        self.phone_book.add_contact('сестра', 1545)

        assert len(self.phone_book.get_all_contacts()) == 3


class TestYandexDisk:
    
    def setup_method(self):
        file_path = os.path.join(os.path.dirname(__file__), 'token.txt')
        with open(file_path, 'r') as file:
            token = file.read().strip()
            self.headers = {
                'Authorization': f'OAuth {token}'
            }

    @pytest.mark.parametrize(
        'key, value, status_code',
        (
            ['pat', 'Image', 400],
            ['path', 'Image', 201],
            ['path', 'Image', 409],
        )
    )
    def test_create_folder(self, key, value, status_code):
        params = {key: value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', 
                                headers=self.headers, 
                                params=params)

        assert response.status_code == status_code

    @pytest.mark.parametrize(
        'path, status_code',
        (
            ['Image', 204],
            ['Image', 404]
        )
    )
    def test_delete_folder(self, path, status_code):
        params = {'path': path}
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources', 
                                headers=self.headers, 
                                params=params)

        assert response.status_code == status_code
    