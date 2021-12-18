def fact(x):
    return [i for i in range(1, x+1) if x%i==0]

print([i for i in range(5, 5001) if sum(fact(i)[:-1]) == i])

def func(x):
    '''
    adds one to a number
    '''
    return x+1

print(func(1))