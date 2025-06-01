"""Repräsentiert einen Studiengang bestehend aus mehreren Semestern."""

from semester import Semester

class Studiengang:
    """
    Modelliert einen Studiengang mit mehreren Semestern.

    Attribute:
        name (str): Name des Studiengangs
        semester_liste (list[Semester]): Liste der zugehörigen Semester
    """
    def __init__(self, name: str, semester_liste: list[Semester]):
        """
        Initialisiert einen Studiengang mit Namen und Semestern.

        :param name: Bezeichnung des Studiengangs
        :param semester_liste: Liste von Semester-Objekten
        """
        self.name = name
        self.semester_liste = semester_liste

    def berechne_gesamtfortschritt(self) -> int :
        """
        Berechnet die Gesamtanzahl der ECTS über alle Semester hinweg.

        :return: Summe aller ECTS-Punkte im Studiengang
        """
        return sum(semester.gesamt_ects() for semester in self.semester_liste)