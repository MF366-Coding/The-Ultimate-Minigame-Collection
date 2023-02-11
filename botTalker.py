# Tool by MF366

from clsCmd import clear

def talkToCarl():
    quittingAsk = False
    quittingNumber = 0
    with open('carl.txt', 'r') as carlFile:
        carlExtract = carlFile.read()
        carlFile.close()
        carl = carlExtract.split('//')
    clear()
    while not quittingAsk:
        recommendGame = str(input('Input: '))
        print('Output: '+carl[quittingNumber])
        quittingNumber += 1
        if quittingNumber == 13:
            quit()
        if recommendGame == 'quit':
        	quittingAsk = True
        	quit()
         
def talkToAnna():
    quittingAsk = False
    quittingNumber = 0
    with open('anna.txt', 'r') as annaFile:
        annaExtract = annaFile.read()
        annaFile.close()
        anna = annaExtract.split('//')
    clear()
    while not quittingAsk:
        recommendGame = str(input('Input: '))
        print('Output: '+anna[quittingNumber])
        quittingNumber += 1
        if quittingNumber == 11:
            quit()
        if recommendGame == 'quit':
        	quittingAsk = True
        	quit()

def talkToZang():
    quittingAsk = False
    quittingNumber = 0
    with open('zang.txt', 'r') as zangFile:
        zangExtract = zangFile.read()
        zangFile.close()
        zang = zangExtract.split('//')
    clear()
    while not quittingAsk:
        recommendGame = str(input('Input: '))
        print('Output: '+zang[quittingNumber])
        quittingNumber += 1
        if quittingNumber == 3:
            quit()
        if recommendGame == 'quit':
        	quittingAsk = True
        	quit()

def talkToURMOM():
    quittingAsk = False
    quittingNumber = 0
    with open('ur-mom.txt', 'r') as urmomFile:
        urmomExtract = urmomFile.read()
        urmomFile.close()
        urmom = urmomExtract.split('//')
    clear()
    while not quittingAsk:
        recommendGame = str(input('Input: '))
        print('Output: '+urmom[quittingNumber]) # Truly a really nice line
        quittingNumber += 1
        if quittingNumber == 13:
            quit()
        if recommendGame == 'quit':
        	quittingAsk = True 
        	quit()
