import pandas as pd

# CSV-Datei laden
rules = pd.read_csv("../Create_Deck/assoziationsregeln_multimengen-Pokemon-006.csv")

# Deck definieren
deck = frozenset({'Artazon Unbekannt 171_1', 'Box of Disaster LOR 214_1', 'Basic Fire Energy SVE 10_2', 'Arven Unbekannt 166_1', "Boss's Orders (Ghetsis) Unbekannt 248_1", 'Fuecoco Unbekannt 201_1', 'Basic Fire Energy SVE 10_4', "Team Yell's Cheer BRS 149_1", 'Jubilife Village ASR 212_1', "Roseanne's Backup BRS 180_1", 'Drayton SSP 232_1', 'Precious Trolley SSP 185_1', 'Collapsed Stadium BRS 137_1', 'Basic Fire Energy SVE 10_1', 'Basic Fire Energy SVE 10_6', 'Raboot SCR 147_1', 'Basic Fire Energy SVE 10_9', 'Tulip Unbekannt 244_1', 'Basic Fire Energy SVE 10_5', "Jasmine's Gaze SSP 178_1", 'Entei Unbekannt 112_1', 'Quad Stone SIT 163_1', 'Kindler BRS 170_1', 'Iron Moth Unbekannt 28_1', 'Monferno BRS 25_1', 'Litwick TWM 36_1', 'Primordial Altar SIT 161_1', 'Candice SIT 204_1', 'Gravity Mountain SSP 250_1', 'Jacq Unbekannt 250_1', 'Kieran TWM 218_1', 'Meddling Memo SSP 181_1', 'Kamado ASR 149_1', 'Charcadet SCR 29_1', "Colress's Experiment CRZ GG59_1", 'Charcadet Unbekannt 39_1', 'Thorton LOR 195_1', 'Energy Loto ASR 140_1', 'Kindler BRS 179_1', 'Basic Fire Energy SVE 10_7', "Marnie's Pride BRS 171_1", 'Technical Machine: Evolution Unbekannt 178_1', 'Cinderace ex SCR 157_1', 'Braixen SIT TG01_1', 'Hearthflame Mask Ogerpon ex TWM 192_1', 'Geeta Unbekannt 188_1', 'Basic Fire Energy SVE 10_10', 'Great Ball CRZ 132_1', 'Basic Fire Energy SVE 10_3', 'Salandit SCR 23_1', "Boss's Orders BRS 132_1", 'Vulpix SSP 16_1', 'Deluxe Bomb SCR 134_1', 'Basic Fire Energy SVE 10_8', 'Awakening Drum TEF 141_1', 'Magmar Unbekannt 126_1', 'Larvesta Unbekannt 40_1', 'Fantina LOR 191_1', 'Lure Module PGO 88_1'})

# Gewichtungsfaktoren
a = 1   # Gewichtung für Support
b = 1.2 # Gewichtung für Confidence
c = 2   # Gewichtung für Lift

# Funktion zur Deckbewertung


def deck_evaluation(rules, deck, a, b, c):
    deck_bewertung = 0
    matching_rules = []  # Liste für passende Regeln

    # Über die Regeln iterieren
    for _, rule in rules.iterrows():
        # Antecedents und Consequents in frozensets umwandeln
        antecedents = frozenset(eval(rule['antecedents']))  # 'antecedents' als Set interpretieren
        consequents = frozenset(eval(rule['consequents']))  # Ebenso für 'consequents'

        # Prüfen, ob Antecedents vollständig im Deck sind und ob Consequents vollständig im Deck sind
        if antecedents.issubset(deck) and consequents.issubset(deck):
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

    return deck_bewertung, matching_rules

# Funktion aufrufen und Ergebnisse ausgeben
deck_bewertung, matching_rules = deck_evaluation(rules, deck, a, b, c)

print("\nGefundene Regeln:")
for i, rule in enumerate(matching_rules, start=1):
    print(f"Regel {i}:")
    print(f"  Antecedents: {rule['antecedents']}")
    print(f"  Consequents: {rule['consequents']}")
    print(f"  Support: {rule['support']}")
    print(f"  Confidence: {rule['confidence']}")
    print(f"  Lift: {rule['lift']}")
    print(f"  Regelbewertung: {rule['rule_bewertung']:.2f}")
    print("-" * 30)


print(f"Deckbewertung: {deck_bewertung}")