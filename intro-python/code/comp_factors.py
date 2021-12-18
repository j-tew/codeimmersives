def factors(x):
    return [i for i in range(1, x+1) if x%i==0]

for i in range(100, 201):
    if len(factors(i)) > 2:
        print(f'Number: {i} | Sum of Factors: {sum(factors(i))} | List of Factors: {factors(i)}')