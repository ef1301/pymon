from trainer import Trainer
from game import Game
from attributes import nature
from attributes import gender

def main():
    gameStatus = input('Are you ready to begin your Pokemon journey? (y/n) ')
    if(gameStatus == 'y'):
        input_name = input('What is your name? ')
        input_gender = int(input('What is your gender? (0 = male/1 = female) '))
        while(input_gender < 0 or input_gender >= len(gender)):
           input_gender = int(input('Please try again. What is your gender? (0 = male/1 = female) '))
        for i in range(len(nature)):
            print(str(i) + " " + nature[i])
        input_nature = int(input('What is your nature? '))
        while(input_nature < 0 or input_nature >= len(nature)):
            for i in range(len(nature)):
                print(str(i) + " " + nature[i])
            input_nature = int(input('Please try again. What is your nature? '))
        trainer = Trainer(input_name,int(input_gender),int(input_nature),0,0)
        game = Game(trainer,'start')

    else:
        return

if __name__ == "__main__":
    main()
