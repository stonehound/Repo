# This is a test for the numpy math operations on ndarrays

import numpy as np

print('This will run through some principal array operations with numpy.') 
print()
print('First, create and print 2 ndarrays and the results of a variety of array operations using numpy.')

'''
Numpy has more than one function to create ndarrays, np.array() & np.arange()
np.array() intakes any iterable data type and converts it to an ndarray
np.arange() intakes parameters for a spaced sequence of values
'''
# Create an ndarray with 4 elements, as 64 bit floating point values, reshaped into a 2x2 matrix
arr1 = np.arange(4, dtype = np.float64).reshape(2, 2)
print('First array:')
print(arr1)

# Create a second ndarray 
arr2 = np.array([12, 12])
print('Second array:')
print(arr2)

# The sum of the ndarrays, note that the output elements are now type float64
print('The sum of the ndarrays:')
print(np.add(arr1, arr2))

# The difference between the two ndarrays
print('The difference between the two ndarrays:')
print(np.subtract(arr1, arr2))

# Multiplying the two ndarrays
print('The product of two arrays:')
print(np.multiply(arr1, arr2))

# Diving the two ndarrays
print('The quotient of the two arrays:')
print(np.divide(arr1, arr2))

print()

'''
The np.reciprocal() function returns the reciprocal of the argument, element-wise.
For elements with absolute value greater than 1, the return will always be  0.
For integer0, this will produce an overflow warning.
'''

# Create a new array for testing np.reciprocal()
print('Testing the np.reciprocal() function.')
print('This is a new array for highlighting the effects of the np.reciprocal() function:')
arr3 = np.array([25, 1.33, 1, 1, 100]) 
print(arr3)

# Apply np.reciprocal()
print('This is the output to np.reciprocal():')
rec_arr3 = np.reciprocal(arr3)
print(rec_arr3)

# Create a second array composed of an integer with absolute value greater than 1
print('This is a second array created to highlight the effects of np.reciprocal() on integers with magnitude greater than 0:')
arr4 = np.array([-25])
print(arr4)

# Apply np.reciprocal()
print('This is the output of np.reciprocal():')
rec_arr4 = np.reciprocal(arr4)
print(rec_arr4)

print()

'''
The np.powers() function takes the elements of the first array, 
and raises it to the power of the corresponding element of the second array.
'''
print('Creating new arrays to test the np.power() function.')

# Create a new array for the base values of the operation
print('First Array:')
arr5 = np.array([5, 10, 15])
print(arr5)

# Find the 10th power of the elements of the array
print('This is the 10th power of the elements of the array:')
print(np.power(arr5, 10))


# Create a second array for the exponent values of the operation
print('Second array:')
arr6 = np.array([1, 2, 3])
print(arr6)

# Apply np.power() function to the two arrays
print('These are the elements of the first array to the power of the elements of the second array:')
print(np.power(arr5, arr6))

print()

'''
The np.mod() function returns the remainder of the division of the corresponding elements of the input arrays.
The np.remainder() function returns the same result.
'''
print('Creating arrays to testing the np.mod() function.')

# Use an array for the numerators of the division:
print('Array values for the Numerator:')
print(arr5)

# Create an array for the values of the denominator of the division
print('Array values for the Denominator:')
arr7 = np.array([2, 5, 9])
print(arr7)

# Apply np.mod()
print('This is the output of np.mod():')
print(np.mod(arr5, arr7))

