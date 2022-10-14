import pandas as pd

df = pd.read_csv('football_players.csv')
mean = df.groupby(['Club']).mean('Wage')['Wage']
median = df.groupby(['Club']).median('Club')['Wage']
print(mean.loc[mean == median].count())
