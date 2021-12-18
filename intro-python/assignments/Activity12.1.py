# Create a Function  that curves grade scores
from statistics import stdev

# List of Grades
exam_grades = [74, 62, 91, 92, 73, 65, 100, 45, 57, 98]

def curvedGrades(grades):
    # Getting the standard deviation
    curve = stdev(grades)
    # List for new values
    newGrades = []
    # Add the curve to each grade and put it in the new list
    for grade in grades:
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

# The OG grades
print(exam_grades)
# The new better ones
print(curvedGrades(exam_grades))