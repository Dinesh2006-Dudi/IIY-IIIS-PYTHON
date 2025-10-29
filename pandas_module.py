# Import pandas module
import pandas as pd

# a. Create and display a one-dimensional array-like object (Series)
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Pandas Series:")
print(series)

# b. Convert the Pandas Series to a Python list and display its type
python_list = series.tolist()
print("\nConverted to Python list:")
print(python_list)

print("\nType of converted object:", type(python_list))
