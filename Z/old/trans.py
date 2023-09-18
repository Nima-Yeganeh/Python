# pip install googletrans==4.0.0-rc1
# pip install --upgrade googletrans
# pip install --upgrade httpcore
# pip install pipdeptree

from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Input text in English
english_text = "Hello, how are you?"

# Detect the language (optional)
detected_language = translator.detect(english_text).lang

# Translate to French
translated_text = translator.translate(english_text, src=detected_language, dest='fr')

# Print the translation
print(f"English: {english_text}")
print(f"Detected Language: {LANGUAGES.get(detected_language).capitalize()}")
print(f"French: {translated_text.text}")
