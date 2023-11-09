#Guess a 3 digit number. Hints will be given according to your guess.
#correct digit wrong position
#correct digit correct position
#no correct digits
#add colour code for the hints
#you have 10 tries.
#will create a wordle clone once this project is complete.
from random import randint
def main():
    coolIntroScreen()
    attempts=0
    answer=randint(1,999)
    print(answer) #to be removed
    while True:
        userInput=input('Please enter your guesss from 0 to 999:')
        if inputValidator(userInput)== True:
            comparator(formatter(answer,userInput))
            break

    
    victoryScreen()
def coolIntroScreen():
    #explains the rules to the player
    print("Welcome! This is a deductive logic game, where you have to guess a digit from 0 to 999.\n If the correct digit is in the wrong position, it will be highlighted in red.\n If the correct digit is in the correct position, it will be highlighted in green.\n Else, the digits will appear as white.\n Now that we're clear on the rules, lets begin!")



def inputValidator(x):
    #ensure that input is within range and numerical
    try:
        if int(x)>=0 and int(x)<=999:
            return True
    except ValueError:
        print('Please enter an appropriate value from 0 to 999')
        return False
def formatter(ans,input):
    #creates a 3 digit format for both answer and user input
    ansFormatted =f'{ans:02d}'
    guessFormatter =f'{input:02d}'
    return ansFormatted, guessFormatter
def comparator(a,b):
    #creates a comparator to give the user hints with color code
    
"""def gameOver():
    #counts the number of attempts the user has made and serves a game over screen all attempts used up
def difficultyGenerator():
    #sets the number of attempts before game over"""
def victoryScreen():
    #congratulates user once complete, returns number of attempts as well
    print('hiphiphooray!')
if __name__=="__main__":
    main()