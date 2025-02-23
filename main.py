import os
import asyncio
import logging
import random
import string

from telethon import TelegramClient
from telethon.errors import FloodWaitError
from telethon.tl.types import (
    DocumentAttributeVideo,
    InputPeerEmpty
)
from telethon.tl.functions.messages import GetDialogsRequest, GetHistoryRequest

# ========== Настройки ==========
API_ID = 20228113
API_HASH = 'bd87a2a83030ed4aadb1fa28815130fa'
SESSION_NAME = "myGrab"

# Для старых версий Telethon (и само Telegram API) обычно лимит ~512 KB на чанк
PART_SIZE_KB = 512

logging.basicConfig(level=logging.INFO)


def random_filename(prefix="file_", ext=".dat") -> str:
    """
    Генерирует случайное имя файла, чтобы не было коллизий.
    """
    rnd = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{prefix}{rnd}{ext}"


async def select_group(client: TelegramClient, prompt: str = "Выберите группу"):
    """
    Показывает список доступных чатов/каналов (первые 300).
    Возвращает выбранный entity (чат/канал).
    """
    result = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=300,
        hash=0
    ))
    all_chats = result.chats

    print(f"\n{prompt}:")
    for idx, chat in enumerate(all_chats):
        title = getattr(chat, 'title', 'Без названия')
        print(f"{idx}) {title}")

    group_index = int(input("Введите индекс нужного чата/канала: "))
    target_entity = all_chats[group_index]
    print(f"Вы выбрали: {target_entity.title}\n")
    return target_entity


async def get_total_messages(client: TelegramClient, entity):
    """
    Возвращает общее количество сообщений в выбранном чате/канале.
    """
    history = await client(GetHistoryRequest(
        peer=entity,
        offset_id=0,
        offset_date=None,
        add_offset=0,
        limit=1,
        max_id=0,
        min_id=0,
        hash=0
    ))
    return history.count


async def iter_download_to_file(client: TelegramClient, message_or_media, out_file: str) -> bool:
    """
    Скачиваем message_or_media через iter_download (чанки ~512 KB),
    записываем на диск.
    Возвращает True, если что-то скачано (не пустое), иначе False.
    """
    size_downloaded = 0
    try:
        async with client.iter_download(message_or_media, chunk_size=512*1024, request_size=512*1024) as generator:
            with open(out_file, 'wb') as fd:
                async for chunk in generator:
                    if not chunk:
                        break
                    fd.write(chunk)
                    size_downloaded += len(chunk)
        return size_downloaded > 0
    except Exception as e:
        logging.error(f"Ошибка при iter_download_to_file: {e}")
        return False


async def reupload_video(client: TelegramClient, message):
    """
    Скачивает видео (iter_download_to_file) + скачивает миниатюру через
    download_media(thumb=-1), формирует dict для send_file(...).
    Это удобно для ОДИНОЧНОГО видео (с сохранением стриминга и превью).
    Для альбомов Telethon часто не применяет атрибуты к каждому видео.
    """
    doc = getattr(message.media, 'document', None)
    if not doc:
        return None

    # 1) Скачиваем само видео
    video_path = random_filename(prefix="video_", ext=".mp4")
    ok = await iter_download_to_file(client, message, video_path)
    if not ok:
        return None

    # 2) Ищем атрибуты (продолжительность, размеры)
    video_attribs = None
    if doc.attributes:
        for attr in doc.attributes:
            if isinstance(attr, DocumentAttributeVideo):
                video_attribs = attr
                break

    # 3) Скачиваем миниатюру thumb через download_media(..., thumb=-1)
    thumb_path = None
    if doc.thumbs:
        thumb_path = random_filename(prefix="thumb_", ext=".jpg")
        try:
            downloaded_path = await client.download_media(
                message=message,
                file=thumb_path,
                thumb=-1
            )
            if not downloaded_path:
                thumb_path = None
        except Exception as e:
            logging.error(f"Не удалось скачать миниатюру: {e}")
            if os.path.exists(thumb_path):
                os.remove(thumb_path)
            thumb_path = None

    # 4) Формируем параметры для send_file
    params = {
        'file': video_path,
        'force_document': False,  # отправляем как "видео"
        'video_note': False,
        'caption': '',
        'allow_cache': False,
        'part_size_kb': PART_SIZE_KB
    }

    if video_attribs:
        params['attributes'] = [
            DocumentAttributeVideo(
                duration=video_attribs.duration,
                w=video_attribs.w,
                h=video_attribs.h,
                supports_streaming=True
            )
        ]
    else:
        params['supports_streaming'] = True

    if thumb_path:
        params['thumb'] = thumb_path

    return params


async def send_album_as_uploads(entity, file_paths, caption=""):
    """
    Создаёт НОВОГО клиента (clientx), загружает фото/видео через upload_file(...)
    и отправляет всё одним списком, чтобы Telegram распознал как «альбом».
    Старой версией Telethon/Telegram могут быть ограничения (Media invalid).
    """

    # Можно использовать те же API_ID и API_HASH, но новую session.
    api_id = 20228113
    api_hash = 'bd87a2a83030ed4aadb1fa28815130fa'
    session_name = "myGrab_album_uploader"

    # Создаём временный клиент
    clientx = TelegramClient(session_name, api_id, api_hash)
    await clientx.start()

    try:
        # Получаем entity целевой группы/чата
        chat_entity = await clientx.get_entity(entity)

        media_to_send = []
        for path in file_paths:
            if not os.path.exists(path):
                continue
            # Определяем, фото или видео
            ext = os.path.splitext(path)[1].lower()
            if ext in (".jpg", ".jpeg", ".png"):
                # Загружаем фото
                f = await clientx.upload_file(path, use_cache=True, part_size_kb=512)
                media_to_send.append(f)
                os.remove(path)
            elif ext in (".mp4", ".mkv", ".avi"):
                # Загружаем видео (без атрибутов - в режиме альбома Telethon их не применит)
                f = await clientx.upload_file(path, use_cache=True, part_size_kb=512)
                media_to_send.append(f)
                os.remove(path)
            else:
                print(f"Unsupported file format: {path}")
                # Можно всё равно отправить как документ
                # f = await clientx.upload_file(path, use_cache=True, part_size_kb=512)
                # media_to_send.append(f)
                # os.remove(path)

        if media_to_send:
            await clientx.send_file(
                chat_entity,
                file=media_to_send,
                caption=caption
            )
            print("Album sent successfully!")
        else:
            print("No media to send as album.")
    finally:
        await clientx.disconnect()


async def main():
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        print("Клиент Telethon запущен!\n")

        # 1) Выбираем источник и приёмник
        source = await select_group(client, "Выберите группу (ИСТОЧНИК)")
        target = await select_group(client, "Выберите группу (ПРИЕМНИК)")

        total = await get_total_messages(client, source)
        print(f"Всего сообщений в источнике: {total}")

        # Начинаем с msg_id = 1 (или любой, который вам нужен)
        msg_id = 36

        while msg_id <= total:
            try:
                msg = await client.get_messages(source, ids=msg_id)
                if not msg:
                    msg_id += 1
                    continue

                # === Если это альбом (grouped_id) ===
                if msg.grouped_id:
                    grouped_id = msg.grouped_id
                    album_paths = []
                    album_caption = ""

                    while True:
                        sub_msg = await client.get_messages(source, ids=msg_id)
                        if not sub_msg or sub_msg.grouped_id != grouped_id:
                            break

                        # Пример замены текста (sergio_open -> sergei_open) - если хотите
                        if (not album_caption) and sub_msg.text:
                            album_caption = sub_msg.text.replace("sergio_open", "sergei_open")

                        if sub_msg.media:
                            # Проверим: фото или видео
                            if getattr(sub_msg, 'video', None) or hasattr(sub_msg.media, 'document'):
                                # Скачиваем видео-файл (без атрибутов для альбома, 
                                # т.к. Telethon всё равно не применит streaming отдельно)
                                temp_video = random_filename(prefix="album_video_", ext=".mp4")
                                ok = await iter_download_to_file(client, sub_msg, temp_video)
                                if ok:
                                    album_paths.append(temp_video)
                                else:
                                    if os.path.exists(temp_video):
                                        os.remove(temp_video)
                            else:
                                # Фото или другое
                                temp_photo = random_filename(prefix="album_photo_", ext=".jpg")
                                ok = await iter_download_to_file(client, sub_msg, temp_photo)
                                if ok:
                                    album_paths.append(temp_photo)
                                else:
                                    if os.path.exists(temp_photo):
                                        os.remove(temp_photo)

                        msg_id += 1
                        if msg_id > total:
                            break

                    # Отправляем альбом
                    if album_paths:
                        try:
                            # Вызываем вспомогательную функцию
                            await send_album_as_uploads(target, album_paths, caption=album_caption)
                        except Exception as e:
                            print(f"Ошибка при отправке альбома: {e}")

                    continue  # переходим к следующему сообщению

                # === Если одиночное медиа ===
                if msg.media:
                    # Проверим, видео ли это (чтобы сделать "reupload_video")
                    if getattr(msg, 'video', None) or hasattr(msg.media, 'document'):
                        params = await reupload_video(client, msg)
                        if params:
                            try:
                                await client.send_file(
                                    target,
                                    **params
                                )
                                print(f"Отправлено одиночное видео (ID={msg.id})")
                            except Exception as e:
                                print(f"Ошибка при отправке видео ID={msg.id}: {e}")

                            # Удаляем временные файлы (видео + thumb)
                            local_video = params['file']
                            if local_video and os.path.exists(local_video):
                                os.remove(local_video)
                            if 'thumb' in params and params['thumb']:
                                if os.path.exists(params['thumb']):
                                    os.remove(params['thumb'])
                        else:
                            print(f"Не удалось скачать видео (ID={msg.id}), пропускаем.")
                    else:
                        # Фото или другое медиа - скачиваем и отправляем
                        photo_path = random_filename("photo_", ".jpg")
                        ok = await iter_download_to_file(client, msg, photo_path)
                        if ok:
                            try:
                                await client.send_file(
                                    target,
                                    file=photo_path,
                                    caption='',  # или свой текст
                                    part_size_kb=PART_SIZE_KB
                                )
                                print(f"Отправлено фото/медиа (ID={msg.id})")
                            except Exception as e:
                                print(f"Ошибка при отправке (ID={msg.id}): {e}")
                            if os.path.exists(photo_path):
                                os.remove(photo_path)

                msg_id += 1

            except FloodWaitError as e:
                print(f"FloodWait: нужно подождать {e.seconds} сек (msg_id={msg_id})")
                await asyncio.sleep(e.seconds)
            except Exception as ex:
                print(f"Ошибка на сообщении {msg_id}: {ex}")
                msg_id += 1
                await asyncio.sleep(1)

        print("Парсинг и копирование завершены.")


if __name__ == "__main__": #1
    asyncio.run(main())


