import random


def get_energy_card_for_type(pokemon_type):
    energy_map = {
        "Darkness": "Basic Darkness Energy Scarlet & Violet 15",
        "Dragon": "Basic Grass Energy Scarlet & Violet 9",  # Drachen nutzen verschiedene Energien
        "Fighting": "Basic Fighting Energy Scarlet & Violet 14",
        "Fire": "Basic Fire Energy Scarlet & Violet 10",
        "Grass": "Basic Grass Energy Scarlet & Violet 9",
        "Lightning": "Basic Lightning Energy Scarlet & Violet 12",
        "Metal": "Basic Metal Energy Scarlet & Violet 16",
        "Psychic": "Basic Psychic Energy Scarlet & Violet 13",
        "Water": "Basic Water Energy Scarlet & Violet 11",
    }
    return energy_map.get(pokemon_type)  # Error-Validation wird vorher abgerufen


def get_specific_type_deck_1x(pokemon_type):
    set_trainer = {
        "Colorless": {
            'Bloodmoon Ursaluna ex Twilight Masquerade 141',
            'Lumineon V Brilliant Stars 40',
            'Rotom V Lost Origin 58',
            'Wellspring Mask Ogerpon ex Twilight Masquerade 64',

            "Boss's Orders Paldea Evolved 172",
            'Bravery Charm Paldea Evolved 173',
            'Forest Seal Stone Silver Tempest 156',
            'Hisuian Heavy Ball Astral Radiance 146',
            'Iono Paldea Evolved 185',
            'Night Stretcher Shrouded Fable 61',
            'Pal Pad Scarlet & Violet 182',
            'Thorton Lost Origin 167',
        },

        "Darkness": {
            "Fezandipiti ex Shrouded Fable 38",
            'Pecharunt ex Shrouded Fable 39',
            'Radiant Greninja Astral Radiance 46',
            "Roaring Moon Temporal Forces 109",

            "Boss's Orders Paldea Evolved 172",
            'Dark Patch Astral Radiance 139',
            'Night Stretcher Shrouded Fable 61',
            'Pal Pad Scarlet & Violet 182',
        },

        "Dragon": {
            'Fezandipiti ex Shrouded Fable 38',
            'Radiant Greninja Astral Radiance 46',
            'Squawkabilly ex Paldea Evolved 169',

            'Pal Pad Scarlet & Violet 182',
            'Pokémon Catcher Scarlet & Violet 187',
            'PokéStop Pokémon GO 68',
            'Prime Catcher Temporal Forces 157',
            'Slither Wing Paradox Rift 107',
        },

        "Fighting": {
            "Frogadier Twilight Masquerade 57",
            'Pidgeot ex Obsidian Flames 164',
            'Rotom V Lost Origin 58',

            'Counter Catcher Paradox Rift 160',
            'Forest Seal Stone Silver Tempest 156',
            'Nest Ball Scarlet & Violet 181',
            'Super Rod Paldea Evolved 188',

            'Double Turbo Energy Brilliant Stars 151',
        },

        "Fire": {
            'Fezandipiti ex Shrouded Fable 38',
            'Flutter Mane Temporal Forces 78',
            'Munkidori Twilight Masquerade 95',
            'Radiant Greninja Astral Radiance 46',
            'Squawkabilly ex Paldea Evolved 169',

            "Boss's Orders Paldea Evolved 172",
            'Forest Seal Stone Silver Tempest 156',
            'Secret Box Twilight Masquerade 163',
        },

        "Grass": {
            'Cleffa Obsidian Flames 80',
            'Dragapult ex Twilight Masquerade 130',
            'Fezandipiti ex Shrouded Fable 38',
            'Giratina VSTAR Lost Origin 131',
            'Hisuian Goodra VSTAR Lost Origin 136',
            'Kyurem Shrouded Fable 47',
            'Mew ex 151 151',
            'Radiant Charizard Crown Zenith 20',
            'Squawkabilly ex Paldea Evolved 169',

            'Canceling Cologne Astral Radiance 136',
            'Jamming Tower Twilight Masquerade 153',
            'Prime Catcher Temporal Forces 157',
            'Switch Scarlet & Violet 194',
        },

        "Lightning": {
            "Fezandipiti ex Shrouded Fable 38",
            "Iron Bundle Paradox Rift 56",
            "Latias ex Surging Sparks 76",
            "Mew ex 151 151",
            "Lumineon V Brilliant Stars 40",
            "Pikachu ex Surging Sparks 57",
            "Raichu V Brilliant Stars 45",
            "Rotom V Lost Origin 58",
            "Squawkabilly ex Paldea Evolved 169",

            'Double Turbo Energy Brilliant Stars 151',
        },

        "Metal": {
            'Fezandipiti ex Shrouded Fable 38',
            'Radiant Greninja Astral Radiance 46',

            'Nest Ball Scarlet & Violet 181',
            'Pokégear 3.0 Scarlet & Violet 186',
            "Professor Turo's Scenario Paradox Rift 171",
        },

        "Psychic": {
            'Munkidori Twilight Masquerade 95',
            'Scream Tail Paradox Rift 86',

            'Artazon Paldea Evolved 171',
            "Boss's Orders Paldea Evolved 172",
            'Counter Catcher Paradox Rift 160',
            'Nest Ball Scarlet & Violet 181',
            "Professor Turo's Scenario Paradox Rift 171",
            'Super Rod Paldea Evolved 188',
        },

        "Water": {
            'Radiant Greninja Astral Radiance 46',

            'Hisuian Heavy Ball Astral Radiance 146',
            'PokéStop Pokémon GO 68',
            'Super Rod Paldea Evolved 188',
        }
    }

    return set_trainer.get(pokemon_type, None)


def get_specific_type_deck_2x(pokemon_type):
    set_trainer = {
        "Colorless": {
            "Pidgey Obsidian Flames 162",
            "Pidgeot ex Obsidian Flames 164",

            "Counter Catcher Paradox Rift 160",
            "Penny Scarlet & Violet 183",
            "Rare Candy Scarlet & Violet 191",

            "Double Turbo Energy Brilliant Stars 151",
        },

        "Darkness": {
            "Ultra Ball Scarlet & Violet 196",
        },

        "Dragon": {
            "Energy Retrieval Scarlet & Violet 171",
            "Night Stretcher Shrouded Fable 61",
            "Pokégear 3.0 Scarlet & Violet 186",
        },

        "Fighting": {
            "Froakie Obsidian Flames 56",
            "Greninja ex Twilight Masquerade 106",

            "Iono Paldea Evolved 185",

            "Water Energy Scarlet & Violet 11",
        },

        "Fire": {
            "Energy Switch Scarlet & Violet 173",

            "Darkness Energy Scarlet & Violet 15",
        },

        "Grass": {
            "Boss's Orders Paldea Evolved 172",
            "Iono Paldea Evolved 185",
            "Super Rod Paldea Evolved 188",

            "Fire Energy Scarlet & Violet 10",
        },

        "Lightning": {
            "Iron Thorns ex Twilight Masquerade 77",
            "Miraidon ex Scarlet & Violet 81",

            "Arven Obsidian Flames 186",
            "Pokégear 3.0 Scarlet & Violet 186",

        },

        "Metal": {
            "Boss's Orders Paldea Evolved 172",
            "Professor's Research Scarlet & Violet 189",
        },

        "Psychic": {
            "Ralts Astral Radiance 60",
            "Ralts Silver Tempest 67",
            "Gardevoir ex Scarlet & Violet 86",

            "Ultra Ball Scarlet & Violet 196",
        },

        "Water": {
            "Baxcalibur Paldea Evolved 60",
            "Chien-Pao ex Paldea Evolved 61",
        }
    }

    return set_trainer.get(pokemon_type, None)


def get_specific_type_deck_3x(pokemon_type):
    set_trainer = {
        "Colorless": {
            "Ultra Ball Scarlet & Violet 196",
        },

        "Darkness": {
            "Nest Ball Scarlet & Violet 181",
            "PokéStop Pokémon GO 68",
        },

        "Dragon": {
            "Raging Bolt ex Temporal Forces 123",
            "Teal Mask Ogerpon ex Twilight Masquerade 25",

            "Fighting Energy Scarlet & Violet 14",
            "Lightning Energy Scarlet & Violet 12",
        },

        "Fighting": {
            "Arven Obsidian Flames 186",
            "Ultra Ball Scarlet & Violet 196",
        },

        "Fire": {
            "Gouging Fire ex Temporal Forces 38",

            "Earthen Vessel Paradox Rift 163",
            "Magma Basin Brilliant Stars 144",
            "Nest Ball Scarlet & Violet 181",
            "Ultra Ball Scarlet & Violet 196",

            "Jet Energy Paldea Evolved 190",
        },

        "Grass": {
            "Regidrago V Silver Tempest 135",
            "Regidrago VSTAR Silver Tempest 136",
            "Teal Mask Ogerpon ex Twilight Masquerade 25",
        },

        "Lightning": {
            "Boss's Orders Paldea Evolved 172",
            "Nest Ball Scarlet & Violet 181",
            "Professor's Research Scarlet & Violet 189",
            "Ultra Ball Scarlet & Violet 196",
        },

        "Metal": {
            "Archaludon ex Surging Sparks 130",
            "Duraludon Stellar Crown 106",

            "Earthen Vessel Paradox Rift 163",
            "Night Stretcher Shrouded Fable 61",
        },

        "Psychic": {
            "Iono Paldea Evolved 185",
        },

        "Water": {
            'Frigibax Paldea Evolved 57',

            "Buddy-Buddy Poffin Temporal Forces 144",
            "Nest Ball Scarlet & Violet 181",
            "Rare Candy Scarlet & Violet 191",
        }
    }

    return set_trainer.get(pokemon_type, None)


def get_specific_type_deck_4x(pokemon_type):
    set_trainer = {
        "Colorless": {
            "Arven Obsidian Flames 186",
            "Nest Ball Scarlet & Violet 181",
        },

        "Darkness": {
            "Earthen Vessel Paradox Rift 163",
            "Professor Sada's Vitality Paradox Rift 170",
        },

        "Dragon": {
            "Earthen Vessel Paradox Rift 163",
            "Nest Ball Scarlet & Violet 181",
            "Professor Sada's Vitality Paradox Rift 170",
        },

        "Fighting": {
            "Buddy-Buddy Poffin Temporal Forces 144",
            "Rare Candy Scarlet & Violet 191",
        },

        "Fire": {
            "Professor Sada's Vitality Paradox Rift 170",
        },

        "Grass": {
            "Earthen Vessel Paradox Rift 163",
            "Energy Switch Scarlet & Violet 173",
            "Nest Ball Scarlet & Violet 181",
            "Professor's Research Scarlet & Violet 189",
            "Ultra Ball Scarlet & Violet 196",
        },

        "Lightning": {

        },

        "Metal": {
            "Ultra Ball Scarlet & Violet 196",
        },

        "Psychic": {
            "Kirlia Silver Tempest 68",

            "Buddy-Buddy Poffin Temporal Forces 144",
        },

        "Water": {
            "Irida Astral Radiance 147",
            "Superior Energy Retrieval Paldea Evolved 189",
        }
    }

    return set_trainer.get(pokemon_type, None)


# Initialisierung des Decks mit anpassbarer Energie
def create_initial_deck(pokemon_type, pokemon_cards, trainer_cards, energy_cards):
    # Die richtige Energie-Karte für den Pokémon-Typ bestimmen
    chosen_energy = get_energy_card_for_type(pokemon_type)
    chosen_deck_1 = get_specific_type_deck_1x(pokemon_type)
    chosen_deck_2 = get_specific_type_deck_2x(pokemon_type)
    chosen_deck_3 = get_specific_type_deck_3x(pokemon_type)
    chosen_deck_4 = get_specific_type_deck_4x(pokemon_type)
    # Erstelle das Deck mit Angaben, wie viele Karten welcher Art im Deck gehören
    # WICHTIG: Insgesamt genau 60!!! --> Intervall: Pokemon = 10 bis 20; Trainer = 30 bis 40; Energy = 4 bis 14


    if pokemon_type == "Colorless":
        initial_deck = (
            random.sample(pokemon_cards, 7) +
            [f"{card}" for card in chosen_deck_1 for i in range(1)] +       # Insgesamt Pokemon: 4, Trainer: 8, Energy: 0
            [f"{card}" for card in chosen_deck_2 for i in range(2)] +       # Insgesamt Pokemon: 4, Trainer: 6, Energy: 2
            [f"{card}" for card in chosen_deck_3 for i in range(3)] +       # Insgesamt Pokemon: 0, Trainer: 3, Energy: 0
            [f"{card}" for card in chosen_deck_4 for i in range(4)] +       # Insgesamt Pokemon: 0, Trainer: 8, Energy: 0
            random.sample(energy_cards, 8) +
            random.sample(trainer_cards, 10)
        )

    elif pokemon_type == "Darkness":
        initial_deck = (
            random.sample(pokemon_cards, 11) +
            [f"{card}" for card in chosen_deck_1 for i in range(1)] +       # Insgesamt Pokemon: 4, Trainer: 4, Energy: 0
            [f"{card}" for card in chosen_deck_2 for i in range(2)] +       # Insgesamt Pokemon: 0, Trainer: 2, Energy: 0
            [f"{card}" for card in chosen_deck_3 for i in range(3)] +       # Insgesamt Pokemon: 0, Trainer: 6, Energy: 0
            [f"{card}" for card in chosen_deck_4 for i in range(4)] +       # Insgesamt Pokemon: 0, Trainer: 8, Energy: 0
            [f"{chosen_energy}" for i in range(10)] +                       # Im gewählten Deck eigentlich nur 6 Dark Energy
            random.sample(trainer_cards, 15)
        )

    elif pokemon_type == "Dragon":
        initial_deck = (
            random.sample(pokemon_cards, 6) +
            [f"{card}" for card in chosen_deck_1 for i in range(1)] +       # Insgesamt Pokemon: 3, Trainer: 5, Energy: 0
            [f"{card}" for card in chosen_deck_2 for i in range(2)] +       # Insgesamt Pokemon: 0, Trainer: 6, Energy: 0
            [f"{card}" for card in chosen_deck_3 for i in range(3)] +       # Insgesamt Pokemon: 6, Trainer: 0, Energy: 6
            [f"{card}" for card in chosen_deck_4 for i in range(4)] +       # Insgesamt Pokemon: 0, Trainer: 12, Energy: 0
            [f"{chosen_energy}" for i in range(6)] +
            random.sample(trainer_cards,10)
        )

    elif pokemon_type == "Fighting":
        initial_deck = (
            random.sample(pokemon_cards, 8) +
            [f"{card}" for card in chosen_deck_1 for i in range(1)] +       # Insgesamt Pokemon: 3, Trainer: 4, Energy: 1
            [f"{card}" for card in chosen_deck_2 for i in range(2)] +       # Insgesamt Pokemon: 4, Trainer: 2, Energy: 2
            [f"{card}" for card in chosen_deck_3 for i in range(3)] +       # Insgesamt Pokemon: 0, Trainer: 6, Energy: 0
            [f"{card}" for card in chosen_deck_4 for i in range(4)] +       # Insgesamt Pokemon: 0, Trainer: 8, Energy: 0
            [f"{chosen_energy}" for i in range(3)] +
            random.sample(energy_cards, 4) +
            random.sample(trainer_cards, 15)
        )

    elif pokemon_type == "Fire":
        initial_deck = (
            random.sample(pokemon_cards, 7) +
            [f"{card}" for card in chosen_deck_1 for i in range(1)] +      # Insgesamt Pokemon: 5, Trainer: 3, Energy: 0
            [f"{card}" for card in chosen_deck_2 for i in range(2)] +      # Insgesamt Pokemon: 0, Trainer: 2, Energy: 2
            [f"{card}" for card in chosen_deck_3 for i in range(3)] +      # Insgesamt Pokemon: 3, Trainer: 12, Energy: 3
            [f"{card}" for card in chosen_deck_4 for i in range(4)] +      # Insgesamt Pokemon: 0, Trainer: 4, Energy: 0
            [f"{chosen_energy}" for i in range(6)] +                       # Im gewählten Deck eigentlich nur 6 Fire Energy
            random.sample(trainer_cards, 13)
        )

    elif pokemon_type == "Grass":
        initial_deck = (
            [f"{card}" for card in chosen_deck_1 for i in range(1)] +       # Insgesamt Pokemon: 9, Trainer: 4, Energy: 0
            [f"{card}" for card in chosen_deck_2 for i in range(2)] +       # Insgesamt Pokemon: 0, Trainer: 6, Energy: 2
            [f"{card}" for card in chosen_deck_3 for i in range(3)] +       # Insgesamt Pokemon: 9, Trainer: 0, Energy: 0
            [f"{card}" for card in chosen_deck_4 for i in range(4)] +       # Insgesamt Pokemon: 0, Trainer: 20, Energy: 0
            [f"{chosen_energy}" for i in range(7)] +                        # Im gewählten Deck nur 7 Grass Energy
            random.sample(trainer_cards, 3)
        )

    elif pokemon_type == "Lightning":
        initial_deck = (
            random.sample(pokemon_cards, 2) +
            [f"{card}" for card in chosen_deck_1 for i in range(1)] +       # Insgesamt Pokemon: 9, Trainer: 0, Energy: 1
            [f"{card}" for card in chosen_deck_2 for i in range(2)] +       # Insgesamt Pokemon: 4, Trainer: 4, Energy: 0
            [f"{card}" for card in chosen_deck_3 for i in range(3)] +       # Insgesamt Pokemon: 0, Trainer: 12, Energy: 0
            [f"{card}" for card in chosen_deck_4 for i in range(4)] +       # Insgesamt Pokemon: 0, Trainer: 0, Energy: 0
            [f"{chosen_energy}" for i in range(9)] +                        # Im gewählten Deck nur 7 Lightning Energy
            random.sample(trainer_cards, 19)
        )

    elif pokemon_type == "Metal":
        initial_deck = (
            random.sample(pokemon_cards, 7) +
            [f"{card}" for card in chosen_deck_1 for i in range(1)] +       # Insgesamt Pokemon: 2, Trainer: 3, Energy: 0
            [f"{card}" for card in chosen_deck_2 for i in range(2)] +       # Insgesamt Pokemon: 0, Trainer: 4, Energy: 0
            [f"{card}" for card in chosen_deck_3 for i in range(3)] +       # Insgesamt Pokemon: 6, Trainer: 6, Energy: 0
            [f"{card}" for card in chosen_deck_4 for i in range(4)] +       # Insgesamt Pokemon: 0, Trainer: 4, Energy: 0
            [f"{chosen_energy}" for i in range(8)] +                        # Im gewählten Deck nur 8 Metal Energy
            random.sample(trainer_cards, 20)
        )

    elif pokemon_type == "Psychic":
        initial_deck = (
            random.sample(pokemon_cards, 3) +
            [f"{card}" for card in chosen_deck_1 for i in range(1)] +       # Insgesamt Pokemon: 2, Trainer: 6, Energy: 0
            [f"{card}" for card in chosen_deck_2 for i in range(2)] +       # Insgesamt Pokemon: 6, Trainer: 2, Energy: 0
            [f"{card}" for card in chosen_deck_3 for i in range(3)] +       # Insgesamt Pokemon: 0, Trainer: 3, Energy: 0
            [f"{card}" for card in chosen_deck_4 for i in range(4)] +       # Insgesamt Pokemon: 4, Trainer: 4, Energy: 0
            [f"{chosen_energy}" for i in range(6)] +                        # Im gewählten Deck nur 6 Psychic Energy
            random.sample(trainer_cards, 24)
        )

    elif pokemon_type == "Water":
        initial_deck = (
            random.sample(pokemon_cards, 7) +
            [f"{card}" for card in chosen_deck_1 for i in range(1)] +       # Insgesamt Pokemon: 1, Trainer: 3, Energy: 0
            [f"{card}" for card in chosen_deck_2 for i in range(2)] +       # Insgesamt Pokemon: 4, Trainer: 0, Energy: 0
            [f"{card}" for card in chosen_deck_3 for i in range(3)] +       # Insgesamt Pokemon: 3, Trainer: 9, Energy: 0
            [f"{card}" for card in chosen_deck_4 for i in range(4)] +       # Insgesamt Pokemon: 0, Trainer: 8, Energy: 0
            [f"{chosen_energy}" for i in range(8)] +                        # Im gewählten Deck nur 8 Water Energy
            random.sample(trainer_cards, 17)
        )

    else:
        raise ValueError(f"Pokemon type {pokemon_type} not supported")

    return initial_deck
