import math


def calculate_bearing_capacity(water_table_position, angle_of_internal_friction, bulk_density_soil, saturated_density_soil, unit_weight_water):
  """
  Calculates the ultimate bearing capacity of a square footing.

  Args:
    water_table_position: The water table position.
    angle_of_internal_friction: The angle of internal friction of the soil.
    bulk_density_soil: The bulk density of the soil.
    saturated_density_soil: The saturated density of the soil.
    unit_weight_water: The unit weight of water.

  Returns:
    The ultimate bearing capacity.
  """

  if water_table_position == "Ground Surface":
    depth_to_water_table = 0
  elif water_table_position == "Footing Level":
    depth_to_water_table = 2
  else:
    depth_to_water_table = 1

  effective_depth = 2 - depth_to_water_table

  # Calculate the bearing capacity using the approximate formulas
  bearing_capacity_approx = (
      0.5 * bulk_density_soil * effective_depth ** 2 * math.tan(angle_of_internal_friction)
  )

  # Calculate the bearing capacity using the conventional method
  bearing_capacity_conventional = (
      0.5 * saturated_density_soil * effective_depth ** 2 * math.tan(angle_of_internal_friction)
  )

  return bearing_capacity_approx, bearing_capacity_conventional


def main():
  # Input data
  angle_of_internal_friction = 35  # degrees
  bulk_density_soil = 18  # kN/m³
  saturated_density_soil = 20  # kN/m³
  unit_weight_water = 10  # kN/m³

  # Calculate the bearing capacity for each water table position
  water_table_positions = ["Ground Surface", "Footing Level", "1 m below Footing"]
  for water_table_position in water_table_positions:
    bearing_capacity_approx, bearing_capacity_conventional = calculate_bearing_capacity(
      water_table_position, angle_of_internal_friction, bulk_density_soil, saturated_density_soil, unit_weight_water
    )

    print(f"Water Table Position: {water_table_position}")
    print(f"Bearing Capacity (Approximate): {bearing_capacity_approx:.2f} kN/m²")
    print(f"Bearing Capacity (Conventional): {bearing_capacity_conventional:.2f} kN/m²")


if __name__ == "__main__":
  main()