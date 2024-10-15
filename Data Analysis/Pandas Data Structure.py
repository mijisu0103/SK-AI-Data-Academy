from IPython.display import Image
import numpy as np

# Pandas

# Pandas Overview
"""Pandas is a Python package designed to make it easy and intuitive to work with relational or labeled data, offering fast and flexible data structures.

It is also one of the most powerful and flexible open-source data analysis/management tools available for any language.

Pandas is suitable for the following types of data:

    Tabular data consisting of rows and columns like SQL tables or Excel spreadsheets
    Time series data, ordered or unordered
    Other forms of observational/statistical datasets"""

# Alias for Pandas
# The pandas library is typically imported with alias pd.
import pandas as pd

pd

# Output
<module 'pandas' from '/home/user/.local/lib/python3.10/site-packages/pandas/__init__.py'>

# Pandas version check
pd.__version__

# Series

"""The Series in Pandas is a one-dimensional array with the following characteristics:

    It holds data in a dimensional array structure.
    Indexing is available.
    It has a data type (dtype)."""

# Creating Series
# Case where created Series using numpy array

# Creating numpy
arr = np.arange(100, 105)
arr

# Output
array([100, 101, 102, 103, 104])

s = pd.Series(arr)
s

# Output
0    100
1    101
2    102
3    103
4    104
dtype: int64

# Case where created Series using dtype
s = pd.Series(arr, dtype='int32')
s

# Output
0    100
1    101
2    102
3    103
4    104
dtype: int32

# Case where created Series using a list
s = pd.Series(['Manager', 'Deputy Manager', 'Assistant Manager', 'Employee', 'Intern'])
s

# Output
0    Manager
1    Deputy Manager
2    Assistant Manager
3    Employee
4    Intern
dtype: object

# Mixed data types:
# When creating a Series with various data type, it will be created with the object dtype.
s = pd.Series([91, 2.5, 'Sports', 4, 5.16])
s

# Output
0    91
1    2.5
2    Sports
3    4
4    5.16
dtype: object

# Exercise
# Create the following series:
    # dtype should be float32

pd.Series([3,5, 7, 9, 11], dtype = 'float32')

# Output
0    3.0
1    5.0
2    7.0
3    9.0
4    11.0
dtype: float32

# More efficient method
arr = np.arane(3, 12, 2)
pd.Series(arr, dtype = 'float32')

# Output
0    3.0
1    5.0
2    7.0
3    9.0
4    11.0
dtype: float32

# Another exercise
pd.Series(['A', 'B', 'C', 'D', 'E'], dtype = 'object')

# Output
0    A
1    B
2    C
3    D
4    E
dtype: object

# More efficient method
pd.Series(list('ABCDE'))

# Output
0    A
1    B
2    C
3    D
4    E
dtype: object

# Indexing
s = pd.Series(['Manager', 'Deputy Manager', 'Assistant Manager', 'Employee', 'Intern'])
s

# Output
0    Manager
1    Deputy Manager
2    Assistant Manager
3    Employee
4    Intern
dtype: object

# When creating a Series, the index is automatically assigned sequentially starting from 0. 
# This default index is known as RangeIndex

s.index

# Output
RangeIndex(start=0, stop=5, step=1)

# Indexing example
s[0]

# Output
'Manager'

# Fancy indexing
s[[1, 3]]

# Output
1    Deputy Manager
3    Employee
dtype: object

idx = [0, 1, 3]
s[idx]

# Output
0    Manager
1    Deputy Manager
3    Employee
dtype: object

s[np.arange(1, 4, 2)]
1    Deputy Manager
3    Employee
dtype: object

# Boolean indexing
# Create a boolean series to filter values based on a condition:
np.random.seed(0)
s = pd.Series(np.random.randint(10000, 20000, size=(10,)))
s

# Output
0    12732
1    19845
2    13264
3    14859
4    19225
5    17891
6    14373
7    15874
8    16744
9    13468
dtype: int64

s > 15000

# Output
0    False
1    True
2    False
3    False
4    True
5    True
6    False
7    True
8    True
9    False
dtype: bool

# Filter the data which is greater than 15000
s[s > 15000]

# Output
1    19845
4    19225
5    17891
7    15874
8    16744
dtype: int64

# You can replace the default RangeIndex with a custom index in a Series.
s = pd.Series(['Marketing', 'Management', 'Development', 'Planning', 'HR'], index=['a', 'b', 'c', 'd', 'e'])
s

# Output
a    Marketing
b    Management
c    Development
d    Planning
e    HR
dtype: object

s.index

# Output
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

# Once a custom index is assigned, you can retrieve data using the new index labels
s['c']

# Output
'Development'

s[['a', 'd']]

# Output
a    Marketing
d    Planning
dtype: object

# Can create a Series first and then assign new index values using the index attribute to specify custom indices:
s = pd.Series(['Marketing', 'Management', 'Development', 'Planning', 'HR'])
s.index

# Output
RangeIndex(start=0, stop=5, step=1)

s.index = list('abcde')
s

# Output
a    Marketing
b    Management
c    Development
d    Planning
e    HR
dtype: object

# Exercise 
# To create the following Series and assign it to the sample variable
sample = pd.Series(np.arange(10, 51, 10), index = list('abcde'))
sample

# Output
a    10
b    20
c    30
d    40
e    50
dtype: int64

# Query 'b' and 'd' data from the sample Series
sample[['b', 'd']]

# Output
b    20
d    40
dtype: int64

np.random.seed(20)
sample2 = pd.Series(np.random.randint(100, 200, size=(15,)))
sample2

0     199
1     190
2     115
3     195
4     128
5     190
6     109
7     120
8     175
9     122
10    171
11    134
12    196
13    140
14    185
dtype: int64

# Filter the data in sample2 for values that are less than or equal to 160
cond = sample2 <= 160
sample2[cond]

# Output
2     115 
4     128
6     109
7     120
9     122
11    134
13    140
dtype: int64

# Filter the data in sample2 where the values are between 130 and 170 (inclusive)
cond = (sample2 >= 130) & (sample2 <= 170)
sample2[cond]

# Output
11    134
13    140
dtype: int64

# Attribute

# Values
# The values attribute in a Pandas Series returns the data (values) in the form of a NumPy array
s.values

# Output
array(['Marketing', 'Management', 'Development', 'Planning', 'HR'], dtype=object)

# ndim - Dimension

# The ndim attribute in a Pandas Series returns the number of dimensions of the data.
# Since a Series is a one-dimensional data structure, ndim will always return 1.

s.ndim

# Output
1

# Shape
""" The shape attribute in a Pandas Series is used to determine the shape of the data. 
For a Series, the shape attribute returns a tuple representing the number of elements in the Series, which is the total count of data points.
The output is displayed in tuple format. """

s.shape

# Output
(5, )

# NaN (Not a Number)
"""
In Pandas, NaN represents missing or null data. 
When one wants to assign missing values to their data, they can use NumPy's np.nan.
"""

s = pd.Series(['Sunwha', 'Kangho', np.nan, 'Sojeong', 'Wooyoung'])
s

# Output
0     Sunwha
1     Kangho
2     NaN
3     Sojeong
4     Wooyoung
dtype: object

# Exercise
# Create the following Series

pd.Series(['apple', np.nan, 'banana', 'kiwi', 'gubong'], index=list('ABCDE'))

# Output
A     apple
B     NaN
C     banana
D     kiwi
E     gubong
dtype: object

# Handling missing values (NaN) in Pandas 
# This can be done using the isnull() and isna() functions.
# Both functions work identically and are used to detect NaN values in a Series or DataFrame.

s.isnull()

# Output
0     False
1     False
2     True
3     False
4     False
dtype: bool

s.isna()
0     False
1     False
2     True
3     False
4     False
dtype: bool

# Can apply isnull() or isna() in boolean indexing to filter out or 
# select only the NaN values or the non-NaN values from a Series or DataFrame.

s[s.isnull()]

# Output
2     NaN
dtype: object

s[s.isna()]
2     NaN
dtype: object

"""The notnull() function in Pandas is used to find values that are not NaN, 
meaning it returns True for values that are not missing and False for NaN values. 
It is useful when you want to filter or work with only non-missing data"""

s.notnull()

# Output
0    True
1    True
2    False
3    True
4    True
dtype: bool

s.notna()

# Output
0    True
1    True
2    False
3    True
4    True
dtype: bool

s[s.notnull()]

# Output
0     Sunwha
1     Kangho
3     Sojeong
4     Wooyoung
dtype: object

# Exercise
sample = pd.Series(['IT Service', np.nan, 'Semiconductor', np.nan, 'Bio', 'Autonomous Driving'])
sample

# Output
0    IT Service
1    NaN
2    Semiconductor
3    NaN
4    Bio
5    Autonomous Driving
dtype: object

# Filter only the missing (NaN) values from the sample Series
idx = sample.isnull()
sample[idx]

1    NaN
3    NaN
dtype: object

# Filter only the non-missing (non-NaN) values from the sample Series
idx = sample.notnull()
sample[idx]

# Output
0    IT Service
2    Semiconductor
4    Bio
5    Autonomous Driving
dtype: object

# Slicing
"""(Note) When accessing elements using numeric indexing in Pandas, the end index is not included. 
This means when you use slicing with numeric indices, the last index specified is not part of the result."""

s = pd.Series(np.arange(100, 150, 10))
s

# Output
0    100
1    110
2    120
3    130
4    140
dtype: int64

s[1:3]

# Output
1    110
2    120
dtype: int64

"""When using a string-based index in Pandas, both the start and end indices are included in the result. 
This differs from numeric indexing, where the end index is excluded."""

s.index = list('ABCDE')
s

# Output
A    100
B    110
C    120
D    130
E    140
dtype: int64

s['B':'D']

# Output
B    110
C    120
D    130
dtype: int64

# Exercise
np.random.seed(0)
sample = pd.Series(np.random.randint(100, 200, size=(10,)))
sample

# Output
0     144
1     147
2     164
3     167 
4     167 
5     109 
6     183 
7     121 
8     136 
9     187
dtype: int64

# Slice the sample Series to achieve the following result
sample[2:7]

# Output
2     164
3     167
4     167
5     109
6     183
dtype: int64

np.random.seed(0)
sample2 = pd.Series(np.random.randint(100, 200, size=(10,)), index=list('ABCDEFGHIJ'))
sample2

# Output
A     144 
B     147 
C     164 
D     167 
E     167 
F     109 
G     183 
H     121 
I     136 
J     187
dtype: int64

# Slice the sample2 Series and achieve the following result
sample2['F':'J']

# Output
F     109 
G     183 
H     121 
I     136 
J     187
dtype: int64

sample2[:'C']

# Output
A     144 
B     147 
C     164 
dtype: int64

sample2['B':'F']

# Output
B     147 
C     164 
D     167 
E     167 
F     109 
dtype: int64



# DataFrame
pd.DataFrame

"""
    two-dimensional data structure in Pandas, similar to an Excel spreadsheet. 
    It is made up of rows and columns, 
    where each column can have its own data type (dtype)
"""

# Creation
"""can create a DataFrame in Pandas using a list, specifically a 2D list (a list of lists). 
Each inner list represents a row of data."""

pd.DataFrame([[1, 2, 3], [4, 5, 6],[7, 8, 9]])

# Output
    0 1 2
---------- 
  0 1 2 3 
  1 4 5 6 
  2 7 8 9

# If one specifies columns while creating a DataFrame, each column will be assigned the given column names
pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['가', '나', '다'])

# Output
    A B C
---------- 
  0 1 2 3 
  1 4 5 6 
  2 7 8 9

"""
can also create a DataFrame using a dictionary, 
where the keys of the dictionary are automatically used as the column names, 
and the values (lists) are treated as the data for each column
"""

data = {
'name': ['Kim', 'Lee', 'Park'], 'age': [24, 27, 34], 'children': [2, 1, 3]
}

pd.DataFrame(data)

# Output
    name  age children
---------------------- 
  0  Kim   24     2 
  1  Lee   27     1 
  2 Park   34     3

# Attributes:
# A DataFrame in Pancas has the following attributes:

"""
    index: The row labels (default is RangeIndex if not specified)
    columns: The column names
    values: The underlying data as a NumPy array
    dtypes: The data types of each column
    T: The transpose of the DataFrame (rows become columns and vice versa)
"""

data = {
    'name': ['Kim', 'Lee', 'Park'], 
    'age': [24, 27, 34], 
    'children': [2, 1, 3]
}
df = pd.DataFrame(data)
df

# Output
    name  age children
---------------------- 
  0  Kim   24     2 
  1  Lee   27     1 
  2 Park   34     3

df.index

# Output
RangeIndex(start=0, stop=3, step=1)

df.columns

# Output
Index(['name', 'age', 'children'], dtype='object')

df.values

# Output
array([['Kim', 24, 2],
       ['Lee', 27, 1],
       ['Park', 34, 3]], dtype=object)

# The dtypes attribute of a DataFrame shows the data type (dtype) of each column. 
""" This helps one understand the type of data stored in each column, such as 
    integers (int64), floats (float64), or objects (typically used for strings)"""

df.dtypes

# Output
name     object
age      int64
children int64
dtype: object

df.T

# Output
            0      1     2   
---------------------------- 
  name     Kim    24     2 
  age      Lee    27     1 
  children Park   34     3

# Specify custom index
df

# Output
    name  age children
---------------------- 
  0  Kim   24     2 
  1  Lee   27     1 
  2 Park   34     3

df.index

# Output
RangeIndex(start=0, stop=3, step=1)

df.index = list('abc')

# Output
    name  age children
---------------------- 
  a  Kim   24     2 
  b  Lee   27     1 
  c Park   34     3

# Dealing with Column
"""
In a DataFrame, one can select a single column by specifying its name as the key. 
When one selects one column, the result is a Pandas Series
"""

df['name']
a     Kim
b     Lee
c     Park
Name: name, dtype: object

type(df['name'])

# Output
pandas.core.series.Series

# To select two or more columns in a Pandas DataFrame, one can use fancy indexing, which involves passing a list of column names. 
# This will return a new DataFrame

df[['name', 'children']]

# Output
    name children
---------------------- 
  a  Kim    2 
  b  Lee    1 
  c Park    3

type(df[['name', 'children']])

# Output
pandas.core.frame.DataFrame

# Can use the rename() method to change column names in a Pandas DataFrame
# The columns parameter takes a dictionary where the keys are the current column names, and the values are the new column names

df.rename(columns={'name': 'Name'})

# Output
    Name  age children
---------------------- 
  a  Kim   24     2 
  b  Lee   27     1 
  c Park   34     3

# The inplace=True option allows one to apply changes directly to the original DataFrame without creating a new copy. 
# This modifies the DataFrame in place

df.rename(columns={'name': 'Name'}, inplace=True)
df

# Output
    Name  age children
---------------------- 
  a  Kim   24     2 
  b  Lee   27     1 
  c Park   34     3

df = df.rename(columns={'name':'Name'})
df

# Output
    Name  age children
---------------------- 
  a  Kim   24     2 
  b  Lee   27     1 
  c Park   34     3

# Exercise
# Create the specified DataFrame and assign it to the variable df:

data = {
    'food': ['KFC', 'McDonald', 'SchoolFood'],
    'price': [1000, 2000, 2500],
    'rating': [4.5, 3.9, 4.2]
}
df = pd.DataFrame(data)
df

# Output
         food   price  rating
-------------------------------
  0  KFC          7     4.5 
  1  McDonald     9     3.9 
  2  SchoolFood  12     4.2

# Select and print only the food and rating columns from the df DataFrame
df[['food', 'rating']]

# Output
         food     rating
-------------------------
  0  KFC           4.5 
  1  McDonald      3.9 
  2  SchoolFood    4.2

# Rename the food column to place using the rename() method
df.rename(columns = {'food':'place'})

# Output
        place   price  rating
-------------------------------
  0  KFC          7     4.5 
  1  McDonald     9     3.9 
  2  SchoolFood  12     4.2
