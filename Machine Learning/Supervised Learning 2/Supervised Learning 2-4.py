# Card payment delinquency prediction
# 0 indicates no delinquency, while 1 indicates delinquency

# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns

# Reading and querying data
# Read /path/creditcard.csv and save it in df
# Query top5 sample(rows)
df = pd.read_csv('/path/creditcard.csv') 
df.head(5)

# Query shape in dataframe
df.shape

# Query missing value in dataframe
df.isna().sum()

# Print information of the dataframe
df.info()

# Conduct basic statistical analysis of the DataFrame
df.describe()

# Use the var() function to check the variance for each column in the DataFrame
df.var()

# Calculate the count for each value in the Class column
df['Class'].value_counts()

# Calculate the ratio for each value in the Class column
df['Class'].value_counts(normalize=True)

# Visualize the results
df['Class'].value_counts(normalize=True).plot(kind='bar')

# Check the distribution of each column in the DataFrame 
# using the hist(figsize=(15, 15), bins=20) function
df.hist(figsize=(15,15), bins=20)
plt.show()

# Extract only the normal data (Class 0) and check the distribution of each column 
# using the hist(figsize=(15, 15), bins=20) function
df[df['Class'] == 0].hist(figsize(15,15), bins=20) 
plt.show()

# Extract only the abnormal data (Class 1) and check the distribution of each column 
# using the hist(figsize=(15, 15), bins=20) function
df[df['Class'] == 1].hist(figsize=(15, 15), bins=20) 
plt.show()

# Draw a BoxPlot for each column using the following parameters:
# subplots=True, layout=(7, 5), and figsize=(15, 21)
df.plot(kind='box', subplots=True, layout=(7, 5), figsize=(15, 21)) 
plt.show()

# Visualize the distribution of the Amount column 
# using the hist function
df['Amount'].hist()

# Create the Amount_log column using the np.log1p function
df['Amount_log'] = np.log1p(df['Amount']) 
df

# Visualize the distribution of the Amount_log column 
# using the hist function
df['Amount_log'].hist()

# Extract the DataFrame where the class column value is 1 and visualize the Time column using the hist function
# Then, extract the DataFrame where the class column value is 0 and visualize the Time column using the hist function as well 
# Use subplots to display both histograms
plt.figure(figsize=(15, 10))
plt.subplot(2, 1, 1)
df.loc[df['Class'] == 1, 'Time'].hist(bins=50, color='r') 
plt.title('Fraud')
plt.subplot(2, 1, 2)
df.loc[df['Class'] == 0, 'Time'].hist(bins=50, color='b') 
plt.title('Normal')

# Extract the DataFrame where the class column value is 1 and visualize the Time column 
  # using the scatter function. Use the plot function with the parameters
  # kind='scatter', x='Time', y='Amount', and color='r'
df.loc[df['Class'] == 1].plot(kind='scatter', x='Time', y='Amount', color='r') 
plt.title('Fraud')

# Extract the DataFrame where the class column value is 0 and visualize the Time column 
  # using the scatter function. Use the plot function with the parameters: 
  # kind='scatter', x='Time', y='Amount', and color='b'
df.loc[df['Class'] == 0].plot(kind='scatter', x='Time', y='Amount', color='b') 
plt.title('Normal')

# Calculate the correlation of the DataFrame
df.corr()

# Visualize the calculated correlation using a heatmap
plt.figure(figsize=(25, 25))
sns.heatmap(df.corr(), fmt='.2f', annot=True, cmap='Greens')

# Extract the DataFrame where the class column value is 1 and visualize the correlation using a heatmap
plt.figure(figsize=(25, 25))
sns.heatmap(df[df['Class']==1].corr(), fmt='.2f', annot=True, cmap='Greens')

# Extract the DataFrame where the class column value is 0 and visualize the correlation using a heatmap
plt.figure(figsize=(25, 25))
sns.heatmap(df[df['Class']==0].corr(), fmt='.2f', annot=True, cmap='Greens')

# Select the features to be used for training
# To exclude features from the training, comment them out
features = [
     'V1',
     'V2',
     'V3',
     'V4',
     'V5',
     'V6',
     'V7',
     'V8',
     'V9',
     'V10',
     'V11',
     'V12',
     'V13',
     'V14',
     'V15',
     'V16',
     'V17',
     'V18',
     'V19',
     'V20',
     'V21',
     'V22',
     'V23',
     'V24',
     'V25',
     'V26',
     'V27',
     'V28',
     'Amount_log'
]
features

# Extract only the column names stored in features and assign them to X
X = df[features] 
X

# Extract the Class column and assign it to Y
Y = df['Class'] 
Y

# Normalize the extracted X data using RobustScaler
from sklearn.preprocessing import RobustScaler 
scaler = RobustScaler()
X_Sclaed = scaler.fit_transform(X)
X_Sclaed

# Split X_scaled and Y into training and test sets, 
# applying stratified sampling and setting random_state to 0
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X_Sclaed, Y, stratify=Y, random_state=0)

# Apply the Decision Tree model and evaluate its performance
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier().fit(x_train, y_train) 
model.score(x_train, y_train), model.score(x_test, y_test)

# When the class distribution is asymmetric, accuracy can be misleadingly high
# To evaluate the model's performance accurately, use the classification_report function to assess the test data
from sklearn.metrics import classification_report 
p_test = model.predict(x_test) 
print(classification_report(y_test, p_test))

# Visualize the feature importance, 
  # excluding those with an importance of 0
  # Display only the top 10 features
fi = pd.Series(model.feature_importances_, index=X.columns) 
fi[fi != 0].sort_values().head(10).plot(kind='barh')

