# Pandas Cheat Sheet
This is a collection of common pandas code used while performing Data Analysis

```python
import pandas as pd
import numpy as np
```
## Handling csv files
- Create a DataFrame from a csv file
```python
csvFilePath = '/path/to/file.csv'
with open (csvFilePath, 'rb') as file:
    dataFrameName = pd.read_csv(file)
```

- Create a DataFrame from a csv file, explicitly definining the file encoding and dtype for each column. note: check sparse and array dtypes not included here.
```python
csvFilePath = '/path/to/file.csv'
with open (csvFilePath, 'rb') as file:
    dataFrameName = pd.read_csv(file, encoding = 'UTF-8',
                                    thousands = ',',
                                    decimal = '.',
                                    dtype = {
                                            'column1name':'float64',
                                            'column2name':'int64',
                                            'column3name':'datetime64',
                                            'column4name':'string',
                                            'column5name':'boolean',
                                            'column6name':'category'
                                            }
                                )
```

- Use convertions while importing data, ie: change a string column like '67%' to float
```python
## define convertion function
def percentToFloat(percent_string):
    return float(percent_string.strip('%'))/100
    
## pass converters parameters in dictionary form
csvFilePath = '/path/to/file.csv'
with open (csvFilePath, 'rb') as file:
    dataFrameName = pd.read_csv(file, encoding = 'UTF-8',
                                    thousands = ',',
                                    decimal = '.',
                                    converters = {
                                                 'column4':percentToFloat,
                                                 'column5':percentToFloat
                                                 }
                                                    
                                    dtype = {
                                            'column1name':'float64',
                                            'column2name':'int64',
                                            'column3name':'datetime64',
                                            'column6name':'category'
                                            } 
                                            # columns 4 and 5 were no longer on the dtype dict
                                )
```

- Export DataFrame to csv
```python
csvFilePath = '/path/to/file.csv' #file.csv should't exist, otherwise you would overwrite
dataFrameName.to_csv(csvFilePath)
```

## "manual" DataFrame creation
- Empty DataFrame
```python
dataFrameName = np.DataFrame()
```
- From a list of dicts (example)
```python
myFriends = pd.DataFrame([
                            {'name':'friendName1',
                            'age':21,
                            'straight':True,
                            'sex':'male'
                            },
                            {'name':'friendName2',
                            'age':20,
                            'straight':False,
                            'sex':'female'
                            },
                            {'name':'friendName3',
                            'age':21,
                            'straight':True,
                            'sex':'female'
                            }
                        ])
```

## Data Frame Info
- Quick view at first elements (default 5 of the DataFrame)
```python
pd.dataFrameName.head()
pd.dataFrameName.head(n=10)
```

- Create a DataFrame describing the dtypes of each of the columns that are part of another dataframe
```python
columnTypes= {}
for column in dataFrameName.columns:
    columnTypes.update({dataFrameName[column].name : dataFrameName[column].dtype})
columnTypes = pd.DataFrame(columnTypes.items(), columns=['column','type'])
```

- DataFrame shape, without considering column labels or row index
```python
pd.dataFrameName.shape()
```

- DataFrame elements quantity, without considering column labels or row index
```python
pd.dataFrameName.size()
```

- Create a new dataFrame a selection of another dataframe columns


## Getting Stats
- Summary stats of numeric columns in a DataFrame
```python
dataFrameName.describe()
```
- Summary stats of an specific column
```python
dataFrameName['columnName'].describe()
```

## Manipulation
- Changing column names
```python
dataFrameName.columns = ['column0newName','column1newName','column2newName','column3newName']
```

- Adding columns to a DataFrame
```python
### empty one:
dataFrameName[newColumnName]=''
### fixed value
dataFrameName[newColumnName2]='myValue'
### as the result of the operation of other columns
dataFrameName[newColumnName3]=(dataFrameName[column3]/dataFrameName[column5])**2
```
- Create a new DataFrame as the selection of another DataFrame columns
```python
newDataFrame = dataFrame[['column1','column2','columnn']]
```

- Change a percent string to float
```python
dataFrameName['columnName'] = dataFrameName['columnName'].str.rstrip('%').astype('float') / 100.0
```

- Filtering
    - By a few elements
    ```python
    condition = dataFrameName['columnName'].isin(['element1', 'element2', 'elementn'])
    newDataFrameName = dataFrameName[condition] 
    ```

    - By elements
    ```python
    elementsToFilter = ['element1',
                        'element2',
                        'elementn']
    condition = dataFrameName['columnName'].isin(elementsToFilter)
    newDataFrameName = dataFrameName[condition] 
    ```
    - By matching criteria
    ```python
    condition = dataFrameName['columnName'] == True
    newDataFrameName = dataFrameName[condition] 
    ```
    
    - By eliminating data below and above certain percentiles (ie, 5 and 95
    ```python
    columnNamep05 =  np.percentile(dataFrameName['columnName'].to_numpy(),5)
    columnNamep95 =  np.percentile(dataFrameName['columnName'].to_numpy(),95)
    condition = ((dataFrameName['columnName'] > columnNamep05) & (dataFrameName['columnName'] > columnNamep95))
    newDataFrameName = dataFrameName[condition]
    ```