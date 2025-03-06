from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q": "types:Dragon AND subtypes:Basic AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"}
dragon_basic_cards = fetch_pokemon_data(url, params)

df = pd.DataFrame(dragon_basic_cards)
print(df)