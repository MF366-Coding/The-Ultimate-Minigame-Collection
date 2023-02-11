'''
Entire code by: MF366
UwU
GitHub | Discord | YouTube (for Gaming)

Hope you enjoy this game.

More minigames to come as soon as possible.
'''

# Importing the needed modules
import numRand
from sys import platform as pf
from os import system
from random import randint
import botTalker
import swapSentence
import webbrowser
from clsCmd import clear
import rain

# Minigame Picker
if __name__ == '__main__':
    with open('tumc_init.txt', 'r', encoding='utf-8') as textkoolInit:
        textkoolExtract = textkoolInit.read()
        textkoolInit.close()
    clear()
    with open('player.txt', 'r', encoding='utf-8') as playerNameFile:
        playerNameExtract = playerNameFile.read()
        playerNameFile.close()
    firstPicker = str(input(str(textkoolExtract)+"\nWelcome back, "+playerNameExtract+"!\nPlease select an option.\n[1] Minigames\n[2] Utilities\n[3] Extra options\n[4] Settings n' Info\nType here please: "))
    if firstPicker == '1':
        clear()
        minigamePicker = str(input("Please select a minigame.\n[1] It's raining outside (Sad story)\n[2] RandomGuesser\nType here please: "))
        if minigamePicker == '1':
            clear()
            rain.startUpGame()
        elif minigamePicker == '2':
            clear()
            randPicker = str(input("Select a difficulty.\n[1] Easy\n[2] Normal\n[3] Hard\n[4] Impossible\nType here please: "))
            if randPicker == '1':
                clear()
                numRand.easyMode()
            if randPicker == '2':
                clear()
                numRand.normalMode()
            if randPicker == '3':
                clear()
                numRand.hardMode()
            if randPicker == '4':
                clear()
                numRand.extremeMode()
    if firstPicker == '2':
        clear()
        toolPicker = str(input("Please select a tool.\n[1] SentenceInvertor\nType here please: "))
        if toolPicker == '1':
            clear()
            textToSwap = str(input("Type the sentece you would like to invert here please:\n"))
            clear()
            swapSentence.professionalSwapper(textToSwap=textToSwap)
    if firstPicker == '3':
        clear()
        extraPicker = str(input("Please select an extra option.\n[1] Jokes\n[2] What game should I play?\n[3] Talk to a bot (because I have no better stuff to do)\nType here please: "))
        if extraPicker == '1':
            clear()
            print('Ready for some jooooooookes?\nType next to skip to the next joke.\nType quit to exit.\n')
            with open('jokes.txt', 'r') as jokesFile:
                jokesExtract = jokesFile.read()
                jokes = jokesExtract.split('//')
                jokesFile.close()
            quittingAsk = False # Nice line
            while quittingAsk == False:
                tellJoke = str(input(str(jokes[randint(0, 1)]+'\n')))
                if tellJoke == 'quit':
                    quittingAsk = True
                    quit()
        if extraPicker == '2':
            clear()
            print('I am your AI BFF.\nJk lmao How could I be friends with something like you?\nAnyways, rules are simple.\nI may have robbed some people and now...\n...well, I have to keep recommending you some games to play! (that is my punishment)\nHit ENTER to skip and quit to... well: quit!!\nDaaah... (i really dont want to do this)\nYou should play....\n')
            with open('games.txt', 'r', encoding='utf-8') as gamesFile:
                gamesExtract = gamesFile.read()
                games = gamesExtract.split('//')
                gamesFile.close()
            quittingAsk = False
            while quittingAsk == False:
                recommendGame = str(input(str(games[randint(0, 23)]+'\n')))
                if recommendGame == 'quit':
                    quittingAsk = True
                    quit()
        if extraPicker == '3':
            clear()
            print("Welcome to BotTalker v1.1.0.\nJust select a character and you're good to start!\n")
            botTalkerInit = str(input("Select a bot to talk with.\n[1] Carl\n[2] Anna\n[3] ur mom (lol)\n[4] Mr. Zang (Awarded business man)\nType here please: "))
            if botTalkerInit == '1':
                botTalker.talkToCarl()
            elif botTalkerInit == '2':
                botTalker.talkToAnna()
            elif botTalkerInit == '3':
                botTalker.talkToURMOM()
            elif botTalkerInit == '4':
                botTalker.talkToZang()
            else:
                quit()
    elif firstPicker == '4':
        clear()
        setUpInfoPicker = str(input("This Python program was made by MF366.\n[1] Go to GitHub\n[2] Change Player Name\n[3] Report a bug\n[4] Recommend a new feature\nType here please: "))
        if setUpInfoPicker == '1':
            clear()
            webbrowser.open('https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection')
            quit()
        elif setUpInfoPicker == '2':
            clear()
            print("Your username: "+playerNameExtract)
            newUsernamePicker = str(input("Type the new username here please: "))
            with open('player.txt', 'w', encoding='utf-8') as playerNameFile:
                playerNameFile.write(newUsernamePicker)
                print("\nYou'll have to reopen TUMC to apply the changes.")
                quit()
        elif setUpInfoPicker == '3':
            clear()
            print('Assign MF366-Coding and label as bug\n')
            webbrowser.open('https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection/issues/new')
            quit()
        elif setUpInfoPicker == '4':
            clear()
            print('Assign MF366-Coding and label as enhancement\n')
            webbrowser.open('https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection/issues/new')
            quit()
            
                