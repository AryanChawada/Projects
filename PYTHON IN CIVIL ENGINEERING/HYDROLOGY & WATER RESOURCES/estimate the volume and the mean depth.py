# Given data
polygon_areas_cm2 = [25, 30, 30, 10, 5]  # Theissen polygon areas in cm^2
rainfall_cm = [125, 175, 225, 275, 325]  # Annual rainfall in cm
scale = 50000  # Scale of the map (1:x)

# Initialize variables for summation
total_volume_cm3 = 0

# Calculate the volume of rainfall for each station's Theissen polygon
for i in range(len(polygon_areas_cm2)):
    polygon_area_cm2 = polygon_areas_cm2[i]
    annual_rainfall_cm = rainfall_cm[i]
    
    # Convert polygon area to m^2 and rainfall to m
    polygon_area_m2 = polygon_area_cm2 / 10000  # 1 cm^2 = 0.0001 m^2
    annual_rainfall_m = annual_rainfall_cm / 100  # 1 cm = 0.01 m
    
    # Calculate the volume of rainfall for the polygon (V = A * P)
    volume_m3 = polygon_area_m2 * annual_rainfall_m
    
    # Convert volume to cm^3 (1 m^3 = 1,000,000 cm^3)
    volume_cm3 = volume_m3 * 1000000
    
    # Add the volume to the total volume
    total_volume_cm3 += volume_cm3

# Calculate the total area of the catchment
total_catchment_area_cm2 = sum(polygon_areas_cm2)

# Calculate the mean depth of rainfall (D = V / A)
mean_depth_cm = total_volume_cm3 / total_catchment_area_cm2

# Print the results
print(f"Total Volume of Rainfall: {total_volume_cm3:.2f} cm^3")
print(f"Mean Depth of Rainfall: {mean_depth_cm:.2f} cm")
