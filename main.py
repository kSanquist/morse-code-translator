import morse_code as mc
import time

def main():
    program_details()
    mode = get_mode()
    if mode == '1':
        sentence = get_sentence()
    else:
        sentence = get_morse_code()
    handle_mode(mode, sentence)


# Pretty banner and version number
# TODO: Morse code -> English
def program_details():
    print("English -> Morse Code Translator")
    print("Version 2.0  by  Kyle Sanquist")
    print()
    print("*******************")
    print("* IMPORTANT NOTES *")
    print("************************************************************")
    print("* (1) DO NOT try to use special characters, it won't work  *")
    print("*     strictly numbers and letters only                    *")
    print("* (2) When translating from morse code to English seperate *")
    print("*     letters by spaces and words by / or |                *")
    print("*     EXAMPLE: .... . .-.. .-.. ---/.-- --- .-. .-.. -..   *")
    print("************************************************************")
    print()


# Asks user which way they want to translate
def get_mode():
    while True:
        print('Which way would you like to translate?')
        print(' (1) English -> Morse Code')
        print(' (2) Morse Code -> English\n')
        mode = input('enter #: ')

        if mode == '1' or mode == '2':
            return mode
        else:
            print('Your input is invalid, try again.\n')

            
# Gets sentence and makes sure there are no invalid characters
def get_sentence():
    invalid_chars = "~`!@#$%^&*()_+={}[]|\\"
    while True:
        invalid = False
        sentence = input("\nInput your Sentence: ")
        for char in invalid_chars:
            if char in sentence:
                print("Your sentence contains an invalid character, try again")
                invalid = True
                break
        if invalid == False:
            print("Your sentence is valid, thank you!")
            return sentence


# Similar to get_sentence() but makes sure only valid characters
# are used
def get_morse_code():
    valid_chars = ".-/ "
    while True:
        valid = True
        morse_code = input("\nInput Morse Code: ")
        for char in morse_code:
            if char not in valid_chars:
                print("Your morse code contains an invalid character, try again")
                valid = False
                break
        if valid == True:
            print("Your morse code is valid, thank you!")
            return morse_code


# Changes fancy "translating..." message depending on which way
# the user chose to translate
def handle_mode(mode, sentence):
    if mode == '1':
        print('\nTranslating English to Morse Code...')
        time.sleep(1)
        print("\nDONE! Here's the Morse Code:")
        translate_e2m(sentence.upper())
    else:
        print('\nTranslating Morse Code to English...')
        time.sleep(1)
        print("\nDONE! Here's the English:")
        translate_m2e(sentence.upper())

            
# Translates English to Morse Code
def translate_e2m(sentence):
    words = sentence.split()
    morse_code_words = []
    for word in words:
        morse_code_word = ''
        for char in word:
            morse_code_word += mc.morse_code_translate.get(char) + ' '
        morse_code_words.append(morse_code_word[:-1])

    formatted = ''
    for word in morse_code_words:
        formatted += word + '   '

    print(formatted[:-1])


# Translate Morse Code to English
def translate_m2e(morse_code):
    key_list = list(mc.morse_code_translate.keys())
    val_list = list(mc.morse_code_translate.values())
    words = morse_code.split('/')
    eng_words = []
    for word in words:
        english_word = ''
        letters = word.split()
        for letter in letters:
            english_word += key_list[val_list.index(letter)]
        eng_words.append(english_word)

    formatted = ''
    for word in eng_words:
        formatted += word + ' '

    print(formatted[:-1])


if __name__ == "__main__":
    main()
