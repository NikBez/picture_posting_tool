import requests
from pathlib import Path

default_images_path = "images/"

def main():
    API_spaceX_patch = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    pictures = fetch_spacex_last_launch(API_spaceX_patch)
    save_image_by_link(pictures, default_images_path)


def save_image_by_link(link, save_path):

    Path(save_path).mkdir(parents=True, exist_ok=True)

    for index, pic_link in enumerate(fligth_picks, start=1):
        response = requests.get(pic_link)
        response.raise_for_status()
        picture = response.content
        with open(f"{save_path}/{index}.jpg", "wb") as pic_file:
            pic_file.write(picture)

def fetch_spacex_last_launch(API_patch):

    response = requests.get(API_patch)
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]

if __name__ == "__main__":
    main()