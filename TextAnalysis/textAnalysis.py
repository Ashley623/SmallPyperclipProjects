import pyperclip as pc
import re
import matplotlib.pyplot as plt
from textblob import TextBlob

# Defines variables to start with, text is taken from the user's clipboard
text = pc.paste()
words = {}

# Removes punctuation
removeExtras = re.compile(r"[!@#$%^&*\(\)\-\'\";/?.,\n]")
text = removeExtras.sub("", text)

# Creates a frequency dictionary
for word in text.split(" "):
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

# Loops through and finds the top 10 most frequent words
maxWordList = {}
for i in range(10):
    maxNum = 0
    maxWord = ""
    for i in zip(words.keys(), words.values()):
        if(i[1] > maxNum):
            maxNum = i[1]
            maxWord = i[0]
    if(maxNum == 0):
        break # Exit early for if there is less than 10 unique words
    maxWordList[maxWord] = maxNum
    words[maxWord] = 0 # Set to 0 so it is not chosen again

# Graph the top 10 most frequent terms (or less if there aren't 10 available)
fig, graph = plt.subplots()
graph.bar(maxWordList.keys(), maxWordList.values())
graph.set(ylim = (0, max(maxWordList.values())), yticks = range(1, max(maxWordList.values())+2))
# Change the labels so it is displayed nicer
graph.set_xlabel("Words")
graph.set_ylabel("Frequency")
graph.set_title("Top " + str(len(maxWordList)) + " most frequent words")
plt.show()

# Now check the sentiment analysis and display it to the user
blob = TextBlob(text)
print("The polarity of the text from -1 (very negative) to 1 (very positive) is", blob.sentiment[0])
print("The subjectivity of the text from 0 (very objective) to 1 (very subjective is", blob.sentiment[1])