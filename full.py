from xmlrpc.client import DateTime
from telethon.sync import TelegramClient

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
import csv
import os
import time



api_id = 25391996
api_hash = '72c6c97b453c642f45dd885c71e1042e'

my_channel_id = -1001750094401
channels = ["me"]

# client = TelegramClient('myGrab', api_id, api_hash)
# print("GRAB - Started")


# @client.on(events.NewMessage(chats=channels))
# async def my_event_handler(event):

#     if event.message.video:
#         await client.send_file(my_channel_id, file=event.message, caption="Самое жесткое гей порно тут👇🏻 \n[💎GPORN💎](https://t.me/gayplaygay)")


client = TelegramClient('test_session', api_id, api_hash)


client.start()

chats = []
last_date = None
chunk_size = 200
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
    print(str(i) + '- ' + g.title)
    i += 1

g_index = input("Введите нужную цифру: ")
target_group = groups[int(g_index)]

i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i += 1

g_index = input("Введите нужную цифру куда будем публковать ")
# link = input("Напиши название ссылки ")
# link1 = input("Отправь ссылку ")
# txt = (f"{input('Напиши текст ')}\n({link})[{link1}]")

txt = "[СПЯЩИЕ ПАРНИ](https://t.me/+R4o9babv-spmMTNi)"

txt1 ="😈Приват спящих парней! \n▶️Стоимость -500 руб. НАВСЕГДА!\n🥵💦💦💦Более 1000 видео,\nкак спящих парней раздевают, трогают и не только)\n[ПРИВАТ](https://t.me/PRIVATsleepbot)"
for_group = groups[int(g_index)]
if target_group.noforwards == True:
    gg =   client.get_messages(target_group.id)
    i = 26
    g = 2
    l = 0
    while g <=gg.total:
            txt2 = txt
            if l == 5:
                 txt2 = txt1
                 l=0
                 
            j =   client.get_messages(target_group.id, ids=i)
            try:
                if j.media != None:
                    
                    k = j.download_media(file="./data")
                    
                    client.send_file(for_group.id, f"{k}", caption=txt2)
                    l = l+1
                    os.remove(f"{k}")
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
    i = 27
    g = 2
    k =  client.get_messages(target_group.id)
    print (k.total)
    l = 0
    while g <=k.total:
        txt2 = txt
        if l == 5:
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
            while hu < 4:
                
                j =  client.get_messages(target_group.id, ids=i)
                a[hu]=j.file
                hu=hu + 1
                
            try:
                client.send_message(for_group.id, file=a, message = txt2)
                i = i + 1
                g = g+ 2
                l = l+1
                time.sleep(2)
            except:
                i = i + 1
                g = g+ 2
                continue
            
            try:
                print(f"текст: {o.text} ;;; id : {o.id} ") 
            except:
                pass
        if j == None:
            continue
        o = j
        if o.file != None:
            if o.video and o.grouped_id == None or o.photo and  o.grouped_id == None:
                
                    try:
                        client.send_file(for_group.id, file=o, caption=txt2)
                        i = i + 1
                        g = g+ 2
                        l = l+1
                        time.sleep(2)
                    except:
                        i = i + 1
                        g = g+ 2
                        continue
                    try:
                        print(f"текст: {o.text} ;;; id : {o.id} ") 
                    except:
                        pass
                
            
            
                # async def handler(event):

                #     # craft a new message and send
                #     await client.send_message(
                #         for_group.id,
                #         file=o.event.messages, # event.messages is a List - meaning we're sending an album
                #         message=event.original_update.message.message,  # get the caption message from the album
                    # )
        else:
                    
                    i = i + 1
                    g = g+ 2
                    try:
                        print(f"текст: {o.text} ;;; id : {o.id} ") 
                    except:
                        pass  
