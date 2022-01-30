def num_count(num: int, *numbers: range) -> int:
    '''Provided a number and a range of numbers, return the occurence of the number in the digits of all numbers in the range'''
    nums = [d for d in str(numbers) if d == str(num)]
    return len(nums)

print(num_count(9, *range(100, 1001)))
