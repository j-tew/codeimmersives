# Create a function that takes an integer as a parameter and generates
# a list of that size with random numbers from 0-1024
from random import getrandbits

def randList(num):
    rand_bits = []
    for i in range(num):
        rand_bits.append(getrandbits(10))
    return rand_bits

print(randList(3))

