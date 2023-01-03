# Pig Latin Mini Project
## About
This project takes the information on the user's clipboard and encodes english to piglatin or decodes piglatin to english. The pigLatinEncoder.py file encodes the english into piglatin with the following rules:
* Words smaller than 4 letters remain the same
* Words that start with a vowel have "yay" added to the end
* Words that start with a consonant have the first letter moved to the end and "ay" added to the end
The pigLatinDecoder.py file decodes the pig latin following the opposite of the above rules. 

## Technologies used
Python is used for this mini project, as well as the pyperclip library. The pyperclip library is used to obtain the text on the clipboard of the user as well as paste the updated text to the clipboard. 
