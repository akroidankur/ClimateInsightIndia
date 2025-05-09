import os
from api import fetch_aqi_data, fetch_temperature_data, fetch_rainfall_data, fetch_water_data, fetch_crop_yield_data

os.makedirs("data", exist_ok=True)

def display_welcome():
    print("\n" + "="*50)
    print("Welcome to Spring Dale International School")
    print("="*50)
    print("ClimateInsightIndia: Analyze climate data for a better future.")
    print("A project for the International Coding Olympiad.")
    print("Focus: Air Quality, Temperature, Rainfall, Water Resources, Crop Yield.")
    print("="*50 + "\n")

def display_menu():
    print("Select a topic to fetch data:")
    print("1. Air Quality Index (AQI)")
    print("2. Temperature Trends")
    print("3. Monsoon Rainfall Variability")
    print("4. Water Resource Depletion")
    print("5. Crop Yield Impact")
    print("0. Exit")
    print("\nEnter the number (e.g., 1, 2, 3, ...):")

def main():
    display_welcome()
    while True:
        display_menu()
        choice = input("> ").strip()

        try:
            if choice == "0":
                print("Exiting ClimateInsightIndia. Goodbye!")
                break
            elif choice == "1":
                df = fetch_aqi_data()
                df.to_csv('data/aqi_data.csv', index=False)
                print("✅ Data fetched from data.gov.in API and saved to data/aqi_data.csv\n")
            elif choice == "2":
                df = fetch_temperature_data()
                df.to_csv('data/temperature_data.csv', index=False)
                print("✅ Data fetched from data.gov.in API and saved to data/temperature_data.csv\n")
            elif choice == "3":
                df = fetch_rainfall_data()
                df.to_csv('data/rainfall_data.csv', index=False)
                print("✅ Data fetched from data.gov.in API and saved to data/rainfall_data.csv\n")
            elif choice == "4":
                df = fetch_water_data()
                df.to_csv('data/water_data.csv', index=False)
                print("✅ Data fetched from data.gov.in API and saved to data/water_data.csv\n")
            elif choice == "5":
                df = fetch_crop_yield_data()
                df.to_csv('data/crop_yield_data.csv', index=False)
                print("✅ Data fetched from data.gov.in API and saved to data/crop_yield_data.csv\n")
            else:
                print("Invalid choice. Please select a number between 0 and 5.\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == '__main__':
    main()