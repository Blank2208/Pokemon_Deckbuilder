# Die Pokemon, die man universell in Decks spielen könnte, weil ihre Ability dies erlaubt
from funktion import fetch_pokemon_data
import pandas as pd

url = 'https://api.pokemontcg.io/v2/cards'
params = {"q": "id:swsh12pt5gg-GG39 OR id:swsh12pt5gg-GG14 OR id:sv2-97 OR id:swshp-SWSH297 OR id:swsh12pt5-111 OR "
               "id:swsh9-121 OR id:swsh9-41 OR id:swsh12pt5-95 OR id:swsh11-58 OR id:sv4pt5-223 OR id:sv3-164 OR "
               "id:sv3-162 OR id:sv3-163"}

supporter_cards = fetch_pokemon_data(url, params)

pd = pd.DataFrame(supporter_cards)
print(pd)