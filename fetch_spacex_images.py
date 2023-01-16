import argparse
import os
import requests
from dotenv import load_dotenv
from utils import save_image_by_link

default_images_path = "images/spaceX/"

def main():

    load_dotenv()

    parser = argparse.ArgumentParser(
    description="Скрипт скачивает фотографии с последнего полета spaceX или с указанного по id полета")
    parser.add_argument('-i', '--id', default='latest', help="SpaceX flight ID")
    args = parser.parse_args()

    spacex_api_url = os.environ["SPACEX_API_URL"]

    response = requests.get(f"{spacex_api_url}{args.id}")
    response.raise_for_status()
    flight_pics = response.json()["links"]["flickr"]["original"]

    save_image_by_link(flight_pics, default_images_path)


if __name__ == "__main__":
    main()