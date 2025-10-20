# This is a test of writing the data from one file to another

import numpy as np

# Allows reading capability
f = open('test.txt', 'r')

# Parsing the file and splitting each line,
# which creates one list where each element
# is on its own line
alist = f.readlines()

# Close the file
f. close

# Open new file to write into
w = open('retest.txt', 'w')

# New dataset
newdata = alist[0] + "So much! \n"

# Write the data into the new file
w.writelines(newdata)

# Close new file
w.close()

