import streamlit as st

# Morse Code Dictionary
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT.get(letter.upper(), '') + ' '
        else:
            cipher += ' '
    return cipher.strip()

def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            citext += letter
        else:
            if citext:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
            elif letter == ' ':
                decipher += ' '
    return decipher

def main():
    # Load and apply custom CSS
    with open('style.css') as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    # App title and introduction
    st.title('Morse Code Converter')

    option = st.selectbox(
        'Choose conversion type:',
        ['String to Morse Code', 'Morse Code to String']
    )

    input_text = st.text_area('Input Text:', '', height=200)

    if st.button('Convert'):
        if option == 'String to Morse Code':
            result = encrypt(input_text)
        elif option == 'Morse Code to String':
            result = decrypt(input_text)
        st.subheader('Result:')
        st.text(result)

if __name__ == '__main__':
    main()
