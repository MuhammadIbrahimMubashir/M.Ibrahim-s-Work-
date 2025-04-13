import math

# Ask for the lengths of the two perpendicular sides
AB = float(input("Enter the length of AB: "))
AC = float(input("Enter the length of AC: "))

# Calculate the hypotenuse (BC)
BC = math.sqrt(AB**2 + AC**2)

# Print the result
print(f"The length of BC (the hypotenuse) is: {BC}")
