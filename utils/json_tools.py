import json

def save_to_json(obj: dict, path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=4)

def load_from_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)