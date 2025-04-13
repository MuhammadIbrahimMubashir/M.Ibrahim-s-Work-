# Constant for speed of light (in m/s)
c = 299792458

# Ask for mass (in kilograms)
mass = float(input("Enter kilos of mass: "))

# Calculate energy using the formula
energy = mass * c * c

# Print the result
print(f"\ne = m * C^2...\nm = {mass} kg\nC = {c} m/s\n{energy} joules of energy!")
