import random
import pandas as pd
import csv
import ast
from collections import defaultdict
from initial_deck import create_initial_deck

# Einlesen der Assoziationsregeln für die Evaluation
rules = pd.read_csv("assoziationsregeln_neuesSet_fpgrowth_030.csv")

# Gewichtungsfaktoren
a = 1   # Gewichtung für Support
b = 1.2 # Gewichtung für Confidence
c = 2   # Gewichtung für Lift


# Hilfsfunktion, damit Decks zu frozensets umgewandelt werden für die Evaluation
def convert_deck_to_frozenset(deck):
    # Return sind die Karten in beliebiger Reihenfolge als frozenset
    return frozenset(deck)

# Funktion zur Deckbewertung
def deck_evaluation_2(rules, deck, a, b, c):

    # Testausgabe
    print("deck_evaluation() aufgerufen")
    deck_dupli = add_duplicate_numbers(deck)
    deck_frozenset = convert_deck_to_frozenset(deck_dupli)
    # Testausgabe
    print(deck_frozenset)

    deck_bewertung = 0
    matching_rules = []  # Liste für passende Regeln

    # Über die Regeln iterieren
    for _, rule in rules.iterrows():
        # Antecedents und Consequents in frozensets umwandeln
        antecedents = frozenset(eval(rule['antecedents']))  # 'antecedents' als Set interpretieren
        consequents = frozenset(eval(rule['consequents']))  # Ebenso für 'consequents'

        # Prüfen, ob Antecedents vollständig im Deck sind und ob Consequents vollständig im Deck sind
        if antecedents.issubset(deck_frozenset) and consequents.issubset(deck_frozenset):
            # Regelbewertung berechnen
            support = rule['support']
            confidence = rule['confidence']
            lift = rule['lift']
            rule_bewertung = support * a + confidence * b + lift * c
            deck_bewertung += rule_bewertung

            # Regel speichern
            matching_rules.append({
                'antecedents': antecedents,
                'consequents': consequents,
                'support': support,
                'confidence': confidence,
                'lift': lift,
                'rule_bewertung': rule_bewertung
            })

    # Testausgabe
    print("deck_bewertung: ", deck_bewertung)

    # Return ist ein int-Wert
    return deck_bewertung


# Speichern der Supertypes aller Trainer und Pokemon des richtigen Typs
def load_supertype_query_library(csv_filename):
    query_library = []  # Liste aller Karten

    # CSV-Datei der Pokemon-Karten einlesen
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Karten aus der CSV lesen
        for row in reader:
            name = row['name']
            supertype = row['supertype']
            set_json = row[("set")].strip()  # Set ist ein JSON-String
            # Expansion (intern als name) aus JSON extrahieren
            try:
                set_data = ast.literal_eval(set_json)  # Sicheres Parsen
                expansion = set_data.get("name", "Unbekannt")
            except (SyntaxError, ValueError):
                expansion = "Unbekannt"  # Falls Fehler auftritt
            number = row['number']
            query_library.append(f"{name} {expansion} {number} {supertype}")

    trainer_cards_for_library = "trainer_cards.csv"
    # CSV-Datei der Trainerkarten einlesen
    with open(trainer_cards_for_library, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Karten aus der CSV lesen
        for row in reader:
            name = row['name']
            supertype = row['supertype']
            set_json = row[("set")].strip()  # Set ist ein JSON-String
            # Expansion (intern als name) aus JSON extrahieren
            try:
                set_data = ast.literal_eval(set_json)  # Sicheres Parsen
                expansion = set_data.get("name", "Unbekannt")
            except (SyntaxError, ValueError):
                expansion = "Unbekannt"  # Falls Fehler auftritt
            number = row['number']
            query_library.append(f"{name} {expansion} {number} {supertype}")

    # Return ist eine Liste aller Karten mit deren Supertypes
    return query_library


# Hilfsfunktion, damit Karten den Duplikatennummer(z.B. _2) rangehängt bekommen für die Evaluation
def add_duplicate_numbers(deck):

    card_counts = defaultdict(int)  # Wie oft jede Karte bereits vorkam
    numbered_deck = []              # Enthält das final nummerierte Deck

    for card in deck:
        card_counts[card] += 1      # Zähler für die aktuelle Karte erhöhen
        numbered_deck.append(f"{card}_{card_counts[card]}")  # Karte mit Nummerierung hinzufügen

    # Return ist das Deck mit nummerierten Karten
    return numbered_deck


# Funktion für das Laden der Ersatzkarten für mutate
def load_replacement_pool(csv_filename):
    replacement_pool = []  # Liste für die Karten-Tupel

    # CSV-Datei einlesen
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Karten aus der CSV lesen
        for row in reader:
            name = row['name']
            set_json = row[("set")].strip()  # Set ist ein JSON-String
            # Expansion (intern als name gekennzeichnet) aus JSON extrahieren
            try:
                set_data = ast.literal_eval(set_json)  # Sicheres Parsen
                expansion = set_data.get("name", "Unbekannt")
            except (SyntaxError, ValueError):
                expansion = "Unbekannt"  # Falls Fehler auftritt
            number = row['number']
            replacement_pool.append(f"{name} {expansion} {number}")

    # Return ist ne Liste aller Karten aus der relevanten Datei
    return replacement_pool


# Die beiden replacement_pools, die immer dieselben sind
trainer_cards = load_replacement_pool("trainer_cards.csv")
energy_cards = load_replacement_pool("energy_cards.csv")


# Hilfsfunktion zur Prüfung, ob eine Karte schon 4-mal im Deck ist
def can_add_card(card, deck, supertype_library):
    # Supertype der Karte nachschauen
    supertype = check_supertype(card, supertype_library)

    # Falls die Karte nicht gefunden, sicherheitshalber das Hinzufügen nicht erlauben
    if supertype is None:
        return False

    # Falls es sich um eine Energie-Karte handelt, gibt es keine Begrenzung
    if supertype == "Energy":
        return True

    # Entferne Duplikatennummer (_X), um Karten korrekt zu zählen
    card_base = "_".join(card.split("_")[:-1]) if "_" in card else card

    # Wie oft die Basisversion der Karte im Deck
    count = sum(1 for i in deck if i.startswith(card_base))

    # Falls weniger als 4-mal, dann das Hinzufügen erlauben
    return count < 4


# Bestimmt den Supertype einer Karte
def check_supertype(card, supertype_library):
    # Entferne Duplikaten-Nummer
    card_base = "_".join(card.split("_")[:-1]) if "_" in card else card

    for entry in supertype_library:
        if entry.startswith(card_base + " "):
            # Return ist ein String
            return entry.split(" ")[-1]  # Supertype ist das letzte Wort im String

    return None  # Falls die Karte nicht gefunden wurde


# Funktion für die Mutation der einzelnen Decks
def mutate(deck, pokemon_replacement_pool, supertype_library, num_mutations=5):

    # Testausgabe
    print("mutate() aufgerufen")

    mutated_deck = deck[:]
    # Zufällige Karten aus dem Deck auswählen
    mutation_indices = random.sample(range(len(deck)), num_mutations)

    for index in mutation_indices:

        # Die Karten werden nur durch andere Karten denselben Supertypes ausgetauscht
        # Energie-Karten werden nicht ersetzt
        supertype = check_supertype(mutated_deck[index], supertype_library)

        if supertype == 'Trainer':
            card = random.choice(trainer_cards)
            # Wenn die Trainer-Karte bereits 4-mal im Deck ist, wähle eine andere
            while not can_add_card(card, mutated_deck, supertype_library):
                card = random.choice(trainer_cards)
            # Füge die Karte zum Deck hinzu
            mutated_deck[index] = card

        elif supertype == 'Pokemon':
            card = random.choice(pokemon_replacement_pool)
            # Wenn die Pokemon-Karte bereits 4-mal im Deck ist, wähle eine andere
            while not can_add_card(card, mutated_deck, supertype_library):
                card = random.choice(pokemon_replacement_pool)
            # Füge die Karte zum Deck hinzu
            mutated_deck[index] = card

    # Testausgabe
    print("mutate() fertig")

    # Return ist das mutierte Deck
    return mutated_deck


# Funktion zur Erzeugung von Mutanten
def mutation(child_deck, pokemon_cards_filename, supertype_library, num_mutants=10, num_mutations=5):
    # Die num_mutants ist eine Angabe, wie viele Decks zu mutieren sind(Original + Kopien)

    # Testausgabe
    print("mutation() aufgerufen")

    pokemon_replacement_pool = load_replacement_pool(pokemon_cards_filename)
    mutated_decks = [mutate(child_deck, pokemon_replacement_pool, supertype_library, num_mutations) for _ in range(num_mutants)]

    print("mutation() fertig")

    # Return sind alle Decks nach der Mutation
    return mutated_decks


# Funktion für die Kreuzung der "besten" Decks
def crossover(parent_deck_1, parent_deck_2):

    # Testausgabe
    print("crossover() aufgerufen")

    if len(parent_deck_1) != 60 or len(parent_deck_2) != 60:
        if len(parent_deck_1) != 60:
            raise ValueError("Fehler: Beide Eltern-Decks müssen genau 60 Karten enthalten. parent_deck_1 falscher Länge")

        if len(parent_deck_2) != 60:
            raise ValueError("Fehler: Beide Eltern-Decks müssen genau 60 Karten enthalten. parent_deck_2 falscher Länge")

    # Sortieren, damit Karten nicht 4 Duplikate überschreiten
    parent_deck_1.sort()
    parent_deck_2.sort()

    child_deck_1 = []
    child_deck_2 = []

    for i in range(60):
        if i % 2 == 0:
            child_deck_1.append(parent_deck_1[i])  # Gerader Index -> Karte von parent_deck_1
            child_deck_2.append(parent_deck_2[i])  # Gerader Index -> Karte von parent_deck_2
        else:
            child_deck_1.append(parent_deck_2[i])  # Ungerader Index -> Karte von parent_deck_2
            child_deck_2.append(parent_deck_1[i])  # Ungerader Index -> Karte von parent_deck_1

    print("crossover() fertig")

    print(child_deck_1)

    print(child_deck_2)
    # Return sind die 2 neue Kinder-Decks
    return child_deck_1, child_deck_2

# Die Hauptfunktion
def genetic_algorithm():

    # Frage nach gewünschtem Type
    pokemon_type = input("Geben Sie den gewünschten Pokémon-Typ (auf Englisch) ein: ")

    # Das relevante replacement_pool der Pokemon auswählen
    pokemon_cards = load_replacement_pool(f"{pokemon_type}_pokemon_cards.csv")
    # Das relevante Pokemon-Typ in die supertype_library hinzufügen
    supertype_library = load_supertype_query_library(f"{pokemon_type}_pokemon_cards.csv")

    # Zufälliges Start-Deck mit dem gewähltem Typ generieren
    initial_deck = create_initial_deck(pokemon_type, pokemon_cards, trainer_cards, energy_cards)

    # Testausgabe
    print("initial_deck: ", initial_deck)

    # Speichern des ersten Decks
    with open("initial_deck.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(initial_deck)

    best_deck = initial_deck
    best_score = 0

    # Anzahl der maximalen Durchläufe, falls best_score nicht den gewünschten Wert erreicht
    # der "erste" Durchlauf mit ganz zufälligem Deck nicht mitgezählt
    max_iterations = 4

    for _ in range(max_iterations):
        print("Iteration Nr.", (_ + 1))

        mutated_decks = mutation(best_deck, f"{pokemon_type}_pokemon_cards.csv", supertype_library)
        scored_decks = [(deck, deck_evaluation_2(rules, deck, a, b, c)) for deck in mutated_decks]

        scored_decks.sort(key=lambda x: x[1], reverse=True)
        parent_deck_1 = scored_decks[0][0]
        parent_deck_2 = scored_decks[1][0]

        # Nochmal die Evaluation des parent_2 abspeichern
        score_parent_2 = deck_evaluation_2(rules, parent_deck_2, a, b, c)

        # wenn das "schlechtere" der Eltern schlechter als alte gen ist, dann stattdessen best_deck nehmen
        if best_score > score_parent_2:
            parent_deck_2 = best_deck

        print("Parentdecks:")
        print(parent_deck_1)
        print(parent_deck_2)

        child_deck_1, child_deck_2 = crossover(parent_deck_1, parent_deck_2)

        score_1 = deck_evaluation_2(rules, child_deck_1, a, b, c)
        score_2 = deck_evaluation_2(rules, child_deck_2, a, b, c)

        if score_1 > best_score or score_2 > best_score:
            best_deck = child_deck_1 if score_1 > score_2 else child_deck_2
            best_score = max(score_1, score_2)

        # Anpassung von best_score-Abbruchkriterium
        if best_score >= 40000:
            break

    # Speichern des besten Decks
    with open("best_deck.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(best_deck)

    print("Bestes Deck:", best_deck)
    print("Die deckBewertung:", best_score)
    if input("Bist du zufrieden? (nein/ja): ") == "nein":
        print("Alternatives Deck:", parent_deck_2)

        # Überschreiben des ersten Decks mit dem Zweitbestem Deck
        with open("best_deck.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(best_deck)

        if input("Bist du zufrieden? (nein/ja): ") == "nein":
            # Nochmal alles von vorne mit neuem Start-Deck
            genetic_algorithm()


if __name__ == "__main__":

    # Test mit testdeck, ob eval funktioniert testdeck = ['Pidgey Obsidian Flames 162','Pidgey Obsidian Flames 162',
    # 'Charmander 151 4','Dusknoir Scarlet & Violet 20','Charizard ex Obsidian Flames 125','Pidgeot ex Obsidian
    # Flames 164','Mew ex 151 151','Fezandipiti ex Scarlet & Violet 38','Chatot Sword & Shield 129','Ditto Scarlet &
    # Violet 132','Tandemaus Scarlet & Violet 73','Shroodle Scarlet & Violet 99','Slaking ex Scarlet & Violet 147',
    # 'Tornadus Scarlet & Violet 120','Slakoth Scarlet & Violet 145','Giacomo Scarlet & Violet 182','Bug Catching Set
    # Scarlet & Violet 143','Canceling Cologne Sword & Shield 136','Wallace Sword & Shield 194','Luxurious Cape
    # Scarlet & Violet 265','Future Booster Energy Capsule Scarlet & Violet 149','Ultra Ball Scarlet & Violet 196',
    # 'Lucian Scarlet & Violet 157','Irida Sword & Shield 147','Friends in Sinnoh Sword & Shield 131',
    # 'Perilous Jungle Scarlet & Violet 156','Salvatore Scarlet & Violet 212','Defiance Vest Scarlet & Violet 162',
    # 'Lucian Scarlet & Violet 208','Beach Court Scarlet & Violet 167','Choice Belt Sword & Shield 211',
    # 'Tulip Scarlet & Violet 181','Perrin Scarlet & Violet 160','Salvatore Scarlet & Violet 202','Picnicker Scarlet
    # & Violet 114','Counter Gain Scarlet & Violet 249',"Janine's Secret Art Scarlet & Violet 59","Cynthia's Ambition
    # Sword & Shield 178","Lana's Aid Scarlet & Violet 155",'Serena Sword & Shield 164',"Daisy's Help Scarlet &
    # Violet 195",'Calamitous Wasteland Scarlet & Violet 175','Iono Scarlet & Violet 254',"Professor's Research (
    # Professor Turo) Scarlet & Violet 241",'Drayton Scarlet & Violet 244',"Giovanni's Charisma Scarlet & Violet
    # 204",'Nemona Scarlet & Violet 82','Sweet Honey Sword & Shield 153','Shauntal Scarlet & Violet 174',
    # "Erika's Invitation Scarlet & Violet 203",'Mist Energy Temporal Forces 161','Mist Energy Temporal Forces 161',
    # 'Mist Energy Temporal Forces 161','Mist Energy Temporal Forces 161','Mist Energy Temporal Forces 161',
    # 'Mist Energy Temporal Forces 161','Mist Energy Temporal Forces 161','Mist Energy Temporal Forces 161',
    # 'Mist Energy Temporal Forces 161','Mist Energy Temporal Forces 161'] deck_evaluation_2(rules, testdeck, a, b, c)
    genetic_algorithm()
