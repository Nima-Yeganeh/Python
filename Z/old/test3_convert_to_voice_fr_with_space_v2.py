# pip install gTTS

from gtts import gTTS

def text_to_speech(text, output_file):
    try:
        # Create a gTTS object with the text and the language
        tts = gTTS(text, lang='fr', slow=True)

        # Save the speech as an MP3 file
        tts.save(output_file)

        print(f"Text converted to speech and saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
org_text_to_convert = "Je me sens fatigué aujourd'hui."
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
output_file = "C:/Users/Nimay/Downloads/output.mp3"
text_to_speech(text_to_convert_with_space, output_file)
