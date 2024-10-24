# Boston area house price prediction
# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# Reading and querying the data
  # Read boston.csv file in /path directory
  # Query top5 sample (rows)
df = pd.read_csv('/path/boston.csv') df.head()

# Data preprocessing
  # Query the number of missing values by column
df.isna().sum()

# Replace missing values to 0
  # ZN: The proportion of residential land zoned for lots over 25,000 square feet
  # CHAS: Charles River adjacency (whether the property is adjacent to the Charles River or not)
df['ZN'] = df['ZN'].fillna(0) 
df['CHAS'] = df['CHAS'].fillna(0)

# The "Unnamed: 0" column is unnecessary
  # Remove it as it is identical to the index
df.drop('Unnamed: 0', axis=1, inplace=True) 
df

# Separate X and Y.
  # X: All columns except the "target" column
  # Y: The "target" column
X=df.loc[:, 'CRIM': 'LSTAT'] 
Y=df['target']

# Print split X
X

# Print split Y
Y

# Split the separated X and Y into train and test sets, 
  # with random_state set to 0
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state = 0)

# Train the model using LinearRegression and print the results
  # Print the R Squared values for both the training data and the evaluation data
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)
model.score(x_train, y_train), model.score(x_test, y_test)

# Apply standardization using StandardScaler and perform partial transformation
from sklearn.preprocessing import StandardScaler scaler = StandardScaler()
scaler.fit(x_train)
x_train_sc = scaler.transform(x_train)
x_test_sc = scaler.transform(x_test)

# Train the model using the standardized data and print the results
model = LinearRegression().fit(x_train_sc, y_train) 
model.score(x_train_sc, y_train), model.score(x_test_sc, y_test)

# Print the coefficients of the trained model
pd.Series(model.coef_, index=X.columns).sort_values()

# Execute the following code to perform residual analysis
  # If the red solid line significantly deviates from the dashed line, it means that the residuals vary greatly depending on the predicted values, indicating non-linearity
  # If an error occurs saying that the statsmodels module is missing, install the statsmodels module
  !pip install statsmodels

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)
model.score(x_train, y_train), model.score(x_test, y_test)

p_test = model.predict(x_test)
residual = y_test - p_test
sns.regplot(x=p_test, y=residual, lowess=True, line_kws={'color':'red'}) 
plt.plot([p_test.min(), p_test.max()], [0, 0], '--', color='gray')

# Apply polynomial transformation.
  # Transform to second-degree terms.
  # Do not include the intercept term.
  # Check the shape of the data before and after transformation

from sklearn.preprocessing import PolynomialFeatures
P = PolynomialFeatures(degree=2, include_bias=False) 
X_Poly = P.fit_transform (X) # Apply polynomial transformation and interaction terms to the X data 
X.shape, X_Poly.shape

# Split the data using the polynomial-transformed data
x_train, x_test, y_train, y_test = train_test_split(X_Poly, Y, random_state=0)

# Train the model using the polynomial-transformed data with the LinearRegression model and print the results
  # Display the R Squared values for both the training data and the evaluation data
model = LinearRegression().fit(x_train, y_train) 
model.score(x_train, y_train), model.score(x_test, y_test)

# Train the Lasso model using the polynomial-transformed data with a regularization strength of 1, 
  # and print the results
  # Display the R Squared values for both the training data and the evaluation data
from sklearn.linear_model import Lasso
model = Lasso(alpha=1).fit(x_train, y_train) 
model.score(x_train, y_train), model.score(x_test, y_test)

# Calculate the number of non-zero coefficients
len(model.coef_[model.coef_!=0])

# Train the Ridge model using the polynomial-transformed data with a regularization strength of 100, 
  # and print the results
  # Display the R Squared values for both the training data and the evaluation data
from sklearn.linear_model import Ridge 
model=Ridge(alpha=100).fit(x_train, y_train) 
model.score(x_train, y_train), model.score(x_test, y_test)

# Calculate the number of non-zero coefficients
len(model.coef_[model.coef_ != 0])
