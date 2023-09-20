# Given data
initial_mass_sludge = 100  # Initial mass of sludge in kg
initial_specific_gravity = 2.2  # Specific gravity of sludge solids
sludge_volume_reduction_factor = 0.5  # Sludge volume reduction factor
density_water = 1000  # Density of water in kg/m³

# Calculate the mass of solids in the initial sludge
mass_solids_initial = initial_mass_sludge * (initial_specific_gravity / (1 + (initial_specific_gravity - 1) * 0.02))

# Calculate the final mass of sludge after thickening
final_mass_sludge = initial_mass_sludge * sludge_volume_reduction_factor

# Calculate the density of the sludge removed from the aeration tank
density_sludge_removed = final_mass_sludge / (initial_mass_sludge - final_mass_sludge)

# Print the result
print(f"Density of Sludge Removed from Aeration: {density_sludge_removed:.2f} kg/m³")
