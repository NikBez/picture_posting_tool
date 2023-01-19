import os
from random import shuffle

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
        with open(os.path.join(save_path, f"space-{index}{extention}"), "wb") as pic_file:
            pic_file.write(picture)


def get_image_extention(image_link):

    path_from_url = parse.urlparse(image_link).path
    return os.path.splitext(path_from_url)[1]


def get_photos():

    allowed_extentions = ('.jpg', '.png', '.jpeg')
    photo_pathes = []

    for root, dirs, files in os.walk(Path.cwd()/"images", topdown=False):
        for name in files:
            file_name, ext = os.path.splitext(name)
            if ext in allowed_extentions:
                photo_pathes.append(os.path.join(root, name))

    shuffle(photo_pathes)
    return photo_pathes