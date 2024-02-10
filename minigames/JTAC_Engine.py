# By Norb#1414 (GitHub: https://github.com/norbcodes)

# JOURNEY TO ALPHA CENTAURI
# A minigame where you have to travel the full 4.2465 light years to get from Earth to the Alpha Centauri system.
# Upgrade your ship by getting better engines!
# This is an idle game, meaning time passes *even after the game is closed.*

import os
import sys

clear = None

# Constants
DISTANCE: int = 40174991951811150
TITLE: str = ""
# yay

def LoadTitle():
    global TITLE
    with open( os.path.join(os.path.dirname(__file__), 'JTAC_Titles.txt'), "rt", encoding="UTF-8" ) as File:
        for _ in range(8): TITLE += File.readline()

def RunGame(_tumc_globs: dict):
    global TITLE, clear

    # Yep
    if clear is None: clear = _tumc_globs["s"].clear

    LoadTitle()

if __name__ == '__main__':
    # THIS RUNS ONLY WHEN THIS FILE IS RAN AS A STANDALONE SCRIPT
    def _c():
        if sys.platform == "linux" or sys.platform == "darwin":
            clearingCommand = 'clear'
            os.system(clearingCommand)
        elif sys.platform == "win32":
            clearingCommand = 'cls'
            os.system(clearingCommand)
        else:
            os.system("clear")
    clear = _c
    del _c
    # Run
    RunGame( {"go_to": ""} )