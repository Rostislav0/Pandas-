import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as ss



df = pd.read_csv('states.csv')
hs_grad = df['hs_grad']
poverty = df['poverty']

print('p =', ss.ttest_ind(hs_grad, poverty)[-1])

b0 = ss.linregress(df['hs_grad'], df['poverty']).intercept
b1 = ss.linregress(df['hs_grad'], df['poverty']).slope
print('b =', b0, '\nb1 =', b1)

print(np.corrcoef(poverty, hs_grad))
plt.scatter(x=hs_grad, y=poverty)
sns.regplot(x=hs_grad, y=poverty, data=df)
plt.ylabel('Бедность(%)')
plt.xlabel('Уровень образования(%)')
plt.title('Связь бедности и уровня образования')
plt.show()
