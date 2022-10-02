# Import
```py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series

%matplotlib inline
%load_ext autoreload
%autoreload 2

# from __future__ import division
from import_file import *
from helpers.parallel_helper import *
load_libs()

```
# Input
```py
df = DataFrame()

#CSV
df = pd.read_csv('file.csv')
df = pd.read_csv('file.csv', header=0, index_col=0, quotechar='"',sep=':', na_values = ['na', '-', '.', ''])
# specifying "." and "NA" as missing values in the Last Name column and "." as missing values in Pre-Test Score column
df = pd.read_csv('../data/example.csv', na_values={'Last Name': ['.', 'NA'], 'Pre-Test Score': ['.']}) 
df = pd.read_csv('../data/example.csv', na_values=sentinels, skiprows=3)    # skipping the top 3 rows
df = pd.read_csv('../data/example.csv', thousands=',')  # interpreting "," in strings around numbers as thousands separators

# CSV (Inline)
from io import StringIO
data = """, Animal, Cuteness, Desirable
row-1, dog, 8.7, True
row-2, cat, 9.5, True
row-3, bat, 2.6, False"""
df = pd.read_csv(StringIO(data),
	header=0, index_col=0,
	skipinitialspace=True)

# JSON
import json
json_data = open('data-text.json').read()
data = json.loads(json_data)
for item in data:
    print item

# XML
from xml.etree import ElementTree as ET
tree = ET.parse('../../data/chp3/data-text.xml')
root = tree.getroot()
print root
data = root.find('Data')
all_data = []
for observation in data:
    record = {}
    for item in observation:
        lookup_key = item.attrib.keys()[0]
        if lookup_key == 'Numeric':
            rec_key = 'NUMERIC'
            rec_value = item.attrib['Numeric']
        else:
            rec_key = item.attrib[lookup_key]
            rec_value = item.attrib['Code']
        record[rec_key] = rec_value
    all_data.append(record)
print all_data

# Excel
workbook = pd.ExcelFile('file.xlsx') 
d = {} # start with an empty dictionary
for sheet_name in workbook.sheet_names:   # Each Excel sheet in a Python dictionary
	df = workbook.parse(sheet_name)
	d[sheet_name] = df

# MySQL
import pymysql
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://'
+'USER:PASSWORD@HOST/DATABASE')
df = pd.read_sql_table('table', engine)
(<a href="#top">Back to top</a>)



### Combine DataFrame
Data in Series then combine into a DataFrame
```python
# Example 1 ...
s1 = Series(range(6))
s2 = s1 * s1
s2.index = s2.index + 2# misalign indexes
df = pd.concat([s1, s2], axis=1)
# Example 2 ...
s3 = Series({'Tom':1, 'Dick':4, 'Har':9})
s4 = Series({'Tom':3, 'Dick':2, 'Mar':5})
df = pd.concat({'A':s3, 'B':s4 }, axis=1)
```

# Output
```py
# CSV
df.to_csv('name.csv', encoding='utf-8')

# Excel
from pandas import ExcelWriter
writer = ExcelWriter('filename.xlsx')
df1.to_excel(writer,'Sheet1')
df2.to_excel(writer,'Sheet2')
writer.save()

# MySQL
import pymysql
from sqlalchemy import create_engine
e = create_engine('mysql+pymysql://' +
	'USER:PASSWORD@HOST/DATABASE')
df.to_sql('TABLE',e, if_exists='replace')

# Python object
d = df.to_dict() # to dictionary
str = df.to_string() # to string
m = df.as_matrix() # to numpy matrix
```
