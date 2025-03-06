from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q": "supertype:Trainer AND subtypes:Supporter AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"}
supporter_cards = fetch_pokemon_data(url, params)

df = pd.DataFrame(supporter_cards)
print(df)