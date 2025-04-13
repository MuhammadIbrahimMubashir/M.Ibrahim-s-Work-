# Create an empty phonebook
phonebook = {}

# Add some entries
phonebook["Alice"] = "123-4567"
phonebook["Bob"] = "987-6543"
phonebook["Charlie"] = "555-0000"

# Ask user for a name and print the phone number if it exists
name = input("Enter a name: ")

if name in phonebook:
    print("Phone number of", name, "is", phonebook[name])
else:
    print(name, "is not in the phonebook.")
