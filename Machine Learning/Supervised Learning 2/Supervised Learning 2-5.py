# Ensemble
# A technique that combines multiple machine learning models to create a more powerful model, similar to aggregating the opinions of several experts to make predictions (collective intelligence)

# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns
from sklearn.model_selection import train_test_split

# Import classification data
df = pd.read_csv('/path/breast_cancer.csv')
df

# Split data
X = df.iloc[:, :-1] 
Y = df.iloc[:, -1] 
X.head()

# Y is categorical > Use a classification model
Y

# Split the data into training and test sets
# Apply stratified sampling
x_train, x_test, y_train, y_test = train_test_split(X, Y, stratify=Y, random_state=0)

# Voting
# Combine different algorithms by using multiple models, 
# where the final decision is made through voting based on the predictions of each model

# Create classifiers to participate in the voting process
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier

knc = KNeighborsClassifier() lr = LogisticRegression()
dtc = DecisionTreeClassifier()

# Create a hard voting classification model
from sklearn.ensemble import VotingClassifier 
hard = VotingClassifier(
    [('knn', knc), ('lr', lr), ('dtc', dtc)],
voting='hard' 
)

# Model training
hard.fit(x_train, y_train) # Only use train data

# Model evaluation (accuracy)
print('train_data_performance :', hard.score(x_train, y_train)) 
print('test_data_performance :', hard.score(x_test, y_test))

# Model prediction
p_test = hard.predict(x_test) # Predict for test data
p_test

# Calculate classification_report
from sklearn.metrics import classification_report 
print(classification_report(y_test, p_test))

# Create a soft voting classification model
from sklearn.ensemble import VotingClassifier soft = VotingClassifier(
    [('knn', knc), ('lr', lr), ('dtc', dtc)],
voting='soft' 
)

# Model training
soft.fit(x_train, y_train) # Only use train data

# Model evaluation (accuracy)
print('train_data_performance :', soft.score(x_train, y_train)) 
print('test_data_performance :', soft.score(x_test, y_test))

# Model prediction
p_test = soft.predict(x_test) # Predict for test data
p_test

# Calculate classification_report
from sklearn.metrics import classification_report 
print(classification_report(y_test, p_test))

# Bagging (Bootstrap Aggregating)
# Combines the same algorithm using different training datasets 
# Samples are drawn multiple times (Bootstrap), and the results from each model are aggregated (Aggregation)

# Create RandomForest classification model
from sklearn.ensemble import RandomForestClassifier 
rfc = RandomForestClassifier()

# Model training
rfc.fit(x_train, y_train) # Only use train data

# RandomForestClassifier
# RandomForestClassifier()

# Model evaluation (accuracy)
print('train_data_performance :', rfc.score(x_train, y_train)) 
print('test_data_performance :', rfc.score(x_test, y_test))

# Model prediction
p_test = rfc.predict(x_test) # Predict for test data
p_test

# Calculate classification_report
from sklearn.metrics import classification_report 
print(classification_report(y_test, p_test))

# Increase the number of classifiers
rfc = RandomForestClassifier(n_estimators=1000)

# Model training
rfc.fit(x_train, y_train) # Only use train data

# RandomForestClassifier
# RandomForestClassifier(n_estimators=1000)

# Model evaluation (accuracy)
print('train_data_performance :', rfc.score(x_train, y_train)) 
print('test_data_performance :', rfc.score(x_test, y_test))

# Boosting
# Multiple models are trained sequentially
# The next model is given weights based on the results of the previous model

# Create GradientBoosting classification model
from sklearn.ensemble import GradientBoostingClassifier 
gbc = GradientBoostingClassifier()

# Model training
gbc.fit(x_train, y_train) # Only use training data

# GradientBoostingClassifier
# GradientBoostingClassifier()

# Model evaluation (accuracy)
print('train_data_performance :', gbc.score(x_train, y_train)) 
print('test_data_performance :', gbc.score(x_test, y_test))

# Model prediction
p_test = rfc.predict(x_test) # Predict for test data
p_test

# Calculate classification_report
from sklearn.metrics import classification_report 
print(classification_report(y_test, p_test))

