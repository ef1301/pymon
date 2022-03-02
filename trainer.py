from attributes import gender
from attributes import nature

class Trainer:
    def __init__(self, name, gender_index, nature_index, boardX, boardY):
        self.name = name
        self.gender = gender[gender_index]
        self.nature = nature[nature_index]
        self.x_pos = 0
        self.y_pos = 0
        self.boardX = boardX
        self.boardY = boardY
        self.team = {}
        self.money = 1000000
        self.bag = {}
    def updatePos(self,x,y):
        self.x_pos = x
        self.y_pos = y
    def validMove(self,x,y):
        if(x >= 0 and y >= 0 and x < self.boardX and y < self.boardY):
            return true
        else:
            return false
    def getPos(self):
        return [self.x_pos, self.y_pos]
    def getName(self):
        return self.name
    def getTeam(self):
        return self.team
    def addToTeam(self, pokemon):
        if(len(self.team) < 5):
            self.team[pokemon.getName()] = pokemon
        else:
            print('Your team is full.')
    def defend(self, pokeIndex, damage):
        return self.team[pokeIndex].defend(damage)
    def lost(self):
        keys = self.team.keys()
        for key in keys:
            if(self.team[key].getHealth() != 0):
                return False
        return True
