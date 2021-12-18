def nine_count(*args):
    nines = [d for d in str(args) if d == '9']
    return len(nines)

print(nine_count(*range(100, 1001)))