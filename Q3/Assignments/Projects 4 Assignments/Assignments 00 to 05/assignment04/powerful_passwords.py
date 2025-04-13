import hashlib

# This function turns the password into a hash
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# This function checks if the password is correct
def login(email, password_to_check, stored_logins):
    if email in stored_logins:
        # Hash the password we want to check
        hashed = hash_password(password_to_check)
        # Compare it to the stored hashed password
        return hashed == stored_logins[email]
    return False

# Example usage:
stored_logins = {
    "user@example.com": hash_password("mypassword123")
}

# Test
print(login("user@example.com", "mypassword123", stored_logins))  # True
print(login("user@example.com", "wrongpass", stored_logins))      # False
