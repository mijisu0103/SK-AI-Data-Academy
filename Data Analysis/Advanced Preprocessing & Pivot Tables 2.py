# Advanced practice problems by chapter
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import glob
# set floating point formatting
pd.options.display.float_format ='{:,.1f}'.format

# Q4
# Range
# Include previous content
# groupby(), pivot_table()

# Dataset
taxis = sns.load_dataset('taxis')
taxis.head()

# Calculate the average of 'distance' by day of the week from the taxis dataset (output in DataFrame format).
# [Note] 0: Monday ~ 6: Sunday

taxis['dayofweek'] = taxis['pickup'].dt.dayofweek
tmp = taxis.groupby('dayofweek')['distance'].mean().reset_index()

# "Based on the statistics calculated above:
  # have obtained the average values of 'distance' by day of the week. 
  # Extract only the data where the values are less than the calculated average for each day of the week. 
  # e.g. If the average 'distance' for Monday (0) is 3.215971, extract only the data that is less than 3.215971.
    # (This applies to all days from Monday to Sunday)
  # After filtering, calculate the median and standard deviation (std) for 'distance', 'fare', and 'tip'."

def is_small(x):
  return x['distance'] < tmp.loc[x['dayofweek'], 'distance']

cond1 = taxis.apply(is_small, axis=1)
cond2 = taxis['passengers'] <= 2
taxis.loc[cond1 & cond2, ['distance', 'fare', 'tip']].agg(['median', 'std'])

# Complete the following pivot table.
# Calculate the median and standard deviation (std) of 'fare' by day of the week (dayofweek) 
# and payment method
taxis.pivot_table(index='dayofweek', columns='payment', values='fare', aggfunc=['median', 'std'])


















