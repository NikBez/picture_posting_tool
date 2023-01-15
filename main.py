import requests
from pathlib import Path

def main():
    picture_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'


def save_image_by_link(link, path):

    pict = requests.get(link)
    pict.raise_for_status()

    Path(path).mkdir(parents=True, exist_ok=True)

    with open("images/habl.jpg", "wb") as picture:
        picture.write(pict.content)


if __name__ == "__main__":
    main()