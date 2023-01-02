import pyperclip as pc
from answers import answers
from answers import questions
# The answers.py file has all the questions and the answers, so if you look at this file you will not get spoilers

points = 0
print("For this scavenger hunt game, copy the answer to the question on to your clipboard")
print("You have 3 tries to copy the correct answer, and the number of points starts at 3 and decreases each try")
for i in range(len(questions)):
    # Print the question
    print(questions[i])
    correct = False
    for j in range(3): # Loops through the 3 different tries for each question
        pc.waitForNewPaste(300) # This pauses the program until the user copies something new
        # Times out after 5 min in case the user forgets to stop the program from running
        if(pc.paste().strip()[:len(answers[i])] == answers[i] or pc.paste().strip()[-len(answers[i]):] == answers[i]):
            # The copied text is striped, and then only the beginning part or the last part are looked at in case
            #   the user copies extra characters aside from the answer (like a period)
            print("You got it correct!!")
            correct = True
            points += 3-j # Number of points recieved decreases by 1 each attempt
            break
    if(not correct):
        # Prints out the correct answer if you didn't get it in 3 tries
        print("You failed to copy the correct answer with your 3 attempts")
        print("The answer was:",answers[i])
        j = 3
    print("You got", 3-j, "points, your total score is", points)
    print("\n")
