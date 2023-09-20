import numpy as np
import matplotlib.pyplot as plt

# Given data
load_force = 2500 * 1000  # Load force in N (2500 kN)
horizontal_distance = 5  # Horizontal distance from the load axis in meters
depths = np.linspace(0, 6, 100)  # Depths ranging from 0 to 6 meters
constant = 1 / (2 * np.pi)

# Initialize lists to store stress values at different depths
vertical_stresses = []

# Calculate vertical stress at different depths
for depth in depths:
    r = np.sqrt(horizontal_distance ** 2 + depth ** 2)
    vertical_stress = (load_force * constant * depth) / r ** 3
    vertical_stresses.append(vertical_stress)

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(vertical_stresses, depths, label="Vertical Stress")
plt.xlabel("Vertical Stress (Pa)")
plt.ylabel("Depth (m)")
plt.title("Vertical Stress Distribution vs. Depth")
plt.grid(True)
plt.legend()
plt.gca().invert_yaxis()
plt.show()
