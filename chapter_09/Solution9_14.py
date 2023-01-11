from random import randint
bucket = [11, 14, 6, 89, 109, 44, 76, 93, 33, 456, 'A ', 'U', 'L', 'G', 'k']

def my_solution():
    guess = randint(0, 14)
    return bucket[guess]

lucky_one = []
for x in range(4):
    lucky_one.append(my_solution())

print(f"Hello any thicket matching this: {lucky_one} wins a prize")
