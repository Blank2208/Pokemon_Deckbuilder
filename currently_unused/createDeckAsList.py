import re
import csv

import re

def parse_deck(filename):
    """
    Liest ein Deck aus einer CSV-Datei und erstellt eine Liste der Karten.

    Args:
        filename (str): Der Pfad zur CSV-Datei.

    Returns:
        list: Eine Liste von Karten im Format [Expansion, Name, Nummer_Instance].
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    card_list = []  # Liste, um die Karten zu speichern
    section = None  # Aktuelle Kategorie (Pokémon, Trainer, Energy)

    for line in lines:
        line = line.strip()

        # Abschnittserkennung
        if line.startswith("Pokémon:") or line.startswith("Trainer:") or line.startswith("Energy:"):
            section = line.split(":")[0]
            continue

        # Überspringe leere Zeilen
        if not line:
            continue

        # Verarbeite Karteneinträge (z. B. "3 Lugia V SIT 138")
        match = re.match(r"(\d+)\s+(.+?)\s+([A-Z]+)\s+(\d+)", line)
        if match:
            count = int(match.group(1))  # Anzahl der Karten
            name = match.group(2)       # Name der Karte
            expansion = match.group(3)  # Expansion (z. B. SIT)
            number = match.group(4)     # Kartennummer (z. B. 138)

            # Füge jede Instanz der Karte einzeln hinzu, mit _1, _2, etc.
            for i in range(1, count + 1):
                card_list.append([expansion, name, f"{number}_{i}"])

    # Sortiere die Liste nach Name und dann Expansion
    card_list.sort(key=lambda x: (x[1], x[0]))

    return card_list

# Beispielnutzung
if __name__ == "__main__":
    # Pfad zur Deck-Datei
    deck_file = "Gardevoir.csv"  # Ersetze durch den tatsächlichen Dateipfad

    # Deck verarbeiten
    parsed_deck = parse_deck(deck_file)

    # Ergebnisse anzeigen
    print("parse_deck output:")
    print("Deck as a List:")
    for card in parsed_deck:
        print(card)

def parse_and_save_deck(input_filename, output_filename):
    """
    Liest ein Deck aus einer CSV-Datei, erstellt eine Liste der Karten als einzelne Instanzen,
    und speichert die Liste aggregiert im gewünschten Format.

    Args:
        input_filename (str): Der Pfad zur Eingabe-CSV-Datei.
        output_filename (str): Der Pfad zur Ausgabe-CSV-Datei.

    Returns:
        list: Eine Liste von Karteninstanzen im Format [Expansion, Name, Nummer_Instance].
    """
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    individual_cards = []  # Liste für einzelne Karteninstanzen
    aggregated_cards = []  # Liste für aggregierte Karten
    section = None         # Aktuelle Kategorie (Pokémon, Trainer, Energy)

    for line in lines:
        line = line.strip()

        # Abschnittserkennung
        if line.startswith("Pokémon:") or line.startswith("Trainer:") or line.startswith("Energy:"):
            section = line.split(":")[0]
            continue

        # Überspringe leere Zeilen
        if not line:
            continue

        # Verarbeite Karteneinträge (z. B. "3 Lugia V SIT 138")
        match = re.match(r"(\d+)\s+(.+?)\s+([A-Z]+)\s+(\d+)", line)
        if match:
            count = int(match.group(1))  # Anzahl der Karten
            name = match.group(2)       # Name der Karte
            expansion = match.group(3)  # Expansion (z. B. SIT)
            number = match.group(4)     # Kartennummer (z. B. 138)

            # Füge jede Instanz der Karte einzeln hinzu, mit _1, _2, etc.
            for i in range(1, count + 1):
                individual_cards.append([expansion, name, f"{number}_{i}"])

            # Füge die Karte für die aggregierte Liste hinzu
            aggregated_cards.append([count, name, expansion, number])

    # Sortiere die individuelle Liste alphabetisch nach Name und dann Expansion
    individual_cards.sort(key=lambda x: (x[1], x[0]))

    # Speichere die aggregierte Liste in eine neue CSV-Datei
    with open(output_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for card in aggregated_cards:
            # Schreibe die Karte im gewünschten Format: "<Anzahl> <Name> <Expansion> <Nummer>"
            writer.writerow([f"{card[0]} {card[1]} {card[2]} {card[3]}"])

    return individual_cards


# Beispielnutzung
if __name__ == "__main__":
    # Pfad zur Eingabe- und Ausgabedatei
    input_file = "Gardevoir.csv"   # Ersetze durch den tatsächlichen Pfad der Eingabedatei
    output_file = "Gardevoir_sorted_deck.csv"  # Ersetze durch den gewünschten Pfad der Ausgabedatei

    # Deck einlesen, verarbeiten und speichern
    parsed_deck = parse_and_save_deck(input_file, output_file)

    # Ergebnisse anzeigen
    print("parse_and_save_deck output:")
    print("Deck as a List:")
    for card in parsed_deck:
        print(card)
