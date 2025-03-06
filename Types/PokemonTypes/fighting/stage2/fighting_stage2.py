from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q": "types:Fighting AND subtypes:Stage AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"}
fighting_stage_cards = fetch_pokemon_data(url, params)

fighting_stage2_cards = []

for card in fighting_stage_cards:
    if "Stage 2" in card.get("subtypes", []):
        fighting_stage2_cards.append(card)

df = pd.DataFrame(fighting_stage2_cards)
print(df)