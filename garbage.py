# By: MF366

# Importing needed modules
from clsCmd import clear
from random import randint

# Setting up the functions
with open('garbage.txt', 'r') as garbageFile:
        garbageExtract = garbageFile.read()
        garbageSplitter = garbageExtract.split('//')

score = 0
garbageGen = 'NULL'
garbageSecret = 0

def garbageGenerator():
    global garbageGen
    global garbageSecret
    garbageSecret = randint(0, 9)
    garbageGen = garbageSplitter[garbageSecret]

def emptyGarbage():
    global score
    global garbageGen
    global garbageSecret
    clear()
    quittingAsk = False
    if quittingAsk == True:
        clear()
        print("Player quitted.\nFinal Score: "+str(score)+"\n")
        quit()
    while quittingAsk == False:
        garbageGenerator()
        clear()
        deleteThis = str(input("Are you sure you want to permantently delete "+garbageGen+"?\n"))
        if deleteThis == 'quit':
            quittingAsk = True
        if garbageSecret == 3 or garbageSecret == 4 or garbageSecret == 7 or garbageSecret == 8 and deleteThis == 'yes':
            score += 1
        elif garbageSecret == 3 or garbageSecret == 4 or garbageSecret == 7 or garbageSecret == 8 and deleteThis == 'no':
            print("Your PC blown up!\nNo tech support for this issue.\nFinal Score: "+str(score)+"\n")
            
def StartUp():
	clear()
	print("You'll be given stuff to delete.\nJust... don't delete important stuff!!\n[NOT FINISHED = MAY CONTAIN BUGS]\n")
	input('')
	emptyGarbage()
