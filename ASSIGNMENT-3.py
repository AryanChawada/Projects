# Given data
design_speed_kmph = 65  # Design speed in km/h
radius_of_curvature_m = 220  # Radius of curvature in meters
allowable_rate_of_superelevation = 1 / 150  # Allowable rate of introduction of superelevation (1 in X)
pavement_width_m = 7.5  # Pavement width including extra widening in meters
g = 9.81  # Acceleration due to gravity in m/s²

# Convert design speed to m/s
design_speed_mps = design_speed_kmph * 1000 / 3600  # 1 km/h = 1000 m/3600 s

# Calculate the length of the transition curve
length_of_transition_curve = (design_speed_mps ** 2) / (g * allowable_rate_of_superelevation)

# Print the result
print(f"Length of the transition curve: {length_of_transition_curve:.2f} meters")
