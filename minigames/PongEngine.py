# By Norb#1414 (Github: https://github.com/norbcodes)

# Import the goodies!
from math import radians, degrees
from random import randint, choice
from time import sleep
import sys
from os import system, path
import keyboard

def clear():
    # Find the system
    if sys.platform == "linux" or sys.platform == "darwin":
        clearingCommand = 'clear'
        system(clearingCommand)
    elif sys.platform == "win32":
        clearingCommand = 'cls'
        system(clearingCommand)
    else:
        system("clear")

# CONSTANTS
FPS = 15
TITLE = ''
NUMBERS = []

def LoadText():
    global TITLE
    txt = open(path.join(path.dirname(__file__), 'PongTitles.txt'), 'rt', encoding='UTF-8')
    for _ in range(8): TITLE += txt.readline()
    for _ in range(10):
        temp = ''
        for z in range(5): temp += txt.readline().replace('\n', '')
        NUMBERS.append(temp)

def PrintText(text):
    print(text, end="")  # lel

class WorldClass:
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
    AI_Mode = None
    AI_Pad_Move_Count = None
    AI_Pad_Move_Dir = None

    StartPrompt = None
    VictoryCondition = False
    Winner = None  # 1 = Player 1 won, Player 2 won
    Paused = None

    def __init__(self, ai):
        self.P1_pad_y = self.MapH//2
        self.P2_pad_y = self.MapH//2
        self.Ball_Y = self.MapH//2
        self.Ball_X = self.MapW//2
        self.Ball_Vel = [1, 2]
        self.StartPrompt = True
        self.Paused = True
        self.Score = [0, 0]
        self.Winner = None
        self.BallRespawnTimer = 0
        self.AI_Mode = ai
        self.AI_Pad_Move_Count = 0

    def Render(self):
        PrintText('\033[H')
        PrintText(' ' + '-' * self.MapW + '\n')
        output = [' ' for _ in range(self.MapH * self.MapW)]

        # Render pads
        if not self.VictoryCondition:
            # Pad 1
            pos = self.P1_pad_y-2
            for x in range(5):
                output[self.Pad_x + ((pos+x) * self.MapW)] = ']'

            # Pad 2
            pos = self.P2_pad_y - 2
            for x in range(5):
                output[(self.MapW - self.Pad_x - 1) + ((pos + x) * self.MapW)] = '['

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

        if self.Paused and not self.StartPrompt:
            text = "--- PAUSED. ---"
            x, y = (self.MapW - len(text))//2 + 1, self.MapH//2
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
                PrintText(f'{x}|\n')
                continue
            if indx % self.MapW == 1:
                PrintText(f'|{x}')
                continue
            PrintText(x)
        PrintText(' ' + '-' * self.MapW + '\n')

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
                    self.Ball_Vel[0] = choice((-1, 1))
                    self.Ball_Vel[1] = choice((-2, 2))
                else:
                    self.Score[0] += 1
                    self.BallRespawnTimer = self.BallRespawnTime
                    self.Ball_Y, self.Ball_X = self.MapH // 2, self.MapW // 2
                    self.Ball_Vel[0] = choice((-1, 1))
                    self.Ball_Vel[1] = choice((-2, 2))

                if self.Score[0] == 10 or self.Score[1] == 10:
                    self.VictoryCondition = True
                    self.Winner = 1 if self.Score[0] == 10 else 2
                    self.Ball_Vel[0] = choice((-1, 1))
                    self.Ball_Vel[1] = choice((-2, 2))
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
                        if self.Ball_Y == self.P2_pad_y:
                            self.Ball_Vel[0] = 0
                        if self.Ball_Y < self.P2_pad_y:
                            self.Ball_Vel[0] = -1
                        if self.Ball_Y > self.P2_pad_y:
                            self.Ball_Vel[0] = 1
                        self.Ball_Vel[1] = -2
                else:
                    if self.Ball_X < (self.Pad_x + 3) and self.Ball_Y in range(self.P1_pad_y-3, self.P1_pad_y+3):
                        if self.Ball_Y == self.P1_pad_y:
                            self.Ball_Vel[0] = 0
                        if self.Ball_Y < self.P1_pad_y:
                            self.Ball_Vel[0] = -1
                        if self.Ball_Y > self.P1_pad_y:
                            self.Ball_Vel[0] = 1
                        self.Ball_Vel[1] = 2

        self.Ball_Y += self.Ball_Vel[0]
        self.Ball_X += self.Ball_Vel[1]

    def ProcessAI(self):
        if not self.AI_Mode:
            return

        if self.AI_Pad_Move_Count != 0:
            if self.P2_pad_y + (-1 if self.AI_Pad_Move_Dir else 1) in range(2, self.MapH - 2):
                self.P2_pad_y += -1 if self.AI_Pad_Move_Dir else 1
                self.AI_Pad_Move_Count -= 1
            else:
                self.AI_Pad_Move_Count = 0
                self.AI_Pad_Move_Dir = None
                return

            if self.AI_Pad_Move_Count == 0:
                self.AI_Pad_Move_Dir = None
            return

        if self.Ball_X > self.MapW//2:
            if self.Ball_Y > 20:
                self.AI_Pad_Move_Count += 3
                self.AI_Pad_Move_Dir = True
                return

            if self.Ball_Y < 5:
                self.AI_Pad_Move_Count += 3
                self.AI_Pad_Move_Dir = False
                return

            if self.Ball_Y > 17 or self.Ball_Y < 8:
                return

            if self.P2_pad_y < self.Ball_Y:
                if not self.AI_Pad_Move_Dir:
                    self.AI_Pad_Move_Count += abs(self.P2_pad_y - self.Ball_Y)
                    return

                self.AI_Pad_Move_Count = abs(self.P2_pad_y - self.Ball_Y) * 2
                self.AI_Pad_Move_Dir = False

            if self.P2_pad_y > self.Ball_Y:
                if self.AI_Pad_Move_Dir:
                    self.AI_Pad_Move_Count += abs(self.P2_pad_y - self.Ball_Y)
                    return

                self.AI_Pad_Move_Count = abs(self.P2_pad_y - self.Ball_Y) * 2
                self.AI_Pad_Move_Dir = True

            if self.P2_pad_y == self.Ball_Y:
                self.AI_Pad_Move_Count = randint(1, 2)
                self.AI_Pad_Move_Dir = choice((True, False))

            # smart fella this ai is

    def MovePad(self, which, dir):
        if which:
            if self.P1_pad_y + (1 if dir else -1) in range(2, self.MapH-2):
                self.P1_pad_y += 1 if dir else -1
            return
        if self.P2_pad_y + (1 if dir else -1) in range(2, self.MapH - 2):
            self.P2_pad_y += 1 if dir else -1

def RunPong(_tumc_globs: dict):
    LoadText()
    while True:
        clear()
        PrintText(TITLE + '\n')
        PrintText('Press 1 to play.\n')
        PrintText('Press 2 for info.\n')
        PrintText('Press 3 to exit.\n')

        keyboard.read_event()

        if keyboard.is_pressed('1'):
            clear()
            PrintText(TITLE + '\n')
            PrintText('Select mode:\n'
                      '[1] Player VS. Player\n'
                      '[2] Player VS. AI\n\n'
                      'Press ESC to return back to main menu.')
            keyboard.read_event()
            keyboard.read_event()

            ai_option = None
            return_back = False

            if keyboard.is_pressed('1'):
                ai_option = False
            if keyboard.is_pressed('2'):
                ai_option = True
            if keyboard.is_pressed('ESC'):
                return_back = True

            if not return_back:
                clear()
                gameRunning = True
                World = WorldClass(ai_option)
                World.Render()
                #       W      S      UP     DOWN
                KEYS = [False, False, False, False]
                # GAME LOOP START
                while gameRunning:
                    sleep(1/FPS)

                    if keyboard.is_pressed('ESC'):
                        break

                    if World.StartPrompt and World.Paused and keyboard.is_pressed('\n'):
                        World.Paused = not World.Paused
                        World.StartPrompt = False

                    if keyboard.is_pressed('P'):
                        World.Paused = not World.Paused

                    KEYS = [False, False, False, False]
                    if not World.Paused:
                        if keyboard.is_pressed('W'):
                            KEYS[0] = True
                        if keyboard.is_pressed('S'):
                            KEYS[1] = True
                        if not World.AI_Mode:
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

                        World.ProcessAI()

                        World.AdvanceBall()
                    World.Render()
                # GAME LOOP END

        if keyboard.is_pressed('2'):
            clear()
            PrintText(TITLE + '\n\n')
            PrintText('Made by Norb for MF366\'s Minigame collection.\n'
                      'Powered by Python 3.10\n'
                      'Needed modules: math, random, time, keyboard, sys (Most of these come with the Python STD.)\n'
                      '\n'
                      'This was an amazing little side project :)\n'
                      'I had much fun making this, learned a bit about the keyboard module and helped MF366.\n'
                      'Hope you\'ll have as much fun playing this as I did making this!\n'
                      '- Norb, the Dev.\n\n'
                      'Press any key to return to main menu.')
            keyboard.read_event()
            keyboard.read_event()

        if keyboard.is_pressed('3'):
            break
    
    clear()
    _tumc_globs['go_to'](_tumc_globs['PACKED'])
    