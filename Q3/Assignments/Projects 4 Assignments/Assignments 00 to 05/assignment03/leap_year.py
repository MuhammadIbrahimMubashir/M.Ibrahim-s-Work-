# Ask user for a year
year = int(input("Enter a year: "))

# Check if it's a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("That's a leap year!")
        else:
            print("That's not a leap year.")
    else:
        print("That's a leap year!")
else:
    print("That's not a leap year.")
