# Import pandas and numpy modules
import pandas as pd
import numpy as np

# Given dictionary data and labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
              'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# a. Create and display a DataFrame with index labels
df = pd.DataFrame(exam_data, index=labels)
print("a) DataFrame created from dictionary with labels:\n")
print(df)

# b. Change the name 'James' to 'Suresh' in the 'name' column
df.loc[df['name'] == 'James', 'name'] = 'Suresh'
print("\n\nb) After changing 'James' to 'Suresh':\n")
print(df)

# c. Insert a new column in existing DataFrame
df['age'] = [20, 21, 19, 18, 22, 20, 19, 23, 21, 20]
print("\n\nc) After inserting a new column 'age':\n")
print(df)

# d. Get list of DataFrame column headers
columns_list = list(df.columns)
print("\n\nd) List of DataFrame column headers:\n")
print(columns_list)
