from typing import Any, Callable, SupportsFloat
import requests, os, sys
from pygame import mixer
from colorama import Fore
from datetime import datetime
from simple_webbrowser import BuildSearchURL

def clamp(_val: SupportsFloat, _min: SupportsFloat, _max: SupportsFloat) -> SupportsFloat:
    if _val < _min:
        return _min
    
    if _val > _max:
        return _max
    
    return _val

class SoundRoom:
    def __init__(self, _globs):
        self.GLOBALS = _globs

        mixer.init()
        self.GLOBALS['s'].clear()

        self.CHANNEL = mixer.music

        self.cur_snd: mixer.Sound | None = None
        
        self.cur_file: str = ''

        self.help_msg = f"""{Fore.YELLOW} ---- SOUNDROOM ---- {Fore.RESET}
{Fore.MAGENTA}load <path>{Fore.RESET} - Load the file located at <path>
{Fore.BLUE}unload{Fore.RESET} - Unload the currently loaded file
{Fore.CYAN}play <[loops]>{Fore.RESET} - Play the currently loaded file from the beggining with <[loops]> amount of loops. <[loops]> is an integer and an optional parameter and it's default value is 0 (a.k.a. play the music one time only)
{Fore.GREEN}pause{Fore.RESET} - Pause the music
{Fore.CYAN}unpause{Fore.RESET} - Unpause the paused music. This starts playing from the time where the music was paused last.
{Fore.BLUE}stop{Fore.RESET} - Stop the current music
{Fore.MAGENTA}volume <val>{Fore.RESET} - Set the volume to <val>, a float (decimal) between 0 and 1, where 1 is 100%. This doesn't affect the system, just the Sound Room.
{Fore.BLUE}q{Fore.RESET} - Leave the Sound Room, without unloading the current file. This is an alias for quit, leave, exit and logout.
{Fore.CYAN}help{Fore.RESET} - Display this help message
{Fore.GREEN}clear{Fore.RESET} - Clear the screen. Alias for cls.
{Fore.CYAN}status{Fore.RESET} - Check if a music is being played right now
"""
        self.LEAVE_CMDS: tuple[str] = (
            "q",
            'quit',
            'leave',
            'exit',
            'logout'
        )

        self.run()

    def run(self) -> bool:
        while True:
            write = self.GLOBALS['s'].print

            __a = input(f"{Fore.YELLOW}>>> {Fore.RESET}").strip()
            __b = __a.lower()

            if __b in self.LEAVE_CMDS:
                return self.__leave()

            if __b == 'unload':
                if self.CHANNEL.get_busy():
                    write(f"{Fore.RED}Please stop the current music first.{Fore.RESET}\n\n")
                    continue
                
                self.CHANNEL.unload()               
                write(f"{Fore.YELLOW}PRO TIP: Loading a music automatically unloads the current one.{Fore.RESET}\n\n")
                write(f"{Fore.GREEN}The current music has been unloaded.{Fore.RESET}\n\n")

            elif __b.startswith("load"):
                try:
                    self.cur_file = new_path = __a[5:]
                    
                except Exception:
                    write(f"{Fore.RED}Invalid syntax for the 'load' command, missing the path argument.{Fore.RESET}\nCorrect use would be: 'load /path/to/file.example'.\n\n")

                else:
                    if not os.path.exists(new_path) or os.path.isdir(new_path):
                        write(f"{Fore.RED}'{new_path}' doesn't seem to be a valid file.{Fore.RESET}\n\n")
                        continue
                    
                    if self.CHANNEL.get_busy():
                        write(f"{Fore.RED}Please stop the current music first.{Fore.RESET}\n\n")
                        continue

                    self.CHANNEL.unload()
                    self.CHANNEL.load(new_path)
                    
                    write(f"{Fore.GREEN}'{new_path}' has been loaded :){Fore.RESET}\n\n")

            elif __b == "clear" or __b == 'cls':
                self.GLOBALS['s'].clear()

            elif __b.startswith("play"):
                try:
                    num_loops: int = int(__a[5:])
                    
                except Exception:
                    num_loops: int = 0
                
                if self.CHANNEL.get_busy():
                    write(f"{Fore.RED}A music is being played. Stop it before playing another one.{Fore.RESET}\n\n")
                    continue
                    
                try:
                    self.CHANNEL.play(num_loops)
                    
                except Exception as e:
                    write(f"{Fore.RED}Couln't play current file ('{self.cur_file}') due to error:\n{Fore.RESET}{e}\n\n")
                
                else:
                    write(f"{Fore.GREEN}Alright, enjoy the music :D{Fore.RESET}\n\n")
                
                finally:
                    continue
                
            elif __b == 'stop':
                if not self.CHANNEL.get_busy():
                    write(f"{Fore.RED}Nothing is being played right now.{Fore.RESET}\n\n")
                    continue
                    
                self.CHANNEL.stop()
                write(f"{Fore.MAGENTA}The music has been stopped.{Fore.RESET}\n\n")
                
            elif __b == 'pause':
                self.CHANNEL.pause()
                write(f"{Fore.CYAN}The music has been paused.{Fore.RESET}\nUse 'unpause' to continue from where you paused it.\n\n")
                
            elif __b == 'unpause':
                self.CHANNEL.unpause()
                write(f"{Fore.GREEN}Alright, enjoy the music :D{Fore.RESET}\n\n")
                
            elif __b.startswith('volume'):
                try:
                    vol = clamp(float(__a[7:]), 0, 1)
                    
                except Exception:
                    vol = self.CHANNEL.get_volume()
                
                self.CHANNEL.set_volume(vol)
                
            elif __b == 'status':
                __status = self.CHANNEL.get_busy()
                __c = Fore.GREEN
                    
                if not __status:
                    __c = Fore.RED
                
                write(f"Something is being played: {__c}{__status}{Fore.RESET}\n\n")
                
            elif __b == 'help':
                write(f"{self.help_msg}\n\n")
            
            else:
                write(f"{Fore.RED}This command doesn't seem to exist or was used in a wrong way.{Fore.RESET}\nUse 'help' to... well, get help on how to use the Sound Room.\n\n")

    def __leave(self) -> bool:
        self.CHANNEL.stop()
        mixer.quit()
        self.GLOBALS["go_to"](self.GLOBALS['PACKED'])
        return True
