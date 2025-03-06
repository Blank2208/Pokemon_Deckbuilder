import csv


def load_card_data(card_database_csv):
    """
    Lädt eine Karten-ID-Datenbank aus einer CSV-Datei.

    Args:
        card_database_csv (str): Der Name der CSV-Datei mit Karten-Informationen.

    Returns:
        dict: Ein Wörterbuch, das Karten-IDs mit ihren Details (Name, Expansion, Nummer) verknüpft.
    """
    card_data = {}

    with open(card_database_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            card_id = row["id"]  # ID der Karte
            card_data[card_id] = {
                "name": row["name"],
                "set": row["set"],
                "number": row["number"]
            }

    return card_data


def id_to_card_converter(input_csv, output_csv, card_database_csv):
    """
    Konvertiert eine CSV-Datei mit Karten-IDs in eine CSV-Datei mit Kartennamen, Expansion und Nummer.

    Args:
        input_csv (str): Name der Eingabe-CSV-Datei mit Karten-IDs.
        output_csv (str): Name der Ausgabe-CSV-Datei mit Kartennamen, Expansion und Nummer.
        card_database_csv (str): Name der CSV-Datei mit Karteninformationen.
    """
    card_data = load_card_data(card_database_csv)

    with open(input_csv, newline='', encoding='utf-8') as infile, \
            open(output_csv, "w", newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Schreibe die Kopfzeile
        writer.writerow(["name", "set", "number"])

        for row in reader:
            card_id = row[0]  # Annahme: Die erste Spalte enthält die ID

            if card_id in card_data:
                writer.writerow([
                    card_data[card_id]["name"],
                    card_data[card_id]["set"],
                    card_data[card_id]["number"]
                ])
            else:
                print(f"Warnung: ID {card_id} nicht in der Datenbank gefunden.")


id_to_card_converter("best_deck.csv", "best_deck_converted.csv", "all_cards.csv")
