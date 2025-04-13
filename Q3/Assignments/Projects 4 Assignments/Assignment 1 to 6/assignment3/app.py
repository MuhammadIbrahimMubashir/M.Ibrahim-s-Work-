def guess_the_number_user():
    print("Welcome to the Guess the Number game!")
    print("Please think of a number between 1 and 100 and I will try to guess it.")
    
    low = 1
    high = 100
    attempts = 0
    
    # The computer will keep guessing until it guesses the correct number
    while True:
        # The computer makes a guess in the middle of the range
        guess = (low + high) // 2
        attempts += 1
        
        # Ask the user if the guess is correct, too high or too low
        print(f"Attempt {attempts}: Is your number {guess}?")
        
        # User provides feedback to the computer's guess
        feedback = input("Enter 'h' if the guess is too high, 'l' if it's too low, or 'c' if the guess is correct: ").lower()
        
        # Feedback conditions
        if feedback == 'h':
            high = guess - 1  # Adjust the high range to be just below the guess
        elif feedback == 'l':
            low = guess + 1  # Adjust the low range to be just above the guess
        elif feedback == 'c':
            print(f"Yay! The computer guessed your number {guess} in {attempts} attempts!")
            break  # Exit the loop since the number was guessed correctly
        else:
            print("Invalid input! Please enter 'h', 'l', or 'c'.")
    
# Run the game
guess_the_number_user()
