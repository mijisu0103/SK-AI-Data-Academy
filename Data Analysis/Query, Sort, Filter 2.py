# Chapter-specific advanced practice problems (Difficulty: Medium)
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import glob

# set floating point formatting
pd.options.display.float_format = '{:,.1f}'.format

# Q1
# Range
"""
Series, DataFrame data structures 
file input/output
querying, sorting, and condition filtering
"""

# Read /path/dataset/insurance.csv file and print this in DataFrame format (Print the top5 row)
pd.read_csv('/path/dataset/insurance.csv').head(5)

# Print the DataFrame that satisfies the following conditions:
  # Filter data where the sex column is 'male'.
  # Filter data where children is 2 or more.
  # Filter data where region is either 'northeast' or 'northwest'.
  # Sort by bmi and age in descending order, and select and print only the 3rd to 5th rows.

df = pd.read_csv('/path/dataset/insurance.csv')
cond1 = (df['sex'] == 'male')
cond2 = (df['children'] >= 2)
cond3 = (df['region'].isin(['northeast', 'northwest']))
df.loc[cond1 & cond2 & cond3].sort_values(['bmi','age'], ascending = False).iloc[3:6]

# Print the DataFrame that satisfies the following conditions:
  # Filter data where the sex column is 'female'.
  # Filter data where the person is a smoker (smoker column is 'yes').
  # Filter data where the age is in the 40s (between 40 and 49 years old).
  # Sort by charges in descending order, and print the top 5 rows.

cond1 = (df['sex'] == 'female')
cond2 = (df['smoker'] == 'yes')
cond3 = (df['age'] >= 40) & (df['age'] <= 49)
df.loc[cond1 & cond2 & cond3].sort_values('charges', ascending = False).head(5)

# Print the Series that satisfies the following conditions:
  # Filter data where bmi is 30 or higher but less than 40.
  # Filter data where the age is in the 30s.
  # Check the distribution of the region column in the filtered data.

cond1 = ((df['bmi'] >= 30) & (df['bmi'] < 40)) 
cond2 = ((df['age'] >= 30) & (df['age'] < 40)) 
df.loc[cond1 & cond2, 'region'].value_counts()





