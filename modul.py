"""
Modulklasse zur Repräsentation eines Studienmoduls mit ECTS, Titel, Status und optionaler Prüfungsleistung.
"""

from pruefungsleistung import Pruefungsleistung

class Modul:
    """
    Repräsentiert ein Studienmodul.

    Attribute:
        code (str): Modulcode (z. B. "DLBIMD01")
        titel (str): Modultitel (z. B. "Mathematik")
        ects (int): Anzahl der ECTS-Punkte
        status (str): Status des Moduls (z. B. "bestanden", "offen")
        pruefungsleistung (Pruefungsleistung, optional): Zugehörige Prüfungsleistung
    """

    def __init__(self, code: str, titel: str, ects: int, status: str, pruefungsleistung: Pruefungsleistung = None):
        """
        Initialisiert ein Modulobjekt.

        :param code: Modulcode
        :param titel: Modultitel
        :param ects: ECTS-Punkte
        :param status: Modulstatus
        :param pruefungsleistung: Optional verknüpfte Prüfungsleistung
        """
        self.code = code
        self.titel = titel
        self.ects = ects
        self.status = status
        self.pruefungsleistung = pruefungsleistung

    def to_dict(self) -> dict:
        """
        Wandelt das Modulobjekt in ein Dictionary um (für Serialisierung).

        :return: Dictionary mit Modulwerten
        """
        return {
            "code": self.code,
            "titel": self.titel,
            "ects": self.ects,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Erstellt ein Modulobjekt aus einem Dictionary (für Deserialisierung).

        :param data: Dictionary mit Modulwerten
        :return: Modulobjekt
        """
        return Modul(
            code=data["code"],
            titel=data["titel"],
            ects=data["ects"],
            status=data["status"]
        )