from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

die = Die()
while True:
    print(die.roll())
    if input("Roll again? (y/n) ") != 'y':
        break