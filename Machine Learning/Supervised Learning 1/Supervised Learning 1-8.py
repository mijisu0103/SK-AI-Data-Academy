# Odds
# The ratio of the probability of success to the probability of failure
  # If the odds are 3, it means that the probability of success is three times the probability of failure

# If A wins 1 time and loses 6 times
1/6

# If A wins 6 times and loses 1 time
6/1

# Logit transformation
  # Logit: The value obtained by applying the logarithm to the odds
  # Logit transformation: The process of transforming the odds by applying a logarithm
  # Since odds are not symmetric, applying a log transformation creates symmetry
import numpy as np 
np.log(1/6)

np.log(6/1)


# Logistic Regression
# Unlike linear regression analysis, it is a model used when the label to be predicted is categorical
# The logistic regression model is based on a linear regression model but approaches it as a probabilistic model
# Except for the fact that the label to be predicted represents probability, the logistic regression model has the same general form as a simple linear regression model
#   In order for the label's value to be a probability (between 0 and 1), the odds and log are applied to the existing regression equation
#     Since the range of values in the original regression model does not match the range of probability values, the odds and log are applied
# A function that returns values between 0 and 1 is called a logistic function, 
#   and the sigmoid function is a representative example of a logistic function
# The logistic regression model is primarily used for binary classification
#   For multinomial classification, multiple models are used

# Logistic Regression Practice
# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression

# Import classification data
df = pd.read_csv('/path/breast_cancer.csv') 
df

# Query the count and data type of each column
df.info()

# Check the distribution of each column
df.hist(figsize=(15, 15)) 
plt.show()

# Check for outliers in each column
df.plot(kind='box', figsize=(15, 15), subplots=True, layout=(6, 6)) 
plt.show()

# Splitting data
X = df.iloc[:, :-1] 
Y = df.iloc[:, -1] 
X.head()

# Y is categorical > Use a classification model
Y

# Check the ratio of categories
pd.value_counts(Y, normalize=True)

# Split the data into training and test sets
  # Apply stratified splitting
x_train, x_test, y_train, y_test = train_test_split(X, Y, stratify=Y, random_state=0)

# Check the result of the split
pd.value_counts(y_train, normalize=True)

# Model Creation
model = LogisticRegression()

# Model Training
model.fit(x_train, y_train) # Only use train data

# LogisticRegression
# LogisticRegression()

# Model evaluation (accuracy)
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Model prediction
p_test = model.predict(x_test) # Predict only for test data
p_test

# Calculate classification_report
from sklearn.metrics import classification_report 
print(classification_report(y_test, p_test))

# Increase the maximum number of iterations
model = LogisticRegression(max_iter=10000) model.fit(x_train, y_train)
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Check the model coefficients
pd.Series(model.coef_[0], index=x_train.columns).sort_values()

# Check the shape of the model coefficients
model.coef_.shape

# Classification data (multinomial classification)
df = pd.read_csv('/path/digits.csv') 
df

# Data visualisation
plt.imshow(df.iloc[0, :-1].values.reshape(8, 8))

# Split data
X = df.iloc[:, :-1] 
Y = df.iloc[:, -1] 
X.head()

# Y is categorical > Use a classification model
Y

# Check the ratio of categories
pd.value_counts(Y, normalize=True)

# Split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0)

# Model creation
model = LogisticRegression()

# Model training
model.fit(x_train, y_train) # Only use train data

# LogisticRegression
# LogisticRegression()

# Model evaluation (accuracy)
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Check the shape of the model coefficients
model.coef_.shape

# Retrieve the model coefficients for the first category
pd.Series(model.coef_[0], index=x_train.columns).sort_values()

