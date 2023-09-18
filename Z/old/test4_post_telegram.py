# pip install python-telegram-bot

import asyncio
from telegram import Bot

# user_input = input("Enter a string: ")
user_input = ""
bot_token = user_input
chat_id = '-1001979088139'

bot = Bot(token=bot_token)

message = "Hello, Telegram!"

async def send_telegram_message():
    await bot.send_message(chat_id=chat_id, text=message)

loop = asyncio.get_event_loop()

loop.run_until_complete(send_telegram_message())
