### Overview of SK-AI-Data-Academy foundational course curriculum through a practical Exercise

""" 
1. bookmark_revised.csv
Records data such as which user watched which program on which device.

2. coin.csv
Records details about which user purchased which type of subscription, when, and how much they bought. It includes monthly subscriptions or top-ups of points (referred to as coins in the Wavve system). For privacy reasons, time-related information is provided at the hourly level, not down to the second.

3. column_code_info.xlsx

4. content_info.csv
Contains information such as the content title, content duration (in seconds), and a summary of the storyline. If the content is a series (e.g., drama, TV animation), each episode is recorded separately. Therefore, Episode 1 and Episode 2 of a particular drama are assigned different content IDs.

5. movie_info.csv
Similar to the 4th file, but it includes additional information like the director, cast, viewing age rating, and the English title. The duration is also recorded in minutes.

6. service_revised.csv
Contains records such as subscription registration date, expiration date, subscription details, the device used for payment, and user information like gender and age.
"""


# Python Library for Data Analysis
"""
Python has several well-known libraries for data analysis, such as pandas, matplotlib, and seaborn.

pandas: This is a Python library for data manipulation and analysis. It provides a data structure called a DataFrame, along with various operations for processing data.

matplotlib: This is a Python library for data visualization (graph output). It allows you to easily create graphs using its various functions.

seaborn: Like matplotlib, seaborn is also a Python library for data visualization. It offers a simpler way to create graphs and provides easy options for styling the graphs, making it more convenient compared to matplotlib.
"""


import numpy as np  # Importing NumPy, a library for numerical computations.
import matplotlib.pyplot as plt  # Importing Matplotlib's Pyplot for creating visualizations.
import seaborn as sns  # Importing Seaborn for easier statistical visualizations.
import pandas as pd  # Importing Pandas for data manipulation and analysis.
import warnings  # Importing the warnings module to manage warning messages.

# Ignoring any warning messages to prevent unnecessary outputs.
warnings.filterwarnings('ignore')

# Removing Unicode minus warning (related to font settings for displaying minus signs properly).
plt.rcParams['axes.unicode_minus'] = False


import matplotlib.font_manager as fm
font_dirs = ['/usr/share/fonts/truetype/nanum', ]
font_files = fm.findSystemFonts(fontpaths=font_dirs) for font_file in font_files:
fm.fontManager.addfont(font_file)


#Font Setting for Korean
plt.rcParams['font.family'] = "NanumBarunGothic"


"""
Column Information Lookup
Tip: A column refers to each vertical data set in a table. In machine learning, it is often referred to as a feature. Conversely, the horizontal data sets are called rows.
"""

"""
Loading Excel Data
The loaded data type is a DataFrame, which has a two-dimensional structure. The data is assigned to the column_code variable.

Tip: Two-dimensional data consists of indices that refer to rows and columns. In contrast, one-dimensional data has only one index.
"""


# pd.DataFrame() -> Two-dimensional data structure, row-column structure

# Loading an excel file
column_code = pd.read_excel('/path/column_code_info.xlsx', header=1)

# View the top 5 rows of a DataFrame
column_code.head()

# To delete the first invalid column (axis=1) of a DataFrame
column_code = column_code.drop('Unnamed: 0', axis=1)

# View the updated table
column_code

# Check the size of a DataFrame (i.e., the number of rows and columns)
column_code.shape


# Coin
# Load the coin.csv file and assign it to the coin variable using pandas
coin = pd.read_csv('/path/coin.csv')

# Check the size of a DataFrame
coin.shape

# Load top 5 rows of a DataFrame
coin.head()
# By default, head() loads 5 rows. 
# If one specifies a number inside the parentheses, it will load that many rows.

"""
Checking for Missing Values
Tip: A missing value refers to data that is missing, often represented as NaN in the dataset.
Missing values can occur due to human error or issues with data recording equipment, among other reasons, and are common in real-world data. 
(For example, in a survey, some questions may not have been answered.)

If we remove all missing data, it can lead to significant data loss, which may cause problems in the analysis. 
How one handles missing data can significantly impact the results of one's data analysis.
"""

coin.isnull().sum()

# View detailed information about each column in a DataFrame
def show_column_desc(df): 
  col_list = []
  for col in df.columns:
    tmp = column_code.loc[column_code['column'] == col] 
    if len(tmp) > 0:
      col_list.append((col, tmp.iloc[0, 2]))
  display(df.head())
  return pd.DataFrame(col_list, columns=['column', 'desc'])

show_column_desc(coin)

# Count the number of occurrences of each productcode in the dataset in descending order
""" Tip. Descending order means that the values decrease in size, as shown below:
     Original data: [1, 2, 3, 4, 5]
     After sorting in descending order: [5, 4, 3, 2, 1] """

coin['productcode'].value_counts().head()

# To sort the values in the pgamount (actual payment amount) column
coin.sort_values('pgamount')

#To sort the values in the pgamount (actual payment amount) in descending order
coint.sort_values('pgamount', ascending = False)

# To sort the pgamount (actual payment amount) column in 
# descending order and display only the top 10 values
coin.sort_values('pgamount', ascending = False).head(10)

# To find the top 10 product codes with the highest average pgamount (actual payment amount)
coin.groupby('productcode')['pgamount'].mean().sort_values(ascending = False).head(10)

# To sort the average pgamount (actual payment amount) by registerhour (time of registration) in descending order
coin.groupby('registerhour')['pgamount'].mean().sort_values(ascending = False).head(10)

"""
To visualize the average pgamount (actual payment amount) by registerhour (time of registration) in descending order, 
one can use the plot() function in pandas
One can set the kind parameter to customize the type of graph (e.g., bar - bar chart, barh - horizontal bar chart, hist - histogram, scatter - scatter plot, box - box plot, etc).
"""

coin.groupby('registerhour')['pgamount'].mean().sort_values().reset_index(drop=True).plot(kind='barh')

# To load the bookmark.csv file with euc-kr encoding and assign it to the bookmark variable
# Tip. The reason for using encoding is to prevent corruption (garbled text) in data written in Korean
bookmark = pd.read_csv('/path/bookmark_revised.csv', encoding='euc-kr')
show_column_desc(bookmark)

# To check the size (number of rows and columns) of the bookmark DataFrame
bookmark.shape

# To view top5 row
bookmark.head()

# To find the top 20 most bookmarked title in the bookmark DataFrame
bookmark['title'].value_counts().head(20)

# To find the devicetype that has the most bookmarks
bookmark['devicetype'].value_counts()

# To load the "device" sheet from the column_code_info.xlsx Excel file 
# and assign it to the device_type variable
device_type = pd.read_excel('/path/column_code_info.xlsx', sheet_name = 'device') device_type

# To count the number of occurrences of each devicetype in the bookmark DataFrame 
# and then create a new DataFrame to store this information assigning bookmark_cnt
bookmark_cnt = bookmark['devicetype'].value_counts().reset_index() 
bookmark_cnt.columns = ['code', 'count']
bookmark_cnt

# Merging device_type and bookmark_cnt
# Tip: One can merge two or more DataFrames into one by using merging functions.

device_type.head()
bookmark_cnt.head()
output = pd.merge(device_type, bookmark_cnt)
output

# To sort the merged DataFrame by the count column in descending order, 
# One can use the sort_values() function
output.sort_values('count', ascending=False, ignore_index = True)

# To load the content_info.csv file and assign it to the content variable
content = pd.read_csv('/path/content_info.csv')

# To view top5 row
content.head()

# To view the information of rows and columns
content.shape

# To view detailed information about each column in the content DataFrame, 
# including data types and the number of non-null values
content.info()

# To extract and view the playtime column from the content DataFrame
content['playtime']

# To force the conversion of the playtime column to a numeric type
# Tip. Numeric data refers to data that is measured in the form of numbers. 
# Examples of numeric data include test scores, height, and weight.
# In contrast, categorical data refers to data that is presented in the form of several categories or items. 
# Examples of categorical data include gender, blood type, and region.
pd.to_numeric(content['playtime'])

# To check for errors or values in the playtime column that could not be converted to numeric, 
# one can look for rows where the conversion resulted in NaN
content.loc[302375]
print(content['playtime'][0])

def convert(x): try:
float(x)
except Exception as e:
        print(f'error: {e}')

content['playtime'].apply(convert)

# Still having an error due to the date format, have to convert this as well
import datetime 
datetime.datetime.fromtimestamp(1466.0).strftime('%H:%M:%S')

24 * 60 + 26

def convert_time(x): 
  try:
    x = float(x)
    ret = datetime.datetime.fromtimestamp(x).strftime('%H:%M:%S') 
  except Exception as e:
    ret = x 
  finally:
    return ret

# The apply() function in Python is used to apply a given function to a column in bulk
content['playtime'].apply(convert_time)

# To apply a function using apply() and reassign the result to the same column
content['playtime'] = content['playtime'].apply(convert_time) 
content['playtime']

# Use pd.to_timedelta() function to calculate 
# the total seconds for the playtime column
content['playtime'] = pd.to_timedelta(content['playtime'])
content['playtime_second'] = content['playtime'].dt.total_seconds()
content['playtime_second']

content['playtime'].dt.total_seconds()

content.info()
content.head()

# To create a histogram that shows the distribution of playtime (or any other numeric column
# Tip. A histogram is a graph that represents the frequency distribution using rectangular bars. 
# It allows one to quickly see how many data points fall into each category
sns.histplot(content['playtime_second'])

# To calculate and display the average playtime from the playtime column
content['playtime_second'].mean()

# To generate summary statistics for the playtime_second column
content['playtime_second'].agg(['min', 'max', 'median', 'mean'])

# Movie
# To load data from movie_info.csv and assign it to movie variable
movie = pd.read_csv('/path/movie_info.csv')

# To view top5 row
movie.head()

# To count the number of movieid entries for each nation, 
# and then sort the results in descending order
movie.groupby('nation')['movieid'].count().sort_values(ascending = False)

# To find the directors who have made the most movies and sort them in descending order
movie.groupby('director')['movieid'].count().sort_values(ascending = False)

# To convret runningtime to numeric column
movie.info()
movie.head(2)
movie.loc[20275]
pd.to_numeric(movie['runningtime'])

# Failed, so have to force the convert using pd.to_numeric()
# Apply errors='coerce'
movie['runningtime'] = pd.to_numeric(movie['runningtime'], errors = 'coerce') 
movie['runningtime']

# To visualize the distribution of runningtime using a histogram
sns.histplot(movie['runningtime'])

# To create a Kernel Density Estimate (KDE) plot for the runningtime column
# Tip. Kernel Density Estimation (KDE) refers to a method of estimating a continuous probability density function based on a kernel function and the data. 
# It is used to create a smooth curve that represents the distribution of data.

# Can visually represent the data distribution intuitively through a KDE plot
sns.kdeplot(movie['runningtime'])

# To compare the average values (e.g., running time or any other relevant metric) 
# for specific countries from one's list
movie['nation'].value_counts()
cond = movie['nation'].isin(['Korea', 'USA', 'Japan', 'UK', 'France', 'Hongkong', 'China', 'Canada', 'Germany', 'Spain', 'Italy'])
movie.loc[cond].groupby('nation')['runningtime'].mean().sort_values().plot(kind = 'barh')
movie.shape

# Service
# To load service.csv file and assign it to service variable
service = pd.read_csv('/path/service_revised.csv')

# To view the size of service DataFrame
service.shape

# To view top5 row
service.head()

# To visualize the distribution of the productcode column
service['productcode'].value_counts()

# Load Productcode sheet from column_code_info.xlsx then assign it to column_code
column_code = pd.read_excel('/path/column_code_info.xlsx', sheet_name = 'Productcode')
column_code.head()

# Merge service and column_code (When merging, merge left/right Productcode/productcode)
service.head(2)
column_code.head(2)

merged = pd.merge(service, column_code, left_on = 'productcode', right_on = 'Productcode', how = 'left').drop('Productcode', axis = 1) 
merged

# To visualize the distribution of the Productcode_name column
merged['Productcode_name'].value_counts()

# To visualize the distribution of the Productcode_name column
plt.figure(figsize=(12, 18)) 
sns.countplot(y='Productcode_name', data=merged) 
plt.show()

plt.figure(figsize=(12, 18))
sns.countplot(y='Productcode_name', data=merged, order=merged['Productcode_name'].value_counts().index) 
plt.show()

# To filter users with Basic plan
merged.loc[merged['Productcode_name'] == 'Basic']

# To view the distribution of devicetypeid for Basic plan users
merged.loc[merged['Productcode_name'] == 'Basic', 'devicetypeid'].value_counts()

# To filter for users with Productcode_name values of 'Basic', 'Standard', and 'Premium', 
# and then calculate the average pgamount for each combination of Productcode_name and gender, 
# followed by sorting the result in descending order
tmp = merged.loc[merged['Productcode_name'].isin(['Basic', 'Standard', 'Premium'])].groupby(['Productcode_name', 'gender'])[['pgamount']].mean() 
tmp.sort_values('pgamount', ascending = False)

# To create a pivot table where the values are the average of pgamount, 
# and store the resulting table in the variable tmp
# Tip. A pivot table is a statistical table that summarizes data from a large table 
# (e.g., databases, spreadsheets, or business intelligence programs).
tmp = merged.loc[merged['Productcode_name'].isin(['Basic', 'Standard', 'Premium'])].pivot_table(index ='gender', columns = 'Productcode_name', values = 'pgamount') 
tmp

# To visualize the tmp pivot table as a heatmap
# Tip. A heatmap is a data visualization technique that transforms data values into colors, allowing for visual analysis. 
# Through a heatmap, one can effectively reveal patterns from large datasets without needing to focus on specific numerical values.
sns.heatmap(tmp, annot = True, fmt='.1f', cmap='cividis')

# Predicting Repurchase Rate using machine learning
service['Repurchase'].value_counts()
service['Repurchase'].isnull().sum()
# Create a variable target, and assign True if Repurchase column is not missing(NaN) and False if it is missing
service.head()
service['target'] = service['Repurchase'].notnull() 
service['target'].value_counts()

# Change target variable's type to int type
service['target'] = service['target'].astype('int')
service['target'].value_counts()

# To replace all missing values (NaN) in a specific column (e.g., Repurchase) 
# or across the entire DataFrame with the value 'X'
service.head()
service = service.fillna('X')
service.head()

# To check the column information of the service DataFrame
service.columns

# Defining Feature(X)
features = [
# 'uno',
  'productcode',
  'pgamount',
  'chargetypeid',
  'concurrentwatchaccount',
  'promo_100',
  'coinReceived',
# 'Repurchase',
  'devicetypeid',
  'isauth',
  'gender',
  'agegroup',
# 'registerdat',
  'registerhour',
  # 'endday',
]

service[features].head()

# Defining X, Y
x = pd.get_dummies(service[features]) 
y = service['target']

x.head()

# To split the dataset
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, stratify=y, test_size=0.2, random_state=123)
  
# To create a machine learning model
# Tip: Machine learning refers to a technology that involves learning from empirical data to make predictions and improve performance over time. 
# It focuses on developing systems and algorithms that can perform these tasks autonomously.
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=123) 
model.fit(x_train, y_train)
pred = model.predict(x_test)

pred[:10]

y_test[:10].values

# To calculate the prediction accuracy of your machine learning model
from sklearn.metrics import accuracy_score 
accuracy_score(y_test, pred)

pd.DataFrame(list(zip(x_train.columns, model.feature_importances_)), columns=['feature', 'importance']).sort_values('importance', ascending=False)

# Improvement: Data preprocessing
# Tip: Data preprocessing refers to preliminary operations to separate, remove, and process unnecessary information from raw data so that it is suitable for the purpose and method of data analysis. 
# How one preprocess data can significantly impact the performance of a machine learning model.

# Preprocessing devicetypeid
service['devicetypeid'].value_counts()

def convert_device(x): 
  if x == 'pc':
    return 0
  elif x in ['android', 'ios', 'mobile']:
    return 1 
  else:
    return 2

service['devicetypeid'] = service['devicetypeid'].apply(convert_device) 
service['devicetypeid'].value_counts()

# Preprocessing productcode
service['productcode'].value_counts()[:10]

service['productcode'] = service['productcode'].apply(lambda x: x if x in ['pk_1487', 'pk_1488', 'pk_2025', 'pk_1508', 'pk_1480'] else 'other') 
service['productcode'].value_counts()

# Preprocessing chargetypeid
service['chargetypeid'].value_counts()[:10]

service['chargetypeid'] = service['chargetypeid'].apply(lambda x: 'other' if x in [170, 121, 160] else x) 
service['chargetypeid'].value_counts()

# To retrain the machine learning models after splitting the dataset and evaluating its performance improvement (from 64% to 68%)
x = pd.get_dummies(service[features]) 
y = service['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, stratify=y, test_size=0.2, random_state=123)

model = RandomForestClassifier(random_state=123, n_estimators=300, max_depth=5) 
model.fit(x_train, y_train)
pred = model.predict(x_test)

# To assess whether additional preprocessing improves the accuracy of the model
accuracy_score(y_test, pred)
