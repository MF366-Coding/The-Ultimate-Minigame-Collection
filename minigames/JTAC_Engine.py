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
UI_BORDER: str = ""
FPS: int = 60
WINDOW_WIDTH = 80
WINDOW_HEIGHT = 25
# Engines (values not accurate to real life)
BaseEngine: tuple[int, int] = (2, 0.2)
# yay

def HideCursor():
    print("\033[?25l")

def ShowCursor():
    print("\033[?25h")

class ScreenClass:
    _f: list[str] = None
    fill_char: str = None
    ui_border: str = None

    def __init__(self):
        global WINDOW_WIDTH, WINDOW_HEIGHT
        # Hey
        self.fill_char = " "
        self._f = [self.fill_char] * (WINDOW_HEIGHT * WINDOW_WIDTH)

    def Clear(self):
        self._f = [self.fill_char] * (WINDOW_HEIGHT * WINDOW_WIDTH)

    def Fill(self, char: str):
        self._f = [char] * (WINDOW_HEIGHT * WINDOW_WIDTH)

    def Show(self):
        for char in enumerate(self._f):
            print(char[1], end="")
            if (char[0] + 1) % 80 == 0:
                print("\n", end="")

    def Draw(self, string: str, x: int, y: int, color: str):
        # NEWLINES ACCEPTED!
        _stuff = string.split("\n")
        _y = y
        for row in _stuff:
            _x = x
            for char in row:
                if _x == x:
                    self._f[_x + _y * WINDOW_WIDTH] = color + char
                else:
                    self._f[_x + _y * WINDOW_WIDTH] = char
                _x += 1
            self._f[(_x - 1) + _y * WINDOW_WIDTH] += "\033[0m"
            _y += 1

Screen: ScreenClass = ScreenClass()

def LoadTitles():
    global TITLE, UI_BORDER
    with open( os.path.join(os.path.dirname(__file__), 'JTAC_Titles.txt'), "rt", encoding="UTF-8" ) as File:
        for _ in range(8): TITLE += File.readline()
        _temp = []
        for _ in range(25): _temp.append(File.readline().replace("\n", ""))
        UI_BORDER = "\n".join(_temp)

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

        Screen.Draw(UI_BORDER, 0, 0, "\033[97m")
        # Test thing to blit
        Screen.Draw("Hello\nHi", random.randint(1, 2), random.randint(1, 2), "\033[33m")
        Screen.Draw("Bruh", random.randint(5, 9), random.randint(9, 12), "\033[31m")
        Screen.Draw("A..\n.B.\n..C", random.randint(15, 16), random.randint(17, 21), "\033[36m")

def JTAC():
    global clear, FPS, Screen
    clear()

    World: WorldClass = WorldClass()
    Clock = pygame.time.Clock()

    HideCursor()

    while True:
        Clock.tick(FPS)

        World.Render()

        Screen.Show()

        Screen.Clear()

def RunGame(_tumc_globs: dict):
    global TITLE, clear
    # Yep
    if clear is None: clear = _tumc_globs["s"].clear
    # Load shit
    LoadTitles()
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