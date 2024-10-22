# An example of basic canvas drawing and styling with matplotlib.pyplot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import warnings
warnings.filterwarnings('ignore')
# Remove Unicode warning
plt.rcParams['axes.unicode_minus']=False
# Set a font for Korean
plt.rcParams['font.family'] = "NanumGothic"
# Set an output size for a graph
plt.rcParams["figure.figsize"] = (12, 8)

# Creating a single graph
# Data creation
data = np.arange(1, 100)

# Plot
plt.plot(data)

# Code to display the graph
plt.show()

# Multiple Graphs
# Create graphs in one canvas
data = np.arange(1, 51)
plt.plot(data)
data2 = np.arange(51, 101)
# plt.figure()
plt.plot(data2)
plt.show()

# Drawing multiple graphs by dividing into two figures
# figure() creates a new graph canvas.

data = np.arange(100, 201)
plt.plot(data)
data2 = np.arange(200, 301)
# figure() creates a new graph
plt.figure()
plt.plot(data2)
plt.show()

# How to create multiple plots (subplot)
# plt.subplot(row, column, index)
data = np.arange(100, 201)
plt.subplot(2, 1, 1)
plt.plot(data)

data2 = np.arange(200, 301)
plt.subplot(2, 1, 2)
plt.plot(data2)

plt.show()

# Or
# Same code as above, but without the commas
data = np.arange(100, 201)

# One can omit the comma and write with row, column, index
# 211 -> row: 2, col: 1, index: 1
plt.subplot(211)
plt.plot(data)

data2 = np.arange(200, 301)
plt.subplot(212)
plt.plot(data2)

# Display the plot
plt.show()



data = np.arange(100, 201)
plt.subplot(1, 3, 1)
plt.plot(data)
data2 = np.arange(200, 301)
plt.subplot(1, 3, 2)
plt.plot(data2)
data3 = np.arange(300, 401)
plt.subplot(1, 3, 3)
plt.plot(data3)
plt.show()

# Method for drawing multiple plots (subplots) - Note the additional 's'.
# plt.subplots(number of rows, number of columns)
data = np.arange(1, 51)
# data creation

# Baseline drawing
fig, axes = plt.subplots(2, 3)

axes[0, 0].plot(data)
axes[0, 1].plot(data * data)
axes[0, 2].plot(data ** 3)
axes[1, 0].plot(data % 10)
axes[1, 1].plot(-data)
axes[1, 2].plot(data // 20)

plt.tight_layout()
plt.show()

# Main style option
# Title
plt.plot([1, 2, 3], [3, 6, 9])
plt.plot([1, 2, 3], [2, 4, 9])

# Set title & font
plt.title('This is a title')
plt.show()

# Adjusting font size
plt.plot([1, 2, 3], [3, 6, 9])
plt.plot([1, 2, 3], [2, 4, 9])
# Set title & font
plt.title('Title - increasing font size', fontsize=20)
plt.show()

# Setting labels for x axis and y axis
plt.plot([1, 2, 3], [3, 6, 9])
plt.plot([1, 2, 3], [2, 4, 9])
# Set title & font
plt.title('An example for setting Labels', fontsize=20)
# Setting labels for X axis & Y axis
plt.xlabel('X-axis', fontsize=20)
plt.ylabel('Y-axis', fontsize=20)
plt.show()

# Setting Ticks for X axis and Y axis (rotation)
# Ticks refer to the marks located on the X and Y axes
plt.plot(np.arange(10), np.arange(10)*2)
plt.plot(np.arange(10), np.arange(10)**2)
plt.plot(np.arange(10), np.log(np.arange(10)))

# Set title & font
plt.title('Adjust X, Y Tick', fontsize=20)

# Set labels for X-axis & Y-axis
plt.xlabel('X-axis', fontsize=20)
plt.ylabel('Y-axis', fontsize=20)

# Set X tick, Y tick
plt.xticks(rotation=90)
plt.yticks(rotation=30)

plt.show()

# Set Legend
plt.plot(np.arange(10), np.arange(10)*2)
plt.plot(np.arange(10), np.arange(10)**2)
plt.plot(np.arange(10), np.log(np.arange(10)))

# Set title & font
plt.title('An example for setting legend', fontsize=20)

# Set labels for X-axis & Y-axis
plt.xlabel('X-axis', fontsize=20)
plt.ylabel('Y-axis', fontsize=20)

# Set X tick, Y tick
plt.xticks(rotation=90)
plt.yticks(rotation=30)

# Set legend
plt.legend(['10 * 2', '10 ** 2', 'log'], fontsize=15)

plt.show()

# Set the limit of X & Y
plt.plot(np.arange(10), np.arange(10)*2)
plt.plot(np.arange(10), np.arange(10)**2)
plt.plot(np.arange(10), np.log(np.arange(10)))

# Set title & font
plt.title('This is a title', fontsize=20)

# Set labels for X-axis & Y-axis
plt.xlabel('X-axis', fontsize=20)
plt.ylabel('Y-axis', fontsize=20)

# Set X tick, Y tick
plt.xticks(rotation=90)
plt.yticks(rotation=30)

# Set legend
plt.legend(['10 * 2', '10 ** 2', 'log'], fontsize=15)

# Set x, y limit
plt.xlim(0, 5)
plt.ylim(0.5, 10)

plt.show()

# Detailed style settings - Marker, Line, Color
# Detailed style settings include marker type, line type, and color, 
# and these can be configured using strings

# Types of markers:
  # '.' : point marker
  # ',' : pixel marker
  # 'o' : circle marker
  # 'v' : triangle_down marker
  # '^' : triangle_up marker
  # '<' : triangle_left marker
  # '>' : triangle_right marker
  # '1' : tri_down marker
  # '2' : tri_up marker
  # '3' : tri_left marker
  # '4' : tri_right marker
  # 's' : square marker
  # 'p' : pentagon marker
  # '*' : star marker
  # 'h' : hexagon1 marker
  # 'H' : hexagon2 marker
  # '+' : plus marker
  # 'x' : x marker
  # 'D' : diamond marker
  # 'd' : thin_diamond marker
  # '|' : vline marker
  # '_' : hline marker

plt.plot(np.arange(10), np.arange(10)*2, marker='o', markersize=5)
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', markersize=10)
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', markersize=15)
plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', markersize=20)

#  Set title & font
plt.title('An example for setting a marker', fontsize=20)

#  Set labels for X-axis & Y-axis
plt.xlabel('X-axis', fontsize=20)
plt.ylabel('Y-axis', fontsize=20)

# Set X tick, Y tick
plt.xticks(rotation=90)
plt.yticks(rotation=30)

plt.show()

# Types of line:
  # '-' : solid line style
  # '--' : dashed line style
  # '-.' : dash-dot line style
  # ':' : dotted line style

plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='')
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='o', linestyle='-')
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='v', linestyle='--')

plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='+', linestyle='-.')
plt.plot(np.arange(10), np.arange(10)*2 - 40, marker='*', linestyle=':')

# Set title & font
plt.title('An example of different types of line', fontsize=20)

# Set labels for X-axis & Y-axis
plt.xlabel('X-axis', fontsize=20)
plt.ylabel('Y-axis', fontsize=20)

# Set X tick, Y tick
plt.xticks(rotation=90)
plt.yticks(rotation=30)

plt.show()

# Types of color
  # 'b' : blue
  # 'g' : green
  # 'r' : red
  # 'c' : cyan
  # 'm' : magenta
  # 'y' : yellow
  # 'k' : black
  # 'w' : white

plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='-', color='b')
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', linestyle='--', color='c')
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', linestyle='-.', color='y')
plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', linestyle=':', color='r')

# Set title & font
plt.title('An example for setting color', fontsize=20)

# Set X-axis & Y-axis Label
plt.xlabel('X-axis', fontsize=20)
plt.ylabel('Y-axis', fontsize=20)

# Set X tick, Y tick
plt.xticks(rotation=90)
plt.yticks(rotation=30)

plt.show()

plt.plot(np.arange(10), np.arange(10)*2, color='b', alpha=0.1)
plt.plot(np.arange(10), np.arange(10)*2 - 10, color='b', alpha=0.3)
plt.plot(np.arange(10), np.arange(10)*2 - 20, color='b', alpha=0.6)
plt.plot(np.arange(10), np.arange(10)*2 - 30, color='b', alpha=1.0)

# Set title & font
plt.title('An example for setting transparency (alpha)', fontsize=20)

# Set X-axis & Y-axis Label
plt.xlabel('X-axis', fontsize=20)
plt.ylabel('Y-axis', fontsize=20)

# Set X tick, Y tick
plt.xticks(rotation=90)
plt.yticks(rotation=30)

plt.show()

# Grid
plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='-', color='b')
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', linestyle='--', color='c')
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', linestyle='-.', color='y')
plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', linestyle=':', color='r')

# Set title & font
plt.title('An example for setting grid', fontsize=20)

# Set X-axis & Y-axis Label
plt.xlabel('X-axis', fontsize=20)
plt.ylabel('Y-axis', fontsize=20)

# Set X tick, Y tick
plt.xticks(rotation=90)
plt.yticks(rotation=30)

# Add grid option
plt.grid()

plt.show()

# Setting annotate
plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='-', color='b')
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', linestyle='--', color='c')
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', linestyle='-.', color='y')
plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', linestyle=':', color='r')

# Set title & font
plt.title('An example for setting grid', fontsize=20)

# Set X-axis & Y-axis Label
plt.xlabel('X-axis', fontsize=20)
plt.ylabel('Y-axis', fontsize=20)

# Set X tick, Y tick
plt.xticks(rotation=90)
plt.yticks(rotation=30)

# Set annotate
plt.annotate('The point where the COVID-19 outbreak began', xy=(3, -20), xytext=(3, -25), arrowprops=dict

# Add grid option
plt.grid()
             
plt.show()













