from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q":"supertype:Pokemon AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"}
all_cards = fetch_pokemon_data(url, params)

df = pd.DataFrame(all_cards)    # Wandelt die gefetchten Daten in eine überschaubare Tabelle um
print(df)


# Hab versucht uns hier ne Excel-Datei zu erstellen, aber die wurde nicht richtig formatiert... :c
# df.to_csv(r"C:/Sonstiges/Pokemon/energy.csv", index=False, encoding="utf-8")
# print("Die Datei wurde erfolgreich erstellt!")