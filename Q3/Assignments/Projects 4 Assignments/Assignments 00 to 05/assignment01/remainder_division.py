# Ask the user for two numbers
num1 = int(input("Please enter an integer to be divided: "))
num2 = int(input("Please enter an integer to divide by: "))

# Perform division and calculate remainder
quotient = num1 // num2
remainder = num1 % num2

# Print the result
print(f"The result of this division is {quotient} with a remainder of {remainder}")
