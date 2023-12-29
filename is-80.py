airplane_mode = False
from time import sleep

# Wait for 5 seconds
sleep(5)

get_battery_level = lambda: int(input("Battery Level: "))
battery_level = get_battery_level()

text = f"Your iPhone's current battery level is {battery_level}%"
print(text)

cellular = True
vibrate_device = True
