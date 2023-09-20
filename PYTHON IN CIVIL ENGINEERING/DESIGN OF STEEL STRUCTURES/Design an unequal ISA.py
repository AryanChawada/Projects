# Given data
tensile_force = 225000  # Tensile force in Newtons (225 kN)
safety_factor = 1.5  # Safety factor as per IS 800

# Assume properties of M20 bolts (you may need to look up the actual values)
bolt_diameter = 20  # Bolt diameter in millimeters (M20)
bolt_yield_strength = 240  # Bolt yield strength in MPa (M20)
bolt_safety_factor = 1.5  # Safety factor for bolts

# Calculate the tensile capacity of the M20 bolts
bolt_area = (3.1416 / 4) * (bolt_diameter / 10) ** 2  # Bolt cross-sectional area in square centimeters
bolt_tensile_capacity = bolt_area * bolt_yield_strength * bolt_safety_factor * 1000  # Convert MPa to N/mm²

# Calculate the required tensile capacity of the angle section
required_tensile_capacity = tensile_force / safety_factor

# Calculate the minimum angle section size needed
angle_size_required = required_tensile_capacity / bolt_tensile_capacity  # Angle size in square centimeters

# Print the results
print(f"Required Tensile Capacity: {required_tensile_capacity} N")
print(f"Bolt Tensile Capacity (M20): {bolt_tensile_capacity} N")
print(f"Minimum Angle Section Size Required: {angle_size_required:.2f} cm²")
