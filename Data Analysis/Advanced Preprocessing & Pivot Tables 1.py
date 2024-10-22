# Module import
from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
# Ignore warnings
warnings.filterwarnings('ignore')

# Load Dataset
df = sns.load_dataset('titanic')
df.head()

# Columns Description
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

# apply() - Applying Functions
# The apply() function in Pandas is widely used for data preprocessing
# The apply() function is particularly useful
# When one wants to apply more complex logic to a DataFrame or a specific column
df.head()

# Can use the apply() function to change the values in the who column based on specific conditions
df['who'].value_counts()

# Defineing Function
def transform_who(x):
  if x == 'man':
    return 'male'
  elif x == 'woman':
    return 'female'
  else:
    return 'child'

# The distribution is as follows:
df['who'].apply(transform_who).value_counts()

def transform_who(x):
  return x['fare'] / x['age']

df.apply(transform_who, axis=1)

# apply() - Lambda Function
# One can use apply() with a lambda function to handle
# simple logic without the need to define a separate function.
df['survived'].value_counts()

# Change the values in a column to represent 0 for "deceased" and 1 for "survived"
df.head()

df['survived'].apply(lambda x: 'survived' if x == 1 else 'deceased')
df['survived'].apply(lambda x: 'survived' if x == 1 else 'deceased').value_counts()

# Exercise
sample = df.copy()
sample.head()

sample['class'].value_counts()

# To use apply() to change the values in the class column of a sample DataFrame 
# and then check the distribution before and after the change
def transform_class(x):
  if x == 'Third':
    return 'Third_class'
  elif x == 'First':
    return 'First_class'
  else:
    return 'Second_class'
sample['class'].apply(transform_class).value_counts()

# groupby() - Grouping Data
# The groupby() function in Pandas is used to group data based on specific criteria. 
# It is similar to creating pivot tables in Excel

df.head()

# To analyze the survival and death rates on the Titanic by gender
df.groupby('sex').mean()

# When using groupby(), it is essential to apply an aggregation function to summarize the grouped data

# Grouping by two or more columns
# One can simply pass a list of column names to the groupby() function

df.groupby(['sex', 'pclass']).mean()

# If one wants to focus on a specific column, such as the survived column, 
# while grouping by multiple columns, one can place the desired column at the end of the aggregation function.
df.groupby(['sex', 'pclass'])['survived'].mean()

# To neatly display the results when one is focusing on a specific column (like the survived column) 
# after performing a groupby() operation, 
# one can either wrap the result in pd.DataFrame() or use double brackets [[ ]] around the survived column
df.groupby(['sex', 'pclass'])['survived'].mean()
pd.DataFrame(df.groupby(['sex', 'pclass'])['survived'].mean())
df.groupby(['sex', 'pclass'])[['survived']].mean()

# reset_index(): Reset index
# reset_index(): This function is used to reset the index of a grouped DataFrame, 
# creating a new DataFrame in the process.
df.groupby(['sex', 'pclass'])['survived'].mean().reset_index()

# To obtain results for multiple columns after performing a groupby() operation in Pandas, 
# one can specify the columns one wants to aggregate at the end
df.groupby(['sex', 'pclass'])[['survived', 'age']].mean()

# When one wants to apply multiple statistical functions to the grouped data in Pandas, 
# one can use the agg() function within the groupby() method. 
df.groupby(['sex', 'pclass'])[['survived', 'age']].agg(['mean', 'sum'])

# Exercise
sample = df.copy()
sample

# Print the following using groupby()
# Survival rate per pclass column
sample.groupby('pclass')['survived'].mean()

# Survival rate and other aggregated statistics per embarked column
sample.groupby('embarked')['survived'].agg(['mean', 'var'])

# Survival rate and the number of survived people per who, pclass columns
sample.groupby(['who', 'pclass'])['survived'].agg(['mean', 'sum'])

# Fill in the missing values of males' ages using the mean of males' age
# Fill in the missing values of females' ages using the mean of females' age

# Check missing values
print(sample['age'].isnull().sum())
print(f"age mean: {sample['age'].mean():.2f}")

sample['age'] = sample.groupby('sex')['age'].apply(lambda x: x.fillna(x.mean()))

print(sample['age'].isnull().sum())
print(f"age mean: {sample['age'].mean():.2f}")


# The pivot_table() function in Pandas allows one to create a pivot table 
# similar to the functionality found in Excel. 
# It provides a way to summarize data by specifying an index, columns, and values to aggregate.

# To obtain a single column result for a specific group
df.pivot_table(index='who', values='survived')

# Write group on columns
df.pivot_table(columns='who', values='survived')

# To obtain a single column result for multiple groups 
df.pivot_table(index=['who', 'pclass'], values='survived')

# To create a pivot table in Pandas without having multi-level indexing (where columns are nested)
df.pivot_table(index='who', columns='pclass', values='survived')

# Applying multiple statistical functions
df.pivot_table(index='who', columns='pclass', values='survived', aggfunc=['sum', 'mean'])

# Exercise
tips = sns.load_dataset('tips')
tips.head()

# To create a pivot table using the tips dataset in Pandas, 
# where the values represent the average of the tip column
tips.pivot_table(index='smoker', columns='day', values='tip')

# Create the following pivot table. 
# For the values, calculate the average and sum for 'total_bill
tips.pivot_table(index='day', columns='time', values='total_bill', aggfunc=['mean','sum])
