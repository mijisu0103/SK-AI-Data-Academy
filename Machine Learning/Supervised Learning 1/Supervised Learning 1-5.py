# Polynomial Regression
  # If the relationship between a continuous label and features is not linear, it cannot be expressed as a first-degree equation, so it is transformed into a polynomial of degree 2 or higher for regression analysis
  # New features are added by applying polynomial transformations to the original features
  # In scikit-learn, PolynomialFeatures can be used to easily add polynomial transformations and interaction terms

# Data creation for polynomial transformation
import pandas as pd
X = pd.DataFrame({
    'X':[1, 2, 3, 4, 5]
})

# Apply polynomial transformation (second-degree terms)
from sklearn.preprocessing import PolynomialFeatures
P = PolynomialFeatures(degree=2)
X_POLY = pd.DataFrame(P.fit_transform(X), columns=P.get_feature_names_out()) X_POLY

# Data creation for polynomial transformation
import pandas as pd
X = pd.DataFrame({
    'X0':[1, 2, 3, 4, 5],
    'X1':[6, 7, 8, 9, 10]
})
X

P = PolynomialFeatures(degree=2)
X_POLY = pd.DataFrame(P.fit_transform(X), columns=P.get_feature_names_out()) 
X_POLY

# Applying polynomial regression
# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression

# Import regression data
df = pd.read_csv('/path/diabetes.csv') 
df

# Split data
X = df.iloc[:, :-1] 
Y = df.iloc[:, -1] 
X.head()

# Apply polynomial transformation
P = PolynomialFeatures(degree=2, include_bias=False) 
X_Poly = P.fit_transform(X)
X.shape, X_Poly.shape

# Split data for training and testing
x_train, x_test, y_train, y_test = train_test_split(X_Poly, Y, random_state=0)

# Model creation
model = LinearRegression()

# Model training
model.fit(x_train, y_train) # Only use data for train data

# LinearRegression
# LinearRegression()

# Model evaluation (R Squared)
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Model prediction
p_test = model.predict(x_test) # Predict only for test data
p_test

# Calculate rmse
from sklearn.metrics import mean_squared_error 
mean_squared_error(y_test, p_test, squared=False)

# Model's performance before polynomial transformation
  # train_data_performance: 0.5554371489353019
  # test_data_performance: 0.35940090989715556

# Model's performance after polynomial transformation
  # train_data_performance: 0.6468753420284549
  # test_data_performance: 0.24413674792366735

