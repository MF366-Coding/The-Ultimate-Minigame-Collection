# Code and Story by: MF366
# WARNING: Sad story ahead
# SPOILER ALERT: Code after line 127 contains SPOILERS

# Importing the needed modules
from clsCmd import clear

'''
You're not allowed to see the story without running the code!
Or else: it would ruin it (spoilers right?).
So yeah...
DON'T DO IT! Just... DON'T!!!
























































What a nice blanc line!

























































'''
def gameEngine(number):
    if number == 1:
        input("Chapter 001\n=================\n")
        input("It's raining outside!\nI have 5 minutes until my Job Interview!\n")
        input("Oh! There is an umbrella over here!\nI'll take it...\n")
        input("Ouch! I tripped!\nMy house is a mess...\nI will clean it!\nAfter the Job Interview, that is!\n")
        input("Quick, quick, quick!\nOkay, here I am in front of my ugly house's door.\n")
        input("I'm applying for Python Developer at DidgeridoooooProdsAndApps.\nI must be fast if I want that damn job!\n")
        input("No, no, no!\nMy car is not working and there are no buses today!\nI don't have enough money for a cab.\n")
        input("I must run then.\nDang it! The wind pushed my umbrella away!\nI'm all wet!\n")
        input("Am I going to be able to get there?\n")
        input("[30 MINUTES LATER]\n")
        input("I arrived! C'mon, c'mon, c'mon...\nWhere is it?\nWhere is his office?\n")
        input("I think I'm lost!\nNo, I'm not!!!\nYay, there is a map over there...\n")
        input("Upper floor? Okidoki!\n")
        input("I'm here, sir!\n")
        input("[BUSINESS OWNER] Sorry, too late!\n")
        input("They already hired someone...\n")
        input("All this for nothing...\nWhy?\nWhy do I exist?\nI always fail!\n")
        input("[BUSINESS OWNER] Wrong.\nThere is something you never fail to do and that is...\n")
        input("What? What is it?\n")
        input("[BUSINESS OWNER] The only one thing where you never fail...\nIs to dissapoint!\n")
        input("I'm going home...\n[At HOME] Bobby (the dog), wassup fella?\n")
        input("I didn't get the job but whatever...\nI'm kinda sad, you know...\n")
        input("I hope my life gets betteeeeeeer...\n[TRIPPED DOWN THE STAIRS]\nB-b-obby...\n[BLACKS OUT]\n")
        input("Find out what happens next when Chapter 2 launches (next update)!\n")
    elif number == 2:
        input("Chapter 002\n=================\n")
        input("[AT THE HOSPITAL] Where... where am I?\n")
        input("[NURSE] Well, you fell down the stairs and hit your head on the door...\n")
        input("I... I gotta go...\n")
        input("[NURSE] Sorry, but you'll have to stay...\nYou need to rest!\n")
        input("She's gone! Goodbye, you fools! I'm leaving!\nCareful... I don't want to fall through this window...\nThankfully, we are Floor 1 only and the building is not that high...\n")
        input("[AT HOME] Bobby?? Yeah, who's a really cute doggy? It's you!!\n")
        input("Well, now Imma sit and code Python... Wait...\n")
        input("I have an idea!\nI'm gonna hack Didgeridoo!!!\n")
        input("They will realize they made the worst mistake of their companie's lifetime.\n")
        input("And I'll be accepted!\nYes, who said I never fail to dissapoint??\n")
        input("[EVIL LAUGHS] Ahahahahahahahahah!\nDidgeridoo will be mine...\n")
        input("But first I should probably learn how to hack with Python...\n")
        input("Find out what happens next when Chapter 3 launches (next update)!\n")
    else:
        quit()


def startUpGame():
    clear()
    print('Just imagine what is being said and relax that way!\n')
    startUp = int(input('Hit ENTER to skip a sentence!\nCurrently available chapters: 1 and 2\nType the number of the Chapter you would like to start with: '))
    clear()
    gameEngine(startUp)

'''   
if __name__ == '__main__':
    startUpGame()
'''