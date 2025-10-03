# This is a code for working with boolean statements and arrays with numpy
# and for plotting it as an image
import numpy as np
import matplotlib.pyplot as plt

# Create an image, that is 2000p x 2000p at greyscale value 3
img1 = np.zeros((20, 20)) + 3

# Create an inner square at greyscale value 6
img1[4:-4,4:-4] = 6
# Create a central square of greyscale value 9
img1[8:-8,8:-8] = 9

# Filter out values greater than 3 and less than 7
index1 = img1 > 3
index2 = img1 < 7

# Create a compound index
compound = index1 & index2

# Use the index to create a new image
img2 = np.copy(img1)
img2[compound] = 0

# Plot img2
plt.imshow(img2, cmap='gray')
# plt.colorbar()
plt.title('Image from NumPy Array')
plt.show()

