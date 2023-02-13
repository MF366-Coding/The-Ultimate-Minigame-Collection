# By Norb#1414 (Github: https://github.com/norbcodes)

# Import the goodies!
from clsCmd import clear
from math import radians, degrees
from random import randint
from time import sleep
import keyboard

# CONSTANTS
FPS = 10
TITLE = ''
NUMBERS = []

def LoadText():
    global TITLE
    txt = open('PongTitles.txt', 'rt', encoding='UTF-8')
    for x in txt.readlines(9): TITLE += x

class World:
    P1_pad_y = None  # Initialize during object creation
    P2_pad_y = None
    Pad_x = 4   # Both pads are 4 units away from border
    Ball_X = None
    Ball_Y = None
    Ball_Vel = [None, None]
    MapW = 81
    MapH = 21

    StartPrompt = None

    def __init__(self):
        self.P1_pad_y = self.MapH//2
        self.P2_pad_y = self.MapH//2
        self.Ball_Y = self.MapH//2
        self.Ball_X = self.MapW//2
        self.Ball_Vel = [1, 2]
        self.StartPrompt = True

    def Render(self):
        clear()
        print(' ' + '-' * self.MapW)
        output = [' ' for _ in range(self.MapH * self.MapW)]

        # Render pads
        # Pad 1
        pos = self.P1_pad_y-2
        for x in range(5):
            output[self.Pad_x + ((pos+x) * self.MapW)] = '▉'

        # Pad 1
        pos = self.P2_pad_y - 2
        for x in range(5):
            output[(self.MapW - self.Pad_x - 1) + ((pos + x) * self.MapW)] = '▉'

        # Render center line
        LineX, LineY = self.MapW//2, 0
        for x in range(self.MapH):
            output[LineX + (LineY * self.MapW)] = '|'
            LineY += 1

        # Render ball
        output[self.Ball_X + (self.Ball_Y * self.MapW)] = '0'

        indx = 0
        for x in output:
            indx += 1
            if indx % self.MapW == 0:
                print(f'{x}|')
                continue
            if indx % self.MapW == 1:
                print(f'|{x}', end='')
                continue
            print(x, end='')
        print(' ' + '-' * self.MapW)

    def AdvanceBall(self):
        if self.Ball_Y > self.MapH-2 or self.Ball_Y < 1:
            self.Ball_Vel[0] *= -1

        if self.Ball_X > self.MapW-2 or self.Ball_X < 2:
            self.Ball_Vel[1] *= -1

        if self.Ball_X not in range(12, self.MapW - 12):
            if self.Ball_X > self.MapW//2:
                if self.Ball_X > (self.MapW - self.Pad_x - 4) and self.Ball_Y in range(self.P2_pad_y-2, self.P2_pad_y+2):
                    self.Ball_Vel[1] *= -1
            else:
                if self.Ball_X < self.Pad_x + 4 and self.Ball_Y in range(self.P1_pad_y-2, self.P1_pad_y+2):
                    self.Ball_Vel[1] *= -1

        self.Ball_Y += self.Ball_Vel[0]
        self.Ball_X += self.Ball_Vel[1]

    def MovePad(self, which, dir):
        if which:
            if self.P1_pad_y + (1 if dir else -1) in range(2, self.MapH-2):
                self.P1_pad_y += 1 if dir else -1
        else:
            if self.P2_pad_y + (1 if dir else -1) in range(2, self.MapH - 2):
                self.P2_pad_y += 1 if dir else -1

if __name__ == '__main__':
    gameRunning = True
    World = World()
    World.Render()
    #       W      S      UP     DOWN
    KEYS = [False, False, False, False]
    while gameRunning:
        sleep(1/FPS)

        KEYS = [False, False, False, False]
        if keyboard.is_pressed('W'):
            KEYS[0] = True
        if keyboard.is_pressed('S'):
            KEYS[1] = True
        if keyboard.is_pressed('UP'):
            KEYS[2] = True
        if keyboard.is_pressed('DOWN'):
            KEYS[3] = True

        if KEYS[0]:
            World.MovePad(True, False)
        if KEYS[1]:
            World.MovePad(True, True)
        if KEYS[2]:
            World.MovePad(False, False)
        if KEYS[3]:
            World.MovePad(False, True)

        World.Render()
        World.AdvanceBall()