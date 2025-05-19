from pruefungsleistung import Pruefungsleistung

class Modul:
    def __init__(self, code: str, titel: str, ects: int, status: str, pruefungsleistung: Pruefungsleistung = None):
        self.code = code
        self.titel = titel
        self.ects = ects
        self.status = status
        self.pruefungsleistung = pruefungsleistung

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "titel": self.titel,
            "ects": self.ects,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict):
        return Modul(
            code=data["code"],
            titel=data["titel"],
            ects=data["ects"],
            status=data["status"]
        )