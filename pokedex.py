from moves import Move

pokedex = {
    1: {
        'poke_index': 1,
        'name': 'Bulbasaur',
        'type_of_pokemon': ['Grass'],
        'nature': '',
        'moves': {
            'Growl': Move('Growl', 'Normal', 40, None, 100),
            'Tackle': Move('Tackle', 'Normal', 35, 40, 100),
            'Vine Whip': Move('Vine Whip', 'Grass', 25, 45, 100),
            'Growth': Move('Growth', 'Normal', 20, None, None)
        },
        'health': 451
    },
    4: {
        'poke_index': 4,
        'name': 'Charmander',
        'type_of_pokemon': ['Fire'],
        'nature': '',
        'moves': {
            'Growl': Move('Growl', 'Normal', 40, None, 100),
            'Scratch': Move('Scratch', 'Normal', 35, 40, 100),
            'Ember': Move('Ember', 'Fire', 25, 40, 100),
            'Smokescreen': Move('Smokescreen', 'Normal', 20, None, 100)
        },
        'health': 451
    },
    7: {
        'poke_index': 7,
        'name': 'Squirtle',
        'type_of_pokemon': ['Water'],
        'nature': '',
        'moves': {
            'Tackle': Move('Tackle', 'Normal', 35, 40, 100),
            'Tail Whip': Move('Tail Whip', 'Normal', 30, None, 100),
            'Water Gun': Move('Water Gun', 'Water', 25, 40, 100),
            'Withdraw': Move('Withdraw', 'Water', 40, None, None)
        },
        'health': 443
    },
    10: {
        'poke_index': 10,
        'name': 'Caterpie',
        'type_of_pokemon': ['Bug'],
        'nature': '',
        'moves': {
            'String Shot': Move('String Shot', 'Bug', 40, None, 95),
            'Tackle': Move('Tackle', 'Normal', 35, 40, 100),
            'Bug Bite': Move('Bug Bite', 'Bug', 20, 60, 100)
        },
        'health': 451
    },
    13: {
        'poke_index': 13,
        'name': 'Weedle',
        'type_of_pokemon': ['Bug', 'Poison'],
        'nature': '',
        'moves': {
            'Poison Sting': Move('Poison String', 'Poison', 35, 15, 100),
            'String Shot': Move('String Shot', 'Bug', 40, None, 95),
            'Bug Bite': Move('Bug Bite', 'Bug', 20, 60, 100)
        },
        'health': 451
    },
    16: {
        'poke_index': 16,
        'name': 'Pidgey',
        'type_of_pokemon': ['Normal', 'Flying'],
        'nature': '',
        'moves': {
            'Tackle': Move('Tackle', 'Normal', 35, 40, 100),
            'Sand Attack': Move('Sand Attack', 'Ground', 15, None, 100),
            'Gust': Move('Gust', 'Flying', 35, 40, 100),
            'Quick Attack': Move('Quick Attack', 'Normal', 30, 40, 100)
        },
        'health': 451
    },
    19: {
        'poke_index': 19,
        'name': 'Rattata',
        'type_of_pokemon': ['Normal'],
        'nature': '',
        'moves': {
            'Tackle': Move('Tackle', 'Normal', 35, 40, 100),
            'Tail Whip': Move('Tail Whip', 'Normal', 30, None, 100),
            'Quick Attack': Move('Quick Attack', 'Normal', 30, 40, 100),
            'Focus Energy': Move('Focus Energy', 'Normal', 30, None, None)
        },
        'health': 451
    }
}
