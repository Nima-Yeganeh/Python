# pip install googletrans
# pip install googletrans==4.0.0-rc1
# python.exe -m pip install --upgrade pip
# pip install translate

from translate import Translator
from gtts import gTTS

def translate_english_to_french(text):
    try:
        # Create a Translator object and specify the source and target languages
        translator = Translator(to_lang="fr", from_lang="en")

        # Translate the text
        translation = translator.translate(text)

        # Return the translated text
        return translation
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Translation failed"

# Example usage
english_text = "The history of art focuses on objects made by humans for any number of spiritual, narrative, philosophical, symbolic, conceptual, documentary, decorative, and even functional and other purposes, but with a primary emphasis on its aesthetic visual form."
french_translation = translate_english_to_french(english_text)

print(f"English: {english_text}")
print(f"French: {french_translation}")

def text_to_speech(text, output_file):
    try:
        # Create a gTTS object with the text and the language
        tts = gTTS(text, lang='en')

        # Save the speech as an MP3 file
        tts.save(output_file)

        print(f"Text converted to speech and saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def text_to_speech_fr(text, output_file):
    try:
        # Create a gTTS object with the text and the language
        tts = gTTS(text, lang='fr')

        # Save the speech as an MP3 file
        tts.save(output_file)

        print(f"Text converted to speech and saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

text_to_convert = english_text
output_file = "C:\\Users\\Nimay\\Downloads\\output.mp3"
text_to_speech(text_to_convert, output_file)
text_to_convert = french_translation
output_file = "C:\\Users\\Nimay\\Downloads\\output_fr.mp3"
text_to_speech_fr(text_to_convert, output_file)
