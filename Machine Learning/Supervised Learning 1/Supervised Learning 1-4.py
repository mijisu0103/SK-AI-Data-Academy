# Predict Energy Efficiency
# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns

# Read and view data
  # Read ENB2012_data.xlsx file in /path directory
  # View top 5 sample (rows)
df = pd.read_excel('/path/ENB2012_data.xlsx') 
df.head()

# Check the number of samples and features (shape)
df.shape

# Rename the columns of df by referring to the column names below
# ['relative_compactness', 'surface_area', 'wall_area', 'roof_area', 'overall_height', 'orientation', 'glazing_area', 'glazing_area_distribution', 'heating_load', 'cooling_load']
df.columns = ['relative_compactness', 'surface_area', 'wall_area', 'roof_area', 'overall_height', 'orientation', 'glazing_area', 'glazing_area_distribution', 'heating_load', 'cooling_load']
df

# Retrieve the information
df.info()

# Handling missing values
# Retrieve the missing values
df.isna().sum()

# Data Analysis
# Display the histogram using df.hist(). 
# Apply the options figsize=(15,15) and bins=5 to the histogram
df.hist(figsize=(15,15), bins=5) 
plt.show()

# To check for outliers in each column, draw a boxplo
df.plot(kind='box', figsize=(16,12)) 
plt.show()

df.plot(kind='box', figsize=(15,10), subplots=True, layout=(3, 4)) 
plt.show()

# To print the correlation between each column 
# and round the values to three decimal places
df.corr().round(3)

# To visualize the correlation between columns as a heatmap, 
# with a "Greens" colormap and values rounded to two decimal places
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(), cmap='Greens', annot=True, fmt='.2f') 
plt.show()

# Feature Engineering
# Create a new column load, which is the sum of the dependent variables heating load and cooling load
df['load'] = df['heating_load'] + df['cooling_load'] 
df

# Check if there are any columns with a variance (or standard deviation) of 0
df.var()

# Check for features with a correlation of 0.97 or higher 
# Print the correlation between relative_compactness and surface_area to three decimal places
np.round(df.corr()[['relative_compactness', 'surface_area']], 3)

# Calculate and print the correlation between roof_area and overall_height, 
# rounded to three decimal places
np.round(df.corr()[['roof_area', 'overall_height']], 3)

# Visualize the changes in load according to surface_area using a line plot 
# Differentiate by overall_height
  # sns.lineplot(x= , y=, data=df)
sns.lineplot(x='surface_area', y='load', hue='overall_height', data=df) 
plt.show()

# Visualize the sample counts for each overall_height using a countplot
  # sns.countplot(x= , data=df)
sns.countplot(x='overall_height', data=df) 
plt.show()

# visualize the average load for each overall_height using a bar plot
  # sns.barplot(x= , y= , data=df)
sns.barplot(x='overall_height', y='load', data=df) 
plt.show()

# Select the columns to be used for training
# Y = load column
# X = The rest of columns except: load, heating_load, cooling_load, relative_compactness, roof_area
# Excluded features should be commented out

features = [
  #'relative_compactness',
  'surface_area',
  'wall_area',
  #'roof_area', 
  'overall_height', 
  #'orientation', 
  'glazing_area', 
  'glazing_area_distribution',
]

# Split X and Y
X = df[features] 
Y = df['load']

# Print the top 5 rows of X and its shape
display(Y.head()) 
Y.shape

# Splitting data
  # Split the data into training and evaluation datasets. 
  # The split ratio is 75:25, 
  # and set random_state=0
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state = 0)

# Print the shape of the split data
print('X Train Shape : ', x_train.shape) 
print('X Test Shape : ', x_test.shape) 
print('Y Train Shape : ', y_train.shape) 
print('Y Test Shape : ', y_test.shape)

# Creating a model and training
  # Train a model using LinearRegression, then print the R-squared metric for both the training and evaluation datasets
  # Model the split data using LinearRegression and print the R-squared values
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)
model.score(x_train, y_train), model.score(x_test, y_test)

# Print the regression coefficients and the intercept of the trained model
model.coef_, model.intercept_

# Model prediction and evaluation
  # Print the prediction results for the entire X dataset
pred = model.predict(X) 
pred

# Add the prediction results as a new column load_pred to the DataFrame df
df['load_pred'] = pred 
df

# Print the R-squared, MSE, and MAE for the actual and predicted heating/cooling load
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
print('Load')
print('R squared : ', r2_score(df['load'], df['load_pred']))
print('Mean Squared Error: ', mean_squared_error(df['load'], df['load_pred'])) 
print('Mean Absolute Error: ', mean_absolute_error(df['load'], df['load_pred']))

