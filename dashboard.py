import streamlit as st
import pandas as pd

# === Basisdaten ===
ziel_note = 2.0
aktuelle_note = 1.4
gesamt_ects = 180
erreicht_ects = 35
max_monate = 36
aktueller_monat = 6

# === Berechnungen ===
ects_prozent = erreicht_ects / gesamt_ects * 100
zeit_prozent = aktueller_monat / max_monate * 100

notendifferenz = ziel_note - aktuelle_note
note_diff_anzeige = f"+{notendifferenz:.1f}" if notendifferenz > 0 else f"{notendifferenz:.1f}"

# Fortschritt bewerten → für Streamlit gültig
if ects_prozent >= zeit_prozent:
    delta_farbe = "normal"    # Fortschritt OK → grün
else:
    delta_farbe = "inverse"   # Rückstand → rot

# === GUI ===
st.title("🎓 Studien-Dashboard")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Aktueller Notenschnitt", f"{aktuelle_note:.1f}", note_diff_anzeige)
with col2:
    st.metric("Studienmonat", f"{aktueller_monat} / {max_monate}", f"{zeit_prozent:.1f} %")
with col3:
    st.metric("ECTS erreicht", f"{erreicht_ects} / {gesamt_ects}", f"{ects_prozent:.1f} %", delta_color=delta_farbe)

st.divider()

# === Tabelle: Module ===
module = [
    {"Modul": "Mathematik", "ECTS": 5, "Note": 2.3, "Bestanden": "Ja"},
    {"Modul": "Programmierung", "ECTS": 5, "Note": 1.0, "Bestanden": "Ja"},
    {"Modul": "KI", "ECTS": 5, "Note": 1.3, "Bestanden": "Ja"},
]

df = pd.DataFrame(module)
df["Note"] = df["Note"].map(lambda x: f"{x:.1f}")

st.subheader("Deine letzten Leistungsnachweise")
st.table(df)