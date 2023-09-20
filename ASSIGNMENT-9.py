# Given data
bod_3_days_20_degC = 50  # BOD at 3 days at 20°C in mg/L
decay_coefficient = 0.23  # Decay coefficient

# Calculate the BOD at 7 days at 25°C using the BOD rate equation
# BOD7 = BOD3 * e^(-k * (t7 - t3))
# Where:
# BOD7 = BOD at 7 days
# BOD3 = BOD at 3 days
# k = Decay coefficient
# t7 = Time at 7 days (converted to hours)
# t3 = Time at 3 days (converted to hours)

t3_hours = 3 * 24  # Time at 3 days converted to hours
t7_hours = 7 * 24  # Time at 7 days converted to hours

bod_7_days_25_degC = bod_3_days_20_degC * (2.71828 ** (-decay_coefficient * (t7_hours - t3_hours)))

# Print the result
print(f"BOD at 7 days at 25°C: {bod_7_days_25_degC:.2f} mg/L")
