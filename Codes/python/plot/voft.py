"""
Graphing a Velocity as a function of Time example for deriving a Position as a function of Time model including Acceleration
"""
# Libraries for matplotlib and numpy to handle calculations for the function to be plotted
import matplotlib.pyplot as plt
import numpy as np

# Setup Variables:
# Final Time is 6(Seconds)
tf = 6
# Create a dataset for Time ranging from 0 to 5(Seconds) with 100 steps
t = np.linspace(0, tf, 100)
# Initial Velocity is 20(meters/second)
vi = 20
# Acceleration is 10(meters/seconds^2)
a = 10
# Velocity as a function of Time
voft = a * t + vi
# Create a dataset for the vertical axis representing the process until Time Final
vf = a * tf + vi
vrange = np.linspace(0, vf, 100)

# Setup Plot:
# Create the plot object
fig, ax = plt.subplots()

# Define Axes
ax.plot(t, voft, linewidth=3, label=r"$v(t)=a*t+vi$")
ax.set(xlim=(0, tf), ylim=(0,vf), xlabel="Time(Seconds)", ylabel="Velocity(Meters/Second)")
ax.legend(fontsize=15)

# Plot the Function
plt.show()
