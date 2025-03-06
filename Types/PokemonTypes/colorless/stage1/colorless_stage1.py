from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q": "types:Colorless AND subtypes:Stage AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"}
colorless_stage_cards = fetch_pokemon_data(url, params)

colorless_stage1_cards = []

for card in colorless_stage_cards:
    if "Stage 1" in card.get("subtypes", []):
        colorless_stage1_cards.append(card)

df = pd.DataFrame(colorless_stage1_cards)
print(df)