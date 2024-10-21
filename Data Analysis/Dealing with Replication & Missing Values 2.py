# Advanced Practice Problems by chapter
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt import seaborn as sns
import glob
# set floating point formatting
pd.options.display.float_format = '{:,.6f}'.format

# Q3
# Range
  # Include previous content
  # Filling in Missing Data

import seaborn as sns
titanic = sns.load_dataset('titanic') titanic.head()

# Print the number of missing values for each column
titanic.isnull().sum()

# fill the missing data in the "age" column according to the following conditions:
"""
For rows where who is "man", fill missing values in the age column with the median of the non-missing values in the age column.
For rows where who is "woman", fill missing values in the age column with the 25th percentile (first quartile) of the non-missing values in the age column.
For rows where who is "child", fill missing values in the age column with the mean of the non-missing values in the age column.
"""

cond_man = (titanic['who'] == 'man')
stat = titanic.loc[cond_man, 'age'].median()
titanic.loc[cond_man, 'age'] = titanic.loc[cond_man, 'age'].fillna(stat)

cond_woman = (titanic['who'] == 'woman')
stat = titanic.loc[cond_woman, 'age'].quantile(0.25)
titanic.loc[cond_woman, 'age'] = titanic.loc[cond_woman, 'age'].fillna(stat)

cond_child = (titanic['who'] == 'child')
stat = titanic.loc[cond_child, 'age'].mean()
titanic.loc[cond_child, 'age'] = titanic.loc[cond_child, 'age'].fillna(stat)

print(f"missing value: {titanic['age'].isnull().sum()}") 
print(f"age mean: {titanic['age'].mean():.4f}")
