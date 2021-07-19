import hashlib
from getpass import getpass

# Allow users to login
# Usernames/passwords stored separately to code
# Encrypted passwords
# Able to change passwords once logged in


def read_credentials():
    # User credentials file read
    file = open("users.txt", "r")
    credentials = file.read().splitlines()     # Read the file
    file.close()
    
    usernames = []
    passwords = []
    for i in range(len(credentials)):
        info = credentials[i]
        if i % 2 == 0:
            usernames.append(info)
        else:
            passwords.append(info)

    return usernames, passwords


def encrypt(password_input):
    # Encode and encrypt the entered password
    encoded_password = password_input.encode()
    encrypted_password = hashlib.md5(encoded_password).hexdigest()
    return encrypted_password


def encrypt_and_check(password_input, index):
    encrypted_password = encrypt(password_input)
    if encrypted_password == passwords[index]:
        return True
    else:
        return False


def change_password(indes):
    new_password = input("Enter new password: ")
    encrypted_new = encrypt(new_password)
    # Read the old user credentials
    file = open("users.txt", "r")
    credentials = file.read().splitlines()
    file.close()

    # Calculate the position of the password in the file
    # using the index of the username.
    password_index = 2 * index + 1
    # Replace the password
    credentials[password_index] = encrypted_new

    # Write the new credentials to disk
    file = open("users.txt", "w")
    for credential in credentials:
        file.write(credential + "\n")
    file.close()


users, passwords = read_credentials()

password_attempts = 0
user_input = input("Enter username: ")

while True:
    # Check if the entered username exists in the list of users
    if user_input in users:
        # Find the position (index) of the user
        index = users.index(user_input)

        password_input = getpass("Enter password: ")
        password_attempts = password_attempts + 1

        if encrypt_and_check(password_input, index):
            print("Access granted.")
            
            change_password(index)
            print("Password changed successfully.")
            break

        else:
            attempts_left = 3 - password_attempts
            if attempts_left > 0:
                print("Incorrect password.", attempts_left, "attempts left." )
            else:
                print("Account locked.")
                break

    else:
        print("Incorrect username.")
        user_input = input("Enter username: ")
