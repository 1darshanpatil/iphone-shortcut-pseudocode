airplane_mode = False
low_power_mode = False

# Wait for 4 seconds
from time import sleep
sleep(4)

cellular = True
btlvl = int(input("Battery Level: "))
text = f"Current battery level is {btlvl}%. Please connect to the charging."
print(text)

cellular = False
low_power_mode = True

# If the phone is lost, you can at least get your phone's location once Cellular Data is turned on,
# which will then be turned off to save power.