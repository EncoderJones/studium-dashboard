from semester import Semester

class Studiengang:
    def __init__(self, name: str, semester_liste: list[Semester]):
        self.name = name
        self.semester_liste = semester_liste

    def berechne_gesamtfortschritt(self):
        return sum(semester.gesamt_ects() for semester in self.semester_liste)