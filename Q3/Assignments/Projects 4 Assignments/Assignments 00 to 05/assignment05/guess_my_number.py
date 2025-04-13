import random

# Computer chooses a number
secret_number = random.randint(0, 99)

print("I am thinking of a number between 0 and 99...")

# Loop until the user guesses correctly
while True:
    guess = int(input("Enter a guess: "))
    
    if guess < secret_number:
        print("Your guess is too low\n")
    elif guess > secret_number:
        print("Your guess is too high\n")
    else:
        print("Congrats! The number was:", secret_number)
        break
