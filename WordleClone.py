from wonderwords import RandomWord
r=RandomWord()
from termcolor import colored
def main():
    coolIntroScreen()
    attempts,answer=freshStart()
    while True:
        userInput=input('Please enter a five letter word: ').upper()
        if inputValidator(userInput)== True:
            x,y=formatter(answer,userInput)
            comparator(x,y)
            if answer==userInput:
                victoryScreen(attempts)
                exit()
            attempts+=1
            if attempts==difficultyGenerator():
                if gameOver(attempts,answer)==True:
                    attempts,answer=freshStart()
                else:
                    print('Thank you for playing. See you again!')
                    exit()
        else:
            print('Invalid input!\n')
def coolIntroScreen():
    #explains the rules to the player
    print("Welcome! This is a deductive logic game, where you have to guess a five letter word.")
    print(colored("If the correct letter is in the wrong position, it will be highlighted in yellow.",'yellow'))
    print(colored("If the correct letter is in the correct position, it will be highlighted in green.",'green'))
    print(colored("Else, the letters will appear as red.",'red'))
    print("You have Five attempts. Now that we're clear on the rules, lets begin!")
def freshStart():
    #initializes the values again
    attempts=0
    answer=r.word(word_min_length=5,word_max_length=5).upper()
    return attempts, answer
def inputValidator(x):
    #ensure that input is within range and alphabetical
    if x.isalpha() and len(x)==5:
            return True
    return False
def gameOver(attempts,answer):
    #counts the number of attempts the user has made and serves a game over screen all attempts used up
    print(f'Game over! You have used up all {attempts} attempts!')
    print(f'The correct answer is: {answer}')
    response =(input('Would you like to play again? Y/N '))
    if response =='y' or response =='Y' or response =='Yes' or response =='yes':
        return True
    return False
def difficultyGenerator():
    #sets the number of attempts before game over
    return 5
def victoryScreen(attempts):
    print(f'Congratulations! You completed the challenge in {attempts} attempts! Well done!')
def formatter(ans,input):
    #creates a 3 digit format for both answer and user input
    ansFormatted=[]
    guessFormatted=[]
    for letter in ans:
        ansFormatted.append(letter)
    for letter in input:
        guessFormatted.append(letter)
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