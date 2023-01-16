import time
import telegram
from dotenv import load_dotenv
import os
from random import shuffle
from utils import get_photos

def main():

    load_dotenv()
    photo_pathes = get_photos()
    gap = int(os.getenv("POST_GAP"))
    bot = telegram.Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    while True:
        shuffle(photo_pathes)
        for pic_path in photo_pathes:
            bot.send_photo(chat_id=os.getenv('TELEGRAM_CHAT_ID'), photo=open(pic_path, 'rb'))
            time.sleep(gap)


if __name__ == "__main__":
    main()