import importlib.machinery, os

def load_module_from_source(module_name: str, source_path: str):
    loader = importlib.machinery.SourceFileLoader(module_name, source_path)
    spec = importlib.util.spec_from_loader(module_name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module

PongEngine = load_module_from_source("PongEngine", os.path.join(os.path.dirname(__file__), "PongEngine.py"))

class Pong:
    def __init__(self, *options) -> None:
        self.options = options
    
    def run(self):
        PongEngine.RunPong()
        
    def pack(self):
        self.run()
