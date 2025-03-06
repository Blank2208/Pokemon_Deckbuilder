from funktion import fetch_pokemon_data
import pandas as pd

url = "https://api.pokemontcg.io/v2/cards"  # API URL
params = {
    "q": (
        "id:ex4-86 OR id:swsh4-162 OR id:swsh1-186 OR id:bw6-117 OR id:bw6-118 OR id:sv6-166 OR id:pop5-8 OR "
        "id:ecard3-142 OR id:xy8-151 OR id:dp5-92 OR id:swsh3-201 OR id:swsh4-163 OR id:sm4-122 OR id:ecard3-143 OR "
        "id:xy7-82 OR id:ex7-94 OR id:ecard2-142 OR id:dc1-33 OR id:sm2-166 OR id:xy6-97 OR id:dc1-34 OR "
        "id:ex14-88 OR id:swsh10-216 OR id:sm12-271 OR id:xy7-83 OR id:base6-100 OR id:swsh11-171 OR id:dp5-94 OR "
        "id:swsh3-174 OR id:xy3-103 OR id:swsh3-175 OR id:ex11-104 OR id:ex11-105 OR id:ex11-106 OR id:swsh2-172 OR "
        "id:sv8-252 OR id:swsh6-158 OR id:sv6-226 OR id:ex4-87 OR id:sv4-182 OR id:sm8-194 OR id:ecard2-143 OR "
        "id:neo4-16 OR id:sv5-161 OR id:dp2-118 OR id:xy4-112 OR id:base6-101 OR id:swsh3-176 OR id:bw4-93 OR "
        "id:ex7-95 OR id:sm7-183 OR id:swsh5-182 OR id:ex12-82 OR id:dp5-96 OR id:sm11-257 OR id:swsh12-168 OR "
        "id:hgss4-90 OR id:ecard3-144 OR id:sv4-266 OR id:ex15-89 OR id:xy5-143 OR id:pl2-101 OR id:swsh2-173 OR "
        "id:swsh6-159 OR id:xy9-113 OR id:swsh4-164 OR id:xy10-115 OR id:sv2-193 OR id:swsh7-165 OR id:sm10-234 OR "
        "id:swsh2-209 OR id:sm6-146 OR id:sm5-170 OR id:sm5-171 OR id:pl2-102 OR id:swsh12-215 OR id:ecard2-147 OR "
        "id:swsh4-165 OR id:sm11-258 OR id:xy5-144 OR id:ex13-98"
    )
}
# Es gibt mehrere Energy-Versionen, daher habe ich irgendeine id von denen genommen
special_energy_cards = fetch_pokemon_data(url, params)

df = pd.DataFrame(special_energy_cards)
sort_df = df.sort_values(by="name", ascending=True)
print(sort_df)