class Move:
    def __init__(self, name, type_of_move, pp, power, accuracy):
        self.name = name
        self.type_of_move = type_of_move
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
    def __str__(self):
        return (
            "\t" + self.name + "\n" +
            "\t" + self.type_of_move + "\n" +
            " ------------------------- "
        )
    def use(self):
        return self.power if self.power != None else 0
