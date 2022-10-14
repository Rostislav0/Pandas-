import pandas as pd

df = pd.read_csv('accountancy.csv')

# get mean salary in several Type for Loopa and Pupa
print(df.groupby(['Executor', 'Type']).mean(['Salary'])['Salary'].unstack())
