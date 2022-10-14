import pandas as pd

df = pd.read_csv('dota_hero_stats.csv')
print(df.groupby(['attack_type', 'primary_attr']).count())