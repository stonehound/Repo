# This is a test of reading data files with python

import numpy as np

# Allows reading capability
f = open('test.txt', 'r')

# Parsing the file and splitting each line,
# which creates one list where each element
# is on its own line
alist = f.readlines()

# Close the file
f. close

# Print the contents of the file after parsing
print(alist)
