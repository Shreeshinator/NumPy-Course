import numpy as np

# arithmetic operations on numpy arrays (scalar operations)
arr = np.array([1,2,3])
print(arr + 1) # adding a scalar to each element
print(arr * 2) # multiplying each element by a scalar
print(arr / 2) # dividing each element by a scalar
print(arr ** 2) # squaring each element

#vectorized operations (element-wise operations between arrays)
arr1 = np.array([1,2,3])
print("Vectorized operations:")
print(np.square(arr1), end=" ") # using numpy's square function for element-wise squaring
print(arr1.round(2), end=" ") # using numpy's round function for element-wise rounding