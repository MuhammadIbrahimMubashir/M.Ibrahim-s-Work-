# Dictionary of fruits and their prices
fruit_prices = {
    "apple": 10.0,
    "durian": 25.5,
    "jackfruit": 30.0,
    "kiwi": 15.0,
    "rambutan": 12.0,
    "mango": 8.0
}

total = 0

# Loop through each fruit and ask the user how many they want
for fruit in fruit_prices:
    count = int(input(f"How many ({fruit}) do you want?: "))
    total += count * fruit_prices[fruit]

# Print total cost
print("Your total is $" + str(total))
