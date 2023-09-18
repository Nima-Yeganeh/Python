# python.exe -m pip install --upgrade pip
# pip install translate
# pip install python-telegram-bot

from translate import Translator
from gtts import gTTS
import asyncio
from telegram import Bot, InputFile

user_input = ""
bot_token = user_input
chat_id = '-1001979088139'

english_text = "Hello. My name is Nima. How are you?"

print('Started!')

def translate_english_to_french(text):
    try:
        translator = Translator(to_lang="fr", from_lang="en")
        translation = translator.translate(text)
        return translation
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Translation failed"

french_translation = translate_english_to_french(english_text)

print(f"English: {english_text}")
print(f"French: {french_translation}")

def text_to_speech(text, output_file):
    try:
        tts = gTTS(text, lang='en')
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
text_to_convert = french_translation
output_file = "C:\\Users\\Nimay\\Downloads\\audio_fr.mp3"
text_to_speech_fr(text_to_convert, output_file)

bot = Bot(token=bot_token)
mp3_path = 'C:\\Users\\Nimay\\Downloads\\audio_en.mp3'
caption = "🔹😊 🇺🇸 " + english_text + " 👉 🇫🇷 " + french_translation + " ✅🌹"
async def send_telegram_audio():
    with open(mp3_path, 'rb') as audio_file:
        await bot.send_audio(chat_id=chat_id, audio=InputFile(audio_file), caption=caption)
loop = asyncio.get_event_loop()
loop.run_until_complete(send_telegram_audio())

bot = Bot(token=bot_token)
mp3_path = 'C:\\Users\\Nimay\\Downloads\\audio_fr.mp3'
caption = "🔹😊 🇫🇷 " + french_translation + " 👉 🇺🇸 " + english_text + " ✅🌹"
async def send_telegram_audio():
    with open(mp3_path, 'rb') as audio_file:
        await bot.send_audio(chat_id=chat_id, audio=InputFile(audio_file), caption=caption)
loop = asyncio.get_event_loop()
loop.run_until_complete(send_telegram_audio())

print('Done!')
