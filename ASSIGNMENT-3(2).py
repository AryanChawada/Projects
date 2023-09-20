# Given data
ewl_constant_values = [330, 1070, 2460, 4620]  # EWL Constant in thousands
aadt_values = [3750, 470, 320, 120]  # Annual Average Daily Traffic (AADT)
traffic_increase_percentage = 60  # 60% increase in traffic over 10 years
years = 10  # Number of years
R = 48  # Repetitions
C = 16  # Cover factor

# Calculate EWL and TI values for 10 years
ewl_values = []
ti_values = []

for i in range(len(ewl_constant_values)):
    ewl_constant = ewl_constant_values[i]
    aadt = aadt_values[i]
    
    # Calculate the equivalent wheel load (EWL) for the current year
    ewl = ewl_constant * (aadt / 1000)  # Convert AADT to thousands
    
    # Calculate the traffic index (TI) for the current year
    ti = ewl / (R * (C ** 4))
    
    ewl_values.append(ewl)
    ti_values.append(ti)
    
    # Update AADT for the next year with the traffic increase
    aadt = aadt + (aadt * (traffic_increase_percentage / 100))

# Calculate the total EWL and TI values for 10 years
total_ewl = sum(ewl_values)
total_ti = sum(ti_values)

# Calculate the required pavement thickness using the total TI value
required_thickness = (total_ti / (C ** 4)) ** (1/4)

# Print the results
print("Year\tEWL (kN)\tTraffic Index")
for i in range(len(ewl_values)):
    print(f"{i + 1}\t{ewl_values[i]}\t\t{ti_values[i]:.4f}")

print(f"\nTotal EWL for 10 years: {total_ewl:.2f} kN")
print(f"Total Traffic Index for 10 years: {total_ti:.4f}")
print(f"Required Pavement Thickness: {required_thickness:.2f} mm")
