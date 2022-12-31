import pyperclip as pc
import re

# Get text from clipboard
text = pc.paste()

# Count number of words
removeExtraWhitespace = re.compile(r"\s+")
withOutExtraWhiteSpace = removeExtraWhitespace.sub(" ", text.strip())
words = len(withOutExtraWhiteSpace.split(" "))

# Count number of characters without spaces
withoutSpaces = removeExtraWhitespace.sub("", text.strip())
charsWithoutSpaces = len(withoutSpaces)

# Count number of paragraphs
removeExtraParagraphs = re.compile("\n+")
withoutExtraParagraphs = removeExtraParagraphs.sub("\n", text.strip())
paragraphs = len(withoutExtraParagraphs.split("\n"))

# Count number of characters
withoutNewLines = removeExtraParagraphs.sub("", text)
# Don't strip text because we are including spaces before and after in the count
characters = len(withoutNewLines)

# Count number of full sentences
toCheckSentences = re.compile(r"[^\.]")
onlyPeriodsFull = toCheckSentences.sub("", text.strip()[1:])
# I am indexing [1:] because I am not counting a period at the beginning as a full sentence
fullSentences = len(onlyPeriodsFull)

# Count number of partial sentences (Beginning and end can be partial)
partialText = text if text.strip()[-1] == "." else text + "."
onlyPeriodsPartial = toCheckSentences.sub("", partialText)
partialSentences = len(onlyPeriodsPartial)


print("Number of characters:", characters)
print("Number of characters excluding whitespace:", charsWithoutSpaces)
print("Number of words", words)
print("Number of paragraphs:", paragraphs)
print("Number of full sentences:", fullSentences)
print("Number of partial sentences:", partialSentences)
