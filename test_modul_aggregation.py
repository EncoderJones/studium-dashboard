"""Test zur Aggregation: Modul enthält Prüfungsleistung als Bestandteil."""

from modul import Modul
from pruefungsleistung import Pruefungsleistung

# Prüfungsleistung erstellen
pl = Pruefungsleistung(2.3, "2025-03-15")

# Modul mit Prüfungsleistung anlegen (Aggregation)
modul = Modul("DLBETIK01", "Ethik", 5, "abgeschlossen", pruefungsleistung=pl)

# Prüfungsleistung anzeigen
print(f"{modul.titel}: {modul.pruefungsleistung.anzeigen()}")