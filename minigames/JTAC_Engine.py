# By Norb#1414 (GitHub: https://github.com/norbcodes)

# JOURNEY TO ALPHA CENTAURI
# A minigame where you have to travel the full 4.2465 light years to get from Earth to the Alpha Centauri system.
# Upgrade your ship by getting better engines!
# This is an idle game, meaning time passes *even after the game is closed.*

import os
import sys

# SHAMELESSLY COPIED <3
def clear():
    # Find the system
    if sys.platform == "linux" or sys.platform == "darwin":
        clearingCommand = 'clear'
        os.system(clearingCommand)
    elif sys.platform == "win32":
        clearingCommand = 'cls'
        os.system(clearingCommand)
    else:
        os.system("clear")

# Constants
DISTANCE: int = 40174991951811150
TITLE: str = ""
# yay

def LoadTitle():
    global TITLE
    with open( os.path.join(os.path.dirname(__file__), 'JTAC_Titles.txt'), "rt", encoding="UTF-8" ) as File:
        for _ in range(8): TITLE += File.readline()

def RunGame(_tumc_globs: dict):
    global TITLE
    LoadTitle()
    print(TITLE)

if __name__ == '__main__':
    RunGame( {"go_to": ""} )