import time
import telegram
from dotenv import load_dotenv
import os
from random import shuffle
from utils import get_photos


def main():

    load_dotenv()
    photo_pathes = get_photos()
    gap = int(os.getenv("POST_GAP", default=14400))
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    while True:
        shuffle(photo_pathes)
        connected = False
        for pic_path in photo_pathes:
            try:
                with open(pic_path, 'rb') as pic:
                    bot.send_photo(chat_id=os.environ['TELEGRAM_CHAT_ID'], photo=pic)
                    connected = True
                time.sleep(gap)
            except telegram.error.NetworkError:
                if connected:
                    connected = False
                    continue
                else:
                    print("Connection error. Try to reconnect.. ")
                    time.sleep(10)

if __name__ == "__main__":
    main()