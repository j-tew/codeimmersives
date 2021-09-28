# Create a function that takes an integer as a parameter and generates
# a list of that size with random numbers from 20-78
from random import randrange

def randList(num):
    rand_bits = []
    for i in range(num):
        rand_bits.append(randrange(20, 78))
    return rand_bits

print(randList(3))
