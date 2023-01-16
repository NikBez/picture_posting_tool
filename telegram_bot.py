import telegram
from dotenv import load_dotenv
import os

def main():

    load_dotenv()
    bot = telegram.Bot(token = os.getenv('TELEGRAM_BOT_TOKEN') )

    bot.send_message(text='Hi John!', chat_id='@production_marketplace')




if __name__ =="__main__":
    main()
