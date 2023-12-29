airplane_mode = False
from time import sleep

# Wait for 5 seconds
sleep(5)

cellular = True
low_power_mode = False

def get_current_location(precision):
    return "location"

current_location = get_current_location("Best")

def get_maps_url_from(crnt_location):
    return "Location_URL"

maps_url = get_maps_url_from(current_location)

text = f"Hi,\nYour iPhone battery dropped below 10%, prompting concerns about unauthorized use. Here's the location link for your iPhone:\n{maps_url}\nWishing you a good time,\niPhone"

def send_email(txt, recep, show_compose=True):
    # This sends an email
    return None

send_email(text, "my_email@example.com", show_compose=False)

send_sms_to_emergency_contact = True

print("Low Battery: Activating Low Power Mode")
low_power_mode = True
