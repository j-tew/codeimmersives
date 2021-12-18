'''
16) Given two int values, return their sum.
Unless the two values are the same,
then return the square their sum.
'''
def sum_squared(x, y):
    return x+y if x!=y else (x+y)**2

num1 = sum_squared(13, 22)
num2 = sum_squared(2, 2)
print(num1, num2)

'''
17) Using List Comprehension, write a function that given
a list of numeric values will generate and return a new list
of values with each item in the original list cubed
(raised to the third power)
'''
nums = [0, 1, 2, 4]
cubes = [i**3 for i in nums]

print(nums, cubes)

'''
18) Given an int array length 2,
return True if it contains a 2 or a 3.
'''
def two_or_three(numList):
    return True if 2 in numList or 3 in numList else False

pairs = [[1, 2], [3, 4], [5, 6]]
answers = [two_or_three(pair) for pair in pairs]
print(answers)

'''
19) Return the number of even ints in the given array.
Note: the % "mod" operator computes the remainder,
e.g. 5 % 2 is 1.
'''
def count_evens(numList):
    evens = 0
    for num in numList:
        if num % 2 == 0:
            evens += 1
    return evens

nums = [0, 2, 13, 22, 43]
print(count_evens(nums))

'''
20) Given 3 int values, a b c, return their sum. However,
if one of the values is 13 then it does not count towards the sum
and values to its right do not count.
So for example, if b is 13, then both b and c do not count.
'''
def lucky_sum(a, b, c):
    nums = (a, b, c)
    total = 0
    for num in nums:
        if num == 13:
            break
        total += num
    return total

ans1 = lucky_sum(1, 2, 3)
ans2 = lucky_sum(1, 2, 13)
ans3 = lucky_sum(1, 13, 3)
print(ans1, ans2, ans3)