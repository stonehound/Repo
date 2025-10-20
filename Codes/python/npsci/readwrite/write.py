# This is a test to write a data file with python

import numpy as np

# Create an array from 0 to 99
arr = np.arange(100)

# Create a text file containing the data 
np.savetxt('hund.txt', arr)

