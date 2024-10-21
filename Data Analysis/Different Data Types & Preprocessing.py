# Module import
from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
# Ignore warning
warnings.filterwarnings('ignore')
# change e notation expression method
pd.options.display.float_format = '{:.2f}'.format
# Show all columns
pd.set_option('display.max_columns', None)

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
  adult_male: Whether the passenger is an adult male
  deck: Deck number (a mix of letters and numbers)
  embark_town: Embarkation port name
  alive: Survival status (yes, no)
  alone: Whether the passenger traveled alone
"""

# To add a new column to a DataFrame
df1 = df.copy()
df1.head()

# Can add a new column by assigning arbitrary values
df1['VIP'] = True
df1.head()

# One can use insert() if one wants to add a column in the middle.
# insert(column_index, column_name, values)
df1.insert(5, 'RICH', df1['fare'] > 100)
df1.head()

# Deletion
# Deletion can be categorized into row deletion and column deletion.

# Row Deletion
# When deleting rows, specify the index to delete.
df1.drop(1)

# When deleting rows, one can specify a range for deletion.
df1.drop(np.arange(10))

# Can delete rows using fancy indexing
df1.drop([1, 3, 5, 7, 9])

# Column Deletion
df1.head()

# When deleting columns, one must specify the axis=1 option. 
# If one specifies the column position (e.g., the second position), one can omit axis=
df1.drop('class', axis=1).head()
df1.drop('class', 1).head()

# Can also delete multiple columns at once.
df1.drop(['who', 'deck', 'alive'], axis=1)

# To apply deletions immediately, one can do one of the following:
  # Specify inplace=True.
  # Reassign the result to the variable.
df1.drop(['who', 'deck', 'alive'], axis=1, inplace=True)
df1.head()

# Exercise
  # Please delete rows 1, 3, and 5 from df1.
  # Please delete the columns embarked, class, and alone from df1.
  # Print the top 10 rows of df1

df1 = df.copy()

df1.drop([1,3,5], inplace=True)
df1.drop(['embarked', 'class', 'alone'], axis=1, inplace=True)
df1.head(10)

# Operations Between Columns
# One can easily perform operations between columns.
df1 = df.copy()

# The total number of family members can be calculated by summing the sibsp column and the parch column
df1['family'] = df1['sibsp'] + df1['parch']
df1.head()

# Can also concatenate strings
df1['gender'] = df1['who'] + '-' + df1['sex']
df1.head()

# When performing operations between columns, one can use round() to specify the number of decimal places
# round(number, decimal_places)
df1['round'] = round(df1['fare'] / df1['age'], 2)
df1.head()

# If any one column involved in the operation contains a NaN value, the result will be NaN
df1.loc[df1['age'].isnull(), ['fare', 'age', 'round']].head()

# Exercise
# Use the Iris flower dataset to solve the following problems.
"""
  species: Type of iris flower
  sepal_length: Length of the sepal
  sepal_width: Width of the sepal
  petal_length: Length of the petal
  petal_width: Width of the petal
"""

iris = sns.load_dataset('iris')
iris.head()

# To create a new column named sepal by multiplying sepal_length and sepal_width, 
# and then display the top 5 rows
iris['sepal'] = iris['sepal_length'] * iris['sepal_width']
iris.head(5)

# create a new column named petal by multiplying petal_length and petal_width, 
# and then display the top 5 rows
iris['petal'] = iris['petal_length'] * iris['petal_width']
iris.head(5)

# remove the petal_length and petal_width columns from the DataFrame 
# and then display the top 5 rows
iris.drop(['petal_length', 'petal_width'], axis=1, inplace=True)
iris.head(5)

# To sort the flowers where species is "setosa" by the sepal column in descending order 
# and then display the top 10 rows
cond1 = (iris['species'] == 'setosa')
iris.loc[cond1].sort_values('sepal', ascending=False).head(10)

# To calculate the difference between the mean of the sepal column and the mean of the petal column
iris['sepal'].mean() - iris['petal'].mean()

# category type
df1 = df.copy()
df1.head(2)

df1.info()

# When one changes a column to a categorical type, the categories will be displayed alongside the values
df1['who'].astype('category').head()

# Apply changes
df1['who'] = df1['who'].astype('category')

# Changing a column to the category type also reduces memory usage
df1.info()

# If one has converted a column to the category type, 
# one can access category-specific attributes using the .cat accessor

# Print category
df1['who'].cat.categories

# To change the names of categories in a categorical column while maintaining the original order
df1['who'].cat.categories = ['child','male','female']
df1['who'].value_counts()

# String Handling
from opendata import dataset
dataset.download('Small_Business_District_Information')

seoul = pd.read_csv('path/Small_Business_District_Information.csv')
seoul.head()

# Swapping columns and rows
seoul.head().T

# Top 5 rows of land_lot_address
seoul['land_lot_address'].head()

# To split the address strings in the land_lot_address column by whitespace, 
# one can use the str.split() function. 
# Remember to use the .str accessor when applying string methods
seoul['land_lot_address'].str.split()

# If one wants to retrieve only the second element (district) from the split lists, 
# one can do so by accessing the index directly after splitting.

# One can access the second element (index 1) from the split lists 
# using the str accessor again after the initial split
seoul['land_lot_address'].str.split().str[1]

# can also use the apply() function to extract the second element (district) 
# from the split address strings without needing to use the str accessor
seoul['land_lost_address'].apply(lambda x: x.split()[1])

# Exercise
# In the Business_Category_Subclassification_Name column, 
# there are several business names like "Hanshik/Baekban/Hanjeongshik" separated by slashes. 
# Please modify it so that only the first value, "Hanshik," is displayed
# In cases where a single business is listed, such as "convenience_store", 
# it should remain as "convenience_store" without any changes.

seoul['Business_Category_Subclassification_Nam'].value_counts().head(10)

seo = seoul['Business_Category_Subclassification_Nam'].str.split('/').str[0]
seo.value_counts().head(10)

# Datetime - Date and Time
"""
The datetime type has unique features. 
One can easily access various date attributes using the .dt accessor in Pandas
The following are some common date-related variables available in Pandas’ dt accessor:
  pandas.Series.dt.year: Year
  pandas.Series.dt.month: Month
  pandas.Series.dt.day: Day
  pandas.Series.dt.hour: Hour
  pandas.Series.dt.minute: Minute
  pandas.Series.dt.second: Second
  pandas.Series.dt.microsecond: Microsecond
  pandas.Series.dt.nanosecond: Nanosecond
  pandas.Series.dt.week: Week
  pandas.Series.dt.weekofyear: Week of the year
  pandas.Series.dt.dayofweek: Day of the week
  pandas.Series.dt.weekday: Day of the week (same as dayofweek)
  pandas.Series.dt.dayofyear: Day of the year
  pandas.Series.dt.quarter: Quarter
"""

# to_datetime
# Load sample public bicycle data for Seoul
from opendata import dataset
dataset.download('Seoul_bicycle')

# Load Dataset
df2 = pd.read_csv('path/seoul_bicycle.csv')
df2.head()

df2.info()

# The rent_date column may appear to be a date-related column, but info() shows it as an object type. 
# To use the .dt accessor, one needs to convert it to a datetime type. 
# One can do this using the pd.to_datetime() function
pd.to_datetime(df2['rent_date'])

# To apply the conversion to the rent_date column by reassigning it directly
df2['rent_date'] = pd.to_datetime(df2['rent_date'])
df2.info()

# After applying the conversion, one can use the .dt accessor to access datetime attributes
df2['rent_date'].dt.year
df2['rent_date'].dt.month
df2['rent_date'].dt.day
df2['rent_date'].dt.dayofweek

# Exercise
# Load Dataset
df2 = pd.read_csv('path/seoul_bicycle.csv')
df2.head()

# To extract the year, month, day, and day of the week from the rent_date column,
# add them as new columns
# and to view top 5 rows
df2['rent_date'] = pd.to_datetime(df2['rent_date'])
df2.head()

# pd.cut() - Binning
# pd.cut() is used to divide continuous values into discrete intervals (bins) and categorize them
df2.head()

# can directly set the ranges for binning when using pd.cut()
# When one specifies right=False in pd.cut(), 
# the right endpoint of the bins will not be included in the intervals

bins = [0, 6000, 100000, df2['distance'].max()]
pd.cut(df2['distance'], bins, right=False)

# When using pd.cut(), one can specify labels for the bins, 
# but the number of labels must be one less than the number of bins
labels = ['low','avg','high']
pd.cut(df2['distance'], bins, labels=labels, right=False)

# can easily group data using pd.cut()
df2.head()

# can specify the number of bins one wants to divide the data into by setting the bins option in pd.cut()
df2['distance_cut'] = pd.cut(df2['distance'], bins=3)
df2['distance_cut'].value_counts()

"""
When one observes that most of the data is concentrated in the first bin, 
it may indicate that using pd.cut() with equal-width bins is not an appropriate method for one's dataset. 
This happens because pd.cut() divides the range from the minimum to the maximum into the specified number of bins, 
which can lead to issues when there are outliers or skewed distributions
"""

# pd.qcut() - Quantile-Based Binning
"""
pd.qcut() is used to divide data into equal-sized bins based on the distribution of the data. 
Unlike pd.cut(), which creates bins of equal width, pd.qcut() ensures that 
each bin has the same number of data points, thus preserving the distribution of the data as much as possible.
"""

df2['distance_qcut'] = pd.qcut(df2['distance'], q=3)
df2['distance_qcut'].value_counts()

# While pd.qcut() creates bins that appear to be evenly distributed in terms of the number of data points, 
# the actual intervals between the bin edges may not be equal.
# Can also specify custom quantiles when using pd.qcut()
qcut_bins = [0, 0.2, 0.8, 1]
pd.qcut(df2['distance'], qcut_bins)

# One can also specify labels when using pd.qcut(), similar to how one does it with pd.cut(). 
# Like before, the number of labels must be one less than the number of bins, 
# since each label corresponds to an interval created by the quantiles.
qcut_labels = ['less','avg','many']
pd.qcut(df2['distance'], qcut_bins, labels=qcut_labels).value_counts()

# Exercise
sample = sns.load_dataset('titanic')
sample.head(3)

# Divide the age into the following ranges:
  # 1. Greater than 0 years and less than or equal to 15 years
  # 2. Greater than 15 years and less than or equal to 30 years
  # 3. Greater than 30 years and less than or equal to 45 years
  # 4. Greater than 45 years and up to the maximum value

# Divide the age data into the specified ranges and create a new column called age_bin 
# using the pd.cut() function
bins = [0, 15, 30, 45, sample['age'].max()]
sample['age_bin'] = pd.cut(sample['age'], bins, right=True)
sample['age_bin'].value_counts()

# To divide the age data into three equal-sized bins (quantiles) 
# and label them as 'young', 'normal', and 'old', 
# one can use the pd.qcut() function
lables = ['young', 'normal', 'old']
sample['age_qbin'] = pd.qcut(sample['age'], q=3, labels = labels)
sample['age_qbin'].value_counts()



