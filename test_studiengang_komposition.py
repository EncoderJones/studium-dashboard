"""Test zur verschachtelten Komposition: Studiengang enthält Semester mit Modulen."""

from modul import Modul
from semester import Semester
from studiengang import Studiengang

# Module erstellen
m1 = Modul("DLBIMD01", "Mathematik", 5, "bestanden")
m2 = Modul("DLBPROG01", "Programmierung", 5, "bestanden")
m3 = Modul("DLBETIK01", "Ethik", 5, "bestanden")
m4 = Modul("DLBKI01", "KI", 5, "bestanden")

# Semester mit Modulen erstellen
sem1 = Semester(1, [m1, m2])
sem2 = Semester(2, [m3, m4])

# Studiengang mit Semestern erstellen
studiengang = Studiengang("Angewandte KI", [sem1, sem2])

# Gesamtfortschritt berechnen
gesamt_ects = studiengang.berechne_gesamtfortschritt()

# Ergebnis ausgeben
print(f"📘 Studiengang '{studiengang.name}' hat aktuell {gesamt_ects} ECTS erreicht.")