from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q": "types:Colorless AND subtypes:Basic AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"}
colorless_basic_cards = fetch_pokemon_data(url, params)

df = pd.DataFrame(colorless_basic_cards)
sort_df = df.sort_values(by="name", ascending=True)
print(sort_df)