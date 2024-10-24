# Regularization
  # As the degree increases in polynomial regression, overfitting can occur, leading to a decrease in predictive performance
  # To prevent overfitting, the size of the weights is controlled
  # By adding a regularization (penalty) term to the existing cost function, the size of the weights can be controlled
  # One can use regularization models implemented in scikit-learn's linear_model, such as Ridge, Lasso, and ElasticNet
  # Regularization strength (Alpha):
    # If Alpha is set too small or to 0, regularization on the weights weakens, leading to overfitting
    # If Alpha is set too large, the regularization on the weights becomes too strong, making the model too simple and resulting in underfitting

# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns

from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression

# Import regression data
df = pd.read_csv('/path/diabetes.csv')
df

# Splitting data
X = df.iloc[:, :-1] 
Y = df.iloc[:, -1] 
X.head()

# Apply polynomial transformation
P = PolynomialFeatures(degree=3, include_bias=False) 
X_Poly = P.fit_transform(X)
X.shape, X_Poly.shape

# Split data for training and testing
x_train, x_test, y_train, y_test = train_test_split(X_Poly, Y, random_state=0)

# Model creation
model = LinearRegression()

# Model training
model.fit(x_train, y_train) # Only use train data

# LinearRegression
# LinearRegression()

# Model evaluation (R Squared)
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Ridge
  # A model with a regularization term (L2 Regularization) applied to the existing linear regression equation 
  # seeks to find appropriate weights and biases that minimize the sum of the squares of the weights, while also minimizing the mean squared error (MSE)
  # Due to the effect of L2 regularization, the weights do not become exactly zero, but it helps control the complexity of the model
  # The influence of features on the output decreases (making the model less dependent on the current features)

# Creating a regularization model
from sklearn.linear_model import Ridge 
model = Ridge(alpha=1)

# Training model
model.fit(x_train, y_train) # Only use train data

# Ridge
# Ridge(alpha=1)

# Model evaluation (R Squared)
print('train_data_performace) :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Relaxing regularization strength
model = Ridge(alpha=0.1)
model.fit(x_train, y_train)
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Lasso
# A model with a regularization term (L1 Regularization) applied to the existing linear regression equation 
# seeks to find appropriate weights and biases that minimize the sum of the absolute values of the weights, while also minimizing the mean squared error (MSE)
# Due to the effect of L1 regularization, some features become zero and are not used in the model
  # It has a feature selection effect, 
# helping to identify the most important features in the model, thereby improving the interpretability of the model

# Creating a regulization model
from sklearn.linear_model import Lasso 
model = Lasso(alpha=1)

# Training model
model.fit(x_train, y_train) # Only use train data

# Lasso
# Lasso(alpha=1)

# Model evaluation (R Squared)
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Querying the number of coefficients used
print('all_coefficients :', len(model.coef_))
print('used_coefficients : ', len(model.coef_[model.coef_ != 0]))

# Relaxing regularization strength
model = Lasso(alpha=0.1)
model.fit(x_train, y_train)
print('train_data_performance :', model.score(x_train, y_train)) 
print('train_data_performance :', model.score(x_test, y_test))

# Querying the number of coefficients used
print('all_coefficients :', len(model.coef_))
print('used_coefficients : ', len(model.coef_[model.coef_ != 0]))

