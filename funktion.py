import requests
import ast
import numpy as np
import pandas as pd
from panda_einstellungen import terminal

terminal()      # Zugriff auf panda_einstellungen


# Ruft die Pokémon-Daten von der API ab; returns List: Eine Liste von Pokémon-Daten, falls erfolgreich. Sonst None.
def fetch_pokemon_data(api_url, params):
    all_cards = []  # Hier sollen alle ausgegebenen Karten gespeichert werden
    page = 1        # Beginn der ersten Seite

    while True:
        print(f"Fetching page {page}...")
        params["page"] = page
        response = requests.get(api_url, params=params)

        if response.status_code == 200:     # Überprüft, ob die Anfrage erfolgreich war
            data = response.json()  # JSON-Daten in lesbaren Python-Code umwandeln

            cards = data.get("data", [])  # Holen der Karten (falls vorhanden)

            if not cards:
                break

            all_cards.extend(cards)
            page += 1
        else:
            print(f"Fehler: {response.status_code}")

    return all_cards

# Speichern der Karten in eine CSV-Datei
def save_cards_to_csv(cards, filename="pokemon_cards.csv"):

    if not cards:
        print("No Cards found.")
        return

    df = pd.DataFrame(cards)

    # Speichern als CSV
    df.to_csv(filename, index=False)
    print(f"Cards saved successfully in {filename}.")

# Einlesen einer CSV-Datei
def load_csv(filename):

    df = pd.read_csv(filename)

    # Konvertieren von verschachtelten JSON-Feldern in der CSV
    for col in ["set", "legalities", "images", "tcgplayer", "cardmarket"]:
        df[col] = df[col].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else np.nan)  # String -> Dictionary

    return df