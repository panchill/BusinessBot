import requests
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

token = os.getenv('API')

headers = {
    'Authorization': f'OAuth {token}'
}
# Получаем информацию о файле, включая прямую ссылку на скачивание
def get_download_url(file_path):
    url = f'https://cloud-api.yandex.net/v1/disk/resources/download?path={file_path}'
    response = requests.get(url, headers=headers)
    data = response.json()
    return data.get('href')  # Прямая ссылка на скачивание файла
