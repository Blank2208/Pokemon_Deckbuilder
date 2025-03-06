from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q": "types:Lightning AND subtypes:Stage AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"}
lightning_stage_cards = fetch_pokemon_data(url, params)

lightning_stage2_cards = []

for card in lightning_stage_cards:
    if "Stage 2" in card.get("subtypes", []):
        lightning_stage2_cards.append(card)

df = pd.DataFrame(lightning_stage2_cards)
print(df)