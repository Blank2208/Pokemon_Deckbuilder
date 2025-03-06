from funktion import fetch_pokemon_data, save_cards_to_csv
import pandas as pd

# Alle legale Trainer-Karten abrufen und speichern
if __name__ == "__main__":
    url = "https://api.pokemontcg.io/v2/cards"
    params = {"q": "supertype:Trainer AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"
              }
    # Abruf
    trainer_cards = fetch_pokemon_data(url, params)

    # Speichern in eine CSV-Datei
    save_cards_to_csv(trainer_cards, "trainer_cards.csv")

df = pd.DataFrame(trainer_cards)
print(df)