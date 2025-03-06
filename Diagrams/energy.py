# File ist für die Ermittlung der Durchschnittswerte von Pokemon, Trainerkarten & Energy in einem Deck
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV-Datei einlesen
df = pd.read_csv("deckbau1.csv")

energy_counts = df["Energy"].value_counts().sort_index()    # Zählt alle Werte von "Energy" und sortiert sie dann

# Balkendiagramm erstellen
plt.figure(figsize=(12, 6))
energy_counts.plot(kind='bar', color='skyblue', edgecolor='black')
y_max = energy_counts.max()
plt.yticks(range(0, y_max + 1))


# Diagramm anpassen
plt.title("Häufigkeit der Anzahl Energie pro Deck", fontsize=16)
plt.xlabel("Anzahl Energie pro Deck", fontsize=14)
plt.ylabel("Anzahl Decks", fontsize=14)
plt.xticks(rotation=0, fontsize=10)  # X-Achsenbeschriftungen lesbar halten
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Diagramm anzeigen
plt.tight_layout()
plt.show()

energy_mean = df["Energy"].mean()
print(f"Durchschnittliche Anzahl Energiekarten pro Deck: {energy_mean}")  # Ausgabe 9.197