# Create a function to perform what the max() function does
nums = [1, 2, 3, 4, 5]

def myMax(l):
    check = 0
    for i in l:
        if i >= check:
            check = i
    return check

print(myMax(nums))