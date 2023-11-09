from telethon import TelegramClient, events
import asyncio
import time
from random import randint
# from may import top, mid, btm
from telethon import TelegramClient, events
import asyncio
import time
from random import randint
import re 
from xmlrpc.client import DateTime
from telethon.sync import TelegramClient
from telethon import TelegramClient
import re
import asyncio
from xmlrpc.client import DateTime
from telethon.sync import TelegramClient
from telethon import TelegramClient
import re
import asyncio
import aiogram
from aiogram.types import InputFile
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from telethon.sync import TelegramClient
# from telethon.errors import PeerIdInvalid
from telethon.tl.types import InputPeerChat
from mainprivat import dowl, dowlalbum
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
import csv
from telethon import TelegramClient, types, functions
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import SendMediaRequest
import os
import logging
import time
from telethon import TelegramClient, events, functions, types
from telethon.sessions import StringSession
from telethon import TelegramClient
from telethon import TelegramClient, utils
from telethon.sessions import StringSession
from telethon.tl.types import (
    KeyboardButton,
    ReplyKeyboardMarkup
    
)
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telethon import types

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
import csv
from telethon import TelegramClient, types, functions
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import SendMediaRequest
import os
import logging
import time
from telethon import TelegramClient, events, functions, types
from telethon.sessions import StringSession
from telethon import TelegramClient

api_id = 20228113
api_hash = 'bd87a2a83030ed4aadb1fa28815130fa'



my_channel_id2=  -1001610804922
my_channel_id=  -1001642708881

mywb= -1001833446046
mynail = -1001745438393

wb = [ 
    -1001624439608, -1001598223666, -1001264267064,  -1001649817752,-1001381733485,-1001393882324,-1001445592509 
    ]
nails= [
     -1001112698907, -1001601965286, -1001403036444, -1001436326580,-1001401438652,-1001241322534
]

boys = [ -1001089863980, -1001866390155, -1001614194945, "me", -1001351007798]
cum_boys = [-1001175187472, -1001328878797, -1001294746933, -1001275320422]

zonas = [-1001528192112]

#channels = ["me"]
channels = [ -1001782993502, -1001436042866, -1001337926477, -1001192438957, 'me']

# wb = [ 
     
#     ]
# nails= [
     
# ]

# boys = [ ]
# cum_boys = []


#channels = ["me"]
# channels = [ ]

session_name = "myGrab2priva"  # Если у вас уже есть StringSession, вставьте его сюда
client = TelegramClient(session_name, api_id, api_hash, system_version="14.16.31-xc")

print("GRAB - Started")
smsboys = "🔥[HOT BOYS](https://t.me/+Bl53stl1qbtkZWQ0)🔥\n\nGPORN: [CLICK](https://t.me/+jO-g593nsXE1Njc0)🌈\nPRIVAT: [CLICK](t.me/Xgpor_prbot?start=dGFyaWZfNDQxMzYx)🍆💦💦\nGAY CHAT: [SP*RM](https://t.me/+TiYEE9l_6LQ5NTlk)🗣️\n\nПРЕДЛОЖКА: [BOT](https://t.me/g_pornbot)\nВЗАИМНЫЙ ПИАР: [CLICK](https://t.me/admi_list)"
smsgporn = "💎[GPORN](https://t.me/+jO-g593nsXE1Njc0)💎\n\nHOT BOYS: [CLICK](https://t.me/+Bl53stl1qbtkZWQ0)🔥\n\n\n⬇️ПРИВАТ|PRIVAT⬇️\n 🇷🇺RUB - [BOT](t.me/Xgpor_prbot?start=dGFyaWZfNDQxMzYx)\n 🇺🇦UAH - [BOT](http://t.me/Xgpor_prbot?start=dGFyaWZfNDQxMzY4)\n 💵USD - [BOT](http://t.me/Xgpor_prbot?start=dGFyaWZfNDQxMzc1)\nGAY CHAT: [SP*RM](https://t.me/+TiYEE9l_6LQ5NTlk)🗣️\n\nПРЕДЛОЖКА: [BOT](https://t.me/g_pornbot)\nВЗАИМНЫЙ ПИАР: [CLICK](https://t.me/admi_list)"
cum_boystxt = "💦[GUYS CUMS](https://t.me/guys_cums)💦\n\nGPORN: [CLICK](https://t.me/+jO-g593nsXE1Njc0)🌈\nPRIVAT: [CLICK](https://t.me/G_pornprivatbot)🍆💦💦\nGAY CHAT: [SP*RM](https://t.me/+TiYEE9l_6LQ5NTlk)🗣️\n\nПРЕДЛОЖКА: [BOT](https://t.me/g_pornbot)\nВЗАИМНЫЙ ПИАР: [CLICK](https://t.me/admi_list)"
zonasl = "[СПЯЩИЕ ПАРНИ](https://t.me/+R4o9babv-spmMTNi)\n\n[PRIVAT СПЯЩИХ - 50%](t.me/Xgpor_prbot?start=dGFyaWZfNDQxMzYz)"

zonasl1 ="[😈Приват спящих парней!](https://t.me/PRIVATsleepbot) \n▶️Стоимость -500 руб. НАВСЕГДА!\n🥵💦💦💦Более 1000 видео,\nкак спящих парней раздевают, трогают и не только)\n[ПРИВАТ](https://t.me/PRIVATsleepbot)"
soldat = [-1001503743792,-1001535200998]
icon = [-1001255427314]

#________________GUYS CUMS_______________

@client.on(events.Album(chats=-1001989715503))
async def handler(event):
        group_id = -1001777227314
        entity = await client.get_entity(group_id)  
        group_name = utils.get_display_name(entity)
        group_id2 = -1001923891046
        entity2 = await client.get_entity(group_id2)  
        group_name2 = utils.get_display_name(entity2)
        
        
        await  dowlalbum(title=group_name, ids=event._message_id, forr=group_name2, client1=client, txt1="t.me/hhdsisk")

@client.on(events.NewMessage(chats=-1001989715503))
async def my_event_handler(event):

    if event.message.video and event.message.grouped_id == None or event.message.photo and event.message.grouped_id == None:
        group_id = -1001777227314
        entity = await client.get_entity(group_id)  
        group_name = utils.get_display_name(entity)
        group_id2 = -1001923891046
        entity2 = await client.get_entity(group_id2)  
        group_name2 = utils.get_display_name(entity2)
        
        await  dowl(title=group_name, ids=event._message_id, forr=group_name2, client1=client, txt=event.message.text, txt1="t.me/hhdsisk")



    # if event.message.video and event.message.grouped_id == None:
    #     try:   
    #         await client.send_file(-1001923891046, file=k, caption=cum_boystxt)
    #     except:
    #         pass   
    # if event.message.photo and event.message.grouped_id == None:
    #     try:
    #         await client.send_file(-1001923891046, file=k, caption=cum_boystxt)
    #     except:
            # pass
sliz =[-1001181310313, "me"]
@client.on(events.Album(chats=sliz))
async def handler(event):
        
        try:
            regex = r"@slivnayakrysask"
            replacement = r"[@sliz'fm](t.me/slizperexod)"
            result = ''
            if event.text !='' and result == '':
                    
                result = re.sub(regex, replacement, event.message.text)
            await client.send_message(
                 -1001768493648,
                file=event.messages,
                message =result
            )
            time.sleep(0.5)
        except:
            pass

@client.on(events.NewMessage(chats=sliz))
async def my_event_handler(event):
   
    try:
        regex = r"@slivnayakrysask"
        replacement = r"[@sliz'fm](t.me/slizperexod)"
        result = ''
        if event.message.text !='' and result == '':
                
            result = re.sub(regex, replacement, event.message.text)
        if event.message.video and event.message.grouped_id == None:
            await client.send_file( -1001768493648, file=event.message, caption=result)
        if event.message.photo and event.message.grouped_id == None:
            await client.send_file( -1001768493648, file=event.message, caption=result)
    except:
        pass


    

client.start()
client.run_until_disconnected()  