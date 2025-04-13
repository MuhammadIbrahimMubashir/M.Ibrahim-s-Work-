import random

# List of words to choose from
words = ["apple", "banana", "grape", "orange", "mango"]

# Pick a random word
word = random.choice(words)

# Create a list with underscores for each letter
hidden = ["_"] * len(word)

# Number of tries
tries = 6

print("Welcome to Hangman!")
print("Guess the word. You have", tries, "tries.")
print(" ".join(hidden))

# Loop until word is guessed or no tries left
while tries > 0 and "_" in hidden:
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = guess
        print("Good job!")
    else:
        tries -= 1
        print("Wrong guess! Tries left:", tries)

    print(" ".join(hidden))

# Check if player won or lost
if "_" not in hidden:
    print("You guessed the word! 🎉")
else:
    print("You lost. The word was:", word)
