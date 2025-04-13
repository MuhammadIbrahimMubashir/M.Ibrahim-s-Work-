# Step 1: Create a function to add three copies to the list
def add_three_copies(message_list, data):
    message_list.append(data)
    message_list.append(data)
    message_list.append(data)

# Step 2: Ask the user for a message
message = input("Enter a message to copy: ")

# Step 3: Create an empty list
messages = []

# Step 4: Print the list before adding copies
print("List before:", messages)

# Step 5: Add three copies of the message to the list
add_three_copies(messages, message)

# Step 6: Print the list after adding copies
print("List after:", messages)
