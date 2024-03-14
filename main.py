from xmlrpc.client import DateTime
from telethon.sync import TelegramClient
from telethon import TelegramClient
import re
import asyncio
import aiogram
from aiogram.types import InputFile
from aiogram import Bot, types

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
# from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telethon import types
# from telethon.tl.custom.button  import  InlineKeyboardButton, InlineKeyboardMarkup
# from types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon.tl.types import DocumentAttributeVideo
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
  
ktxt= "**Не упусти возможность!** 🔥\nВ [привате](t.me/Osmotr_bot_bot?start=dGFyaWZfNDU5NTEx) доступны **полные видео**,\nкоторые стоит увидеть! 😍\n\nВход всего за **1000 рублей, и это навсегда!** \n\n🎉 **Более 6800 скрытых видео из мужских душевых, туалетов, раздевалок, уже ждут тебя! **👀\n\n✅ **Обновления каждый день**, чтобы тебе никогда не было скучно! 🔄\n\n▶️ Чтобы приобрести доступ, **[жми сюда](t.me/Osmotr_bot_bot?start=dGFyaWZfNDU5NTEx)**" 

# bot = Bot(token='6208274643:AAGaFq8OkYzimh9JlGL_Yke7XFD2B0Lg3QU')
# dp = Dispatcher(bot)



my_channel_id = -1001750094401
channels = ["me"]

# client = TelegramClient('myGrab', api_id, api_hash)
# print("GRAB - Started")


# @client.on(events.NewMessage(chats=channels))
# async def my_event_handler(event):

#     if event.message.video:
#         client.send_file(my_channel_id, file=event.message, caption="Самое жесткое гей порно тут👇🏻 \n[💎GPORN💎](https://t.me/gayplaygay)")


api_id = 20228113
api_hash = 'bd87a2a83030ed4aadb1fa28815130fa'

# Создайте или укажите StringSession, чтобы сохранить сессию авторизации
session_name = "myGrab"  # Если у вас уже есть StringSession, вставьте его сюда
client = TelegramClient(session_name, api_id, api_hash, system_version="14.16.31-xc")
 

client.start()

chats = []
last_date = None
chunk_size = 300
groups = []

result = client(GetDialogsRequest(
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

print('Выберете группу для парсинга сообщений и членов группы:')
i = 0
for g in groups:
    
    if g.title == "ГАРАНТИЯ":
        print(str(i) + '-                 ' + g.title)
        i += 1
        continue
        
    print(str(i) + '- ' + g.title)
    i += 1

g_index = input("Введите нужную цифру: ")
target_group = groups[int(g_index)]

i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i += 1

g_index = input("Введите нужную цифру куда будем публковать ")
for_group = groups[int(g_index)]

# link = input("Напиши название ссылки ")
# link1 = input("Отправь ссылку ")
# txt = (f"{input('Напиши текст ')}\n({link})[{link1}]")

# async def send_video(chat_id , video, txt, i, j):
#     # bot = Bot(token='6208274643:AAGaFq8OkYzimh9JlGL_Yke7XFD2B0Lg3QU')
    
#     # chat_id=f"100{chat_id}"
#     # chat_id= -int(chat_id)
#     # if i != "note":
        
#     #     bot.send_video(chat_id=chat_id, video= InputFile(video), caption=txt,duration=j.file.duration,  # Du
#     #                         #  j.file.duration, w=j.file.width, h= j.file.heightration of the video in seconds
#     #         width=j.file.width,  # Width of the video in pixels
#     #         height=j.file.height,  # Height of the video in pixels
#     #         supports_streaming=True,  # Whether the video supports streaming
#     #         thumb=InputFile(video),  # Thumbnail for the video
#     #           # ID of the message being replied to
#     #         allow_sending_without_reply=True )
        
#     else:
#          bot.send_video_note(chat_id, InputFile(video))
# txt = "[SLIV ONLYFANS MEN | SOM](https://t.me/+AaiVm8vt4n5lZGVl)"

# txt1 ="😈Приват тихого солдата! \n▶️Стоимость -500 руб. НАВСЕГДА!\n🥵💦💦💦Более 1000 видео,\nкак тихие солдатики дрочат в туалете, или спят с причендалами наружу)\n[ПРИВАТ](https://t.me/soldatprivatbot)"

# txt = "[МОЛОДНЯК](https://t.me/zonasnaboy)"

# txt1 = "😈[Приват спящих парней](https://t.me/privatsleepbot)!\n ▶️Стоимость -500 руб. НАВСЕГДА! 🥵💦💦💦\nБолее 9000 видео,\nкак спящих парней раздевают, \nтрогают и не только)\n[ПРИВАТ](https://t.me/privatsleepbot)"

# txt = input("text 1 ")

# txt1 =input("text 2 ")
txt ="**[СЛИВАЕМ НАТУРАЛОВ](https://t.me/+fdC2S4RO7A1hODRi)**\nзалетай к нам в приват @slivnature_bot\n\nЕЩЕ БОЛЬШЕ НАТУРАЛОВ:  **[ЖМИ](https://t.me/slivnature_bot)**"
txt1 ="[❤️ Самые **сочные** мальчики у нас в **ПРИВАТЕ** 🍌](t.me/Molode_bot?start=dGFyaWZfNDc2MDg1)\n\nСкорее в наш  **[приват!](t.me/Molode_bot?start=dGFyaWZfNDc2MDg1)**\n\nЗоходи и смотри первым\n[WebCam Privat](t.me/Molode_bot?start=dGFyaWZfNDc2MDg1)\n\n         **ПОДПИСЫВАЙСЯ **⬇️\n         👉 [WebCamPrivat](t.me/Molode_bot?start=dGFyaWZfNDc2MDg1)👈\n\n➡️ t.me/Molode_bot?start=dGFyaWZfNDc2MDg1 ⬅️"

# keyboard = InlineKeyboardMarkup(row_width=1)
# keyboard.add(
#     InlineKeyboardButton(text='Открыть BotFather🤖👨🏼', url='https://t.me/BotFather'),
#     InlineKeyboardButton("⬅ Назад", callback_data="project_type_back")
# )


# txt1 ="😈SLIV ONLYFANS MEN PRIVAT! \n▶️Стоимость -600 руб. НАВСЕГДА!\n🥵💦💦💦Более 1000 видео и фото,\nслитых с ONLYFANS)\n[ПРИВАТ](https://t.me/somprivat_bot)"
# for_group = groups[int(g_index)]
# class Dict(dict):
#     def __new__(cls, *args, **kwargs):
#         self = dict.__new__(cls, *args, **kwargs)
#         self.__dict__ = self
#         return self
ktxt= "**Не упусти возможность!** 🔥\nВ [привате](t.me/Osmotr_bot_bot?start=dGFyaWZfNDU5NTEx) доступны **полные видео**,\nкоторые стоит увидеть! 😍\n\nВход всего за **1000 рублей, и это навсегда!** \n\n🎉 **Более 6800 скрытых видео из мужских душевых, туалетов, раздевалок, уже ждут тебя! **👀\n\n✅ **Обновления каждый день**, чтобы тебе никогда не было скучно! 🔄\n\n▶️ Чтобы приобрести доступ, **[жми сюда](t.me/Osmotr_bot_bot?start=dGFyaWZfNDU5NTEx)**" 

ktxt= "**Не упусти возможность!** \n[🔥приваты|privats🔥](t.me/oplatabotbot) " 
# target_group = Dict(id = 1581979119)
# for_group = Dict(id =1989715503)
if target_group.noforwards == True:
# if target_group.id == 1989715503:
    


    gg = client.get_messages(target_group.id)
    i = 1

    # 188
    # video id 756
    g = 2
    l = 0
    while g <=gg.total:
            txt2 = txt
            if l == 5:
                 txt2 = txt1 
                 l=0   
            txt=""
            j =  client.get_messages(target_group.id, ids=i)
            o=j
            if o ==None:
                i = i+1
                continue
            if o.grouped_id != None:
                gpid = o.grouped_id

            # chat_id = target_group.id
                album = []
                result = ''
                while gpid == o.grouped_id:
                    message =  client.get_messages(target_group.id, ids=i)
                    if message == None:
                        break
            # Check if the message has an album
                    gpid = message.grouped_id
                    if message.media and isinstance(message.media, types.MessageMediaPhoto) and message.media.photo.sizes:
                    # Forward the message to your target group with a custom caption
                        i = i + 1
                        regex = r"sergio_open"
                        replacement = rf"sergei_open"
                        
                        if o.text !='' and result == '':
                                
                            resulttxt = re.sub(regex, replacement, o.text)
                        k = message.download_media()
                        album.append(k)
                        message = client.get_messages(target_group.id, ids=i)
                        if message == None:
                            break
                        gpid = message.grouped_id
                    elif message.media and message.video:
                        i = i + 1
                        regex = r"sergio_open"
                        replacement = rf"sergei_open"
                        result = ''
                        if o.text !='' and result == '':
                                
                            resulttxt = re.sub(regex, replacement, o.text)
                        k = message.download_media()
                        album.append(k)
                        message = client.get_messages(target_group.id, ids=i)
                        if message == None:
                            break
                        gpid = message.grouped_id
                    else:
                        i = i + 1
                async def send_album(group_id, file_paths, ktxt):
                        api_id = 20228113
                        api_hash = 'bd87a2a83030ed4aadb1fa28815130fa'

# Создайте или укажите StringSession, чтобы сохранить сессию авторизации
                        session_name = "myGrab11x"  # Если у вас уже есть StringSession, вставьте его сюда
                        clientx = TelegramClient(session_name, api_id, api_hash, system_version="14.16.31-xc")
                        clientx.start()
                        try:
                            # Get the group entity
                            entity = clientx.get_entity(-1001978707166)

                            # Send the media as an album
                            media = []
                            for file_path in file_paths:
                                if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
                                    media.append(clientx.upload_file(file_path, use_cache=True))
                                    os.remove(file_path)
                                elif file_path.lower().endswith(('.mp4', '.mkv', '.avi')):
                                    media.append(clientx.upload_file(file_path, use_cache=True, part_size_kb=5120, progress_callback=None))
                                    os.remove(file_path)
                                else:
                                    print(f"Unsupported file format: {file_path}")

                            clientx.send_file(entity, file=media, caption=resulttxt)

                            print("Album sent successfully!")
                        except Exception as e:
                            print(f"Error sending the album: {e}")
                send_album(for_group, album, resulttxt)
                    # client.forward_messages(for_group.id, message, target_group.id)
                time.sleep(8)
                i = i - 1
            j =   client.get_messages(target_group.id, ids=i)
            if o.grouped_id == None:
                try:
                    if j.media != None:
                        
                        # if j.file.size > 200000000:
                        #     i = i + 1
                        #     g = g+ 1
                        #     print("пропускаю слишком большой файл")
                            # continue 
                        print(f"приступаю к загрузки\nразмер файла ({(j.file.size ) / 8000000} mb) ")
                        k = j.download_media()
                        # txt = re.sub(r'@max_barzz(?!\d*_bot)', '@iconparablllle1', j.text)
                        # txt = re.sub(r'@maxbarz_bot', '@maxbraz_bot', txt)
                        # # txt = j.text.replace("incomparablllle1_bot", "iconparablllle")
                        # txt = txt.replace("instagram.com/vlad_fit1", " ")
                        # txt = txt.replace("twitter.com/incomparablllle", " ")
                        # txt = re.sub(r'\b((http|https)://[^\s]+|\S+\.com|\S+\.ru|\S+vlad_fit1)\b', '', txt2)
                        
                        
                        
                        
                        # try:
                        #     print(f"сохранил файл с id {i}\nПриступаю к отправки в телеграм" )



                            # from moviepy.editor import VideoFileClip

                            # # Открываем исходный видеофайл
                            # video = VideoFileClip(f"./{k}")

                            # # Уменьшаем размер видео в два раза
                            # # video_resized = video.resize((int(video.w/2), int(video.h/2)))

                            # # Сохраняем сжатое видео в формате mp4
                            # video.write_videofile(f"./{k}",bitrate='200k', codec='libx264')
                        try:
                            if j.video_note:
                                regex = r"(https?:\/\/\S+|t\.me\/[\w-]+)(?=\))"
                                replacement = rf"https://t.me/TXPRIVAT_BOT"
                                result = ''
                                if o.text !='' and result == '':
                                    
                                    resulttxt = re.sub(regex, replacement, o.text)
                                else:
                                    resulttxt = ''
                                client.send_file(for_group.id, f"./{k}", caption=txt)
                                # video_note = types.InputMediaFile(file=f"./{k}", duration=j.file.duration, w=j.file.width, h= j.file.height, supports_streaming=True)
                                # client(functions.messages.SendMediaRequest(
                                #     peer=for_group.id,
                                #     media=video_note,
                                #     random_id=client.get_random_id(),
                                #     reply_to_msg_id=None
                                # ))
                                i = i + 1
                                continue 
                            
                            

        # Do something with the thumbnail, e.g. save it to a file
                            # thumbnail_file_path = './thumbnail.jpg'
                            # try:
                            #     thumbnail_bytes = j.download_media(j.video.thumbs[1])
                            #     thumbnail = bytearray(thumbnail_bytes)
                            #     with open(thumbnail_file_path, 'wb') as f:
                            #         f.write(thumbnail)
                            # except IndexError:
                            #     print('No thumbnail found for video.')
                            # except Exception as e:
                            #     print('Error downloading thumbnail:', e)
                            # async def send_video(chat_id , video, txt, i):
                            if j.video and not j.video_note:
                                regex = r"(https?:\/\/\S+|t\.me\/[\w-]+)(?=\))"
                                replacement = rf"https://t.me/TXPRIVAT_BOT"
                                result = ''
                                if o.text !='' and result == '':
                                        
                                    resulttxt = re.sub(regex, replacement, o.text)
                                else:
                                    resulttxt = ''
                                client.send_file(for_group.id, f"./{k}", caption=resulttxt)
                                i = i + 1
                            if j.photo:
                                regex = r"(https?:\/\/\S+|t\.me\/[\w-]+)(?=\))"
                                replacement = rf"https://t.me/TXPRIVAT_BOT"
                                result = ''
                                if o.text !='' and result == '':
                                        
                                    resulttxt = re.sub(regex, replacement, o.text)
                                else:
                                    resulttxt = ''
                                i = i + 1
                                client.send_file(for_group.id, f"./{k}", caption=resulttxt)
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
                        i = i + 1
                        g = g+ 1
                    else:
                        i = i + 1
                        g = g+ 1
                        continue
                except:
                    i = i + 1
                    g = g+ 1
                    
                    continue
else:

    
    k =  client.get_messages(target_group.id)
    print (k.total)
    l = 0
    # i = 542
    g = 2
    i=1
    
    while g <=k.total:
        if i == 14:
             pass
        txt2 = txt
        if l == 3:
                txt2 = txt1
                l= 0
        j =  client.get_messages(target_group.id, ids=i)
        if j == None:
            i = i + 1
            g = g+ 2
            continue
        o = j
        a = {}
        hu = 0
        if o.grouped_id != None:
            gpid = o.grouped_id

            chat_id = target_group.id
            album = []
            result = ''
            while gpid == o.grouped_id:
                message =  client.get_messages(target_group.id, ids=i)
                if message == None:
                     break
        # Check if the message has an album
                gpid = message.grouped_id
                if message.media and isinstance(message.media, types.MessageMediaPhoto) and message.media.photo.sizes:
                # Forward the message to your target group with a custom caption
                    i = i + 1
                    regex = r"(https?:\/\/\S+|t\.me\/[\w-]+)(?=\))"
                    replacement = r" "
                    
                    if o.text !='' and result == '':
                            
                        result = re.sub(regex, replacement, o.text)
                        
                    album.append(message.media.photo)
                    message =  client.get_messages(target_group.id, ids=i)
                    if message == None:
                        break
                    gpid = message.grouped_id
                elif message.media and message.video:
                    i = i + 1
                    regex = r"(https?:\/\/\S+|t\.me\/[\w-]+)(?=\))"
                    replacement = r" "
                    result = ''
                    if o.text !='' and result == '':
                            
                        result = re.sub(regex, replacement, o.text)
                    album.append(message.file.media)
                    message =  client.get_messages(target_group.id, ids=i)
                    if message == None:
                        break
                    gpid = message.grouped_id
                else:
                    i = i + 1
            client.send_message(for_group.id, file=album, message=f"{result}\n{ktxt}")
            time.sleep(2)
            # client.send_message(1800185022, file=album, message="")
                # client.forward_messages(for_group.id, message, target_group.id)
            time.sleep(8)
            i = i - 1
        if j == None:
            i = i + 1
            g = g+ 1
            continue
            
        o = j
        if o.file != None:
            if o.video and o.grouped_id == None or o.photo and  o.grouped_id == None:
                
                    try:
                        regex = r"(https?:\/\/\S+|t\.me\/[\w-]+)(?=\))"
                        replacement = r" "
                        result = ''
                        if o.text !='':
                             
                            result = re.sub(regex, replacement, o.text)
                        client.send_file(for_group.id, file=o, caption=f"{result}\n{ktxt}")
                        # time.sleep(2)
                        # client.send_file(1800185022, file=o, caption=ktxt)
                        
                        # client.send_file(5308827264, file="./client.send_file(for_group.id, file=o, caption=txt2)", caption=txt2)
                        i = i + 1
                        g = g+ 1
                        l = l + 1
                        time.sleep(8)
                    except:
                        i = i + 1
                        g = g+ 1
                        continue
                    try:
                        print(f"текст: {o.text} ;;; id : {o.id} ") 
                    except:
                        pass
                
            
            
                # async def handler(event):

                #     # craft a new message and send
                #     client.send_message(
                #         for_group.id,
                #         file=o.event.messages, # event.messages is a List - meaning we're sending an album
            else:   #         message=event.original_update.message.message,  # get the caption message from the album
                i = i + 1
                g = g+ 1
                l = l + 1       # )
        else:
                    
                    i = i + 1
                    g = g+ 2
                    try:
                        print(f"текст: {o.text} ;;; id : {o.id} ") 
                    except:
                        pass  
