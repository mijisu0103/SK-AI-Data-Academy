# Splitting Data
# In order to properly train the model, the data must be split
#   If all the data is used for training, it is impossible to assess the generalization performance
#   A portion of the data is excluded from training and is used to evaluate the model once training is complete
#     This checks whether the model can make accurate predictions on data it has not seen before
# Typically, 75% of the data is used for training and 25% for evaluation
#   Only the training data is used for training the machine learning model
#   The evaluation data is used to assess the performance of the machine learning model

from sklearn.model_selection import train_test_split 
train_test_split(
  *arrays, # Data to be split
  test_size=0.25, # Proportion of test data
  shuffle=True, # Whether to apply data shuffling
  stratify=False, # Whether to apply stratified splitting
  random_state=None # Seed value
)

# Create data to be split
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
data

from sklearn.model_selection import train_test_split 
train_test_split(data)

# Seed specification for reproducibility of split results
train_test_split(data, random_state=0)

# Adjusting the test data ratio
train_test_split(data, test_size=0.4, random_state=0)

# Without applying data shuffling
train_test_split(data, test_size=0.4, shuffle=False, random_state=0)

# Create data to be split
X = [1, 2, 3, 4, 5]
Y = [True, False, True, False, True]
len(X), len(Y) # The number of data should be matched

# Splitting two variables
train_test_split(X, Y, random_state=0)

# Saving the split result
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0)

# Loading data for splitting
import pandas as pd
df = pd.read_csv('/path/iris.csv') 
df

# Splitting the data into X (features) and Y (labels)
X = df.iloc[:, :-1]
Y = df.iloc[:, -1]
X.shape, Y.shape # The number of data matches (150)

# Data splitting and checking the split results
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0) print('X Train Shape', x_train.shape)
print('X Test Shape', x_test.shape)
print('Y Train Shape', y_train.shape)
print('Y Test Shape', y_test.shape)

pd.value_counts(Y, normalize=True)

pd.value_counts(y_train, normalize=True)

pd.value_counts(y_test, normalize=True)

# Applying stratified splitting (to split the data while maintaining similar proportions of categories)
x_train, x_test, y_train, y_test = train_test_split(X, Y, stratify=Y, random_state=0)

pd.value_counts(y_train, normalize=True)

pd.value_counts(y_test, normalize=True)

