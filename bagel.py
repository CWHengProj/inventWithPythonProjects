#will create a wordle clone once this project is complete.
from random import randint
from termcolor import colored
def main():
    coolIntroScreen()
    attempts,answer=freshStart()
    while True:
        userInput=input('Please enter your guesss from 0 to 999:')
        if inputValidator(userInput)== True:
            x,y=formatter(answer,userInput)
            comparator(x,y)
            if int(answer)==int(userInput):
                victoryScreen(attempts)
                exit()
            attempts+=1
            if attempts==difficultyGenerator():
                if gameOver(attempts)==True:
                    attempts,answer=freshStart()
                else:
                    print('Thank you for playing. See you again!')
                    exit()
def coolIntroScreen():
    #explains the rules to the player
    print("Welcome! This is a deductive logic game, where you have to guess a digit from 0 to 999.")
    print(colored("If the correct digit is in the wrong position, it will be highlighted in yellow.",'yellow'))
    print(colored("If the correct digit is in the correct position, it will be highlighted in green.",'green'))
    print(colored("Else, the digits will appear as red.",'red'))
    print("Now that we're clear on the rules, lets begin!")
def freshStart():
    #initializes the values again
    attempts=0
    answer=randint(1,999)
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
def victoryScreen(attempts):
    print(f'Congratulations! You completed the challenge in {attempts} attempts! Well done!')
def formatter(ans,input):
    #creates a 3 digit format for both answer and user input
    ansFormatted=[]
    guessFormatted=[]
    a=('{:02d}'.format(ans))
    g=('{:03d}'.format(int(input)))
    for value in a:
        ansFormatted.append(value)
    for value in g:
        guessFormatted.append(value)
    return ansFormatted, guessFormatted
def comparator(a,b):
    #creates a comparator to give the user hints with color code
    for i in range(len(a)):
        if b[i]==a[i]:
            #turn the value green
            b[i]=colored(b[i],'green')
        elif b[i] in a:
            #turn the value yellow
            b[i]=colored(b[i],'yellow')
        else:
            b[i]=colored(b[i],'red')
    #print the 3 values in a box
    for i in b:
        print(f"{i}", end="")
    print('\n')
if __name__=="__main__":
    main()