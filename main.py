from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetMessagesViewsRequest
import asyncio
import time
import re 

api_id = 4286228
api_hash = 'fd2063177e1adb516785fc59a890842f'

my_channel_id = -1001750094401
channels = [-1001318162241, -1001447926604, -1001476226929, -1001255427314, -1001464284599, -1001417309568, "me"]

# client = TelegramClient('myGrab', api_id, api_hash)
# print("GRAB - Started")


# @client.on(events.NewMessage(chats=channels))
# async def my_event_handler(event):
   
#     if event.message.video:
#         await client.send_file(my_channel_id, file=event.message, caption="Самое жесткое гей порно тут👇🏻 \n[💎GPORN💎](https://t.me/gayplaygay)")


client = TelegramClient('session', api_id, api_hash)

@client.on(events.Album(chats="@probaprov"))
async def handler(event):

    # craft a new message and send
    await client.send_message(
        -1001833446046,
        file=event.messages, # event.messages is a List - meaning we're sending an album
        message=event.original_update.message.message,  # get the caption message from the album
    )


@client.on(events.NewMessage(chats="@your_nails_u"))
async def my_event_handler(event):
    print(event.message.message)
    gg = (event.message.message)
    ii = int(gg)
    k =  await client.get_messages(ii)
    yak = 0
    i = (k.total - 2000)
    # i = 2
    while i <=k.total:
        
        j =  await client.get_messages(ii, ids=i)
        o = j
        if o != None:
            if o.file != None :
                if o.video and o.grouped_id == None or o.photo and  o.grouped_id == None :

                    text1 = re.sub(r't.me\S+', 't.me/your_nails_u\n',o.text)
                    a = re.sub(r'@\S+', '[YOUR NAILS](https://t.me/your_nails_u)\n', text1)
                    
                    
                    await client.send_file(-1001745438393, file=o, caption=f"{a}\nПоделись с подругой☺️\n\nКрутая подборка товаров WB\n ⬇ ⬇ ⬇\n[Твоя находка🌺](https://t.me/tvoya_tochka)")
                    i = i + 1
                    time.sleep(1)
                    print(f"текст: {o.text} ;;; id : {o.id} ") 
                        
                        
                    
                if o.grouped_id != None:
                    # await client.send_message(-1001659081796,file  message=o, from_peer=o.chat_id )
                    i = i + 1
                    yak = 0

                    
                    continue
            else:
                        
                        i = i + 1
                        
                        print(f" id : {o.id} ")       
        else:
                        
                        i = i + 1
                        
                          
        

        

        


client.start()
client.run_until_disconnected()  
