# Given data
compacted_soil_cbr = 6  # CBR for compacted soil (%)
poorly_graded_gravels_cbr = 12  # CBR for poorly graded gravels (%)
well_graded_gravel_cbr = 60  # CBR for well-graded gravel (%)
bituminous_surface_thickness_cm = 4  # Thickness of bituminous surface (cm)
wheel_load_kg = 4085  # Wheel load in kg
tyre_pressure_kg_per_cm2 = 7  # Tyre pressure in kg/cm^2

# Load and Penetration data for the CBR test
load_data = [60, 82]  # Load in kg
penetration_data = [2.5, 5.0]  # Penetration in mm
standard_load_data = [1370, 2055]  # Standard load in kg

# Calculate the CBR values for each test point
cbr_values = []

for i in range(len(load_data)):
    load = load_data[i]
    penetration = penetration_data[i]
    standard_load = standard_load_data[i]
    
    # Calculate the CBR for the current test point
    cbr = (load / standard_load) * 100
    
    cbr_values.append(cbr)

# Calculate the average CBR from the test data
average_cbr = sum(cbr_values) / len(cbr_values)

# Calculate the thickness correction factor for the bituminous surface
thickness_correction_factor = 1 + (bituminous_surface_thickness_cm / 10)

# Calculate the effective CBR for the pavement structure
effective_cbr = average_cbr * thickness_correction_factor

# Determine the type of material based on effective CBR
material_type = None
if effective_cbr < compacted_soil_cbr:
    material_type = "Compacted Soil"
elif effective_cbr < poorly_graded_gravels_cbr:
    material_type = "Poorly Graded Gravels"
elif effective_cbr < well_graded_gravel_cbr:
    material_type = "Well-graded Gravel"
else:
    material_type = "Unknown (High CBR)"

# Print the results
print(f"Average CBR from test data: {average_cbr:.2f}%")
print(f"Thickness Correction Factor: {thickness_correction_factor:.2f}")
print(f"Effective CBR for pavement structure: {effective_cbr:.2f}%")
print(f"Type of material based on effective CBR: {material_type}")

