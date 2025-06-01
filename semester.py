"""Repräsentiert ein Semester mit einer Liste von Modulen."""

from modul import Modul

class Semester:
    """
    Modelliert ein Semester innerhalb eines Studiengangs.

    Attribute:
        nummer (int): Semesternummer (z. B. 1, 2, 3, ...)
        module (list[Modul]): Liste der enthaltenen Module
    """
    def __init__(self, nummer: int, module: list[Modul]):
        """
        Initialisiert ein Semester mit Nummer und Modulliste.

        :param nummer: Die Semesternummer
        :param module: Liste von Modul-Objekten im Semester
        """
        self.nummer = nummer
        self.module = module

    def anzahl_module(self) -> int :
        """
        Gibt die Anzahl der enthaltenen Module zurück.

        :return: Anzahl der Module im Semester
        """
        return len(self.module)

    def gesamt_ects(self) -> int :
        """
        Berechnet die Summe der ECTS-Punkte aller Module im Semester.

        :return: Gesamte ECTS-Punkte des Semesters
        """
        return sum(modul.ects for modul in self.module)