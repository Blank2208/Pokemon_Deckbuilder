import pandas as pd
import re

def replace_set_abbreviation(card_name, mapping):
    """Ersetzt die Set-Abkürzungen durch vollständige Namen."""
    for abbr, full_name in mapping.items():
        card_name = re.sub(rf"\b{abbr}\b", full_name, card_name)
    return card_name

def convert_pokemon_csv(input_file, output_file):
    """Liest eine CSV-Datei, ersetzt Set-Abkürzungen und speichert die geänderte Datei."""
    # Vollständiges Mapping für Regulation Mark F bis H
    set_mapping = {
        "BRS": "Brilliant Stars",
        "ASR": "Astral Radiance",
        "PGO": "Pokémon GO",
        "LOR": "Lost Origin",
        "SIT": "Silver Tempest",
        "CRZ": "Crown Zenith",
        "SVI": "Scarlet & Violet",
        "PAL": "Paldea Evolved",
        "OBF": "Obsidian Flames",
        "MEW": "151",
        "PAR": "Paradox Rift",
        "TEF": "Temporal Forces",
        "TWM": "Twilight Masquerade",
        "SSP": "Surging Sparks",
        "SFA": "Shrouded Fable",
        "SVE": "Scarlet & Violet",
        "PAF": "Paldean Fates",
        "SCR": "Stellar Crown"
    }

    # CSV-Datei einlesen
    df = pd.read_csv(input_file)

    # Ersetzen der Set-Abkürzungen
    df["Card Name"] = df["Card Name"].apply(lambda x: replace_set_abbreviation(x, set_mapping))

    # Neue Datei speichern
    df.to_csv(output_file, index=False)
    print(f"Die konvertierte Datei wurde gespeichert unter: {output_file}")

# Beispielaufruf des Programms
if __name__ == "__main__":
    input_csv = "Assoziations-Decklisten/Water.csv"
    output_csv = "Water.csv"
    convert_pokemon_csv(input_csv, output_csv)