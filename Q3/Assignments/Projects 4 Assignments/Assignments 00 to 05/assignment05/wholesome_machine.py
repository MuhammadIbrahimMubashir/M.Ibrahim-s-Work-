affirmation = "I am capable of doing anything I put my mind to."

# Keep asking until the user types the affirmation correctly
while True:
    user_input = input("Please type the following affirmation: ")
    if user_input == affirmation:
        print("That's right! :)")
        break
    else:
        print("Hmmm That was not the affirmation. Please try again.")
