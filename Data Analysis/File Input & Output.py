# Module Import
from IPython.display import Image
import numpy as np
import pandas as pd

Data Download
from opendata import dataset

# Dataset Download
dataset.download('Seoul Public Transportation')
dataset.download('Seoul Resident Population Registration')

# Excel
# Importing Excel
"""
To read Excel data directly into a pandas DataFrame and specify a particular sheet, one can use the pd.read_excel() function. 
If one encounters errors when loading the data, adding engine='openpyxl' can often resolve these issues.
"""

excel = pd.read_excel('path/seoul_transportation.xlsx', sheet_name='railway')
excel.head()

excel = pd.read_excel('path/seoul_transportation.xlsx', sheet_name='bus') excel.head()

# If one specifies sheet_name as None, it will retrieve all sheets from the Excel file. 
# When fetching, it is returned as an OrderedDict, and one can use keys() to view the sheet names.
excel = pd.read_excel('path/seoul_transportation.xlsx', sheet_name=None)
excel

# To retrieve the sheet names from the Excel file after loading all sheets into an OrderedDict, 
# one can use the keys() method.
excel.keys()

dict_keys(['railway', 'bus'])

excel['railway].head()

excel['bus'].head()

# Excel - Save
"""
One can save a DataFrame to an Excel file and specify the filename. 
The index=False option is highly recommended; if not specified, the index will be saved as a separate column. 
One can also specify sheet_name to change the name of the sheet being saved.
"""

excel = pd.read_excel('path/seoul_transportation.xlsx', sheet_name='railway') 
excel.head()

# Saving without specified sheet_name
excel.to_excel('sample.xlsx', index=True)

# Saving specifying sheet_name as sample
excel.to_excel('sample1.xlsx', index=False, sheet_name='sample')

# CSV (Comma Separated Values)
"""
Each line corresponds to a single row, and commas (,) are used to separate the columns. 
Compared to Excel, CSV files are much lighter and take up less space, which is why most file data is provided in CSV format.
"""

# CSV - Importing
df = pd.read_csv('path/seoul_population.csv')
df

# CSV - Saving
# Way to save CSV files is similar to excel. However, for CSV file format, it does not have sheet_name
df = pd.read_csv('data/seoul_population.csv')

# Can save files in CSV file format using to_csv()
df.to_csv('sample.csv', index=False)

# Can save imported Excel file as CSV
excel = pd.read_excel('path/seoul_transportation.xlsx', sheet_name='bus', engine='openpyxl')
excel.head()

excel.to_csv('sample1.csv', index=False)

#JSON (JavaScript Object Notation)
"""
JSON (JavaScript Object Notation) is an abbreviation for a lightweight data interchange format that is widely used for storing or transmitting data. 
It has a small size and its structure is intuitive, making it commonly used for data transfer.
"""

import pprint
import json
import requests
# USD Exchange Rate Info Live Request API
# Return result format as JSON
url = "https://api.exchangerate-api.com/v4/latest/USD"
# Request live data using API
ret = requests.get(url)
# Load file in JSON format 
json_data = json.loads(ret.text)
# 출력 
pprint.pprint(json_data)

# Loading JSON format file
# The read_json() function can accept both an API URL that returns JSON format and a file path.

# Load file using read_json
df = pd.read_json(url) 
df

# Save file in JSON format
df.to_json('currency.json')

# Exercise
# Dataset Download
dataset.download('pandasinputoutput_sample')

# Read and load pth/file_sample.xlsx into sample variable
# Aftert loading, print all the sheets

sample = pd.read_excel('path/file_sample.xlsx', sheet_name=None) 
sample.keys()

dict_keys(['2020 Jan'], ['2020 Feb'], ['2020 Mar'], ['2020 Apr'], ['2020 May'], ['2020 Jun'], ['2020 Jul'], ['2020 Aug'], ['2020 Sep'], ['2020 Oct'], ['2020 Nov'], ['2020 Dec'])

# Load 2020 Oct sheet to sample_202010
sample_202010 = pd.read_excel('path/file_sample.xlsx', sheet_name='2020 Oct') 
sample_202010.head()

# Export sample_202010 to 2020-10-oil-price.csv
# Do not specify index
sample_202010.to_csv('2020-10-oil-price.csv', index = False)



