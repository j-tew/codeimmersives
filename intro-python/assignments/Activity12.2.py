# Create a function that gets the average of the curved grades
from statistics import stdev, mean

# List of Grades
exam_grades = [74, 62, 91, 92, 73, 65, 100, 45, 57, 98]

def curvedGrades(x=exam_grades):
    # Getting the standard deviation
    curve = stdev(x)
    # List for new values
    newGrades = []
    # Add the curve to each grade and put it in the new list
    for grade in x:
        if grade != 100:
            # Round the ouput to be pretty
            newGrade = round((grade + curve), 1)
            # If the new grade exceeds max grade, just make it 100
            if newGrade > 100:
                newGrade = 100
            newGrades.append(newGrade)
        # If the grade is already outstanding, keep it
        else:
            newGrades.append(100)
    #Show the new grades
    return newGrades

# Average of curved grades
def avgCrvd(x=curvedGrades()):
    avg = mean(x)
    return avg

# Average of OG grades
def avgOG(x=exam_grades):
    avg = mean(x)
    return avg

print(curvedGrades(), "\n", avgCrvd(), "\n", avgOG())