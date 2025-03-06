from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q": "types:Fighting AND subtypes:Basic AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"}
fighting_basic_cards = fetch_pokemon_data(url, params)

df = pd.DataFrame(fighting_basic_cards)
print(df)