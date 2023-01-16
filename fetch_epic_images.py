from datetime import datetime
import os
import requests
from dotenv import load_dotenv
from utils import save_image_by_link


default_images_path = "images/EPIC/"

def main():

    load_dotenv()

    nasa_api_token = os.environ['NASA_API_TOKEN']
    nasa_epic_url = os.environ["NASA_EPIC_DATA_URL"]
    nasa_epic_picture_url = os.environ["NASA_EPIC_PICTURE_URL"]

    pictures = []
    response = requests.get(nasa_epic_url, params={'api_key': nasa_api_token, })
    response.raise_for_status()
    for image_data in response.json():
        picture_name = image_data['image']
        picture_date = datetime.strptime(image_data['date'], "%Y-%m-%d %H:%M:%S")
        pictures.append(
            f"{nasa_epic_picture_url}{picture_date.year}/{picture_date.month:02d}/{picture_date.day:02d}/png/{picture_name}.png?api_token={nasa_api_token}")

    save_image_by_link(pictures, default_images_path)


if __name__ == "__main__":
    main()