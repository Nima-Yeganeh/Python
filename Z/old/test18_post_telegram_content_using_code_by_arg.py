# pip install python-telegram-bot
import asyncio
from telegram import Bot, InputFile
# import test10_my_encrypt_decrypt_module
import sys
import os

if len(sys.argv) > 2:

    bot_token = sys.argv[1]
    chat_id = '@'+sys.argv[2]

    bot = Bot(token=bot_token)

    photofile = 'zjpgfile.txt'
    photo_path = ''  

    with open(photofile, 'r') as file:
        content = file.readlines()
    if content:
        photo_path = content[0].strip()
        print(photo_path)
    else:
        print("File is empty.")

    captionfile = 'ztelcontentfile.txt'
    caption = ''

    with open(captionfile, 'r') as file:
        caption = file.read()
    # print(caption)

    async def send_telegram_photo():
        with open(photo_path, 'rb') as image_file:
            await bot.send_photo(chat_id=chat_id, photo=InputFile(image_file), caption=caption)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_telegram_photo())

    captionfile = 'zteltitlefile.txt'
    caption = ''

    with open(captionfile, 'r') as file:
        caption = file.read()
    # print(caption)

    mp3file = 'zmp3file.txt'
    mp3file_path = ''

    with open(mp3file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        mp3file_path = line.strip()
        if os.path.isfile(mp3file_path) and os.path.getsize(mp3file_path) > 0:
            print("File exists and has size greater than zero:", mp3file_path)
            async def send_telegram_audio():
                with open(mp3file_path, 'rb') as audio_file:
                    await bot.send_audio(chat_id=chat_id, audio=InputFile(audio_file), caption=caption)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(send_telegram_audio())
        else:
            print("File not found: ", mp3file_path)

    mp4file = 'zmp4file.txt'
    mp4file_path = ''

    with open(mp4file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        mp4file_path = line.strip()
        if os.path.isfile(mp4file_path) and os.path.getsize(mp4file_path) > 0:
            print("File exists and has size greater than zero:", mp4file_path)
            async def send_telegram_video():
                with open(mp4file_path, 'rb') as video_file:
                    await bot.send_video(chat_id=chat_id, video=InputFile(video_file), caption=caption)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(send_telegram_video())
        else:
            print("File not found: ", mp4file_path)

else:
    print("No input provided.")

