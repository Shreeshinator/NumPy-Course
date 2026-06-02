import numpy as np

# Filtering in numpy is the process of selecting elements from an array based on certain conditions.
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65], 
                 [39, 22, 15, 99, 18, 19, 25, 40]]) # Array of ages

teenagers = ages[ages < 18] # Filter ages less than 18 (boolean indexing)
print("Teenagers:", teenagers) # Print the filtered array of teenagers
#>>>>>>>>> ARRAY IS NOW FLATENED TO 1D ARRAY OF TEENAGERS <<<<<<<<<<<<<
adults = ages[ages >= 18] # Filter ages greater than or equal to 18 (boolean indexing)
print("Adults:", adults) # Print the filtered array of adults
#>>>>>>>>> ARRAY IS NOW FLATENED TO 1D ARRAY OF ADULTS <<<<<<<<<<<<<
senior_citizens = ages[ages >= 65] # Filter ages greater than or equal to 65 (boolean indexing)
print("Senior Citizens:", senior_citizens) # Print the filtered array of senior citizens
