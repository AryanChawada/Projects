# Given data
grade_m40_max_wc_ratio = 0.45
desired_workability_mm = 100
min_cement_content_kg_per_m3 = 320
max_cement_content_kg_per_m3 = 450
specific_gravity_cement = 3.15
specific_gravity_fine_aggregates = 2.74
specific_gravity_coarse_aggregates = 2.74

# Calculate the water-cement ratio (W/C ratio)
wc_ratio = grade_m40_max_wc_ratio

# Calculate the water content for the desired workability
water_content_mm = desired_workability_mm
water_content_kg_per_m3 = water_content_mm * 2  # Assume 2 kg/m³ per mm of water requirement

# Calculate the cement content based on the water content
cement_content_kg_per_m3 = min_cement_content_kg_per_m3 + water_content_kg_per_m3

# Calculate the fine aggregate content based on the desired workability and cement content
fine_aggregate_content_kg_per_m3 = cement_content_kg_per_m3 / ((1 / wc_ratio) - 1)  # Assuming fine aggregates are saturated and surface dry

# Calculate the coarse aggregate content based on the specified maximum size of aggregates
max_size_of_aggregates_mm = 20
coarse_aggregate_content_kg_per_m3 = 1000 - (cement_content_kg_per_m3 + fine_aggregate_content_kg_per_m3)

# Check if the grading of fine aggregates and coarse aggregates conforms to Zone-I
# You may need to provide the grading curve data to perform this check.

# Print the results
print("Concrete Mix Design Results:")
print(f"Water-Cement Ratio (W/C ratio): {wc_ratio:.2f}")
print(f"Water Content for Workability ({desired_workability_mm} mm): {water_content_kg_per_m3:.2f} kg/m³")
print(f"Cement Content (Minimum): {min_cement_content_kg_per_m3} kg/m³")
print(f"Cement Content (Calculated): {cement_content_kg_per_m3:.2f} kg/m³")
print(f"Fine Aggregate Content: {fine_aggregate_content_kg_per_m3:.2f} kg/m³")
print(f"Coarse Aggregate Content: {coarse_aggregate_content_kg_per_m3:.2f} kg/m³")
