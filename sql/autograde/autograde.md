# Autograde

## Given a collection of answers and keys for exams as text files:

    1. Create a class roster -> ('PYTHON_PTI_CAPSTONE_CLASS_ROSTER.TXT')
        - An unduplicated list of names in *'Lastname, Firstname'* format
            - Alphabetical order by last name then first name and in proper case for names
        - Parse filenames to get names
    2. Creat a new class roster with scores and their means -> ('PYTHON_PTI_CAPSTONE_CLASS_ROSTER_GPA.TXT')
        - Format should be all scores following first name, then the mean, all comma seperated
        - Find the mean for each student by adding all scores and dividing by the number of tests taken.
    3. Create a class summary report
        - Provide number of students in the class
        - Provide the mean and standard deviation of each exam
