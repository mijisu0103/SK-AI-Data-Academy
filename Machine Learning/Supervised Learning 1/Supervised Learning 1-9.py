# The wafer pass/fail classification 
  # -1 representing pass and 1 representing fail
  # The data's timestamp refers to a specific test point

# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# Reading and querying data
  # Read uci-secom.csv file in /path directory
  # Query top5 sample (rows)
data = pd.read_csv('/path/uci-secom.csv')
data.head()

# Calculate the count for each value in the Pass/Fail column
data['Pass/Fail'].value_counts()

# Handling missing value
# Print the number of missing values for each column
data.isna().sum()

# Visualize the distribution of the calculated number of missing values for each column
plt.hist(data.isna().sum()) 
plt.show()

# Calculate the descriptive statistics for the result of the number of missing values per column
data.isna().sum().describe()

# Print the total number of missing (NA) values
data.isna().sum().sum()

# Print the DataFrame information and check the data count and data type for each column
  # Set verbose=True and show_counts=True
data.info(verbose=True, show_counts=True)

# After filling the missing values with 0, print the total number of missing values
data=data.fillna(0) 
data.isna().sum().sum()

# Additional data processing
  # Delete the unnecessary 'Time' column and then check the shape of the DataFrame
data = data.drop('Time', axis=1) 
data.shape

# ML
  # Extract X and Y for training:
  # Y is the 'Pass/Fail' column, X is all columns except 'Pass/Fail'
x=data.iloc[:, :-1] 
y=data.iloc[:, -1] 
print("shape of x:", x.shape) 
print("shape of y:", y.shape)

# Apply Standard Scaling (standardization) to the X data
from sklearn.preprocessing import StandardScaler 
x_scaled = StandardScaler().fit_transform(x)

# Split the standardized X data into train and test sets
# with a ratio of 8:2 (test_size=0.2)
# Set stratified sampling by using stratify=y

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_scaled, y, test_size = 0.2, random_state=0, stratify = y)

print("shape of x_train:", X_train.shape) 
print("shape of x_test:", X_test.shape) 
print("shape of y_train:", y_train.shape) 
print("shape of x_train:", y_test.shape)

# Apply the logistic regression algorithm and print the score
# Set max_iter=1000
from sklearn.linear_model import LogisticRegression
lg = LogisticRegression(max_iter=1000).fit(X_train,y_train)
print('train : {:.3f}, test : {:.3f}' .format(lg.score(X_train, y_train), lg.score(X_test, y_test)))

# Using the trained model, predict the results for the x_test data and print the output
y_pred = lg.predict(X_test) 
print("y_pred", y_pred)

# Print the classification report for the predictions made on the x_test data
from sklearn.metrics import classification_report 
print(classification_report(y_test, y_pred))


