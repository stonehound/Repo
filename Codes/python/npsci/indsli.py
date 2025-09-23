# This is a test of indexing and slicing arrays in numpy

"""
The index list for ndarrays in numpy begins with element 0,
following suit with lists in python. 
"""

import numpy as np
from time import sleep

# Sleep() input
t = .8

print()
print('This is an example of indexing and slicing arrays with numpy.\nIndexing allows us to access specific rows and collumns from n-dimensional array.')
print()
sleep(t)

# Make a list
alist = [[1,2],[3,4]]

# Print element[1] from list[0]
# print(alist[0][1])
sleep(t)

# Make an array from the list
print('Make a 2x2 array:')
arr1 = np.array(alist)
print(arr1)
sleep(t)

# From list[0] print element[1]
print('From list[0], print element[1]:')
print(arr1[0,1])
sleep(t)

# Access the last collumn of the array
print('All elements from the last collumn:')
print(arr1[:,1])
sleep(t)

# Access the elements of the bottom row
print('Elements from the bottom row:')
print(arr1[1,:])
sleep(t)

'''
We can achieve conditional indexing using the numpy.where() function.
This function can return the desired indices from an array, regardless
of dimensions, based on some condition/s
'''

print()
print('The numpy.where() function can be used to conditionally index.')
print()
sleep(t)

# Create an array
print('Create an array with 6 elements:')
arr2 = np.arange(6)
print(arr2)
sleep(t)

# Create an index array for values greater than 2
print('Creating an index array for values greater than 2:')
index = np.where(arr2 > 2)
print(index)
sleep(t)


# Create a new array from the index list
print('We can create a new array from the index list:')
arr3 = arr2[index]
print(arr3)
sleep(t)


"""
We can remove specific indices with the numpy.delete() function.
This requires the target array and indices you want to remove.
"""

print()
print('The numpy.delete() function is useful for the removal of selective elements from an array:')
print()
sleep(t)

# Remove the index list from the array 
print('Make a new array by removing the index list contents from the previous array:')
arr4 = np.delete(arr2, index)
print(arr4)
sleep(t)

print()
print('Instead of the numpy.where() function, we can return specific elements using a boolean array.\nThis method is significantly faster for arrays with a large number of elements when compared to the numpy.where() function.\nWe can easily invert True and False objects in an array by using ~index, which is far faster than redoing the numpy.where() function.')
print()
sleep(t)

# Index with boolean array
print('Create a boolean array for previous array elements with value greater than 2:')
ind = arr2 > 2
print(ind)
print()
sleep(t)

# Create a new array using the boolean array
print('Use the boolean array to select elements from one array to pruduce another:')
arr5 = arr2[ind]
print(arr5)
print()
