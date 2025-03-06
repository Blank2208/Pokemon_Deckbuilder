import time
import pandas as pd
from collections import Counter
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder


# Funktion, um die CSV-Datei zu laden und die Daten für den FP-Growth Algorithmus vorzubereiten
def prepare_data_for_fpgrowth(file_path):
    df = pd.read_csv(file_path)

    # Filterungen
    transactions_list = []

    for deck_name, group in df.groupby('Deck Name'):
        transaction = Counter()
        for _, row in group.iterrows():
            # Verwalte Karten und deren Anzahl
            transaction[row['Card Name']] += 1

        # Expandiere Multimenge in eine Liste mit suffigierten Elementen
        expanded_transaction = [
            f"{card}_{i}" for card, count in transaction.items() for i in range(1, count + 1)
        ]
        transactions_list.append(expanded_transaction)

    # Umwandeln der Transaktionen in FP-Growth Format
    te = TransactionEncoder()
    te_ary = te.fit(transactions_list).transform(transactions_list)
    df_transformed = pd.DataFrame(te_ary, columns=te.columns_)

    return df_transformed


# Funktion, um Assoziationsregeln mit FP-Growth zu erstellen
def generate_association_rules_with_fpgrowth(file_path, min_support, min_threshold):
    print(f"Starten der Datenvorbereitung...")
    df_transformed = prepare_data_for_fpgrowth(file_path)

    # Für die Laufzeit
    start_time = time.time()    # Starten der Laufzeit

    print(f"Starten des FP-Growth Algorithmus mit min_support={min_support} und min_threshold={min_threshold}")
    frequent_itemsets = fpgrowth(df_transformed, min_support=min_support, use_colnames=True)

    end_time = time.time()      # Beenden der Laufzeit
    elapsed_time = end_time - start_time

    print(f"Frequente Itemsets gefunden: {len(frequent_itemsets)}")
    print(f"Zeit für die Berechnung der Itemsets: {elapsed_time:.4f} Sekunden")

    if frequent_itemsets.empty:
        print("Keine häufigen Itemsets gefunden.")
        return None

    print(f"Generierung der Assoziationsregeln...")
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_threshold, num_itemsets=None)

    print(f"Anzahl der generierten Regeln nach Filterung: {len(rules)}")
    # Filterung: Maximal 4 Vorgänger oder Nachfolger
    rules = rules[
        (rules['antecedents'].apply(len) >= 7) &
        (rules['consequents'].apply(len) >= 7)
        ]
    print(f"Anzahl der Regeln nach dem Filter: {len(rules)}")

    if rules.empty:
        print("Keine Assoziationsregeln gefunden.")
        return None

    # Auswahl der gewünschten Spalten
    rules = rules[["antecedents", "consequents", "support", "confidence", "lift"]]

    return rules


# Assoziationsaufruf mit FP-Growth
input_file = "../Assoziationsregeln/Assoziations-Decklisten/Psychic.csv"  # Decks mit Multimengen
min_support = 0.60
# min_confidence = 1
min_threshold = 1

rules = generate_association_rules_with_fpgrowth(
    input_file,
    min_support=min_support,
    min_threshold=min_threshold,
)
# min_confidence=min_confidence

if rules is not None:
    print("Generierte Assoziationsregeln:")
    print(rules)

    # Speicherung der Assoziationsregeln in einer CSV-Datei
    rules.to_csv("Test_fpgrowth_060.csv", index=False)
else:
    print("Es wurden keine Assoziationsregeln generiert.")
