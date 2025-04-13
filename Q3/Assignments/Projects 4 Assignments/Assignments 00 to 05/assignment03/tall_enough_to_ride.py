# Set the minimum height
minimum_height = 50

# Ask the user for their height
height = input("How tall are you? ")

# Check if they entered something
if height != "":
    # Convert the height to a number
    height = float(height)
    
    # Check if they are tall enough
    if height >= minimum_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
