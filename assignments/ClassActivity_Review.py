# Create a function that checks if a number is even
def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

nums = range(0, 13)

# Print results
for i in nums:
    if isEven(i) == True:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
