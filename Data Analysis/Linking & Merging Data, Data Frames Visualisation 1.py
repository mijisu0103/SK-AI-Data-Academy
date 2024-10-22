# Module import
from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
# Ignore warnings
warnings.filterwarnings('ignore')

# Load Dataset
from opendata import dataset

# Download oil price data
dataset.download('oilprice')

# Load the data for the first half of the year from January to June
gas1 = pd.read_csv('data/gas_first_2019.csv', encoding='euc-kr')

print(gas1.shape)
gas1.head()

gas2 = pd.read_csv('data/gas_second_2019.csv', encoding='euc-kr')

# Load the data for the second half of the year from July to December
print(gas2.shape)
gas2.head()

# concat() - Data connection
# concat() connects DataFrames.
# It simply connects the specified DataFrames sequentially.

# Connection in the row direction
# By default, axis=0 is specified, connecting in the row direction.
# Additionally, it automatically finds and connects the same columns.
pd.concat([gas1, gas2])

# When connecting, the index is not reset as shown above, 
# so the number of the entire DataFrame and the index do not match
pd.concat([gas1, gas2]).iloc[90588:90593]

# Can connect while ignoring the index
gas = pd.concat([gas1, gas2], ignore_index=True)
gas

# Even if some columns of the DataFrames to be merged are missing or out of order, 
# it will automatically merge the same columns together
gas11 = gas1[['Region', 'Address', 'Name', 'Brand', 'Gasoline']] 
gas22 = gas2[['Brand', 'Number', 'Region', 'Name', 'Address', 'Diesel', 'Gasoline']]

gas11.head()

gas22.head()

pd.concat([gas11, gas22], ignore_index=True)

# Connect in the column direction
# Can connect in the column direction, and it can be specified with axis=1

# Arbitrary splitting of DataFrame for practice
gas1 = gas.iloc[:, :5]
gas2 = gas.iloc[:, 5:]

gas1.head()

gas2.head()

# Rows with the same index will be connected
 pd.concat([gas1, gas2], axis=1)

# merge() - Merge
# Even if the DataFrames have different structures, they can be merged if they have a common key (column)
df1 = pd.DataFrame({
    'Customer Name': ['Park Seri', 'Lee Daeho', 'Son Heungmin', 'Kim Yuna', 'Michael Jordan'],
    'Date of Birth': ['1980-01-02', '1982-02-22', '1993-06-12', '1988-10-16', '1970-03-03'],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male']
})
df1

df2 = pd.DataFrame({
    'Customer Name': ['Kim Yuna', 'Park Seri', 'Son Heungmin', 'Lee Daeho', 'Tiger Woods'],
    'Salary': ['2000 won', '3000 won', '1500 won', '2500 won', '3500 won']
})
df2

pd.merge(df1, df2)

# There are four ways to merge. 
# By specifying the how option, one can merge in four different ways, 
# each producing different results.
  # how: {left, right, outer, inner},
  # The default value is inner.

# how='inner'
pd.merge(df1, df2)

# how='left'
pd.merge(df1, df2, how='left')

# how='right'
pd.merge(df1, df2, how='right')

# how='outer'
pd.merge(df1, df2, how='outer')


# When the names of the columns to be merged are different
df1 = pd.DataFrame({
    'Name': ['Park Seri', 'Lee Daeho', 'Son Heungmin', 'Kim Yuna', 'Michael Jordan'],
    'Date of Birth': ['1980-01-02', '1982-02-22', '1993-06-12', '1988-10-16', '1970-03-03'],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male']
})
df1

df2 = pd.DataFrame({
    'Customer Name': ['Kim Yuna', 'Park Seri', 'Son Heungmin', 'Lee Daeho', 'Tiger Woods'],
    'Salary': ['2000 won', '3000 won', '1500 won', '2500 won', '3500 won']
})
df2

# Specify left_on and right_on.
# Ensure that both the 'Name' and 'Customer Name' columns are not dropped and remain intact
pd.merge(df1, df2, left_on='Name', right_on='Customer Name')








