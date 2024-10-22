# Advanced practice problems by chapter
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import glob

# set floating point formatting
pd.options.display.float_format ='{:,.3f}'.format

# Q6
# Range
  # Include previous content
  # Visualisation

# To generate and visualize the data from rental.csv based on the instructions

# Requirements:
  # date: Time. Expressed as Year-Month-Day Hour:Minute (e.g., 2011-01-01 00:00:00 means January 1, 2011, at 00:00:00).
  # businessday: Workday. 1 indicates a workday, and 0 indicates a non-workday.
  # holiday: Holiday. 1 indicates a holiday, and 0 indicates a non-holiday.
  # season: Season. Expressed in the order of spring, summer, fall, and winter.
  # weather: Weather. Takes values between 1 and 4, 
  # specifically: 
    # 1: Clear weather 
    # 2: Slight fog and cloudy weather 
    # 3: Some snow, rain, or thunder 
    # 4: Heavy rain or hail
  # humid: Humidity
  # wind: Wind speed
  # temp: Temperature
  # sense_temp: Perceived temperature
  # onetime: Number of scooter rentals by non-members.
  # membership: Number of scooter rentals by members with a subscription.
  # count: Total number of scooter rentals. The sum of non-members (onetime) and members (membership) who rented scooters.

# Dataset
rental = pd.read_csv('/path/rental.csv')
rental.head()

# Generates a bar graph showing the average temperature by month from the date column
rental['date'] = pd.to_datetime(rental['date'])
rental['year'] = rental['date'].dt.year
rental['month'] = rental['date'].dt.month
rental['dayofweek'] = rental['date'].dt.dayofweek
rental['hour'] = rental['date'].dt.hour
rental.groupby('month')['temp'].mean().plot(kind='bar')

# Generate a bar graph of the average temperature by month, split by year
sns.barplot(x='month', y='temp', hue='year', data=rental)

# Generate a comparative bar graph of the monthly count, divided by year
sns.barplot(x='month', y='count', hue='year', data=rental)

# Visualize the rental count for 2011 as a boxplot by day of the week. 
# Similarly, visualize the rental count for 2012 as a boxplot by day of the week for comparison
fig, axes = plt.subplots(2, 1)
fig.set_size_inches(10, 5)

sns.boxplot(x='dayofweek', y='count', data=rental.loc[rental['year'] == 2011], ax=axes[0])
sns.boxplot(x='dayofweek', y='count', data=rental.loc[rental['year'] == 2012], ax=axes[1])
plt.show()

# Generate a point plot for the rental count in 2011, divided by hour and day of the week
plt.figure(figsize=(12, 6))
sns.pointplot(x='hour', y='count', hue='dayofweek', data=rental.loc[rental['year']

# Using the 2012 data, create a pivot table with month as the index and dayofweek as the columns for the wind data. 
# Then, output a heatmap using the following color map: cmap='coolwarm'
a = rental.loc[rental['year'] == 2012].pivot_table(index='month', columns='dayofweek', values='wind', aggfunc='mean')
plt.figure(figsize=(8, 8))
sns.heatmap(a, annot=True, cmap='coolwarm')
plt.show()

# Complete the correlation matrix for each feature in the rental DataFrame 
# and generate a heatmap using the following colormap: cmap='Greens'
plt.figure(figsize=(10,8))
sns.heatmap(rental.corr(), annot=True, cmap='Greens')
plt.show()

