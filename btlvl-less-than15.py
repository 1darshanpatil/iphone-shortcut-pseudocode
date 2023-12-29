# Prompts the user to enter the battery level
battery_level = int(input("Enter battery level: "))

# Check if battery level is below 15%
if battery_level <= 15:
    print("Unauthorized use suspected. Battery level is falling below the critical level of 15%. Please charge your iPhone!")

    # Activate Unauthorized user suspect mode
    low_power_mode = True
    airplane_mode = False
    wifi = True
    bluetooth = True
    cellular = True


# Check if battery level is below the personal threshold of 35%
# print("Note: Battery level is below the personal threshold of 35%, indicating possible unauthorized use.")
