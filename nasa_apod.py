import requests
import os
from urllib.parse import unquote, urlparse
from download import download_image
from dotenv import load_dotenv


def get_extension(url):
    url_unquote = unquote(url)
    parsed_url = urlparse(url_unquote)
    path, fullname = os.path.split(parsed_url.path)
    filename, extension = os.path.splitext(fullname)
    return filename, extension


def get_apod_images(nasa_token, count, folder_name):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    params = {"api_key": nasa_token, 'count': count}
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    nasa_images = response.json()
    for nasa_image in nasa_images:
        if nasa_image.get('media_type') == 'image':
            nasa_link_image = nasa_image.get('hdurl') or nasa_image.get('url') 
        else:
            continue
        filename, extension = get_extension(nasa_link_image)
        file_path = os.path.join(folder_name, f"{filename}{extension}")
        download_image(nasa_link_image, file_path)


def main(): 
    load_dotenv()
    count = os.environ.get("NASA_COUNT_IMAGE", 10)
    nasa_token = os.environ.get("NASA_TOKEN", "DEMO_KEY")
    folder = os.environ.get("FOLDER_FOR_IMAGES", "images")
    os.makedirs(folder, exist_ok=True)
    get_apod_images(nasa_token, count, folder)

    
if __name__ == "__main__":
    main()