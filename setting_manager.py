import json, os
from typing_extensions import Any

path_to_json = os.path.join(os.path.dirname(__file__), "settings.json")

def get_settings(__path: str = path_to_json) -> dict[str, Any] | None:
    __settings: dict | None = {}
    
    with open(__path, "r", encoding="utf-8") as f:
        __settings = json.load(f)
        f.close()

    return __settings

def save_settings(__object: dict[str, Any], __path: str = path_to_json) -> str | None:
    with open(__path, "w", encoding="utf-8") as f:
        json.dump(__object, f, indent=4)
        f.close()
        
    return __path
