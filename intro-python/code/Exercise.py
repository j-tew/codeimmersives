'''
Exercise 1
Find all even numbers in the following list
'''
x = [12,3,'William',14,5,20,'Olga',22,104,'Ralph',99,8,17]

evens = [num for num in x if isinstance(num, int) and num % 2 == 0]
print(evens)

'''
Exercise 2
Extract all managers from the list of titles. 'Manager' in the title.
'''
titles = ['team leader','squad leader','manager','managing director','director of operations',
         'operations manager','operations manager (US)', 'operations manager (Canada)',
          'Operations manager (Mexico)']

managers = [title for title in titles if 'manager' in title]
print(managers)

'''
Exercise 3:
Find all 2 number combinations that add to 10
'''
x = [1,3,6,5,-2,22,7,-94,104,99,2,8,17,12]
sum_10 = []
for i in x:
    check = 10 - i
    if check in x and check != i:
        pair = (i, check)
        if (check, i) not in sum_10:
            sum_10.append(pair)
print(sum_10)

# Find all the 3 number combinations that add up to a prime
import itertools

def isPrime(x):
    for n in range(2,int(x**1/2)+1):
        if x%n==0:
            return False
    return True

x = [1,3,6,5,-2,22,7,-94,104,99,2,8,17,12]

nums = itertools.combinations(x,3)
combos = [combo for combo in nums if isPrime(sum(combo))]
print(combos)