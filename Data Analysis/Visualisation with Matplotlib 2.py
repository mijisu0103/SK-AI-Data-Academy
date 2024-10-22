# matplotlib Graph

# Module import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
# Remove Unicode warning
plt.rcParams['axes.unicode_minus']=False
# Set a font for Korean
plt.rcParams['font.family'] = "NanumGothic"
# Set an output size for graph
plt.rcParams["figure.figsize"] = (12, 10)

# Scatterplot
# Generate a random value between 0 and 1
np.random.rand(50)

# Setting x, y, colors, and area
  # Colors are random values that are converted into color values.
  # Area represents the size of the points; as the value increases, the area also increases

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.arange(50)
area = x * y * 250

plt.scatter(x, y, s=area, c=colors)
plt.show()

# Color & Alpha
# If one specifies a color for color, all points will have the same color.
# The alpha value represents transparency and can be set between 0 and 1, 
# where values closer to 0 are more transparent

np.random.rand(50)

plt.figure(figsize=(12, 6))

plt.subplot(131)
plt.scatter(x, y, s=area, color='purple', alpha=0.1)
plt.title('alpha=0.1')

plt.subplot(132)
plt.title('alpha=0.5')
plt.scatter(x, y, s=area, color='purple', alpha=0.5)

plt.subplot(133)
plt.title('alpha=1.0')
plt.scatter(x, y, s=area, color='purple', alpha=1.0)

plt.show()

# Barplot, Barhplot
# Drawing multiple graphs on a single canvas

# Create Barplot
x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
y = [66, 80, 60, 50, 80, 10]

plt.figure(figsize=(6, 3))
# plt.bar(x, y)
plt.bar(x, y, align='center', alpha=0.7, color='red')
plt.xticks(x)
plt.ylabel('Number of Students')
plt.title('Subjects')

plt.show()

# Barh plot (axis transformation)
# In the barh function, the xticks setting is changed to yticks
x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
y = [66, 80, 60, 50, 80, 10]

plt.barh(x, y, align='center', alpha=0.7, color='green')
plt.yticks(x)
plt.xlabel('Number of Students')
plt.title('Subjects')

plt.show()

# Drawing a comparison graph using a Bar plot
x_label = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
x = np.arange(len(x_label))
y_1 = [66, 80, 60, 50, 80, 10]
y_2 = [55, 90, 40, 60, 70, 20]

# Specify width
width = 0.35

# Create subplots
fig, axes = plt.subplots()

# Set area
axes.bar(x - width/2, y_1, width, align='center', alpha=0.5)
axes.bar(x + width/2, y_2, width, align='center', alpha=0.8)

# Set xtick
plt.xticks(x)
axes.set_xticklabels(x_label)
plt.ylabel('Number of Students')
plt.title('Subjects')

plt.legend(['john', 'peter'])

plt.show()


x_label = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
x = np.arange(len(x_label))
y_1 = [66, 80, 60, 50, 80, 10]
y_2 = [55, 90, 40, 60, 70, 20]

# Specify width
width = 0.35

# Create subplots
fig, axes = plt.subplots()

# Set area
axes.barh(x - width/2, y_1, width, align='center', alpha=0.5, color='green')
axes.barh(x + width/2, y_2, width, align='center', alpha=0.8, color='red')

# Set xtick
plt.yticks(x)
axes.set_yticklabels(x_label)
plt.xlabel('Number of Students')
plt.title('Subjects')
plt.legend(['john', 'peter'])
plt.show()

# Line Plot
# Create basic lineplot
x = np.arange(0, 10, 0.1)
y = 1 + np.sin(x)

plt.plot(x, y)

plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin graph', fontsize=18)

plt.grid()

plt.show()

# Drawing more than two graphs
  # color: Color option
  # alpha: Transparency option
x = np.arange(0, 10, 0.1)
y_1 = 1 + np.sin(x)
y_2 = 1 + np.cos(x)

plt.plot(x, y_1, label='1+sin', color='blue', alpha=0.3)
plt.plot(x, y_2, label='1+cos', color='red', alpha=0.7)

plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin and cos graph', fontsize=18)

plt.grid()
plt.legend()

plt.show()

# Marker styling
  # marker: marker option
x = np.arange(0, 10, 0.1)
y_1 = 1 + np.sin(x)
y_2 = 1 + np.cos(x)

plt.plot(x, y_1, label='1+sin', color='blue', alpha=0.3, marker='o')
plt.plot(x, y_2, label='1+cos', color='red', alpha=0.7, marker='+')

plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin and cos graph', fontsize=18)

plt.grid()
plt.legend()

plt.show()

# Change line style
  # linestyle: Line style change options
x = np.arange(0, 10, 0.1)
y_1 = 1 + np.sin(x)
y_2 = 1 + np.cos(x)

plt.plot(x, y_1, label='1+sin', color='blue', linestyle=':')
plt.plot(x, y_2, label='1+cos', color='red', linestyle='-.')

plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin and cos graph', fontsize=18)

plt.grid()
plt.legend()

plt.show()

# Areaplot (Filled Area)
# In matplotlib, to draw an area plot, the fill_between function is used
y = np.random.randint(low=5, high=10, size=20)
y

# Draw basic areaplot
x = np.arange(1,21)
y = np.random.randint(low=5, high=10, size=20)

# Color using fill_between
plt.fill_between(x, y, color="green", alpha=0.6)
plt.show()

# Apply the effect of drawing the boundary line thickly and making the area light
plt.fill_between(x, y, color="green", alpha=0.3)
plt.plot(x, y, color="green", alpha=0.8)

# Overlaying multiple graphs
x = np.arange(1, 10, 0.05)
y_1 = np.cos(x)+1
y_2 = np.sin(x)+1
y_3 = y_1 * y_2 / np.pi

plt.fill_between(x, y_1, color="green", alpha=0.1)
plt.fill_between(x, y_2, color="blue", alpha=0.2)
plt.fill_between(x, y_3, color="red", alpha=0.3)

# Histogram
# Create basic Histogram
N = 100000
bins = 30

x = np.random.randn(N)

plt.hist(x, bins=bins)

plt.show()

# sharey: Multiple graphs share the y-axis
# tight_layout: Automatically adjusts the padding of the graphs to create a well-fitted layout

# Multiple histograms and changing the size of the bins
N = 100000
bins = 30

x = np.random.randn(N)
fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=True)

fig.set_size_inches(12, 5)

axs[0].hist(x, bins=bins)
axs[1].hist(x, bins=bins*2)
axs[2].hist(x, bins=bins*4)

plt.show()

# Displaying Density on the Y-axis
N = 100000
bins = 30

x = np.random.randn(N)
fig, axs = plt.subplots(1, 2, tight_layout=True)
fig.set_size_inches(9, 3)

# Can display density on y-axis through the value of density=True
axs[0].hist(x, bins=bins, density=True, cumulative=True)
axs[1].hist(x, bins=bins, density=True)

plt.show()

# Pie Chart
# pie chart option
  # explode: The proportion of the pie that appears to pop out.
    # autopct: Automatically display the percentage.
    # shadow: Display a shadow behind the pie.
    # startangle: The angle to start drawing the pie.
  # Returns texts and autotexts arguments.

# texts are used to handle text effects for labels,
# and autotexts are used when handling text effects drawn on the pie itself.

labels = ['Samsung', 'Huawei', 'Apple', 'Xiaomi', 'Oppo', 'Etc']
sizes = [20.4, 15.8, 10.5, 9, 7.6, 36.7]
explode = (0.3, 0, 0, 0, 0, 0)

# Apply text styling using texts, autotexts arguments
patches, texts, autotexts = plt.pie(sizes,
explode=explode,
labels=labels,
autopct='%1.1f%%',
shadow=True,
startangle=90)

plt.title('Smartphone pie', fontsize=15)

# Applying styles to label text
for t in texts:
  t.set_fontsize(12)
  t.set_color('gray')

# Applying styles to texts on pie
for t in autotexts:
  t.set_color("white")
  t.set_fontsize(10)

plt.show()

# Box Plot
# Create sample data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))

# Create basic boxplot
plt.boxplot(data)
plt.tight_layout()
plt.show()

# Switching the axis of a Box Plot
# One can change the axis one wants to display by using the vert=False option.
plt.title('Horizontal Box Plot', fontsize=15)
plt.boxplot(data, vert=False)

plt.show()

# Changing Outlier marker symbol and color
outlier_marker = dict(markerfacecolor='r', marker='D')

plt.title('Changed Outlier Symbols', fontsize=15)
plt.boxplot(data, flierprops=outlier_marker)

plt.show()

# 3D graph
# To draw 3D graphs, one needs to additionally import mplot3d

from mpl_toolkits import mplot3d

# Drawing baseline (canvas)
fig = plt.figure()
ax = plt.axes(projection='3d')

# Drawing 3d plot
# Set project=3d
ax = plt.axes(projection='3d')

# Create x, y, z data
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)

ax.plot3D(x, y, z, 'gray')
plt.show()


# Set project=3d
ax = plt.axes(projection='3d')

sample_size = 100
x = np.cumsum(np.random.normal(0, 1, sample_size))
y = np.cumsum(np.random.normal(0, 1, sample_size))
z = np.cumsum(np.random.normal(0, 1, sample_size))

# Add marker
ax.plot3D(x, y, z, alpha=0.6, marker='o')

plt.title("ax.plot")
plt.show()

# 3d-scatter
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d') # Axe3D object

sample_size = 500

x = np.cumsum(np.random.normal(0, 5, sample_size))
y = np.cumsum(np.random.normal(0, 5, sample_size))
z = np.cumsum(np.random.normal(0, 5, sample_size))

ax.scatter(x, y, z, c = z, s=20, alpha=0.5, cmap='Greens')

plt.title("ax.scatter")
plt.show()


# Drawing 3D contour plots (contour3D)
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
x, y = np.meshgrid(x, y)

z = np.sin(np.sqrt(x**2 + y**2))

fig = plt.figure(figsize=(12, 6))
ax = plt.axes(projection='3d')

ax.contour3D(x, y, z, 20, cmap='Reds')

plt.title("ax.contour3D")
plt.show()

# imshow
# When visualizing image data in array format, use imshow
import matplotlib.image as mpimg
from PIL import Image
import urllib

# Download sample image
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/png/img6.png'
image_data = Image.open(urllib.request.urlopen(url))
image_data

img = np.asarray(image_data)
img[:5, :5, 0]

plt.imshow(img)
plt.show()












