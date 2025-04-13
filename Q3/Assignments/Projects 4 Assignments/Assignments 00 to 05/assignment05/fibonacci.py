# Constant for the max value
MAX_VALUE = 10000

# Starting two numbers
a = 0
b = 1

# Print until we reach MAX_VALUE
while a < MAX_VALUE:
    print(a, end=" ")
    # Get the next number
    a, b = b, a + b
