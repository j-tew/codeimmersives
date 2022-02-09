import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data/president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)

print(f'Mean: {np.mean(heights)}')
print(f'Stdev: {np.std(heights)}')
print(f'Min: {np.min(heights)}')
print(f'Max: {np.max(heights)}')

q1 = np.percentile(heights, 25)
q2 = np.percentile(heights, 50)
q3 = np.percentile(heights, 75)

print(f'1st Quartile: {q1}\n2nd Quartile: {q2}\n3rd Quartile: {q3}')

plt.hist(heights)
