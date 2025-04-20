import requests
import os
from download import download_image
from dotenv import load_dotenv


def fetch_spacex_last_launch(launch_id, folder_name):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    spacex_urls = response.json()['links']['flickr']['original']
    for number, url in enumerate(spacex_urls):
        file_path = os.path.join(folder_name, f"spacex_{number}.jpg")
        download_image(url, file_path)


def main(): 
    load_dotenv()
    folder = os.environ.get("FOLDER_NAME", "images")
    launch_id = os.environ.get("SPACEX_LAUNCH_ID", "latest")
    os.makedirs(folder, exist_ok=True)
    fetch_spacex_last_launch(launch_id, folder)


if __name__ == "__main__":
    main()