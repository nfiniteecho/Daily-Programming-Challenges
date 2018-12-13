from random import randint

# Roll a number of dice with a certain number of faces for D&D
def roll(num_and_sides):
    num = int(num_and_sides[0])
    sides = int(num_and_sides[1])
    rollList = []
    total = 0

    for i in range(num):
        randomRoll = randint(1,sides)
        total += randomRoll
        rollList.append(randomRoll)
        
    return print(f'Num Dice: {num} \tSides: {sides} \tTotal: {total} \tRolls: {rollList}')

roll('3d6'.split('d'))
roll('4d12'.split('d'))
roll('1d10'.split('d'))
roll('5d4'.split('d'))
roll('2d10'.split('d'))