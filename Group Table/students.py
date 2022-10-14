import pandas as pd

df = pd.read_csv('students.csv')
# print(df)
# print(df[['Group', 'Mark']])
# print(df[['Group', 'Mark']].groupby(['Group']).mean())
print(df['Group'])
for element in df.groupby(['Group']):
    print(element)
