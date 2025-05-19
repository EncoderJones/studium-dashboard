class Pruefungsleistung:
    def __init__(self, note: float, datum: str):
        self.note = note
        self.datum = datum

    def ist_bestanden(self):
        return self.note <= 4.0

    def anzeigen(self):
        return f"Note: {self.note} ({'Bestanden' if self.ist_bestanden() else 'Nicht bestanden'})"