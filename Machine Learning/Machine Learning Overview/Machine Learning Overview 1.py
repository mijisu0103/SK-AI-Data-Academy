# Classification
# Classifying an object into predefined categories.
"""
A method of categorizing an object based on given features (target).
  Used when the label or target is categorical.
When there are two categories, it is called Binary Classification.
When there are more than two categories, it is called Multiclass Classification
"""

# Loading classification prediction result data
import pandas as pd
df = pd.read_csv('/path/classification result.csv')
df

# Confusion Matrix
# sklearn.metrics.confusion_matrix
# A confusion matrix is a classification table that shows whether the predicted values match the actual values.
# One axis of the table represents the predicted categories, while the other axis represents the actual categories.
"""
In binary classification, the results can be seen in 4 metrics based on predicted and actual categories:
  True Positive (TP): The result was correctly predicted as Positive.
  False Negative (FN): The result was incorrectly predicted as Negative.
  False Positive (FP): The result was incorrectly predicted as Positive.
  True Negative (TN): The result was correctly predicted as Negative
"""

# Confusion Matrix Calculation
from sklearn.metrics import confusion_matrix
confusion_matrix(df['actual_value'], df['predicted_value'])

# Save the result of confusion matrix calculation result
tn, fp, fn, tp = confusion_matrix(df['actual_value'], df['predicted_value']).ravel()
print('True Negative :', tn)
print('False Positive :', fp)
print('False Negative :', fn)
print('True Positive :', tp)

# Accuracy
# sklearn.metrics.accuracy_score
# (TP + TN) / (TP + FN + FP + TN)
# Accuracy represents the proportion of the entire dataset that was classified correctly.
(tp + tn) / (tp + fn + fp + tn)

from sklearn.metrics import accuracy_score
accuracy_score(df['actual_value'], df['predicted_value'])

# Recall
# sklearn.metrics.precision_score
# TP / (TP + FP)
# Recall represents the ratio of true positives to the total number of actual positives
tp / (tp + fp)

from sklearn.metrics import precision_score
precision_score(df['actual_value'], df['predicted_value'])

# F1 Score
# sklearn.metrics.f1_score
# 2TP / (2TP + FP + FN)
# The F1 Score is the harmonic mean of precision and recall
# The F1 score ensures that when either precision or recall is close to 0, the F1 score will also be low
2 * tp / (2 * tp + fp + fn)

from sklearn.metrics import f1_score
f1_score(df['actual_value'], df['predicted_value'])

# RoC(Receiver operating characteristic) Curve
# sklearn.metrics.roc_curve
# The relationship between the False Positive Rate (FPR) and the True Positive Rate (TPR)
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(df['actual_value'], df['predicted_value'])
# the first and last values of both the False Positive Rate (FPR) and True Positive Rate (TPR) 
# are set to specific values for graphing purposes
print('FPR', fpr[1:-1])
print('TPR', tpr[1:-1])
print('thresholds', thresholds[1:-1])

#AUC (Area Under the Curve)
# sklearn.metrics.roc_auc_score
# Area under the curve (AUC).
# The closer it is to 1, the better the performance
from sklearn.metrics import roc_auc_score
roc_auc_score(df['actual_value'], df['predicted_value'])

from sklearn.metrics import auc
auc(fpr, tpr) # X-axis, Y-axis

# RoC Curve visualisation
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 6))
plt.plot(fpr, tpr, label=f'Roc Curve (AUC : {auc(fpr, tpr)} )')

plt.plot([0, 1], [0, 1], color="gray", linestyle="--")
plt.legend()

from sklearn.metrics import classification_report
print(classification_report(df['actual_value'], df['predicted_value']))

