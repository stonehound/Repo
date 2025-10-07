"""
This is a code to test creating a gaussian distribution, selecting certain elements, manipulating and replacing them.
Then the original and modified arrays will be plotted as histograms.
"""
import numpy.random as rand
import matplotlib.pyplot as plt

# Create a 100 element array of random values following the gaussian distribution
rando = rand.randn(200)

a = rando - .1

# Index values greater than .2
index  = a > .2
b = a[index]

# Operate on those values from the random set
b = b ** 2 + .1

# Reinsert modified value
a[index] = b

# Create background figure and axes, formatted to share y-axes, with 1 row and 2 columns
fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# set number of bins to subdivide dataset
n_bins = 50

# We can set the number of bins with the *bins* keyword argument.
axs[0].hist(rando, bins=n_bins)
axs[1].hist(a, bins=n_bins)

plt.show()
