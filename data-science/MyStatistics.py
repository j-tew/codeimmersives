def calculate_mean(x: list) -> int | float:
    '''Calculates the mean of a given list of numbers'''
    return sum(x)/len(x)

def calculate_mode(x: list) -> int | float:
    '''Calculates the mode of a given list of numbers'''
    counts = {i: x.count(i) for i in x}
    return [k for k,v in counts.items() if v == max(counts.values())]

def calculate_median(x: list) -> int | float:
    '''Calculates the median of a given list of numbers'''
    x.sort()
    return (x[int(l/2+1)] + x[int(l/2-1)]) / 2 if (l := len(x)) % 2 == 0 else x[l/2]

def calculate_variance(x: list = grades) -> float:
    '''Calculate the variance of a given a list of numbers'''
    return sum([(i - sum(x) / len(x))**2 for i in x]) / len(x)

def calculate_standard_dev(x: list = grades) -> float:
    '''Calculate the standard deviation of a given a list of numbers'''
    variance = sum([(i - sum(x) / len(x))**2 for i in x]) / len(x)
    return round((variance ** 0.5), 3)