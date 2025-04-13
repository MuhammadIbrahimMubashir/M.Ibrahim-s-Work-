# Basics
# ===========================================
# 1. Simple Joke Bot
# ===========================================
# Constants
PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes"

def joke_bot():
    user_input = input(PROMPT)
    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)

# Uncomment the below line to run this program
# joke_bot()

# ===========================================
# 2. Double the Number Until It’s 100 or Greater
# ===========================================
def double_until_100():
    curr_value = int(input("Enter a number: "))
    while curr_value < 100:
        curr_value *= 2
        print(curr_value)

# Uncomment the below line to run this program
# double_until_100()

# ===========================================
# 3. Countdown and Liftoff
# ===========================================
def countdown():
    for i in range(10, 0, -1):
        print(i, end=" ")
    print("Liftoff!")

# Uncomment the below line to run this program
# countdown()

# ===========================================
# 4. Guess My Number
# ===========================================
import random

def guess_my_number():
    number = random.randint(0, 99)
    guess = -1
    while guess != number:
        guess = int(input("Enter a guess: "))
        if guess < number:
            print("Your guess is too low")
        elif guess > number:
            print("Your guess is too high")
    print(f"Congrats! The number was: {number}")

# Uncomment the below line to run this program
# guess_my_number()

# ===========================================
# 5. Print 10 Random Numbers (1 to 100)
# ===========================================
def print_random_numbers():
    for _ in range(10):
        print(random.randint(1, 100), end=" ")

# Uncomment the below line to run this program
# print_random_numbers()


# Intermediate
# ===========================================
# 1. High-Low Game
# ===========================================
import random

def high_low_game():
    # Generate numbers
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"Your number: {user_number}")
    guess = input("Is your number higher or lower than the computer's number? (Type 'higher' or 'lower'): ").lower()

    # Check the guess
    if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
        print(f"Correct! The computer's number was {computer_number}. You earn 1 point.")
    else:
        print(f"Incorrect. The computer's number was {computer_number}.")

# Uncomment the below line to run this program
# high_low_game()

# ===========================================
# 2. Weight on Mars Calculation
# ===========================================
def weight_on_mars():
    earth_weight = float(input("Enter your weight on Earth (in kg): "))
    mars_weight = earth_weight * 0.378
    print(f"Your weight on Mars is: {round(mars_weight, 2)} kg.")

# Uncomment the below line to run this program
# weight_on_mars()

# ===========================================
# 3. Fruit List Operations
# ===========================================
def fruit_list_operations():
    # Create the list of fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print(f"Length of fruit_list: {len(fruit_list)}")
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print(f"Updated fruit list: {fruit_list}")

# Uncomment the below line to run this program
# fruit_list_operations()

# ===========================================
# 4. Index Game
# ===========================================
def access_element(lst, index):
    if index < 0 or index >= len(lst):
        return "Index is out of range"
    else:
        return lst[index]

def modify_element(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return "Index is out of range"
    else:
        lst[index] = new_value
        return lst

def slice_list(lst, start, end):
    if start < 0 or end > len(lst) or start > end:
        return "Invalid range"
    else:
        return lst[start:end]

def index_game():
    # Create a list of elements
    sample_list = [10, 'apple', 3.14, 'banana', 42]
    
    print("Select an operation:")
    print("1. Access an element")
    print("2. Modify an element")
    print("3. Slice the list")
    
    operation = int(input("Enter the operation number (1/2/3): "))
    
    if operation == 1:
        index = int(input(f"Enter an index between 0 and {len(sample_list)-1}: "))
        result = access_element(sample_list, index)
        print(f"Element at index {index}: {result}")
    
    elif operation == 2:
        index = int(input(f"Enter an index between 0 and {len(sample_list)-1}: "))
        new_value = input("Enter the new value: ")
        result = modify_element(sample_list, index, new_value)
        print(f"Updated list: {result}")
    
    elif operation == 3:
        start = int(input(f"Enter the start index (0 to {len(sample_list)-1}): "))
        end = int(input(f"Enter the end index (1 to {len(sample_list)}): "))
        result = slice_list(sample_list, start, end)
        print(f"Sliced list: {result}")
    
    else:
        print("Invalid operation choice!")

# Uncomment the below line to run this program
# index_game()
