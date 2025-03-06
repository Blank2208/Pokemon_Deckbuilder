import ast
from funktion import load_csv
import pandas as pd
from panda_einstellungen import terminal

terminal()      # Zugriff auf panda_einstellungen


# Pokemon-Karten nach Pokemon-`types` filtern, also Fire, Water usw.
def filter_by_type(df, card_type):

    # Prüfen, ob `card_type` in der Liste von `types` ist
    filtered_df = df[df["types"].apply(lambda x: card_type in ast.literal_eval(x))]
    return filtered_df


# Karten nach `subtypes` filtern, also Ancient usw.
def filter_by_subtype(df, card_subtype):

    # Prüfen, ob `card_subtype` in der Liste von `types` ist
    filtered_df = df[df["subtypes"].apply(lambda x: card_subtype in ast.literal_eval(x))]
    return filtered_df


# Funktion, um nach einer Karte zu suchen
def search_by_evolves_from(df, evolves_from_value):

    # Prüfen, ob die Spalte 'evolvesFrom' existiert
    if 'evolvesFrom' in df.columns:
        # Filtern: Ignoriere NaN und suche nach Übereinstimmung
        filtered_df = df[df['evolvesFrom'].fillna('').str.contains(evolves_from_value, case=False)]
        return filtered_df
    else:
        print("'evolvesFrom' does not exist.")
        return pd.DataFrame()  # Leerer DataFrame, wenn Spalte fehlt


# Funktion zum Speichern des gefilterten in eine neue CSV
def save_filtered_csv(df, filename):

    df.to_csv(filename, index=False)
    print(f"Filtered Cards saved in {filename}.")


# Beispiels-Aufrufe
if __name__ == "__main__":
    # Bei original_csv den gewünschten CSV-Datei-Namen eingeben
    original_csv = "pokemon_cards.csv"
    df = load_csv(original_csv)

    # Nach `type` filtern
    # filtered_fire_df = filter_by_type(df, "Fire")
    # Nach `subtype` filtern
    # filtered_ancient_df = filter_by_subtype(df, "Ancient")

    # Gefiltertes in eine neue CSV speichern
    # save_filtered_csv(filtered_fire_df, "fire_pokemon_cards.csv")
    # save_filtered_csv(filtered_ancient_df, "ancient_all_cards.csv")

    # Nach Karten suchen, die von 'Bulbasaur' evolvieren
    evolves_from_value = "Bulbasaur"
    result_df = search_by_evolves_from(df, evolves_from_value)

    # Ergebnis anzeigen oder speichern
    if not result_df.empty:
        print(result_df)
        result_df.to_csv(f"cards_evolving_from_{evolves_from_value}.csv", index=False)
        print(f"Ergebnisse gespeichert in 'cards_evolving_from_{evolves_from_value}.csv'")
    else:
        print(f"Keine Karten gefunden, die von '{evolves_from_value}' evolvieren.")
