# Bridget D. Harrell
# Module 4 Assignment


from sys import exit #will be explained
from random import randint   #will be explained


myData = {}
guesses = 0
wins = 0

with open("questions.txt", "r") as infile:   #reading questions from text file "questions
    questions = infile.readlines()
    for question in questions:
        if "first" in question: 
            myData["first_name"] = input(question) #if "first" in question, display first name
        elif "last" in question:
            myData["last_name"] = input(question) #also if "last" in question, display last name
        else:
            print("badquestion in inputfile")    #or else display
            exit() #get out of loop

for play in range(10):   #10 attempts
    number = randint(0,100)   #1 to 100
    solved = False
    while not solved:  #execute if not guessed correctly
        guess = int(input(f"Guess a number from 0 to 100 : "))  #instruction - guess number 1 to 100
        guess +=1   #1 more guess
        if guess == number:    #if guess is equal to the number, display: "Great job name..."
            print(f"Great Job {myData['first_name']}, your guess of {guess} is correct!!!") 
            wins +=1    #add a win
            solved = True
            break   #terminate the loop
        if guess != number:  #if guess is wrong, display "your guess is incorrect!"
            print(f"Your guess of {guess} is incorrect!")

        if guess > number:
            print(f"Sorry, you guessed too high!!") #if the guess is too high, display: your guess is too high
        elif guess < number:
            print(f"Sorry, you guessed too low!!")  #if the guess is to low display: your guess is too low
        else:
            pass  #no execution


        if solved:   #if guessed correctly, display: "Let's play again..."
            print(f"Let's play again, you have completed {wins} out of 10 plays.")
            continue   #back to the beginning of the loop

print(f"{myData['first_name']} {myData['last_name']} guessed the correct number {wins} out of 10 plays.")
#display: Fist name +last name guessed the correct number..."
print(f"it took {myData['first_name']} {myData['last_name']} (guesses) guesses to do this!")
#display: Ik took first name +last name # guesses to do this" 
exit()  #exit Python
    




            
        
      
