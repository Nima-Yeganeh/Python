


# python.exe -m pip install --upgrade pip
# pip install translate
# pip install python-telegram-bot

from translate import Translator
from gtts import gTTS
import asyncio
from telegram import Bot, InputFile
import os
import openai
import time
import datetime
import random

user_input = ""
bot_token = user_input
chat_id = '-1001979088139'
openai.api_key = ""

# Define the filenames for file1 and file2
file1_name = 'C:/Users/Nimay/nima_git/Python/Z/zsample.txt'
file2_name = 'C:/Users/Nimay/nima_git/Python/Z/done.txt'
# Read the contents of file2 into a set for efficient membership checking
with open(file2_name, 'r') as file2:
    lines_in_file2 = set(file2.read().splitlines())
# Open file1 in read mode
with open(file1_name, 'r') as file1:
    # Create a list to store lines that are not in file2
    lines_to_add = []
    # Check each line in file1
    for line in file1:
        lines_to_add = []
        if line.strip() not in lines_in_file2:
            # If the line is not in file2, add it to the list
            lines_to_add.append(line)
            # Print the lines that were added to file2
            for line in lines_to_add:
                print(line.strip())
                inputtext=line.strip()           
            print(inputtext)
            english_text = inputtext
            print('Started!')

            def generate_response(question):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                            {"role": "system", "content": "You are a chatbot"},
                            {"role": "user", "content": question},
                        ]
                )
                result = ''
                for choice in response.choices:
                    result += choice.message.content
                return(result)

            ztext = english_text
            prompt = "translate to french >> " + ztext
            print(prompt)
            story = generate_response(prompt)
            print(story)
            # time.sleep(60)
            french_translation = story

            print(f"English: {english_text}")
            print(f"French: {french_translation}")

            def text_to_speech(text, output_file):
                try:
                    tts = gTTS(text, lang='en')
                    tts.save(output_file)
                    print(f"Text converted to speech and saved as {output_file}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            def text_to_speech_fr_slow(text, output_file):
                try:
                    tts = gTTS(text, lang='fr', slow=True)
                    tts.save(output_file)
                    print(f"Text converted to speech and saved as {output_file}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            def text_to_speech_fr(text, output_file):
                try:
                    tts = gTTS(text, lang='fr')
                    tts.save(output_file)
                    print(f"Text converted to speech and saved as {output_file}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            text_to_convert = english_text
            output_file = "C:\\Users\\Nimay\\Downloads\\audio_en.mp3"
            text_to_speech(text_to_convert, output_file)

            org_text_to_convert = french_translation
            words = org_text_to_convert.split()
            text_to_convert = " ".join([word + " " + word for word in words])
            text_to_convert = text_to_convert + " " + org_text_to_convert + " " + org_text_to_convert
            print(text_to_convert)
            space_syntax = '        ................        '
            text_to_convert_with_space = text_to_convert.replace('.', '')
            text_to_convert_with_space = text_to_convert_with_space.replace('?', '')
            text_to_convert_with_space = text_to_convert_with_space.replace('!', '')
            text_to_convert_with_space = text_to_convert_with_space.replace('  ', ' ')
            text_to_convert_with_space = text_to_convert_with_space.replace(' ', space_syntax)
            text_to_convert_with_space = space_syntax + text_to_convert_with_space + space_syntax
            print(text_to_convert_with_space)
            output_file = "C:\\Users\\Nimay\\Downloads\\audio_fr_slow.mp3"
            text_to_speech_fr_slow(text_to_convert_with_space, output_file)

            text_to_convert = french_translation
            output_file = "C:\\Users\\Nimay\\Downloads\\audio_fr.mp3"
            text_to_speech_fr(text_to_convert, output_file)

            bot = Bot(token=bot_token)
            mp3_path = 'C:\\Users\\Nimay\\Downloads\\audio_en.mp3'
            caption = " 🇺🇸  🇺🇸  🇺🇸  🇺🇸 " + english_text + " 🔹 👉 🇫🇷 " + french_translation + " 😊 ✅🌹"
            async def send_telegram_audio():
                with open(mp3_path, 'rb') as audio_file:
                    await bot.send_audio(chat_id=chat_id, audio=InputFile(audio_file), caption=caption)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(send_telegram_audio())

            bot = Bot(token=bot_token)
            mp3_path = 'C:\\Users\\Nimay\\Downloads\\audio_fr_slow.mp3'
            text_to_convert_without_space = text_to_convert_with_space
            text_to_convert_without_space = text_to_convert_without_space.replace('..', ' ')
            text_to_convert_without_space = text_to_convert_without_space.replace('        ', ' ')
            print(text_to_convert_without_space)
            caption = " 🇫🇷  🇫🇷  🇫🇷  🇫🇷 " + text_to_convert_without_space + " 🔹 👉 🇺🇸 " + english_text + " 😊 ✅🌹"
            async def send_telegram_audio():
                with open(mp3_path, 'rb') as audio_file:
                    await bot.send_audio(chat_id=chat_id, audio=InputFile(audio_file), caption=caption)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(send_telegram_audio())

            bot = Bot(token=bot_token)
            mp3_path = 'C:\\Users\\Nimay\\Downloads\\audio_fr.mp3'
            caption = " 🇫🇷  🇫🇷  🇫🇷  🇫🇷 " + french_translation + " 🔹 👉 🇺🇸 " + english_text + " 😊 ✅🌹"
            async def send_telegram_audio():
                with open(mp3_path, 'rb') as audio_file:
                    await bot.send_audio(chat_id=chat_id, audio=InputFile(audio_file), caption=caption)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(send_telegram_audio())

            print('Done!')

            # Open file2 in append mode and write the lines that are not in file2
            with open(file2_name, 'a') as file2:
                file2.writelines(lines_to_add)
            print("Process completed.")
 
            time.sleep(30)

