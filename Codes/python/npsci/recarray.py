# This code is to practice record arrays in numpy
'''
While arrays are typically composed of integers and floats,
record arrays can be used to selectively reassign entire
collumns with more complex data types.
'''

import numpy as np

"""
The variable recarr serves as a record arrar. After constructing
the array, the collumns can have their data types individually
specified. The designation i4 stands for 32 bit Integer, the
designation f4 stands for 32 bit Float, and the designation S10
stands for a String with a length of 10 characters.
"""

# Create record array
r = np.zeros((2,), dtype=('i4,f4,S10'))
recarr = r

# Create information to add to record array
toadd1 = [(1,2.0,'Hello'),(2,3.0,'World')]

# Assign variables to record array
recarr[:] = toadd1

print('The recarr test results:')
print(recarr)

print()

"""
The global function zip() can be used to create lists of tuples
that can be used to populate record arrays with information.
"""

# Reset recarr
recarr = r
# Set up collumns
col1 = np.arange(2, dtype=np.int32) + 5
col2 = np.arange(2, dtype=np.float32)
col3 = ['Goodbye', 'World']

# Use zip() to create the list of tuples to be added
toadd2 = list(zip(col1, col2, col3))

# Assign variables to record array
recarr[:] = toadd2

print('The zip() test results:')
print(recarr)

print()

"""
Names for each column are by default f0, f1, f2.
They can be changes with recar.dtype.names assignment.
"""

recarr.dtype.names = ('Integers' , 'Floats' , 'Strings')

print(recarr['Strings'])
print()

