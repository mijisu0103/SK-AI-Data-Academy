# Decision Tree regression practice
# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Import regression data
df = pd.read_csv('/path/boston.csv')
df

# Query the count and data type for each column
df.info()

# Handling missing value
df['ZN'] = df['ZN'].fillna(0)
df['CHAS'] = df['CHAS'].fillna(0)

# Remove unnecessary column
df.drop('Unnamed: 0', axis=1, inplace=True) 
df

# Split data
X = df.iloc[:, :-1] 
Y = df.iloc[:, -1] 
X.head()

# Y is continuous > Use a regression model.
Y

# Split data
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0)

# Model creation
model = DecisionTreeRegressor()

# Model training
model.fit(x_train, y_train) # Only use train data

# DecisionTreeRegressor
# DecisionTreeRegressor()

# Model evaluation (R Squared)
print('train_data_performance :', model.score(x_train, y_train))
print('test_data_performance :', model.score(x_test, y_test))

# Model prediction
p_test = model.predict(x_test) # Predict for test data
p_test

# Adjust maximum depth
model = DecisionTreeRegressor(max_depth=10) model.fit(x_train, y_train)
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Query feature importances
model.feature_importances_

# Visualise feature importances
fi = pd.Series(model.feature_importances_, index=model.feature_names_in_)
fi[fi != 0].sort_values().plot(kind='barh')

# Visulising decision making tree
from sklearn.tree import export_graphviz 
export_graphviz(
  model,
  out_file='model.dot', 
  feature_names=model.
  feature_names_in_, 
  impurity=True
)

import graphviz
with open('model.dot') as f:
  data = f.read() 
graphviz.Source(data).render('model')

