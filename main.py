from datetime import datetime, timedelta
import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from urllib import parse

default_images_path = "images/"

def main():

    load_dotenv()

    nasa_api_token = os.environ['NASA_API_TOKEN']
    spacex_api_url = os.environ["SPACEX_API_URL"]
    nasa_api_url = os.environ["NASA_API_URL"]
    nasa_epic_url = os.environ["NASA_EPIC_DATA_URL"]
    nasa_epic_picture_url = os.environ["NASA_EPIC_PICTURE_URL"]

    pictures = []
    pictures += fetch_spacex_launches(spacex_api_url)
    pictures += fetch_nasa_pics(nasa_api_url, nasa_api_token)
    pictures += fetch_epic_pics(nasa_epic_url, nasa_epic_picture_url, nasa_api_token)

    save_image_by_link(pictures, default_images_path)


def save_image_by_link(links, save_path):

    Path(save_path).mkdir(parents=True, exist_ok=True)

    for index, link in enumerate(links, start=1):
        response = requests.get(link)
        response.raise_for_status()
        picture = response.content
        extention = get_image_extention(link)
        with open(f"{save_path}/space-{index}{extention}", "wb") as pic_file:
            pic_file.write(picture)

def fetch_spacex_launches(api_url):

    pictures = []
    response = requests.get(api_url)
    response.raise_for_status()

    flights = response.json()
    for flight in flights[:20]:
        flight_picks = flight["links"]["flickr"]["original"]
        pictures += flight_picks

    return pictures

def fetch_nasa_pics(api_url, nasa_api_token):

    pictures = []

    start_date = datetime.now() - timedelta(days=10)
    api_params = {'api_key': nasa_api_token,
                  'start_date': start_date.strftime("%Y-%m-%d")
                  }

    response = requests.get(api_url, params=api_params)
    response.raise_for_status()
    pictures_with_data = response.json()
    for picture in pictures_with_data:
        pictures.append(picture['url'])

    return pictures


def fetch_epic_pics(epic_data_url, epic_picture_url, nasa_api_token):

    pictures = []
    response = requests.get(epic_data_url, params={'api_key': nasa_api_token, })
    response.raise_for_status()
    for image_data in response.json():
        picture_name = image_data['image']
        picture_date = datetime.strptime(image_data['date'], "%Y-%m-%d %H:%M:%S")
        pictures.append(
            f"{epic_picture_url}{picture_date.year}/{picture_date.month:02d}/{picture_date.day:02d}/png/{picture_name}.png?api_token={nasa_api_token}")
    return pictures


def get_image_extention(image_link):

    path_from_url = parse.urlparse(image_link).path
    return os.path.splitext(path_from_url)[1]

if __name__ == "__main__":
    main()