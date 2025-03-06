# File ist für die Ermittlung der Durchschnittswerte von Pokemon, Trainerkarten & Energy in einem Deck
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV-Datei einlesen
df = pd.read_csv("deckbau1.csv")

df_werte = pd.DataFrame(df)

pokemon_counts = df["Pokemon"].value_counts().sort_index()

# Balkendiagramm erstellen
plt.figure(figsize=(12, 6))
pokemon_counts.plot(kind='bar', color='skyblue', edgecolor='black')

# Damit die y-Achse jede Zahl anzeigt
y_max = pokemon_counts.max()
plt.yticks(range(0, y_max + 1))

# Diagramm anpassen
plt.title("Häufigkeit der Anzahl Pokémon pro Deck", fontsize=16)
plt.xlabel("Anzahl Pokémon pro Deck", fontsize=14)
plt.ylabel("Anzahl Decks", fontsize=14)
plt.xticks(rotation=0, fontsize=10)  # X-Achsenbeschriftungen lesbar halten
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Diagramm anzeigen
plt.tight_layout()
plt.show()

pokemon_mean = df["Pokemon"].mean()
print(f"Durchschnittliche Anzahl Pokemon pro Deck: {pokemon_mean}")      # Ausgabe: 15.495