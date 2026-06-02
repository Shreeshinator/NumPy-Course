import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]) # 4x4 array

# array[start:stop:step] - slicing syntax
print(arr[::-2])# Slicing every second row in reverse order
print(arr[0:2,0:2]) # Slicing the top-left 2x2 subarray
print(arr[1:3,1:3]) # Slicing the middle 2x2 subarray