def mySort(x, y, z):
    myList = [x, y, z]
    myList.sort()
    mySortedTpl = tuple(myList)
    return mySortedTpl

first = (input(f"Please Enter the First Number: "))
second = (input(f"Please Enter the Second Number: "))
third = (input(f"Please Enter the Third Number: "))

print(mySort(first, second, third))