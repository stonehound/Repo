# This code is practice for array creation with numpy

import numpy as np
import time

# Create an array with 10^7 elements
arr = np.arange(1E7) 

# Convert the array to a list
larr = arr.tolist()

'''
Lists cannot be broadcast by default,
so a function is coded so we can emmulate
what an ndarray can do.
'''
# Enumerate return (Index, Value) from the list or array 
def list_time(alist, scalar):
    for i, val in enumerate(alist):
        alist[i] = val * scalar
    return alist

print('We will compare the time it takes to process an ndarray vs a list.')

# use time to measure how long it takes to process
start = time.perf_counter()
a =  arr * 1.1
end = time.perf_counter()
print('This is the time it takes to process the ndarray:')
print(end - start, 'seconds')
print()

t1 = end - start

# Compare the time it takes both to process
start = time.perf_counter()
b = list_time(larr, 1.1)
end = time.perf_counter()
print('This is the time it takes to process the list:')
print(end - start, 'seconds')
print()

t2 = end - start

print('The difference in time between the two processes was:')
print(abs(t1 - t2), 'seconds')
print()
print('The ndarray processed', ((t2/t1)*100), '% faster than the list.')

