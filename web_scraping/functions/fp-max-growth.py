import time
import pandas as pd
from collections import Counter
from mlxtend.frequent_patterns import fpmax
from mlxtend.preprocessing import TransactionEncoder


# Funktion, um die CSV-Datei zu laden und die Daten für den FPMax-Algorithmus vorzubereiten
def prepare_data_for_fpmax(file_path):
    df = pd.read_csv(file_path)

    transactions_list = []
    for deck_name, group in df.groupby('Deck Name'):
        transaction = Counter()
        for _, row in group.iterrows():
            transaction[row['Card Name']] += 1

        # Expandiere Multimenge in eine Liste mit suffigierten Elementen
        expanded_transaction = [
            f"{card}_{i}" for card, count in transaction.items() for i in range(1, count + 1)
        ]
        transactions_list.append(expanded_transaction)

    # Umwandeln der Transaktionen in FPMax Format
    te = TransactionEncoder()
    te_ary = te.fit(transactions_list).transform(transactions_list)
    df_transformed = pd.DataFrame(te_ary, columns=te.columns_)

    return df_transformed


# Funktion, um maximale frequentierte Itemsets mit FPMax zu erstellen
def generate_maximal_itemsets_with_fpmax(file_path, min_support):
    print(f"Starten der Datenvorbereitung...")
    df_transformed = prepare_data_for_fpmax(file_path)

    # Laufzeitmessung für die Itemset-Berechnung
    start_time = time.time()

    print(f"Starten des FPMax Algorithmus mit min_support={min_support}")
    maximal_itemsets = fpmax(df_transformed, min_support=min_support, use_colnames=True)

    end_time = time.time()  # Zeitmessung beenden
    elapsed_time = end_time - start_time  # Berechnete Zeit in Sekunden

    print(f"Maximale Itemsets gefunden: {len(maximal_itemsets)}")
    print(f"Zeit für die Berechnung der maximalen Itemsets: {elapsed_time:.4f} Sekunden")

    if maximal_itemsets.empty:
        print("Keine maximalen Itemsets gefunden.")
        return None

    return maximal_itemsets


# FPMax-Algorithmus ausführen
input_file = "../Assoziationsregeln/Assoziations-Decklisten/Water.csv"
min_support = 0.35

maximal_itemsets = generate_maximal_itemsets_with_fpmax(
    input_file,
    min_support=min_support
)

if maximal_itemsets is not None:
    print("Vor dem Filtern:", len(maximal_itemsets))

    # Filtern der Itemsets mit maximal 40 Karten
    maximal_itemsets['itemsets'] = maximal_itemsets['itemsets'].apply(lambda x: list(x))
    maximal_itemsets = maximal_itemsets[(maximal_itemsets['itemsets'].apply(len) >= 30) & (maximal_itemsets['itemsets'].apply(len) <= 40)]
    # Falls mehrere gültige Itemsets übrig bleiben, bestes nach Support auswählen
    # maximal_itemsets = maximal_itemsets.sort_values(by='support', ascending=False).iloc[:1]

    #print("Nach dem Filtern:", len(maximal_itemsets))

    if not maximal_itemsets.empty:
        print("Generierte maximale Itemsets:")
        print(maximal_itemsets)

        # Speicherung in einer CSV-Datei
        maximal_itemsets.to_csv("Water_fpmax_035_filtered.csv", index=False)
    else:
        print("Keine gültigen Itemsets mit maximal 40 Karten gefunden.")
else:
    print("Es wurden keine maximalen Itemsets generiert.")

