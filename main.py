from modul import Modul
from utils.json_tools import save_to_json, load_from_json

mein_modul = Modul("DLBIMD01", "Mathematik", 5, "bestanden")

save_to_json(mein_modul.to_dict(), "_data/module.json")
print("✅ Modul gespeichert.")

data = load_from_json("_data/module.json")

geladenes_modul = Modul.from_dict(data)

print("📦 Geladenes Modul:")
print(f"Code: {geladenes_modul.code}")
print(f"Titel: {geladenes_modul.titel}")
print(f"ECTS: {geladenes_modul.ects}")
print(f"Status: {geladenes_modul.status}")

import matplotlib.pyplot as plt

gesamt_ects = 180
erreicht_ects = 35

plt.bar(["Erreicht", "Ziel"], [erreicht_ects, gesamt_ects], color=["green", "gray"])
plt.title("ECTS-Fortschritt")
plt.ylabel("Punkte")
plt.ylim(0, 200)
plt.grid(axis='y')

plt.show()