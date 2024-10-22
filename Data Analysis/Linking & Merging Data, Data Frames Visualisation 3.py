# Download the necessary data files for the practice
# Install the downloader for the necessary data files for practice
!pip install opendata-kr -q

from opendata import dataset
dataset.download('PrivateApartmentSale')

# Basic import
from IPython.display import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
# Remove Unicode warning)
plt.rcParams['axes.unicode_minus']=False
# Setting a font for Korean
plt.rcParams['font.family'] = "NanumGothic"
# Setting the output size for the graph
plt.rcParams["figure.figsize"] = (12, 8)

# Load dataset
# Housing and Urban Guarantee Corporation - National New Private Apartment Sale Price Trends
# Source: Public Data Portal (https://www.data.go.kr/)
df = pd.read_csv('data/house_price.csv')
df.head()

# Visualization using DataFrame
  # kind option:
    # line: Line graph
    # bar: Bar graph
    # barh: Horizontal bar graph
    # hist: Histogram
    # kde: Kernel density plot
    # box: Box plot
    # pie: Pie chart
    # scatter: Scatter plot

# Line Graph
# A line graph is appropriate to use when the data is continuous, such as stock price data.
df['saleprice'].plot(kind='line')

# Filter by the Seoul region
df_seoul = df.loc[df['region'] == 'Seoul']
df_seoul

# Print the average sale price by year
df_seoul_year = df_seoul.groupby('year')[['saleprice']].mean()
df_seoul_year

df_seoul_year['saleprice'].plot(kind='line')

# Bar Graph
# Bar graphs are useful for comparing groups
df.groupby('region')['saleprice'].mean()

df.groupby('region')['saleprice'].mean().plot(kind='bar')

df.groupby('region')['saleprice'].mean().plot(kind='barh')

# Histogram (hist)
# Histograms visualize distribution and frequency.
# The horizontal axis shows the distribution, and the vertical axis shows the frequency
df['saleprice'].plot(kind='hist')

# Kernel Density Plot
# It is a graph that shows density, similar to a histogram.
# It has a shape similar to a histogram but features smooth lines.
df['saleprice'].plot(kind='kde')

# Box Plot (Box)
df_seoul = df.loc[df['region'] == 'Seoul']
df_seoul['saleprice'].plot(kind='box')

# IQR refers to Inter Quantile Range
# (3Q - 1Q) * 1.5

# Pie Graph
df.groupby('연도')['분양가'].count().plot(kind='pie', autopct="%.2f", figsize=(8, 8))

# Scatter Plot
# It displays data using dots.
# One needs to provide x and y values (similar to hexbin).
# By specifying the x and y axes, one can see the corresponding data distribution.
# Only numeric columns can be specified
df.head()

df.plot(x='month', y='saleprice', kind='scatter')
















