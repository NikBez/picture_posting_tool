import argparse
import os
import requests
from dotenv import load_dotenv
from utils import save_image_by_link
from pathlib import Path

default_images_path = Path.cwd()/"images/NASA/"

def main():

    load_dotenv()

    parser = argparse.ArgumentParser(
    description="Скрипт скачивает Astronomy Picture of the Day from NASA ")
    parser.add_argument('-d', '--date', default='', help="Date of a picture in format YYYY-MM-DD")
    args = parser.parse_args()


    nasa_api_token = os.environ['NASA_API_TOKEN']
    nasa_api_url = os.getenv("NASA_API_URL", default='https://api.nasa.gov/planetary/apod/')


    api_params = {'api_key': nasa_api_token,
                  'date': args.date
                  }
    pictures = []
    response = requests.get(nasa_api_url, params=api_params)
    response.raise_for_status()
    pictures.append(response.json()['url'])

    save_image_by_link(pictures, default_images_path)


if __name__ == "__main__":
    main()