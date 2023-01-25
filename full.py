from telethon import TelegramClient, events
import asyncio
import time
from random import randint
import re 


api_id = 4286228
api_hash = 'fd2063177e1adb516785fc59a890842f'


mywb= -1001833446046

wb = [ "me"]

client = TelegramClient('myGrab', api_id, api_hash,)
print("GRAB - Started")





@client.on(events.Album(chats=wb))
async def handler(event):
    
        

        
        text1 = re.sub(r't.me\S+', 't.me/tvoya_tochka\n',event.text)
        aaa = re.sub(r'@\S+', '[YOUR WB](https://t.me/tvoya_tochka)\n', text1)
        aaa = re.sub(r'[*]', '', aaa)


        await client.send_message(
          
            mywb,
            file=event.messages,
            message =f"[YOUR WB](https://t.me/tvoya_tochka)\n\n{aaa}\n\nКрутые ноготочки\n ⬇ ⬇ ⬇\n[YOUR NAILS](https://t.me/your_nails_u)"
        )
        time.sleep(0.5)

     

@client.on(events.NewMessage(chats=wb))
async def my_event_handler(event):
        
    

    


    
    text1 = re.sub(r't.me\S+', 't.me/tvoya_tochka\n',event.text)
    aaa = re.sub(r'@\S+', '[YOUR WB](https://t.me/tvoya_tochka)\n', text1)
    aaa = re.sub(r'[*]', '', aaa)

     
  
    if event.message.video and event.message.grouped_id == None:
        await client.send_file(mywb, file=event.message, caption=f"[YOUR WB](https://t.me/tvoya_tochka)\n\n{aaa}\n\nКрутые ноготочки\n ⬇ ⬇ ⬇\n[YOUR NAILS](https://t.me/your_nails_u)")
        
    if event.message.photo and event.message.grouped_id == None:
        await client.send_file(mywb, file=event.message, caption=f"[YOUR WB](https://t.me/tvoya_tochka)\n\n{aaa}\n\nКрутые ноготочки\n ⬇ ⬇ ⬇\n[YOUR NAILS](https://t.me/your_nails_u)")

    

client.start()
client.run_until_disconnected()  

        
