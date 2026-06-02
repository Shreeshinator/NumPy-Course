import pandas as pd 
# Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). 
# The axis labels are collectively referred to as the index.

data = [100, 102, 104, 200, 202]
series = pd.Series(data) # Create a Series from a list of data

print(series) # Print the Series

series_with_index = pd.Series(data, index=['a', 'b', 'c', 'd', 'e']) # Create a Series with custom index labels

print()
print(series_with_index) # Print the Series with custom index labels

print()
print(series.loc[0]) # Access the first element of the Series using .loc
# loc is location by index
series.loc[0] = 101 # Update the first element of the Series using .loc
print("After updating the first element to 101:")
print(series) # Print the updated Series

print(series[series > 150]) # Filter the Series 