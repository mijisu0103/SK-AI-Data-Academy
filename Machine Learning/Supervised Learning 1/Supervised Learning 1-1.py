# K-Nearest Neighbor
"""
A method of predicting new data by using the information of the K nearest neighbors ranked by distance
  For regression problems, predictions are made using the average value of the dependent variable
  For classification problems, predictions are made using the majority category of the dependent variable
  
KNN's results can vary greatly depending on the distance measurement method used
  There are various methods to calculate distances, with the Euclidean Distance being the most commonly used.
KNN is not heavily affected by outliers in the training data, and it is an effective algorithm if there is a large amount of training data 
  because it only uses the nearest K neighbors
However, a downside is that it can take a long time to compute when there is a large amount of data, 
  as it calculates the distance between all the reference data and the prediction data
"""

# K-Nearest Neighbor exercise (Classification)
# Setting environment
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns

from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier   # Classification model
from sklearn.neighbors import KNeighborsRegressor  # Regression model

# Import classification data
df = pd.read_csv('/path/iris.csv')
df

# Checking for missing values by column
df.isna().sum()

# Check datatype by column
df.dtypes

# Checking the data count and type for each column
df.info()

# Split data
X = df.iloc[:, :-1] 
Y = df.iloc[:, -1] 
X.head()

Y # For categorical data, a classification model is used

# Split data for train and test
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0)

# Create a model
model = KNeighborsClassifier(n_neighbors=5) # set nearest neighbors to 5

# Train model
model.fit(x_train, y_train) # Only use train data

# KNeighborsClassifier
# KNeighborsClassifier()

# Assess model
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Model prediction
p_test = model.predict(x_test) # Predict test data
p_test

# Calculate classification_report
from sklearn.metrics import classification_report 
print(classification_report(y_test, p_test))

# K-Nearest Neighbors exercise (Regression)
# Import regression data
df = pd.read_csv('/path/boston.csv') 
df

# Check missing values by column
df.isna().sum()

# Check datatype by column
df.dtypes

# # Checking the data count and type for each column
df.info()

# Handling missing values
df['ZN'].fillna(0, inplace=True) 
df['CHAS'].fillna(0, inplace=True)

# Split data
features = [
    'CRIM',
    'ZN',
    'INDUS',
    'CHAS',
    'NOX',
    'RM',
    'AGE',
    'DIS',
    'RAD',
    'TAX',
    'PTRATIO',
    'B',
    'LSTAT',
]
X = df[features] 
Y = df['target'] 
X.head()

Y # For continuous data, a regression model is used

# Split data for train and test
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0)

# Create a model
model = KNeighborsRegressor(n_neighbors=5) # Set nearest neighbor as 5

# Train model
model.fit(x_train, y_train) # Only use train data

# KNeighborsRegressor
# KNeighborsRegressor()

# Assess model
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Predict model
p_test = model.predict(x_test) # predict test data
p_test

# Calculate rmse
from sklearn.metrics import mean_squared_error 
mean_squared_error(y_test, p_test, squared=False)

# Optimizing K-Nearest Neighbors (KNN)
"""
In the K-Nearest Neighbor (KNN) model, the number of nearest neighbors (K) is the most important hyperparameter
There is no predefined statistical or mathematical method to find the best K value
To find the K value that provides the best model performance, we typically use experimentation by changing the number of nearest neighbors in a loop
You can also use hyperparameter tuning tools like GridSearch, RandomSearch, or Optuna to find the best hyperparameters
"""

K_RANGE = range(1, 101) # Set a range to use for experiment

TRAIN_SCORE = [] # Save train data performance
TEST_SCORE = [] # Save test data performance

for K in K_RANGE:
  model=KNeighborsRegressor(n_neighbors=K) # Create model while changing K value
  model.fit(x_train, y_train) # Train model
  
  TRAIN_SCORE.append(model.score(x_train, y_train)) # Train data performance
  TEST_SCORE.append(model.score(x_test, y_test)) # Test data performance

# Visualise experiment result
plt.plot(K_RANGE, TRAIN_SCORE, label='Train R2') 
plt.plot(K_RANGE, TEST_SCORE, label='Test R2')

