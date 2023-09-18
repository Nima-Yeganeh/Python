# pip install googletrans
# pip install googletrans==4.0.0-rc1
# python.exe -m pip install --upgrade pip
# pip install translate

from translate import Translator

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
english_text = "Hello. My name is Nima and I work in Berlin."
french_translation = translate_english_to_french(english_text)

print(f"English: {english_text}")
print(f"French: {french_translation}")
