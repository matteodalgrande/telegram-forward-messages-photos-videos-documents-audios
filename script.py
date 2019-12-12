# python -m pip install configparser
# python -m pip install telethon
import configparser
import json

from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError

#per ottenere i membri del canale
import telethon.sync

from pprint import pprint

#Leggo il file config.ini
config = configparser.ConfigParser()
config.read("config.ini")

#Setto i valori di configurazione[che sono da inserire nel file config.ini]
api_id = config['Telegram']['api_id']
api_hash = str(config['Telegram']['api_hash'])
phone = config['Telegram']['phone']
username = config['Telegram']['username']

chat_id = int(config['Telegram']['chat_id'])
username_to_send = str(config['Telegram']['username_to_send'])

#Creazione di un client e connessione allo stesso
client = TelegramClient(username, api_id, api_hash)
@client.on(events.NewMessage)
async def my_event_handler(event):
    #pprint(dir(event))#dir serve per stampare l'oggetto con tutti parametri dell'evento
    if event.chat_id == chat_id:
        await client.send_message(username_to_send, event.message)

client.start()
#Questa riga serve per trovare l'id di una chat, tra virgolette si mette l'username
#pprint(dir(client.get_entity('Lucks123')))

client.run_until_disconnected()