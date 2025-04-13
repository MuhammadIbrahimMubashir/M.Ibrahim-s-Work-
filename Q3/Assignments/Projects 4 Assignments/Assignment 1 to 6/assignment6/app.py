import time

# Ask the user for number of seconds
seconds = int(input("Enter time in seconds: "))

# Countdown loop
while seconds > 0:
    print("Time left:", seconds, "seconds")
    time.sleep(1)  # Wait for 1 second
    seconds -= 1

print("Time's up! ⏰")
