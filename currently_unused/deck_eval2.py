rules = pd.read_csv("assoziationsregeln_multimengen-Pokemon-006.csv")

# Gewichtungsfaktoren
a = 1   # Gewichtung für Support
b = 1.2 # Gewichtung für Confidence
c = 2   # Gewichtung für Lift

# Funktion zur Deckbewertung
def deck_evaluation_2(rules, deck, a, b, c):

    print("deck_evaluation() aufgerufen")

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

    print("deck_bewertung: ", deck_bewertung)

    # return ist ein int-Wert
    return deck_bewertung
