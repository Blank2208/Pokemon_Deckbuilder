from funktion import fetch_pokemon_data, save_cards_to_csv
import pandas as pd

# Alle relevante Energy-Karten abrufen und speichern
if __name__ == "__main__":
    url = "https://api.pokemontcg.io/v2/cards"
    params = {"q": "supertype:Energy AND (regulationMark:F OR regulationMark:G OR regulationMark:H) OR id:sve-9 OR id:sve-10 OR id:sve-11 OR id:sve-12 OR id:sve-13 OR id:sve-14 OR id:sve-15 OR id:sve-16"}

    # Abruf
    energy_cards = fetch_pokemon_data(url, params)

    # Speichern in eine CSV-Datei
    save_cards_to_csv(energy_cards, "energy_cards.csv")

df = pd.DataFrame(energy_cards)
print(df)