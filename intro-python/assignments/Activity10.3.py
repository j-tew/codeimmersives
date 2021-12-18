def isSorted(x):
    check = x[0]
    for num in x:
        if num < check:
            break
        else:
            check = num
    if check == x[-1]:
        return True
    else:
        return False

sList = [1, 2, 3, 4, 5]
nsList = [13, 7, 2, 22]

print(f"{sList} is sorted: {isSorted(sList)}\n")
print(f"{nsList} is sorted: {isSorted(nsList)}\n")