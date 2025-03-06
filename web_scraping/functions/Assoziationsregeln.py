import time
import pandas as pd
from collections import Counter
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder


# Funktion, um die CSV-Datei zu laden und die Daten für den Apriori-Algorithmus vorzubereiten
def prepare_data_for_apriori(file_path):
    # Gesamte Deckliste(n) werden geladen
    df = pd.read_csv(file_path)

    # Filterungen
    # df_pokemon = df[df['Type'] == 'Pokemon']
    # df_trainer = df[df['Type'] == 'Trainer']
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

    # Umwandeln der Transaktionen in Apriori Format
    te = TransactionEncoder()
    te_ary = te.fit(transactions_list).transform(transactions_list)
    df_transformed = pd.DataFrame(te_ary, columns=te.columns_)

    return df_transformed


# Funktion, um Assoziationsregeln aus den Deck-Daten zu erstellen
def generate_association_rules(file_path, min_support, min_threshold):
    print(f"Starten der Datenvorbereitung...")
    df_transformed = prepare_data_for_apriori(file_path)

    print(f"Starten des Apriori-Algorithmus mit min_support={min_support}")

    start_time = time.time()
    frequent_itemsets = apriori(df_transformed, min_support=min_support, use_colnames=True)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Frequente Itemsets gefunden: {len(frequent_itemsets)}")
    print(f"Benötigte Laufzeit: {elapsed_time:.4f}")

    if frequent_itemsets.empty:
        print("Keine häufigen Itemsets gefunden.")
        return None

    print(f"Generierung der Assoziationsregeln...")
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_threshold, num_itemsets=None)
    print(f"Anzahl der generierten Regeln: {len(rules)}")

    # Filterung: Maximal 4 Vorgänger oder Nachfolger
    rules = rules[
        (rules['antecedents'].apply(len) <= 3) &
        (rules['consequents'].apply(len) <= 3)
        ]
    print(f"Anzahl der Regeln nach dem Filter: {len(rules)}")

    if rules.empty:
        print("Keine Assoziationsregeln gefunden.")
        return None

    # Auswahl der gewünschten Spalten
    rules = rules[["antecedents", "consequents", "support", "confidence", "lift"]]

    return rules


# Assoziationsaufruf
input_file = "../decklisten/decks_anpassung.csv"  # Decks mit Multimengen
rules = generate_association_rules(input_file, min_support=0.30, min_threshold=1)

if rules is not None:
    print("Generierte Assoziationsregeln:")
    print(rules)

    # Speicherung der Assoziationsregeln in einer CSV-Datei
    rules.to_csv("assoziationsregeln_multimengen-030.csv", index=False)
else:
    print("Es wurden keine Assoziationsregeln generiert.")
