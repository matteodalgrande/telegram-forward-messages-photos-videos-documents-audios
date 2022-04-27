# python -m pip install configparser
# python -m pip install telethon
import configparser
import json

from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError

# to obtain channel's members
import telethon.sync

from pprint import pprint

# Read the config.ini file
config = configparser.ConfigParser()
config.read("config.ini")

# Set the configuration value [which are in config.ini]
api_id = config['Telegram']['api_id']
api_hash = str(config['Telegram']['api_hash'])
phone = config['Telegram']['phone']
username = config['Telegram']['username']

chat_id = int(config['Telegram']['chat_id'])
username_to_send = str(config['Telegram']['username_to_send'])

# Create a Client and connect to it
client = TelegramClient(username, api_id, api_hash)
@client.on(events.NewMessage)
async def my_event_handler(event):
    #pprint(dir(event))# dir  --> print the object whit all the parameters of the event
    if event.chat_id == chat_id:
        await client.send_message(username_to_send, event.message)

client.start()
# This line is useful to find out the id of a chat, in quotes you can put the username
#pprint(dir(client.get_entity('Lucks123')))

client.run_until_disconnected()