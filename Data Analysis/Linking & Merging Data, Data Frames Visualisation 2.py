# Advanced practice problems by chapter
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os
# set floating point formatting
pd.options.display.float_format ='{:,.1f}'.format
root_dir = '/path/dataset/restaurant'

# Q5
sorted(glob.glob(os.path.join(root_dir, "*")))
['/path/dataset/restaurant/chefmozaccepts.csv',
'/path/dataset/restaurant/chefmozcuisine.csv',
'/path/dataset/restaurant/chefmozhours4.csv',
'/path/dataset/restaurant/chefmozparking.csv',
'/path/dataset/restaurant/geoplaces2.csv',
'/path/dataset/restaurant/rating_final.csv',
'/path/dataset/restaurant/usercuisine.csv',
'/path/dataset/restaurant/userpayment.csv',
'/path/dataset/restaurant/userprofile.csv']

# Restaurants
  # chefmozaccepts.csv
  # chefmozcuisine.csv
  # chefmozhours4.csv
  # chefmozparking.csv
  # geoplaces2.csv

# Consumers
  # usercuisine.csv
  # userpayment.csv
  # userprofile.csv

# User-Item Rating
  # rating_final.csv

# Perform the following:
  # Merge the two datasets below.
  # After merging, group by smoking_area and check the data distribution for price (value_counts).
  # Output the result in a DataFrame format as shown below

# Dataset
chefmozaccepts = pd.read_csv(os.path.join(root_dir, 'chefmozaccepts.csv'))
geoplaces2 = pd.read_csv(os.path.join(root_dir, 'geoplaces2.csv'))

a = pd.merge(chefmozaccepts, geoplaces2).groupby('smoking_area')['price'].value_cou
a.name = 'values'
a.reset_index()

# Using userprofile.csv and rating_final.csv, perform the following: 
  # Merge rating_final.csv and userprofile.csv, 
  # then filter for those born between 1980 and 1989 (people born in the 1980s) 
  # based on birth_year. After filtering, calculate the average and standard deviation of rating.

# Dataset
userprofile = pd.read_csv(os.path.join(root_dir, 'userprofile.csv'))
rating_final = pd.read_csv(os.path.join(root_dir, 'rating_final.csv'))

merged = pd.merge(userprofile, rating_final)
cond = (merged['birth_year'] >= 1980) & (merged['birth_year'] <= 1989)
merged.loc[cond, 'rating'].agg(['mean', 'std'])

# Using the three datasets userprofile.csv, rating_final.csv, and geoplaces2.csv, perform the following:

  # Merge the three datasets based on userID and placeID to create one DataFrame.
"""
[Merge Guidelines]

Merge userprofile.csv and rating_final.csv using an inner join on userID.
Merge the previously merged DataFrame with geoplaces2.csv using a left join on placeID.
When merging, if there are common key values, specify on='placeID'.
Example: pd.merge(df1, df2, how='left', on='placeID')
Filtering Condition

In the merged DataFrame, filter based on the drink_level column where the data is 'social drinker'.
Then, calculate the average rating by city.
Output the result sorted in descending order.
"""

# Dataset
userprofile = pd.read_csv(os.path.join(root_dir, 'userprofile.csv'))
rating_final = pd.read_csv(os.path.join(root_dir, 'rating_final.csv'))
geoplaces2 = pd.read_csv(os.path.join(root_dir, 'geoplaces2.csv'))

merged = pd.merge(userprofile, rating_final, on='userID')
merged = pd.merge(merged, geoplaces2, how='left', on='placeID')
cond = (merged['drink_level'] == 'social_drinker')
merged.loc[cond].groupby('city')['rating'].mean().reset_index().sort_values('rating', ascending=False)
