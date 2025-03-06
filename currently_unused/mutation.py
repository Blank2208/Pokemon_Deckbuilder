import random
import csv

def load_replacement_pool(csv_filename):
    """
    Lädt mögliche Ersatzkarten aus einer CSV-Datei.

    Args:
        csv_filename (str): Der Name der CSV-Datei mit Karten.

    Returns:
        list: Liste von Karten aus der Datei.
    """
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader]  # Annahme: Jede Zeile enthält eine einzelne Karte


def mutate(deck, replacement_pool, num_mutations=15):
    """
    Ersetzt zufällige Karten im Deck durch zufällige Karten aus der Ersatzliste.

    Args:
        deck (list): Das Deck, das mutiert werden soll.
        replacement_pool (list): Liste möglicher Ersatzkarten.
        num_mutations (int): Anzahl der Karten, die ersetzt werden sollen.

    Returns:
        list: Das mutierte Deck.
    """
    mutated_deck = deck[:]
    mutation_indices = random.sample(range(len(deck)), num_mutations)

    for index in mutation_indices:
        mutated_deck[index] = random.choice(replacement_pool)

    return mutated_deck


def mutation(child_deck, csv_filename, num_mutants=19, num_mutations=15):
    """
    Erstellt mutierte Versionen eines Decks.

    Args:
        child_deck (list): Ursprüngliches Kind-Deck.
        csv_filename (str): Name der CSV-Datei mit möglichen Ersatzkarten.
        num_mutants (int): Anzahl der mutierten Decks, die erstellt werden.
        num_mutations (int): Anzahl der Karten, die in jedem Deck ausgetauscht werden.

    Returns:
        list: Liste mit mutierten Decks.
    """
    replacement_pool = load_replacement_pool(csv_filename)
    mutated_decks = [mutate(child_deck, replacement_pool, num_mutations) for _ in range(num_mutants)]

    return mutated_decks


# Beispielaufruf
if __name__ == "__main__":
    child_deck = ["a", "b", "c", "d", "e", "f"] * 10  # Beispiel mit 60 Karten
    csv_file = "card_pool.csv"  # CSV-Datei mit möglichen Ersatzkarten
    mutated_decks = mutation(child_deck, csv_file)

    for i, deck in enumerate(mutated_decks):
        print(f"Mutiertes Deck {i + 1}: {deck}")
