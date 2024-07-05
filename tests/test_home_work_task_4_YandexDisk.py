import requests
import pytest
import os


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
    