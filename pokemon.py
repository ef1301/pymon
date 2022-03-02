from attributes import gender
from attributes import nature
from pokedex import pokedex
from moves import Move
import random

starterPokemon = {
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
    }
}

def starters():
    pokemon = {
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
        }
    }
    for p in pokemon:
        x = createPokemon(pokemon[p]['poke_index'],pokemon[p]['name'])
        print(x)

def createPokemon(pokeIndex, name):
    pokemon = pokedex[pokeIndex]
    pokemonObj = Pokemon(pokeIndex,
                         name,
                         pokemon['type_of_pokemon'],
                         pokemon['moves'],
                         pokemon['health'])
    return pokemonObj

class Pokemon:
    def __init__(self, poke_index, nickname, type_of_pokemon, moves, health):
        self.poke_index = poke_index
        self.name = nickname
        self.type_of_pokemon = type_of_pokemon
        self.nature = nature[random.randint(0,len(nature)-1)]
        self.moves = moves
        self.health = health
    def __str__(self):
        types = ""
        moves = ""
        for i in self.type_of_pokemon:
            types += i + " "
        for i in self.moves.keys():
            moves += str(self.moves[i]) + "\n"
        return (
            "Pokedex Index: " + str(self.poke_index) + "\n" +
            "Name: " + self.name + "\n" +
            "Health: " + str(self.health) + "\n" +
            "Types: " + types + "\n" +
            "Natures: " + str(self.nature) + "\n" +
            "Moves: " + "\n" + moves + "\n"
        )
    def getName(self):
        return self.name
    def printMoves(self):
        for move in self.moves:
            print(move)
    def getMoves(self):
        return self.moves
    def getHealth(self):
        return self.health
    def use(self, move):
        damage = self.moves[move].use()
        print(self.name + " used " + move + " and dealt " + str(damage) + " damage! \n" )
        return damage
    def defend(self, attack):
        if(self.health - int(attack) < 0):
            self.health = 0
            return False
        else:
            self.health -= int(attack)
            return True
    def fainted(self):
        return self.health == 0
