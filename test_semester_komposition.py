from modul import Modul
from semester import Semester

m1 = Modul("DLBIMD01", "Mathematik", 5, "bestanden")
m2 = Modul("DLBPROG01", "Programmierung", 5, "bestanden")

mein_semester = Semester(1, [m1, m2])

print(f"📚 Semester {mein_semester.nummer} enthält {mein_semester.anzahl_module()} Module.")
print(f"📊 Gesamt-ECTS: {mein_semester.gesamt_ects()}")

for modul in mein_semester.module:
    print(f"- {modul.titel} ({modul.ects} ECTS)")