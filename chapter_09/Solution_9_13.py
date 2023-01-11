from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number = randint(1, self.sides)
        return number

prova1 = Die(10)
prova2 = Die(20)

result_A = []
result_B = []

for t in range(10):
    zeta = prova1.roll_die()
    result_A.append(zeta)
for x in range(10):
    theta = prova2.roll_die()
    result_B.append(theta)

ordine_A = sorted(result_A)
ordine_B = sorted(result_B)
print(result_A)
print(ordine_A)
print(result_B)
print(ordine_B)
print(type(result_A))