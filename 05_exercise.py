import numpy as np

radii = np.array([1, 2, 3]) # array of radi
print("Radii:", radii)
# Calculate the area of circles with the given radii
areas = np.pi * radii ** 2 # using numpy's pi constant and element-wise squaring
print("Areas of circles:", areas)

# Element-wise operations between arrays

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("Element-wise addition:", arr1 + arr2) # adding two arrays element-wise