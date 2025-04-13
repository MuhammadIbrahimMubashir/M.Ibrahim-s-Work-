import random

# Function to simulate rolling two dice
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

# Roll the dice three times and print the results
for i in range(3):
    die1, die2 = roll_dice()
    print(f"Roll {i+1}: Die 1 = {die1}, Die 2 = {die2}")
