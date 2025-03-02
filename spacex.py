import requests
import os
from download import download_image
from dotenv import load_dotenv


def fetch_spacex_last_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    spacex_urls = response.json()['links']['flickr']['original']
    for number, url in enumerate(spacex_urls):
        download_image(url,f"spacex_{number}.jpg" )


def main(): 
    load_dotenv()
    launch_id=os.environ["LAUNCH_ID"]
    fetch_spacex_last_launch(launch_id)


if __name__ == "__main__":
    main()