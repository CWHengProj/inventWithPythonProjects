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
    attempts,answer=freshStart()
    while True:
        userInput=input('Please enter your guesss from 0 to 999:')
        if inputValidator(userInput)== True:
            if comparator(formatter(answer,userInput)):
                victoryScreen()
                exit()
            attempts+=1
            if attempts==difficultyGenerator():
                if gameOver()==True:
                    freshStart()
                    continue
                else:
                    print('Thank you for playing. See you again!')
                    exit()
            break
def coolIntroScreen():
    #explains the rules to the player
    print("Welcome! This is a deductive logic game, where you have to guess a digit from 0 to 999.\n If the correct digit is in the wrong position, it will be highlighted in red.\n If the correct digit is in the correct position, it will be highlighted in green.\n Else, the digits will appear as white.\n Now that we're clear on the rules, lets begin!")
def freshStart():
    #initializes the values again
    attempts=0
    answer=randint(1,999)
    print(answer) #to be removed
    return attempts, answer
def inputValidator(x):
    #ensure that input is within range and numerical
    try:
        if int(x)>=0 and int(x)<=999:
            return True
    except ValueError:
        print('Please enter an appropriate value from 0 to 999')
        return False
def gameOver(attempts):
    #counts the number of attempts the user has made and serves a game over screen all attempts used up
    print(f'Game over! You have used up all {attempts} attempts!')
    response =(input('Would you like to play again? Y/N'))
    if response =='y' or response =='Y' or response =='Yes' or response =='yes':
        return True
    return False
def difficultyGenerator():
    #sets the number of attempts before game over
    return 10
def victoryScreen():
    #congratulates user once complete, returns number of attempts as well
    print('hiphiphooray!')
def formatter(ans,input):
    #creates a 3 digit format for both answer and user input
    ansFormatted =(f'{ans:02d}').split()
    guessFormatter =(f'{input:02d}').split()
    return ansFormatted, guessFormatter
def comparator(a,b):
    #creates a comparator to give the user hints with color code
    for i in range(len(a)):
        if b[i]==a[i]:
            #turn the value green
        if b[i]!=a[i] and b[i] in a:
            #turn the value orange
    if a=b:
        return True
if __name__=="__main__":
    main()