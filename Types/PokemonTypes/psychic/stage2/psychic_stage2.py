from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q": "types:Psychic AND subtypes:Stage AND (regulationMark:F OR regulationMark:G OR regulationMark:H)"}
psychic_stage_cards = fetch_pokemon_data(url, params)

psychic_stage2_cards = []

for card in psychic_stage_cards:
    if "Stage 2" in card.get("subtypes", []):
        psychic_stage2_cards.append(card)

df = pd.DataFrame(psychic_stage2_cards)
print(df)