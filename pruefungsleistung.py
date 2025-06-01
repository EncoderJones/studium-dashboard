"""Repräsentiert eine Prüfungsleistung mit Note und Prüfungsdatum."""


class Pruefungsleistung:
    """
    Modelliert eine Prüfungsleistung.

    Attribute:
        note (float): Die erhaltene Note.
        datum (str): Das Prüfungsdatum im Format 'JJJJ-MM-TT'.
    """
    def __init__(self, note: float, datum: str):
        """
        Initialisiert eine Prüfungsleistung mit Note und Datum.

        :param note: Die Note der Prüfungsleistung
        :param datum: Das Datum der Prüfungsleistung
        """
        self.note = note
        self.datum = datum

    def ist_bestanden(self) -> bool:
        """
            Prüft, ob die Prüfungsleistung bestanden ist (Note ≤ 4,0).

            :return: True, wenn bestanden, sonst False
            """
        return self.note <= 4.0

    def anzeigen(self) -> str :
        """
        Gibt die Prüfungsleistung als formatierte Zeichenkette aus.

        :return: Formatierter String mit Note und Status
        """
        return f"Note: {self.note} ({'Bestanden' if self.ist_bestanden() else 'Nicht bestanden'})"