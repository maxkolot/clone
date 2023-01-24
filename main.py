from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetMessagesViewsRequest
import asyncio

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


@client.on(events.NewMessage(chats="@probaprov"))
async def my_event_handler(event):
    print(event.text)
    # await client.send_file(-1001833446046, file=event.message, caption=f"{event.text}")
    # client.GetHistoryRequest
    next_post = client.iter_messages(
                entity= None,
                limit=100,
                min_id=2,
                reverse=True
            )
    i = 67
    
    # while i <= 28:
        
    k =  await client.get_messages(-1001659081796)
    g = 2
    while g <=k.total:
        
        j =  await client.get_messages(-1001659081796, ids=i)
        if j == None:
            continue
        o = j
        a = {}
        hu = 0
        if o.grouped_id != None:
            while hu < 4:
                
                j =  await client.get_messages(-1001659081796, ids=i)
                a[hu]=j.file
                hu=hu + 1
                
            await client.send_message(-1001833446046, file=a, message = f"*")
            i = i + 1
            g = g+ 2
            print(f"текст: {o.text} ;;; id : {o.id} ") 
        if j == None:
            continue
        o = j
        if o.file != None:
            if o.video and o.grouped_id == None or o.photo and  o.grouped_id == None:
                
                    await client.send_file(-1001833446046, file=o, caption=f"{o.text}")
                    i = i + 1
                    g = g+ 2
                    print(f"текст: {o.text} ;;; id : {o.id} ") 
                
            
            
                # async def handler(event):

                #     # craft a new message and send
                #     await client.send_message(
                #         -1001833446046,
                #         file=o.event.messages, # event.messages is a List - meaning we're sending an album
                #         message=event.original_update.message.message,  # get the caption message from the album
                    # )
        else:
                    
                    i = i + 1
                    g = g+ 2
                    print(f"текст: {o.text} ;;; id : {o.id} ")       
        

        

        


client.start()
client.run_until_disconnected()  
