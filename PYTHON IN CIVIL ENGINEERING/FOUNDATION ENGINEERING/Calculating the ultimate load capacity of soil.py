# Given data
pile_side_length = 0.45  # Side length of the square pile in meters (450 mm)
pile_length = 15.0  # Length of the pile in meters (15 m)
average_ucs = 75.0  # Average UCS (Unconfined Compressive Strength) of the clay in kN/m² (75 kN/m²)
ca = 0.8  # Pile-soil interaction coefficient

# Calculate the area of the pile base
pile_base_area = pile_side_length ** 2  # Square pile base area in square meters

# Calculate the ultimate load capacity of the pile
ultimate_load_capacity = average_ucs * pile_base_area * pile_length * ca

# Print the result
print(f"Ultimate Load Capacity of the Pile: {ultimate_load_capacity:.2f} kN")
