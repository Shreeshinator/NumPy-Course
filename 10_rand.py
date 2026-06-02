import numpy as np

rng = np.random.default_rng() # Create a random number generator
np.integer  = rng.integers(1, 7) # Generate a random integer between 1 and 10
int_array = rng.integers(1, 10, size=(3, 4)) # Generate a 3x4 array of random integers between 1 and 10
print("Random integer:", np.integer) # Print the random integer
print("Integer array:", int_array) # Print the integer array