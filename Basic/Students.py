import pandas as pd

df = pd.read_csv('StudentsPerformance (2).csv')

# print(df.loc[df['lunch'] == 'free/reduced'].describe())
# print(df.describe())
# df = df.rename(columns={'writing score': 'writing_score'})
# print(df.query("writing_score > 80"))

# get columns have in title "score"
print('including "score" in columns:', [i for i in list(df) if 'score' in i])
print(df[[i for i in list(df) if 'score' in i]].head())
# just method
print(df.filter(like='score').head())
