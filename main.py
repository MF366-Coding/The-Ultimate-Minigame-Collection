
'''
Entire code by: MF366
UwU
GitHub | Discord | YouTube (for Gaming)

Hope you enjot this game.

More minigames to come as soon as possible.

This app sends you the log file to your e-mail after use, if you want so.
'''

# Importing the needed modules
import mathTime
import numRand
from sys import platform as pf
from os import system
from random import randint
import swapSentence

# Find the system
clearingCommand = 'NULL'
if pf == "linux" or pf == "linux2" or pf == "darwin":
    clearingCommand = 'clear'
elif pf == "win32":
    clearingCommand = 'cls'

# Functions
def clsCmd():
    system(clearingCommand)

# Minigame Picker
if __name__ == '__main__':
    clsCmd()
    firstPicker = str(input("Please select an option.\n[1] Minigames\n[2] Utilities\n[3] Extra options\nType here please: "))
    if firstPicker == '1':
        clsCmd()
        minigamePicker = str(input("Please select a minigame.\n[1] QuickMaths\n[2] RandomGuesser\nType here please: "))
        if minigamePicker == '1':
            clsCmd()
            mathTime.StartUp()
        elif minigamePicker == '2':
            clsCmd()
            randPicker = str(input("Select a difficulty.\n[1] Easy\n[2] Normal\n[3] Hard\n[4] Impossible\nType here please: "))
            if randPicker == '1':
                clsCmd()
                numRand.easyMode()
            if randPicker == '2':
                clsCmd()
                numRand.normalMode()
            if randPicker == '3':
                clsCmd()
                numRand.hardMode()
            if randPicker == '4':
                clsCmd()
                numRand.extremeMode()
    if firstPicker == '2':
        clsCmd()
        toolPicker = str(input("Please select a tool.\n[1] SentenceInvertor\nType here please: "))
        if toolPicker == '1':
            clsCmd()
            textToSwap = str(input("Type the sentece you would like to invert here please:\n"))
            clsCmd()
            swapSentence.professionalSwapper(textToSwap=textToSwap)
    if firstPicker == '3':
        clsCmd()
        extraPicker = str(input("Please select an extra option.\n[1] Jokes\nType here please: "))
        if extraPicker == '1':
            clsCmd()
            print('Ready for some jooooooookes?\nType next to skip to the next joke.\nType quit to exit.\n')
            with open('jokes.txt', 'r') as jokesFile:
                jokesExtract = jokesFile.read()
                jokes = jokesExtract.split('//')
                jokesFile.close()
            quittingAsk = False
            while quittingAsk == False:
                tellJoke = str(input(str(jokes[randint(0, 1)]+'\n')))
                if tellJoke == 'quit':
                    quittingAsk = True
                    quit()
                