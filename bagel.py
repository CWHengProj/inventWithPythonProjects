#Guess a 3 digit number. Hints will be given according to your guess.
#correct digit wrong position
#correct digit correct position
#no correct digits
#add colour code for the hints
#you have 10 tries.
#will create a wordle clone once this project is complete.
from random import randint
def main():
    welcomeMsg='Hell0!'
    print(welcomeMsg)
    attempts=0
    answer=randint(1,999)
    print(answer) #to be removed
    while True:
        checker(int(input('Make your guess!:')))
def checker(x):
    try:
        print(x)
    except ValueError:
        print('Please enter an appropriate value (between 0 to 999)')
if __name__=="__main__":
    main()