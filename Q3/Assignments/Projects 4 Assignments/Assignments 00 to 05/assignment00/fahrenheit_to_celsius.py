# Ask the user for temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius using the formula
celsius = (fahrenheit - 32) * 5.0 / 9.0

# Show the result
print("Temperature:", fahrenheit, "F =", celsius, "C")
