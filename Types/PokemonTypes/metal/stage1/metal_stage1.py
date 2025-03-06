from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q": "types:Metal AND subtypes:Stage AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"}
metal_stage_cards = fetch_pokemon_data(url, params)

metal_stage1_cards = []

for card in metal_stage_cards:
    if "Stage 1" in card.get("subtypes", []):
        metal_stage1_cards.append(card)

df = pd.DataFrame(metal_stage1_cards)
print(df)