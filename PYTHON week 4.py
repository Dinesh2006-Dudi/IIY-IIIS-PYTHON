1a,b
import pandas as pd
import numpy as np

# Create a Pandas Series from a list of data
data_list = pd.Series([10, 20, 30, 40, 50])

# Display the Series
print("Pandas Series created from a list:")
print(data_list)
# Convert the Series to a Python list
data_list = data_list.tolist()

# Display the list
print(data_list)

# Display the type of the new object
print("Type of the converted object:", type(data_list))



2 a b c d 
import pandas as pd
import numpy as np

# Sample Python dictionary data and list labels
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 1, 1, 2, 1, 1, 2],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'yes', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create the DataFrame with the specified data and index labels
df = pd.DataFrame(exam_data, index=labels)

# Display the DataFrame
print("DataFrame created from the dictionary:")
print(df)

# Change the name 'James' to 'Suresh' in the 'name' column
df.loc['d', 'name'] = 'Suresh'

# Display the updated DataFrame
print(df)

# Create a list of salaries
salaries = [50000, 60000, 75000, 45000, 55000, 80000, 70000, 48000, 62000, 78000]

# Insert the new column 'salary'
df['salary'] = salaries

# Display the DataFrame with the new column
print(df)

# Get the list of column headers
column_headers = df.columns.tolist()

# Display the list of headers
print(column_headers)