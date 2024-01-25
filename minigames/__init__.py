
# /-/ import importlib.machinery, os, keyboard, random
from typing import Any # /-/, Literal
# /-/ from pygame import mixer
import tracemalloc
import time
import minigames.PongEngine as PongEngine

tracemalloc.start()

'''
def load_module_from_source(module_name: str, source_path: str):
    loader = importlib.machinery.SourceFileLoader(module_name, source_path)
    spec = importlib.util.spec_from_loader(module_name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module

PongEngine = load_module_from_source("PongEngine", os.path.join(os.path.dirname(__file__), "PongEngine.py"))
'''

class Pong:
    def __init__(self, _globs: dict[str, Any]) -> None:
        self.GLOBALS = _globs
        self.run()
    
    def run(self):
        PongEngine.RunPong(self.GLOBALS)

class ClickerGame:
    def __init__(self, _globs: dict[str, Any]):
        self.GLOBALS = _globs
        
        try:
            self.clicks: int = self.GLOBALS['settings']['clicker']['clicks']
            
        except Exception:
            self.clicks: int = 0
            
        self.LOGOUT_METHODS: tuple[str] = ('q', 'exit', 'logout', 'quit', '...')
        self.BOOL_STR: dict[str, bool] = {
            'y': True,
            'n': False
        }
        
        self.GLOBALS["s"].clear()
        self.run()
    
    def run(self) -> None:
        while True:
            if self.clicks > 1000:
                time.sleep(0.25)
                
            elif self.clicks < 100:
                time.sleep(0.35)
                
            else:
                time.sleep(0.30)
            
            __a = input(f"{self.clicks} clicks - Hit ENTER!").lower()
            
            self.GLOBALS['s'].print('\033[H')
            
            if __a in self.LOGOUT_METHODS:
                __b = input("Would you like to save your clicks?").lower()[:1]
                
                if __b not in self.BOOL_STR.keys():
                    __b = True
                    
                else:
                    __b = self.BOOL_STR[__b]
                
                if __b:
                    self.GLOBALS['settings']['clicker'] = {"clicks": self.clicks}
                    self.GLOBALS['save_settings'](self.GLOBALS['settings'])
                
                self.leave()
                break
            
            self.clicks += 1
                
    def leave(self) -> bool:
        self.GLOBALS["s"].clear()
        self.GLOBALS["go_to"](self.GLOBALS['PACKED'])
        return True
