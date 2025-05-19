from modul import Modul
from utils.json_tools import save_to_json, load_from_json

mein_modul = Modul("DLBIMD01", "Mathematik", 5, "bestanden")

save_to_json(mein_modul.to_dict(), "_data/module.json")
print(" Modul gespeichert.")

data = load_from_json("_data/module.json")
geladenes_modul = Modul.from_dict(data)
from modul import Modul
from utils.json_tools import save_to_json, load_from_json

mein_modul = Modul("DLBIMD01", "Mathematik", 5, "bestanden")

save_to_json(mein_modul.to_dict(), "_data/module.json")
print("✅ Modul gespeichert.")

data = load_from_json("_data/module.json")
geladenes_modul = Modul.from_dict(data)

print(" Geladenes Modul:")
print(f"Code: {geladenes_modul.code}")
print(f"Titel: {geladenes_modul.titel}")
print(f"ECTS: {geladenes_modul.ects}")
print(f"Status: {geladenes_modul.status}")

print(" Geladenes Modul:")
print(f"Code: {geladenes_modul.code}")
print(f"Titel: {geladenes_modul.titel}")
print(f"ECTS: {geladenes_modul.ects}")
print(f"Status: {geladenes_modul.status}")