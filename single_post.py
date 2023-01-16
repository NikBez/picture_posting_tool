import telegram
from dotenv import load_dotenv
import os
import argparse
from random import choice
from utils import get_photos

def main():

    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Script publicate photo in Telegram group")
    parser.add_argument('-p', '--path', help="Path to photo")
    args = parser.parse_args()
    pic_path = args.path if args.path else choice(get_photos())

    bot = telegram.Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    bot.send_photo(chat_id=os.getenv('TELEGRAM_CHAT_ID'), photo=open(pic_path, 'rb'))

if __name__ == "__main__":
    main()
