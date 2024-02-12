# By Norb#1414 (GitHub: https://github.com/norbcodes)

# JOURNEY TO ALPHA CENTAURI
# A minigame where you have to travel the full 4.2465 light years to get from Earth to the Alpha Centauri system.
# Upgrade your ship by getting better engines!
# This is an idle game, meaning time passes *even after the game is closed.*

# Screen is 80x15 characters big.

import os
import sys
import time

clear = None

# Constants
_ALPHA_CENTAURI: int = 40_174_991_951_811_150  # meters
TITLE: str = ""
FPS: int = 60
# Engines (values not accurate to real life)
BaseEngine: tuple[int, int] = (2, 0.2)
# yay

def LoadTitle():
    global TITLE
    with open( os.path.join(os.path.dirname(__file__), 'JTAC_Titles.txt'), "rt", encoding="UTF-8" ) as File:
        for _ in range(8): TITLE += File.readline()

class Engine:
    Power: int = None  # Acceleration per second
    Consumption: int = None  # Fuel consumption per second

    def __init__(self, eng_stats: tuple[int, int]):
        self.Power, self.Consumption = eng_stats[0], eng_stats[1]

class PlayerClass:
    X: int = None
    Fuel: int = None
    MaxFuel: int = None
    CurrentUpgrades: dict = None

    def __init__(self, load_from: str = None):
        global BaseEngine
        # INIT BITCHHHHH
        self.X = 0  # On Earth!
        self.Fuel, self.MaxFuel = 100, 100  # Base fuel
        self.CurrentUpgrades = {
            "Engine": Engine(BaseEngine)
        }

class WorldClass:
    Player: PlayerClass = None
    Distance: int = None

    def __init__(self):
        global _ALPHA_CENTAURI
        # INIT!!!!
        self.Player = PlayerClass()
        self.Distance = _ALPHA_CENTAURI

def JTAC():
    global clear, FPS
    World: WorldClass = WorldClass()

    while True:
        time.sleep(1/FPS)

def RunGame(_tumc_globs: dict):
    global TITLE, clear
    # Yep
    if clear is None: clear = _tumc_globs["s"].clear
    # Load shit
    LoadTitle()
    # Play!
    JTAC()

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