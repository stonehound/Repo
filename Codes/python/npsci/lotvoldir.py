# This is a code to simulate and plot the Lotka Volterra Equations as a directional graph

import matplotlib.pyplot as plt
import numpy as np

# Define the Lotka-Volterra equations
def lotka_volterra(X, t, alpha, beta, delta, gamma):
    x, y = X
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Create a grid for the phase plane
x_grid, y_grid = np.meshgrid(np.linspace(0, 100, 200), np.linspace(0, 100, 200))

# Calculate the derivatives at each point in the grid
dx_grid, dy_grid = lotka_volterra([x_grid, y_grid], 0, 1.0, 0.1, 0.1, 1.0) # Example parameters

plt.streamplot(x_grid, y_grid, dx_grid, dy_grid, color='blue', linewidth=0.5)
plt.xlabel('Prey Population')
plt.ylabel('Predator Population')
plt.title('Lotka-Volterra Direction Field')
plt.show()
