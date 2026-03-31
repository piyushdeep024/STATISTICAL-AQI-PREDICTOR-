import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

# CONFIGURATION
MAX_RECORDS = 100
SYSTEM_NAME = "V-AIR: Statistical AQI Predictor"


# DATA MODEL
@dataclass
class AirQualityRecord:
    hour: int
    aqi: float
    category: str


# CORE SYSTEM CLASS

class AQIPredictor:
    def __init__(self):
        self.records = []
        print(f"[*] {SYSTEM_NAME} Initialized.\n")

 # AQI CATEGORY CLASSIFICATION
    @staticmethod
    def get_category(aqi):
        if aqi <= 50:
            return "GOOD"
        elif aqi <= 100:
            return "MODERATE"
        elif aqi <= 200:
            return "UNHEALTHY"
        elif aqi <= 300:
            return "VERY UNHEALTHY"
        return "HAZARDOUS"
    
  # ADD DATA
    def add_reading(self):
        if len(self.records) >= MAX_RECORDS:
            print("[!] Database full.\n")
            return

        try:
            aqi_value = float(input("Enter AQI value: "))
        except ValueError:
            print("[!] Invalid input. Please enter a number.\n")
            return

        hour = len(self.records) + 1
        category = self.get_category(aqi_value)

        record = AirQualityRecord(hour, aqi_value, category)
        self.records.append(record)

        print("[✓] Reading added successfully.\n")

   # DISPLAY DATA
    def show_history(self):
        if not self.records:
            print("[!] No data available.\n")
            return

        print(f"\n{'HOUR':<6}{'AQI':<10}{'CATEGORY'}")
        print("-" * 30)

        for r in self.records:
            print(f"{r.hour:<6}{r.aqi:<10.2f}{r.category}")
        print()

     # LINEAR REGRESSION
    def predict(self):
        if len(self.records) < 2:
            print("[!] Need at least 2 data points.\n")
            return None

        x = np.array([r.hour for r in self.records])
        y = np.array([r.aqi for r in self.records])

        n = len(x)

        # Calculate slope (m) and intercept (c)
        m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / \
            (n * np.sum(x**2) - (np.sum(x) ** 2))

        c = (np.sum(y) - m * np.sum(x)) / n

        next_hour = x[-1] + 1
        prediction = m * next_hour + c

        print("\n--- Prediction Result ---")
        print(f"Slope (m): {m:.2f}")
        print(f"Intercept (c): {c:.2f}")
        print(f"Next Hour AQI: {prediction:.2f}")
        print(f"Category: {self.get_category(prediction)}\n")

        return m, c

   # VISUALIZATION
    def plot(self, m, c):
        if not self.records:
            print("[!] No data to plot.\n")
            return

        x = np.array([r.hour for r in self.records])
        y = np.array([r.aqi for r in self.records])

        trend = m * x + c

        plt.figure(figsize=(10, 5))
        plt.scatter(x, y, label="Actual AQI")
        plt.plot(x, trend, label="Trend Line")

        plt.title("AQI Trend Prediction")
        plt.xlabel("Hour")
        plt.ylabel("AQI")
        plt.grid(True)
        plt.legend()
        plt.show()


# MAIN APPLICATION
def main():
    app = AQIPredictor()
    m, c = None, None

    while True:
        print("===== MENU =====")
        print("1. Add AQI Reading")
        print("2. Show History")
        print("3. Predict AQI")
        print("4. Show Graph")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("[!] Invalid choice.\n")
            continue

        if choice == 1:
            app.add_reading()

        elif choice == 2:
            app.show_history()

        elif choice == 3:
            result = app.predict()
            if result:
                m, c = result

        elif choice == 4:
            if m is None or c is None:
                print("[!] Run prediction first.\n")
            else:
                app.plot(m, c)

        elif choice == 5:
            print("Exiting... Goodbye!")
            break

        else:
            print("[!] Invalid option.\n")


# ENTRY POINT
if __name__ == "__main__":
    main()