import os
import requests
from pathlib import Path
from urllib import parse


def save_image_by_link(links, save_path):

    Path(save_path).mkdir(parents=True, exist_ok=True)

    for index, link in enumerate(links, start=1):
        response = requests.get(link)
        response.raise_for_status()
        picture = response.content
        extention = get_image_extention(link)
        with open(f"{save_path}/space-{index}{extention}", "wb") as pic_file:
            pic_file.write(picture)


def get_image_extention(image_link):

    path_from_url = parse.urlparse(image_link).path
    return os.path.splitext(path_from_url)[1]
