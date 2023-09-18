# pip install python-telegram-bot

import asyncio
from telegram import Bot, InputFile

# user_input = input("Enter a string: ")
user_input = ""
bot_token = user_input
chat_id = '-1001979088139'

bot = Bot(token=bot_token)

mp3_path = 'C:\\Users\\Nimay\\Downloads\\output_fr.mp3'
caption = 'Check out this amazing audio!'

async def send_telegram_audio():
    with open(mp3_path, 'rb') as audio_file:
        await bot.send_audio(chat_id=chat_id, audio=InputFile(audio_file), caption=caption)

loop = asyncio.get_event_loop()

loop.run_until_complete(send_telegram_audio())
