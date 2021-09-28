from random import getrandbits

def randList(num):
    rand_bits = []
    for i in range(num):
        rand_bits.append(getrandbits(10))
    return rand_bits

print(randList(3))

