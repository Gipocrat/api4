import requests
import os


def download_image(url, filename, folder=os.environ.get("FOLDER_NAME", "images"), params=None):
    os.makedirs(folder, exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()
    file_path = os.path.join(folder, filename)
    with open(file_path, 'wb') as file:
        file.write(response.content)

    