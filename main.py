'''
Entire code by: MF366 (except for PongEngine by Norb)

GitHub       | Discord                | YouTube
MF366-Coding | not gonna tell you lel | @mf_366

Hope you enjoy this little game!

More minigames and tools to come as soon as possible.
'''

# Importing the needed modules
from random import randint, shuffle
import webbrowser
import rain
import PongEngine
import sys
from os import system

def clear():
    # Find the system
    if sys.platform == "linux" or sys.platform == "darwin":
        clearingCommand = 'clear'
        system(clearingCommand)
    elif sys.platform == "win32":
        clearingCommand = 'cls'
        system(clearingCommand)
    else:
        system("clear")

class swapSentence:
    @staticmethod
    def professionalSwapper(textToSwap):
        clear()
        swappedText = textToSwap[::-1]
        print("Given sentence: "+textToSwap+"\nInverted sentence: "+swappedText+"\n")
        review = str(input("Is this correct?\nType 'yes' or 'no' here please: "))
        if review == 'yes':
            clear()
            print('Thank you!\n')
            quit()
        if review == 'no':
            print('We are sorry to hear that...\n')
            goToIssues = str(input("Would you like to report this issue?\nIf so, you need a screenshot of the output.\nType 'yes' or 'no' here please: "))
            if goToIssues == 'yes':
                webbrowser.open('https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection/issues')
                quit()

class news:
    @staticmethod
    def RunCode():
        updates = input("[ WHAT'S NEW IN TUMC? ]\nBiggest update to TUMC so far...\n\n[ Pong Minigame by Norb ]\nPlay Pong on the Command Prompt. Yes, you heard this right!!!\nNote that this only runs on Windows (we tested in Linux, but not in Mac).\nCheck README.md for more info.\n\n[ This Section ]\nYeah, that's right! Now, this app comes with a ''What's new?'' section!\n\n[ AT GITHUB ]\nFor more info, check https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection.\n\nThanks for downloading this project.\n\nMade by MF366.\n\n< Press ENTER to go to the repo. >\n< Type 'quit' and hit ENTER to quit the app. >\n\nYour choice: ")
        if updates == 'quit':
            quit()
        else:
            webbrowser.open('https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection')


class numRand:
    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

class botTalker:
    @staticmethod
    def talkToCarl():
        quittingAsk = False
        quittingNumber = 0
        with open('carl.txt', 'r') as carlFile:
            carlExtract = carlFile.read()
            carlFile.close()
            carl = carlExtract.split('//')
        clear()
        while quittingAsk == False:
            recommendGame = str(input('Input: '))
            print('Output: '+carl[quittingNumber])
            quittingNumber += 1
            if quittingNumber == 15:
                quit()
            if recommendGame == 'quit':
                quittingAsk = True
                quit()

    @staticmethod
    def talkToAnna():
        quittingAsk = False
        quittingNumber = 0
        with open('anna.txt', 'r') as annaFile:
            annaExtract = annaFile.read()
            annaFile.close()
            anna = annaExtract.split('//')
        clear()
        while quittingAsk == False:
            recommendGame = str(input('Input: '))
            print('Output: '+anna[quittingNumber])
            quittingNumber += 1
            if quittingNumber == 11:
                quit()
            if recommendGame == 'quit':
                quittingAsk = True
                quit()

    @staticmethod
    def talkToZang():
        quittingAsk = False
        quittingNumber = 0
        with open('zang.txt', 'r') as zangFile:
            zangExtract = zangFile.read()
            zangFile.close()
            zang = zangExtract.split('//')
        clear()
        while quittingAsk == False:
            recommendGame = str(input('Input: '))
            print('Output: '+zang[quittingNumber])
            quittingNumber += 1
            if quittingNumber == 3:
                quit()
            if recommendGame == 'quit':
                quittingAsk = True
                quit()

    @staticmethod
    def talkToURMOM():
        quittingAsk = False
        quittingNumber = 0
        with open('ur-mom.txt', 'r') as urmomFile:
            urmomExtract = urmomFile.read()
            urmomFile.close()
            urmom = urmomExtract.split('//')
        clear()
        while quittingAsk == False:
            recommendGame = str(input('Input: '))
            print('Output: '+urmom[quittingNumber]) # Truly a really nice line
            quittingNumber += 1
            if quittingNumber == 13:
                quit()
            if recommendGame == 'quit':
                quittingAsk = True
                quit()

# Minigame Picker
if __name__ == '__main__':
    clear()
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
        minigamePicker = str(input("Please select a minigame.\n[1] RandomGuesser\n[2] Pong CMD Edition by Norb (Check README.md before playing)\nType here please: "))
        if minigamePicker == '1':
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
        elif minigamePicker == '2':
            clear()
            PongEngine.RunPong()
            
    if firstPicker == '2':
        clear()
        toolPicker = str(input("Please select a tool.\n[1] SentenceInvertor\nType here please: "))
        if toolPicker == '1':
            clear()
            textToSwap = str(input("Type the sentence you would like to invert here please:\n"))
            clear()
            swapSentence.professionalSwapper(textToSwap=textToSwap)
            
    if firstPicker == '3':
        clear()
        extraPicker = str(input("Please select an extra option.\n[1] Jokes\n[2] What game should I play?\n[3] Talk to a bot (because I have no better stuff to do)\n[4] It's raining outside (Sad story)\nType here please: "))
        if extraPicker == '1':
            clear()
            print('Ready for some jooooooookes?\nHit ENTER to skip to the next joke.\nType quit to exit.\n')
            with open('jokes.txt', 'r') as jokesFile:
                jokesExtract = jokesFile.read()
                jokes = jokesExtract.split('//')
                jokesFile.close()

            quittingAsk = False

            jokeArray = []
            def regenJokes():
                global jokeArray
                jokeArray = jokes.copy()
                shuffle(jokeArray)

            while not quittingAsk:
                if len(jokeArray) == 0:
                    regenJokes()
                tellJoke = str(input(str(jokeArray.pop(randint(0, len(jokeArray)-1))+'\n')))
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
            while not quittingAsk:
                recommendGame = str(input(str(games[randint(0, 33)]+'\n')))
                if recommendGame == 'quit':
                    quittingAsk = True
                    quit()
        if extraPicker == '3':
            clear()
            print("Welcome to BotTalker v1.1.1.\nJust select a character and you're good to start!\n")
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
        if extraPicker == '4':
            clear()
            rain.startUpGame()
    elif firstPicker == '4':
        clear()
        setUpInfoPicker = str(input("This Python program was made by MF366.\n[1] Go to GitHub\n[2] Change Player Name\n[3] Report a bug\n[4] Recommend a new feature\n[5] What's new over here?\nType here please: "))
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
        elif setUpInfoPicker == '5':
            clear()
            news.RunCode()
        elif setUpInfoPicker == '6':
            clear()
            print("I really don't think you were suppose to be able to read this but...\nI also don't care about it...\nEnjoy this useless secret!")
            quit()
