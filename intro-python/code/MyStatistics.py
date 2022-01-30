def calculate_mean(x: list) -> int:
    '''Calculates the mean of a given list of integers'''
    return sum(x)/len(x)

def calculate_mode(x: list) -> int:
    '''Calculates the mode of a given list of integers'''
    counts = {i: x.count(i) for i in x}
    return [k for k,v in counts.items() if v == max(counts.values())]

def calculate_median(x: list) -> float:
    '''Calculates the median of a given list of integers'''
    x.sort()
    return (x[int(l/2+1)] + x[int(l/2-1)]) / 2 if (l := len(x)) % 2 == 0 else x[l/2]
