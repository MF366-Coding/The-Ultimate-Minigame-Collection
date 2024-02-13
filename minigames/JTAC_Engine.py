# By Norb#1414 (GitHub: https://github.com/norbcodes)

# JOURNEY TO ALPHA CENTAURI
# A minigame where you have to travel the full 4.2465 light years to get from Earth to the Alpha Centauri system.
# Upgrade your ship by getting better engines!
# This is an idle game, meaning time passes *even after the game is closed.*

import pygame  # YYYIIIAAAAAAAAAAAAAHH!!!
import textwrap
import os
import sys
import random

clear = None

# Constants
_ALPHA_CENTAURI: int = 40_174_991_951_811_150  # meters
TITLE: str = ""
FPS: int = 60
WINDOW_WIDTH = 80
WINDOW_HEIGHT = 25
# Engines (values not accurate to real life)
BaseEngine: tuple[int, int] = (2, 0.2)
# yay

class ScreenClass:
    _f: list[str] = None

    def __init__(self):
        global WINDOW_WIDTH, WINDOW_HEIGHT
        # Hey
        self._f = [" "] * (WINDOW_HEIGHT * WINDOW_WIDTH)

    def Clear(self):
        self._f = [" "] * (WINDOW_HEIGHT * WINDOW_WIDTH)

    def Fill(self, char: str):
        self._f = [char] * (WINDOW_HEIGHT * WINDOW_WIDTH)

    def Show(self):
        for char in enumerate(self._f):
            print(char[1], end="")
            if (char[0] + 1) % 80 == 0:
                print("\n", end="")

    def Draw(self, string: str, x: int, y: int):
        # NEWLINES ACCEPTED!
        _stuff = string.split("\n")
        _y = y
        for row in _stuff:
            _x = x
            for char in row:
                self._f[_x + _y * WINDOW_WIDTH] = char
                _x += 1
            _y += 1

Screen: ScreenClass = ScreenClass()

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

    def Render(self):
        global WINDOW_WIDTH, WINDOW_HEIGHT, Screen

        # Bring the cursor to the top of the screen
        print("\033[H", end="")

        # Test thing to blit
        Screen.Draw("BRUH\nYou serious?\nNAAAh", random.randint(0, 1), random.randint(0, 1))

def JTAC():
    global clear, FPS, Screen
    clear()

    World: WorldClass = WorldClass()
    Clock = pygame.time.Clock()

    while True:
        Clock.tick(FPS)

        Screen.Clear()

        World.Render()

        Screen.Show()

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