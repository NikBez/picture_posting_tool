# Space picture downloader

Tool allows to download space photos from few souces using API

## Install
````
 pip3 install -r requirements.txt
````
## Settings
`POST_GAP` - gap between posts in infitity mode (in seconds)  
`TELEGRAM_CHAT_ID` - id of Telegram group to work with  
`TELEGRAM_BOT_TOKEN` - pass you Telegram bot token here

## How to run
This script will download photos with [epic.gsfc.nasa](https://epic.gsfc.nasa.gov/):
````
python3 fetch_epic_images.py
````

This script will download photos with [nasa.gov/apod/astropix](https://apod.nasa.gov/apod/astropix.html):
````
python3 fetch_nasa_images.py -d [YYYY-MM_DD]
````
default -today

This script will download photos with [SpaceX open API](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1):
````
python3 fetch_spacex_images.py -i [index_of_flight]
````
default - last flight

Run to post single image:
````
python3 single_post.py -p [path]
````
default is random image from /images/..

Run to activate infinity posting:
````
python3 infinity_posting.py
````

