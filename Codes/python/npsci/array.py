# This code is practice for array creation with numpy

import numpy as np
from time import sleep

# List of arrays
a = []

# List of comments
com = []

# Create an array with 10^7 elements
com.append('This array contains ten million elements:')
a.append(np.arange(1E7))

# Create an array ranging from 111 to 666
com.append('This array ranges from 111 to 666:')
a.append(np.arange(111,666))

# Create a 3x3 matrix
com.append('This array has been reshapes into a 3x3 matrix of integers [1-9]:')
a.append(np.array(np.linspace(1,9,9)).reshape(3,3))

# Create a 6x6 matrix composed of 0s
com.append('This array of zeros has been reshaped into a 6x6 matrix:')
a.append(np.zeros(36).reshape(6,6))

# Create an array ranging from [1-10] in log10 space in 100 steps
com.append('This array of 100 elements will increasing by the pattern log10:') 
a.append(np.logspace(1, 10, 100, base=10.0))

# Create a 5x5 array fo random values
com.append('This array will be converted into a 5x5 matrix of random values:')
a.append(np.random.normal(size = 25).reshape(5,5))

# Make a 3x3x3 cube of 6s
com.append('This array will be shaped as a 3x3x3 cube of sixes:')
cube = np.zeros((3,3,3)).astype(int) + 6
a.append(cube)

# Unravel the cube into a 1D array
com.append('This array will be the 1D unravelled cube of sixes:')
a.append(cube.ravel())

print('This is a collection of arrays made with numpy.')
print()

sleep(1)

# Print all arrays
for x in range(len(a)):
    print('This is array number: ' + str(x + 1))
    print(com[x])
    print(a[x])
    print()
    sleep(3)

