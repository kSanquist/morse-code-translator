# morse-code-translator
This command line program allows the user to translate from Morse Code to English and vice versa!

## What you'll find
### READ ME
- What you're in right now, gives a much more thorough discription of this program

### main.py
- The meat and potatoes, where all the logical code is that makes the program what it is

### morse_code.py
- A long dictionary containing the letters of the English alphabet, numbers 1 - 10, a couple of punctuation marks, and their respective morse code translations

## How morse_code.py dictionary is set up
format: letter:morse_code
- example: "A":".-"

## Functions you will find in main.py
### main()
- The hub for all other functions to run off of
- If you care about this project, you probably have enough understanding of the 'main' function

### program_details()
- A LOT of print statements
- Displays name of program, author, and important notes on how to use the program

### get_mode()
- Asks the user which way in which they want to translate
- Either from English -> Morse Code or vice versa
- Makes sure input is acceptable before returning

### get_sentence()
- Provides an invalid characters list and checks to see if the inputted sentence has any of those characters in it
- Makes you input a new sentence until the sentence is valid

### get_morse_code()
- Similar to get_sentence() but instead, provides a list of valid characters and checks to see if the inputted sentences has only those characters in it
  - Easiest way to do it since there are only 4 characters that are valid when inputting Morse Code into the program

### handle_mode()
- Changes fancy "translating..." depending on which mode the user inputted in get_mode() function
- If user inputs mode 1 (English -> Morse Code) the program runs the translate_e2m() function
- If user inputs mode 2 (Morse Code -> English) the program runs  the translate_m2e() function

### translate_e2m()
- e2m = English to Morse Code
- Splits words in provided sentence and then goes through each letter of each words and converts that letter to its respective Morse Code translation
- Adds each letter to morse_code_word and then appends that variable to morse_code_words until all words have been converted
- Finally formats into one string and prints it out

### translate_m2e()
- Similar to translate_e2m()
- Had to get key from dictionary instead of value so I used the list.index() method
- Knows every word is seperated by a ( / ) and every letter is seperated by a space
- For every word, splits letter into a list of letters and then for every letter converts it to its respective English translation and adds it to english_word string
- Adds final English word to list of English words that have been translated
- Finally formats in a similar way to translate_e2m() function
