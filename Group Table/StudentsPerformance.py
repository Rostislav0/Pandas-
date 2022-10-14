import pandas as pd

df = pd.read_csv('StudentsPerformance (1).csv')

# print(df.groupby(['race/ethnicity', 'gender']).median('reading score').max()['reading score'])

df = df.groupby(['gender', "parental level of education"]).mean().mean(axis=1)
# x = (x['math score'] + x['reading score'] + x['writing score'])/3 = .mean(axis=1)
print(df.loc[('male', df.loc['female'].idxmax())].round(1))
