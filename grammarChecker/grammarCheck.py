import pyperclip as pc
import re

# Paste the text from clipboard
text = pc.paste()

# Defines variables to be used in the for loop
# maybeCapitalized is True when it is the first letter in a word, to allow for
#       proper nouns to not have the capitalization removed
# yesCapitalised is True when it is the first letter in a sentence
yesCapitalized = True
maybeCapitalized = False
whitespace = [" ", "    ", "\t", "\n"]
punctuation = [".", "!", "?"]

for i in range(len(text)):
    letter = text[i]
    if yesCapitalized and letter not in whitespace:
        # Capitalizes the first letter in a sentence
        text = text[:i] + letter.upper() + text[i+1:]
        yesCapitalized = False
    elif not maybeCapitalized:
        # Removes capital letter in the middle of a word
        text = text[:i] + letter.lower() + text[i+1:]
    elif maybeCapitalized:
        # Allows for the first letter in a word to stay as it is
        maybeCapitalized = False
    
    if letter in punctuation:
        # Means a new sentence is starting
        yesCapitalized = True
    elif letter in whitespace:
        # Means a new word is starting
        maybeCapitalized = True

# Remove extra spaces
removeExtraSpaces = re.compile(r" {2,}")
text = removeExtraSpaces.sub(" ", text)
        
# Make sure I is capitalized
checkForI = re.compile(r" i([ .!?])")
text = checkForI.sub(r" I\1", text)

# Paste the changed text to the clipboard
pc.copy(text)