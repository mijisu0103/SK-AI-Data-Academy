# California area house price prediction
# Data structure and type

# Variable                       Definition                              Type
""" 
  longitude                        Longitude                          Continuous
  latitude                         Latitude                           Continuous
  housingmedianage       Median age of houses in area                 Continuous
  total_rooms          Avg No. of rooms of houses in area             Continuous
  total_bedrooms       Avg No. of bedrooms of houses in area          Continuous
  population                  No. of people in area                   Continuous
  households                No. of households in area                 Continuous
  median_income            Median income of household                 Continuous
  medianhousevalue       Median value of houses in area               Continuous
  ocean_proximity              Proximity to ocean                     Continuous
"""

# Setting
!pip install folium

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium as folium
from folium import plugins
from folium.plugins import HeatMap
from pandas.plotting import scatter_matrix import warnings warnings.filterwarnings('ignore')

# Reading and querying data
# Read /path/housing.csv and save it in df
df = pd.read_csv('/path/housing.csv') 
df

# Query top20 in dataframe
df.head(20)

# Check dataframe's shape
df.shape

# Check information in dataframe
df.info()

# Query the number of missing values in each column
df.isna().sum()

# Check the percentage of missing values for each column
# ratio = missing value / all data
df.isna().mean()

# Check row information that has missing values
df[df['total_bedrooms'].isna()]

#Visualize the location of missing values using the isna() function, 
# applying a colormap of cmap='gray'
plt.figure(figsize=(15,15))
sns.heatmap(df.isna(), cmap='gray')

# Visualize the median_house_value column using the sns.histplot function 
# with kde=True and bins=40
sns.histplot(df['median_house_value'], kde=True, bins=40)

# Retrieve the statistical summary information for the median_house_value column
df['median_house_value'].describe()

# Replace the missing values in total_bedrooms with the median value
df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())
df

# Check for the presence of missing values
df.isna().sum()

# Check the number of unique values for each column using the nunique function
df.nunique()

# Use the DataFrame's hist function to check the distribution of each column
# Apply bins=50 and figsize=(20, 15) 
df.hist(bins=50, figsize=(20,15))
plt.show()

# Create two lists:
  # continuous: A list containing the names of columns with continuous data types
  # categorical: A list containing the names of columns with categorical data types
continuous = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
'median_house_value']
categorical = ['ocean_proximity']

# Calculate the count for each category in the categorical column ocean_proximity
df['ocean_proximity'].value_counts()

# Calculate the ratio for each category in the categorical column ocean_proximity
df['ocean_proximity'].value_counts(normalize=True)

# Visualize the results as a bar plot
df['ocean_proximity'].value_counts(normalize=True).plot(kind='bar')

# Modify the values in the ocean_proximity column, 
# changing <1H OCEAN to 1H OCEAN by removing the < symbol
df['ocean_proximity'] = df['ocean_proximity'].str.replace('<', '') 
df.loc[df['ocean_proximity'] == '<1H OCEAN', 'ocean_proximity'] = '1H OCEAN'

# Recalculate the ratio for each category in the categorical column ocean_proximity
df['ocean_proximity'].value_counts(normalize=True)

# Use scatter_matrix to examine the relationships between columns and the density of each column
scatter_matrix(df, figsize = (25,25), alpha=0.9, diagonal="kde", marker="o");

# Use folium to visualize the data on an actual map
california_map = folium.Map(location=[36.7783,-119.4179], zoom_start = 6, min_zoom=5) df_map = df[['latitude', 'longitude']]
data = [[row['latitude'],row['longitude']] for index, row in df_map.iterrows()]
_ = HeatMap(data, radius=10).add_to(california_map)
california_map
# The closer the color is to red, the more data is present

# Extract the longitude and latitude columns from the DataFrame and store them in X, 
# while extracting the median_house_value column and storing it in Y
X = df[['longitude','latitude']]
Y = df['median_house_value']

# Use DecisionTreeRegressor to train on X and Y
from sklearn.tree import DecisionTreeRegressor 
model = DecisionTreeRegressor().fit(X, Y)

# Use the plot_tree function to visualize the decision tree graph
from sklearn.tree import plot_tree
plt.figure(figsize=(10,10), dpi=150)
plot_tree(model, max_depth=2,feature_names=df.columns, impurity=False, filled=True) 
plt.show()

# Create a scatter plot with the longitude column as the x-axis and the latitude column as the y-axis
# Set the color (c) to DarkBlue and the size of the points (s) to 1.5
plt.figure(figsize=[6,4], dpi=120) 
plt.scatter(x=df["longitude"],y=df["latitude"], c='DarkBlue', s=1.5)

# Examine how much "location" influences house prices
plt.figure(figsize=[6,4], dpi=120) 
plt.scatter(x=df["longitude"],y=df["latitude"],c=df["median_house_value"], s=1.5)
splits = model.tree_.threshold[:2]
plt.plot([-125,-114],[splits[0],splits[0]], c='red') 
plt.plot([splits[1],splits[1]],[32,splits[0]], c='red')
# plt.ylim(32,42)
# plt.xlim(-125,-114)
plt.ylabel("Latitude")
plt.xlabel("Longitude")
plt.title("Median House Value")
plt.colorbar()
plt.show()

# Split X and Y into training and test sets, 
# setting random_state to 0
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0)

# Train and evaluate the model using the Decision Tree algorithm
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor().fit(x_train, y_train)
model.score(x_train, y_train), model.score(x_test, y_test)

# Calculate the MSE, MAE, and RMSE errors for the test data
from sklearn.metrics import mean_absolute_error, mean_squared_error 
p_test = model.predict(x_test)
print('MAE :',mean_absolute_error(y_test, p_test))
print('MSE :',mean_squared_error(y_test, p_test))
print('RMSE :',np.sqrt(mean_squared_error(y_test, p_test)))

# Use subplot and sns.histplot to check the distribution of the continuous columns
plt.figure(figsize=(15, 15))
for index, col_name in enumerate(continuous):
  plt.subplot(3,3,index+1)  
  sns.histplot(df[col_name])

# Apply log transformation to the following columns
# total_rooms, total_bedrooms, population, households, median_income, median_house_value
target_col = 'total_rooms, total_bedrooms, population, households, median_income, median_house_value'.split(', ') 
for col_name in target_col:
  df[col_name] = np.log1p(df[col_name])

# Use subplot and sns.histplot to recheck the distribution of the continuous columns after the log transformation
plt.figure(figsize=(15, 15))
for index, col_name in enumerate(continuous):
  plt.subplot(3,3,index+1) 
  sns.histplot(df[col_name])

# Extract only the continuous columns and save them to df_continuous 
# using the copy function
df_continuous = df[continuous].copy() 
df_continuous

# Standardize the df_continuous DataFrame
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler()
X_Scaled = scaler.fit_transform(df_continuous)

# Assign the standardized results back to the df DataFrame
df.loc[:, continuous] = X_Scaled

# Apply One-Hot encoding to the categorical columns using the get_dummies function
df = pd.get_dummies(df) 
df

# Save all columns except for median_house_value into the variable X
X = df.loc[:, df.columns != 'median_house_value'] 
X

# Save the median_house_value column into the variable Y
Y = df.loc[:, 'median_house_value'] 
Y

# Split X and Y into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, Y)

# Train and evaluate the model using the DecisionTreeRegressor
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor().fit(x_train, y_train) 
model.score(x_train, y_train), model.score(x_test, y_test)

# Calculate the MSE, MAE, and RMSE errors for the test data
p_test = model.predict(x_test)
print('MAE :',mean_absolute_error(y_test, p_test)) 
print('MSE :',mean_squared_error(y_test, p_test)) 
print('RMSE :',np.sqrt(mean_squared_error(y_test, p_test)))

