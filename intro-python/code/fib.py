def fib(sequence, iters):
    '''Given a sequence of numbers, will add the last two values and append the new value to the sequence'''
    for i in range(iters):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

x = [1, 2]
print(fib(x, 3))
