# Minigame by MF366

from os import system
from sys import platform as pf
import webbrowser

# Find the system
clearingCommand = 'NULL'
if pf == "linux" or pf == "linux2" or pf == "darwin":
    clearingCommand = 'clear'
elif pf == "win32":
    clearingCommand = 'cls'

# Functions
def clsCmd():
    system(clearingCommand)
    
def professionalSwapper(textToSwap):
    clsCmd()
    swappedText = textToSwap[::-1]
    print("Given sentence: "+textToSwap+"\nInverted sentence: "+swappedText+"\n")
    review = str(input("Is this correct?\nType 'yes' or 'no' here please: "))
    if review == 'yes':
        clsCmd()
        print('Thank you!\n')
        quit()
    if review == 'no':
        print('We are sorry to hear that...\n')
        goToIssues = str(input("Would you like to report this issue?\nIf so, you need a screenshot of the output.\nType 'yes' or 'no' here please: "))
        if goToIssues == 'yes':
            webbrowser.open('https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection/issues')
            quit()
