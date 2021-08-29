from pyrogram import Client

from W2HMUSIC1 import config

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
run = client.run
