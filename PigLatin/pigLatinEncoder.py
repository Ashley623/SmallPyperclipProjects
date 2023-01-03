import pyperclip as pc

# Define vowels and punctuation to use later
vowels = ["a", "e", "i", "o", "u"]
punctuation = [",", ".", "?", "!", ";"]

# Obtain the text from the user's clipboard and turns it into a list
text = pc.paste().strip().split(" ")

pigLatin = ""
for word in text: # Loop though each word
    if len(word) > 3: 
        ep = ""
        if(word[-1] in punctuation): # Save any punctuation to add back later
            ep = word[-1]
            word = word[:-1]
        if(word[0] in vowels): # For words starting with a vowel, "yay" is added to the end
            pigLatin += word + "yay" + ep + " "
        else: # For words starting with a consonant, the consonant is moved to the end and "ay" is added
            pigLatin += word[1:] + word[1] + "ay" + ep + " "
    else:
        pigLatin += word + " "

# Remove extra space from the end
pigLatin = pigLatin[:-1]

# Copy the pig latin to the clipboard
pc.copy(pigLatin)
