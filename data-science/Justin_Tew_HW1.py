class YearObj:

    def __init__(self, current_year: int = 2022):
        self.year = current_year
        # Dictionary of months (month_number: days_in_month)
        self.months = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
            }

        # Create a list of all the leap years until the year 3000
        leap_years = [y for y in range(3000) if y % 4 == 0]

        # If this year is a leap year, add a day in February
        if self.year in leap_years:
            self.months[2] = 29

    # Function for obtaining info about the month
    def generate_months(self):
        '''Returns a generator that can be iterated to get a list of the first day, last day, and number of days for each month.'''
        # Iterating the dictionary of months
        for month,days in self.months.items():
            # Formatting the month info into the list and yielding it
            yield [f'{month}/1/{self.year}', f'{month}/{days}/{self.year}', f'{days} days']

# Create an instance of the year
y = YearObj(2024)
# Save the generator to a variable to allow next() method
month_gen = y.generate_months()

# Iterate through the generator function
for month in month_gen:
    print(month)

###--- Just for fun ---###
# Labeling each list with the month name

# Create a new generator since we used it up the first time
month_gen = y.generate_months()
# List of month names
month_names = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
    ]

# Create a super pretty seperator for the output
print(f'\n{"#" * 50}\n')
# Iterate through the month names and print the month name with the month info using next() method
for month in month_names:
    print(f'{month}: {next(month_gen)}')