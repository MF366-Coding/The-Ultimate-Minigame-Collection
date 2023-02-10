# Minigame by MF366

# Importing needed modules
import datetime
import random
from os import system
from sys import platform as pf

# Find the system
clearingCommand = 'NULL'
if pf == "linux" or pf == "linux2" or pf == "darwin":
    clearingCommand = 'clear'
elif pf == "win32":
    clearingCommand = 'cls'

# Functions
def clsCmd():
    system(clearingCommand)

def randomizedMaths():
    firstNumber = random.random()
    secondNumber = random.random()
    clsCmd()
    firstNumberString = str(firstNumber)
    secondNumberString = str(secondNumber)
    firstAndSecondFull = firstNumberString+' + '+secondNumberString
    goAnswer = eval(input(firstAndSecondFull+'\nAnswer: '))
    score = 0
    if goAnswer == firstNumber+secondNumber:
        clsCmd()
        score += 1
        print('Your score: '+str(score)+'\n')
        randomizedMaths()
    else:
        clsCmd()
        print('Final Score: '+str(score)+'\nBetter luck next time!\n')
        quit()

# Start up
def StartUp():
	print("You'll be given a multiplication and you must type the result.\nEasy, right? Maybe...\n")
	startGameAsk = str(input("Are you ready?\nType 'yes' or 'no': "))
	if startGameAsk == 'yes':
		randomizedMaths()
	elif startGameAsk == 'no':
		quit()

