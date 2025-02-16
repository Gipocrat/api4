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


def apod_image(nasa_token):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    params = {"api_key": nasa_token, 'count': 30}
    response = requests.get(nasa_url, params=params)
    nasa_images = response.json()
    response.raise_for_status()
    for nasa_image in nasa_images:
        if nasa_image.get('media_type') == 'image':
            nasa_link_image = nasa_image.get('hdurl') or nasa_image.get('url') 
        filename, extension = get_extension(nasa_link_image)
        download_image(nasa_link_image,f"{filename}{extension}")


def main(): 
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    apod_image(nasa_token)

    
if __name__ == "__main__":
    main()