# Given data
width_initial = 3.5  # Initial width of the channel in meters
width_constricted = 2.5  # Constricted width of the channel in meters
discharge = 15  # Discharge in m^3/s
depth_initial = 2  # Initial depth of flow in meters

# Calculate the cross-sectional area of the channel before and after the constriction
area_initial = width_initial * depth_initial
area_constricted = width_constricted * depth_initial

# Calculate the velocity of flow before and after the constriction using the principle of continuity
velocity_initial = discharge / area_initial
velocity_constricted = discharge / area_constricted

# Calculate the water surface elevation at the upstream and downstream of the constriction
# Upstream elevation remains the same
upstream_elevation = depth_initial

# Downstream elevation can be calculated using the specific energy equation
# E = y + (v^2) / (2 * g), where E is the specific energy, y is the depth of flow, v is the velocity, and g is the acceleration due to gravity
g = 9.81  # Acceleration due to gravity in m/s^2
downstream_elevation = depth_initial + (velocity_initial**2) / (2 * g) - (velocity_constricted**2) / (2 * g)

# Print the results
print(f"Upstream water surface elevation: {upstream_elevation:.2f} meters")
print(f"Downstream water surface elevation: {downstream_elevation:.2f} meters")
