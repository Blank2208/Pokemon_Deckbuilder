from funktion import fetch_pokemon_data, save_cards_to_csv
import pandas as pd

# Alle legalen Karten abrufen und speichern
if __name__ == "__main__":
    url = "https://api.pokemontcg.io/v2/cards"
    params = {"q": "regulationMark:F OR regulationMark:G OR regulationMark:H"
              }
    # Abruf
    all_cards = fetch_pokemon_data(url, params)

    # Speichern in eine CSV-Datei
    save_cards_to_csv(all_cards, "all_cards.csv")

df = pd.DataFrame(all_cards)
print(df)