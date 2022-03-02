
option = ["Pick an action. ", "[F] Fight ", "[I] Use an Item. ", "[C] Change Pokemon ", "[E] Escape "]

def callOptions():
    s = "\n"
    for i in option:
        s += i + "\n"
    print(s)

def battleTrainer(MC, CPU):
    MCTurn = True
    currMCPokemon = list(MC.getTeam().keys())[0]
    currCPUPokemon = list(CPU.getTeam().keys())[0]
    print('Trainer Battle running: ')
    while(MC.lost() == False):
        if(CPU.lost() == True):
            print('Victory!!! \n')
            print("Before running away, " + CPU.getName() + " says, '" + CPU.getFunFact() + "'")
            return MC
        elif(MC.lost() == True):
            print('You lost, loser. \n')
            return MC
        elif(MCTurn): #MC make a choice
            callOptions()
            choice = input(">> ")
            print(choice)
            #while(choice != 'F' or choice != 'I' or choice != 'C' or choice != 'E'):
            if(choice == 'F'):
                moves = MC.getTeam()[currMCPokemon].getMoves()
                MC.getTeam()[currMCPokemon].printMoves()
                moveChoice = input('Select a move. \n >> ')
                while(moveChoice not in moves):
                    MC.getTeam()[currMCPokemon].printMoves()
                    MC.getTeam()[currMCPokemon].getMoves()
                    moveChoice = input('Select a move.')
                #CPU needs to defend against attack
                CPU.getTeam()[currCPUPokemon].defend(MC.getTeam()[currMCPokemon].use(moveChoice))
                print(CPU.getTeam()[currCPUPokemon].getName() + " has " + str(CPU.getTeam()[currCPUPokemon].getHealth()) + "HP. \n")
                #fight
                MCTurn = False
            elif(choice == 'I'):
                #bag
                print("Get pooped on. You can't do that, loser. \n")
                MCTurn = False
            elif(choice == 'C'):
                #change pokemon
                print("Get pooped on. You can't do that, loser. \n")
                MCTurn = False
            elif(choice == 'E'):
                print("You have escaped \n")
                return MC
            else:
                print("Please try again.")
                callOptions()
                choice = input(">> ")
        else: #CPU fights MC
            MC = CPU.fight(currCPUPokemon, currMCPokemon, MC)
            print(MC.getTeam()[currMCPokemon].getName() + " has " + str(MC.getTeam()[currMCPokemon].getHealth()) + "HP. \n")
            MCTurn = True
    return MC

def battlePokemon(MC, CPU):
    MCTurn = True
    currMCPokemon = list(MC.getTeam().keys())[0]
    print('Pokemon Battle running: ')
    while(MC.lost() == False):
        if(CPU.fainted() == True):
            print('Victory!!! \n')
            return MC
        elif(MC.lost() == True):
            print('You lost, loser. \n')
            return MC
        elif(MCTurn): #MC make a choice
            callOptions()
            choice = input(">> ")
            print(choice)
            if(choice == 'F'):
                moves = MC.getTeam()[currMCPokemon].getMoves()
                MC.getTeam()[currMCPokemon].printMoves()
                moveChoice = input('Select a move. \n >> ')
                while(moveChoice not in moves):
                    MC.getTeam()[currMCPokemon].printMoves()
                    MC.getTeam()[currMCPokemon].getMoves()
                    moveChoice = input('Select a move.')
                #MC needs to defend against attack
                CPU.defend(MC.getTeam()[currMCPokemon].use(moveChoice))
                print(CPU.getName() + " has " + str(CPU.getHealth()) + "HP. \n")
                #fight
                MCTurn = False
            elif(choice == 'I'):
                #bag
                print("Get pooped on. You can't do that, loser. \n")
                MCTurn = False
            elif(choice == 'C'):
                #change pokemon
                print("Get pooped on. You can't do that, loser. \n")
                MCTurn = False
            elif(choice == 'E'):
                print("You have escaped \n")
                return MC
            else:
                print("Please try again.")
                callOptions()
                choice = input(">> ")
        else: #CPU fights MC
            MC = CPU.fight(currMCPokemon, MC)
            print(MC.getTeam()[currMCPokemon].getName() + " has " + str(MC.getTeam()[currMCPokemon].getHealth()) + "HP. \n")
            MCTurn = True
    return MC


def battle(fType, MC, CPU):
    if(fType == 'Trainer'):
        return battleTrainer(MC,CPU)
    if(fType == 'Pokemon'):
        return battlePokemon(MC, CPU)
