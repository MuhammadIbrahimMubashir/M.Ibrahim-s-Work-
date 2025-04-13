def mad_libs():
    # Collecting user input for different parts of speech
    print("Welcome to Mad Libs! Let's create a fun story.")

    # Asking for user input for each required part of speech
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb (past tense): ")
    noun2 = input("Enter another noun: ")
    adjective2 = input("Enter another adjective: ")
    verb2 = input("Enter a verb: ")
    noun3 = input("Enter a noun: ")
    place = input("Enter a place: ")
    
    # Creating the story with the user input
    story = f"""
    Once upon a time, there was a {adjective1} {noun1}. It loved to {verb1} every day. One day, it saw a {adjective2} {noun2} and decided to {verb2} it. 
    They traveled to {place} and lived happily ever after. The end. But the {noun3} was always remembered as the hero of the story.
    """
    
    # Printing out the story
    print("\nHere's your Mad Libs story:")
    print(story)

# Call the mad_libs function to start the game
mad_libs()
