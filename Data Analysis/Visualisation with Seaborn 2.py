# Statistical-based graphs
# The appeal of the seaborn library lies in its ability to create statistical charts.
# In this practice, we will cover a few of the most representative statistical charts provided by seaborn

# Module import
from IPython.display import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
# Remove Unicode warning
plt.rcParams['axes.unicode_minus']=False
# Set style
sns.set_style('white')
# Set an output size for a graph
plt.rcParams["figure.figsize"] = (12, 8)

# Load sample dataset
titanic = sns.load_dataset('titanic')
titanic

# Columns Description
"""
  survived: Survival status (1: Survived, 0: Deceased)
  pclass: Ticket class (1st, 2nd, 3rd class)
  sex: Gender
  age: Age
  sibsp: Number of siblings + spouses aboard
  parch: Number of parents + children aboard
  fare: Fare paid for the ticket
  embarked: Port of embarkation (S: Southampton, C: Cherbourg, Q: Queenstown)
  class: Same as pclass (ticket class)
  who: Man, Woman, Child
  adult_male: Whether the person is an adult male (True/False)
  deck: Deck number (mix of letters and numbers)
  embark_town: Name of the port of embarkation
  alive: Survival status (yes: Survived, no: Deceased)
  alone: Whether the passenger was traveling alone (True/False)
"""

tips = sns.load_dataset('tips')
tips

# Columns Description
"""
  total_bill: The total bill amount
  tip: The tip given
  sex: Gender of the person paying
  smoker: Whether they are a smoker
  day: Day of the week
  time: Time of the meal
  size: Number of people dining
"""

# Countplot
# Countplot is a type of plot that counts the number of occurrences for each category.
# It automatically separates and displays the values that make up the specified column

# Drawing the countplot vertically
sns.countplot(x="class", hue="who", data=titanic)

# Drawing the countplot horizontally
sns.countplot(y="class", hue="who", data=titanic, palette='rocket')

#kdeplot
# KDE (Kernel Density Estimate) is a method that shows a smoother distribution curve compared to a histogram

# Create sample data
x = np.random.randn(100)

sns.kdeplot(x=x)

# rugplot
# Rugplot's 'rug' represents the position of the data on the x-axis with small line segments, 
# showing the location and distribution of the data
sns.kdeplot(x=x)
sns.rugplot(x=x)

# heatmap
# The characteristic feature is that it outputs various information, which can be represented through colors, as a heatmap, 
# showing data in a visual form of distribution over a set image

# Correlation Visualisation
# The corr() function shows the correlation between the data
titanic.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(titanic.corr(), annot=True, cmap="RdBu_r")
plt.show()

# pairplot
# Pairplot creates a grid of plots showing histograms and scatter plots for each combination of variables. 
# It only plots numerical columns
iris = sns.load_dataset('iris')
iris.head()

# Create basic pairplot
sns.pairplot(iris)

# Using the hue option to distinguish characteristics
sns.pairplot(iris, hue='species', palette="Set1")

# Violinplot
# Violinplot is a plot that resembles a violin.
# It allows one to compare the distribution of data for a column.
# The curved, wider part represents the distribution of the data,
# while the pointed ends represent the minimum and maximum values of the data

# Draw basic violinplot
sns.violinplot(x=tips["total_bill"])

# Checking comparative distributions
# By specifying the x and y axes, one can split the violin to see the comparative distribution
sns.violinplot(x="day", y="total_bill", data=tips)

# Using the hue option to compare distributions
# Without the hue option, the violin plot is symmetric, so comparing distributions doesn't hold much meaning.
# However, by using the hue option, one can compare the violin shapes for a single column
sns.violinplot(x="day", y="total_bill", hue="smoker", data=tips, palette="muted")

# Using the split option, one can merge and compare the violins in a single view.
sns.violinplot(x="day", y="total_bill", hue="smoker", data=tips, palette="muted", split=True)

# Implot
# Implot is a chart useful for checking linear relationships between columns.
# Additionally, it allows for a rough estimation of outliers

# Basic Implot
sns.lmplot(x="total_bill", y="tip", data=tips)

# Using the hue option to draw multiple linear relationships.
# In the graph below, one can see that non-smokers have a steeper linear relationship compared to smokers.
sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips)

# By adding the col option, one can create separate plots for different categories.
# Additionally, one can specify the number of columns per row using col_wrap
sns.lmplot(x='total_bill', y='tip', hue='smoker', col='day', col_wrap=2, data=tips)

# jointplot
# Scatter plot and histogram can be drawn together, but only numerical data can be represented, 
# so keep that in mind.

# Draw basic jointplot
sns.jointplot(x="total_bill", y="tip", height=7, data=tips)

# Drawing a regression line to represent linear relationships.
# Add the option kind='reg'
sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")

# Viewing hexagonal density 
# View hexagonal density using kind='hex' option
sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")

# Swarm Plot
sns.swarmplot(x='day', y='total_bill', data=tips)

sns.boxplot(x='day', y='total_bill', data=tips)
sns.swarmplot(x='day', y='total_bill', data=tips, color='black')

# Catplot
# One can visualize graphs categorized by splitting them into rows or columns based on a certain category
  # The black bars represent error bars, indicating the 95% confidence interval
titanic.head()

# barplot
sns.catplot(x='who', y='survived',
  col='pclass',
  row='embarked',
  kind='bar',
  height=3,
  data=titanic)

# Countplot
sns.catplot(x='survived',
  col='pclass',
  row='embarked',
  kind='count',
  height=3,
  data=titanic)

sns.catplot(x='who',
  y='age',
  col='pclass',
  row='embarked',
  kind='box',
  height=3,
  data=titanic)

# violinplot
sns.catplot(x='who',
  y='fare',
  col='pclass',
  kind='violin',
  height=3,
  data=titanic)













