# Scavenger Hunt Mini Project
## About
This project is a scavenger hunt about things related to Python, Pyperclip, or GitHub. The answer must be copied to the clipboard within 3 tries to get points for the question. The number of points given decrease by the number of attempts needed. The copied text is striped of whitespace, and then only the beginning part or the last part are looked at in case the user copies extra characters aside from the answer (like a period). The answers.py file has all of the questions and answers to the program, so if you want to try the game without spoilers don't look at that file.

Note- The program times out after 5 min without something new copied in case the user forgets to stop the program from running

## Technologies used
Python is used for this mini project, as well as the pyperclip and re libraries. The pyperclip library is used to obtain the information on the clipboard of the user. It is also used to pause the program until it registers the user copying something new. 
