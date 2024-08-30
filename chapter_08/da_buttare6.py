""" Write a function taht asks a number and generate a randon
number between the given number and 0."""

import random

def random_number(n):
    return random.randint(0, n)
    
print(random_number(10))
    