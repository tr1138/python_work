from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)

rolls = 10
sides = [6, 10, 20]
for side in sides:
    die = Die(side)
    low = side
    high = 1

    print(f'Rolling {side}-sided die {rolls} times:')
    for i in range(rolls):
        roll = die.roll_die()
        if roll < low:
            low = roll
        if roll > high:
            high = roll
        print(f'Roll {i + 1}: {roll}')

    print(f'{side}-side highest roll: {high}\nLowest roll: {low}\n')