from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {"q": "id:sve-9 OR id:sve-10 OR id:sve-11 OR id:sve-12 OR id:sve-13 OR id:sve-14 OR id:sve-15 OR id:sve-16"}
# Es gibt mehrere Energy-Versionen, daher habe ich irgendeine id von denen genommen
# Von Links nach Rechts: Grass, Fire, Water, Lightning, Psychic, Fighting, Darkness, Metal
basic_energy_cards = fetch_pokemon_data(url, params)

df = pd.DataFrame(basic_energy_cards)
print(df)