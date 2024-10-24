# Scaling
  # Certain algorithms are greatly affected by the scale (range of observations) of the data, 
  # so methods such as Standardization and Normalization exist to align the range of observations uniformly

# Import the data that will have scaling applied
import pandas as pd
df = pd.read_csv('/path/iris.csv') 
df

df.columns[:-1].tolist()

# Extracting feature data for scaling
features = [
    'sepal length (cm)',
    'sepal width (cm)',
    'petal length (cm)',
    'petal width (cm)'
] # Columns to be excluded are commented out
X = df[features]
X

# Standardization
  # sklearn.preprocessing.MinMaxScaler
  # This method is used to unify different feature values into the same range
  # Mostly use Min-Max Normalization, which transforms data into a range between 0 and 1

# Whole transformation
from sklearn.preprocessing import MinMaxScaler 
scaler = MinMaxScaler() # Create scaler
X_Sclaed = scaler.fit_transform(X)

from sklearn.model_selection import train_test_split 
x_train, x_test = train_test_split(X)

# Partial transformation
scaler = MinMaxScaler() # Create scaler
x_train_scaled = scaler.fit_transform(x_train) 
x_test_scaled = scaler.transform(x_test) # Performs only the transformation

import matplotlib.pyplot as plt 
plt.subplot(1, 2, 1) 
plt.boxplot(X) 
plt.title('Before') 
plt.subplot(1, 2, 2) 
plt.boxplot(X_Sclaed) 
plt.title('After') 
plt.savefig('Standardization result') 
plt.show()

# Check transformation result
x_train_scaled

# Check inverse transformation result
scaler.inverse_transform(x_train_scaled)

# Compare with the original
x_train.values

