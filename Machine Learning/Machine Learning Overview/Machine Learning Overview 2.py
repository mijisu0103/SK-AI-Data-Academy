# Regression
# A method of modeling the relationship between
#   independent variables (features) and the dependent variable (label)
# Used when the label or target is continuous
# It finds the optimal regression coefficients 
#   based on the relationship between the independent and dependent variables

# Load the regression prediction result data
import pandas as pd
df = pd.read_csv('/path/regression result.csv')
df

# R Squared
# sklearn.metrics.r2_score
# The ratio of the variance of predicted values to the variance of actual values (best: 1, worst: negative).
# It is used to evaluate the performance (explanatory power) of the model's predictions

import numpy as np
1 - (np.sum(np.square(df['actual_value'] - df['predicted_value'])) / np.sum(np.square(df['actual_value'] - df['actual_value'].mean())))

from sklearn.metrics import r2_score 
r2_score(df['actual_value'], df['predicted_value'])

# Mean Absolute Error
# sklearn.metrics.mean_absolute_error
# It calculates the average of the absolute differences between actual values and predicted values, 
# reflecting the magnitude of the error
# The smaller, the better; however, if it's too small, it may indicate overfitting

np.mean(np.abs(df['actual_value'] - df['predicted_value']))

from sklearn.metrics import mean_absolute_error 
mean_absolute_error(df['actual_value'], df['predicted_value'])

# Mean Squared Error
# sklearn.metrics.mean_squared_error(squared=True)
# It calculates the average of the squared differences between actual values and predicted values
# The smaller, the better; however, if it's too small, it may indicate overfitting
# It is sensitive to outliers because larger errors are penalized more heavily, and smaller errors are penalized less

np.mean(np.square(df['actual_value'] - df['predicted_value']))

from sklearn.metrics import mean_squared_error 
mean_squared_error(df['actual_value'], df['predicted_value'])

# Root Mean Squared Error
# sklearn.metrics.mean_squared_error(squared=False)
# Used to check the average magnitude of errors, allowing comparison of residuals between models
#   It is less sensitive to outliers
# Heavily penalizes large error differences, 
# and it is used to reduce the size of MSE

np.sqrt(np.mean(np.square(df['actual_value'] - df['predicted_value'])))

from sklearn.metrics import mean_squared_error
mean_squared_error(df['actual_value'], df['expected_value'], squared=False)

# RMSLE (Root Mean Squared Logarithmic Error)
# Less sensitive to outliers (robust)
#   Has low fluctuation in values
# Measures relative error
#   When predicted value = 100 and actual value = 90, RMSLE = 0.1053, RMSE = 10
#   When predicted value = 10,000 and actual value = 9,000, RMSLE = 0.1053, RMSE = 1,000
# Heavily penalizes underestimation

from sklearn.metrics import mean_squared_log_error
mean_squared_log_error(df['actual_value'], df['[predicted_value'], squared=False)

