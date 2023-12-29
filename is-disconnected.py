get_battery_level = lambda: int(input("Enter battery level: "))
btlvl = get_battery_level()

if btlvl < 80:
    calculation_result = 80 - btlvl
    text = f"Battery state indicates the current level is {btlvl}, which is {calculation_result}% less than 80%. Maintaining connection to the charger. Initiating low power mode!"
    low_power_mode = True
    print(text)
else:
    text = f"Battery state is currently {btlvl}%. Disabling battery-saving mode."
    low_power_mode = False
    airplane_mode = False
    cellular = True
    vibrate_device = True
    print(text)
