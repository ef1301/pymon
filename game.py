from trainer import Trainer
from pokemon import Pokemon
from pokemon import createPokemon
from battle import battle
from pokedex import pokedex
from pokemon import starters
from pokemon import starterPokemon
import CPU
import random
import emoji

def moveUp(x,y):
    return [x - 1, y]
def moveDown(x,y):
    return [x + 1, y]
def moveLeft(x,y):
    return [x, y - 1]
def moveRight(x,y):
    return [x, y + 1]


class Game:
    board = [[]]
    def __init__(self, trainer, gameStatus):
        self.MC = trainer
        self.board = GameBoard(trainer.getName())
        self.board.createBoard()

        starters()
        MCStarter = int(input('Pick a starter Pokemon. Enter the poke_index. '))
        while(MCStarter not in starterPokemon.keys()):
            MCStarter = int(input('Please try again. Pick a starter Pokemon. Enter the poke_index. '))
        starterPE = starterPokemon[MCStarter]
        starterNickname = input("What is your pokemon's name? ")
        MCStarter = createPokemon(MCStarter, starterNickname)
        print(MCStarter)
        self.MC.addToTeam(MCStarter)

        print(self.board)

        while(gameStatus == 'start'):
            action = input('Pick a direction to move to. (UP/DOWN/LEFT/RIGHT) ')
            trainerPos = self.MC.getPos()
            newPos = self.MC.getPos()
            if(action == 'UP'):
                newPos = moveUp(trainerPos[0], trainerPos[1])
                if(self.board.validMove(newPos[0], newPos[1])):
                    self.board.emptyCurrTile(trainerPos[0], trainerPos[1])
                    self.MC.updatePos(newPos[0], newPos[1])
                    #self.board.interactWith(newPos[0], newPos[1])
                    self.MC = self.board.updateMCPos(self.MC, newPos[0], newPos[1])
                else:
                    print("Can't move here... ")
            elif(action == 'DOWN'):
                newPos = moveDown(trainerPos[0], trainerPos[1])
                if(self.board.validMove(newPos[0], newPos[1])):
                    self.board.emptyCurrTile(trainerPos[0], trainerPos[1])
                    self.MC.updatePos(newPos[0], newPos[1])
                    #self.board.interactWith(newPos[0], newPos[1])
                    self.MC = self.board.updateMCPos(self.MC, newPos[0], newPos[1])
                else:
                    print("Can't move here... ")
            elif(action == 'LEFT'):
                newPos = moveLeft(trainerPos[0], trainerPos[1])
                if(self.board.validMove(newPos[0], newPos[1])):
                    self.board.emptyCurrTile(trainerPos[0], trainerPos[1])
                    self.MC.updatePos(newPos[0], newPos[1])
                    #self.board.interactWith(newPos[0], newPos[1])
                    self.MC = self.board.updateMCPos(self.MC, newPos[0], newPos[1])
                else:
                    print("Can't move here... ")
            elif(action == 'RIGHT'):
                newPos = moveRight(trainerPos[0], trainerPos[1])
                if(self.board.validMove(newPos[0], newPos[1])):
                    self.board.emptyCurrTile(trainerPos[0], trainerPos[1])
                    self.MC.updatePos(newPos[0], newPos[1])
                    #self.board.interactWith(newPos[0], newPos[1])
                    self.MC = self.board.updateMCPos(self.MC, newPos[0], newPos[1])
                else:
                    print("Can't move here... ")
            else:
                print('Invalid Move. ')
            print(self.board)
    def move(self,action):
        if(action == 'UP'):
            self.MC.moveUp()
            board[trainerPos[0]][trainerPos[1]].interact()
        elif(action == 'DOWN'):
            self.MC.moveDown()
        elif(action == 'LEFT'):
            self.MC.moveLeft()
        else:
            self.MC.moveRight()

class GameBoard:
    def __init__(self, trainerName, width = 8, height = 8):
        self.dimensions = [width, height]
        self.board = []
        self.tileOptions = ['Trainer',
                            'Pokemon',
                            # 'Obstacle',
                            'Empty']
        self.trainerName = trainerName
    def __str__(self):
        s = [[str(e) for e in row] for row in self.board]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return '\n'.join(table) + '\n'
    def createBoard(self):
        initial_board_instance = self.board
        for row in range(self.dimensions[0]):
            initial_board_instance.append([])
            for column in range(self.dimensions[1]):
                tile = GameTile(self.tileOptions[random.randint(0,len(self.tileOptions)-1)])
                initial_board_instance[-1].append(tile)
        initial_board_instance[0][0] = GameTile(self.trainerName)
        return initial_board_instance
    def validMove(self,x,y):
        if(x >= 0 and y >= 0 and x < self.dimensions[0] and y < self.dimensions[1]):
            if(self.board[x][y].tileType() != 'Obstacle'):
                return True
            else:
                return False
        else:
            return False
    def emptyCurrTile(self, x, y):
        self.board[x][y] = GameTile('Empty')
    def updateMCPos(self, MC, x, y):
        updatedMC = self.board[x][y].interact(MC)
        self.board[x][y] = GameTile(self.trainerName)
        return updatedMC
    def getDimensions(self):
        return self.dimensions
    #def interactWith(self, x, y):
    #    print(type(self.board[x][y]))

class GameTile:
    def __init__(self, tType):
        self.tType = tType
        self.icons = {
            'Trainer': ':T:',
            'Pokemon': ':P:',
            'Empty': '0',
            #'Obstacle': ':evergreen_tree:'
        }
        if(tType == 'Pokemon'):
            randomPokemon = random.choice(list(pokedex))
            self.data = CPU.createCPUPokemon(randomPokemon)
        elif(tType == 'Trainer'):
            self.data = CPU.CPU_Trainer()
    def __str__(self):
        if(self.tType in self.icons):
            return emoji.emojize(self.icons[self.tType])
        else:
            return self.tType
    def tileType(self):
        return self.tType
    def interact(self, MC):
        if(self.tType == 'Trainer'):
            return battle('Trainer', MC, self.data)
        elif(self.tType == 'Pokemon'):
            return battle('Pokemon', MC, self.data)
        elif(self.tType == 'Empty'):
            return MC
        #elif(tType == 'Obstacle'):
        #    return false
        else:
            return MC
