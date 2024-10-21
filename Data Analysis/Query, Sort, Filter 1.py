# Module import
from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

# Dataset that will be used for exercieses
# Titanic: Data analysis of passengers' fatalities and survivors

"""
Titanic was the largest passenger ship in the world at the time of its construction, but it collided with an iceberg and sank on its first and last voyage in 1912, becoming a tragic passenger ship. 
It is probably the most famous passenger ship and shipwreck in the world. Although it has been over 100 years since it sank, it is still the most famous shipwreck in the world.

While the number of deaths is not the highest, its fame is partly due to the impact of a globally renowned movie. 
Additionally, it had a significant influence on society, which had high expectations for the cutting-edge technology of the time. 
It became a major disaster shortly after the dawn of the modern era, with several notable figures losing their lives.
Because of this, it became the most famous shipwreck.

Furthermore, this event led to the establishment of various safety treaties, which adds to its lasting fame
"""

df = sns.load_dataset("titanic")
df.head()

# Explanation of each column
  """
  survived: Survival status (1: Survived, 0: Deceased)
  pclass: Ticket class (1st, 2nd, 3rd class)
  sex: Gender
  age: Age
  sibsp: Number of siblings + spouses aboard
  parch: Number of parents + children aboard
  fare: Fare paid for the ticket
  embarked: Port of embarkation (S: Southampton, C: Cherbourg, Q: Queenstown)
  class: Same as pclass (ticket class)
  who: Man, Woman, Child
  adult_male: Whether the person is an adult male (True/False)
  deck: Deck number (mix of letters and numbers)
  embark_town: Name of the port of embarkation
  alive: Survival status (yes: Survived, no: Deceased)
  alone: Whether the passenger was traveling alone (True/False)
  """

# Data Analysis
# Main goal
  # Analysis of Titanic Survivors and Deceased Using Pandas
  # Based on the data, determine which passengers had a high survival rate and which had a low survival rate.

# head() for Viewing the Beginning / tail() for Viewing the End
"""
By default, 5 rows are retrieved. 
One can specify the number of rows one wants to retrieve by explicitly entering a number inside the parentheses.
"""

df.head()

df.tail()

df.head(3)

df.tail(7)


# info()
# Displays Information by Column
# This is used to check the number of entries in the data and the data type (dtype) of each column

df.info()

"""
The object type can be easily thought of as a string.
However, there is also a category type. 
The category type refers to columns that contain strings but can be categorized, such as "male" and "female."
"""

# value_counts()
"""
This is used to check the distribution of values in each column.
If one wants to check the data distribution for men, women, and children, one can execute it as follows.
"""

df['who'].value_counts()

# Exercise
df.head()


# embark_town is a column that indicates the port where the passenger boarded. 
# Please check the data distribution of passengers based on the port of embarkation.
df['embark_town'].value_counts()

# Please check the data distribution for the who column.
df['who'].value_counts()

# Attributes
"""
Attribute values are not retrieved in a functional form.
The commonly used attributes for a DataFrame are as follows:

  ndim
  shape
  index
  columns
  values
  T
"""

# ndim refers to the number of dimention. 
# DataFrame prints 2
df.ndim
# Output: 2

# shape refers to the number of rows and columns
df.shape
# Output: (number of rows, number of columns)

# index has the default value of RangeIndex
df.index
# Output: RangeIndex(start = 0, stop=900, step=1)

# Columns prints the name of columns
df.columns
# Output: 
"""
Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
       'alive', 'alone'],
      dtype='object')
"""

# Values print out all the data values in numpy array format
df.values
# Output: 
"""
array([[0, 3, 'male', ..., 'Southampton', 'no', False],
       [1, 1, 'female', ..., 'Cherbourg', 'yes', False],
       [1, 3, 'female', ..., 'Southampton', 'yes', True],
       ...,
       [0, 3, 'female', ..., 'Southampton', 'no', False],
       [1, 1, 'male', ..., 'Cherbourg', 'yes', True],
       [0, 3, 'male', ..., 'Queenstown', 'no', True]], dtype=object)
"""

# T stands for Transpose, which swaps the axis of Index and Column
df.T
# Output: Index becomes the columns e.g. 0, 1, 2, 3... Columns become Index e.g. survived, pclass, ...

# Type Conversion (astype)
df.info()

# Convert to int32 type
df['pclass'].astype('int32').head()

# Convert to float32 type
df['pclass'].astype('float32').head()

# Convert to object
df['pclass'].astype('str').head()

# Convert to category
# When converting to category, categories are printed as well
df['pclass'].astype('category').head()

# Sort
"""
sort_index: Sorting by index
Sorts the data based on the index. (By default, it is sorted in ascending order) 
To apply descending order, set the option ascending=False.)
"""

df.sort_index().head(5)

df.sort_index(ascending=False).head(5)

# sort_values: Sorting by values
"""
Sort rows based on values.
Set the row to be used as the basis in the by parameter.
One can specify more than one column in by to sort.
One can also specify ascending/descending order for each column.
"""

df.sort_values(by='age').head()

# Sorting in descending order: ascending=False
df.sort_values(by='age', ascending=False).head()

# String columns can also be sorted in ascending/descending order, and they will be sorted alphabetically
df.sort_values(by='class', ascending=False).head()

# One can sort values based on more than one column
df.sort_values(by=['fare', 'age']).head()

# One can also specify ascending/descending order for each column individually
df.sort_values(by=['fare', 'age'], ascending=[False, True]).head()

# Exercise
# The tips dataset represents the revenue of a U.S. restaurant and the tips paid to the waitstaff.
tips = sns.load_dataset('tips')
tips.head()

# Sort by total_bill and tip in descending order and display the top 10 entries
tips.sort_values(by = ['total_bill', 'tip'], ascending = [False, False]).head(10)

# Sort by size in descending order and by tip in ascending order. 
# Display only the top 10 data
tips.sort_values(by = ['size', 'tip'], ascending = [False, True]).head(10)

# Indexing, Slicing, Condition Filtering
df.head()

# loc - indexing / slicing
# Can do indexing and slicing
# Be mindful that slicing follows the rule [start (inclusive): end (inclusive)], and both are included

# Indexing example
df.loc[5, 'class']

# Fancy Indexing example
df.loc[2:5, ['age', 'fare', 'who']]

# Slicing example
df.loc[2:5, 'class':'deck'].head()

df.loc[:6, 'class':'deck']

# Exercise
df

# Index or slice in a way that produces the following result
# Q1
df.loc[3:7]

#Q2
df.loc[:4, 'pclass':'fare']

#Q3
df.loc[2:10:2, 'age' : 'who' : 6]

# loc - Condition Filtering
# By creating the boolean index, can extract data that only meet the condition
cond = (df['age'] >= 70)
cond

df.loc[cond]

# loc - multiple conditions
# First, define the conditions and then create composite conditions using the & and | operators.

# Define Condition 1
cond1 = (df['fare'] > 30)

# Define Condition 2
cond2 = (df['who'] == 'woman')

# Composite conditions using AND (&)
df.loc[cond1 & cond2]

# Composite conditions using OR (|)
df.loc[cond1 | cond2]

# Assign data after applying condition filters
cond = (df['age'] >= 70)
cond

# Filter condition
df.loc[cond]

# Extract age column only
df.loc[cond, 'age']

# Can assign desired values after applying condition filters. 
# Be mindful of selecting a single column
df.loc[cond, 'age'] = -1

df.loc[cond]

# Exercise
# Reload the data
df = sns.load_dataset("titanic")
df.head()

"""
Enter the code that satisfies the following conditions: 
Filter male passengers aged 30 or older, 
sort them in descending order by fare, and 
display the top 10 results
"""

cond1 = (df['who'] == 'man')
cond2 = (df['age'] >= 30)
df.loc[cond1 & cond2].sort_values('fare', ascending=False).head(10)

"""
Enter the code that satisfies the following conditions: 
Filter passengers aged 20 or older but under 40, 
who are in either 1st or 2nd class. 
Display only the columns 'survived,' 'pclass,' 'age,' and 'fare,' and 
limit the output to 10 rows
"""

cond1 = (df['age'] >= 20) & (df['age'] < 40)
cond2 = (df['pclass'] < 3)
df.loc[cond1 & cond2, ['survived','pclass','age','fare']].head(10)

#iloc
"""
Similar to loc, but only indexes are allowed. 
Like loc, both indexing and slicing are possible
"""

df.head()

# Indexing
df.iloc[1, 3]

# Fancy Indexing
df.iloc[[0, 3, 4], [0, 1, 5, 6]]

# Slicing
df.iloc[:3, :5]

# isin
# The inclusion of specific values can be compared using the isin function. 
# The Python in keyword cannot be used
sample = pd.DataFrame({'name': ['kim', 'lee', 'park', 'choi'],
                        'age': [24, 27, 34, 19]
                      })
sample

sample['name'].isin(['kim', 'lee'])

sample.isin(['kim', 'lee'])

# It works perfectly with condition filtering using loc as well
condition = sample['name'].isin(['kim', 'lee'])

sample.loc[condition]

# Exercise
tips = sns.load_dataset('tips')
tips.head()

"""
Filter the tips dataset to include only rows where the day is Friday (Fri) or Saturday (Sat). 
Then, filter rows where the tip is less than $10. 
Display only the columns total_bill, tip, smoker, and time. 
Show the top 10 rows
"""

cond1 = (tips['day'] == 'Fri') | (tips['day'] == 'Sat')
cond2 = (tips['tip'] < 10)
tips.loc[cond1 & cond2, ['total_bill','tip','smoker','time']].head(10)
















