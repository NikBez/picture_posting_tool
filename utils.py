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
        extension = get_image_extension(link)
        with open(os.path.join(save_path, f"space-{index}{extension}"), "wb") as pic_file:
            pic_file.write(picture)


def get_image_extension(image_link):

    path_from_url = parse.urlparse(image_link).path
    return os.path.splitext(path_from_url)[1]


def get_photos():

    images_root_path = os.getenv("IMAGES_ROOT_PATH", default=Path.cwd() / "images/")

    allowed_extensions = ('.jpg', '.png', '.jpeg')
    photo_pathes = []

    for root, dirs, files in os.walk(images_root_path, topdown=False):
        for name in files:
            file_name, ext = os.path.splitext(name)
            if ext in allowed_extensions:
                photo_pathes.append(os.path.join(root, name))

    shuffle(photo_pathes)
    return photo_pathes