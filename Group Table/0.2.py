import pandas as pd
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df = pd.read_csv('dataset_345422_14.txt')
df['Date'] = pd.to_datetime(df['Date'])
df['day_of_week'] = df['Date'].dt.dayofweek
# print(df.groupby(['Date']).sum().mean(axis=1).max())
print(days[df.groupby(['day_of_week']).mean('Date').mean(axis=1).idxmax()])