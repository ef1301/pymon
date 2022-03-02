from pokemon import Pokemon
from pokedex import pokedex
import random

class CPU_Pokemon(Pokemon):
    def __init__(self, poke_index, nickname, type_of_pokemon, moves, health):
        super().__init__(poke_index, nickname, type_of_pokemon, moves, health)
    def attack(self):
        return randomMove.use()
    def fight(self, opponent, MC):
        #breaks here8
        randomMove = random.choice(list(self.moves.keys()))
        MC.defend(opponent,self.use(randomMove))
        return MC



def createCPUPokemon(pokeIndex):
    pokemon = pokedex[pokeIndex]
    pokemonObj = CPU_Pokemon(pokeIndex,
                         pokemon['name'],
                         pokemon['type_of_pokemon'],
                         pokemon['moves'],
                         pokemon['health'])
    return pokemonObj

def generateTeam():
    team = {}
    #teamSize = random.randint(1,4)
    #i = 0
    #while(i < teamSize):
    randomPokemon = random.choice(list(pokedex))
        #if(randomPokemon not in team):
        #    team[randomPokemon['poke_index']] = randomPokemon
        #    i += 1
    teamMember = createCPUPokemon(randomPokemon)
    team[randomPokemon] = teamMember
    return team

cpuNames = ['Charlie', 'John', 'Syd', 'Conrad', 'Marcus', 'Silvia']
fun_facts = ["I am lactose intolerant.", "I've never broken a bone.", "I'm going to catch them all the pokemon in the world.", "I have an abnormally long pinky toe."]

class CPU_Trainer:
    def __init__(self):
        self.name = random.choice(cpuNames)
        self.team = generateTeam()
        self.money = random.randint(1,5) * 100
        self.fun_fact = random.choice(fun_facts)
    def getTeam(self):
        return self.team
    def getReward(self):
        return self.money
    def getName(self):
        return self.name
    def getFunFact(self):
        return self.fun_fact
    def lost(self):
        keys = self.team.keys()
        for key in keys:
            if(self.team[key].getHealth() != 0):
                return False
        return True
    def fight(self, teamMember, opponent, MC):
        #breaks here8
        move = random.choice(list(self.team[teamMember].getMoves()))
        self.team[teamMember].use(move)
        return MC
