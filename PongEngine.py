# By Norb#1414 (Github: https://github.com/norbcodes)

# Import the goodies!
from clsCmd import clear
from math import radians, degrees
from random import randint, choice
from time import sleep
import keyboard

# CONSTANTS
FPS = 15
TITLE = ''
NUMBERS = []

def LoadText():
    global TITLE
    txt = open('PongTitles.txt', 'rt', encoding='UTF-8')
    for _ in range(8): TITLE += txt.readline()
    for _ in range(10):
        temp = ''
        for z in range(5): temp += txt.readline().removesuffix('\n')
        NUMBERS.append(temp)

class World:
    P1_pad_y = None  # Initialize during object creation
    P2_pad_y = None
    Pad_x = 4   # Both pads are 4 units away from border
    Ball_X = None
    Ball_Y = None
    Ball_Vel = [None, None]
    MapW = 106
    MapH = 25
    Score = [None, None]
    BallRespawnTime = FPS * 2  # 5 seconds.
    BallRespawnTimer = None

    StartPrompt = None
    VictoryCondition = False
    Winner = None  # 1 = Player 1 won, Player 2 won
    Paused = None

    def __init__(self):
        self.P1_pad_y = self.MapH//2
        self.P2_pad_y = self.MapH//2
        self.Ball_Y = self.MapH//2
        self.Ball_X = self.MapW//2
        self.Ball_Vel = [1, 2]
        self.StartPrompt = False
        self.Paused = False
        self.Score = [0, 0]
        self.Winner = None
        self.BallRespawnTimer = 0

    def Render(self):
        clear()
        print(' ' + '-' * self.MapW)
        output = [' ' for _ in range(self.MapH * self.MapW)]

        # Render pads
        if not self.VictoryCondition:
            # Pad 1
            pos = self.P1_pad_y-2
            for x in range(5):
                output[self.Pad_x + ((pos+x) * self.MapW)] = '▉'

            # Pad 2
            pos = self.P2_pad_y - 2
            for x in range(5):
                output[(self.MapW - self.Pad_x - 1) + ((pos + x) * self.MapW)] = '▉'

        # Render center line
        LineX, LineY = self.MapW//2, 0
        for x in range(self.MapH):
            output[LineX + (LineY * self.MapW)] = '|'
            LineY += 1

        # Render ball
        if self.BallRespawnTimer == 0:
            output[self.Ball_X + (self.Ball_Y * self.MapW)] = '0'

        if self.StartPrompt:
            text = "Press Enter to play. Press ESC to quit at any time. Press P to pause."
            x, y = (self.MapW - len(text))//2, 3
            for char in range(len(text)):
                output[(x + char) + (y * self.MapW)] = text[char]

        # Render score, if Start Prompt is not shown.
        if not self.StartPrompt:
            if not self.VictoryCondition:
                score1 = NUMBERS[self.Score[0]]
                x, y = self.MapW // 2 - 7, 1
                for A in range(5):
                    for B in range(5):
                        output[x + B + ((y + A) * self.MapW)] = score1[B + (A * 5)]

                score2 = NUMBERS[self.Score[1]]
                x, y = self.MapW // 2 + 3, 1
                for A in range(5):
                    for B in range(5):
                        output[x + B + ((y + A) * self.MapW)] = score2[B + (A * 5)]

            if self.Winner == 1:
                x, y = self.MapW // 2 - 7, 1
                for A in range(5):
                    for B in range(5):
                        output[x + B + ((y + A) * self.MapW)] = NUMBERS[0][B + (A * 5)]

                x, y = self.MapW // 2 - 14, 1
                for A in range(5):
                    for B in range(5):
                        output[x + B + ((y + A) * self.MapW)] = NUMBERS[1][B + (A * 5)]

                scoreL = NUMBERS[self.Score[1]]
                x, y = self.MapW // 2 + 3, 1
                for A in range(5):
                    for B in range(5):
                        output[x + B + ((y + A) * self.MapW)] = scoreL[B + (A * 5)]

            if self.Winner == 2:
                x, y = self.MapW // 2 + 10, 1
                for A in range(5):
                    for B in range(5):
                        output[x + B + ((y + A) * self.MapW)] = NUMBERS[0][B + (A * 5)]

                x, y = self.MapW // 2 + 3, 1
                for A in range(5):
                    for B in range(5):
                        output[x + B + ((y + A) * self.MapW)] = NUMBERS[1][B + (A * 5)]

                scoreL = NUMBERS[self.Score[0]]
                x, y = self.MapW // 2 - 7, 1
                for A in range(5):
                    for B in range(5):
                        output[x + B + ((y + A) * self.MapW)] = scoreL[B + (A * 5)]

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
        if self.BallRespawnTimer != 0:
             return

        if self.Ball_Y > self.MapH-2 or self.Ball_Y < 1:
            self.Ball_Vel[0] *= -1

        if self.Ball_X > self.MapW-2 or self.Ball_X < 2:
            if not self.VictoryCondition:
                if self.Ball_X < self.MapW//2:
                    self.Score[1] += 1
                    self.BallRespawnTimer = self.BallRespawnTime
                    self.Ball_Y, self.Ball_X = self.MapH // 2, self.MapW // 2
                    self.Ball_Vel[0] *= choice((-1, 1))
                    self.Ball_Vel[1] *= choice((-1, 1))
                else:
                    self.Score[0] += 1
                    self.BallRespawnTimer = self.BallRespawnTime
                    self.Ball_Y, self.Ball_X = self.MapH // 2, self.MapW // 2
                    self.Ball_Vel[0] *= choice((-1, 1))
                    self.Ball_Vel[1] *= choice((-1, 1))

                if self.Score[0] == 10 or self.Score[1] == 10:
                    self.VictoryCondition = True
                    self.Winner = 1 if self.Score[0] == 10 else 2
                    self.Ball_Vel[0] *= choice((-1, 1))
                    self.Ball_Vel[1] *= choice((-1, 1))
                    self.Ball_Y, self.Ball_X = self.MapH // 2, self.MapW // 2
                    self.BallRespawnTimer = 0
                    return

                return
            else:
                self.Ball_Vel[1] *= -1

        if not self.VictoryCondition:
            if self.Ball_X not in range(12, self.MapW - 12):
                if self.Ball_X > self.MapW//2:
                    if self.Ball_X > (self.MapW - self.Pad_x - 4) and self.Ball_Y in range(self.P2_pad_y-3, self.P2_pad_y+3):
                        self.Ball_Vel[1] *= -1
                else:
                    if self.Ball_X < (self.Pad_x + 3) and self.Ball_Y in range(self.P1_pad_y-3, self.P1_pad_y+3):
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
    LoadText()

    gameRunning = True
    World = World()
    World.Render()
    #       W      S      UP     DOWN
    KEYS = [False, False, False, False]
    while gameRunning:
        sleep(1/FPS)

        if keyboard.is_pressed('ESC'):
            break

        if World.StartPrompt and World.Paused and keyboard.is_pressed('\n'):
            World.Paused = not World.Paused
            World.StartPrompt = False

        if keyboard.is_pressed('P'):
            World.Paused = not World.Paused

        if World.Paused:
            continue

        KEYS = [False, False, False, False]
        if keyboard.is_pressed('W'):
            KEYS[0] = True
        if keyboard.is_pressed('S'):
            KEYS[1] = True
        if keyboard.is_pressed('UP'):
            KEYS[2] = True
        if keyboard.is_pressed('DOWN'):
            KEYS[3] = True

        if World.BallRespawnTimer == 0:
            if KEYS[0]:
                World.MovePad(True, False)
            if KEYS[1]:
                World.MovePad(True, True)
            if KEYS[2]:
                World.MovePad(False, False)
            if KEYS[3]:
                World.MovePad(False, True)

        if World.BallRespawnTimer != 0:
            World.BallRespawnTimer -= 1

        World.AdvanceBall()
        World.Render()