# Support Vector Machine
# A machine learning model based on supervised learning used for classification, regression, and outlier detection
#   It works well for complex classification problems and is suitable for small to medium-sized datasets
# Support Vector Machines (SVMs) aim to find a decision boundary that maximizes the margin 
# The margin is defined as the distance between the decision boundary (hyperplane) that separates the classes 
# Support Vector is the closest training samples to this hyperplane

# SVM is sensitive to feature scaling
#   adjusting the scale through standardization can significantly improve the decision boundary 

# SVMs tend to use a large margin because it lowers the generalization error
#   while a small margin can lead to overfitting.

# For example, if the decision boundary H3 does not classify the classes properly, H1 and H2 do
#   However, H1 may not work well for new samples because it is close to the support vectors
#   while H2, which is further from the support vectors, performs better

# When all samples are correctly classified outside the margin, it's called hard margin classification
# Hard margin classification has two issues: 
#   it only works well when the data is linearly separable 
#   and is sensitive to outliers
  
# To balance margin errors, soft margin classification is used 
#   by adjusting the hyperparameter C 
#   If overfitting occurs, reducing C can help regularize the model

# Setting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns

from sklearn.model_selection import train_test_split from sklearn.svm import SVC # Classification model
from sklearn.svm import SVR # Regression model

# Import classification data
df = pd.read_csv('/path/iris.csv') 
df

# Query missing value by column
df.isna().sum()

# Query data type by column
df.dtypes

# Query the number of data and data type by column
df.info()

df['target']

# Split data
  # For visualisation, only use two features (petal length, petal width)
  # Change the classification to a binary one where the target is whether the category is Virginica or not
X = df.loc[:, ['petal length (cm)', 'petal width (cm)']] 
Y = df.loc[:, 'target'] == 2
X.head()

# Y is categorical > Use a classification model
Y

# SVM is sensitive to scaling > Apply standardization
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler()
X_Scaled = scaler.fit_transform(X)

# Split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X_Scaled, Y, random_state=0)

# Create and train a linear SVM model
from sklearn.svm import LinearSVC
model = LinearSVC(C=1, loss='hinge', random_state=42) 
model.fit(x_train, y_train)

# LinearSVC
# LinearSVC(C=1, loss='hinge', random_state=42)

# Model evaluation
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Model prediction
p_test = model.predict(x_test) # Predict test data 
p_test

# Calculate classification_report
from sklearn.metrics import classification_report 
print(classification_report(y_test, p_test))

# Use SVC model
from sklearn.svm import SVC 
model = SVC(C=1) 
model.fit(x_train, y_train)

# SVC
# SVC(C=1)

# Model evaluation
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Model prediction
p_test = model.predict(x_test) # Predict test data
p_test

# Calculate classification_report
from sklearn.metrics import classification_report 
print(classification_report(y_test, p_test))

# For datasets that cannot be classified linearly, additional datasets like polynomial features can be added 
  # using PolynomialFeatures

# When using the kernel trick, nonlinear classification becomes possible 
  # This method produces results as if many polynomial features were added, without actually adding any new features

# Import non-linear classification data
df = pd.read_csv('/path/moon.csv') df

# Split data
X = df.loc[:, df.columns != 'y'] 
Y = df.loc[:, 'y']
X.head()

# Check the categories
Y.head()

# Data visualisation
plt.plot(X.loc[Y==0, 'X1'], X.loc[Y==0, 'X2'], 'bs') 
plt.plot(X.loc[Y==1, 'X1'], X.loc[Y==1, 'X2'], 'g^')

# Apply polynomial transformation
from sklearn.preprocessing import PolynomialFeatures 
P = PolynomialFeatures(degree=3)
X_Poly = P.fit_transform(X)

# Apply standardisation
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler()
X_Scaled = scaler.fit_transform(X_Poly)

# Model creation and training
model = LinearSVC(C=10, loss='hinge') 
model.fit(X_Scaled, Y)

# LinearSVC
# LinearSVC(C=10, loss='hinge')

# Result visualisation
def plot_predictions(clf, axes):
  x0s = np.linspace(axes[0], axes[1], 100) 
  x1s = np.linspace(axes[2], axes[3], 100) 
  x0, x1 = np.meshgrid(x0s, x1s)
  x = np.c_[x0.ravel(), x1.ravel()] 
  x_poly = P.transform(x)
  x_scaled = scaler.transform(x_poly)
  y_pred = clf.predict(x_scaled).reshape(x0.shape)
  y_decision = clf.decision_function(x_scaled).reshape(x0.shape) 
  plt.contourf(x0, x1, y_pred, cmap=plt.cm.brg, alpha=0.2) 
  plt.contourf(x0, x1, y_decision, cmap=plt.cm.brg, alpha=0.1)

plot_predictions(model, [-1.5, 2.5, -1, 1.5]) 
plt.plot(X.loc[Y==0, 'X1'], X.loc[Y==0, 'X2'], 'bs') 
plt.plot(X.loc[Y==1, 'X1'], X.loc[Y==1, 'X2'], 'g^')

# Use the polynomial kernel model
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler()
X_Scaled = scaler.fit_transform(X)

model = SVC(kernel='poly', degree=3, coef0=1, C=5) 
model.fit(X_Scaled, Y)

# SVC
# SVC(C=5, coef0=1, kernel='poly')

# Result visualisation
def plot_predictions(clf, axes):
  x0s = np.linspace(axes[0], axes[1], 100) 
  x1s = np.linspace(axes[2], axes[3], 100) 
  x0, x1 = np.meshgrid(x0s, x1s)
  x = np.c_[x0.ravel(), x1.ravel()] 
  x_scaled = scaler.transform(x)
  y_pred = clf.predict(x_scaled).reshape(x0.shape)
  y_decision = clf.decision_function(x_scaled).reshape(x0.shape) 
  plt.contourf(x0, x1, y_pred, cmap=plt.cm.brg, alpha=0.2) 
  plt.contourf(x0, x1, y_decision, cmap=plt.cm.brg, alpha=0.1)

plot_predictions(model, [-1.5, 2.5, -1, 1.5]) 
plt.plot(X.loc[Y==0, 'X1'], X.loc[Y==0, 'X2'], 'bs') 
plt.plot(X.loc[Y==1, 'X1'], X.loc[Y==1, 'X2'], 'g^')

# In SVM regression, the model is trained to include as many samples as possible within a limited margin of error
# The size of the margin is controlled by the hyperparameter 𝜖
# Adding training samples within the margin does not affect the model's predictions
# For nonlinear regression, a kernel SVM model is used

# Import regression data
df = pd.read_csv('/path/diabetes.csv') 
df

# Query the count and data type for each column
df.info()

# Split data
X = df.iloc[:, :-1] 
Y = df.iloc[:, -1] 
X.head()

# Y is continuous > Use a regression model
Y

# Apply standardisation
from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler()
X_Scaled = scaler.fit_transform(X)

# Split data for training and testing
x_train, x_test, y_train, y_test = train_test_split(X_Scaled, Y, random_state=0)

# Model creation
model = SVR(C=10)

# Model training
model.fit(x_train, y_train) # Only use train data

# SVR
# SVR(C=10)

# Model evaluation (R Squared)
print('train_data_performance :', model.score(x_train, y_train)) 
print('test_data_performance :', model.score(x_test, y_test))

# Model prediction
p_test = model.predict(x_test) # Predict test data
p_test

# Calculate rmse
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, p_test, squared=False)

