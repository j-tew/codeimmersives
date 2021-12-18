def myMean(nums):
    l = sorted(nums)
    return int((l[0] + l[-1]) / 2)

def myMedian(nums):
    size = len(nums)
    if size % 2 == 0:
        median = nums[size / 2]
    else:
        x,y = int(size / 2),int(size/2 + 1)
        median = (nums[x] + nums[y]) / 2
    return median

grades = {'100': {'Quiz-1': 80, 'Quiz-2': 92, 'Quiz-3': 84},
         '101': {'Quiz-1': 93, 'Quiz-2': 95, 'Quiz-3': 90},
         '102': {'Quiz-1': 88, 'Quiz-2': 94, 'Quiz-3': 88},
         '103': {'Quiz-1': 88, 'Quiz-2': 97, 'Quiz-3': 93},
         '104': {'Quiz-1': 85, 'Quiz-2': 92, 'Quiz-3': 90}}

students = {'101': ['Morgan','Debra'],
           '100': ['Palmer','Sara'],
           '102': ['Delgado','Luis'],
           '104': ['Cruz','Maria'],
           '103': ['Korencho','Victor']}

# Calculate the mean, median for each individual Quiz
quiz1_scores = [grade['Quiz-1'] for grade in grades.values()]
quiz2_scores = [grade['Quiz-2'] for grade in grades.values()]
quiz3_scores = [grade['Quiz-3'] for grade in grades.values()]

print(f'''Quiz 1 mean: {myMean(quiz1_scores)}, median: {myMedian(quiz1_scores)}
Quiz 2 mean: {myMean(quiz2_scores)}, median: {myMedian(quiz2_scores)}
Quiz 3 mean: {myMean(quiz3_scores)}, median: {myMedian(quiz3_scores)}
''')

# Calculate the mean for each student:
student_means = [(student_id, myMean(g.values())) for student_id,g in grades.items()]
for student in student_means:
    name = f'{students[student[0]][0]}, {students[student[0]][1][0]}'
    print(f'{name}: {student[1]}')