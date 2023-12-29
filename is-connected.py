get_battery_level = lambda: int(input("Enter battery level: "))
battery_level = get_battery_level()

airplane_mode = False
from time import sleep

# Wait for 5 seconds
sleep(5)

cellular = True

if battery_level >= 80:
    text = f"The current battery level is {battery_level}%, surpassing the recommended 80%. Please disconnect the charging for optimal battery maintenance."
    low_power_mode = False
    print(text)
else:
    text = f"The present battery level is {battery_level}%.\nInitiating low power mode for charging. Ensure a consistent connection during charging and disconnect when it reaches 80%."
    low_power_mode = True
    print(text)

vibrate_device = True
