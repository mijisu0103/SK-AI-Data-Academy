# Heart disease prediction
  # indicates no disease, while 1 indicates the presence of disease

# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# Reading and querying data
# Read heart.csv file in /path directory
# Query top5 sample (rows)

data = pd.read_csv('/path/heart.csv') 
data.head()

# Calculate the count for each value in the target column
data['target'].value_counts()

# Handling missing values
# Print the number of missing values for each column
data.isna().sum()

# Print the DataFrame information 
  # and check the data count and data type for each column
data.info()

# ML
# Extract X and Y for training:
#   Y is the 'target' column
#   X is all columns except 'target'

x=data.iloc[:, :-1] 
y=data.iloc[:, -1]
print("shape of x:" , x.shape) 
print("shape of y:", y.shape)

# Apply Standard Scaling (standardization) to the X data
from sklearn.preprocessing import StandardScaler 
x_scaled = StandardScaler().fit_transform(x)

# Split the standardized X data into training and test sets 
# with a ratio of 8:2 (test_size=0.2)
# Set stratified sampling using stratify=y

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_scaled, y, test_size = 0.2, random_state=0, stratify=y)

print("shape of x_train:", X_train.shape) 
print("shape of x_test:", X_test.shape) 
print("shape of y_train:", y_train.shape) 
print("shape of y_test:", y_train.shape)

# Apply the SVM classification algorithm and print the score
from sklearn.svm import SVC
svm = SVC().fit(X_train, y_train)
print("train: {:.3f}, test: {:.3f}" .format(svm.score(X_train, y_train), svm.score(X_test, y_test)))

# Print support vector
svm.support_vectors_

# Use the trained model to predict results for the x_test data and print the output
y_pred = svm.predict(X_test) 
print("y_pred", y_pred)

# Print the classification report for the predictions made on the x_test data
from sklearn.metrics import classification_report 
print(classification_report(y_test, y_pred))

