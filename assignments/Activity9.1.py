# Create a function that sorts 5 numbers in a list
# Don't use sort() or sorted() methods
nums = [22, 13, 3, 2, 1]

def mySort(l):
    new = []
    for num in range(len(l)):
        for i in l:
            if i == min(l):
                new += [i]
                l.remove(i)
    return new

print(mySort(nums))
