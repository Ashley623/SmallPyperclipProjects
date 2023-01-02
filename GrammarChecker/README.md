# Grammar Checker Mini Project
## About
This project takes what the user has on their clipboard, fixes some of the grammar, and then pastes the updated results back to the clipboard. The specific grammar it will change are:
* The word "I" will be capitalized
* Unnecessary spaces will be removed
* The first letter of every sentence will be capitalized
* Any letter that is not the first letter in a word will be made lowercase

Note that this list does not check for all grammar errors. Specifically, words with the first letter capitalized are assumed to be proper nouns and will not be changed to lower case. Similarily, proper nouns that are not capitalized will not become capitalized unless they are the first word in the sentence. 

## Technologies used
Python is used for this mini project, as well as the pyperclip and re libraries. The pyperclip library is used to obtain the text on the clipboard of the user as well as paste the updated text to the clipboard. The re library is used to preform regex to remove the extra spaces and to make sure all I's are capitalized.
