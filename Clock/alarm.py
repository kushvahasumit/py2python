# Importing the necessary modules
from playsound import playsound
import time

# ANSI escape codes for clearing the console and moving the cursor
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# Function to set an alarm for a given number of seconds
def alarm(seconds):
    time_elapsed = 0

    # Clearing the console screen
    print(CLEAR)
    
    # Looping until the specified number of seconds is reached
    while time_elapsed < seconds:
        # Waiting for 1 second
        time.sleep(1)
        time_elapsed += 1

        # Calculating time left in minutes and seconds
        time_left = seconds - time_elapsed
        minute_left = time_left // 60
        second_left = time_left % 60

        # Displaying the time left in the format MM:SS
        print(f"{CLEAR_AND_RETURN}{minute_left:02d}:{second_left:02d}")

    # Playing the alarm sound
    playsound("alarm.mp3")

# Calling the alarm function with a 10-second duration
alarm(10)
