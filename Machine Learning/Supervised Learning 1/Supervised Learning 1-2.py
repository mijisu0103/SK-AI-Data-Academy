# Classifying Wine Type
# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns

# Read and query data
  # Read red_wine.csv file in the /path directory
  # View top 5 sample (rows)
red = pd.read_csv('/path/red_wine.csv', sep=";") 
red.head()

  # Read white_wine.csv file in the /path directory
  # View top 5 sample (rows)
white = pd.read_csv('/path/white_wine.csv', sep=";") 
white.head()

# Add a type column that has 'red' value in red_wine dataframe
red['type'] = 'red' 
red

# Add a type column that has 'white' value in white_wine dataframe
# Add a category for classification
white['type'] = 'white' 
white

# Merge red_wine dataframe and white_wine dataframe
  # Use concat()
  # When merging dataframe, ignore index or initialise index after merging
wine = pd.concat([red, white], ignore_index = True) 
wine

# Change the name of column
  # ['Acidity', 'Aroma', 'Freshness', 'Sweetness', 'Saltiness', 'Sulfur Compound 1', 'Sulfur Compound 2,
  #  'Body', 'Sourness', 'Sulfur Compound 3', 'Alcohol', 'Quality', 'Type']
wine.columns=['Acidity', 'Aroma', 'Freshness', 'Sweetness', 'Saltiness', 'Sulfur Compound 1', 'Sulfur Compound 2','Body', 'Sourness', 'Sulfur Compound 3', 'Alcohol', 'Quality', 'Type']
wine

# Split X and Y
  # X: The rest of the columns except Type column
  # Y: Type column

X = wine.loc[:, wine.columns != 'Type']
Y = wine['Type']

# Print split X
X

# Print split Y
Y 

# Using split X and Y, split them into Train and Test
  # Split them in 7:3 ratio
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

# Use KNN model to train and print the result
  # Set K as 5
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 5).fit(x_train, y_train) 
model.score(x_train, y_train), model.score(x_test, y_test)
