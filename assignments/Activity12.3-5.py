from statistics import mean

# Activity12.3 Create a function that gets the mean from a list of grades
def meanOf(grades):
    m = mean(grades)
    return m

# Activity 12.4: Create a function that takes a list of grades and makes a list of bools for passing
def passing(grades):
    passLst = []
    for grade in grades:
        if grade < 55:
            passLst.append(False)
        else:
            passLst.append(True)
    return passLst

# Activity 12.5 Create a function that prints a count of passes and fails
def passCount(bools):
    passes = passFail.count(True)
    fails = passFail.count(False)
    total = f"\nPasses: {passes}\nFails: {fails}"
    return total

exam = [74, 62, 91, 92, 73, 65, 100, 45, 57, 98]

print(meanOf(exam))
print(passing(exam), passCount(passing(exam)))
