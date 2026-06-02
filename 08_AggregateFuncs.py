import numpy as np

# Aggregate functions in numpy are used to perform operations on arrays that return a single value, such as sum, mean, min, max, etc.
#  These functions can be applied to the entire array or along a specific axis.

array = np.array([[1, 2, 3, 4, 5], 
                  [6, 7, 8, 9, 10]]) # 2D array

print("Sum:", np.sum(array)) # Sum of all elements in the array
print("Mean:", np.mean(array)) # Mean of all elements in the array
print("Standard deviation:", np.stdev(array)) # Standard deviation of all elements in the array
print("Index of minimum value:", np.argmin(array)) # Index of the minimum value in the array
print("Index of maximum value:", np.argmax(array)) # Index of the maximum value in the array
print("Sum along columns:", np.sum(array, axis=0)) # Sum along columns (axis 0)
print("Sum along rows:", np.sum(array, axis=1)) # Sum along rows (