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
