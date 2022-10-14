import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt

# 1
# dateparse = lambda x: datetime.strptime(x, '%d.%m.%Y %H:%M:%S')
# source_data = pd.read_csv('export.csv', sep=';', parse_dates=['IP_PROP5562'], date_parser=dateparse)
# print(source_data['IP_PROP5562'].map(lambda x: x.date()))  # without time
# print(source_data.head())


# 2
source_data = pd.read_csv('export.csv', sep=';')
source_data['IP_PROP5562'] = pd.to_datetime(source_data['IP_PROP5562'], format='%d.%m.%Y %H:%M:%S')
# print(source_data['IP_PROP5562'].dt.date)  # without time
# print(source_data.head())


# new col
source_data['date'] = source_data['IP_PROP5562'].dt.date
# print(source_data.head())
source_data[['date', 'IE_ID']].groupby('date').count().plot(kind='bar', figsize=(13,8))
plt.show()

