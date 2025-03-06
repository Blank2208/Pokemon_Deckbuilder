# File ist für die Ermittlung der Durchschnittswerte von Pokemon, Trainerkarten & Energy in einem Deck
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV-Datei einlesen
df = pd.read_csv("deckbau1.csv")

df_werte = pd.DataFrame(df)

trainer_counts = df["Trainer"].value_counts().sort_index()

# Balkendiagramm erstellen
plt.figure(figsize=(12, 6))
trainer_counts.plot(kind='bar', color='skyblue', edgecolor='black')

y_max = trainer_counts.max()

# Diagramm anpassen
plt.title("Häufigkeit der Anzahl Trainer pro Deck", fontsize=16)
plt.xlabel("Anzahl Trainer pro Deck", fontsize=14)
plt.ylabel("Anzahl Decks", fontsize=14)
plt.xticks(rotation=0, fontsize=10)  # X-Achsenbeschriftungen lesbar halten
plt.yticks(range(0, y_max + 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Diagramm anzeigen
plt.tight_layout()
plt.show()

trainer_mean = df["Trainer"].mean()
print(f"Durchschnittliche Anzahl Trainerkarten pro Deck: {trainer_mean}")       # Ausgabe: 35.307