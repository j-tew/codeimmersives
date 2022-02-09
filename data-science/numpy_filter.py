import numpy as np

# Here's how to use filter with numpy

# A simple array from 0-10
array1 = np.array(range(10))
# Assign the filter to a variable (WARNING: 'filter' is a keyword)
filter1 = array1 % 2 == 0

# See what that creates
print(f'Our Original array:\n{array1}\n')
print(f'Our filter returns an array with booleans values:\n{filter1}\n')

# Now to make a new array using the Filter
filtered_array = array1[filter1]

# The Filtered output
print(f'The Filtered array:\n{filtered_array}\n')