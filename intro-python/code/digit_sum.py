def is_even(x):
    return True if x%2 == 0 else False

count = 0
for i in range(1000, 3001):
    if is_even(i):
        num = [int(j) for j in str(i)]
        if sum(num) % 5 == 0:
            print(i)
            count += 1
print(count)
