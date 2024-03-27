from cryptography.fernet import Fernet  # Import Fernet for encryption
import os  # Import os module for file operations

# Function to generate and write a new encryption key to file
def write_key():
    key = Fernet.generate_key()  # Generate a new encryption key
    with open("key.key", "wb") as key_file:  # Open key file in write binary mode
        key_file.write(key)  # Write the generated key to file

# Function to load the encryption key from file
def load_key():
    try:
        with open("key.key", "rb") as file:  # Open key file in read binary mode
            key = file.read()  # Read the key from file
        return key  # Return the loaded key
    except FileNotFoundError:
        print("Error: key.key file not found.")  # Print error message if key file not found
        return None  # Return None if key file not found

# Load the encryption key
key = load_key()
fer = Fernet(key)  # Initialize Fernet cipher with the loaded key

# Function to view decrypted passwords from file
def view():
    with open('password.txt', 'r') as f:  # Open password file in read mode
        for line in f.readlines():  # Read lines from file
            data = line.rstrip()  # Remove trailing newline character
            user, passwd = data.split("|")  # Split line into username and encrypted password
            print("User:", user, "| Password:", fer.decrypt(passwd.encode()).decode())  # Decrypt and print password

# Function to add new password to file
def add():
    name = input("Account Name: ")  # Prompt user for account name
    passwd = input("Password: ")  # Prompt user for password
    with open('password.txt', 'a') as f:  # Open password file in append mode
        f.write(name + "|" + fer.encrypt(passwd.encode()).decode() + "\n")  # Encrypt and write new password to file

# Main loop for user interaction
while True:
    mode = input("Do you want to add a new password or view existing ones (view, add)? Press 'q' to quit. ").lower()
    if mode == 'q':
        break  # Break the loop if user enters 'q'

    if mode == 'view':
        view()  # Call view function to display passwords
    elif mode == 'add':
        add()  # Call add function to add new password
    else:
        print("Please select a valid option!")  # Print error message for invalid input
