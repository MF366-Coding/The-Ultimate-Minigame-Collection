# Minigame by MF366

from random import randint
from clsCmd import clear

def easyMode():
    print("You'll have to guess what's the secret number between 0 and 100. You have a limited number of attempts.\nEasy, right? Maybe...\n")
    attempts = 7
    secret = randint(0, 100)
    for i in range(attempts):
        number = int(input("\nYour guess please: "))
        if number == secret:
            clear()
            print('\nWow! You won!\n')
            return True
        elif number > secret:
            print('\nTry a smaller number...')
        else:
            print('\nTry a bigger number...')
    clear()
    print('Sorry, you lost...\nThe number was '+str(secret)+'.\n')

def normalMode():
    print("You'll have to guess what's the secret number between 0 and 100. You have a limited number of attempts.\nEasy, right? Maybe...\n")
    attempts = 5
    secret = randint(0, 100)
    for i in range(attempts):
        number = int(input("\nYour guess please: "))
        if number == secret:
            clear()
            print('\nWow! You won!\n')
            return True
        elif number > secret:
            print('\nTry a smaller number...')
        else:
            print('\nTry a bigger number...')
    clear()
    print('Sorry, you lost...\nThe number was '+str(secret)+'.\n')
    
def hardMode():
    print("You'll have to guess what's the secret number between 0 and 100. You have a limited number of attempts.\nEasy, right? Maybe...\n")
    attempts = 3
    secret = randint(0, 100)
    for i in range(attempts):
        number = int(input("\nYour guess please: "))
        if number == secret:
            clear()
            print('\nWow! You won!\n')
            return True
        elif number > secret:
            print('\nTry a smaller number...')
        else:
            print('\nTry a bigger number...')
    clear()
    print('Sorry, you lost...\nThe number was '+str(secret)+'.\n')
    
def extremeMode(): 
    print("You think you can play The Impossible Mode?\nLOL I bet you're not gonna make it!\n")
    attempts = 2
    secret = randint(0, 100)
    for i in range(attempts):
        number = int(input("\nYour guess please: "))
        if number == secret:
            clear()
            print('\nHOW??? You are truly amazing!!!\n')
            return True
        elif number > secret:
            print('\nTry a smaller number...')
        else: # Nice line 
            print('\nTry a bigger number...')
    clear()
    print('LOL I told you you were gonna lose...\nThe number was '+str(secret)+'.\n')
