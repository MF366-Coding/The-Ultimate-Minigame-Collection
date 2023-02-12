# By Norb#1414 (Github: https://github.com/norbcodes)

# Import the goodies!
from clsCmd import clear
from math import radians, degrees
from random import randint
import pygame

pygame.init()

# CONSTANTS
FPS = 10

class World:
    P1_pad_y = None  # Initialize during object creation
    P2_pad_y = None
    Pad_x = 4   # Both pads are 4 units away from border
    Ball_X = None
    Ball_Y = None
    Ball_Angle = degrees(90)
    MapW = 81
    MapH = 20

    StartPrompt = None

    def __init__(self):
        self.P1_pad_y = self.MapH//2-1
        self.P2_pad_y = self.MapH//2-1
        self.Ball_Y = self.MapH//2
        self.Ball_X = self.MapW//2
        self.StartPrompt = True

    def Render(self):
        clear()
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
        output[self.Ball_X + (self.Ball_Y * self.MapW)] = '𝐎'

        indx = 0
        for x in output:
            indx += 1
            print(x, end='') if indx % self.MapW != 0 else print(x)

if __name__ == '__main__':
    World = World()
    World.Render()