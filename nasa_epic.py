import requests
import datetime
from download import download_image
from dotenv import load_dotenv
import os


def get_epic_image(nasa_token, count, folder_name):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {"api_key": nasa_token, 'count': count}
    response = requests.get(epic_url, params=params)
    response.raise_for_status()
    nasa_images = response.json()
    for epic_image in nasa_images:
        epic_name = epic_image['image']
        epic_date = epic_image['date']
        epic_date = datetime.datetime.fromisoformat(epic_date).strftime('%Y/%m/%d')
        epic_image_link = f'https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_name}.png'
        file_path = os.path.join(folder_name, f'{epic_name}.png')
        download_image(epic_image_link, file_path, params)


def main(): 
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    count = os.environ.get("NASA_COUNT_IMAGE", 10)
    folder = os.environ.get("FOLDER_NAME", "images")
    get_epic_image(nasa_token, count, folder)

    
if __name__ == "__main__":
    main()

