import argparse
import os
import requests
from dotenv import load_dotenv
from utils import save_image_by_link
from pathlib import Path



def main():

    load_dotenv()
    images_root_path = os.getenv("IMAGES_ROOT_PATH", default=Path.cwd() / "images/")

    parser = argparse.ArgumentParser(
    description="Скрипт скачивает фотографии с последнего полета spaceX или с указанного по id полета")
    parser.add_argument('-i', '--id', default='latest', help="SpaceX flight ID")
    args = parser.parse_args()

    spacex_api_url = 'https://api.spacexdata.com/v5/launches/'

    response = requests.get(f"{spacex_api_url}{args.id}")
    response.raise_for_status()
    flight_pics = response.json()["links"]["flickr"]["original"]

    save_image_by_link(flight_pics, os.path.join(images_root_path, 'spaceX'))

if __name__ == "__main__":
    main()