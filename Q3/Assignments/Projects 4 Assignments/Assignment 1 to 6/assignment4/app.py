import random

def play_game():
    # List of possible choices
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # Prompt the user to enter their choice
        user_choice = input("Enter 'rock', 'paper', or 'scissors' (or 'quit' to exit): ").lower()

        # Check if the user wants to quit the game
        if user_choice == "quit":
            print("Thanks for playing!")
            break
        
        # Validate the user's input
        if user_choice not in choices:
            print("Invalid input! Please enter 'rock', 'paper', or 'scissors'.")
            continue
        
        # The computer randomly selects a choice
        computer_choice = random.choice(choices)

        # Display both choices
        print(f"You chose {user_choice}, and the computer chose {computer_choice}.")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

# Start the game
play_game()
