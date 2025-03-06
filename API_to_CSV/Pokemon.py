from funktion import fetch_pokemon_data, save_cards_to_csv
import pandas as pd

# Alle legale Pokemon-Karten abrufen und speichern
if __name__ == "__main__":
    url = "https://api.pokemontcg.io/v2/cards"
    params = {"q": "supertype:Pokemon AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"
              }
    # Abruf
    pokemon_cards = fetch_pokemon_data(url, params)

    # Speichern in eine CSV-Datei
    save_cards_to_csv(pokemon_cards, "pokemon_cards.csv")

df = pd.DataFrame(pokemon_cards)
print(df)