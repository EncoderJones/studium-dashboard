from modul import Modul

class Semester:
    def __init__(self, nummer: int, module: list[Modul]):
        self.nummer = nummer
        self.module = module

    def anzahl_module(self):
        return len(self.module)

    def gesamt_ects(self):
        return sum(modul.ects for modul in self.module)