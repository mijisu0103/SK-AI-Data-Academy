# Module import
from IPython.display import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
# Remove Unicode warning
plt.rcParams['axes.unicode_minus']=False
# Set a font for Korean
plt.rcParams['font.family'] = "NanumGothic"
# Set an output size for a graph
plt.rcParams["figure.figsize"] = (12, 8)

# Seaborn
# Seaborn is a library that makes matplotlib easier to use

# Load sample dataset
tips = sns.load_dataset("tips")

# Why Seaborn?
# Most visualizations can be done with matplotlib. However, many people prefer seaborn for the following reasons:
"""
  Ease of use (one-line graph creation)
  Statistical plots that are only available in seaborn
  Beautiful styling
  High compatibility with Pandas DataFrames
"""

# Beautiful Styling
# One of the greatest advantages of seaborn is its beautiful color palettes
"""
Compared to the default colors in matplotlib, 
seaborn provides aesthetically pleasing color combinations by default, without much effort needed for styling
"""

fig, axes = plt.subplots(1, 2)
fig.set_size_inches(12, 6)

axes[0].bar(tips['day'], tips['total_bill'])
axes[0].set_title('matplotlib')
sns.barplot(x="day", y="total_bill", data=tips, palette='Set1', ax=axes[1])
axes[1].set_title('seaborn')
plt.show()

# Color Palette
sns.color_palette()

# Light
sns.light_palette("seagreen", n_colors=10)

# Dark
sns.dark_palette("#69d", n_colors=10)

# Diverging
sns.color_palette('vlag', n_colors=10)

sns.diverging_palette(220, 20, n=10)

# Custom
sns.cubehelix_palette(10, start=9.9)

# Various examples
sns.palplot(sns.light_palette((210, 90, 60), input="husl"))
sns.palplot(sns.dark_palette("muted purple", input="xkcd"))
sns.palplot(sns.color_palette("BrBG", 10))
sns.palplot(sns.color_palette("BrBG_r", 10))
sns.palplot(sns.color_palette("coolwarm", 10))
sns.palplot(sns.diverging_palette(255, 133, l=60, n=10, center="dark"))

sns.barplot(x="tip", y="total_bill", data=tips, palette='coolwarm')

sns.barplot(x="tip", y="total_bill", data=tips, palette='Reds')

# Seaborn Graph
# Scatterplot
# Set x, y, colors, area

# Colors are random values that are converted into color values.
# Area represents the size of the points; as the value increases, the area also increases

# Create sample data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.arange(50)
area = x * y * 250

# In seaborn, one specifies both size and sizes simultaneously.
"""
The sizes option allows one to specify the minimum and maximum size.
hue is the color option.
One can use seaborn's beautiful palettes through the palette option
"""

sns.scatterplot(x=x, y=y, size=area, sizes=(area.min(), area.max()), hue=area, palette="viridis")

# Setting camp and alpha
"""
Setting cmap and alpha: If one specifies a color in cmap, all points can have the same color.
The alpha value represents transparency, and it can be set between 0 and 1, 
where values closer to 0 are more transparent
"""

sns.scatterplot(x=x, y=y, size=area, sizes=(area.min(), area.max()), hue=area, alpha=0.6)

# Pointplot
# Pointplot estimates the central tendency of a numerical variable based on point positions 
# and uses error bars to indicate the uncertainty around the estimate
np.random.seed(123)
x = np.random.rand(50).round(1)
y = np.random.rand(50).round(1)

# Create pointplot
sns.pointplot(x=x, y=y)

"""
Error bars are used to represent the expected measurement error. 
In other words, error bars indicate the uncertainty of the value.
In pointplot and barplot, the error bars are automatically drawn based on the confidence interval (CI), 
which represents the range of values where the true population parameter lies with a certain level of confidence.

What is a confidence interval (CI)?
A confidence interval is a commonly used concept, even though it may seem complicated at first glance.
Let's look at an example to understand how confidence intervals are used:

The value between 10 and 15 likely comes from the average time it takes to ride this bus, based on multiple observations."

This example demonstrates the concept of uncertainty around an estimate, and the confidence interval provides a range within which the true value is expected to fall.

Why don't we just say '12.5 minutes' exactly instead of 'it takes about 10-15 minutes'?
This is because there is uncertainty involved. Therefore, we express the range where we can be reasonably certain.
For example, in a poll, you might have heard something like 'Candidate A has 31% support, Candidate B has 28% support, with a margin of error of ±2.0%.'
That ±2.0% is exactly the same concept as a confidence interval.
"""

# Barplot, Barhplot
  # Drawing multiple graphs on a single canvas
  # Drawing a basic Barplot
  # Creating sample data

score = pd.DataFrame({
'subject': ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics'],
'score': [66, 80, 60, 50, 80, 10]
})
score

# Create bar graph
sns.barplot(x='subject', y='score', data=score, alpha=0.8, palette='YlGnBu')

# Drawing basic Barhplot
# In the barh function, the xticks setting is changed to yticks
sns.barplot(y='subject', x='score', data=score, alpha=0.8, palette='YlGnBu')

# Creating comparison bar plots
# In seaborn, one can easily create comparison bar plots using the hue option

# Load sample dataset
titanic = sns.load_dataset('titanic')
titanic.head(2)

# Specify the column name that acts as the splitting condition in the hue option.
sns.barplot(x='sex', y='survived', hue='pclass', data=titanic, palette="muted")

# Line Plot
# Create sample dataset
x = np.arange(0, 10, 0.1)
y_1 = 1 + np.sin(x)
y_2 = 1 + np.cos(x)

# color: color option
# alpha: transparency option

# Create lineplot
sns.lineplot(x=x, y=y_1, label='1+sin', color='navy', alpha=0.3)
sns.lineplot(x=x, y=y_2, label='1+cos', color='red', alpha=0.7)

# Marker Styling
# marker: marker option
sns.lineplot(x=x, y=y_1, label='1+sin', color='navy', alpha=0.3, marker='o')
sns.lineplot(x=x, y=y_2, label='1+cos', color='red', alpha=0.7, marker='+')

# Change linestyle
# linestyle: line style change option
sns.lineplot(x=x, y=y_1, label='1+sin', color='blue', linestyle=':')
sns.lineplot(x=x, y=y_2, label='1+cos', color='red', linestyle='-.')

# Histogram
# Create sample data
N = 100000
bins = 30

x = np.random.randn(N)

sns.histplot(x, bins=bins, kde=False, color='g')

# If one sets kde to True, it displays density on y-axis
sns.histplot(x, bins=bins, kde=True, color='g')

# Frequency distribution table and cumulative frequency distribution table
# Create sample dataset
x = np.random.randn(100)

fig, axes = plt.subplots(1, 2, tight_layout=True)
fig.set_size_inches(12, 4)

# Create histogram
sns.histplot(x=x, bins=bins, ax=axes[0])
sns.histplot(x=x, bins=bins, cumulative=True, ax=axes[1])

# Box Plot
# Create sample data
titanic = sns.load_dataset('titanic')

# When drawing a boxplot in seaborn, it is mainly used with a DataFrame
# In seaborn, one can easily create comparison boxplots using the hue option.
sns.boxplot(x='pclass', y='age', hue='survived', data=titanic)

