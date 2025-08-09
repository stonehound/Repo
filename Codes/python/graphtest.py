# Testing graphing with Python:
# Libraries
import numpy as np
from scipy.optimize import curve_fit

# Define a function
def fun(x, a, b):
    return a * x + b

# Generate clean data
x = np.linspace(0, 10, 100)
y = fun(x, 1, 2)

# Adding noise to the data
yn = y + .9 * np.random.normal(size = len(x))

# Executing curve_fit on noisy data
popt, pcov = curve_fit(fun, x, yn)  # 'popt' returns the best-fitvalues for the parameters of the given model(fun)

# Print plot
print(popt)
# Note that these results can vary as the data is 'randomly' generated

