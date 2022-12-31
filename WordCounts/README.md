# Word Counts Mini Project
## What it does
This project takes what text you have on your clipboard when it is run, and prints out the following information regarding the specified test:
* Characters- The number of characters in the text, including spaces and tabs but excluding the newline characters
* Characters excluding whitespace- The number of characters in the text excluding tabs, spaces, and the newline characters
* Words- The number of words in the text
* Paragraphs- The number of paragraphs in the text, where each paragraph is separated by one or more newline characters
* Full sentences- The number of sentences in the text, where each sentence is separated by a period. Does not include a period at the beginning or the ending sentence if it does not end in a period
* Partial sentences- The number of sentences in the text, where each sentence is separated by a period. Includes a period at the beginning or the ending sentence even if it does not end in a period

## Technologies used
Python is used for this mini project, as well as the pyperclip and re libraries. The pyperclip library is used to obtain the information on the clipboard of the user. The re library is used to preform regex to obtain the information needed about the text, specifically to avoid problems with double spaces or double newlines and in other cases to remove information not being counted at the time. 
