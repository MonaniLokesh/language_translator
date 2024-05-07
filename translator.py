import streamlit as st
from googletrans import Translator

# Function to translate English text to Hindi
def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, dest='hi')
    return translation.text

# Function to translate English text to French
def translate_to_french(text):
    translator = Translator()
    translation = translator.translate(text, dest='fr')
    return translation.text

# Function to translate English text to Spanish
def translate_to_spanish(text):
    translator = Translator()
    translation = translator.translate(text, dest='es')
    return translation.text

# Streamlit app
def main():
    st.title('Multilingual Translator')

    # Input text box for English text
    english_text = st.text_area('Enter English text to translate')

    if st.button('Translate'):
        if english_text:
            hindi_translation = translate_to_hindi(english_text)
            french_translation = translate_to_french(english_text)
            spanish_translation = translate_to_spanish(english_text)

            st.success(f'Hindi Translation: {hindi_translation}')
            st.success(f'French Translation: {french_translation}')
            st.success(f'Spanish Translation: {spanish_translation}')
        else:
            st.warning('Please enter some text to translate.')

if __name__ == '__main__':
    main()
