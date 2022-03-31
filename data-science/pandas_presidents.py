import pandas as pd

df = pd.read_csv('presidents.txt')

# Remove the quotes from the values
df = df.apply(lambda x: x.str.strip("'"))
# Remove the quotes from the column names
df.rename(lambda x: x.strip("'"), axis=1, inplace=True)

x = df['Name']
x = x.apply(lambda x: x.split(' '))
print(x)

#x = sorted([''.join(re.findall('\d', i)) for i in df['Name']])


