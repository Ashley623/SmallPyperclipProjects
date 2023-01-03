import pyperclip as pc

vowels = ["a", "e", "i", "o", "u"]
punctuation = [",", ".", "?", "!", ";"]

# Obtain the text from the user's clipboard and turns it into a list
text = pc.paste().strip().split(" ")

english = ""
for word in text: # Loops through each word
    if(len(word) > 3):
        ep = ""
        if(word[-1] in punctuation): # Save any punctuation to add back later
            ep = word[-1]
            word = word[:-1]
        if(word[-3:] == "yay"): # If it ends in "yay", all that's needed is for "yay" to be removed
            english += word[:-3] + ep + " "
        else: # Otherwise the consonant needs to be moved to the front and "ay" needs to be removed
            english += word[-3] + word[:-3] + ep + " "
    else:
        english += word + " " # Words less than 4 letters long do not need to be decoded

# Remove extra space from the end
english = english[:-1]

# Copy the english text to the clipboard
pc.copy(english)