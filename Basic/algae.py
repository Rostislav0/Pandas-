import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('algae.csv')

# get min, mean, max alanin concentration values for Fucus
print(*round(df.loc[df['genus'] == 'Fucus']['alanin'].describe()[['min', 'mean', 'max']], 2))
df.hist()
plt.tight_layout()
plt.show()