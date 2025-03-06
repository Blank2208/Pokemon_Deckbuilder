from funktion import fetch_pokemon_data, save_cards_to_csv
import pandas as pd

# Basic-Energy-Karten abrufen und speichern
if __name__ == "__main__":
    url = "https://api.pokemontcg.io/v2/cards"
    params = {"q": "id:sve-9 OR id:sve-10 OR id:sve-11 OR id:sve-12 OR id:sve-13 OR id:sve-14 OR id:sve-15 OR id:sve-16"
              }
    # Abruf
    basic_energy_cards = fetch_pokemon_data(url, params)

    # Speichern in eine CSV-Datei
    save_cards_to_csv(basic_energy_cards, "basic_energy_cards.csv")

df = pd.DataFrame(basic_energy_cards)
print(df)