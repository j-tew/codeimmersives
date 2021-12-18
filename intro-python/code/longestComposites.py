def is_prime(number):
    for n in range(2,int(number**1/2)+1):
        if number%n==0:
            return False
    return True

runs = []
for i in range(1000, 3001):
    if is_prime(i):
        continue
    else:
        runs.append(i)

breaks = []
for i in range(len(runs) + 1):
    try:
        if runs[i] - 1 != runs[i-1]:
            breaks.append(i)
    except IndexError:
        pass

longest_run = 0
for i in range(len(breaks) + 1):
    try:
        run = breaks[i] - breaks[i-1]
        if run > longest_run:
            longest_run = run
    except IndexError:
        pass
print(longest_run)

