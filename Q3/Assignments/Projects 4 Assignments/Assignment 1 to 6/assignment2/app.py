import random

# Guess the Number Game

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    
    # The computer randomly selects a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    # Loop until the player guesses the correct number
    while True:
        # Prompt the player to enter a guess
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        # Increment attempts
        attempts += 1
        
        # Check if the guess is correct, too high, or too low
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congrats! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

# Run the game
guess_the_number()
