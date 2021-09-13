import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Changing the theme
sns.set_theme()

# print(sns.get_dataset_names())
tips = sns.load_dataset("tips")
# print(tips)

# Dist Plots
# sns.distplot(tips['total_bill'], kde = False, bins = 30)

# Joint Plots
# sns.jointplot(x='total_bill', y='tip', data=tips)
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='scatter')
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='hist')
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
# sns.jointplot(x='total_bill', y='tip', data=tips, kind='resid')

# Pair plots
# sns.pairplot(tips, hue='sex')

# Rug plots
sns.rugplot(tips['total_bill'])

plt.show()