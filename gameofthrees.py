# If the number is divisible by 3, divide it by 3.
# If it's not, either add 1 or subtract 1 (to make it divisible by 3)
# then divide it by 3
def game_of_threes(num):
    while num != 1:
        if num % 3 == 0:
            num /= 3
        elif (num + 1) % 3 == 0:
            num += 1
            num /= 3
        elif (num - 1) % 3 == 0:
            num -= 1
            num /= 3
        print(num)

# Better solution with added operation notifier in print
def game_of_threes_better(num):
    while num != 1:
        if num % 3 == 0:
            print(f'{num} 0')
        elif num % 3 == 1:
            print(f'{num} -1')
            num -= 1
        elif num % 3 == 2:
            print(f'{num} 1')
            num += 1
        num /= 3
    print(num)

# Better solution using a tuple indexed by modulo remainders of 0, 1 ,2
def game_of_threes_tuple(num):
    while num != 1:
        # If modulo is 0, we don't need to add anything to num, so the 0th place in the tuple has the value 0. 
        # If the modulo is 1, we need to remove 1 from it, so the 1st place in the tuple has the value -1. 
        # If the modulo is 2, we need to add 1.
        # These modulos (0, 1, 2) index the tuple 
        op = (0, -1, 1)[int(num % 3)]
        print(f'{num} {op}')
        num = (num + op) / 3
    print(num)

game_of_threes(100)
print()
game_of_threes_better(100)
print()
game_of_threes_tuple(120)