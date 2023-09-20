import math
# Given data
initial_infiltration_capacity = 6  # Initial infiltration capacity in cm/hr
final_infiltration_capacity = 1.2  # Final infiltration capacity in cm/hr
decay_coefficient = 0.888  # Decay coefficient in 1/hr
storm_duration_hours = 8  # Duration of the storm event in hours

# Calculate the total infiltration using Horton's equation
total_infiltration = 0
time_elapsed = 0

while time_elapsed < storm_duration_hours:
    # Calculate the infiltration rate at the current time
    current_infiltration_capacity = initial_infiltration_capacity + (final_infiltration_capacity - initial_infiltration_capacity) * (1 - math.exp(-decay_coefficient * time_elapsed))
    # Calculate the time step for the current iteration (assuming small time steps)
    delta_time = 0.01  # You can adjust this for accuracy
    
    # Calculate the infiltration during this time step using the average infiltration rate
    infiltration_during_step = current_infiltration_capacity * delta_time
    
    # Add the infiltration during this time step to the total infiltration
    total_infiltration += infiltration_during_step
    
    # Update the time elapsed
    time_elapsed += delta_time

# Convert the total infiltration from cm to mm
total_infiltration_mm = total_infiltration * 10  # 1 cm = 10 mm

# Print the total infiltration
print(f"Total infiltration during the 8-hour storm event: {total_infiltration_mm:.2f} mm")
