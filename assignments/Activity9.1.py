# Create a function that sorts 5 numbers in a list
# Don't use sort() or sorted() methods
nums = [5, 4, 3, 2, 1]

def mySort(l):
    new = []
    while len(new) < 5:
        for i in l:
            if i == min(l):
                new += [i]
                l.remove(i)
            else:
                continue
    return new

print(mySort(nums))
