# This will affirm my love

import numpy as np

# Create an array from 0 to 99
love = "I love Ray!"

lovearr = np.zeros((1,), dtype=str)

col1 = [love]

lovearr[:] = col1

# Create a text file containing the data 
np.savetxt('love.txt', lovearr)

