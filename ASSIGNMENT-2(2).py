# Given isohetal data
isohytes_intervals = [14, 12, 10, 8, 6, 4, 2, 0]
inter_area = [90, 140, 125, 140, 85, 40, 20]
total_area_km2 = 640  # Total area of the drainage basin in km²

# Initialize variables for summation
total_precipitation = 0
total_weighted_area = 0

# Calculate the weighted precipitation for each interval and accumulate
for i in range(len(isohytes_intervals) - 1):
    isohyte_midpoint = (isohytes_intervals[i] + isohytes_intervals[i + 1]) / 2
    interval_area = inter_area[i]
    weighted_precipitation = isohyte_midpoint * interval_area
    total_precipitation += weighted_precipitation
    total_weighted_area += interval_area

# Calculate the mean precipitation
mean_precipitation = total_precipitation / total_weighted_area

# Print the mean precipitation
print(f"Mean Precipitation for the drainage basin: {mean_precipitation:.2f} cm")
