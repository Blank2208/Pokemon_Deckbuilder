from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q": "supertype:Trainer AND subtypes:stadium AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"}
stadium_cards = fetch_pokemon_data(url, params)

df = pd.DataFrame(stadium_cards)
print(df)