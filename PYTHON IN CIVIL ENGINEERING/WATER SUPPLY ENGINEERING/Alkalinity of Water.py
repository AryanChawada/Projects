import numpy as np

# Given data
initial_ph = 10
final_ph_1 = 4.5
final_ph_2 = 8.3
volume_1 = 30  # mL
volume_2 = 11  # mL
normality_h2so4 = 0.02  # N

# Constants for molecular weights
molecular_weight_h2so4 = 98.08  # g/mol (molecular weight of H2SO4)
molecular_weight_caco3 = 100.09  # g/mol (molecular weight of CaCO3)

# Calculate the equivalent weight of CaCO3
equivalent_weight_caco3 = molecular_weight_caco3 / 2  # Equivalent weight (eq/g) for CaCO3

# Convert volumes to liters
volume_1_liters = volume_1 / 1000  # Convert mL to L
volume_2_liters = volume_2 / 1000  # Convert mL to L

# Calculate the moles of H2SO4 used in each titration
moles_h2so4_1 = normality_h2so4 * volume_1_liters
moles_h2so4_2 = normality_h2so4 * volume_2_liters

# Define the system of linear equations:
# 1. Moles of OH- in initial solution - Moles of H2SO4 added = Moles of OH- in final solution at pH 4.5
# 2. Moles of OH- in initial solution - Moles of H2SO4 added = Moles of OH- in final solution at pH 8.3

# Define the coefficients matrix and the constants vector
coefficients_matrix = np.array([[1, -moles_h2so4_1], [1, -moles_h2so4_2]])
constants_vector = np.array([10**(-initial_ph), 10**(-initial_ph)])

# Solve the system of linear equations
alkalinity_moles = np.linalg.solve(coefficients_matrix, constants_vector)

# Calculate the total alkalinity in moles and convert it to mg/L as CaCO3
total_alkalinity_mg_per_L = alkalinity_moles * equivalent_weight_caco3 * 1000  # Convert moles to mg/L

# Print the results
print(f"a. Total Alkalinity of Water: {total_alkalinity_mg_per_L[0]:.2f} mg/L as CaCO3")
print(f"b. Concentration of Alkaline Species at pH 8.3: {total_alkalinity_mg_per_L[1]:.2f} mg/L as CaCO3")
