"""
Hauptprogramm zur Demonstration:
- Erstellung und Serialisierung eines Modul-Objekts
- Laden aus JSON-Datei
- Ausgabe der Modulwerte
- Visualisierung des ECTS-Fortschritts mit matplotlib
"""

from modul import Modul
from utils.json_tools import save_to_json, load_from_json

# Neues Modul-Objekt erstellen
mein_modul = Modul("DLBIMD01", "Mathematik", 5, "bestanden")

# Modul in JSON-Datei speichern
save_to_json(mein_modul.to_dict(), "_data/module.json")
print("✅ Modul gespeichert.")

# Modul aus JSON-Datei wieder laden
data = load_from_json("_data/module.json")

# Geladenes Modul ausgeben
geladenes_modul = Modul.from_dict(data)

print("📦 Geladenes Modul:")
print(f"Code: {geladenes_modul.code}")
print(f"Titel: {geladenes_modul.titel}")
print(f"ECTS: {geladenes_modul.ects}")
print(f"Status: {geladenes_modul.status}")

# Visualisierung: ECTS-Fortschritt mit Balkendiagramm
import matplotlib.pyplot as plt

gesamt_ects = 180
erreicht_ects = 35

plt.bar(["Erreicht", "Ziel"], [erreicht_ects, gesamt_ects], color=["green", "gray"])
plt.title("ECTS-Fortschritt")
plt.ylabel("Punkte")
plt.ylim(0, 200)
plt.grid(axis='y')

plt.show()