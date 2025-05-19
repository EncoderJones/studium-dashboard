from modul import Modul
from pruefungsleistung import Pruefungsleistung

pl = Pruefungsleistung(2.3, "2025-03-15")

modul = Modul("DLBETIK01", "Ethik", 5, "abgeschlossen", pruefungsleistung=pl)

print(f"{modul.titel}: {modul.pruefungsleistung.anzeigen()}")