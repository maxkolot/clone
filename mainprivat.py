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
from telethon.tl.types import (
    KeyboardButton,
    ReplyKeyboardMarkup
    
)
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telethon import types
# from telethon.tl.custom.button  import  InlineKeyboardButton, InlineKeyboardMarkup
# from types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon.tl.types import DocumentAttributeVideo
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
  
ktxt= "**Не упусти возможность!** 🔥\nВ [привате](http://t.me/Poodglazel_bot?start=dGFyaWZfNDU5NTEx) доступны **полные видео**,\nкоторые стоит увидеть! 😍\n\nВход всего за **1000 рублей, и это навсегда!** \n\n🎉 **Более 6800 скрытых видео из мужских душевых, туалетов, раздевалок, уже ждут тебя! **👀\n\n✅ **Обновления каждый день**, чтобы тебе никогда не было скучно! 🔄\n\n▶️ Чтобы приобрести доступ, **[жми сюда](http://t.me/Poodglazel_bot?start=dGFyaWZfNDU5NTEx)**" 
bot = Bot(token='6208274643:AAGaFq8OkYzimh9JlGL_Yke7XFD2B0Lg3QU')
dp = Dispatcher(bot)



my_channel_id = -1001750094401
channels = ["me"]

# client = TelegramClient('myGrab', api_id, api_hash)
# print("GRAB - Started")


# @client.on(events.NewMessage(chats=channels))
# async def my_event_handler(event):

#     if event.message.video:
#         await client.send_file(my_channel_id, file=event.message, caption="Самое жесткое гей порно тут👇🏻 \n[💎GPORN💎](https://t.me/gayplaygay)")
api_id = 20228113
api_hash = 'bd87a2a83030ed4aadb1fa28815130fa'
session_name = "myGrab11"  # Если у вас уже есть StringSession, вставьте его сюда
client = TelegramClient(session_name, api_id, api_hash, system_version="14.16.31-xc")
 

client.start()







async def dowlalbum(title, ids, forr, client1, txt1):

    
     
    chats = []
    last_date = None
    chunk_size = 200
    groups = []

    result = await client1(GetDialogsRequest(
        offset_date=last_date, 
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
        ))

    chats.extend(result.chats)
    for chat in chats:
        try:
            # if chat.megagroup == False:
                groups.append(chat)
        except:
            continue

    for g in groups:
    
        if g.title == title:
            target_group = g
        if g.title == forr:
            for_group = g
    i=ids
    j =  await client.get_messages(target_group.id, ids=i)
    o=j
    if o.grouped_id != None:
            gpid = o.grouped_id

            # chat_id = target_group.id
            album = []
            result = ''
            while gpid == o.grouped_id:
                message = await  client1.get_messages(target_group.id, ids=i)
                if message == None:
                     break
        # Check if the message has an album
                gpid = message.grouped_id
                if message.media and isinstance(message.media, types.MessageMediaPhoto) and message.media.photo.sizes:
                # Forward the message to your target group with a custom caption
                    i = i + 1
                    regex = r"(https?:\/\/\S+|t\.me\/[\w-]+)(?=\))"
                    replacement = rf"{txt1}"
                    
                    if o.text !='' and result == '':
                            
                        resulttxt = re.sub(regex, replacement, o.text)
                    k = await message.download_media()
                    album.append(k)
                    message = await client1.get_messages(target_group.id, ids=i)
                    if message == None:
                        break
                    gpid = message.grouped_id
                elif message.media and message.video:
                    i = i + 1
                    regex = r"(https?:\/\/\S+|t\.me\/[\w-]+)(?=\))"
                    replacement = rf"{txt1}"
                    result = ''
                    if o.text !='' and result == '':
                            
                        resulttxt = re.sub(regex, replacement, o.text)
                    k = await message.download_media()
                    album.append(k)
                    message = await client1.get_messages(target_group.id, ids=i)
                    if message == None:
                        break
                    gpid = message.grouped_id
                else:
                    i = i + 1
            async def send_album(group_id, file_paths, resulttxt):
                
                    try:
                        # Get the group entity
                        entity = await client1.get_entity(group_id)

                        # Send the media as an album
                        media = []
                        for file_path in file_paths:
                            if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
                                media.append(await client1.upload_file(file_path, use_cache=True))
                            elif file_path.lower().endswith(('.mp4', '.mkv', '.avi')):
                                media.append(await client1.upload_file(file_path, use_cache=True, part_size_kb=5120, progress_callback=None))
                            else:
                                print(f"Unsupported file format: {file_path}")

                        await client.send_file(entity, file=media, caption=resulttxt)

                        print("Album sent successfully!")
                    except Exception as e:
                        print(f"Error sending the album: {e}")
            await send_album(forr, album, resulttxt)
                # client.forward_messages(for_group.id, message, target_group.id)
            time.sleep(8)
            i = i - 1
        
 
async def dowl(title, ids, forr, client1, txt, txt1):
    regex = r"(https?:\/\/\S+|t\.me\/[\w-]+)(?=\))"
    replacement = rf"{txt1}"
                    
                    
                            
    resulttxt = re.sub(regex, replacement, txt)
     
    chats = []
    last_date = None
    chunk_size = 200
    groups = []

    result = await client1(GetDialogsRequest(
        offset_date=last_date, 
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
        ))

    chats.extend(result.chats)
    for chat in chats:
        try:
            # if chat.megagroup == False:
                groups.append(chat)
        except:
            continue

    for g in groups:
    
        if g.title == title:
            target_group = g
        if g.title == forr:
            for_group = g

    if target_group.noforwards == True:
    # if target_group.id == 1989715503:
        


        
        i = ids

        # 188
        # video id 756
        g = 2
        
        
        j =   await client1.get_messages(target_group.id, ids=i)
        try:
            if j.media != None:
                
                print(f"приступаю к загрузки\nразмер файла ({(j.file.size ) / 8000000} mb) ")
                k = await j.download_media()
                
                try:
                    if j.video_note:
                    
                        await client1.send_file(for_group.id, f"./{k}", caption=resulttxt)
                        
                    if j.video and not j.video_note:
                        await client1.send_file(for_group.id, f"./{k}", caption=resulttxt )
                        
                    if j.photo:
                        i = i + 1
                        await client1.send_file(for_group.id, f"./{k}", caption=resulttxt )
                    logging.info("File sent successfully")
                    print(f"\nотправленно {k}")
                    
                except Exception as e:
                    logging.error(f"Error sending file: {e}")
                    print(f"\nне отправленно {k}")
                
                try:
                    os.remove(f"./{k}")
                    print(f"\n{k} удалено")
                except:
                    print(f"\n{k} не удалено")
                
            else:
                pass
        except:
            pass








































     
     


