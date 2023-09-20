import math

# Given data
discharge = 100  # Discharge in m^3/s
roughness_coefficient = 0.015
channel_slope = 1 / 2500  # Channel bed slope (S)
freeboard_percentage = 0.10  # 10% of depth as freeboard

# Calculate the hydraulic radius using Manning's equation
# Q = (1/n) * A * R^(2/3) * S^(1/2)
# Where Q is the discharge, n is the Manning's roughness coefficient, A is the cross-sectional area, R is the hydraulic radius, and S is the channel slope.

# We can rearrange the equation to solve for the hydraulic radius R:
# R = (Q / (n * A * S^(1/2)))^(3/2)

# To design an efficient trapezoidal channel, we'll assume a particular side slope (Z) and calculate the dimensions.

# Calculate the width (b) based on a chosen side slope (Z)
Z = 2  # Assume a 2:1 side slope
b = 1.0  # Initial guess for channel bottom width
R = 1.0  # Initial guess for hydraulic radius

# Iterate to find the correct width (b) and hydraulic radius (R)
max_iterations = 100
tolerance = 1e-6  # Tolerance for convergence

for i in range(max_iterations):
    A = (b + Z * R) * R  # Cross-sectional area
    hyd_radius_calc = (discharge / (roughness_coefficient * A * (channel_slope**0.5)))**(2/3)
    
    # Check for convergence
    if abs(hyd_radius_calc - R) < tolerance:
        break
    
    R = hyd_radius_calc
    
    # Recalculate width (b) based on the hydraulic radius
    b = A / (R + Z * R)

# Calculate the depth of flow (y)
y = R / Z

# Calculate the Froude number (Fr)
g = 9.81  # Acceleration due to gravity in m/s^2
velocity = discharge / A
Fr = velocity / (math.sqrt(g * y))

# Calculate the freeboard
freeboard = freeboard_percentage * y

# Print the results
print(f"Design Parameters:")
print(f"Bottom Width (b): {b:.2f} meters")
print(f"Depth of Flow (y): {y:.2f} meters")
print(f"Hydraulic Radius (R): {R:.2f} meters")
print(f"Freeboard: {freeboard:.2f} meters")
print(f"Froude Number (Fr): {Fr:.4f}")

# Check if the computed Fr is greater than 1 (supercritical flow)
if Fr > 1:
    print("The flow is supercritical.")
else:
    print("The flow is subcritical.")
