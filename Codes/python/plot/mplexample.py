# Matplot Example
"""Libraries for matplotlib and numpy to handle 
calculations for the function to be plotted
"""
import matplotlib.pyplot as plt
import numpy as np

# Create a dataset ranging from -10 to 10 with 100 steps
t = np.linspace(-10, 10, 100)
# Create a function to be plotted
# sig = 1 / (1 + np.exp(-t))
# secondary function to be plotted
sig = np.sin(t)

# Setup Plot
# Create the plot obeject
fig, ax = plt.subplots()
# Define axes
ax.axhline(y=0, color="black", linestyle="--")
ax.axhline(y=0.5, color="black", linestyle=":")
ax.axhline(y=1.0, color="black", linestyle="--")
ax.axvline(color="grey")
ax.axline((0, 0.5), slope=0.25, color="black", linestyle=(0, (5, 5)))
ax.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
ax.set(xlim=(-10, 10), xlabel="t")
ax.legend(fontsize=14)
# Plot the function
plt.show()
