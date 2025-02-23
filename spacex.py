import requests
from download import download_image


def fetch_spacex_last_launch():
    launch_id = input('Введите свою launch_id: ')
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    spacex_urls = response.json()['links']['flickr']['original']
    for number, url in enumerate(spacex_urls):
        download_image(url,f"spacex_{number}.jpg" )


def main(): 
    fetch_spacex_last_launch()


if __name__ == "__main__":
    main()