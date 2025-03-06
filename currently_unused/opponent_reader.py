import csv
import numpy as np

def opponent_reader(file_path):

    # Leeres Array für ein Deck
    # Format: [Anzahl][Name][Expansion][Number], 60-mal (weil maximal 60 verschiedene Karten im Deck sein können)
    # Expansion nur definiert, sodass der Rest leichter einlesbar ist
    deckarray_2d = np.empty((60, 4), dtype=object)

    # Öffnen und Lesen der CSV-Datei
    with open(file_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ') # Der delimiter ist nur ein Leerzeichen
        row_index = 0   # Anfang an der ersten Zeile

        for row in spamreader:
            if row_index >= 60:  # Falls irgendwie mehr als 60 Zeilen, Abbruch
                break

            # Mache weiter, wenn mindestens 4 Spalten gelesen werden
            # Hiermit das einlesen leichter gemacht, damit das Deck nicht per Hand leicht angepasst werden muss
            # siehe Regidrago und Regidrago2 was damit gemeint ist
            if len(row) >= 4:

                number_of_copies = row[0]  # Erste Spalte: Anzahl dieser Karte im Deck
                card_number = row[-1]  # Vierte Spalte: Number (das letzte eingelesene Objekt der Zeile)
                expansion = row[-2]  # Dritte Spalte: Expansion (vorletztes Objekt der Zeile)

                # Zweite Spalte: Name der Karte (alle verbleibende Objekte in der Mitte zusammen als String)
                card_name = ' '.join(row[1:-2])

                # Hinzufügen ins Array
                deckarray_2d[row_index, 0] = number_of_copies
                deckarray_2d[row_index, 1] = card_name
                deckarray_2d[row_index, 2] = expansion
                deckarray_2d[row_index, 3] = card_number

                row_index += 1  # Nächste Zeile weitermachen

    # Nur die nicht-leeren Zeilen werden erkannt
    non_empty_rows = ~np.all(deckarray_2d == None, axis=1)  # Vor 'None' die '==' lassen, der pycharm "fix" bricht es
    # Ins gefilterte Array die nicht-leeren Zeilen hinzufügen
    filtered_deckarray_2d = deckarray_2d[non_empty_rows]

    return filtered_deckarray_2d

file_path = 'Snorlax_Stall.csv'    # Hier Dateiname der CSV-Datei(Da es im selben Ordner ist, reicht Dateiname)

opponent_deck = opponent_reader(file_path)

print(opponent_deck)