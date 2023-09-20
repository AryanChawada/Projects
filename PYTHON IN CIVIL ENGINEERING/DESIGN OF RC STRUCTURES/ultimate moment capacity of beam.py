# Given data
b_eff = 230  # Effective width of the beam section in mm
d = 400  # Overall depth of the beam section in mm
steel_reinforcement = [(2, 16), (2, 20)]  # Steel reinforcement: [(number of bars, diameter in mm), ...]
material_grade_concrete = "M20"  # Concrete grade
material_grade_steel = "Fe415"  # Steel grade

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

# Calculate the area of steel reinforcement
steel_area = sum([(n * (diameter/10)**2 * 0.25 * 3.1416) for n, diameter in steel_reinforcement])  # Convert diameter to cm

# Calculate the lever arm (d') to the centroid of the tensile reinforcement
d_prime = d - (0.5 * 20)  # Assuming the bars are symmetrically placed

# Determine the yield strength of the steel
steel_yield_strength = steel_grade_strength[material_grade_steel]

# Calculate the lever arm (d) to the centroid of the compressive concrete block
d = d_prime - (0.5 * 16)  # Assuming the bars are symmetrically placed

# Calculate the ultimate moment carrying capacity (Mu) in N-mm
Mu = (steel_area * steel_yield_strength * (d - 0.416 * d_prime)) / 1000  # Convert to N-m

# Print the result
print(f"Ultimate Moment Carrying Capacity (Mu): {Mu:.2f} N-m")
