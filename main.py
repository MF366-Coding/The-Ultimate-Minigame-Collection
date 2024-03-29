'''
Main TUMC code and some tools/minigames/extras by: MF366

GitHub       | YouTube
MF366-Coding | @mf_366

Hope you enjoy this little game!

More minigames and tools to come ASAP.
'''

# [i] Importing the needed modules
import random, platform, os, sys
import simple_webbrowser as swb
import minigames, tools, extras
from setting_manager import get_settings, save_settings
from colorama import Fore, Back, Style
from typing import Callable, Any, Literal, Iterable

def clamp(val: int | float, _min: int | float = 0, _max: int | float = 100) -> int | float:
    if val < _min:
        return _min
    
    if val > _max:
        return _max
      
    return val

ASCII_TITLES: list | None = []

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "titles.txt"), "r", encoding="utf-8") as titles_file:
    ASCII_TITLES = [line for line in titles_file.readlines()]
    titles_file.close()

settings: dict[str, Any] | None = get_settings()

class Stack:
    def __init__(self, initial_values: list | tuple = ()):
        self.items = []

        if len(initial_values) > 0:
            for value in initial_values:
                self.items.append(value)

    def __str__(self) -> str:
        return str(self.items)

    def __len__(self) -> int | float | str | Any:
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self) -> Any:
        """
        Basically, calls the built-in len method
        """
        return len(self.items)

class Screen:
    def __init__(self, history_stack: Stack, prog: str, license_info: str | None = None, colorama_props: list | tuple = (Fore.RESET, Back.RESET, Style.RESET_ALL)) -> None:
        """
        Initialises a Screen class

        Args:
            self: an instance of the Screen class
            history_stack: Stack object where the history of lines printed will be kept
            prog (str): The title of the program
            (optional) license_info (str | None): Info about the LICENSE of the program that displays, defaults to None
            (optional) colorama_props (list | tuple): A list of properties to pass to colorama, defaults to all blank

        colorama_props (optional, tuple | list):
            index 0 (str): Foreground color
            index 1 (str): Background color
            index 2 (str | Any): Style to apply
        """
        self.prog_name = prog
        self.license_info = license_info
        self.fg_color = colorama_props[0]
        self.bg_color = colorama_props[1]
        self.style_colorama = colorama_props[2]
        self.history = history_stack
        self.platform = None
        
        self.COLORMAPS_ORIG = [(Fore.RED, Fore.LIGHTRED_EX), (Fore.BLUE, Fore.LIGHTBLUE_EX), (Fore.GREEN, Fore.LIGHTGREEN_EX), (Fore.CYAN, Fore.LIGHTCYAN_EX), (Fore.MAGENTA, Fore.LIGHTMAGENTA_EX), (Fore.YELLOW, Fore.LIGHTYELLOW_EX)]
        random.shuffle(self.COLORMAPS_ORIG)
        self.COLORMAPS = self.COLORMAPS_ORIG[:]

        if sys.platform == "win32":
            self.platform = "mswin"
            # [i] win32 is the sys codename for MS Windows

        elif sys.platform == "linux" or sys.platform == "darwin":
            self.platform = "unix"
            # [i] since Unix based OSes use the clear command instead of cls, they get combined
            # [i] darwin is the sys codename for Apple's MacOS

        elif sys.platform == "linux2":
            self.platform = "oldlinux"
            # [i] linux2 is the sys codename for Python 2 powered Linux
            # [!?] since it is mostly deprecated, I only add it here for compatibility purposes

        else:
            self.platform = "unidentified"
            # [i] in case the platform is not one of the above, we won't clear the screen
            # [!?] instead, we will insert a bunch of newlines

        self.clear()
        self.print(f"{self.bg_color}{self.fg_color}{self.style_colorama}{self.prog_name}")

        if self.license_info != None:
            self.print(f"\n{Back.RESET}{Style.RESET_ALL}{self.fg_color}{self.license_info}{Fore.RESET}")

        return

    def print(self, __s: str | Any, __m: bool = False) -> int:
        """
        Internal function.
        """
        
        if __m:
            self.history.push(str(__s))

        return sys.stdout.write(str(__s))
    
    def write(self, abc: str, *params: bool) -> int:
        """
        Internal function.
        """
        if len(params) == 0:
            params = (False)
        
        return self.print(abc, params[0])
    
    def print_ascii(self, __list: Iterable[str], __ind: int, height: int = 6, __m: bool = True) -> int:
        """
        print_ascii prints a decorated ASCII art based on an iterable containing them

        Args:
            __list (Iterable[str]): the list where all the ASCII art, splitted by the \\n escape character.
            __ind (int): the starting index.
            height (int): when should the current ASCII art end. The index is converted to __ind + height
            __m (bool, optional): should the current ASCII art be saved in the stdout memory? Defaults to True.

        Returns:
            int: the value of the stdout.write operation
        """
                    
        # /-/ COLORMAPS = [(Fore.RED, Fore.MAGENTA), (Fore.BLUE, Fore.CYAN), (Fore.GREEN, Fore.YELLOW)]
        
        if self.COLORMAPS[0] == self.COLORMAPS_ORIG[0] and random.randint(0, 20) == 0:
            random.shuffle(self.COLORMAPS_ORIG)
            self.COLORMAPS = self.COLORMAPS_ORIG[:]
        
        color_index = 0
        cur_index = 0
        
        __lines: str = ""
        
        for i in range(int(__ind), int(__ind + height)):
            if i == int(__ind):
                self.print(self.COLORMAPS[color_index][cur_index])
            
            if clamp(cur_index, 0, 1) == 1:
                cur_index -= 1
                
            elif clamp(cur_index, 0, 1) == 0:
                cur_index += 1
                
            __lines += f"{__list[i]}{self.COLORMAPS[color_index][cur_index]}"
        
        self.COLORMAPS.append(self.COLORMAPS.pop(color_index))
        
        self.print_lines(__lines.split("\n"), "\n", True)
        
        return self.print(f"\n{Fore.RESET}")
        
    def print_lines(self, __lines: Iterable[str], __sep: str = "\n", __m: bool = False):
        """
        Internal function.
        """
        
        for line in __lines:
            self.print(line, __m)
            self.print(__sep)

    def _leave(self, __status = None) -> None:
        """
        Internal function.
        """
        
        sys.exit(__status)
        
    def pack(self, *args) -> None:
        """
        Internal function.
        """
        
        self._leave()
    
    def exit(self) -> None:
        """
        Internal function.
        """
        
        self._leave()
    
    def get_details(self) -> tuple[str]:
        """
        get_platform_data returns some data about the current OS

        It uses `sys`, `os` and `platform` for this purpose.

        Data by tuple index:
            0. Platform Name (either `mswin`, `unix`, `oldlinux` or `unidentified`; given by `Screen.platform`)
            1. Platform Name (given by `os.name`)
            2. Platform Name (either `win32`, `linux`, `linux2`, `darwin`, ...; given by `sys.platform`)
            3. OS Bitness (either `32bit` or `64bit`; given by `platform.architecture()[0]`)
            4. `platform.architecture()[1]`
            5. Python Executable (an absolute path; given by `sys.executable`)
            6. Machine Type (e.g. 'i386'; given by `platform.machine()`)

        Returns:
            tuple[str]: all the data above, all of it in a form of string, packed as a tuple
        """
        
        __pl = platform.architecture()
        
        return (self.platform, os.name, sys.platform, __pl[0], __pl[1], sys.executable, platform.machine())        
    
    def clear(self):
        """
        clear clears the terminal screen.
        """
        
        def unix_clear():
            """
            unix_clear clears the screen the Linux/Darwin (macOS) way.
            """
            os.system("clear")

        def win_clear():
            """
            win_clear clears the screen the Win32 (Microsoft Windows) way.
            """
            os.system("cls")

        def other_clear():
            """
            other_clear clears the screen by adding 150 newlines
            """
            sys.stdout.write("\n"*150)

        match self.platform:
            case 'mswin':
                win_clear()
                
            case 'unix':
                unix_clear()
                
            # [!] Compatibility with Linux (python 2) has ended and so it will be treated as Unidentified OS
                
            case _:
                other_clear()

class MenuIsFinal(Exception): ...
class CommandNotFound(Exception): ...
class MenuMustBeFinal(Exception): ...

PACKED = None

class Menu:
    def __init__(self, screen_obj: Screen, menu_type: Literal["start", "sub"], title: int, prev_menu = None, subtitle: str = "", description: str = "") -> None:
        """
        __init__ for Menu class

        Args:
            screen_obj (Screen): an instance of the Screen object
            menu_type (str, either "start" or "sub"): the type of the menu. If "start", then that's the starting point and going back should exit the app. Else, it should go to the previous menu given by `prev_menu`
            title (int): the index of the ASCII title to print
            prev_menu (Menu, optional): the previous menu that gets called when going back. Defaults to None. If not a Menu object and `menu_type` is sub, the `menu_type` argument will be overwritten.
            subtitle (str, optional): a short subtitle for the menu. Defaults to an empty string.
            description (str, optional): a short description about the menu. Defaults to an empty string.
        """
        
        self._screen = screen_obj
        self.title = title
        self.subtitle = subtitle
        
        if menu_type == "start" or type(prev_menu) == type(None):
            self.prev_menu = self._screen
            
        else:
            self.prev_menu = prev_menu
        
        self.description = description
        self._commands: list[list] = []
        self.__final = False
        return

    def add_command(self, name: str, menu, _type: Literal["menu", "minigame", "tool", "extra", "info"]):
        """
        add_command adds a new command to the Menu

        Args:
            name (str): the name of the command
            menu (Menu): submenu that should be called
            _type (either 'menu' or 'minigame'): if the command refers to a minigame or to a menu/Screen object
            
        For _type, 'tool', 'extra' and 'info' are also allowed but they all refer to 'minigame'.
        """
        
        if self.__final:
            raise MenuIsFinal("Menu has been set to final and can't be changed.")
        
        if _type != 'menu':
            _type = 'minigame'
        
        self._commands.append([name, menu, _type])

    def command_index(self, name: str) -> int:
        index: int = 0

        for command in self._commands:
            if command[0] == name:
                return index
            
            index += 1

        raise CommandNotFound("Could not find the command.")
    
    def get_name(self, __ind: int) -> str:
        return self._commands[__ind][0]
    
    def _call_command(self, __ind: int):       
        if self._commands[__ind][2] == 'minigame':
            a = self._commands[__ind][1](globals())
            return a
        
        return self._commands[__ind][1].pack()
    
    def final(self) -> bool:
        if not self.__final:
            self.__final = True
            
            if self.prev_menu == self._screen:
                self._commands.append(["Exit", self.prev_menu, "menu"])
                
            else:
                self._commands.append(["Go back", self.prev_menu, "menu"])            
            
            return self.prev_menu
        
        raise MenuIsFinal("The Menu is already in its final state.")
    
    def finalize(self) -> bool:
        return self.final()
    
    def get_previous_menu(self) -> Any:
        return self.prev_menu
    
    def get_prev(self):
        return self.get_previous_menu()
    
    def pack(self, *args):
        global settings, PACKED
        
        settings = get_settings()
        
        if not self.__final:
            raise MenuMustBeFinal("The Menu must be set as final before packing.")
        
        PACKED = self
        
        self._screen.clear()
        
        self._screen.print_ascii(ASCII_TITLES, self.title)
        self._screen.print_lines((self.subtitle, self.description))
        
        x = 0
        
        for command in self._commands:
            if command == self._commands[-1]:
                self._screen.print(f"{Fore.RED}[{x}]{Fore.RESET} {command[0]}\n")
                break
            
            self._screen.print(f"{Fore.YELLOW}[{x}]{Fore.RESET} {command[0]}\n")
            x += 1
        
        try:
            tag = int(input("\nRun command: "))

            self._call_command(tag)
            
        except (TypeError, IndexError, ValueError):
            self.pack()
        
    def __len__(self):
        return len(self._commands)
    
    def __str__(self) -> str:
        return ASCII_TITLES[self.title]

def go_to(_menu: Menu | Screen):
    return _menu.pack()

h = Stack()
t = Stack()
s = Screen(h, "The Ultimate Minigame Collection", "Copyright (C) 2024  MF366", (Fore.YELLOW, Back.RESET, Style.BRIGHT))

# [!!] This is gonna be organized tomorrow! (hopefully!)
start_menu = Menu(s, "start", 0, None, "The Ultimate Minigame Collection featuring useful tools and extras as well.")
minigame_menu = Menu(s, "sub", 6, start_menu, "Minigames are cool. Here are some of ours.", "TUMC's original and new minigames.")
tools_menu = Menu(s, "sub", 12, start_menu, "Need a tool? Find one in here!", "Tools to help out with pretty much everything, from downloading YouTube videos and playlists to finding more information about your OS.")

# [*] Adding commands and submenus
minigame_menu.add_command("Commandline Pong by Norb", minigames.Pong, "minigame")
minigame_menu.add_command("Clicker Game (BETA)", minigames.ClickerGame, "minigame")

tools_menu.add_command("Sound Room", tools.SoundRoom, "minigame")

# [*] Mark submenus as final
minigame_menu.final()
tools_menu.final()

# [*] Finish Starting Menu setup
start_menu.add_command("Minigames", minigame_menu, "menu")
start_menu.add_command("Tools", tools_menu, "menu")
start_menu.final()
start_menu.pack()

'''
class swapSentence:
    @staticmethod
    def professionalSwapper(textToSwap):
        s.clear()
        swappedText = textToSwap[::-1]
        print("Given sentence: "+textToSwap+"\nInverted sentence: "+swappedText+"\n")
        review = str(input("Is this correct?\nType 'yes' or 'no' here please: "))
        if review == 'yes':
            s.clear()
            print('Thank you!\n')
            quit()
        if review == 'no':
            print('We are sorry to hear that...\n')
            goToIssues = str(input("Would you like to report this issue?\nIf so, you need a screenshot of the output.\nType 'yes' or 'no' here please: "))
            if goToIssues == 'yes':
                simple_webbrowser.Website('https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection/issues')
                quit()

class news:
    @staticmethod
    def RunCode():
        updates = input("[ WHAT'S NEW IN TUMC? ]\nBiggest update to TUMC so far...\n\n[ Pong Minigame by Norb ]\nPlay Pong on the Command Prompt. Yes, you heard this right!!!\nNote that this only runs on Windows (we tested in Linux, but not in Mac).\nCheck README.md for more info.\n\n[ This Section ]\nYeah, that's right! Now, this app comes with a ''What's new?'' section!\n\n[ AT GITHUB ]\nFor more info, check https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection.\n\nThanks for downloading this project.\n\nMade by MF366.\n\n< Press ENTER to go to the repo. >\n< Type 'quit' and hit ENTER to quit the app. >\n\nYour choice: ")
        if updates == 'quit':
            quit()
        else:
            simple_webbrowser.Website('https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection')


class numRand:
    @staticmethod
    def easyMode():
        print("You'll have to guess what's the secret number between 0 and 100. You have a limited number of attempts.\nEasy, right? Maybe...\n")
        attempts = 7
        secret = randint(0, 100)
        for i in range(attempts):
            number = int(input("\nYour guess please: "))
            if number == secret:
                s.clear()
                print('\nWow! You won!\n')
                return True
            elif number > secret:
                print('\nTry a smaller number...')
            else:
                print('\nTry a bigger number...')
        s.clear()
        print('Sorry, you lost...\nThe number was '+str(secret)+'.\n')

    @staticmethod
    def normalMode():
        print("You'll have to guess what's the secret number between 0 and 100. You have a limited number of attempts.\nEasy, right? Maybe...\n")
        attempts = 5
        secret = randint(0, 100)
        for i in range(attempts):
            number = int(input("\nYour guess please: "))
            if number == secret:
                s.clear()
                print('\nWow! You won!\n')
                return True
            elif number > secret:
                print('\nTry a smaller number...')
            else:
                print('\nTry a bigger number...')
        s.clear()
        print('Sorry, you lost...\nThe number was '+str(secret)+'.\n')

    @staticmethod
    def hardMode():
        print("You'll have to guess what's the secret number between 0 and 100. You have a limited number of attempts.\nEasy, right? Maybe...\n")
        attempts = 3
        secret = randint(0, 100)
        for i in range(attempts):
            number = int(input("\nYour guess please: "))
            if number == secret:
                s.clear()
                print('\nWow! You won!\n')
                return True
            elif number > secret:
                print('\nTry a smaller number...')
            else:
                print('\nTry a bigger number...')
        s.clear()
        print('Sorry, you lost...\nThe number was '+str(secret)+'.\n')

    @staticmethod
    def extremeMode():
        print("You think you can play The Impossible Mode?\nLOL I bet you're not gonna make it!\n")
        attempts = 2
        secret = randint(0, 100)
        for i in range(attempts):
            number = int(input("\nYour guess please: "))
            if number == secret:
                s.clear()
                print('\nHOW??? You are truly amazing!!!\n')
                return True
            elif number > secret:
                print('\nTry a smaller number...')
            else: # Nice line
                print('\nTry a bigger number...')
        s.clear()
        print('LOL I told you you were gonna lose...\nThe number was '+str(secret)+'.\n')

class botTalker:
    @staticmethod
    def talkToCarl():
        quittingAsk = False
        quittingNumber = 0
        with open('carl.txt', 'r') as carlFile:
            carlExtract = carlFile.read()
            carlFile.close()
            carl = carlExtract.split('//')
        s.clear()
        while quittingAsk == False:
            recommendGame = str(input('Input: '))
            print('Output: '+carl[quittingNumber])
            quittingNumber += 1
            if quittingNumber == 15:
                quit()
            if recommendGame == 'quit':
                quittingAsk = True
                quit()

    @staticmethod
    def talkToAnna():
        quittingAsk = False
        quittingNumber = 0
        with open('anna.txt', 'r') as annaFile:
            annaExtract = annaFile.read()
            annaFile.close()
            anna = annaExtract.split('//')
        s.clear()
        while quittingAsk == False:
            recommendGame = str(input('Input: '))
            print('Output: '+anna[quittingNumber])
            quittingNumber += 1
            if quittingNumber == 11:
                quit()
            if recommendGame == 'quit':
                quittingAsk = True
                quit()

    @staticmethod
    def talkToZang():
        quittingAsk = False
        quittingNumber = 0
        with open('zang.txt', 'r') as zangFile:
            zangExtract = zangFile.read()
            zangFile.close()
            zang = zangExtract.split('//')
        s.clear()
        while quittingAsk == False:
            recommendGame = str(input('Input: '))
            print('Output: '+zang[quittingNumber])
            quittingNumber += 1
            if quittingNumber == 3:
                quit()
            if recommendGame == 'quit':
                quittingAsk = True
                quit()

    @staticmethod
    def talkToURMOM():
        quittingAsk = False
        quittingNumber = 0
        with open('ur-mom.txt', 'r') as urmomFile:
            urmomExtract = urmomFile.read()
            urmomFile.close()
            urmom = urmomExtract.split('//')
        s.clear()
        while quittingAsk == False:
            recommendGame = str(input('Input: '))
            print('Output: '+urmom[quittingNumber]) # Truly a really nice line
            quittingNumber += 1
            if quittingNumber == 13:
                quit()
            if recommendGame == 'quit':
                quittingAsk = True
                quit()

# Minigame Picker
if __name__ == '__main__':
    s.clear()

    with open('tumc_init.txt', 'r', encoding='utf-8') as textkoolInit:
        textkoolExtract = textkoolInit.read()
        textkoolInit.close()

    with open('player.txt', 'r', encoding='utf-8') as playerNameFile:
        playerNameExtract = playerNameFile.read()
        playerNameFile.close()

    Picker = str(input(f"{str(textkoolExtract)}\nWelcome back, {playerNameExtract}!\nPlease select a minigame/util to start with.\n\tTip: Press 'guide' to acess the manual of commands.\nYour command: "))
    if Picker == '1':
        s.clear()
        minigamePicker = str(input("Please select a minigame.\n[1] RandomGuesser\n[2] Pong CMD Edition by Norb (Check README.md before playing)\nType here please: "))
        if minigamePicker == '1':
            s.clear()
            randPicker = str(input("Select a difficulty.\n[1] Easy\n[2] Normal\n[3] Hard\n[4] Impossible\nType here please: "))
            if randPicker == '1':
                s.clear()
                numRand.easyMode()
            if randPicker == '2':
                s.clear()
                numRand.normalMode()
            if randPicker == '3':
                s.clear()
                numRand.hardMode()
            if randPicker == '4':
                s.clear()
                numRand.extremeMode()
        elif minigamePicker == '2':
            s.clear()
            PongEngine.RunPong()

    if Picker == '2':
        s.clear()
        toolPicker = str(input("Please select a tool.\n[1] SentenceInvertor\nType here please: "))
        if toolPicker == '1':
            s.clear()
            textToSwap = str(input("Type the sentence you would like to invert here please:\n"))
            s.clear()
            swapSentence.professionalSwapper(textToSwap=textToSwap)

    if Picker == '3':
        s.clear()
        extraPicker = str(input("Please select an extra option.\n[1] Jokes\n[2] What game should I play?\n[3] Talk to a bot (because I have no better stuff to do)\n[4] It's raining outside (Sad story)\nType here please: "))
        if extraPicker == '1':
            s.clear()
            print('Ready for some jooooooookes?\nHit ENTER to skip to the next joke.\nType quit to exit.\n')
            with open('jokes.txt', 'r') as jokesFile:
                jokesExtract = jokesFile.read()
                jokes = jokesExtract.split('//')
                jokesFile.close()

            quittingAsk = False

            jokeArray = []
            def regenJokes():
                global jokeArray
                jokeArray = jokes.copy()
                shuffle(jokeArray)

            while not quittingAsk:
                if len(jokeArray) == 0:
                    regenJokes()
                tellJoke = str(input(str(jokeArray.pop(randint(0, len(jokeArray)-1))+'\n')))
                if tellJoke == 'quit':
                    quittingAsk = True
                    quit()

        if extraPicker == '2':
            s.clear()
            print('I am your AI BFF.\nJk lmao How could I be friends with something like you?\nAnyways, rules are simple.\nI may have robbed some people and now...\n...well, I have to keep recommending you some games to play! (that is my punishment)\nHit ENTER to skip and quit to... well: quit!!\nDaaah... (i really dont want to do this)\nYou should play....\n')
            with open('games.txt', 'r', encoding='utf-8') as gamesFile:
                gamesExtract = gamesFile.read()
                games = gamesExtract.split('//')
                gamesFile.close()
            quittingAsk = False
            while not quittingAsk:
                recommendGame = str(input(str(games[randint(0, 33)]+'\n')))
                if recommendGame == 'quit':
                    quittingAsk = True
                    quit()
        if extraPicker == '3':
            s.clear()
            print("Welcome to BotTalker v1.1.1.\nJust select a character and you're good to start!\n")
            botTalkerInit = str(input("Select a bot to talk with.\n[1] Carl\n[2] Anna\n[3] ur mom (lol)\n[4] Mr. Zang (Awarded business man)\nType here please: "))
            if botTalkerInit == '1':
                botTalker.talkToCarl()
            elif botTalkerInit == '2':
                botTalker.talkToAnna()
            elif botTalkerInit == '3':
                botTalker.talkToURMOM()
            elif botTalkerInit == '4':
                botTalker.talkToZang()
            else:
                quit()
        if extraPicker == '4':
            s.clear()
            rain.startUpGame()
    elif Picker == '4':
        s.clear()
        setUpInfoPicker = str(input("This Python program was made by MF366.\n[1] Go to GitHub\n[2] Change Player Name\n[3] Report a bug\n[4] Recommend a new feature\n[5] What's new over here?\nType here please: "))
        if setUpInfoPicker == '1':
            s.clear()
            simple_webbrowser.Website('https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection')
            quit()
        elif setUpInfoPicker == '2':
            s.clear()
            print("Your username: "+playerNameExtract)
            newUsernamePicker = str(input("Type the new username here please: "))
            with open('player.txt', 'w', encoding='utf-8') as playerNameFile:
                playerNameFile.write(newUsernamePicker)
                print("\nYou'll have to reopen TUMC to apply the changes.")
                quit()
        elif setUpInfoPicker == '3':
            s.clear()
            print('Assign MF366-Coding and label as bug\n')
            simple_webbrowser.Website('https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection/issues/new')
            quit()
        elif setUpInfoPicker == '4':
            s.clear()
            print('Assign MF366-Coding and label as enhancement\n')
            simple_webbrowser.Website('https://github.com/MF366-Coding/The-Ultimate-Minigame-Collection/issues/new')
            quit()
        elif setUpInfoPicker == '5':
            s.clear()
            news.RunCode()
        elif setUpInfoPicker == '6':
            s.clear()
            print("I really don't think you were suppose to be able to read this but...\nI also don't care about it...\nEnjoy this useless secret!")
            quit()
'''
