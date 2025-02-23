import requests
import os


def download_image(url, filename, params=None):
    os.makedirs(os.environ["FOLDER_NAME"], exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()
    file_path = os.path.join('images', filename)
    with open(file_path, 'wb') as file:
        file.write(response.content)

    