from telethon import TelegramClient, events
import asyncio
import time
from random import randint
import re 


api_id = 4286228
api_hash = 'fd2063177e1adb516785fc59a890842f'


mywb= -1001833446046
mynail = -1001745438393

wb = [ 
    -1001624439608,
    -1001767158390,
    -1001453526584,
    -1001622636246,
    -1001765559949
    ]
nails= [
     -1001547526695, -1001403036444, -1001499470038, -1001143530935, -1001142275363, -1001073035721
]

client = TelegramClient('myGrab', api_id, api_hash,)
print("GRAB - Started")





@client.on(events.Album(chats=wb))
async def handler(event):
        text1 = re.sub(r't.me\S+', 't.me/tvoya_tochka\n',event.text)
        aaa = re.sub(r'@\S+', '[YOUR WB💕](https://t.me/tvoya_tochka)\n', text1)
        aaa = re.sub(r'[*]', '', aaa)

        await client.send_message(
            mywb,
            file=event.messages,
            message =f"[YOUR WB💕](https://t.me/tvoya_tochka)\n\n{aaa}\n\nКрутые ноготочки\n ⬇ ⬇ ⬇\n[YOUR NAILS](https://t.me/your_nails_u)"
        )
        time.sleep(0.5)

     

@client.on(events.NewMessage(chats=wb))
async def my_event_handler(event):
   
    text1 = re.sub(r't.me\S+', 't.me/tvoya_tochka\n',event.text)
    aaa = re.sub(r'@\S+', '[YOUR WB💕](https://t.me/tvoya_tochka)\n', text1)
    aaa = re.sub(r'[*]', '', aaa)

    if event.message.video and event.message.grouped_id == None:
        await client.send_file(mywb, file=event.message, caption=f"[YOUR WB💕](https://t.me/tvoya_tochka)\n\n{aaa}\n\nКрутые ноготочки\n ⬇ ⬇ ⬇\n[YOUR NAILS](https://t.me/your_nails_u)")
        
    if event.message.photo and event.message.grouped_id == None:
        await client.send_file(mywb, file=event.message, caption=f"[YOUR WB💕](https://t.me/tvoya_tochka)\n\n{aaa}\n\nКрутые ноготочки\n ⬇ ⬇ ⬇\n[YOUR NAILS](https://t.me/your_nails_u)")

@client.on(events.Album(chats=nails))
async def handler(event):
        text1 = re.sub(r't.me\S+', 't.me/tvoya_tochka\n',event.text)
        aaa = re.sub(r'@\S+', '[YOUR NAILS💕](https://t.me/your_nails_u)\n', text1)
        aaa = re.sub(r'[*]', '', aaa)

        await client.send_message(
            mynail,
            file=event.messages,
            message =f"[YOUR NAILS💕](https://t.me/your_nails_u)\n\n{aaa}\n\nПоделись с подругой☺️\n\nКрутая подборка товаров WB\n ⬇ ⬇ ⬇\n[YOUR WB](https://t.me/tvoya_tochka)"
        )
        time.sleep(0.5)

     

@client.on(events.NewMessage(chats=nails))
async def my_event_handler(event):
   
    text1 = re.sub(r't.me\S+', 't.me/tvoya_tochka\n',event.text)
    aaa = re.sub(r'@\S+', '[YOUR NAILS💕](https://t.me/your_nails_u)\n', text1)
    aaa = re.sub(r'[*]', '', aaa)

    if event.message.video and event.message.grouped_id == None:
        await client.send_file(mynail, file=event.message, caption=f"[YOUR NAILS💕](https://t.me/your_nails_u)\n\n{aaa}\n\nПоделись с подругой☺️\n\nКрутая подборка товаров WB\n ⬇ ⬇ ⬇\n[YOUR WB](https://t.me/tvoya_tochka)")
        
    if event.message.photo and event.message.grouped_id == None:
        await client.send_file(mynail, file=event.message, caption=f"[YOUR NAILS💕](https://t.me/your_nails_u)\n\n{aaa}\n\nПоделись с подругой☺️\n\nКрутая подборка товаров WB\n ⬇ ⬇ ⬇\n[YOUR WB](https://t.me/tvoya_tochka)")
    

client.start()
client.run_until_disconnected()  

        
