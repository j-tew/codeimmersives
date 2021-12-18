# Frank Smith M 94
# Sharon Post F 96
# David Ware M 88
# Warren Childs M 89
# Sara Tolken F 85
# Phillip Lee M 83
# Tara Holds F 78
# Samuel Jenkins M 86
# Paula Fere F 88
# Alonzo Moore M 85


student_id = 1
students = {}
while student_id < 10:
    print(f'Please enter the following info:\n')
    student = {
        'first': input(f'First Name: '),
        'last': input(f'Last Name: '),
        'gender': input(f'Gender: ').upper(),
        'grade': int(input(f'Grade: '))
    }
    students.update({student_id: student})
    student_id += 1

all_grades = [student['grade'] for student in students.values()]
boy_grades = [student['grade'] for student in students.values() if student['gender'] == 'M']
girl_grades = [student['grade'] for student in students.values() if student['gender'] == 'F']

print(all_grades, boy_grades, girl_grades)

# mean =
# median =
# mode = 
