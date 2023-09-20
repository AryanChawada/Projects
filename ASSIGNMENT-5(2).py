import math

# Given data
effective_span = 3.0  # Effective span of the slab in meters
support_width = 0.23  # Support width in meters (230 mm)
live_load = 4.0  # Live load in kN/m
floor_finish_load = 1.8  # Floor finish load in kN/m
clear_cover = 20  # Clear cover in mm
main_reinforcement_dia = 12  # Diameter of main reinforcement bars in mm
distribution_reinforcement_dia = 8  # Diameter of distribution reinforcement bars in mm
concrete_grade = "M20"  # Concrete grade
steel_grade = "Fe415"  # Steel grade
self_weight_concrete = 24  # Self-weight of concrete in kN/m^3

# Constants for material properties
concrete_grade_strength = {
    "M15": 15,
    "M20": 20,
    "M25": 25,
    # Add more grades and strengths as needed
}

steel_grade_strength = {
    "Fe415": 415,
    "Fe500": 500,
    # Add more grades and strengths as needed
}

# Calculate the design moment (Mu) due to live load and floor finish
total_load = live_load + floor_finish_load  # Total applied load in kN/m
Mu = (total_load * effective_span**2) / 8  # Ultimate moment in kN-m

# Calculate the effective depth of the slab (d)
concrete_strength = concrete_grade_strength[concrete_grade]
steel_strength = steel_grade_strength[steel_grade]
d = math.sqrt((Mu * 1000) / (0.138 * concrete_strength))  # Effective depth in mm

# Check for the minimum and maximum steel percentages
min_steel_percentage = 0.12  # Minimum steel percentage for M20 concrete
max_steel_percentage = 0.15  # Maximum steel percentage for M20 concrete

# Calculate the required main reinforcement area (As_main)
As_main = (Mu * 10**6) / (0.87 * steel_strength * d)  # Required main reinforcement area in mm^2
As_main = max(As_main, min_steel_percentage * 1000 * d * effective_span)  # Ensure it meets the minimum steel requirement
As_main = min(As_main, max_steel_percentage * 1000 * d * effective_span)  # Ensure it doesn't exceed the maximum steel limit

# Calculate the spacing of main reinforcement bars
main_reinforcement_spacing = (math.pi * (main_reinforcement_dia / 10)**2) / (4 * As_main)  # Spacing in mm

# Calculate the required distribution reinforcement area (As_dist)
As_dist = 0.12 / 100 * effective_span * d  # Required distribution reinforcement area in mm^2

# Calculate the spacing of distribution reinforcement bars
distribution_reinforcement_spacing = (math.pi * (distribution_reinforcement_dia / 10)**2) / (4 * As_dist)  # Spacing in mm

# Print the results
print("Design Results:")
print(f"Effective Depth (d): {d:.2f} mm")
print(f"Required Main Reinforcement Area (As_main): {As_main:.2f} mm^2")
print(f"Main Reinforcement Spacing: {main_reinforcement_spacing:.2f} mm (center-to-center)")
print(f"Required Distribution Reinforcement Area (As_dist): {As_dist:.2f} mm^2")
print(f"Distribution Reinforcement Spacing: {distribution_reinforcement_spacing:.2f} mm (center-to-center)")
