from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q": "name:regidrago AND number:135"}
a_card = fetch_pokemon_data(url, params)

df = pd.DataFrame(a_card)
print(df)

# Evaluation der karten an sich, potenziell Usage-Rate?
