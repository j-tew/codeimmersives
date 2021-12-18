# Without Comprehension
nums = range(1, 31)

for num in nums:
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)

# FizzBuzz With Comprehension
for x in ["fizz"*(x%3==0)+"buzz"*(x%5==0)+str(x)*(x%3 > 0 and x%5 > 0) for x in range(1,31)]:
    print(x)

