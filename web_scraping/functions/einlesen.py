import pandas as pd

def parse_deck_to_csv(copied_text, deck_name, output_file):
    """
    Verarbeitet den kopierten Text eines Decks von Limitless und speichert ihn als CSV.

    Args:
        copied_text (str): Der Text, der von Limitless kopiert wurde.
        deck_name (str): Der Name des Decks.
        output_file (str): Der Name der CSV-Datei.
    """
    # Initialisierung der Listen
    card_data = []
    section_counts = {"Pokemon": 0, "Trainer": 0, "Energy": 0}
    current_section = None

    for line in copied_text.splitlines():
        line = line.strip()

        # Abschnittsüberschriften erkennen und speichern
        if line.startswith("Pokémon"):
            current_section = "Pokemon"
            section_counts["Pokemon"] = int(line.split(":")[1].strip())  # Anzahl Pokémon-Karten speichern
            continue
        elif line.startswith("Trainer"):
            current_section = "Trainer"
            section_counts["Trainer"] = int(line.split(":")[1].strip())  # Anzahl Trainerkarten speichern
            continue
        elif line.startswith("Energy"):
            current_section = "Energy"
            section_counts["Energy"] = int(line.split(":")[1].strip())  # Anzahl Energiekarten speichern
            continue

        # Zeile mit der Anzahl und dem Kartenname
        if line:
            try:
                quantity, card_name = line.split(" ", 1)
                quantity = int(quantity)

                # Kartentyp festlegen
                if current_section == "Pokemon":
                    card_type = "Pokemon"
                elif current_section == "Trainer":
                    card_type = "Trainer"
                elif current_section == "Energy":
                    card_type = "Energy"
                else:
                    raise ValueError(f"Unbekannter Kartentyp: {line}")

                # Karten-Daten in die Liste einfügen
                card_data.append({
                    "Deck Name": deck_name,
                    "Card Name": card_name,
                    "Quantity": quantity,
                    "Type": card_type
                })
            except ValueError:
                print(f"Fehler beim Parsen der Zeile: {line}")

    # Daten in DataFrame umwandeln
    df = pd.DataFrame(card_data)

    # CSV speichern
    if not df.empty:
        df.to_csv(output_file, index=False, mode="a", header=not pd.io.common.file_exists(output_file))
        print(f"Deck '{deck_name}' erfolgreich in {output_file} gespeichert.")
    else:
        print("Keine Daten gefunden. Überprüfen Sie den kopierten Text.")

    # Gesamtzahl der Karten
    total_pokemon = section_counts["Pokemon"]
    total_trainer = section_counts["Trainer"]
    total_energy = section_counts["Energy"]

    # Erstelle eine Zeile mit der Gesamtzahl der Karten und füge sie zur CSV-Datei hinzu
    total_line = {
        "Deck Name": "Cards",
        "Card Name": f"{total_pokemon} Pokemon, {total_trainer} Trainer, {total_energy} Energy",
        "Quantity": "",
        "Type": ""
    }

    # Konvertiere total_line in einen DataFrame und speichere es am Ende der CSV
    total_df = pd.DataFrame([total_line])
    total_df.to_csv(output_file, index=False, mode="a", header=False)

# Deckaufruf
copied_text = """
Pokémon: 16
4 Deino SSP 117
1 Zweilous SSP 118
3 Hydreigon ex SSP 119
2 Pidgey OBF 162
2 Pidgeot ex OBF 164
1 Rotom V LOR 58
1 Lumineon V BRS 40
1 Fezandipiti ex SFA 38
1 Pecharunt ex SFA 39

Trainer: 37
4 Arven OBF 186
2 Iono PAL 185
1 Boss's Orders PAL 172
1 Eri TEF 146
1 Roseanne's Backup BRS 148
4 Nest Ball SVI 181
4 Rare Candy SVI 191
3 Ultra Ball SVI 196
3 Buddy-Buddy Poffin TEF 144
2 Dark Patch ASR 139
2 Counter Catcher PAR 160
1 Super Rod PAL 188
1 Night Stretcher SFA 61
1 Earthen Vessel PAR 163
1 Feather Ball ASR 141
1 Tera Orb SSP 189
1 Binding Mochi SFA 55
1 Counter Gain SSP 169
1 Forest Seal Stone SIT 156
2 Pokémon League Headquarters OBF 192

Energy: 7
6 Darkness Energy SVE 15
1 Neo Upper Energy TEF 162
"""
deck_name = "Hydreigon"
output_file = "../test.csv"

parse_deck_to_csv(copied_text, deck_name, output_file)
