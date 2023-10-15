import matplotlib.pyplot as plt

class IndianAQICalculator:
    def __init__(self, aqi_values):
        self.aqi_values = aqi_values
        self.aqi_range = [
            (0, 50, "No impact"),
            (51, 100, "Breathing difficulty"),
            (101, 200, "Lung and heart disease"),
            (201, 300, "Long and short exposure on heart disease"),
            (301, 400, "Respiratory illness for longer duration"),
            (401, 500, "Several health impacts")
        ]

    def calculate_7_day_avg_aqi(self):
        if len(self.aqi_values) != 7:
            print("Exactly 7 days of data required for calculation.")
            return None
        return sum(self.aqi_values) / 7

    def get_aqi_category(self, aqi_value):
        for low, high, category in self.aqi_range:
            if low <= aqi_value <= high:
                return category

    def plot_aqi_values(self):
        days = [f"Day {i+1}" for i in range(7)]
        plt.plot(days, self.aqi_values, marker='o')
        plt.title('AQI Index for 7 Days')
        plt.xlabel('Days')
        plt.ylabel('AQI Value')
        plt.show()

# Example usage:
aqi_values = [45, 88, 123, 265, 340, 420, 200]  # Sample AQI values for 7 days
aqi_calculator = IndianAQICalculator(aqi_values)

# Calculate 7-day average AQI and its category
avg_aqi = aqi_calculator.calculate_7_day_avg_aqi()
if avg_aqi is not None:
    print(f"7-day average AQI: {avg_aqi}")
    print(f"Impact: {aqi_calculator.get_aqi_category(avg_aqi)}")

# Plot the graph
aqi_calculator.plot_aqi_values()
