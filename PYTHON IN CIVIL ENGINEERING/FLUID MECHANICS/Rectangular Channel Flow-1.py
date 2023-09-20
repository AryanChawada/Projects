# Given data
b = 2  # Width of the channel in meters
Q = 4.8  # Discharge in m^3/s
y1 = 1.6  # Initial depth of flow in meters
hump_height = 0.1  # Hump height in meters
g = 9.81  # Acceleration due to gravity in m/s^2

# Calculate velocity at upstream section (v1)
v1 = Q / (b * y1)

# Calculate y2 (depth downstream of the hump)
y2 = Q / (b * v1)

# Calculate specific energies at upstream (E1) and downstream (E2) sections
E1 = y1 + (v1**2) / (2 * g)
E2 = y2 + (v1**2) / (2 * g)

# Calculate the likely change in water surface elevation (Δy)
delta_y = y2 - y1

print(f"a.) Likely change in water surface elevation (Δy): {delta_y:.2f} meters")

# Given data for the higher hump height
hump_height_high = 0.5  # Hump height in meters

# Calculate y2 (depth downstream of the higher hump)
y2_high = Q / (b * v1)

print(f"b.) Upstream depth of flow for higher hump: {y1:.2f} meters")
print(f"    Downstream depth of flow for higher hump: {y2_high:.2f} meters")

max_hump_height = 1.0  # Maximum hump height to test
increment = 0.01  # Increment for hump height

while hump_height < max_hump_height:
    y2_test = Q / (b * v1)  # Calculate downstream depth for the current hump height
    E2_test = y2_test + (v1**2) / (2 * g)  # Calculate specific energy downstream
    if E2_test < E1:
        break
    hump_height += increment

max_delta_z = hump_height  # Maximum rise in bed level

print(f"c.) Maximum rise in bed level possible without changing the upstream condition (Δz): {max_delta_z:.2f} meters")
