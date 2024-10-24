# Decision Trees
# An algorithm that uses a tree structure to represent patterns in the data as a combination of predictable rules
  # It is similar to the game of twenty questions
  # Decision trees can be used for both classification (categorical labels) and regression (continuous labels)
#The algorithm generates rules by recursively splitting the regions of each variable in the dataset. 
# The rules are expressed in an if-else format
# In classification, the tree splits the feature space in a way that maximizes information homogeneity (the degree to which the information contained in the classified sets is similar)
  # Information Homogeneity: Methods to measure information homogeneity include entropy and Gini impurity
# In regression, the tree splits the data to minimize the sum of squared residuals
# After partitioning the regions, the learning process aims to maximize the purity of each region while minimizing impurity or uncertainty

# Gini impurity
# The impurity of a given dataset (the smaller the value, the more homogeneous the data)
  # As it approaches 0, the data is more uniform, and as it approaches 1, it becomes more unequal

# Entropy
# The congestion of a given dataset (the smaller the value, the more homogeneous the data)

# Decision Tree classification practice
# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns

from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier

# Import classification data
df = pd.read_csv('/path/breast_cancer.csv') 
df

# Query the count and data type for each column
df.info()

# Split data
X = df.iloc[:, :-1] 
Y = df.iloc[:, -1] 
X.head()

# Y is categorical > Use a classification model
Y

# Check the category ratios using
pd.value_counts(Y, normalize=True)

# Split data for training and testing
# Apply stratified sampling
x_train, x_test, y_train, y_test = train_test_split(X, Y, stratify=Y, random_state=0)

# Check the results of the split
pd.value_counts(y_train, normalize=True)

# Check the results of the split
pd.value_counts(y_test, normalize=True)

# Model creation
model = DecisionTreeClassifier()

# Model training
model.fit(x_train, y_train) # Only use training data

# DecisionTreeClassifier
# DecisionTreeClassifier()

# Model evaluation (accuracy)
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Model prediction
p_test = model.predict(x_test) # Predict for test data
p_test

# Calculate classification_report
from sklearn.metrics import classification_report 
print(classification_report(y_test, p_test))

# Adjust maximum depth
model = DecisionTreeClassifier(max_depth=3) model.fit(x_train, y_train)
print('train_data_performance :', model.score(x_train, y_train))
print('test_data_performance :', model.score(x_test, y_test))

# Query feature importances
model.feature_importances_

# Visualise feature importances
fi = pd.Series(model.feature_importances_, index=model.feature_names_in_) 
fi[fi != 0].sort_values().plot(kind='barh')
