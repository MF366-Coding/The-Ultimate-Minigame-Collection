import imp, os

PongEngine = imp.load_source("PongEngine.py", os.path.join(os.path.dirname(__file__), "PongEngine.py"))

class Pong:
    def __init__(self, *options) -> None:
        self.options = options
    
    def run(self):
        PongEngine.RunPong()
