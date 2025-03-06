def crossover(parent_deck_1, parent_deck_2):
    """
    Führt ein Crossover zwischen zwei sortierten Decks durch und gibt zwei Kind-Decks zurück.

    Args:
        parent_deck_1 (list): Erstes Eltern-Deck (sortierte Liste von Karten).
        parent_deck_2 (list): Zweites Eltern-Deck (sortierte Liste von Karten).

    Returns:
        tuple: Zwei neue Kind-Decks nach dem Crossover (abwechselnde Auswahl der Karten).
    """
    if len(parent_deck_1) != 60 or len(parent_deck_2) != 60:
        raise ValueError("Beide Eltern-Decks müssen genau 60 Karten enthalten.")

    child_deck_1 = []
    child_deck_2 = []

    for i in range(60):
        if i % 2 == 0:
            child_deck_1.append(parent_deck_1[i])  # Gerade Indexe -> Karte von parent_deck_1
            child_deck_2.append(parent_deck_2[i])  # Gerade Indexe -> Karte von parent_deck_2
        else:
            child_deck_1.append(parent_deck_2[i])  # Ungerade Indexe -> Karte von parent_deck_2
            child_deck_2.append(parent_deck_1[i])  # Ungerade Indexe -> Karte von parent_deck_1

    return child_deck_1, child_deck_2


if __name__ == "__main__":
    # Beispiel-Eltern-Decks mit 60 Karten
    parent_deck_1 = [f"CardA_{i}" for i in range(1, 61)]
    parent_deck_2 = [f"CardB_{i}" for i in range(1, 61)]

    # Crossover durchführen
    child_deck_1, child_deck_2 = crossover(parent_deck_1, parent_deck_2)

    # Ergebnisse ausgeben
    print("Child Deck 1:")
    print(child_deck_1)

    print("\nChild Deck 2:")
    print(child_deck_2)
