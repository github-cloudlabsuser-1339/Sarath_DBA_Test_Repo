from googletrans import Translator

def translate_to_telugu(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='te')
    return translated.text

if __name__ == "__main__":
    english_text = "Hello, how are you?"
    telugu_translation = translate_to_telugu(english_text)
    print(f"English: {english_text}")
    print(f"Telugu: {telugu_translation}")