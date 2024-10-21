# Module import
from IPython.display import Image import numpy as np
import pandas as pd
import seaborn as sns
import warnings warnings.filterwarnings('ignore')

# Load dataset
df = sns.load_dataset('titanic') 
df.head()

# Column Descriptions:
"""
  survived: Survival status (1: Survived, 0: Died)
  pclass: Seat class (1st class, 2nd class, 3rd class)
  sex: Gender
  age: Age
  sibsp: Number of siblings + spouses
  parch: Number of parents + children
  fare: Seat fare
  embarked: Port of embarkation (S, C, Q)
  class: Same as pclass
  who: Man, Woman, Child
  adult_male: Whether the person is an adult male
  deck: Deck number (mix of letters and numbers)
  embark_town: Name of the embarkation town
  alive: Survival status (yes, no)
"""

# Statistics
"""
Statistics are a very important factor in data analysis. 
Since Pandas provides statistical calculation functions for data, 
it is easy to compute statistical values.
"""

# describe() - Summary statistics: 
# One can check the overall key statistics. 
# By default, it displays the statistical table for numerical columns.
"""
  count: Number of data points
  mean: Average
  std: Standard deviation
  min: Minimum value
  max: Maximum value
"""

df.describe()

# One can also check the statistical table for string (categorical) columns.
"""
  count: Number of data points
  unique: Number of unique values
  top: Most frequent value
  freq: Frequency of the most frequent value
"""

df.describe(include='object')

# count() - Count
# Calculates the number of data points.
# When calculating the total count for the entire DataFrame
df.count()
df['age'].count()

# mean() - Mean
# Calculates the average of the data.
# The mean of the DataFrame.
df.mean()
df['age'].mean()

# Mean - Conditional Mean
# Calculate the average age of adult males
condition = (df['adult_male'] == True) 
df.loc[condition, 'age'].mean()

# Exercise
# Calculate the average age and the count of passengers who meet the following conditions:
  # Fare paid is between 30 (inclusive) and 40 (exclusive).
  # Pclass is 1st class
df.head()

# Calculate the count of data in the age column
cond1 = ((df['fare'] >= 30) & (df['fare'] < 40)) 
cond2 = (df['pclass'] == 1)
df.loc[cond1 & cond2, 'age'].count()

# Calculate the mean of the age column
df.loc[cond1 & cond2, 'age'].mean()

# skipna = True option
# In descriptive statistics functions, skipna=True is set by default.
# If skipna=False is set, any column containing NaN values will return NaN in the output.

# Case when specifying skipna = False
df.mean(skipna=False)
# NaN value is shown

# Case when specifying skipna = True
df.mean(skipna=True)
# NaN value does not exist in the output

# median() - Median
# Prints the median value of the data. It is the middle value when the data is sorted in ascending order.
# In cases where outliers exist, the median is often preferred over the mean as a representative value.
pd.Series([1, 2, 3, 4, 5]).median()
# Output: 3.0

pd.Series([4, 5, 1, 2, 3]).median()
# Output: 3.0

# In the case of an even number of data points, 
# the median is calculated by taking the average of the two middle values.
pd.Series([1, 2, 3, 4, 5, 6]).median()
# Output: 3.5

# One can observe a slight difference between the mean and median of the age column.
print(f"Average age: {df['age'].mean():.5f}\nMedian age: {df['age'].median()}\nDifference: {df['age'].mean() - df['age'].median():.5f}")
# Output:
"""
Average age: 29.69912
Median age: 28.0
Difference: 1.69912
"""

# sum() - Total
# The sum of the data. For string columns, all data may be concatenated and output as a single string
df.loc[:, ['age', 'fare']].sum()

# Print the total for a single column.
df['fare'].sum()

# cumsum() - Cumulative sum & cumprod() - Cumulative product
# Can calculate cumulative sum
df['age'].cumsum()

# Can also calculate cumulative product, but generally are not used much as values get too large
df['age'].cumprod()

# var() - Variance
data = [your_data]  # Replace with your list of numbers

# mean = sum(data) / len(data)
# variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)


# Mean
fare_mean = df['fare'].values.mean()

# Variance
my_var = ((df['fare'].values - fare_mean) ** 2).sum() / (df['fare'].count() - 1) 
my_var

df['fare'].var()

# std() - Standard Deviation
# Standard Deviation = square root of variance
np.sqrt(df['fare'].var())

df['fare'].std()

# min() - Minimum value, max() - Maximum value
# Min value
df['age'].min()

# Max value
df['age'].max()

# agg - Aggregation: Applying multiple statistical functions (multiple functions applied)
# Apply agg to a single column.
df['age'].agg(['min', 'max', 'count', 'mean'])

# Apply agg to multiple columns
df[['age', 'fare']].agg(['min', 'max', 'count', 'mean'])

# Exercise
# Solve the following problems using diamond data
diamond = sns.load_dataset('diamonds') 
diamond

# Find the minimum value of depth
diamond['depth'].min()

# Print the mean and the variance of carat simultaneously
diamond['carat'].agg(['mean', 'var'])

# Print the sum and the standard deviation of x and y
diamond[['x', 'y']].agg(['sum', 'std'])

# Quantile() - Quantile
"""
A quantile refers to a point that divides given data into equal-sized intervals. 
For example, to calculate the 10th percentile, one input 0.1, and for the 80th percentile, one input 0.8 to get the value.
"""

# 10% quantile
df['age'].quantile(0.1)

# 80% quantile
df['age'].quantile(0.8)

# unique() - Unique values, nunique() - Number of unique values
# These functions are used when you want to find unique values and the number of unique values.

# unique()
df['who'].unique()

# nunique()
df['who'].nunique()

# mode() - Mode
# The mode refers to the data that appears most frequently.
df['who'].mode()

# It can also be applied to categorical data.
df['deck'].mode()

# Exercise
# Solve following problems using penguin data
penguin = sns.load_dataset('penguins') 
penguin

# Print unique value of species column
penguin['species'].unique()

# Print the mode of the "island" column
penguin['island'].mode()

# Print the 10th percentile value (lower 10%) of the "body_mass_g" column
penguin['body_mass_g'].quantile(0.1)

# Print the 80th percentile value (higher 20%) of the "body_mass_g" column
penguin['body_mass_g'].quantile(0.8)

# corr() - Correlation
# One can check the correlation between columns using corr().
# It has a range between -1 and 1.
# The closer to -1, the more inversely proportional the relationship; 
# the closer to 1, the more directly proportional the relationship.

df.corr()

# can check the correlation for a specific column
df.corr()['survived']
























