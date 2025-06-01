"""
Hilfsfunktionen zum Speichern und Laden von Python-Datenstrukturen im JSON-Format.
"""

import json

def save_to_json(obj: dict, path: str):
    """
    Speichert ein Dictionary als JSON-Datei.

    :param obj: Die zu speichernde Datenstruktur (Dictionary)
    :param path: Dateipfad, unter dem die Datei gespeichert werden soll
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=4)

def load_from_json(path: str) -> dict:
    """
    Lädt ein Dictionary aus einer JSON-Datei.

    :param path: Pfad zur JSON-Datei
    :return: Geladene Daten als Dictionary
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

