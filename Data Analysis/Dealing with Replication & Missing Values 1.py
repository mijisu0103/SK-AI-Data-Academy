# Module import
from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

# Load Dataset
df = sns.load_dataset('titanic')
df.head()

# Column Descriptions:
"""
  survived: Survival status (1: Survived, 0: Deceased)
  pclass: Seat class (1st class, 2nd class, 3rd class)
  sex: Gender
  age: Age
  sibsp: Number of siblings + spouses
  parch: Number of parents + children
  fare: Ticket fare
  embarked: Embarkation port (S, C, Q)
  class: Same as pclass
  who: Man, woman, or child
  adult_male: Whether the person is an adult male
  deck: Deck number (combination of letters and numbers)
  embark_town: Embarkation port name
  alive: Survival status (yes, no)
"""

# copy
# Duplicate DataFrame. Modifying the duplicated DataFrame does not affect the original one
df.head()

df_copy = df.copy()
df_copy.head()

# Modify the 'age' in df_copy to 99999 arbitrarily
df_copy.loc[0, 'age'] = 99999
# Can check the modification has been reflected
df_copy.head()

# However, original DataFrame's data remains the same without the changes
df.head()

# Missing values
# Missing values refers to empty or null values. 
# Handling missing data is crucial. To deal with missing data, one must know the following steps:
"""
  Checking for missing data
  Checking for non-missing data
  Filling in missing data
  Removing missing data
"""

# To check missing values - isnull(), isna()
# To check the number of missing values for each column, one can use the sum() function.
# isnull()
df.isnull().sum()

# isna()
# It works exactly the same as isnull(). 
# Feel free to use whichever is more convenient (even the documentation is the same)
df.isna().sum()

# To sum up the total number of missing values in the entire DataFrame, 
# one can use the sum() function twice
df.isnull().sum().sum()

# Checking for non-missing data - notnull()
# notnull() is exactly the opposite of isnull()
df.notnull().sum()

# Filtering Missing Data
# The isnull() function is a boolean index that identifies missing data.
# In other words, one can apply it to loc to filter data based on conditions
df.loc[df['age'].isnull()]

# Exercise
# Please fill in the missing values of the "age" column with 30 for the Titanic passengers' data.
df = sns.load_dataset('titanic')

df['age'].isnull().sum()

cond = (df['age'].isnull())
df.loc[cond, 'age']=30

assert df['age'].isnull().sum() == 0
assert df['age'].mean().round(4) == 29.7589

# Filling Missing Data - fillna()
# By using fillna(), one can fill in missing values all at once with a specified value
df = sns.load_dataset('titanic')
df1 = df.copy()
df1.tail()

# One can confirm that the missing value at index 888 has been filled with 700
df1['age'].fillna(700).tail()

df1['age'] = df1['age'].fillna(700)
df1.tail()

# Filling with statistical values
# One can fill missing values using statistical measures such as the mean, median, or mode
df1 = df.copy()
df1.tail()

# Fill missing values with the mean
df1['age'].fillna(df1['age'].mean()).tail()

# Fill missing values with the median
df1['age'].fillna(df1['age'].median()).tail()

# Exercise
"""
Fill the missing values for male passengers' ages with their mean values
Fill the missing values for female passengers' ages with their mean values
After filling all missing values, print the mean of age column (Execute verification code to check whether right values are being printed)
"""

cond_male = (df1['sex'] == 'male')
male_mean = df1.loc[cond_male, 'age'].mean()
df1.loc[cond_male, 'age'] = df1.loc[cond_male, 'age'].fillna(male_mean)

cond_female = (df1['sex'] == 'female')
female_mean = df1.loc[cond_female, 'age'].mean()
df1.loc[cond_female, 'age'] = df1.loc[cond_female, 'age'].fillna(female_mean)

assert (df1['age'].isnull().sum() == 0)
assert df1['age'].mean().round(5) == 29.73603

# To fill missing values with mode
df1['deck'].mode()

# When filling missing values with the mode (most frequent value), 
# one must specify the 0th index to extract the value before using it to fill the missing data
df1['deck'].mode()[0]
df1['deck'].fillna(df1['deck'].mode()[0]).tail()

# To remove rows with NaN (missing) values
df1 = df.copy()
df1.tail()

# Using dropna() with how='any' removes any row that contains at least one NaN value
df1.dropna()

# The default option for dropna() is how='any'. You can change this behavior as follows:
"""  
  how='any': Drops the row if at least one NaN value is present.
  how='all': Drops the row only if all values in that row are NaN.
"""

df1.dropna(how='all')















